#!/bin/sh

# Check if two arguments are provided
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <arg1> <arg2>"
  exit 1
fi

# Assign arguments to variables
ARG1=$1
ARG2=$2

# Perform some operation (concatenate the arguments)
RESULT="${ARG1} ${ARG2}"

# Output the result
echo "The result of combining your arguments is: ${RESULT}"