# case-studies
researching best practices

Case 1: combinations without itertools

Question:\ 
s = 'a/b/c/d'\

for t in [s.split("/", i)[-1] for i in range(s.count("/")+1)]:\
    for x in [t.rsplit("/", j)[0] for j in range(t.count("/"), -1, -1)]:\
        print x\

a/
a/b/
a/b/c/
a/b/c/d/
b/
b/c/
b/c/d/
c/
c/d/
d/


Implementation: path-combinations.py
