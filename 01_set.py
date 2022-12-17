

set_countries = {"col", "mex", "bol"}
print(set_countries)
print(type(set_countries))


set_numbers = {1, 2, 34, 45}
print(set_numbers)

set_types = {1,"hola", True, 45}
print(set_types)

set_from_string = set("hola")
print(set_from_string)


set_from_tuples = set(("abc", "cbc", "as"))
print(set_from_tuples)

numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)

unique_numbers = list(set_numbers)
print(unique_numbers)
