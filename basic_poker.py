import random
from collections import Counter


class Hand:
    def __init__(self):
        self.cards = []
        self.bank = 500
        self.bet = 0
        self.pay_out = None

    def deal(self):
        for i in range(1, 6):
            self.cards.append(random.randrange(1, 11))

    def redraw(self, index):
        self.cards[index] = random.randrange(1, 11)

    def update_bet(self, bet_amount):
        self.bet = bet_amount
        self.pay_out = [-self.bet, 0, self.bet, self.bet * 2, self.bet * 3, self.bet * 9,
                        self.bet * 81, self.bet * (81 * 81)]

    def check_hand(self, hand):
        hand = self.cards
        card_counts = Counter(hand)

        if 5 in card_counts.values():
            return "5x"
        elif 4 in card_counts.values():
            return "4x"
        elif set(card_counts.values()) == {2, 3}:
            return "FS"
        elif len(set(hand)) == 5 and (max(hand) - min(hand) == 4):
            return "S"
        elif 3 in card_counts.values():
            return "3x"
        elif list(card_counts.values()).count(2) == 2:
            return "2x"
        elif 2 in card_counts.values():
            return "1x"

        return "You Lose!"

    def payout(self):
        if self.check_hand(self.cards) == "You Lose!":
            self.bank += self.pay_out[0]
        elif self.check_hand(self.cards) == "1x":
            self.bank += self.pay_out[1]
        elif self.check_hand(self.cards) == "2x":
            self.bank += self.bet
        elif self.check_hand(self.cards) == "3x":
            self.bank += self.pay_out[3]
        elif self.check_hand(self.cards) == "S":
            self.bank += self.pay_out[4]
        elif self.check_hand(self.cards) == "FS":
            self.bank += self.pay_out[5]
        elif self.check_hand(self.cards) == "4x":
            self.bank += self.pay_out[6]
        elif self.check_hand(self.cards) == "5x":
            self.bank += self.pay_out[7]

        if self.check_hand(self.cards) == "You Lose!":
            print("You lost the hand!")
            print(f"{self.bet} has been taken from your bank.")
        else:
            print("Congratulations! YOU WIN THE HAND!")
            print(f"Your new amount is {self.bank}!")


player = Hand()


def run():
    while True:
        player.cards = []
        bet = input(f"You currently have {player.bank}. Enter bet (or [Q] to quit): ")
        if bet.lower() == 'q' or 'q' in bet.lower():
            print("Thanks for playing.")
            exit(1)
        elif int(bet) > player.bank:
            print("Cannot place that bet. Try again.")
            continue
        else:
            player.update_bet(int(bet))
            player.deal()
            print(player.cards)
            draw_1 = input("Draw new card 1? [y]es or [any] for no: ")
            draw_2 = input("Draw new card 2? [y]es or [any] for no:  ")
            draw_3 = input("Draw new card 3? [y]es or [any] for no:  ")
            draw_4 = input("Draw new card 4? [y]es or [any] for no:  ")
            draw_5 = input("Draw new card 5? [y]es or [any] for no:  ")
            if draw_1 == 'y':
                player.redraw(0)
            if draw_2 == 'y':
                player.redraw(1)
            if draw_3 == 'y':
                player.redraw(2)
            if draw_4 == 'y':
                player.redraw(3)
            if draw_5 == 'y':
                player.redraw(4)
            print()
            print(player.cards)
            player.payout()
            if player.bank <= 0:
                print("You're out of money!!")
                print("GAME OVER!!")
                print()
                retry = input("Play again? [y]es [any]I had enough: ")
                if retry.lower() == 'y':
                    player.bank = 500
                    continue
                else:
                    print("Thanks for playing!")
                    exit(1)
            else:
                play_another = input("Play another hand? [y]es [any]I know when to fold 'em: ")
                if play_another.lower() == 'y':
                    continue
                else:
                    print("Thanks for playing!")
                    exit(1)


if __name__ == '__main__':
    run()
