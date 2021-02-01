"""
vards=input(" Kā tevi sauc? ")
print("Labdien, "+vards)

vecums=int(input("Cik tev gadu? "))
#print("Tev ir " +vecums+ " gadi.")
print(f"Tev ir {vecums} gadi.")
print(f"Tavs dzimšanas gads ir {2021-vecums}.")
"""
dzimsGads=2021-vecums
print(f"Tavs dzimšanas gads ir {dzimsGads}.")
gradi=float(input("Cik grādu pēc Celsija skalas? "))
print(f"Pēc Fārenheita skalas tas ir {gradi*9/5+32} grādi.")

platums=float(input("Ievadi platumu: "))
augstums=float(input("Ievadi augstumu: "))
garumu=float(input("Ievadi garumu: "))
print(f"Telpas tilpums ir {platums*augstums*garums}")

print("sveiki")
print('sveiki')
print("I am ging on a run")
print("Sveika, /npasaule!") #drika 2 rindās
print("Sveika, /tpasule")  #drukā ar tabulācijas atkāpi

#String garums-len
print(len("sveiki"))
print(len("Ko tu domā?"))

# {sākums:beigas:solis}
myString = "Sveiki, pasaule"
print(myString)
print(myString[0])