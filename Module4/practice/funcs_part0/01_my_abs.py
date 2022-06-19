def my_abs(...):
    ...
    return ...


print(my_abs(-5))
print(my_abs(5))
print(my_abs(0))


def my_abs(n):
    if n < 0:
        return -n
    return n

print(my_abs(-19))
print(my_abs(-11115))
print(my_abs(-0.25))
