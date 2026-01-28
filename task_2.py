class UserData:
    def __init__(self, name, age):
        self.user_name = name
        self.age = age
    def print_info(self):
        print(f"User: {self.user_name}, age: {self.age}")

def process_data(data_list):
    result = []
    for user in data_list:
        if user.age > 18:
            result.append(user.user_name.upper())
    return result