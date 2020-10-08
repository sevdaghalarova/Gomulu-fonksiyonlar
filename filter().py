# filter(fonksiyon(true,False), iterasyon yapili veri tipi)

def cift(x):
    if x%2==0:
        return True
    else:
        return False

print(list((filter(cift,[3,7,9,4]))))
print(list(filter(lambda x:x%2==0,[1,2,2,3,2])))