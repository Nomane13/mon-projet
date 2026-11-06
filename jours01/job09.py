name="Plapla"
price_unit=3
quantiter_en_stock=30
user=""
alerte=10

user= int(input("Bonjour quel quantiter souhaiteer vous acheter ?"))
quantiter_en_stock=quantiter_en_stock-user

if quantiter_en_stock < alerte :
    print("Alerte Ravitallier le stock")

elif user > quantiter_en_stock:
    print("Produit pas disponible")

    
elif user==0:
    print("Quantite Nulle")
else:
    print("vous avez,encore assez de produit")

print(quantiter_en_stock)
print(price_unit*1.10)
    
