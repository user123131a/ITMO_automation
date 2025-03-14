num = 3


if num >= 0:
    print('число больше либо равно 0')


else:
    print('число отрицательное')



def task_yes_no(str_1, str_2):
    if str_1 in str_2:
        print('да')
    else:
        print('нет')


task_yes_no(str_1='test', str_2='test1')