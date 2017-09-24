# -*- coding: utf-8 -*-
# File::     view_base.rb
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

require 'singleton'
require 'erb'
require 'forwardable'

class ERBToString
  def initialize(script, binding)
    @erb     = ERB.new(script)
    @binding = binding
  end

  def to_s
    @erb.result(@binding)
  end
end

class ViewBase
  extend Forwardable

  def_delegators(:@erb, :to_s)

  def initialize(script)
    @erb = ERBToString.new(script, binding)
  end

  def header
    <<EOF
Content-Type: text/html; charset=utf-8

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Happy Yudetamago Web.</title>
<link href="css/bootstrap.min.css" rel="stylesheet">
<style type="text/css" media="screen,print">
html{
margin:0;
padding:0;
}

body{
color:#333333;
background-color:#fff;
font-size:81.25%;
font-family:'Hiragino Maru Gothic Pro','Hiragino Kaku Gothic Pro',Meiryo,arial,sans-serif;
line-height:1.5;
}

h1{
margin:2;
padding:0;
background-color:#fff;
position:relative;
font-weight:bold;
border-bottom:double 2px;
}

h2{
margin:2;
padding:0;
background-color:#f90;
position:relative;
font-weight:bold;
border-top:dotted 1px;
border-bottom:dotted 1px;
}


p{
margin:0;
padding:0;
}

pre{
background-color:#eef;
white-space:pre;
white-space:pre-wrap;
word-wrap:break-word;
border:solid 1px;
}

button, input{
line-height:normal;
}

textarea{
overflow:auto;
vertical-align:top;
}

</style>
</head>
EOF
  end

  def footer
    <<EOF
</html>
EOF
  end
end

# Log
# 24-Sep-2017 yoshitake Created.
