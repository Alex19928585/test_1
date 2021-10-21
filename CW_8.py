import os
import sys



def foo(*args, **kwargs):
    print(args)
    print(kwargs)


foo([1, 2], {3: 4})
foo(*[1, 2], *{'3': 4})
foo(*[1, 2], **{'3': 4})

for i in range(10):
    print(i)
    if i == 2:
        break
else:
    print("ElSE")

a = 1


def f1(x=10, y=11):
    return x + y

d = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
len1 = 1
