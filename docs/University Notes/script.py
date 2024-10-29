import os
import sys

if (len(sys.argv) == 1):
    print("Usage: <script relative to target dir> <lectures listing file relative to target dir>")
    exit()

filename = sys.argv[1]

myFile = open(filename, "r")
lines = myFile.readlines()


for line in lines:
    parent = line.strip()
    child = "Imgs"
    full_path = os.path.join(parent, child)
    os.makedirs(full_path)
    newfile = open(os.path.join(parent, "Lecture.md"), "x")

myFile.close()
