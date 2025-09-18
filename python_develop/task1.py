def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

while True:
    print("Введите строку или напишите 'выход' для выхода из программы.")
    s = input()
    if s == 'выход':
        break
    print(isValid(s))
    print()