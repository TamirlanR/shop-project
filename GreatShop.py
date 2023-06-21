import os 
class Queue(): # Корзина будет работать как куекуе(очередь) first in first out
    def __init__(self):
        self.queue = []
    def enqueue(self, item): # Добавляет элемент в конец куекуе(очереди), аналог пуша(stack.push)
        self.queue.append(item)
    def dequeue(self): # Обобщенная очередь(dequeue) получает первый или последний элемент, как поп(stack.pop)
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    def show(self): # Крч вывод этого всего, с проверкой, ну тут понятно
        if len(self.queue) != 0: # Если что - то тут есть то он выводит
            print(self.queue)
        else: # Если нет то выводит Null (x . x)
            print("It's empty")
            return None
    def clear(self):
        self.queue.clear()
    def num(self): # Просто показывает сколько наших элементов в Корзине
        print(len(self.queue)-1)
cart_name = Queue()     

def accoaunt():
    question = input("[1 - Yes,i want to create an account] \n[2 - No, I have already created my account]:\n: ")
    if question=="1":
        name = input("Enter your name: ")
        subname=name
        file=open(f"{name}.txt","w")
        name="Name "+name+"\n"
        file.write(name)
        password = input("Please Enter password: ")
        password = "Password "+ password +"\n"
        file.write(password)
        file.write("Balance 0\n")
        file.write("status user")

        subfile=open("Accounts.txt","a")
        subfile.write(name)
        subfile.write(password)
        subfile.write(";")
        subfile.close()
        print("succses")
        file.close()
        data={}
        file=open(f"{subname}.txt","r")
        for line in file:
                key,value=line.split()
                data[key] = value
        return data


    elif question=="2":
        name= input("please Enter your name: ")
        password=input("please Enter your password: ")
        data={}
        try:
            file=open(f"{name}.txt")  
        except:
            print("Account not found,try again or create a new one")
            return accoaunt()
        for line in file:
                key,value=line.split()
                data[key] = value
        print(data) 
        if data["Name"]==name and data["Password"]==password:
            print("Welcome:)")
            file.close()
            return data
        else: 
            print("Incorrect password")
            return accoaunt()

data = accoaunt()  

def multiple():
    data={}
    file=open("Admin_file.txt","r")
    for line in file:
        key,value=line.split()
        data[key] = value
    file.close()
    return data
    

def user_account(data):
    name=data["Name"]
    print(f"--------- Hello {name} -----------")
    admin_balance=[]
    admin_cart=[]
    def balans_change(data):
        data["Balance"]=int(input("Enter value of money to put in your account: "))+int(data["Balance"])
        return data

    def shop_cart(cart_bl, cart_name, balance, summary):
        tumbler = True
        while(tumbler):
            balance=int(data["Balance"])
            print(f"[Your balance is:{balance}]")            
            ch_1 = int(input('What do you want to do? \n1)Show your cart \n2)Buy all elements \n3)Delete from your cart: \n: '))
            if ch_1 == 1: #Тута просто показывает все элементы и их общую цену
                print('Your shopping cart: ')
                cart_name.show()
                # admin_cart.append(cart_name.name())
                print('Total price: ')
                summary = (sum((int(cart_bl[i]) for i in range(0, int(len(cart_bl))))))
                print(summary, '\n')

            elif ch_1 == 2: # Проверка на бомжа 2
                if balance < summary:
                    print("You don't have enough funds: ")
                else:
                    print("Congratulations on your purchase: ")
                    balance = balance - summary
                    admin_balance.append(summary)
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~","Your balance know: ", balance,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

                    cart_name.clear()
                    cart_bl.clear()
                    return balance

            elif ch_1 == 3: # Удаляю последний элемент
                cart_name.dequeue()
                cart_bl.pop(0)
                return balance
            else:
                tumbler = False # Корзина магазина
                return balance
    def rewrite(data):
        name=data["Name"] 
        file=open(f"{name}.txt","w") 
        file=open(f"{name}.txt","w")
        for key, value in data.items():
            file.write(str(key)+" "+str(value)+"\n")
        file.close()
        print("(((((Succsesfull)))))")
            

    def main(): # Главное тело кода (Не знаю главное оно или нет но главное покупателя уж точно)
        admin_file=multiple()
        balance = data["Balance"]
        balance = int(balance)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~","Your balance know: ", balance,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        flag = True
        summary = 0

        dict_p = []
        cart_bl = []

        data_shop={}
        while(flag): 

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~","Your balance know: ", balance,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            file = open("Shop.txt","r")
            arr_store=file.read().split(";")
            
            for x in range(len(arr_store)):
                data_shop={}
                arr_store[x]=arr_store[x].split(",")
                for line in arr_store[x]:
                    key,value=line.split()
                    data_shop[key] = value
                dict_p.append(data_shop)
            print("===============================================")    
            for x in range(len(dict_p)): 
                for key, value in dict_p[x].items():
                    print(str(key)+" "+str(value))
                print("===============================================")
                    
            ch = int(input('Do you want to buy something?: \n1)Yes \n2)No \n3)Goto shop cart \n4)add money to your account: '))

            if ch == 1:
                enter = input("\nEnter the name of your product: ")               
                # Тут выберают продукт, он добовляется в корзину, еще тут пишется сколько товара осталось и все такое
                for x in range(len(dict_p)):
                    if dict_p[x]["Name"]==enter:
                        print("\n",dict_p[x])
                        cart_name.enqueue(dict_p[x]["Name"])
                        admin_cart.append(dict_p[x]["Name"])
                        cart_bl.append(int(dict_p[x]['price']))
                        a=x
                # Проверка на бомжа (АХХПХАХАХХАХХАХПХАХП)
                if balance == 0 or balance < int(dict_p[a]['price']):
                    print("**You can't buy anything, your have not enught money**")

            elif ch == 2:
                summer = sum(admin_balance)
                summer=int(admin_file["Balance"])+summer
                slovo=""
                for x in range(len( admin_cart)):
                    slovo+=admin_cart[x]
                items=admin_file["Items"]+ slovo
                adfile=open("Admin_file.txt","w")
                adfile.write(f"Balance {summer}\n")
                adfile.write(f"Items {items}")
                adfile.close()

                flag = False

            elif ch == 3: # Это Корзина магазина
                bal=shop_cart(cart_bl, cart_name, balance, summary)
                data["Balance"]=bal
                rewrite(data)

            elif ch==4:
                name=data["Name"]
                balans_change(data)
                file=open(f"{name}.txt","w")
                for key, value in data.items():
                    file.write(str(key)+" "+str(value)+"\n")
                file.close()
                print("Succsesfull")
               
            else:
                flag = True            
    main()
def admin_account(data):
    ditails=int(input("[1-Delete user account]\n[2-For show ditalysation]: "))
    if ditails==1:
        b=[]
        file=open("Accounts.txt","r")
        a = file.read().split(";")
        for x in range(len(a)):
            data={}
            a[x]=a[x].split("\n")
            print(a[x])
            a[x].remove(a[x][-1])
            for i in a[x]:
                print(i)
                key,value=i.split()
                data[key] = value
            b.append(data)
        print(b)
        b.remove(b[-1])
        name= input("Enter account name: ") 
        for x in range(len(b)):
            if name==b[x]["Name"]:
                os.remove(f"{name}.txt")
                print("accoaunt was succsesfully delelted:)")
            else:
                print("We tring to find account")
        admin_account(data)    
    elif ditails==2:
        adata={}
        file=open("Admin_file.txt","r")
        for line in file:
                key,value=line.split()
                adata[key] = value
        print(adata)
        admin_account(data)
    elif ditails==3:
        print("Good bye)")
    else:
        print("try again")
        admin_account(data)
        
    
if data["status"]=="user":
    user_account(data)
elif data["status"]=="admin":
    admin_account(data)
