#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# ToDoList Formatter
# Copyright © 2014-2016, Chris Warrick.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions, and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions, and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the author of this software nor the names of
#    contributors to this software may be used to endorse or promote
#    products derived from this software without specific prior written
#    consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Pretty-print to-do lists."""

import codecs
import os
import colorama

COLORS = dict(red=colorama.Fore.RED, yellow=colorama.Fore.YELLOW, green=colorama.Fore.GREEN, bold=colorama.Style.BRIGHT, reset=colorama.Style.RESET_ALL)

def print_list(items):
    print(u"{red}[{bold}{yellow}TODO:{reset}{red}]{reset}".format(**COLORS))
    if items:
        boxfs = u"{red}[{bold}{yellow}{number}{reset}{red}]{reset}"
        eboxfs = u"[{number}]"
        for n, i in enumerate(items):
            p = 7 - len(eboxfs.format(number=n + 1))
            print(p * u' ' + u' '.join((boxfs.format(number=n + 1, **COLORS), i)))
    else:
        print(u"    {bold}{green}nothing!{reset}".format(**COLORS))

if __name__ == '__main__':
    try:
        with codecs.open(os.path.expanduser('~/todo'), encoding='utf-8') as fh:
            print_list([i.rstrip() for i in fh.readlines()])
    except IOError:
        print_list([])
