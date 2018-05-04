
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s)

s[0] = 'X'
print(s)
print(s[2:5])

s[2:5] = ['C', 'D', 'E']
print(s)

s[2:5] = []
print(s)

s[:] = []
print(s)


n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)


n.append(100)  # 一番最後に要素を追加したい時
print(n)

n.insert(0, 200)  # 指定した要素位置にデータを挿入したい時（この場合は 0番目に200を挿入）
print(n)

print(n.pop(0))   # 指定した要素のデータを取りだす（この場合は要素 0 ）
print(n)          # 取り出したので　全体の要素は減っている

print(n.pop())    # 引数を指定しないと一番最後の要素を取り出す

del n[0]    # del文は完全にデータを削除する
print(n)


a = [1, 2, 3, 4, 5,]
b = [6, 7, 8, 9, 10]

print(a + b)
print(a)

a.extend(b)
print(a)