import random as r

pitcher = input("Welcome! Who is the pitcher? ").capitalize()

computer_number = []
player_guess = []

while len(computer_number) < 3:  # recommended number is 3 or 4
    num = r.randint(0, 9)  # range 0 ~ 9, also can be setted by 1 ~ 9
    if num not in computer_number:
        computer_number.append(num)
    round = 0

# print(computer_number)
print("-" * 50)

while player_guess != computer_number:
    round += 1
    ball = 0
    strike = 0
    out = 0
    print(f"round {round}")

    try:
        player_guess = list(map(int, input(f"{pitcher} pitch: ").split()))
    except:
        print("You Can Only Input Number")
        round -= 1
        continue

    if len(player_guess) != len(computer_number):
        print(f"Please Input {len(computer_number)} Number")
        round -= 1
        continue
    elif len(set(player_guess)) != len(computer_number):
        print(f"Please Input {len(computer_number)} Diffrent Number")
        round -= 1
        continue
    # range 0 ~ 9, also can be setted by 1 ~ 9
    elif min(player_guess) < 0 or max(player_guess) > 9:
        # range 0 ~ 9, also can be setted by 1 ~ 9
        print("Please Input Number Between 0 to 9")
        round -= 1
        continue

    for guess in player_guess:
        if guess not in computer_number:
            out += 1
        elif player_guess.index(guess) == computer_number.index(guess):
            strike += 1
        else:
            ball += 1

    print(f"out:{out}, ball:{ball}, strike:{strike}")
    print("-" * 50)

print(f"Congratulation {pitcher}! You got it in {round} turn")
