import re

line = input()
print(re.sub(r'(\b\S+\b)\s+(\b\1\b)', r'\1', line))


