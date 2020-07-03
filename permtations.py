import sys
with open(sys.argv[1], 'r') as f:
	contents = f.read()
sep = contents.split(',')
last = sep[-1]
del sep[-1]
sop = last[0:len(last)-1]
sep.append(sop)
# print(sep)
ans= []
for i in 'abcdefghijklmnopqrstuvwxyz':
	for j in sep:
		ans.append(i+j)
print(ans)

