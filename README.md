# case-studies
researching best practices

## Case 1: combinations without itertools combinations

Question: How can we preserve order when generating combinations?\
string = 'a/b/c/d'

expected output:\
a\
a/b\
a/b/c\
a/b/c/d\
b\
b/c\
b/c/d\
c\
c/d\
d


Implementation: path-combinations.py\
REPL: https://repl.it/@PhilipLarson/NewAfraidMarkuplanguage

## Case 2: grab very specific version names.

Question: how do I extract part of this string reliably?

The version in this filename can change from numbers to strings, including a period character. The period to the right then becomes an obstacle, as well as the underscore to the left of the capture group we would like:

nuke_11.3v4_93.8.xml

nuke_11.3v4_test.xml

https://repl.it/@PhilipLarson/RuralCelebratedScales

## Case 3: Grab the right email alias.

Question: on an input field where someone can write anything they want, how do I grab the closest email alias from a list?

This is a tough one because as a resource if someone inputs something it shouldn't do many changes if the user didn't intend the changes, you want to return exactly what they intended. When it comes time to make an email out of that for a developer, there are certain assumptions to be made so they know which email to use.

https://repl.it/@PhilipLarson/UnderstatedKnowingPlane
