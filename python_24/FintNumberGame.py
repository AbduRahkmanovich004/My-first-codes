import random as tanlaovchi
print('''==============================\n==--------FintNumberGame---------==\n==============================
Bu oyin sharti oylangan sonni topish!\n================================================
--qaysi sonlar oraligida son topmoqchisiz?--\n================================================''')
a=int(input("Oraliqning boshini kirgazing!:_"))
b=int(input("Oraliqning oxirini  kirgazing!:_"))
while 1:
    son=input('shu oraliqdagi sonni 1 ta son ayting!   [oyindan  chiqish uchun kalit so`z \'exit\'] ')
    if son=='exit':
        break
    else:
        oylangan_son=tanlaovchi.sample(range(a,b+1),1)
        if int(son) in oylangan_son:
            print("You are winer")
        else:
            print("GameOver")
        


