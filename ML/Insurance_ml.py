import pandas as pd
dataPath = r'C:\AAUTOMATION\ML\DATA-SET.xlsx'
# fd = open(dataPath,'r+')
# print(fd.readline())
# for line in fd.readlines():
#     print(line)
fd = pd.read_excel(dataPath)
count = sum(1 for address in fd['ADDRESS'] if address =='Hyderabad')
print(count)

# Using Tensorflow filter Hyderabad 
x = [1, 2, 3]
print('X-memory: ',id(x))
y = x
print('Y-memory: ',id(y))
y.append(4)
try:
    print('Y-memory: ',id(y))
except Exception:
    print(x)