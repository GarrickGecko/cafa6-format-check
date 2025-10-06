
### CAFA6 Format Checker and Parser

This repository contains Python scripts for checking the format of 
prediction files for CAFA6, and parsing text results from Gene
Ontology (GO) results.

For more information on CAFA  see: https://biofunctionprediction.org/cafa/

Running

For any prediction file:
```bash
python cafa6_format_checker_parser.py filename
```

Where "filename" is the path to the prediction file in .tsv format


CAFA6 format checker will check that the filename is correctly formatted.
GO and text results are parsed into two seperate dataframes, and format
verification is done on both. Parsed .tsv files are written in the active
directory.


Authored by Garrick Hohm. Distributed under GPLv3 license (attached)

