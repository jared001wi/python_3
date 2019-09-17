contacts = {}
WhereTo = ""
with open("dict.txt") as f:
    bestandsdata = f.read().split('\n')
    for item in bestandsdata:
        if not item == '': 
            woord1, woord2 = item.split("=")
            contacts[woord1] = woord2

def see():
    print("")
    for key in contacts.keys():
        print(key + " : " + contacts[key])
    print("Amount of contacts: " + str(len(contacts.keys())))

    


def new():
    exitnew = False
    correctnew = False
    while exitnew == False:
        print("")
        newkey = input('''
To make a new contact first type in your contacts name.
type here: ''')
        if newkey in contacts:
            print("you already have a contact with that name")
        else:
            exitnew = True
    newvaleu = input('''
Now type in the contacts phone number.
type here: ''')
    correct = input('''
Is this correct? ''' + newkey + " : " + newvaleu + '''
type here: ''')
    while correctnew == False:
        if correct == "yes":
            contacts[newkey] = newvaleu
            print("Alright, the contact has been made")
            correctnew = True

        if correct == "no":
            print("Ok, try again")
            correctnew = True
     
        else:
            print("Please type yes or no")



def delete():
    exitdelete = False
    correctdelete = False
    if (len(contacts) == 0):
        print("You are lonley.")
        exitdelete = True
        correctdelete = True
    while exitdelete == False:
        print("")
        print('Choose a contact you want to delete.')
        for key in contacts.keys():
            print(key)
        deletekey = input("type here: ")
        if deletekey not in contacts.keys():
            print("Please choose a contact.")
        else:
            exitdelete = True
            
    while correctdelete == False:
        correct = input("Are you sure you want to delete " + deletekey + ''' from you contacts?
type here: ''')
        if correct == "yes":
            print("Alright, " + deletekey + ''' is deleted from your contacts.''')
            del contacts[deletekey]
            correctdelete = True
            
        elif correct == "no":
            correctdelete = True
            
        else:
            print("Please type yes or no")

    
def change():
    newname = ""
    exitchange = False
    correctchange = False
    correctchange2 = False
    if (len(contacts) == 0):
        print("You are lonley.")
        exitchange = True
        correctchange = True
        correctchange2 = True
    while exitchange == False:
        print('Choose a contact you want to change.')
        for key in contacts.keys():
            print(key)
        changekey = input("type here: ")
        if changekey not in contacts.keys():
            print("Please choose a contact.")
        else:
            exitchange = True
    while correctchange == False:
        keyorvalue = input('''
Do you want to change this contacts name or phonenumber?
type here: ''')
        if keyorvalue == "name":
            newname = input('''
what do you want to change the name to
type here: ''')
            newnumber = contacts[changekey]
            correctchange = True
        elif keyorvalue == "phonenumber":
            newnumber = input('''
what do you want to change the phonenumber to
type here: ''')
            newname = changekey
            correctchange = True
        else:
            print("please type in \"name\" or \"phonenumber\"")

    while correctchange2 == False:
        print("Is this what you want?")
        print(newname + ":" + newnumber)
        correct = input("type here: ")
        if correct == "yes":
            if keyorvalue == "name":
                del contacts[changekey]
                    
            contacts[newname] = newnumber
            print("alright, your contact has been changed.")
            correctchange2 = True
        if correct == "no":
            correctchange2 = True
        else:
            print("Please type yes or no")

def save():
    f = open("dict.txt","w")
    for key in contacts.keys():
        f.write(key + "=" + contacts[key] + '''
''')
    f.close()
    print("")
    print("Contacts saved")
    print("Goodbye")


while WhereTo != "quit": 
    WhereTo = input('''
If you want to see all your cantacts type "see".
If you want to make a new contact type "new".
If you want to delete a contact type "delete".
If you want to see a phonenumber type "change".
If you want to quit type "quit".
type here: ''')
    if WhereTo == "see":
        see()
    elif WhereTo == "new":
        new()
    elif WhereTo == "delete":
        delete()
    elif WhereTo == "change":
        change()  
    elif WhereTo == "quit":
        save()
    else:
        print("That is not a valid command.")

    
        



