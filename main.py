print("Hello World")
print("Artem")
print("hello python")
print("qwerty")
print("vork")

def Fun(a, b):
    c = b
    b = a
    a = c
    return(a, b)


q = Fun(input("Первый аргумент:"), input("Второй аргумент:"))
print("Первый аргумент:", q[0])
print("Второй аргумент:", q[1])
