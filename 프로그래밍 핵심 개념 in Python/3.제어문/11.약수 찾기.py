N = 120
i = 1
total = 0

while i <= N:
    if 120 % i == 0:
        print(i)
        total += 1
    i += 1

print(f"{N}의 약수는 총 {total}개입니다.")
