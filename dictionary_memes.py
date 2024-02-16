meme_dict = {"doxear":"robar informaci´´on privada de una persona",
            "F":"dar el pesame",
            "xd": "risa descontrolada",
            }

word = input("escribe la palabra que no entiendas (en minúsculas):")

if word in meme_dict.keys():
    print(meme_dict[word])

else:
    print("La palabra no se encuentra en el diccionario")
