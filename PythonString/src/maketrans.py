#!/usr/bin/python
from string import maketrans
# Required to call maketrans function.
intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)
str1 = "this is string example....wow!!!";
print (str1.translate(trantab));