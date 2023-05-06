import random

hiragana = [[None, "あ", "い", "う", "え", "お"],
            [None, "か", "き", "く", "け", "こ", "が", "ぎ", "ぐ", "げ", "ご"],
            [None, "さ", "し", "す", "せ", "そ", "ざ", "じ", "ず", "ぜ", "ぞ"],
            [None, "た", "ち", "つ", "て", "と", "だ", "ぢ", "づ", "で", "ど", "っ"],
            [None, "な", "に", "ぬ", "ね", "の"],
            [None, "は", "ひ", "ふ", "へ", "ほ", "ば", "び", "ぶ", "べ", "ぼ", "ぱ", "ぴ", "ぷ", "ぺ", "ぽ"],
            [None, "ま", "み", "む", "め", "も"],
            [None, "や", None, "ゆ", None, "よ", "ゃ", "ゅ", "ょ"],
            [None, "ら", "り", "る", "れ", "ろ"],
            [None, "わ", "ゐ", None, "ゑ", "を"],
            [None, "ん", None, None, None, None]]


todofuken = ["ほっかいど", "あおもり", "いわて", "みやぎ", "あきた", "やまがた", "ふくしま",
             "いばらき", "とちぎ", "ぐんま", "さいたま", "ちば", "とうきょう", "かながわ",
             "にいがた", "とやま", "いしかわ", "ふくい", "やまなし", "ながの", "ぎふ", "しずおか", "あいち",
             "みえ", "しが", "きょうと", "おおさか", "ひょうご", "なら", "わかやま",
             "とっとり", "しまね", "おかやま", "ひろしま", "やまぐち",
             "とくしま", "かがわ", "えひめ", "こうち",
             "ふくおか", "さが", "ながさき", "くまもと", "おおいた", "みやざき", "かごしま", "おきなわ"]

hiragana_consonants = "AKSTNHMYRWN"
hiragana_categories = []

for i in range(len(hiragana)):
    hiragana_categories.append(hiragana_consonants[i])


def get_puzzle(code):
    puzzle = ""
    for letter in code:
        for categories in range(len(hiragana)):
            if letter in hiragana[categories]:
                puzzle += f"{hiragana_categories[categories]}-{hiragana[categories].index(letter)} "

    return puzzle

def get_answer():
    answer = todofuken[random.randrange(0, len(todofuken))]
    return answer


def run():
    chances = 0
    solution = ""
    code = ""
    wins = 0
    losses = 0

    def init(reset_wins_losses = True):
        nonlocal chances, solution, code, wins, losses
        solution = get_answer()
        code = get_puzzle(solution)
        chances = 5
        if reset_wins_losses:
            wins = 0
            losses = 0


    init()
    play = input("始めますか。 [y]はい [なんでも]修了: ")
    if play.lower() == 'y':
        while True:
            print(f"チャンス：あと {chances}回")
            print(code)
            guess = input("ひらがなで予想して： ")
            if guess != solution:
                print("間違えました！残念ながら1回チャンスを使いました！")
                chances -= 1
                if chances > 0:
                    print("難しいでしょう！　自動解きますか。（「負け」の数に足す）")
                    solve = input("[y]はい　[なんでも]もう一回やってみる：　")
                    if solve.lower() == 'y':
                        losses += 1
                        print(f"パズルは：　{code}")
                        print(f"答えは：   {solution}")
                        print("")
                        print(f"あなたは　{wins}回勝ち、{losses}回負けた")
                        retry = input("新しいパズルやってみますか。[y]はい [なんでも]修了：　")
                        if retry.lower() == 'y':
                            init(reset_wins_losses=False)
                            continue
                        else:
                            print("遊んでくれてありがとうございました！")
                            exit(1)
                    else:
                        continue
                else:
                    print("残念ながら、チャンスがなくなりました。")
                    print(f"答えは： {solution}")
                    losses += 1
                    print(f"あなたは　{wins}回勝ち、{losses}回負けた")
                    try_again = input("もう一度やってみますか。")
                    if try_again.lower() == 'y':
                        init(reset_wins_losses=False)
                        continue
                    else:
                        print("遊んでくれてありがとうございました！")
                        exit(1)
            else:
                print("よくできました！")
                print(f"答えは： {solution} でした！")
                wins += 1
                print(f"あなたは　{wins}回勝ち、{losses}回負けた")
                try_again = input("もう一度やってみますか。")
                if try_again.lower() == 'y':
                    init(reset_wins_losses=False)
                    continue
                else:
                    print("遊んでくれてありがとうございました！")
                    exit(1)
    else:
        print("遊んでくれてありがとうございました！")
        exit(1)


if __name__ == '__main__':
    run()