# list(map(fonksiyon,iterasyon yapili veri tipi)
def carp(x,y):
    return x*y
print(list(map(carp,[1,2,3],[3,4,5])))
print(list(map(lambda x,y:x*y,[3,4,5],[6,5,7,8]))) # lambda ile ifadesi
liste1=[3,7,8,9,6]
liste2=[3,4,5,2,1,5,4]
liste3=[5,4,3,4,5,3,2,4,5,4]
print(list(map(lambda x,y:x-y,liste1,liste2)))