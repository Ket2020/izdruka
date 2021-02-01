

#string uzdevumi
x=input("Ievadi teikumu:")
print(len("teikums:"))
vards=input("Ievadi vārdu:")
myString=vards
print("vards:"[0])

myString = "Sveiki, pasaule"
print(myString[8])
teikums=input("Ievadi vārdu:")
print(teikums.upper())
teikums=input("Ievadi teikumu:")
print(teikums.lower())
txt="samercēt"
x = txt.replace("s", "p")
print(x)
x = txt.strip()
print("Sveika, pasule!")

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


