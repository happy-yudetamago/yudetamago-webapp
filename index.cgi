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


require 'cgi'
require './config'
require './view_base'

class IndexView < ViewBase
  def initialize(ids)
    super(SCRIPT)
    @ids = ids
  end

  SCRIPT = <<SOURCE_EOF
<%= header %>
<body>

<h1><img src="yudetamago_logo.svg" /></h1>

<h2>Happy Yudetamago ID</h2>

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
