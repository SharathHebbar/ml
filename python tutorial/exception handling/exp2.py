

from typing import Type


try:
    raise TypeError('Type error')

except TypeError as e:
    print(e)
