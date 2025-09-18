def isAnagram(s, t):
    if len(s) != len(t):
        return False
    count = [0] * 26
    for char in s:
        count[ord(char) - ord('a')] += 1
    for char in t:
        count[ord(char) - ord('a')] -= 1
        if count[ord(char) - ord('a')] < 0:
            return False
    return True

while True:
    print("Введите первую строку или выход для выхода:")
    s = input()
    if s == 'выход':
        break
    
    print("Введите вторую строку:")
    t = input()
    
    print(f"Являются ли анаграммами: {isAnagram(s, t)}")
    print()