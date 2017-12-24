class tictactoe:
    def __init__(self):
        self.board = [1,2,3,4,5,6,7,8,9]
    def board_set(self,position,value):
        if self.board[position] == 'X' or self.board[position] == 'Y':
            return False
        else:
            self.board[position] = value
            return True
    def board_print(self):
        print( '\n **tic_tac_toe board**')
        print( '|' , self.board[0] , '|' , self.board[1] , '|' , self.board[2] , '|')
        print( ' -----------')
        print( '|' , self.board[3] , '|' , self.board[4] , '|' , self.board[5] , '|')
        print( ' -----------')
        print( '|' , self.board[6] , '|' , self.board[7] , '|' , self.board[8] , '|')
        print( ' -------------------------------\n')
    def board_check(self):
        if ((self.board[0] == self.board[1] and self.board[1] == self.board[2]) or
            (self.board[3] == self.board[4] and self.board[4] == self.board[5]) or
            (self.board[6] == self.board[7] and self.board[7] == self.board[8]) or
            (self.board[0] == self.board[3] and self.board[3] == self.board[6]) or
            (self.board[1] == self.board[4] and self.board[4] == self.board[7]) or
            (self.board[2] == self.board[5] and self.board[5] == self.board[8]) or
            (self.board[0] == self.board[4] and self.board[4] == self.board[8]) or
            (self.board[6] == self.board[4] and self.board[4] == self.board[2])):
            return True
        else:
            return False

def main():
    count = 9
    print(count)
    count = 'abc'
    print(count)
    game = tictactoe()
    while count:
        game.board_print()
        if count % 2 == 1:
            print("player 1 insert position for X", "\n")
            val = 'X'
        else:
            print("player 1 insert position for O", "\n")
            val = 'Y'
        pos = int(input("enter position now"))
        pos = pos-1
        if (pos < 0 or pos > 8):
            print("enter a valid position", "\n")
            continue
        set_board = game.board_set(pos,val)
        if set_board == True:
            print("success: position set")
            win = game.board_check()
            if win == True:
                if count % 2 == 1:
                    print("************player 1 wins***********", "\n")
                    game.board_print()
                    return
                else:
                    print("************player 2 wins***********", "\n")
                    game.board_print()
                    return
        else:
            print("error: position already set")
            continue
        count = count-1
    print("no result")
    game.board_print()

if __name__ == '__main__':
    main()
