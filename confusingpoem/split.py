import re

splitter = re.compile(',|，|。|\\.|？|\\?|!|！')
all_lines = ''

while True:
    try:
        line = input()
        all_lines += line
    except:
        break

splitted = splitter.split(all_lines)
need_remove = []
for i in range(len(splitted)):
    if splitted[i] == '':
        need_remove.append(i)

for i in reversed(need_remove):
    del(splitted[i])

open('splitted.txt', 'w').write('\n'.join(splitted))
