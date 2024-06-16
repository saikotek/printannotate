i: int = 1000000000
j: int = 1
f: float = 10123.141592653589793

# number formatting
print(f"i: {i:_}") # i: 1_000_000_000
print(f"f: {f:.2f}") # f: 10123.14
print(f"f: {f:.0f}") # f: 10123
print(f"f: {f:_.2f}") # f: 10_123.14

# text aligning
text = "Hello World"
print(f"{text:_>20}:") # _________Hello World:
print(f"{text:-<20}:") # Hello World---------:
print(f"{text:=^20}:") # ====Hello World=====:

# print operation
print(f"{i + j=}") # i + j=1000000001
print(f"{int(i - f)=}") # int(i - f)=999989876

nums = [1, 2, 3, 4, 5]
print(f"{nums=}") # nums=[1, 2, 3, 4, 5]
print(f"{list(map(lambda x: x * 2, nums))=}") # list(map(lambda x: x * 2, nums))=[2, 4, 6, 8, 10]

def call_me(bool):
    return "I am true" if bool else "I am false"


print(f"{call_me(True)=}") # call_me(True)='I am true'
