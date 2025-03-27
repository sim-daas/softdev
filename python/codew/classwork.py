def is_armstrong(n):
    if not isinstance(n, int) or n < 100 or n >= 1000:
        return False
    sum_cubes = sum(int(d) ** 3 for d in str(n))
    return sum_cubes == n


def ms_to_hours(ms):
    return ms // 3600000


def find_p(s):
    for i in range(len(s)):
        if s[i] == 'P':
            return i
    return -1

def first_last(s):
    if len(s) < 2:
        return ""
    return s[0:2] + s[-2:]

def process_nums(nums):
    squares = []
    for n in nums:
        squares.append(n**2)
    
    evens = []
    for n in squares:
        if n % 2 == 0:
            evens.append(n)
    
    total = 0
    for n in evens:
        total += n
    
    return total

def is_armstrong(num):
    num_str = str(num)
    length = len(num_str)
    total = 0
    
    for digit in num_str:
        total += int(digit)**length
    
    if total == num:
        return True
    else:
        return False

def curry_check(base):
    def check(num):
        return is_armstrong(num)
    return check

def gen_armstrong():
    num = 1
    while True:
        if is_armstrong(num):
            yield num
        num += 1

def change_base(num_str, from_base, to_base):
    # First convert to decimal
    decimal = 0
    for digit in num_str:
        if '0' <= digit <= '9':
            val = ord(digit) - ord('0')
        else:
            val = ord(digit.upper()) - ord('A') + 10
        decimal = decimal * from_base + val
    
    # Then convert to target base
    if decimal == 0:
        return '0'
    
    result = ""
    while decimal > 0:
        remainder = decimal % to_base
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(remainder - 10 + ord('A')) + result
        decimal = decimal // to_base
    
    return result

def simple_convert(num, from_base, to_base, result=""):
    if num == 0:
        if result == "":
            return "0"
        return result
    
    digit = num % to_base
    if digit < 10:
        char = str(digit)
    else:
        char = chr(digit - 10 + ord('A'))
    
    return simple_convert(num // to_base, from_base, to_base, char + result)

# Main code to test functions
s = "Welcome to Python"
pos = find_p(s)
print(f"Position of 'P' in '{s}': {pos}")

s = input("Enter a string: ")
result = first_last(s)
print(f"String manipulation result: {result}")

numbers = [1, 2, 3, 4, 5, 6]
sum_even = process_nums(numbers)
print(f"Sum of even squares: {sum_even}")

num = 153
print(f"{num} is Armstrong: {is_armstrong(num)}")

check10 = curry_check(10)
print(f"153 is Armstrong in base 10: {check10(153)}")

arm_gen = gen_armstrong()
print("First 5 Armstrong numbers:")
for i in range(5):
    print(next(arm_gen))

bin_num = "1010"
dec_result = change_base(bin_num, 2, 10)
print(f"{bin_num} in base 2 is {dec_result} in base 10")

dec_num = 28
hex_result = simple_convert(dec_num, 10, 16)
print(f"{dec_num} in base 10 is {hex_result} in base 16")

def ms_to_minutes_and_seconds(ms):
    minutes = ms // 60000
    seconds = (ms % 60000) / 1000
    return f"{minutes} minutes, {seconds} seconds"


def is_palindrome(s):
    cleaned_s = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned_s == cleaned_s[::-1]


print(is_armstrong(int(input("Enter a number: "))))
print(is_palindrome(input("Enter a string: ")))
print(ms_to_hours(int(input("Enter a number of milliseconds: "))))
print(ms_to_minutes_and_seconds(int(input("Enter a number of milliseconds: "))))
