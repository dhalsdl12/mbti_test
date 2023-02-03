# readline_test.py
f = open("mbti.txt", 'r', encoding="utf-8")
check = ''
for i in range(48):
    line = f.readline()
    if i % 3 == 0:
        tmp = line.split(' ')
        check = tmp[0]
        continue
    tmp = line.split(',')
    tmp2 = []
    for t in tmp:
        t = t.strip()
        tmp2.append(t)
    print(tmp2)
f.close()