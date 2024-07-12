bank_balance = 50000000
APARTMENT_PRICE_2016 = 1100000000
interest_rate = 0.12
year = 1988

while year < 2016:
    bank_balance = bank_balance * (1 + 0.12)
    year += 1

if bank_balance > APARTMENT_PRICE_2016:
    print(f'{int(bank_balance - APARTMENT_PRICE_2016)}원 차이로 동일 아저씨 말씀이 맞습니다.')
elif APARTMENT_PRICE_2016 > bank_balance:
    print(f"{int(APARTMENT_PRICE_2016 - bank_balance)}원 차이로 미란 아주머니 말씀이 맞습니다.")
    