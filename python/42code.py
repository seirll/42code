#!/usr/bin/python2
#coding: utf-8

#    42Code Decrypter
#    Copyright (C) 2011  Association PROLOGIN <http://www.prologin.org>
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

def usage():
    print "Usage: 42code.py <-d|-e> <input> <output>"
    print "    -e, --encrypt: converts the input file to the 42 language;"
    print "    -d, --decrypt: converts the input file from the 42 language."

if __name__ == '__main__':
    if len(arg) != 4:
        usage()

    elif arg[1] == '-d' or arg[1] == '--decrypt':
        with open(arg[2], "r") as inputf:
            for i in inputf.read().split():
                if i != "42":
                    print "[ERROR]", arg[2], "is not in the 42Code format."
                    sys.exit(1)

            content = []
            inputf.seek(0)
            for i in inputf.readlines():
                lenght = len(i.split())
                octet = struct.pack('B', lenght)
                content.append(octet)

        with open(arg[3], "w") as outputf:
            outputf.write("".join(content))

    elif arg[1] == '-e' or arg[1] == '--encrypt':
        content = []
        with open(arg[2], "rb") as inputf:
            while True:
                octet = inputf.read(1)
                if not octet:
                    break
                lenght = struct.unpack('B', octet)[0]
                content.append("42 " * lenght + "\n")

        with open(arg[3], "w") as outputf:
            for line in content:
                outputf.write(line)

    else:
        usage()
