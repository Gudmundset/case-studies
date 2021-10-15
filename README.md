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

## Case 4: vlookup, iferror, if, google forms

Part of the fun of being in a nonprofit is working with other people. We wanted to send out a quick two question survey. This requires unknown soft skills. Because google forms is the only drive product without revision history, somebody was making edits to the form without my knowledge. I had a simple "Name" field, which was changed twice to other people's names. The three options for "Are you returning" were "yes", "no", and "other". "yes" and "no" options were deleted at some point. Instead of wagging fingers, I removed the other collaborators while the survey was getting filled out because we were getting a lot of incorrect responses.

In order to tabulate who was returning, I performed a regex on the contact sheet someone else had filled out, grabbed the emails from the form spreadsheet and did a VLOOKUP for if a member was returning, and their comment.

`=Regexextract(A2,"[A-z0-9\.\_]+@[a-z\.]+")`

`=if(iserror(VLOOKUP(D2, 'Form Responses 1'!B:D, 3, FALSE)), "", VLOOKUP(D2, 'Form Responses 1'!B:D, 3, FALSE))`

This allowed us to have one sheet of everybody's emails, names, if they had a response and what their comment was, and will continue to populate on additional survey responses, no maintenance necessary.

