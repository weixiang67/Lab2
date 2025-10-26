def main():
    print("ET0735 (Devops for AIot) - Lab 2 - Introduction to") #indentation matters in python
    display_main_menu()
    num_list = get_user_input()
    print(calc_average_temperature(num_list))
    print(calc_min_max_temperature(num_list))
    print(sort_temperature(num_list))
    asc = sort_temperature(num_list)
    print(calc_median_temperature(asc))

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    x = input()
    temp_list = x
    py_list = temp_list.split(",") #use .split to split the inputs into list
    float_list = []
    for num in py_list:
        float_list.append(float(num)) #loops through the numbers in the list, append as float
    return float_list

def calc_average_temperature(num_list):
    average = sum(num_list)/len(num_list)
    return average
    
def calc_min_max_temperature(num_list):
    minimum = min(num_list)
    maximum = max(num_list)
    return [minimum,maximum]

def sort_temperature(num_list):
    num_list.sort()
    asc = num_list
    return asc

def calc_median_temperature(asc):
    n = len(asc)
    mid = n//2
    if n%2 == 0:
        return ((asc[mid-1]+asc[mid])/2) #rem that array starts from 0
    else:
        return asc[mid]

if __name__ == "__main__": 
    main()






   