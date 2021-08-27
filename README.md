# External sort

This repository implements sorting algorithm for big files. It contains of two parts.

## Generating

You can generate a file to be sorted via generate.py executable.
It has three command line arguments.

#### --number (required)
Number of lines in a file.

#### --length (required)
Maximum length of one string in a file.

#### --file (optional)
Name for a newly generated file. Defaults to 'some_file' name.

## Sorting

You can sort a file via sort.py executable. There are two command line arguments.
As a result you will see a new file created in a directory with an original filename plus '_sorted' addition.

#### --file (required)
A file to be sorted.

#### --memory (optional)
Memory limit to be used in a sorting process. Memory is counted in bytes. Defaults to 100.
