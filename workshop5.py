
import random

def guess_random_num(tries, start, stop):
    db = {} 
    random_num = random.randint(start, stop)
    print("chosen is:", random_num)
    while tries:
        print("Number of tries left:", tries)
        guess = int(input("Guess a number between " +
                    str(start) + " and " + str(stop) + ": "))
        if db and guess == db.get(guess):
            print("existed")

        elif guess == random_num:
            print("You guessed the correct number!")
            return

        elif guess < random_num:
            print("Guess higher!")

        else:
            print("Guess lower!")
        
        db[guess] = guess
        tries -= 1

    print("You have failed to guess the number:", random_num)

def guess_random_num_linear(tries, start, stop):
    random_num = random.randint(start, stop)

    print("The number for the program to guess is:", random_num)

    for num in range(start, stop+1):

        if not tries:
            print("The program has failed to guess the correct number.")
            return

        print("Number of tries left:", tries)
        print("The program is guessing...", num)

        if num == random_num:
            print("The program has guessed the correct number!")
            return

        tries -= 1


def guess_random_num_binary(tries, start, stop):
    random_num = random.randint(start, stop)
    print("Random number to find:", random_num)

    lower_bound = start
    upper_bound = stop

    while tries:
        pivot = (lower_bound + upper_bound) // 2

        if pivot == random_num:
            print("Found it!", random_num)
            return
        if pivot > random_num:
            print("Guessing lower!")
            upper_bound = pivot - 1
        else:
            print("Guessing higher!")
            lower_bound = pivot + 1
        tries -= 1

    print("Your program failed to find the number.")

    def gambling_game():  
        money = 10
        while money and money <= 50:
            print("You have $" + str(money) + " left.")
            while True:
                bet = int(
                input("How much do you wish to bet that the computer will guess correctly?: "))
                if bet < 1 or bet > money:
                    print("You can't bet that amount!")
                else:
                    break

            if guess_random_num_linear(5, 1, 10):
                print("You win $" + str(bet))
                money += bet
            else:
                print("You lose $" + str(bet))
                money -= bet

        if money:
            print("Congratulations, you have won over $50")
        else:
            print("You've lost all your money!")


## Driver Code Task One
## 5 == tries
## 0, 10 == Range of random integers to choose from.

guess_random_num(5, 0, 10)

## Driver Code Task Two 
## 5 == tries
## 0, 10 == Range of random integers to choose from.

guess_random_num_linear(5, 0, 10)

## Driver Code Task Three
## 5 == tries
## 0, 100 == Range of random integers to choose from.

guess_random_num_binary(5, 0, 100)

