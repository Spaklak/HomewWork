data = open('17-1.txt', 'r')
def chekcer(a,b,c):
    if a < average and b < average:
        return 1
    elif a < average and c < average:
        return 1
    elif c < average and b < average:
        return 1
    else:
        return 0

def chekcer2(a,b,c):
    if str(a)[-1] == str(b)[-1] == '8':
        return 1
    elif str(a)[-1] == str(c)[-1] == '8':
        return 1
    elif str(c)[-1] == str(b)[-1] == '8':
        return 1
    else:
        return 0

spisok = data.read().split()

spisokMain = [int(x) for x in spisok]

average = sum(spisokMain) / len(spisokMain)

count = 0

maxim = -10000

for i in range(0, len(spisokMain) - 2):
    if (chekcer(spisokMain[i], spisokMain[i + 1], spisokMain[i + 2]) == 1) and (chekcer2(spisokMain[i], spisokMain[i + 1], spisokMain[i + 2]) == 1):
        count += 1
        maxim = max(maxim, spisokMain[i] + spisokMain[i+2] + spisokMain[i+1])

print(count, maxim)

data.close()