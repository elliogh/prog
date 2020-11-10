import re

file = open("example3.txt", encoding="utf8")
p = file.readlines()
unsortedarr = []

for i in p:
    while re.search(r'?=\s*([б-джзй-нп-тф-щ])+([ауыиэяюёе])+([б-джзй-нп-тф-щ]*\2*)*\s*', i) != None:
        match = re.search(r'?=\s*([б-джзй-нп-тф-щ])+([ауыиэяюёе])+([б-джзй-нп-тф-щ]*\2*)*\s*', i)
        unsortedarr.append(match[0])
        i = i.replace(match[0], '')

sortedarr = sorted (unsortedarr, key = len)
print(*sortedarr)
