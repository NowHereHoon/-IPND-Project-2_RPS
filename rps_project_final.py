import random
moves = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def move(self):
        return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        else:
            return "rock"


class HumanPlayer(Player):
    def move(self):
        input_word = (input("Rock, paper, scissors? > ")).lower()
        while input_word not in moves:
            input_word = (input("Rock, paper, scissors? > ")).lower()
        return input_word


def beats(one, two):
    if ((one == 'rock' and two == 'scissors') or
        (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock')) is True:
        return "one"
    elif ((one == 'rock' and two == 'rock') or
          (one == 'scissors' and two == 'scissors') or
          (one == 'paper' and two == 'paper')) is True:
        return "tie"
    else:
        return "two"


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"You player {move1}.\nOpponent played {move2}.\n")
        if beats(move1, move2) == "one":
            print("** PLAYER ONE WINS **\n")
            self.w1 += 1
        elif beats(move1, move2) == "two":
            print("** PLAYER TWO WINS **\n")
            self.w2 += 1
        else:
            print("** TIE **\n")
        print(f"Score: Player One {self.w1}, Player Two {self.w2}\n")
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Rock Paper Scissors, Go!\n")
        self.w1 = 0
        self.w2 = 0
        self.round = 0
        while abs(self.w1 - self.w2) < 3:
            print(f"Round {self.round + 1} --")
            self.play_round()
            self.round += 1
        if self.w1 - self.w2 == 3:
            print("\n<<<<< PLAYER ONE WON THE GAME >>>>>\n")
        else:
            print("\n<<<<< PLAYER TWO WON THE GAME >>>>>\n")
        print(f"Score: Player One {self.w1} vs Player Two {self.w2}\n")
        print("Game over!")


if __name__ == '__main__':
    human = HumanPlayer("rock", "rock")
    computer = random.choice([Player("rock", "rock"),
                              RandomPlayer("rock", "rock"),
                              ReflectPlayer("rock", "rock"),
                              CyclePlayer("rock", "rock")])
    game = Game(human, computer)
    game.play_game()
