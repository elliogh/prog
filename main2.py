import re

file = open("Hamlet.txt", encoding="utf8")
doc = file.readlines()

for i in doc:
    match = re.search(r'(?<=[.?!])\s\w+(\s\w+){,4}\?|\A\w+(\s\w+){,4}\?', i)
    if match:
        print(match[0])