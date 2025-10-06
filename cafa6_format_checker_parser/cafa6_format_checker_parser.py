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
import glob
import pandas as pd

from cafa6_go_format_checker import go_checker as go
from cafa6_text_format_checker import text_checker as text
from cafa6_parser import parser as parser

CAFA_VERSION = 6

def cafa6_file_validator(folder_path):
    """ Validates the filenaming of CAFA submissions """
    is_valid = True
    all_is_valid = True
    message = "VALIDATION SUCCESSFUL\n all files meets CAFA6 file naming specifications"
    error_preamble = "\nVALIDATION FAILED"

    if len(sys.argv) < 2:
        print("Usage: python cafa6_format_checker_parser.py <folder_path>")
        sys.exit(1)

    # Find all TSV files in folder
    tsv_files = glob.glob(os.path.join(folder_path, "*.tsv"))
    file_names = [os.path.basename(f) for f in tsv_files]


    if not tsv_files: # If no TSV files found
        is_valid = False
        message = "No TSV files found"

    if is_valid:
        all_dfs = [] # Read each TSV
        for file in tsv_files:
            df = pd.read_csv(file, sep="\t", header=None)
            all_dfs.append(df)

        counter = 0
        for df in all_dfs: # Process each TSV
            filepath = file_names[counter]
            filepath_short = filepath.split("/")[-1]

            counter = counter + 1
            df_text, df_go = parser(df)

            if not df_text.empty:
                df_go = df_go.drop(df_go.columns[-1], axis=1)

            try:
                if df_go.shape[1] != 3 and (not df_go.empty):
                        print(df_go.shape[1])
                        is_valid = False
                        message = "Incorrect number of columns, should be 3"
                elif df_text.shape[1] != 4 and (not df_text.empty):
                        is_valid = False
                        message = "Incorrect number of columns, should be 4"     
                else:
                    if not df_go.empty:
                        is_valid, message = go(df_go, filepath)
                    if not df_text.empty:
                        is_valid, message = text(df_text, filepath)

            except Exception as e:
                is_valid = False
                message = f"Error reading {filepath_short} as a TSV file: {str(e)}"

            if not is_valid:
                print(error_preamble)
                print(message)
                all_is_valid = False
            else:
                print(filepath_short + " was parsed successfully and contains no formatting errors")
                if not df_text.empty:
                    df_text.to_csv('text_' + filepath_short, sep='\t', index=False, header=False)
                if not df_go.empty:
                    df_go.to_csv('go_' + filepath_short, sep='\t', index=False, header=False)
    
    return all_is_valid

def usage():
    print("Usage: cafa6_format_check.py <path to input file>")

if __name__ == "__main__":
    try:
        cafa6_file_validator(sys.argv[1])
    except IndexError:
        usage()