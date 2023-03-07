#!/usr/bin/python3
for i in range(97, 123):
    tableAsciiToAlphabet = chr(i)
    asciiToAlpha = "" + tableAsciiToAlphabet
    if i == 101 or i=113:
        continue
    print("{}".format(asciiToAlpha), end='')
