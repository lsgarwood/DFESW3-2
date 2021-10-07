#import pdb
#pdb.set_trace()

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x):
            if x % n == 0:
                return False
            return True

returnVar = is_prime(7)
print(returnVar)

#item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
#n = 0

#while n < 5:
#    for i in item_list:
#        print(item_list[i])

#print(item_list[2])