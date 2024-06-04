import random

class GameState():

    def __init__(self):
        self.deck = [i for i in range(2,15) for x in range(4)]
        random.shuffle(self.deck)
        self.board = []
        for i in range(9):
            self.board.append(self.deck.pop())
        self.total_value = sum(self.deck)


    def play_at_location(self, index: int, higher: bool):
        if len(self.board) <= index:
            raise Exception("Trying to play on a board spot that doesnt exist")
        card_played = self.deck.pop()
        if (card_played > self.board[index]) == higher:
            self.board[index] = card_played
        else:
            self.board.pop(index)
        return card_played


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

    def get_low_val_on_board(self):
        return min(self.board)
    
    def get_high_val_on_board(self):
        return max(self.board)
    
    def get_lowest_index_on_board(self):
        return self.board.index(min(self.board))

    def get_highest_index_on_board(self):
        return self.board.index(max(self.board))

    def make_move_perfect(self):
        if len(self.board) == 0:
            raise Exception("The board is empty so the game is over")
        if len(self.deck) == 0:
            raise Exception("The deck is empty you won")
        
        #print(self.get_expected_value())
        
        if self.get_high_val_on_board() - self.get_expected_value() > self.get_expected_value() - self.get_low_val_on_board():
            #print("low: " + str(self.get_high_val_on_board()))
            self.total_value -= self.play_at_location(self.get_highest_index_on_board(), False)
        else:
            #print("high: " + str(self.get_low_val_on_board()))
            self.total_value -= self.play_at_location(self.get_lowest_index_on_board(), True)
        

    def play_game_perfect(self):
        while len(self.board) > 0 and len(self.deck) > 0:
            #print(self.get_board())
            self.make_move_perfect()
        
        if len(self.board) == 0:
            return False
        elif len(self.deck) == 0:
            return True
        else:
            raise Exception("something went very wrong")

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
    
    def get_expected_value(self):
        return self.total_value / len(self.deck)
        
        


def main():
    counter = 0

    for i in range(1000000):
        game = GameState()
        if game.play_game_perfect():
            counter = counter + 1
        #print("board state: " + str(game.get_board()))
        #print("deck remaining: " + str(game.get_deck()))
    print("win percentage sample 1000000: ")
    print(counter / 1000000 * 100)

if __name__ == "__main__":
    main()