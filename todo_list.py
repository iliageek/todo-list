def welcome():
    print("Welcome To TODO List!\n")
    menu()


def showlist():
    list = open("practice.csv", "r")
    print(list.read())


def writetask():
    list = open("practice.csv", "w")
    list.write(input("Add New Task: "))
    list = open("practice.csv", "r")
    print(list.read())


def checktask():
    list = open("practice.csv", "r")
    print(list.read())
    input("\n\nWhich Task You Want To Check? : ").lower().strip()


def deltask():
    list = open("practice.csv", "r")
    print(list.read())
    input("\n\nWhich Task You Want To Delete? : ").lower().strip()


def restart():
    restrt = input("Do You Want To Do Anything? [Y/N] :").strip().capitalize()
    if restrt == "Y":
        menu()
    elif restrt == "N":
        exit()


def menu():
    menu = input("\nWhat Do You Want To Do?\n\n[1: See My List]\n[2: Add New Task]\n[3: Check My Tasks]\n[4: Delete My Tasks]\n").strip().lower()

    if menu == "1":
        showlist()

    elif menu == "2":
        writetask()

    elif menu == "3":
        checktask()

    elif menu == "4":
        deltask()

welcome()

while "1" == "1" :
    restart()

quit()