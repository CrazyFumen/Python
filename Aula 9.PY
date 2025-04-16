#coding: utf-8
for fruta in [ "banana", "maçã", "uva" ]:
    print ("Fruta : " + fruta)
    print("------------------------------")

for i in range (0,10): #(Inclui o Zero, NÃO INCLUI O 10)
    print ("i = " + str ( i ))
print("------------------------------")

for i in range(0,10):
    print ('Não realizado!')
    if i == 0:
        break
print ('Realizado!')