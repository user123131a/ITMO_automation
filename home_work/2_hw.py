def task_1() -> str:
    r: int = 10
    b: float = 3.14
    c: str = "hello"
    d: list = [1, 2, 3]
    e: bool = True
    print(type(r))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))


task_1()



def task_2() -> str:
    a = [1, 2, 3, 5, 8, 13, 21]
    print(a[1:4])


task_2()




def task_3(f: int) -> int:
    return f*f

print(task_3(3))

