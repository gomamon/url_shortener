import random
import string
import base64
import re


def get_next_alphanum(str_a):
    alphanum = list(str(i) for i in range(10))
    alphanum += list(string.ascii_uppercase)
    alphanum += list(string.ascii_lowercase)

    num_a = list( int(alphanum.index(i)) for i in str_a)
    num_a[len(str_a)-1]+= 1

    cnt = len(str_a)-1
    for i in reversed(num_a):
        carry = cnt - 1
        if i > 61 :
            if cnt>0:
                num_a[carry]+= 1
            num_a[cnt] %= 62
        cnt-=1
    str_a = ''
    for i in num_a:
        str_a += alphanum[i]

    return str_a
