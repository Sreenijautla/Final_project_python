#Run this code
from admin_user import *
obj=Restaurant()
print('Welcome to Food Ordering App')
print('-'*29)
while True:
    n=int(input('Choose one of the options\n1.Admin\n2.User\n3.Exit\n'))
    if n==1:
        print("Please register your details for admin")
        print('-'*39)
        obj.Register()
        obj.login()
        while True:
            admin=int(input('Enter your preference\n1.Add food items\n2.Edit food items\n3.View all food items\n4.Remove food items\n5.Logout\n'))
            if admin==1:
                obj.add_new_food_items()
                new_item=int(input('Do you want to add more items\n1.Yes\n2.No\n'))
                if new_item==1:
                    obj.add_new_food_items()
                elif new_item==2:
                    pass
                else:
                    print("-----Choose the correct option-----")
            elif admin==2:
                obj.edit_food_items()
            elif admin==3:
                obj.view_all_food_items()
            elif admin==4:
                obj.remove_food_items()
            elif admin==5:
                print('*****Thank you!! Logging out from the admin application*****')
                break
            else:
                print("-----Choose the correct option-----")
    elif n==2:
        print("Please register your details for user")
        print('-'*39)
        obj.Register()
        obj.login()
        while True:
            user=int(input('Enter your preference\n1.Place New Order\n2.Order History\n3.Update Profile\n4.Logout\n'))
            if user==1:
                obj.place_new_order()
                new_order=int(input('Do you want to add more items\n1.Yes\n2.No\n'))
                if new_order==1:
                    obj.place_new_order()
                elif new_order==2:
                    pass
                else:
                    print("-----Choose the correct option-----")
            elif user==2:
                obj.order_history()
            elif user==3:
                obj.update_profile()
            elif user==4:
                print('*****Thank you!! Logging out from the user application*****')
                break
            else:
                print("-----Choose the correct option-----")
    elif n==3:
        print("*****Exiting from the application*****")
        break
    else:
        print("-----Choose the correct option-----")

# Output

# Welcome to Food Ordering App
# -----------------------------
# Choose one of the options    
# 1.Admin
# 2.User
# 3.Exit
# 1
# Please register your details for admin
# ---------------------------------------
# Enter your full name : Sreenija
# Enter your phone number : 7485912635
# Enter your email ID : sree@gmail.com
# Enter your address : Hyderabad
# Enter your username : sree_11
# Enter your password : sree@1807
# *****Registration is successful*****
# Please login to the portal to continue
# ---------------------------------------
# Enter your username : sree_11
# Enter your password : s
# -----Invalid username/password, please try again-----
# Enter your username : sree_11
# Enter your password : sree@1807
# *****Login successful*****
# Enter your preference
# 1.Add food items
# 2.Edit food items
# 3.View all food items
# 4.Remove food items
# 5.Logout
# 1
# Enter the food name you want to add : Manchuria
# Enter the food quantity you want to add: 70 grams
# Enter the price of food (in rupees) : 100
# Enter the discount of food item (in percentage) : 3
# Enter the amount of food stock left in restaurant : 100 grams
# {1: {'Name': 'Manchuria', 'Quantity': '70 grams', 'Price': 100, 'Discount': 3, 'Stock': '100 grams'}}
# *****Items added successfully*****
# Do you want to add more items
# 1.Yes
# 2.No
# 1
# Enter the food name you want to add : Biryani
# Enter the food quantity you want to add: 1 k
# Enter the price of food (in rupees) : 300
# Enter the discount of food item (in percentage) : 10
# Enter the amount of food stock left in restaurant : 7 kgs
# {1: {'Name': 'Manchuria', 'Quantity': '70 grams', 'Price': 100, 'Discount': 3, 'Stock': '100 grams'}, 2: {'Name': 'Biryani', 'Quantity': '1 k', 'Price': 300, 'Discount': 10, 'Stock': '7 kgs'}}
# *****Items added successfully*****
# Enter your preference
# 1.Add food items
# 2.Edit food items
# 3.View all food items
# 4.Remove food items
# 5.Logout
# 1
# Enter the food name you want to add : Noodles
# Enter the food quantity you want to add: 1 cup noodles
# Enter the price of food (in rupees) : 70
# Enter the discount of food item (in percentage) : 3
# Enter the amount of food stock left in restaurant : 7 cups of noodles
# {1: {'Name': 'Manchuria', 'Quantity': '70 grams', 'Price': 100, 'Discount': 3, 'Stock': '100 grams'}, 2: {'Name': 'Biryani', 'Quantity': '1 k', 'Price': 300, 'Discount': 10, 'Stock': '7 kgs'}, 3: {'Name': 'Noodles', 'Quantity': '1 cup noodles', 'Price': 70, 'Discount': 3, 'Stock': '7 cups of noodles'}}
# *****Items added successfully*****
# Do you want to add more items
# 1.Yes
# 2.No
# 1
# Enter the food name you want to add : Dosa
# Enter the food quantity you want to add: 4 dosas
# Enter the price of food (in rupees) : 160
# Enter the discount of food item (in percentage) : 12
# Enter the amount of food stock left in restaurant : 6 dosas
# {1: {'Name': 'Manchuria', 'Quantity': '70 grams', 'Price': 100, 'Discount': 3, 'Stock': '100 grams'}, 2: {'Name': 'Biryani', 'Quantity': '1 k', 'Price': 300, 'Discount': 10, 'Stock': '7 kgs'}, 3: {'Name': 'Noodles', 'Quantity': '1 cup noodles', 'Price': 70, 'Discount': 3, 'Stock': '7 cups of noodles'}, 4: {'Name': 'Dosa', 'Quantity': '4 dosas', 'Price': 160, 'Discount': 12, 'Stock': '6 dosas'}}
# *****Items added successfully*****
# Enter your preference
# 1.Add food items
# 2.Edit food items
# 3.View all food items
# 4.Remove food items
# 5.Logout
# 2
# Enter the food ID you want to edit : 2
# Enter Name you want to update : Chicken Biryani
# Enter Quantity you want to update : 1 kg
# Enter Price you want to update : 200
# Enter Discount you want to update : 10
# Enter Stock you want to update : 7 kgs
# Food items are updated successfully :
#  {1: {'Name': 'Manchuria', 'Quantity': '70 grams', 'Price': 100, 'Discount': 3, 'Stock': '100 grams'}, 2: {'Name': 'Chicken Biryani', 'Quantity': 
# '1 kg', 'Price': '200', 'Discount': '10', 'Stock': '7 kgs'}, 3: {'Name': 'Noodles', 'Quantity': '1 cup noodles', 'Price': 70, 'Discount': 3, 'Stock': '7 cups of noodles'}, 4: {'Name': 'Dosa', 'Quantity': '4 dosas', 'Price': 160, 'Discount': 12, 'Stock': '6 dosas'}}
# Enter your preference
# 1.Add food items
# 2.Edit food items
# 3.View all food items
# 4.Remove food items
# 5.Logout
# 4
# Enter the food ID you want to remove : 4
# Remaining food items available are :
#  {1: {'Name': 'Manchuria', 'Quantity': '70 grams', 'Price': 100, 'Discount': 3, 'Stock': '100 grams'}, 2: {'Name': 'Chicken Biryani', 'Quantity': 
# '1 kg', 'Price': '200', 'Discount': '10', 'Stock': '7 kgs'}, 3: {'Name': 'Noodles', 'Quantity': '1 cup noodles', 'Price': 70, 'Discount': 3, 'Stock': '7 cups of noodles'}}
# Enter your preference
# 1.Add food items
# 2.Edit food items
# 3.View all food items
# 4.Remove food items
# 5.Logout
# 3
# All food items present are : 
# Food ID :  1
# -------------
# Name : Manchuria
# Quantity : 70 grams
# Price : 100
# Discount : 3
# Stock : 100 grams
# Food ID :  2
# -------------
# Name : Chicken Biryani
# Quantity : 1 kg
# Price : 200
# Discount : 10
# Stock : 7 kgs
# Food ID :  3
# -------------
# Name : Noodles
# Quantity : 1 cup noodles
# Price : 70
# Discount : 3
# Stock : 7 cups of noodles
# Enter your preference
# 1.Add food items
# 2.Edit food items
# 3.View all food items
# 4.Remove food items
# 5.Logout
# 5
# *****Thank you!! Logging out from the admin application*****
# Choose one of the options
# 1.Admin
# 2.User
# 3.Exit
# 2
# Please register your details for user
# ---------------------------------------
# Enter your full name : Lakshmi
# Enter your phone number : 8741529635
# Enter your email ID : srilakshmi@gmail.com
# Enter your address : Banglore
# Enter your username : srilakshmi_28
# Enter your password : lakshmi@2828
# *****Registration is successful*****
# Please login to the portal to continue
# ---------------------------------------
# Enter your username : srilakshmi_28
# Enter your password : lakshmi@2828 
# *****Login successful*****
# Enter your preference
# 1.Place New Order
# 2.Order History
# 3.Update Profile
# 4.Logout
# 1
# Choose from the below menu
# ---------------------------
# [{'Name': 'Tandoori Chicken', 'Quantity': '4 pieces', 'Price (in INR)': 240}, {'Name': 'Vegan Burger', 'Quantity': '1 piece', 'Price (in INR)': 320}, {'Name': 'Truffle Cake', 'Quantity': '500 gm', 'Price (in INR)': 900}]
# Select food items you want to order
# 1.Tandoori Chicken
# 2.Vegan Burger
# 3.Truffle Cake
# 2
# {'Name': 'Vegan Burger', 'Quantity': '1 piece', 'Price (in INR)': 320}
# Do you want to confirm the order?
# 1.Yes
# 2.No
# 1
# *****Order is confirmed*****
# Do you want to add more items
# 1.Yes
# 2.No
# 1
# Choose from the below menu
# ---------------------------
# [{'Name': 'Tandoori Chicken', 'Quantity': '4 pieces', 'Price (in INR)': 240}, {'Name': 'Vegan Burger', 'Quantity': '1 piece', 'Price (in INR)': 320}, {'Name': 'Truffle Cake', 'Quantity': '500 gm', 'Price (in INR)': 900}]
# Select food items you want to order
# 1.Tandoori Chicken
# 2.Vegan Burger
# 3.Truffle Cake
# 3
# {'Name': 'Truffle Cake', 'Quantity': '500 gm', 'Price (in INR)': 900}
# Do you want to confirm the order?
# 1.Yes
# 2.No
# 1
# *****Order is confirmed*****
# Enter your preference
# 1.Place New Order
# 2.Order History
# 3.Update Profile
# 4.Logout
# 2
# Your previous orders are :
#  {'Name': 'Vegan Burger', 'Quantity': '1 piece', 'Price (in INR)': 320}
# Your previous orders are :
#  {'Name': 'Truffle Cake', 'Quantity': '500 gm', 'Price (in INR)': 900}
# Enter your preference
# 1.Place New Order
# 2.Order History
# 3.Update Profile
# 4.Logout
# 3
# Enter Full_Name you want to update : Sri Lakshmi Y
# Enter Phone Number you want to update : 8475129635
# Enter Email you want to update : srilakshmi@gmail.com
# Enter Address you want to update : Banglore
# Enter User Name you want to update : srilakshmi_28
# Enter Password you want to update : lakshmi@2828
# Your profile is updated successfully 
#  {'Full_Name': 'Sri Lakshmi Y', 'Phone Number': '8475129635', 'Email': 'srilakshmi@gmail.com', 'Address': 'Banglore', 'User Name': 'srilakshmi_28', 'Password': 'lakshmi@2828'}
# Enter your preference
# 1.Place New Order
# 2.Order History
# 3.Update Profile
# 4.Logout
# 4
# *****Thank you!! Logging out from the user application*****
# Choose one of the options
# 1.Admin
# 2.User
# 3.Exit
# 3
# *****Exiting from the application*****