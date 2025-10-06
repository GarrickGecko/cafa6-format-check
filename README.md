
## CAFA6 Format Checker and Parser

This repository contains Python scripts for checking the format of 
prediction files for CAFA6, and parsing text results from Gene
Ontology (GO) results.

All scripts are available in the `cafa6_format_checker_parser` folder. Test data is
available in the `test_data` folder.

For more information on CAFA  see: https://biofunctionprediction.org/cafa/

### Running:  
For any prediction folder:
```bash
python cafa6_format_checker_parser.py folder
```
Where "folder" is a directory path which contains one or more `.tsv` files

### Functions:

The `cafa6_format_checker_parser.py` script contains the main wrapper
`cafa6_file_validator`, which searches a given folder for `.tsv` files,
with each file being loaded into a pandas dataframe. For each dataframe, files are
parsed into a `go` and `text` dataframe depending if the string 'Text' is present
in the second column of the data. 
`go` dataframes are verified to be 3 columns, and `text` dataframes to be 4 columns. 

The `cafa6_parser` script contains the `parser` function, which takes a dataframe as
input and outputs two dataframes, one with text entries and one with GO entries.

Next the `cafa6_go_format_checker` script contains the `go_checker` function, which
iterates through each line of the program, calling the format checker `go_prediction_check` 
and the error handler `handle_error` for every line.
the following format checks of each 'go' dataframe are done as listed below: 
- All entries in the 'target' column must contain only numbers and uppercase letters,
with entries being at least 6 characters long
- All entries in the 'go' column must start with the string 'GO:' followed by 5-7 numbers.
- All entries in the 'confidence' column must be numbers within the range (0, 1]

Similarly, the `cafa6_text_format_checker` script contains the `text_checker` function, which
iterates through each line of the program, calling the format checker `text_prediction_check` 
and the error handler `handle_error` for every line.
the following format checks of each 'text' dataframe are done as listed below:
- All entries in the 'target' column must contain only numbers and uppercase letters,
with entries being at least 6 characters long
- All entries in the 'go' column must contain only the string 'Text'
- All entries in the 'confidence' column must be numbers within the range (0, 1]

### Output: 

Parsed dataframes confirmed to be in the correct format are written in the 
active directory as .tsv files. If the formatting for a given file is incorrect, the
appropriate error message is printed to the console. An example error is given below:

```
VALIDATION FAILED  
Error in file2.tsv, line 1, GO prediction: error in first (Target ID) field. EntryID is not valid
```

Authored by Garrick Hohm. Distributed under GPLv3 license (attached)

