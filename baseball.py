from random import randint
OUT_COUNT = 3

def generate_numbers():
    numbers = []
    
    while len(numbers) < OUT_COUNT:
        random = randint(0,9)
        if random not in numbers:
            numbers.append(random)

    print(f"0과 9 사이의 서로 다른 숫자 {OUT_COUNT}개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess():
    print(f"숫자 {OUT_COUNT}개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    while (n:=len(new_guess)) < OUT_COUNT:
        num = int(input(f"{n+1}번째 숫자를 입력하세요: "))
        
        if num > 9 or num < 0:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue
        elif num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(num)
    
    return new_guess

def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for i in range(OUT_COUNT):
        if guesses[i] in solution:
            if guesses[i] == solution[i]:
                strike_count += 1
            else:
                ball_count += 1

    return strike_count, ball_count

# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True:
    guesses = take_guess()
    s,b = get_score(guesses,ANSWER)
    print(f"{s}S {b}B")
    tries += 1
    
    if s == OUT_COUNT:
        break

print(f"축하합니다. {tries}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.")