import Lab2.Lab2 as lab2

def test_find_min_max(): 
    imp_list = [10,20,30,40,50]
    result = lab2.calc_min_max_temperature(imp_list)
    assert (result == [10,50])

def test_calc_avg():
    imp_list = [10, 1 , 1 ,1 , 1]
    result = lab2.calc_average_temperature(imp_list)
    assert (result == 2.8)

def test_calc_median_temperature():
    imp_list = [1,2,3,4,5]
    result = lab2.calc_median_temperature(imp_list)
    assert (result == 3)

def test_calc_min_max():
    imp_list = [5,4,3,2,1]
    result = lab2.calc_min_max_temperature(imp_list)
    assert (result == [1,5])

def test_calc_average():
    imp_list = [10,20,30]
    result = lab2.calc_average_temperature(imp_list)
    assert (result == 20)

def test_calc_median_temperature():
    imp_list = [1, 2, 3, 4, 5]
    result = lab2.calc_median_temperature(imp_list)
    assert (result == 3)

