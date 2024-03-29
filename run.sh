#!/bin/bash

# The name of the file to save grades.
filename="data/academic_module_grades.csv"

# Create the file and write the header.
if [ ! -f "$filename" ]; then
  echo "code,name,credits,fheq,grade" > "$filename"
  echo "CSV data file created with a header. It can be found in path: ./"$filename
fi

# Run the main program.
cd code
python main.py
