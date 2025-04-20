from typing import Union

def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b

print(add_numbers(3, 5))
print(add_numbers(3.5, 2.5))

#print(add_numbers("hello", 5))