#!/bin/bash
cd svg
for file in *.svg; do
  if [ -e "$file" ]; then
    mv "$file" "$(echo $file | sed 's/\$//g')"
    echo "${file} - "$(echo $file | sed 's/\$//g')""
  fi
done
