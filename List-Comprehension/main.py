
# This is one way

temps = [221, 234, 340, 230]

new_numbers = []

for temp in temps:
    divide = temp / 10
    new_numbers.append(divide)


print(new_numbers)


# using List Comprehension

new_temps = [temp / 10 for temp in temps]

print(new_temps)


# List comprehensionwith If conditional

tempe = [221, 234, 340, -9999, 230]
# the if condition will exclude the -9999 because we don't want to calculate this number for being negative
# Will only divide numbers that are different from -9999
new_tempe = [temper / 10 for temper in tempe if temper != -9999]


print(new_tempe)


# is instance check if the i is integer, if is will return it
def foo(lst):
    return [i for i in lst if isinstance(i, int)]


print(foo([1, 23, 4, 4, 5, "2332", "sdfsdfsd"]))

# This function will only return numbers greater than Zero...


def foo(num):
    return [i for i in num if i > 0]


temperatures = [221, 234, 340, -9999, 230]

temperature = [temp / 10 if temp != -9999 else 0 for temp in temperatures]

print(temperature)


def foo(*args):
    arg = [i.upper() for i in args]
    return sorted(arg)


def find_sum(**kwargs):
    return sum(kwargs.values())


print(find_sum(a=3, b=3, c=3))
