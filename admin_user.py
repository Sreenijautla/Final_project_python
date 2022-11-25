# Admin

import json
class Restaurant:
    def __init__(self):
        self.foods={}
        self_food_id=len(self.foods)+1
        self.user={}
        self.user_id=len(self.user)+1
        self.ordered=[]

    def add_new_food_items(self):
        self.name=input("Enter the food name you want to add : ")
        self.quantity=input("Enter the food quantity you want to add: ")
        self.price=int(input("Enter the price of food (in rupees) : ",))
        self.discount=int(input("Enter the discount of food item (in percentage) : "))
        self.stock=input("Enter the amount of food stock left in restaurant : ")
        self.items={"Name":self.name,"Quantity":self.quantity,"Price":self.price,"Discount":self.discount,"Stock":self.stock}
        self_food_id=len(self.foods)+1
        self.foods[self_food_id]=self.items
        print(self.foods)
        print("*****Items added successfully*****")
        with open("food_items.json",'w') as f:
            json.dump(self.foods,f)

    def edit_food_items(self):
        if len(self.foods)<1:
            print("-----You need to add food items first-----")
        else:
            x=int(input('Enter the food ID you want to edit : '))
            for i in self.foods[x]:
                self.foods[x][i]=input(f"Enter {i} you want to update : ")
            print('Food items are updated successfully :\n',self.foods)
            with open("food_items.json",'w') as f:
                json.dump(self.foods,f)

    def remove_food_items(self):
        if len(self.foods)<1:
            print("-----You need to add food items first-----")
        else:
            y=int(input("Enter the food ID you want to remove : "))
            del self.foods[y]
            print("Remaining food items available are :\n",self.foods)
            with open("food_items.json",'w') as f:
                json.dump(self.foods,f)

    def view_all_food_items(self):
        if len(self.foods)<1:
            print("-----You need to add food items first-----")
        else:
            print('All food items present are : ')
            for i in self.foods:
                print("Food ID : ",i)
                print('-'*13)
                for j in self.foods[i]:
                    print(j,':',self.foods[i][j])
            with open("food_items.json",'w') as f:
                json.dump(self.foods,f)

# User

    def Register(self):
        self.full_name=input("Enter your full name : ")
        self.phone_no=int(input("Enter your phone number : "))
        self.email=input("Enter your email ID : ")
        self.address=input("Enter your address : ")
        self.user_name=input("Enter your username : ")
        self.password=input("Enter your password : ")
        self.details={"Full_Name":self.full_name,"Phone Number":self.phone_no,"Email":self.email,"Address":self.address,"User Name":self.user_name,"Password":self.password}
        self_user_id=len(self.user)+1
        self.user[self_user_id]=self.details
        #print(self.user)
        print("*****Registration is successful*****")

    def login(self):
        print("Please login to the portal to continue")
        print('-'*39)
        while True:
            user_name=input("Enter your username : ")
            password=input("Enter your password : ")
            if user_name==self.user_name and password==self.password:
                print("*****Login successful*****")
                break
            else:
                print("-----Invalid username/password, please try again-----")

    def place_new_order(self):
        print('Choose from the below menu')
        print('-'*27)
        l=[{'Name':'Tandoori Chicken','Quantity':'4 pieces','Price (in INR)':240},
           {'Name':'Vegan Burger','Quantity':'1 piece','Price (in INR)':320},
           {'Name':'Truffle Cake','Quantity':'500 gm','Price (in INR)':900}]
        print(l)
        num=int(input("Select food items you want to order \n1.Tandoori Chicken\n2.Vegan Burger\n3.Truffle Cake\n"))
        if num==1:
            self.ordered.append(l[0])
            print(l[0])
        elif num==2:
            self.ordered.append(l[1])
            print(l[1])
        elif num==3:
            self.ordered.append(l[2])
            print(l[2])
        else:
            print('-----Choose food items from the given menu-----')
        num=int(input("Do you want to confirm the order?\n1.Yes\n2.No\n"))
        if num==1:
            print("*****Order is confirmed*****")
        elif num==2:
            print("-----Order is cancelled-----")
        else:
            print("-----Choose either 1 or 2-----")

    def order_history(self):
        if len(self.ordered)<1:
            print("-----You have not ordered any items yet-----")
        else:
            for i in self.ordered:
                print('Your previous orders are :\n',i)

    def update_profile(self):
        for i in self.details:
            self.details[i]=input(f'Enter {i} you want to update : ')
        print('Your profile is updated successfully \n',self.details)
