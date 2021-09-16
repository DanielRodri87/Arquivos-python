# dic = {12345:'Daniel' ' 26/05/2005', 43211:'Selles' ' 21/01/1987'}
# dic[43211] = '20/01/1872'
# dic[343454] = 'Nome' ' 00/00/0000'
# for chave, valores, in dic.items():
#     print(chave, valores)
# print(dic.keys())

#################################33

import time
count = 0
while count <= 10:
    time.sleep(1)
    print(count)
    count += 1
    
#import time
for x in range(10):
    time.sleep(1)
    print(x)