def calculate_bmi(weight, height):
    print("Height ="+ height)
    print("Weight ="+ weight)

calculate_bmi(weight="57",height="1.73")  #using string to append to another string


def calculate_bmi(weight, height):
    print("Height ="+ str(height))
    print("Weight ="+ str(weight))
    bmi = weight/(height*height)
    print("Bmi ="+ str(round(bmi,2)))
    if (bmi<18.5):
        return -1
    elif (bmi>=18.5 and bmi <=25):
        return 0
    else:
        return 1
calculate_bmi(weight=54,height=1.70) #need to convert floating point to string

print(calculate_bmi(weight=54,height=1.70))


