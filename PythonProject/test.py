# user_input = input("Provide the string input to be considered for character check :")
# #
# # list_1 = list(user_input)
# # character_count = 0
# #
# # dict_1 ={}
# # for i in user_input:
# #     character_count += 1
# #     print(f"{i} in string is {character_count}")
# #
# #
# #

class Person:
    def __int__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age


class Employee(Person):
    def __int__(self, person_name, person_age):
        self.name = person_name

    def generate_emp_id(self):
        name = self.name
        age = self.age

    # def no_of_employee(self):
    #
    #     employee_id_start = 1
    #
    #     print(f"")
