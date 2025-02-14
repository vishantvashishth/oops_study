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
            self.mypost()
        elif user_input=="4":
            self.messeage()
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

    def mypost(self):
        if self.login==True:
            post=input("Enter you Post here :")
            print(f"Your post has been posted :{post}")
            self.menu()

        else:
            print("Please sign in first to create any post")
            print("/n")
            self.menu()

    def messeage(self):
        if self.login==True:
            friend=input("whom to send the message :")
            message=input("Enter your message :")
            print(f"your friend {friend} has recieved the message")
            self.menu()

        else:
            print("Please signin first")
            print("\n")
            self.menu()




# sam=ChatBook()