
#Regular expressions

text = "The agent's phone is 408-555-1234. Call soon!"
print('phone' in text)

import re

pattern = 'phone'
print(re.search(pattern,text))


pattern2 = 'NOT IN TEXT'
print(re.search(pattern2,text))

match = re.search(pattern,text)
print(match.span())
print(match.start())
print(match.end())

#gives only first match
text2 = 'my phone once, my phone twice'
match = re.search('phone', text)
print(match)
print(match.span())

#all matches

matches = re.findall('phone',text2)         # findall returns just back list of the strings themselves
print(matches)
print(len(matches))


for match in re.finditer('phone',text2):
    print(match.span())


for match in re.finditer('phone',text2):
    print(match.group(0))
    captured_grp = match.groups()


print(captured_grp)





