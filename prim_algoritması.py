import math

sonsuz = math.inf
düğüm_sayisi = 13

G = [[0, 540 ,560 ,980 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
     [540, 0 ,0 ,0 ,0 ,450 ,0 ,380 ,0 ,0 ,0 ,0 ,0],
     [560, 0 ,0 ,605 ,345 ,320 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
     [980, 0 ,605 ,0 ,0 ,0 ,750 ,0 ,0 ,0 ,0 ,0 ,0],
     [0, 345 ,0 ,0 ,0 ,425 ,240 ,0 ,650 ,0 ,0 ,0 ,0],
     [450, 320 ,0 ,0 ,425 ,0 ,0 ,0 ,0 ,150 ,0 ,780 ,0],
     [0, 0 ,0 ,750 ,240 ,0 ,0 ,0 ,195 ,0 ,0 ,0 ,0],
     [380, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,120 ,360 ,0 ,0],
     [0, 0 ,0 ,0 ,650 ,0 ,195 ,0 ,0 ,0 ,0 ,265 ,160],
     [0, 0 ,0 ,0 ,0 ,150 ,0 ,120 ,0 ,0 ,110 ,260 ,0],
     [0, 0 ,0 ,0 ,0 ,0 ,0 ,360 ,0 ,110 ,0 ,490 ,0],
     [0, 0 ,0 ,0 ,0 ,780 ,0 ,0 ,265 ,260 ,490 ,0 ,420],
     [0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,160 ,0 ,0 ,420 ,0]
     ]
print("Matris: ")

for i in G:
    print(i)
    
print()
print()
s_matrisi = ""
mesafe = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
baslangic = 0
mesafe[0] = True
topla = 0

print("Kullanılan düğümler ve mesafeler: " )
while (baslangic < düğüm_sayisi - 1):
    minimum = sonsuz
    x = 0
    y = 0
    for i in range(düğüm_sayisi):
        if mesafe[i]:
            for j in range(düğüm_sayisi):
                if ((not mesafe[j]) and G[i][j]):  
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    s_matrisi = s_matrisi + str(x) + "-" + str(y) + " " 
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    
    topla = topla + G[x][y]
    mesafe[y] = True
    baslangic += 1

print()
print()

print("S matrisi: ", s_matrisi)
print("Toplam mesafe: ",topla,"metre")
