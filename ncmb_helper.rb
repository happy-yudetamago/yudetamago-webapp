#!/bin/env ruby
# -*- coding: utf-8 -*-
# File::     ncmb_helper.rb
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

module NcmbHelper
  def find_ncmb_object(ncmb_objects, id)
    return ncmb_objects.find { |o| o[:objectId] == id }
  end

  def ncmb_label(ncmb_objects, id)
    o = find_ncmb_object(ncmb_objects, id)
    o && o[:label]
  end

  def ncmb_existing(ncmb_objects, id)
    o = find_ncmb_object(ncmb_objects, id)
    o && o[:existing]
  end

  def yudetamago_image(ncmb_objects, id)
    case ncmb_existing(ncmb_objects, id)
    when '1'
      return '<img id="status" src="yudetamago_existing.svg" />'
    when '0'
      return '<img id="status" src="yudetamago_not_existing.svg" />'
    else
      return ''
    end
  end

  def create_get_args(id, ids)
    return unless id
    return unless ids
    "id=#{URI.escape(id)}&ids=#{URI.escape(ids)}"
  end
end

# Log
# 24-Sep-2017 yoshitake Created.
