s = input()

values = input().split()
i = int(values[0])
c = values[1]

print(s[:i-1] + c + s[i:])
