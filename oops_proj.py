class ChatBook:
    def __init__(self):
        self.username=""
        self.password=""
        self.login=False
        self.menu()


    def menu(self):
        user_input=input("""Welcome to chatbook !! how would you like to proceed?
                         1. press 1 to sign up
                         2. press 2 to sign in
                         3. press 3 to write a post
                         4. press 4 to message a friend
                         5. press any other key to exit:  """)
        
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            pass
        elif user_input=="4":
            pass
        else:
            exit()

    def signup(self):
        email=input("Enter your Email id:")
        password=input("setup your password:")
        self.username=email
        self.password=password
        print(f"{self.username} has signed up successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=="" and self.password=="":
            print("Please sign up first by pressing 1 in the main menu")
            self.menu()
        else:
            usrname=input("Enter you email:")
            pasword=input("Enter your password:")
            if self.username==usrname and self.password==pasword:
                print(f"{usrname} have signed in sucessfully")
                self.login=True
            else:
                print("Please enter correct username and password")

        print("\n")
        self.menu()



sam=ChatBook()