#!/usr/bin/env python


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
import os
from cafa_go_format_checker import cafa_checker as go

CAFA_VERSION = 6

def cafa6_file_validator(filepath):
    """ Validates the filenaming of CAFA submissions """
    is_valid = True
    filepath_short = filepath.split("/")[-1]
    message = "VALIDATION SUCCESSFUL\n{filepath} meets CAFA6 file naming specifications".format(filepath=filepath_short)
    error_preamble = "\nVALIDATION FAILED"

    if  filepath.endswith(".tsv"):
        with open(filepath, "r") as read_handle:
            is_valid, message = go(read_handle, filepath)
    else:
        is_valid = False
        message = "Could not parse {filepath}".format(filepath=filepath_short)
    
    if not is_valid:
        print(error_preamble)
    print(message)

    return is_valid


def usage():
    print("Usage: cafa6_format_check.py <path to input file>")


if __name__ == "__main__":
    try:
        cafa6_file_validator(sys.argv[1])
    except IndexError:
        usage()