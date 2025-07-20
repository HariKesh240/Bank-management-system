import pandas as pd
import pwinput
class Bank:
    def __init__(self):
        self.file='User details.xlsx'
        self.df=pd.read_excel(self.file)
        self.user_index=None

    def verify(self,name,password):
        if 999<password and password<10000:
            user=self.df[(self.df['Name']==name) & (self.df['Pin']==password)]
            if not user.empty:
                self.user_index=user.index[0]
                return True
            return False
        else:
            print("--Invalid Password!!")

    def create_account(self,name,pin):
        if name in self.df['Name'].values:
            return "--Account already exisited--\n--Try Another User Name--"
        if 999<pin and pin<10000:
            new_user={'Name':name,'Pin':pin,'Balance':0}
            self.df=pd.concat([self.df,pd.DataFrame([new_user])],ignore_index=True)
            self.save()
            return "--New Account Created!!--"
        else:
            return "--Invalid Password!!"

    def deposit(self,amount):
        self.df.at[self.user_index,'Balance']+=amount
        self.save()
        return "--Successfully Deposited--"

    def withdraw(self,amount):
        if amount>0:
            if amount<=self.df.at[self.user_index,'Balance']:
                self.df.at[self.user_index,'Balance'] -= amount
                self.save()
                return "--Withdraw Successful--"
            return "--Insufficient Balance--"
        return "--Enter Valid Amount"

    def display(self):
        bal=self.df.at[self.user_index,'Balance']
        return f"₹{bal}"

    def acct_transfer(self,name,amount):
        if name in self.df['Name'].values:
            if amount>0:
                if amount<=self.df.at[self.user_index,'Balance']:
                    target_index=self.df[self.df['Name']==name].index[0]
                    if self.user_index!=target_index:
                        self.df.at[self.user_index,'Balance']-=amount
                        self.df.at[target_index,'Balance']+=amount
                        self.save()
                        return "--Money Transfer successful--"
                    else:
                        return"--You Can't Transfer to Same Acct."
                return "--Insufficient Balance"
            return "--Invalid amount"
        return "--User Name Not found!!"

    def save(self):
        self.df.to_excel(self.file,index=False)
        
# ============================================================================================================================
obj = Bank()
def main():
    attempt=3
    while attempt>0:
        name=input("Enter the Account Holder Name:\n--")
        try:
            password=int(pwinput.pwinput(prompt="Enter your 4 digit pin:\n--",mask='*'))
        except Exception:
            print("Enter Valid Pin!!")
            continue


        if obj.verify(name,password):
            print("--Access Granted!!")
            while True:
                op=int(input("1.Deposit Amt\n2.Withdraw Amt\n3.Check balance\n4.Account Transfer\n5.Exit\n--"))
                if(op==1):
                    try:
                        amt=int(input("Enter the Amount:\n--"))
                        print(obj.deposit(amt))
                    except Exception:
                        print("--Enter Valid amount")
                        continue
                elif(op==2):
                    amt=int(input("Enter the Amount:\n--"))
                    try:
                        print(obj.withdraw(amt))
                    except Exception:
                        print("--Enter Valid amount")
                        continue
                elif(op==3):
                    print(obj.display())
                elif(op==4):
                    name=input("Enter the Acct.holder Name to Transfer:\n--")
                    try:
                        amount=int(input("Enter the Amount:\n--"))
                        print(obj.acct_transfer(name,amount))
                    except Exception:
                        print("--Invalid Input")
                        continue
                elif(op==5):
                    print("--Thank You!! Visit Again<<<<")
                    attempt=0
                    break
                else:
                    print("--Error Occurred!!")
        else:
            attempt=attempt-1
            if attempt==0:
                print("--Sorry 0 Attempts!! Come Again later<<<")
                print("=========================================================================================================")
            else:
                print("-Invalid Access!!\n--Only",attempt,"Attempts left...")

#=============================================================================================================================
while True:
    print("=========================================================================================================")
    print("                                                                                                          People's Bank                                                                                                                     ")
    print("\n1.Login\n2.Create Account\n3.Exit")
    opt=int(input("Enter Any Option to Continue:\n--"))
    if opt==1:
        main()
    elif opt==2:
        print("--Welcome New user")
        name=input("Enter New User Name:\n--")
        try:
            pin=int(input("Enter 4 digit pin:\n--"))
            print(obj.create_account(name,pin))
        except Exception:
            print("EnterValid Pin!!")
            continue
    elif opt==3:
        print("--ATM Closing--")
        print("=========================================================================================================")
        break
    else:
        print("--Invalid Input--")

    
                 
