from random import randint
import string
#1


def str_return(string, ind):
    string = ()
    ind = [0, 2, 3]
    return string.append(ind)
print(str_return('крот'))

2 
def list_num(inp_dict: int): #
    inp_dict = []
    result = {inp_dict: inp_dict ** 2}
    return result
    #return result

dict_1 = [2, 8, 9]

print(list_num([2:8, 3:9, 4:16]))
# print(list_num)

#3 
def generate_list(num = 10, step = 1):
    i = 0 
    while i < num:
        yield i
        i += step 

for sym in generate_list():
    print(sym)  

generate_list(10)

#4
# add добавление в множество
# append для списков
# union для объединения множеств

def find_similar(l1, l2):
    return list(set(l1) | set(l2))

print(find_similar([1, 2, 3], [3, 4, 5]))

# # 5

def inside_func(num, p):
    num = input('Введите число: ')
    p = input('Введите индекс числа: ')
    try:
        num = int(p)
        p = int(p)
    except:
        print('Вводить можно только числа!')

    else:
        print(num in p)

inside_func(10, 2)    

