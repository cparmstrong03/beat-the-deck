import random

class GameState():

    def __init__(self):
        self.deck = [i for i in range(2,15) for x in range(4)]
        random.shuffle(self.deck)
        self.board = []
        for i in range(9):
            self.board.append(self.deck.pop())


    def play_at_location(self, index: int, higher: bool):
        if len(self.board) <= index:
            raise Exception("Trying to play on a board spot that doesnt exist")
        card_played = self.deck.pop()
        if (card_played > self.board[index]) == higher:
            self.board[index] = card_played
        else:
            self.board.pop(index)


    def make_move_basic(self):
        if len(self.board) == 0:
            raise Exception("The board is empty so the game is over")
        if len(self.deck) == 0:
            raise Exception("The deck is empty you won")
        
        if self.board[0] > 8:
            #print(str(self.board[0]) + " low")
            self.play_at_location(0, False)
        elif self.board[0] < 8:
            #print(str(self.board[0]) + " high")
            self.play_at_location(0, True)
        else:
            self.play_at_location(0, random.choice([True, False]))
            #print("random")

    def play_game(self):
        while len(self.board) > 0 and len(self.deck) > 0:
            #print(self.get_board())
            self.make_move_basic()
        
        if len(self.board) == 0:
            return False
        elif len(self.deck) == 0:
            return True
        else:
            raise Exception("something went very wrong")
        
    def get_board(self):
        return self.board
    
    def get_deck(self):
        return self.deck
        
        


def main():
    counter = 0

    for i in range(1000000):
        game = GameState()
        if game.play_game():
            counter = counter + 1
        #print("board state: " + str(game.get_board()))
        #print("deck remaining: " + str(game.get_deck()))
    print("win percentage sample 1000000: ")
    print(counter / 1000000 * 100)

if __name__ == "__main__":
    main()