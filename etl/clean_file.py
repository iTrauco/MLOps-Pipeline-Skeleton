#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re

def clean_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Remove brackets, double quotes, and trim surrounding whitespace from each line
    cleaned_lines = [re.sub(r'[\[\]{}"()]', '', line).strip() + ',' for line in lines]

    with open(output_file, 'w') as outfile:
        outfile.write('\n'.join(cleaned_lines))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_file")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    clean_file(input_file, output_file)
    print(f"Cleaned content with commas added to the end of every line. Written to {output_file}")