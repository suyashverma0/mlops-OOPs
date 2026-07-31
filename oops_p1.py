class Chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.loggedin= False
        self.menu()


    def menu(self):
        user_input = input('''welcome to chatbook how would like to proceed?
                           1.press 1 tp signup
                           2. press 2 to signin
                           3. press 3 to massege a friend
                           4. write a any post
                           5. press any other key to exit  :''')
        if user_input=="1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post
        elif user_input=="4":
            self.send_massege()
        else:
            exit()

    def signup(self):
        email = input("enter your email")
        pwd = input("enter your passwprd")
        self.username = email
        self.password = pwd

        print("sign up sucessfully")
        self.menu()

    def signin(self):
        if self.username==""and self.password=="":
            print("please signup in the main menu")
        else:
            uname = input("enter your username")
            pas = input("enter your password")
            if self.username== uname and self.password == pas:
                print("you have signin sucessfully")
                self.loggedin = True
            else:
                print("please input correct credential")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin == True:
            txt = input("enter your message here")

            print(f"following content has been posted ->{txt}")
        else:
            print("first you sign in plaese")
            self.menu()
    def send_massege(self):
        if self.loggedin == True:
            txt = input("enter your massage here ->")
            frnd= input("whome to send the age ->")
            print(f"your massage has been send to {frnd}")
        else:
            print("please input correct credential")
            print("\n")
            self.menu()

obj = Chatbook()