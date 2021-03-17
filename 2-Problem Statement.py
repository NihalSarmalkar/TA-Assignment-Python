#creating the Grocery list
import pandas as pd
cart=[]
budget=int(input("Enter Your budget : "))

#adding product to the Grocery List
def add_product(budget):
    flag=0
    name=str(input("Enter product : "))
    quantity=str(input("Enter quantity : "))
    price=int(input("Enter Price : "))
    
    if(budget<price):
        print("Can't Buy the product budget is low !")
        return budget
    
    if name in cart:
        flag=1
        n=cart.index(name)
        cart[n+1]=quantity
        cart[n+2]=price
    
    budget=budget-price
    if flag==0:
        cart.append(name)
        cart.append(quantity)
        cart.append(price)
    
    print("\nAmount left : ",budget)
    print("\n")
    return budget
    
#menu driven code
while(True):
    print(" 1.Add an item\n","2.Exit\n")
    ch=input("Enter the choice : ")
    if(ch=="1"):
        budget=add_product(budget)
    elif(ch=="2"):
        break
    
    
#finding product to purches if any money is left in the budget
temp=[]
for i in range(len(cart)):
    if (i*3)+2 >= len(cart):
        break
    else:
        if cart[((i*3)+2)] <= budget:
            temp.append((i*3)+2)
            
print("Amount left can buy you following : ")
for j in temp:
    print("  ",cart[j-2])
    #printing product names
    
#printing the grocery list in tabular form
print("\n")
print("GROCERY LIST is : ")
print("\n")
temp_list=[]
temp_list1=[]
for i in range(len(cart)):
    if (i*3)+2 >= len(cart):
        break
    else:
        temp_list.append(((i*3)+2))
for j in temp_list:
    temp_list1.append([cart[j-2],cart[j-1],cart[j]])

print(pd.DataFrame(temp_list1,columns=["Product name","Quantity","Price"]))
    