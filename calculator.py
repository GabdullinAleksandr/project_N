import math


def main():
    us_input = input('Введите выражение: ')
    list_ = us_input.split('+')
    list_prod = [i.split('*') for i in list_ if '*' in i]
    list_ = [int(i) for i in list_ if '*' not in i]
    for i in list_prod:
        res = list(map(int, i))
        list_.append(math.prod(res))

    return us_input, sum(list_)


res = main()
print(f'{res[0]} = {res[1]}')

