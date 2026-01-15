def get_age_category(age):
    if age >= 0 and age <=150:
        if age < 18:
            return "minor"
        elif 18 < age < 65:
            return "adult"
        else:
            return "senior"
    else:
        return "invalid"

first_val = 10
second_val = 20
third_val = 30

if first_val < second_val < third_val:
    print("Increasing sequence")