data = open('17-1.txt', 'r')

spisok = data.read().split()

spisokMain = [int(x) for x in spisok]

average = sum(spisokMain) / len(spisokMain)

count = 0

maxim = -10000

for i in range(0, len(spisokMain) - 2):
    if ((spisokMain[i] < average) or (spisokMain[i + 1] < average) or (spisokMain[i + 2] < average)) \
        and (spisokMain[i] % 10 == 6 or  spisokMain[i+1] % 10 == 6 or spisokMain[i+2] % 10 == 6):
        count += 1
        maxim = max(maxim, spisokMain[i] + spisokMain[i+2] + spisokMain[i+1])

print(count, maxim)

data.close()