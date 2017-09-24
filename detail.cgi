#!/bin/env ruby
# -*- coding: utf-8 -*-
# File::     detail.cgi
# LastEdit:: yoshitake 24-Sep-2017
#
# Copyright 2017 yoshitake
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR
# ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH
# THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

require './bootstrap'
require 'uri'
require 'cgi'
require 'ncmb'
require './config'
require './view_base'
require './ncmb_helper'

class DetailView < ViewBase
  include NcmbHelper

  def initialize(id, ids, ncmb_objects)
    super(SCRIPT)
    @id  = id
    @ids = ids
    @ncmb_objects = ncmb_objects
  end

  def select_status_checked(ncmb_objects, id, status)
    if ncmb_existing(ncmb_objects, id) == status
      return "checked"
    else
      return
    end
  end

  def select_status_active(ncmb_objects, id, status)
    if ncmb_existing(ncmb_objects, id) == status
      return "active"
    else
      return
    end
  end

  SCRIPT = <<SOURCE_EOF
<%= header %>
<body>

<h1><img src="yudetamago_logo.svg" /></h1>

<form method="post" action="detail.cgi?<%= create_get_args(@id, @ids) %>">
<input type="hidden" name="method" value="update" />
<input type="hidden" name="id" value="<%= @id %>" />
<input type="hidden" name="ids" value="<%= @ids %>" />
<h2>状態</h2>

<%= yudetamago_image(@ncmb_objects, @id) %>
<script>
$(function () {
  $('input[name="select_status"]:radio').change(function() {
    if ( $(this).val() == "1" ) {
      $("#status").attr("src", "yudetamago_existing.svg");
    } else {
      $("#status").attr("src", "yudetamago_not_existing.svg");
    }
  });
});
</script>

<div class="btn-group" data-toggle="buttons">
  <label class="btn btn-warning <%= select_status_active(@ncmb_objects, @id, "1") %>">
    <input type="radio" name="select_status" autocomplete="off" value="1" <%= select_status_checked(@ncmb_objects, @id, "1") %>>on</input>
  </label>
  <label class="btn btn-warning <%= select_status_active(@ncmb_objects, @id, "0") %>">
    <input type="radio" name="select_status" autocomplete="off" value="0" <%= select_status_checked(@ncmb_objects, @id, "0") %>>off</input>
  </label>
</div>

<h2>名前</h2>

<textarea name="name" rows="1" cols="20"><%= ncmb_label(@ncmb_objects, @id) %></textarea>

<hr />

<input type="submit" class="btn btn-default"></input>

</form>

<hr />

<p>
@2017 yoshitake. All rights reserved.
</p>
</body>
<%= footer %>
SOURCE_EOF
end

class DetailMain
  include Singleton
  include NcmbHelper

  def main
    @cgi = CGI.new
    method        = @cgi.params['method'][0]
    select_status = @cgi.params['select_status'][0]
    name          = @cgi.params['name'][0]
    id            = @cgi.params['id'][0]
    ids           = @cgi.params['ids'][0]
    ids           = "" unless ids

    NCMB.initialize(:application_key => APPLICATION_KEY,
                    :client_key => CLIENT_KEY)
    ts = NCMB::DataStore.new('ToggleStocker')
    ncmb_objects = ts.get
    if method == "update"
      o = find_ncmb_object(ncmb_objects, id)
      if o
        o.set('existing', select_status)
        o.set('label',    name)
        o.update
        ncmb_objects = ts.get
      end
    end
    puts DetailView.new(id, ids, ncmb_objects)
  end
end

DetailMain.instance.main

# Log
# 24-Sep-2017 yoshitake Created.
