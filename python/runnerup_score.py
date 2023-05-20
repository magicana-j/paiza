str = "2 3 6 6 5"

l = list(map(int, str.split()))
score_desc = sorted(list((set(l))), reverse=True)
print(score_desc[1])
