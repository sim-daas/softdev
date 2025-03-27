def is_armstrong(n):
    if not isinstance(n, int) or n < 100 or n >= 1000:
        return False
    sum_cubes = sum(int(d) ** 3 for d in str(n))
    return sum_cubes == n


def ms_to_hours(ms):
    return ms // 3600000


def ms_to_minutes_and_seconds(ms):
    minutes = ms // 60000
    seconds = (ms % 60000) // 1000
    return f"{minutes} minutes, {seconds} seconds"


def is_palindrome(s):
    cleaned_s = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned_s == cleaned_s[::-1]


print(is_armstrong(int(input("Enter a number: "))))
print(is_palindrome(input("Enter a string: ")))
print(ms_to_hours(int(input("Enter a number of milliseconds: "))))
print(ms_to_minutes_and_seconds(int(input("Enter a number of milliseconds: "))))
