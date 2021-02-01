#lists jeb saraksti
['Sveika,',100, 3.59,[1,26]]
myLists=[1, 2, 3,100, 3.59,[1,26]]
print(len(myLists)) #saraksta garumu

my_list=["viens","divi" ,"trīs",'četri']
print(my_list[2]) #izdruka elementu ar norādīto indeksu
print(my_list[1:]) #izdruka no norādīta indeksa līdz beigam

#sarakstu apvienošana jeb konkatinācija
cits_list=["pieci","seši"]
print(my_list+cits_list) #izdrukā sarakstu ar abu mainīgu elementiem
jauns_list=my_list+cits_list
print(jauns_list)

#sarakstu mainīšana
jauns_list[0]=1
print(jauns_list)

jauns_list.append("septiņi") #pievieno pēdēju elementu
print(jauns_list)
jauns_list.append(8)
print(jauns_list)

pop_elem=jauns_list.pop(0) #noņem elementu ar noradīto indeksu
print(jauns_list)
print(pop_elem)

#elemetu kārtošana
new_list=["b","a","z","e"]
print(new_list)
num_list=[4,1,8,3]
print(num_list)
new_list.sort()
print(new_list)
#num_list.sort()
print(num_list)
num_list.reverse() #sakārto pretējā secība
print(num_list)
my_list=[1,2,3,100,3.59,]
my_list.sort()
print(my_list)

#sarakts sarakstā(nested)
nested_list=[1,5,[7,2]]
print(nested_list[2][1])

augli=["ābols","banāns","gurķis"]
print(augli[2])
#aizstāt elementu-ģurķis ->apelsīns
augli[2]= "apelsīns"

#pievieno beigās "bumbieris"
augli.append("bumbieris")
print(augli)

#iespraust konkrētā vietā jaunu "citrons"
augli.insert(2,"citrons")
print(augli)
#izņemt no saraksta "banāns"
augli.pop(1)
print(augli)

#izdrukāt pilnā teikumā, cik augļi ir sarakstā
print(f"Sarakstā ir {len(augli)} dažādi augļi.")

