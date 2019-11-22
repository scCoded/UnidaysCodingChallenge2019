#unidays coding challenge
import math

AddAnother=True
allItems=(["ItemA", 8.00],["ItemB", 12.00],["ItemC", 4.00],["ItemD", 7.00],["ItemE", 5.00])                 #another list containing items to choose from

class UnidaysDiscountChallenge(object):             
    def __init__(self):
        self.items = list()                                                                     #constructor for new list aka basket
        
    def __len__(self):                                                                          #allows me to check the length of a class list
        return len(self.items)

    def AddToBasket(self, name, price, amount):                                                 #method to add item to class
        if name not in self.items:                                                              #checking if the item is already in list
            self.items.extend([name, price, amount])                                            #if not then it will add as a whole new item to basket
        else:
            changingIndex = self.items.index(name) + 2                                          #if it is then the index corresponding to that items quantity/amount is retrieved
            amountToUpdate = self.items[changingIndex]
            self.items.pop(changingIndex)                                                      #the quantity is updated by removing the previous quantity/amount value then adding the new calculated one.
            self.items.insert(changingIndex, amountToUpdate + amount)
 
    def PricingRules(self,indexI, mult, usualPrice, total):
        numberOfItems = self.items[self.items.index(indexI) + 2]     #1) For numberOfItems/priceOfItems value accessed through adding 2 or 1 to current index...
        priceOfItem = self.items[self.items.index(indexI) + 1]        #2) ...this is because price and quantity values are always a certain number of elements away from name.
        discountMultiple = math.floor(numberOfItems / mult)
        if numberOfItems / mult>= 1 and indexI != "ItemA":
            if indexI == "ItemB" or indexI == "ItemC":  
                numberOfItems -= (discountMultiple * mult)
                total+= ((usualPrice * discountMultiple) + (priceOfItem * numberOfItems))
                return(total)
            elif indexI == "itemD" or indexI == "ItemE":
                total+= ((numberOfItems * priceOfItem) - (priceOfItem * discountMultiple))
                return(total)
        else:
            total+= numberOfItems * priceOfItem
            return(total)          #adds to total here under else statement below if no discount applicable

    def CalculateTotalPrice(self):
        total = 0
        for i in self.items:
            if i=="ItemA":                                #ItemA
                total = self.PricingRules(i, 1, 0, total)
            elif i == "ItemB":                              #ItemB, 2 for £20
                total = self.PricingRules(i, 2, 20, total)                                                                                                                                                                                                                                                                                                                                                         
            elif i == "ItemC":                              #ItemC, 3 for £10
                total = self.PricingRules(i, 3, 10, total)                                                                      
            elif i == "ItemD":                            #ItemD, 2 for 1"
                total=self.PricingRules(i, 2, 0, total)
            elif i == "ItemE":                            #ItemE, 3 for 2"
                total = self.PricingRules(i, 3, 0, total)                                                                                                          

        if total<50:                                 #delivery charge is calculated if total less than 50 pounds then 7 pound charge is added...
            total+=7
            print("£7 Delivery charge applied.")
            return(total)
        else:
            print("Total over £50. No Delivery charge applied.")
            return(total)                                                                                   #if over or equal to 50 pounds then delivery is free of charge!   
        
    def PrintBasket(self):
            print(self.items)

basket = UnidaysDiscountChallenge()                              #initialised basket list that will contain customer items

def AmountValidation(n):                                 #validation to check if the number of items they add in one go is within a reasonable range, lets say upper limit 20.  
    if n >=1 and n <= 20:
        valid=True
        return (valid)    
    else:
        valid=False
        return (valid)

def Main(basket, position):
    try:
        howMany=int(input("How many would you like to add?: "))
        valid = AmountValidation(howMany)                                                           #checking if input is valid for use by calling function.
        if valid==True:
            basket.AddToBasket(allItems[position][0], allItems[position][1], howMany)                              #uses method to add specific items to basket depending on the item value selected.
            basket.PrintBasket()
            return(basket)
        else:
            print("Invalid amount of items : Please try again.")
    except ValueError:
        print("Input error, make sure input is an integer (whole number).")

while AddAnother!= False or len(basket) == 0:                                                                                      #while the customer keeps wanting to add another item and/or the basket is empty the nested code will loop      
    KeepAdding=input("Would you like to add to your basket? Type 'y' or 'yes' to add. Or anything else to exit.").lower()         #user asked if they want to add an item
    if KeepAdding == "yes" or KeepAdding == "y":
        AddAnother=True
        itemValue=input("Which item would you like to add (Enter A, B, C, D or E)?").lower() 
        if itemValue == "a":                                                        #adding itemA
            Main(basket, 0)
        elif itemValue == "b":                                                      #adding itemB
            Main(basket, 1)
        elif itemValue == "c":                                                      #adding itemC
            Main(basket, 2)
        elif itemValue == "d":                                                      #adding itemD
            Main(basket, 3)
        elif itemValue == "e":                                                      #adding itemE
            Main(basket, 4)                                                    
        else:
            print("Input Error : Please try again.")  
    else:
        AddAnother = False                                                                                     #user no longer wants to add items

FinalPrice = basket.CalculateTotalPrice()                                                                     #final price with delivery and discounts applied
print("Total: £", FinalPrice)
