#!/usr/bin/python2
#coding: utf-8
#    42Code Decrypter
#    Copyright (C) 2011  Antoine Pietri (Serialk) for Prologin™
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


import sys
import struct

arg = sys.argv

if arg[1] == '-d' or arg[1] == '--decrypt':
    inputf = open(arg[2], "r")
    outputf = open(arg[3], "w")
    
    tab = inputf.read().split()
    for i in tab:
        if i != "42":
            print "Fatal error : ", arg[2], " is not in the 42Code format."
            break
    
    content = []
    
    for i in inputf.readlines():
        lenght = len(i.split())
        octet = struct.pack('c', lenght)
        content.append(octet)
    
    outputf.write("".join(content))
    
    inputf.close()
    outputf.close()
    
elif arg[1] == '-e' or arg[1] == '--encrypt':
    pass

else:
    print "Usage: 42code.py <operation> <input> <output>"
    print "    -e, --encrypt: converts the input file to the 42 language;"
    print "    -d, --decrypt: converts the input file from the 42 language."
