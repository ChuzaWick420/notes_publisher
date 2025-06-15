import os
import sys

if (len(sys.argv) == 1):
    print("Usage: <script relative to target dir> <lectures listing file relative to target dir>")
    exit()

filename = sys.argv[1]

myFile = open(filename, "r")
lines = myFile.readlines()


for line in lines:
    file = line.strip()
    newfile = open(f"{file}.md", "x")

myFile.close()
