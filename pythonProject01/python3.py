a = int(input())
b = int(input())

# Первое нечётное число не меньше a
a_odd = a + (not (a % 2))
# Крайнее нечётное число не больше b
b_odd = b - (not (a % 2))

result = list(str(i) for i in range(a_odd, b_odd+1, 2))

print(' '.join(result))