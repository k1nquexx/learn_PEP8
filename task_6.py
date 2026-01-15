x = 1 + 2 * 3 - 4 / 5
list_of_numbs = [1, 2, 3, 4, 5]
char_coordinate = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

def calc_sum_squares(x = 0, y = 0):
    return x ** 2 + y ** 2

calc_result = calc_sum_squares(2, 3)
if calc_result > 10 and calc_result < 20:
    print("Result in range")