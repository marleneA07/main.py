#Shopping List App. Make a list of items to buy at the store

grocery_list = []
need_grocery = True

while need_grocery == True:
    groceryAdd = input('Enter item to list: ')
    grocery_list.append(groceryAdd)


    for x in grocery_list:
        print(x)


    stopList = input('   => Type \'stop\' to end list or click \'Enter\' to continue <= ') #change this
    if stopList == "stop":
        need_grocery = False
        print('Your Items are: ', grocery_list)

