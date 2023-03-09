ukam={"ism":"zafarbek",
      "fam":"xudoyberdiyev",
      "yosh":12,
      "kasb":"o'quvchi"
      }
print(f"{ukam['ism'].title()} {ukam['fam'].title()} \
    {ukam['yosh']}ga to'lgan.\
    U {ukam['kasb']}")




means={"ukam":"manti",
       "dadam":"shashlik",
       "onam":"shashlik",
       "opam":"somsa"
       }
ovqat=means.get("ukam","bunda kishi yuq!\n\n\n")
print(f" ukamni sevimli taomi {ovqat.title()}")


python={
         "string":"matn",
         "integer":"butun son",
         "float":"haqiqiy son",
         "if":"agar",
         "else":"yoqsa",
         "elif":"if/else",
         'for':'takrorlanuvchi',
         'list':'ro`yhat',
         'tuple':'ozgarmas',
         'input':'ozlashtiruvchi'
         }



print("1 chi usul 🤔🤔🤔🤔🤔🤔")
key=input('kalit sozni kirgazing').lower()
translat=python.get(key)
if translat==None:
    print("bunday soz mavjud emas")
else:
    print(f'{key} sozi {translat} deb tarjima qilinadi')



print("2 chi usul 🤔🤔🤔🤔🤔🤔")
key=input('kalit sozni kirgazing').lower()
print(python.get(key,"bunday soz mavjud emas"))








    
