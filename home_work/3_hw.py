def numbers(a, b):
    if a<b:
        print(b)
    elif a>b:
        print(a)
numbers(4, 5)


def check_difference(c, d):
    if abs(c - d) == 135:
        print("yes")
    else:
        print("No")


check_difference(200, 335)



def seasons(s):
    if s == 12 or s in [1, 2]:
        print("зима")
    elif s in [3, 4, 5]:
        print("весна")
    elif s in [6, 7, 8]:
        print("лето")
    elif s in [9, 10, 11]:
        print("осень")
    else:
        print("введите число от 1-12")


seasons(5)


def num(f, g, h):
    if f > 10 and g > 10 and h > 10:
        print("yes")
    else:
        print("no")


num(13, 12, 75)






