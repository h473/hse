inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
resultList = []

for i in range(len(lines)):
    resultList.append(lines[i].split())
    resultList[i].pop(2)

resultList.sort()
out = open('output.txt', 'w', encoding='utf-8')
for i in range(len(resultList)):
    print(' '.join(map(str, resultList[i])), sep='', file=out)

out.close()
