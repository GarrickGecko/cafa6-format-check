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

import pandas as pd
import re
import sys

go_field = re.compile("Text")
target_field = re.compile("^[A-Z0-9]{6,}$")


def text_prediction_check(row):
    """
    A module to check the format of the different records in the CAFA prediction file.
    Accept the current record (inrec). Then returns a boolean value if it is correct or 
    not, and an applicable error message.

    The "correct" and "errmsg" variables then should be passed to the "handle_error" function

    Each current record should consist of a target (enzyme) ID, the word "Text", a confidence
    score within the range (0, 1] with less than or equal to 3 significant figures, and a text
    description specifying the protein function.
    """
    correct = True
    errmsg = None
    
    target_id = row[1]
    go_id = row[2]
    confidence = row[3]

    #print(target_id, go_id, confidence)

    if len(row) != 5:
        correct = False
        print(len(row))
        errmsg = "Text prediction: " + str(len(row)) + " fields detected. Should be 5"
    elif not target_field.match(target_id):
        correct = False
        errmsg = "Text prediction: error in first (Target ID) field. " + str(target_id) + " is not valid"
    elif not go_field.match(go_id):
        correct = False
        errmsg = "Text prediction: error in second 'Text' field. " + str(go_id) + " is not valid"
    elif confidence > 1.0 or confidence <= 0.0:
        correct = False
        errmsg = "Text prediction: error in third (confidence) field, cannot be > 1.0 or <= 0.0. " + str(confidence) + " is not valid"
    #elif count_sig_figs(str(confidence)) > 3:
    #    correct = False
    #    errmsg = "Text prediction: error in third (confidence) field. " + str(confidence) + " is not less than or equal to 3 significant figures"
    return correct, errmsg



def count_sig_figs(number):
    """
    Function to count significant figures. Accepts a number as a string, returns the number
    of significant figures that number contains.
    """
    number_str = str(number)
    number_str = number_str.strip().lstrip("0")
    if "." in number_str:
        number_str = number_str.rstrip("0")
    number_str = number_str.replace(".", "")
    return len(number_str)



def handle_error(correct, errmsg, inrec, line_num, fileName):
    """
    Function builds the error message to incorporate the filename and what line the error was raised on.
    Returns the status of whether the line is correct and the error message if one exists.
    """
    if not correct:
        line = "Error in %s, line %s, " % (fileName, line_num)
        return False,  line + errmsg
    else:
        return True, "Nothing wrong here"
    


def text_checker(df, fileName):
    """
    Main program that: 
    1. Loops through the lines of a file
    2. Calls the Text prediction checker to check each field contains correct info.
    3. calls the error handler "handle_error" to check for error messages/ build the error report.  
    """
    line_num = 0

    for row in df.itertuples(index=True, name="Row"):
        line_num += 1
        correct, errmsg = text_prediction_check(row)
        correct, errmsg = handle_error(correct, errmsg, row, line_num, fileName)

        if not correct:
            return correct, errmsg
        
    return True, "%s, passed the CAFA 6 text prediction format checker" % fileName