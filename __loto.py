#!/usr/bin/env python3.7

import os
from os import listdir, remove, path
from os.path import isfile, join
from random import shuffle

def main():

    mypath = "."
    sounds = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith(('.mp3', '.aif', '.wav'))]
    # sounds = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith(('.wav'))]
    shuffle(sounds)
    for s in sounds:
        print(" ----- " + s)
        os.system("cvlc " + s + " 2>/dev/null")
        continue

if __name__== "__main__":
    main()
