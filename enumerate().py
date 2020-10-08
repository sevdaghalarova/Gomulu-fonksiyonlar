# enumerate() - listedeki elemanlari indexleri ile birlikde gosterir
liste=["elma","armut","kiraz"]
print(list((enumerate(liste))))

for i,j in enumerate(liste):
    print(i,j)