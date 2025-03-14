num_float = 3.4


if num_float > 0:
    print("положительное число")
elif num_float == 0:
    print("ноль")
else:
    print('число отрицательное')


def student_rank(years_os_study):
    if years_os_study == 1 or years_os_study == 2 or years_os_study == 3 or years_os_study == 4:
        print("вы - бакалавр")
    elif years_os_study == 5 or years_os_study == 6:
        print("вы - магистр")
    elif years_os_study == 7 or years_os_study == 8 or years_os_study == 9:
        print("вы - аспирант")
    else:
        print("некоректный стаж обучения")

student_rank(3)



number = -25

if number > 100 or number < -100:
    print("-")
else:
    print("+")


