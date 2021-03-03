# Assignment Description
## Situation
Imagine, you work at the IT department of a company. A senior collegue needs more information about the companies PCs.
Therefore, he gives you the log file of the ticket system and asks you to give him more information about:
- The most common errors
- The tickets per user

He wants the output in html-files. To do this, he gives you a csv-to-html-converter.

## Problem Statement
The goal of the final assignment of the course "Using Python to Interact with the Operating System" is:

Turn a given log-file into two html-files

- One file must contain all the types of errors and their occurences
This file must be sorted from most common to least common errors
- The other file must contain the number of info messages and the number of error messages per user
This file must be sorted aphabetically with respect to the name of the user

## Project Structure
In doing so, you have to follow the following steps:
1. Use regular expressions to parse through the log file
2. Use dictionaries to store this data
3. Turn these dictionaries into csv-files
4. Use the given tool to turn the csv-files into html-files.