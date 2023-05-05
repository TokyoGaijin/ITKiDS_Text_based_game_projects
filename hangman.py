import random

words = ["dog", "cat", "elephant", "lion", "tiger", "piano", "guitar", "trumpet", "saxophone", "game", "japan", "america", "africa", "europe"]

class Hangman():
    def __init__(self):
        self.head = "〇"
        self.torso = "|"
        self.shoulders = "---"
        self.left_armleg = "/"
        self.right_armleg = "|"
        self.body = []
        self.points = 0

    def add_bodypart(self, part):
        if part == 1:
            self.body.append(self.head)
        elif part == 2:
            self.body.append(self.shoulders)
        elif part == 3:
            self.body.append(self.left_armleg)
        elif part == 4:
            self.body.append(self.right_armleg)
        elif part == 5:
            self.body.append(self.torso)
        elif part == 6:
            self.body.append(self.left_armleg)
        elif part == 7:
            self.body.append(self.right_armleg)

    def draw_body(self):
        if self.points == 1:
            print("".join(self.body[0]))
        elif self.points == 2:
            print(f" {self.body[0]}")
            print(f"{self.body[1]}")
        elif self.points == 3:
            print(f" {self.body[0]}")
            print(f"{self.body[1]}")
            print(f"{self.body[2]}")
        elif self.points == 4:
            print(f" {self.body[0]}")
            print(f"{self.body[1]}")
            print(f"{self.body[2]} {self.body[3]}")
        elif self.points == 5:
            print(f" {self.body[0]}")
            print(f"{self.body[1]}")
            print(f"{self.body[2]}{self.body[4]}{self.body[3]}")
        elif self.points == 6:
            print(f" {self.body[0]}")
            print(f"{self.body[1]}")
            print(f"{self.body[2]}{self.body[4]}{self.body[3]}")
            print(f"{self.body[2]}")
        elif self.points == 7:
            print(f" {self.body[0]}")
            print(f"{self.body[1]}")
            print(f"{self.body[2]}{self.body[4]}{self.body[3]}")
            print(f"{self.body[2]} {self.body[3]}")

def init():
    global solution, game_board, used_letters, score
    solution = words[random.randrange(0, len(words))]
    deadman.body = []
    game_board = []
    used_letters = []
    score = 0
    for i in range(0, len(solution)):
        game_board.append("-")


deadman = Hangman()
solution = None
game_board = None
used_letters = None
score = None

def run():
    global solution, game_board, used_letters, score
    init()

    while True:
        print("================================")
        print("".join(game_board))
        print(f"You have {score} points.")
        guess = input("Guess a letter (or solve the puzzle): ").lower()
        if guess in solution:
            for i, char in enumerate(solution):
                if char == guess:
                    index = solution.index(char, i)
                    game_board[index] = guess
            for i in range(0, len(game_board)):
                if "-" not in game_board:
                    print("Congratulations! You win!")
                    print(f"{solution} was the correct answer!!")
                    print("")
                    choice = input("Play again? [Y/y for yes or any to quit]: ")
                    if choice.lower() == "y":
                        init()
                    else:
                        print("Thank you for playing.")
                        exit(1)
            continue
        else:
            used_letters.append(guess)
            print("Letter not found.")
            print("".join(used_letters))
            score += 1
            deadman.points = score
            deadman.add_bodypart(score)
            deadman.draw_body()
            if score >= 7:
                print(f"The answer was {solution}")
                print("You lose! GAME OVER!")
                print("")
                choice1 = input("Play again? [Y/y for yes or anything to quit]: ")
                if choice1.lower() == "y":
                    init()
                else:
                    print("Thank you for playing.")
                    exit(1)
            continue





if __name__ == '__main__':
    run()