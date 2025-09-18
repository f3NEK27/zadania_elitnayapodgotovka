def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

while True:
    print("Введите первый массив через пробел или выход для выхода из программы")
    input_str = input()
    if input_str == 'выход':
        break
    
    nums1 = list(map(int, input_str.split()))
    
    print("Введите значение m:")
    m = int(input())
    
    print("Введите второй массив через пробел")
    nums2 = list(map(int, input().split()))
    
    print("Введите значение n:")
    n = int(input())
    
    merge(nums1, m, nums2, n)
    print(f"Результат: {nums1}")
    print()