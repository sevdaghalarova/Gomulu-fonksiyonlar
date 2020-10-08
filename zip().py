# zip()  listeleri bir biri ile karsilastirir
liste1=[1,2,3,4,5]
liste2=[2,8,5,4,6]
liste3=["ccv","34","python","java","c+"]
print(list((zip(liste1,liste2,liste3))))

for i in zip(liste1,liste2):
    print(i)