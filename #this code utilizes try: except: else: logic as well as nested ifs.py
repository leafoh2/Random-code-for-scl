#made by @67bf on discord

#This code utilizes try: except: else: logic as well as nested ifs.

try:
    #ask the user to enther the price of the item being bought
    salePrice = input("Enter the price of the item being bought (or press enter for 0)")
    price = float(salePrice or "0")

    if price > 0:
        #ask the user to tner the quantity of the product
        itemQuantity = input("Enter the quantity of the product being bought (enter for 0)")
        quantity = float(itemQuantity or "0")
        if quantity > 0:
            #calculate the unit price
            unitPrice = price / quantity
            print ("Unit price: " + str(unitPrice))
        else:
            print ("Please enter the quantity > 0")
    else:
        print ("Please enther a price > 0")
except ValueError:
    print ("Invalid input! Please enther a numeric value")

else:
    print ()
    print ("Unit price default message")
