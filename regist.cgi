#!/bin/env ruby
# -*- coding: utf-8 -*-
# File::     index.cgi
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

class IndexView < ViewBase
  include NcmbHelper

  def initialize(ids)
    super(SCRIPT)
    @ids = ids
  end

  SCRIPT = <<SOURCE_EOF
<%= header %>
<body>

<h1><img src="img/yudetamago_logo.svg" /></h1>

<nav class="navbar navbar-toggleable-md navbar-dark bg-dark">
  <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <a class="navbar-brand" href="#">Regist Happy Yudetamago ID</a>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="index.html">Home</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="regist.cgi?<%= create_get_args("", @ids) %>">Regist Happy Yudetamago ID</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="list.cgi?<%= create_get_args(@id, @ids) %>">List</a>
      </li>
    </ul>
  </div>
</nav>

<form action="list.cgi" method="get">

<textarea name="ids" class="form-control" rows="10"><%= @ids %></textarea>

<p>
<input type="submit" class="btn btn-default" />
</p>
</form>

<hr />

<p>
@2017 Happy Yudetamago. All rights reserved.
</p>
</body>
<%= footer %>
SOURCE_EOF
end

class IndexMain
  include Singleton

  def main
    @cgi = CGI.new
    ids  = @cgi.params['ids'][0]
    puts IndexView.new(ids)
  end
end

IndexMain.instance.main

# Log
# 24-Sep-2017 yoshitake Created.
