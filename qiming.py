from urllib import request
from itertools import permutations as perm
import re

url = 'https://github.com/okxy/Author-Rank/blob/master/main.md'
try:
    s = request.urlopen(url).read().decode('utf-8')
except:
    pass
ss = re.findall('：.*?<',s)
sss = [i[1:][:-1].split('\u3000') for i in ss]
s3 = [j for i in sss for j in i]
s2 = set(s3)
with open('qiming.txt', 'w', encoding='utf-8') as f:
    n = 0
    for i in perm(s2, 2):
        n += 1
        f.write(''.join(i).capitalize())
        if n%10 == 0:
            f.write('\n\n')
        else:
            f.write(' ')

print('finished.')    
print(n,'names')
