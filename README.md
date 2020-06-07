# SyntheaJSON
Python to Parse Synthea JSON

A python with Tkinter GUI for parsing very large JSON FHIR resources of patient data created with Synthea.  For practice in using jsonpath.
Not at all ready for prime time at this point.  The jsonpath filters don't work at all.

New Approach:
It is much faster to just grep each line for substrings.
So the new file "SyntheaGrep.py" is very fast.
To use it you will be reading all the json patient
data and scanning them all for common substrings.
For example arthritis, copd, tnf, and pneumonia.  Case
Does not matter as they will all be converted to lower
case.  For each string you do a "DataRun". This builds
up a dictionary of integer(converted to string) keys
one for each patient, and a value which is a list.
The list is the string if it was found in a file.
So for a patient (number 2 for example), with two of the
strings, you'd get 2:["copd", "arthritis"] for an example.
There will be as many lists in the dictionary as there
were patient files to parse.  Each patient is just a
sequential number (as a string to be a dictionar key)

You  enter a search word, and hit "DataRun" for as
many "diseases" as you are looking for.  This is
of course lexical so it is not so great for real
research.  You could even enter SNOMED codes, but then
if the data was generated with a value set you would
have to have all the codes that could be in the data.

Once you have run "DataRun" with as many search strings
as you like (usually 4 for most data tool scenarios), 
then you are ready to run the "Count A Cohor" function.
You enter a string with hyphen separated diagnosis strings 
that must exacly match the ones you entered (but in lower case)
of the cohort you want to count.
For example "copd-tnf-arthrits" will count that cohort

