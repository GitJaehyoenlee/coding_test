N = int(input())
K = int(input())

cnt = 0
while True:
    mok = N // K
    cha = N - mok * K

    if mok == 0:
        cnt += N - 1
        break
    else:
        cnt = cnt +  cha + 1
        N = mok

print(cnt)

