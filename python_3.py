library = {"1":"steen", "2":"papier", "3":"schaar",}
loop = True
change = True
del_ = True

while loop:
    change = True
    del_ = True
    print(library)
    kies = input("typ \"del\" als je een key wilt verwijderen kies \"make\" als je een key met een waarde wilt maken en kies \"change\" als je een waarde van een key wilt veranderen. ")

    if kies == "del":
        while del_:
            key = input("kies een key die je wilt verwijderen. ")
            if key in library:
                del library[key]
                del_ = False
            else:
                input("dat is geen key. ")
        
    elif kies == "make":
        key = input("kies de naam van de key. ")
        waarde = input("kies de waarde. ")
        library[key] = waarde
        
    elif kies == "change":
        while change:
            key = input("kies een key waavan je de waarde wilt veranderen. ")
            if key in library:
                waarde = input("kies de nieuwe waarde. ")
                library[key] = waarde
                change = False
            else:
                input("dat is geen key. ")
            
    else:
        input("kies del, make of change")
