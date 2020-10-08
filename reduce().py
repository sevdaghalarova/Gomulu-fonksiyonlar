# reduce()
# reduce(fonksiyon, iterasyon yapili veri tipi)
from _functools import reduce
def max(x,y):
    if x>y:
        return x
    else:
        return y

print(reduce(max,[1,-2,4,-1]))

print(reduce(lambda x,y:x+y,[1,2,3,4,5]))

# reduce() soldan baslayarak 2-2 islem yapmaya baslar, o islemin sonucunu 3,cu ile devam etdirir
