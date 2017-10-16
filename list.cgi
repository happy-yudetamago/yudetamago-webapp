#!/bin/env ruby
# -*- coding: utf-8 -*-
# File::     list.cgi
# LastEdit:: yoshitake 21-Sep-2017
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
require 'cgi'
require 'ncmb'
require './config'
require './view_base'
require './ncmb_helper'

class ListView < ViewBase
  include NcmbHelper

  def initialize(ids, ncmb_objects)
    super(SCRIPT)
    @ids = ids
    @ncmb_objects = ncmb_objects
  end

  SCRIPT = <<SOURCE_EOF
<%= header %>
<body>

<h1><img src="img/yudetamago_logo.svg" /></h1>

<nav class="navbar navbar-toggleable-md navbar-dark bg-dark">
  <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <a class="navbar-brand" href="#">List</a>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="index.html">Home</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="regist.cgi?<%= create_get_args("", @ids) %>">Regist Happy Yudetamago ID</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="list.cgi?<%= create_get_args("", @ids) %>">List</a>
      </li>
    </ul>
  </div>
</nav>

<table class="table table-responsive table-striped">
<tr>
  <th>状態</th>
  <th></th>
  <th>名前</th>
  <th>変更</th>
</tr>
<% @ids.split(/[\r\n]/).each do |id| id.chomp! %>
<tr>
  <td><%= yudetamago_image(@ncmb_objects, id) %></td>
  <script>
  $(function () {
    $('input[name="existing_<%= id %>"]:radio').change(function() {
      if ( $(this).val() == "1" ) {
        $("#status_<%= id %>").attr("src", "img/yudetamago_existing.svg");
      } else {
        $("#status_<%= id %>").attr("src", "img/yudetamago_not_existing.svg");
      }
    });
  });
  </script>
  <td>
    <div class="btn-group" data-toggle="buttons">
      <label class="btn btn-warning <%= existing_active(@ncmb_objects, id, "1") %>">
        <input type="radio" name="existing_<%= id %>" autocomplete="off" value="1" <%= existing_checked(@ncmb_objects, id, "1") %>>on</input>
      </label>
      <label class="btn btn-warning <%= existing_active(@ncmb_objects, id, "0") %>">
        <input type="radio" name="existing_<%= id %>" autocomplete="off" value="0" <%= existing_checked(@ncmb_objects, id, "0") %>>off</input>
      </label>
    </div>
  </td>
  <td><%= ncmb_label(@ncmb_objects, id) %></td>
  <td><a class="btn btn-default" href="detail.cgi?<%= create_get_args(id, @ids) %>">変更</a></td>
</tr>
<% end %>
</table>

<hr />

<p>
@2017 Happy Yudetamago. All rights reserved.
</p>
</body>
<%= footer %>
SOURCE_EOF
end

class ListMain
  include Singleton

  def main
    @cgi = CGI.new
    ids  = @cgi.params['ids'][0]
    ids  = "" unless ids

    NCMB.initialize(:application_key => APPLICATION_KEY,
                    :client_key => CLIENT_KEY)
    ts = NCMB::DataStore.new('ToggleStocker')
    ncmb_objects = ts.get
    puts ListView.new(ids, ncmb_objects)
  end
end

ListMain.instance.main

# Log
# 21-Sep-2017 yoshitake Created.
