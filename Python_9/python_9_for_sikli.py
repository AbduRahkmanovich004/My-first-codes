#data:29/01/2023
#Criditor:Xudoyberdiyev A.
#Dars7/for sikli



print("-----------------------------------------------1")
mehmonlar=["Ali","Vali","Ochil","Navruz","Mansur","Haydar","Nodir"]
for mehmon in mehmonlar:#: nuqtaga etiborli boling
                        #bu yerda mehmonlar ichigi mehmonni bir martadan hisobla degandir
    print("salomlar qadrdonlar ",mehmon)

    print("hayr ",mehmon)#buning oldidan TAB ni bosib joiy tashlash zarurdir
                         #BUni ustunlari orasida joy tashlasa vazifasi buzulmaydi,joy tashlash mumkin




print("-----------------------------------------------2")

for l in mehmonlar:
    print(f"siz {l}, ertaga oshga taklif qilamiz")




print("-----------------------------------------------3")
   
sonlar=list(range(1,15))
for son in sonlar:
    print(son)
    print(son**2)
    print("\n\n")






print("------------------------------------------------4")

sonlar=list(range(1,11))
son_kvadrati=[]
for son in sonlar:
    son_kvadrati.append(son**2)
print(sonlar)
print(son_kvadrati)






print("------------------------------------------------5")
dostlar=[]
print("5 ta eng yaqin dostingizni kirgazing:")
for m in range(5):
    dostlar.append(input(f"{m+1}-do`stingizni kirgaing:"))
print(dostlar)
                    

