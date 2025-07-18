import re

s = input()

words = re.findall(r'[a-zA-Z]+', s)

print(len(words))
