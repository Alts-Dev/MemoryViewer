import sys

memory_value = 0

def translate(value):
    memory_value = memoryview(bytes(value))
    print(memory_value)

translate(15)