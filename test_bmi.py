import bmi

def test_bmi_normal_weight():
    result = 1
    result = bmi.calculate_bmi(weight=50, height=1.5)
    assert(result == 0)

def test_bmi_over_weight():
    result = 0
    result = bmi.calculate_bmi(70,1.2)
    assert(result == 1)

def test_bmi_under_weight():
    result = 1
    result = bmi.calculate_bmi(10,1.2)
    assert(result == -1)