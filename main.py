from src.word_functions import createSecret
from src.api import collect_word
from src.player import Player

def main()->None:
    player_zodiac = Player()

    while(True):

        word = collect_word()
        secret = createSecret(word , 2)


        print(f"secret : {secret}")

        guessed_word = input("guess secret word: ")
        if guessed_word == word:
            print("you win")
            break
        else:
            player_zodiac.lose_hp()
            print(f"your current hp: {player_zodiac.hp}")

        if player_zodiac.hp == 0:
            print("Game Over you lose")
            break
        
        
if __name__ == "__main__":
    main()