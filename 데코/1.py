import random
target_number = random.randint(1, 100)
attempts = 0

print("1부터 100 사이의 숫자를 맞추시오.")

while True:
    try:
        guess = int(input("숫자를 입력하시오: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("1에서 100 사이의 숫자를 입력해주세요.")
            continue
        if guess < target_number:
            print("큼!")
        elif guess > target_number:
            print("낮음!")
        else:
            print(f"축하합니다. 시도 횟수= {attempts}")
            break

    except ValueError:
        print("유효한 숫자를 입력해주세요.")
        