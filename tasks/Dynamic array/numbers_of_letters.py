# 英字小文字の数
num_of_letters = ord("z") - ord("a") + 1


# 文字列strの、a～zの出現回数を数えて配列で返す
def count_letters(str):
    ans = [0] * num_of_letters
    for i in range(num_of_letters):
        character = chr(i + ord("a"))
        ans[i] = str.count(character)
    return ans


s = "aaabbbccdddde"
answers = count_letters(s)
print(" ".join(map(str, answers)))
