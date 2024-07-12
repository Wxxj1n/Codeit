def calculate_change(payment, cost):
    change = payment - cost
    fifty_thousand = change // 50000
    ten_thousand = (change % 50000) // 10000
    five_thousand = (change % 10000) // 5000
    one_thousand = (change % 5000) // 1000

    print(f'50000원 지폐: {fifty_thousand}장')
    print(f'10000원 지폐: {ten_thousand}장')
    print(f'5000원 지폐: {five_thousand}장')
    print(f'1000원 지폐: {one_thousand}장')


# 테스트 코드
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)
