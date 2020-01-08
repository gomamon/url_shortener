import random
import string
import base64
import re


def shortener(original):
    data_string = original
    data_bytes = data_string.encode("UTF-8")
    encode = base64.b64encode(data_bytes)
    encode = str(encode, "utf-8")
    encode = re.sub('[^A-Za-z0-9]+', '', encode)
    shorten = encode[3:11]
    print(shorten)
    return shorten



