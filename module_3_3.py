def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params()
print_params("key", False,34)
print_params(b = 25)
print_params(c=[1,2,3])


values_list = [22,11,95]
values_dict = {"a":22, "b":11, "c":95}
print_params(*values_list)
print_params(**values_dict)

value_list2 = [True,False]
print_params(*value_list2,42)