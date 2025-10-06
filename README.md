
### CAFA6 Format Checker and Parser

This repository contains Python scripts for checking the format of 
prediction files for CAFA6, and parsing text results from Gene
Ontology (GO) results.

For more information on CAFA  see: https://biofunctionprediction.org/cafa/

Running
For any prediction file:
```bash
python cafa6_format_checker_parser.py folder
```
Where "folder" is a directory path which contains one or more `.tsv` files


The `cafa6_file_validator` function searches a given folder for `.tsv` files,
with each file being loaded into a pandas dataframe. For each dataframe, files are
parsed into a `go` and `text` dataframe depending if the string 'Text' is present
in the second column of the data. The width of each dataframe is verified, with
`go` dataframes being 3 columns and `text` dataframes being 4 columns. 

the following format checks of each 'go' dataframe are done as listed below: 
- All entries in the 'target' column must contain only numbers and uppercase letters,
with entries being at least 6 characters long
- All entries in the 'go' column must start with the string 'GO:' followed by 5-7 numbers.
- All entries in the 'confidence' column must be numbers within the range (0, 1]

the following format checks of each 'text' dataframe are done as listed below:
- All entries in the 'target' column must contain only numbers and uppercase letters,
with entries being at least 6 characters long
- All entries in the 'go' column must contain only the string 'Text'
- All entries in the 'confidence' column must be numbers within the range (0, 1]

Parsed dataframes confirmed to be in the correct format are written in the 
active directory as .tsv files. If the formatting for a given file is incorrect, the
appropriate error message is printed to the console. 


Authored by Garrick Hohm. Distributed under GPLv3 license (attached)

