# # matrix=[[1,0], [0,1]]
# # A=len(matrix)
# # print(A)
# #
# # name_lst = ["Vijay", "Vickey"]
# # tup = ("Item_1", 0.5, name_lst)
# # name_lst.append("Vishal")
# # print(tup)
# #
# # elements = (10, 20, 30, 40, 50, 60, 70, 80)
# # print(elements[2:5], elements[:4], elements[3:100])
# #
# # dict1 = {'age': 35, 'name': 'abc', 'salary': 45000}
# #
# # val = dict1['age']
# #
# # if val in dict1:
# #     print('This is a member of the dictionary')
# # else:
# #     print('This is not a member of the dictionary')
# #
# # freshers = {
# #     'student1': {'name': 'yash', 'salary': 7500},
# #     'student2': {'name': 'heet', 'salary': 8000},
# #     'student3': {'name':'smit', 'salary': 6500}
# # }
# #
# # freshers['student3']['salary'] = 8500
# # print(freshers)
# #
# # bbt = {'Sheldon': 1, 'Leonard': 2}
# # bbt.update({'Penny': 2})
# # print(bbt)
#
# # set1 = {1, 2, 4}
# # set2 = {4, 5, 6}
# # print(len(set1 + set2))
# #
# sets = {3, 4, 5}
# sets.update([1, 2, 3])
# print(sets)
# #
# # a={'Aurn', 'Nikhil', 'Seeta'}
# # a[0]= 'Arun'
# # print(a)
#
#
#
# def unique_count(tup):
#     freq = dict()
#
#     for element in tup:
#         element_key = str(element)
#         if element_key in freq:
#             freq[element_key] += 1
#         else:
#             freq[element_key] = 1
#
#     for element, frequency in freq.items():
#         print(f"{element} : {frequency}")
#
#
# # Example usage:
# my_tuple = (1, 2, 3, [1, 2], 2, 4, 5, [1, 2], 3, 6, 7, 1, 2)
#
#
# unique_count(my_tuple)
# def convert(t):
#     return t*9/5 + 32
#
# print(convert(20))
#
#
# def fun1(name, age):
#     print(name, age)
#
# fun1("Mohit", age=23)
# fun1(age =23, name="Mohit")
# fun1(23, "Mohit")


def Interest(p,c,t=2,r=0.09):
    return p*t*r
Interest(p=1000,c=5)