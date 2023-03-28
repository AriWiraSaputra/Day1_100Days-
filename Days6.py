#Days_4 "What the elif this is?"
#
#18 MARCH 2023


def exercies_1():
    print("SECURE LOGIN")
    username = input("Username >")
    password = input("Password >")
    if username == "Mark" and password == "123456":
        print("welcome Mark!")
    elif username == "Suzanne" and password == "123456":
        print("Hey there Suzanne")
    else:
        print("Go away!")


def exercies_2():
    season = input("What is Your Favorite season?")
    if season == "spring":
        print("Ah! The birds are chirping and flowers blooming")
    elif season == "summer":
        print("The Leaves are Changing and the air is crisp. Enjoy!")
    elif season == "winter":
        print("Stay warm bye the fire and watch the snow fall")
    else:
        print("I don't know that season.plase try again")


def exercies_3():
    Name = input("Enter Your Name: ")
    Password = input("Enter Your Password: ")
    if Name == "Ari" and Password == "12":
        print("Hello", Name, "How Are You?")
    elif Name == "Wira" and Password == "123":
        print("Holla", Name, "How are You?!...")
    elif Name == "Saputra" and Password == "123":
        print("heii Mr", Name, "How are You?!...")
    else:
        print(Name, "Name Or Password is Worng!...")


def call():
    exercies_1()
    exercies_2()
    exercies_3()


call()
