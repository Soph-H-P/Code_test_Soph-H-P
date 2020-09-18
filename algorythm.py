# 1: Create a function that, given a list of integers, returns the highest product between three
# of those numbers. For example, given the list [1, 10, 2, 6, 5, 3] the highest product would
# be 10 * 6 * 5 = 300

#Create function that takes list of integers as param
def highest_product(lst):

#ensures list length is > 3
    if (len(lst) < 3):                                         
        return "Please input list with 3 or more integers"
    else:

#sorts list(ascending)
        lst.sort()  

#selects the last 3 items in the list
        last_three = lst[-3:]    

#finds highest product of 3 highest integers
        highest_product = 0
        for num in last_three:
            if highest_product == 0:
                highest_product += num
            else:
                highest_product *= num
    return "Highest Product: "+str(highest_product)






test_list = [1, 10, 2, 6, 5, 3]
small_test_list = [1, 4]


print(highest_product(test_list))
print(highest_product(small_test_list))

