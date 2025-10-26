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
        print("Under weight")
    elif (bmi>=18.5 and bmi <=25):
        print("Normal weight")
    else:
        print("overweight")
calculate_bmi(weight=54,height=1.70) #need to convert floating point to string


