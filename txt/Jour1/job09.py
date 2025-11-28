nom="jupe"
prix_uninitaire=40
inflation=10
quantité_stock=4

for i in range(2):
    #affichage des informtion
    print(nom)
    print("prix:", prix_uninitaire,"€")
    print("stock:", quantité_stock)

    ajout = int(input("ajout du stock:")) # ajout par l'utilisateur le stock
    quantite += ajout
    print("inflation de 10%")
    prix_uninitaire += (inflation / 100)
    print("Mise a jour du produit:")
quantité_stock2=10