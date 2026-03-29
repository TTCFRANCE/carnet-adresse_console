contacts = {}
while True:

    nom = input("Nom : ")
    tel = input("Téléphone : ")
    email = input("Email : ")
    ville = input("Ville : ")

    contacts[nom] = {
        "téléphone": tel,
        "email": email,
        "ville": ville
    }
    print(f"{nom} a été ajouté au carnet !")
    print("Tapez 'q' pour quitter, appuyez sur Entrée pour ajouter un autre contact ou a pour afficher les contacts.")
    choix = input("Votre choix : ")
    if choix == "q":
        break
    elif choix == "":
        continue
    elif choix == "a":
        for nom, info in contacts.items():
            print("Nom :", nom)
            print("Infos :", info)
            print("-" * 20)
    continue