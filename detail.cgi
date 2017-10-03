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

  def existing_checked(ncmb_objects, id, status)
    if ncmb_existing(ncmb_objects, id) == status
      return "checked"
    else
      return
    end
  end

  def existing_active(ncmb_objects, id, status)
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

<nav class="navbar navbar-toggleable-md navbar-dark bg-dark">
  <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="index.cgi?<%= create_get_args(@id, @ids) %>">Home</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="list.cgi?<%= create_get_args(@id, @ids) %>">List</a>
      </li>
    </ul>
  </div>
</nav>

<form method="post" action="detail.cgi?<%= create_get_args(@id, @ids) %>">
<input type="hidden" name="method" value="update" />
<input type="hidden" name="id" value="<%= @id %>" />
<input type="hidden" name="ids" value="<%= @ids %>" />

<%= yudetamago_image(@ncmb_objects, @id) %>
<script>
$(function () {
  $('input[name="existing"]:radio').change(function() {
    if ( $(this).val() == "1" ) {
      $("#status").attr("src", "yudetamago_existing.svg");
    } else {
      $("#status").attr("src", "yudetamago_not_existing.svg");
    }
  });
});
</script>

<div class="btn-group" data-toggle="buttons">
  <label class="btn btn-warning <%= existing_active(@ncmb_objects, @id, "1") %>">
    <input type="radio" name="existing" autocomplete="off" value="1" <%= existing_checked(@ncmb_objects, @id, "1") %>>on</input>
  </label>
  <label class="btn btn-warning <%= existing_active(@ncmb_objects, @id, "0") %>">
    <input type="radio" name="existing" autocomplete="off" value="0" <%= existing_checked(@ncmb_objects, @id, "0") %>>off</input>
  </label>
</div>

<textarea name="label" class="form-control" rows="1"><%= ncmb_label(@ncmb_objects, @id) %></textarea>

<hr />

<input type="submit" class="btn btn-default"></input>

</form>

<hr />

<p>
@2017 Happy Yudetamago. All rights reserved.
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
    method   = @cgi.params['method'][0]
    existing = @cgi.params['existing'][0]
    label    = @cgi.params['label'][0]
    id       = @cgi.params['id'][0]
    ids      = @cgi.params['ids'][0]
    ids      = "" unless ids

    NCMB.initialize(:application_key => APPLICATION_KEY,
                    :client_key => CLIENT_KEY)
    ts = NCMB::DataStore.new('ToggleStocker')
    ncmb_objects = ts.get
    if method == "update"
      o = find_ncmb_object(ncmb_objects, id)
      if o
        o.set('existing', existing)
        o.set('label',    label)
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
