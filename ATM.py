from ast import Return
import pwinput as ps
class ATM ():
    def __init__(self) :
        print("Welcome To ATM ")
        self.name = "Khaled Mohamed"
        self.dob = "12/4/1977"
        self.accountnum = "4570 1548 4772 1449"
        self.account = 1000
                
    def password (self):
            while True :
                x = ps.pwinput(prompt="Enter your new password : ",mask="*")
                if len(x) == 4 :
                    y = ps.pwinput(prompt="Confirm your new password : ",mask="*")
                    if y == x :
                        print("Your password is set successfully ")
                        print(f"Welcome {self.name}")
                        print(f"Your date of birth : {self.dob}")
                        print(f"Your account number : {self.accountnum}")
                        print(f"You have : {self.account} L.E")
                        break
                    else :
                        print("Something went wrong , Wrong entry !!")
                else :
                    print("Sorry your password must consist of four digits !!")
                    
    
    def deposit (self,d) :
        while True :
            if d == "y" :
                c = (int(input("Enter the amount you want to deposit : ")))
                r = c + self.account 
                print(f"Your account after deposit {r}")
                break
            elif d == "n" :
                print("Thank you have a nice day")
                break 
            else :
                
                print("Wrong entry")
                d = input("Please enter y/n , Do you want to deposit to your account ? y/n : ")
                
    def withdraw (self,w):
        while True :
            if w == "y" :
                s = int(input("Enter the amount you want to withdraw : "))
                t = self.account - s
                print("Wait while your transaction is processing ....")
                print(f"Your account now is : {t}")
                break
            elif w == "n" :
                print("Thank you have a nice day")
                print("Return to the main menu")
                break 
            else :
                print("Wrong entry")
                w = input("Please enter y/n , Do you want to withdraw from your account ? y/n : ")

    def transfer (self,p) :
            while True :
                if p == "y" :
                    s5 = (input("Enter the account number you want to transfer : "))
                    while True:
                        if len(s5) == 12:
                            try:
                                a1 = int(input("Enter the amount you want to transfer : "))
                                if a1 <=self.account :
                                    a2 = input(f"Are you sure you want to transfer {a1} L.E to account number {s5} ? y/n : ").lower()
                                    
                                    if a2 == "y" :
                                        print("Wait while your tranaction is processing ...")
                                        print(f"You transfered {a1} L.E succesufully to account number {s5} ")
                                        a3 = self.account - a1
                                        print(f"Your account now is : {a3} .. Thank you for banking with us !!!")
                                        return  
                                    elif a2 == "n" :
                                        print("Return to the main menu")
                                        return
                                    else :
                                        print("Wrong entry")
                            except:
                                print('Wrong Num .. !')
                                    
                            else :
                                print("Sorry your account is insufficient !! ")
                            
                        else :
                            print("Wrong Entry .. You have entered invaild account number")
                        
                elif p == "n":
                    print("Thank you have a nice day")
                    print("Return to the main menu")
                    break
                
                else :
                    print("Wrong entry")
                    p = input("Please enter y/n , Do you want to transfer money ? y/n : ").lower()    
                     
a = ATM()
a.password()
a.deposit(input("Do you want to deposit to your account ? y/n : ").lower())
a.withdraw(input("Do you want to withdraw from your account ? y/n : ").lower())
a.transfer(input("Do you want to transfer money ? y/n : ").lower())
