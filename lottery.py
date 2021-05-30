import random
def menu():
    given_set = get_number()
    lottery_set = get_lottry_number()
    result = given_set.intersection(lottery_set)
    print ("The given match {}, you won ${} ".format(result, 100** len(result)))

def get_number():
     num_csv = input("enter 6 values, separated by comma:")
     num_str = num_csv.split(",")
     num_set = {int(number) for number in num_str}
     return num_set

def get_lottry_number():
    values = set()
    while (len(values)<6):
        values.add(random.randint(1,20))
    return values 

menu()
     
  
