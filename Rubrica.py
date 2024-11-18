#Rubrica



import uuid

# Crea una lista di dizionari per i contatti
contacts = [
    {
        "id": uuid.uuid4(),
        "name": "Fabio",
        "surname": "Ronchi",
        "birth_date": "09-09-1994",
        "mobile": "3345466567",
        "mail": "fabioronchi@gmail.com"
    },
    {
        "id": uuid.uuid4(),
        "name": "Carlo",
        "surname": "Deruso",
        "birth_date": "04-07-1989",
        "mobile": "3275644546",
        "mail": "carloderuso@gmail.com"
    },
    {
        "id": uuid.uuid4(),
        "name": "Giada",
        "surname": "Morosi",
        "birth_date": "23-11-1992",
        "mobile": "3209877896",
        "mail": "giadamorosi@gmail.com"
    }
]

# Funzione per inserire nuovi contatti
def contact_insert():
    insert_contact = input("Tap [i] for insert new contact or tap any other button for exit: ")
    if insert_contact.lower() == "i":
        new_contact = {
            "id": uuid.uuid4(),
            "name": input("Name: "),
            "surname": input("Surname: "),
            "birth_date": input("Birth date [dd-mm-yyyy]: "),
            "mobile": input("Mobile: "),
            "mail": input("Mail: ")
        }
        contacts.append(new_contact)
        print("New contact added:", new_contact)
    else:
        print("Exit")

# Funzione per visualizzare i contatti
def view_contacts():
    contact_view = input("Tap [v] for contact's check or tap any other button for exit: ")
    if contact_view.lower() == "v":
        for i, contact in enumerate(contacts):
            print(f"Contact {i + 1}:")
            print(f"  ID: {contact['id']}")
            print(f"  Name: {contact['name']}")
            print(f"  Surname: {contact['surname']}")
            print(f"  Birth Date: {contact['birth_date']}")
            print(f"  Mobile: {contact['mobile']}")
            print(f"  Mail: {contact['mail']}")
            print()
    else:
        print("Exit")

# Funzione per cercare un contatto
def searcher():
    user_input = input("Tap [s] to search a contact, or tap any other button to exit: ")
    if user_input.lower() == "s":
        search = input("Enter the contact name, surname, ID, birth date, mobile, or email to search for: ")
        found = False
        for contact in contacts:
            if (contact["name"].lower() == search.lower() or
                contact["surname"].lower() == search.lower() or
                str(contact["id"]) == search or
                contact["birth_date"] == search or
                contact["mobile"] == search or
                contact["mail"].lower() == search.lower()):
                
                # Stampa i dettagli del contatto trovato
                print("Contact found:")
                print(f"  ID: {contact['id']}")
                print(f"  Name: {contact['name']}")
                print(f"  Surname: {contact['surname']}")
                print(f"  Birth Date: {contact['birth_date']}")
                print(f"  Mobile: {contact['mobile']}")
                print(f"  Mail: {contact['mail']}")
                print()
                found = True
        if not found:
            print(f"{search} not found.")
    else:
        print("Exit")

# Funzione per cancellare un contatto
def delete_contact():
    user_input = input("Tap [d] to delete a contact, or tap any other button to exit: ")
    if user_input.lower() == "d":
        id_insert = input("Insert the id of the contact to remove: ")
        found = False
        for contact in contacts:
            if id_insert == str(contact["id"]):
                contacts.remove(contact)  # Rimuove il contatto dalla lista
                print(f"Contact with ID {id_insert} has been removed.")
                found = True
                break  # Esci dal ciclo dopo aver trovato e rimosso il contatto
        if not found:
            print(f"{id_insert} not found.")
    else:
        print("Exit")


# Chiamate alle funzioni
while True:
    action = input("Choose an action: [i] Insert, [v] View, [s] Search, [d] Delete, [q] Quit: ")
    if action.lower() == 'i':
        contact_insert()
    elif action.lower() == 'v':
        view_contacts()
    elif action.lower() == 's':
        searcher()
    elif action.lower() == "d":
        delete_contact()
    elif action.lower() == 'q':
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")