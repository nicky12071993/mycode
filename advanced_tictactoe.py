#after completion of this program it feels alive
#its creative and sexy
import os

def clear_screen():
    os.system("cls")

class tictactoeten:

    def __init__(self):        #initializing the sub and main tic_tac_toe
        #self.first = [1,2,3,4,5,6,7,8,9]
        self.first = [82,83,84,85,86,87,88,89,90]
        self.second = [10,11,12,13,14,15,16,17,18]
        self.third = [19,20,21,22,23,24,25,26,27]
        self.fourth = [28,29,30,31,32,33,34,35,36]
        self.fifth = [37,38,39,40,41,42,43,44,45]
        self.sixth = [46,47,48,49,50,51,52,53,54]
        self.seventh = [55,56,57,58,59,60,61,62,63]
        self.eighth = [64,65,66,67,68,69,70,71,72]
        self.ninth = [73,74,75,76,77,78,79,80,81]
        self.zeroth = [1,2,3,4,5,6,7,8,9]     #initializing main tic_tac_toe

    def full_board_print(self):    #print the board
        def print_board(a,b,c):
            print(' ',a[0],' ',a[1],' ',a[2], end='  |')
            print(' ',b[0],' ',b[1],' ',b[2], end='  |')
            print(' ',c[0] ,' ',c[1],' ',c[2])
            print( '                |                |           ')
            print(' ',a[3],' ',a[4],' ',a[5], end='  |')
            print(' ',b[3],' ',b[4],' ',b[5], end='  |')
            print(' ',c[3] ,' ',c[4],' ',c[5])
            print( '                |                |           ')
            print(' ',a[6],' ',a[7],' ',a[8], end='  |')
            print(' ',b[6],' ',b[7],' ',b[8], end='  |')
            print(' ',c[6] ,' ',c[7],' ',c[8])
            print( ' ---------------|----------------|-------------')
        print("************** Nick Tac Toe Ten **************")
        print_board(self.first,self.second,self.third)
        print_board(self.fourth,self.fifth,self.sixth)
        print_board(self.seventh,self.eighth,self.ninth)

    def get_insertion_position(self,last_position):      #get what position to enter
        if last_position == 100:       #first entry anywhere on the board
            lower_limit = 10
            upper_limit = 90
        elif last_position == 0:
            lower_limit = 82
            upper_limit = 90
        elif last_position == 1:
            lower_limit = 10
            upper_limit = 18
        elif last_position == 2:
            lower_limit = 19
            upper_limit = 27
        elif last_position == 3:
            lower_limit = 28
            upper_limit = 36
        elif last_position == 4:
            lower_limit = 37
            upper_limit = 45
        elif last_position == 5:
            lower_limit = 46
            upper_limit = 54
        elif last_position == 6:
            lower_limit = 55
            upper_limit = 63
        elif last_position == 7:
            lower_limit = 64
            upper_limit = 72
        elif last_position == 8:
            lower_limit = 73
            upper_limit = 81
        return (lower_limit,upper_limit)

    def position_check(self,last_position,board_position):          #ready the parameters to insert in the sub tic_tac_toe
        if board_position>=82 and board_position<=90:
            insert_pos = board_position-82             #set position to insert
            sub_tictactoe = self.first         #set the sub tictactoe
            zeroth_pos = 0         #set the main tictactoe
            if last_position == 0 or last_position == 100:       #set true for correct sub tictactoe and first entry
                pos_check_flag = True
                return (insert_pos,sub_tictactoe,zeroth_pos,pos_check_flag)
            else:
                pos_check_flag = False
                return (insert_pos,sub_tictactoe,zeroth_pos,pos_check_flag)
        elif board_position>=10 and board_position<=18:
            insert_pos = board_position-10
            sub_tictactoe = self.second
            zeroth_pos = 1
            if last_position == 1 or last_position == 100:
                pos_check_flag = True
                return (insert_pos,sub_tictactoe,zeroth_pos,pos_check_flag)
            else:
                pos_check_flag = False
                return (insert_pos,sub_tictactoe,zeroth_pos,pos_check_flag)
        elif board_position>=19 and board_position<=27:
            insert_pos = board_position-19
            sub_tictactoe = self.third
            zeroth_pos = 2
            if last_position == 2 or last_position == 100:
                pos_check_flag = True
                return (insert_pos,sub_tictactoe,zeroth_pos,pos_check_flag)
            else:
                pos_check_flag = False
                return (insert_pos,sub_tictactoe,zeroth_pos,pos_check_flag)
        elif board_position>=28 and board_position<=36:
            insert_pos = board_position-28
            sub_tictactoe = self.fourth
            zeroth_pos = 3
            if last_position == 3 or last_position == 100:
                pos_check_flag = True
                return (insert_pos,sub_tictactoe,zeroth_pos,pos_check_flag)
            else:
                pos_check_flag = False
                return (insert_pos,sub_tictactoe,zeroth_pos,pos_check_flag)
        elif board_position>=37 and board_position<=45:
            insert_pos = board_position-37
            sub_tictactoe = self.fifth
            zeroth_pos = 4
            if last_position == 4 or last_position == 100:
                pos_check_flag = True
                return (insert_pos,sub_tictactoe,zeroth_pos,pos_check_flag)
            else:
                pos_check_flag = False
                return (insert_pos,sub_tictactoe,zeroth_pos,pos_check_flag)
        elif board_position>=46 and board_position<=54:
            insert_pos = board_position-46
            sub_tictactoe = self.sixth
            zeroth_pos = 5
            if last_position == 5 or last_position == 100:
                pos_check_flag = True
                return (insert_pos,sub_tictactoe,zeroth_pos,pos_check_flag)
            else:
                pos_check_flag = False
                return (insert_pos,sub_tictactoe,zeroth_pos,pos_check_flag)
        elif board_position>=55 and board_position<=63:
            insert_pos = board_position-55
            sub_tictactoe = self.seventh
            zeroth_pos = 6
            if last_position == 6 or last_position == 100:
                pos_check_flag = True
                return (insert_pos,sub_tictactoe,zeroth_pos,pos_check_flag)
            else:
                pos_check_flag = False
                return (insert_pos,sub_tictactoe,zeroth_pos,pos_check_flag)
        elif board_position>=64 and board_position<=72:
            insert_pos = board_position-64
            sub_tictactoe = self.eighth
            zeroth_pos = 7
            if last_position == 7 or last_position == 100:
                pos_check_flag = True
                return (insert_pos,sub_tictactoe,zeroth_pos,pos_check_flag)
            else:
                pos_check_flag = False
                return (insert_pos,sub_tictactoe,zeroth_pos,pos_check_flag)
        elif board_position>=73 and board_position<=81:
            insert_pos = board_position-73
            sub_tictactoe = self.ninth
            zeroth_pos = 8
            if last_position == 8 or last_position == 100:
                pos_check_flag = True
                return (insert_pos,sub_tictactoe,zeroth_pos,pos_check_flag)
            else:
                pos_check_flag = False
                return (insert_pos,sub_tictactoe,zeroth_pos,pos_check_flag)
        
    def board_check(self,board_name):  #check board win
        if ((board_name[0] == board_name[1] and board_name[1] == board_name[2]) or
            (board_name[3] == board_name[4] and board_name[4] == board_name[5]) or
            (board_name[6] == board_name[7] and board_name[7] == board_name[8]) or
            (board_name[0] == board_name[3] and board_name[3] == board_name[6]) or
            (board_name[1] == board_name[4] and board_name[4] == board_name[7]) or
            (board_name[2] == board_name[5] and board_name[5] == board_name[8]) or
            (board_name[0] == board_name[4] and board_name[4] == board_name[8]) or
            (board_name[6] == board_name[4] and board_name[4] == board_name[2])):
            return True
        else:
            return False

    def board_set(self,board_name,position,value):  #set all sub tictactoe
        if board_name[position] == 'XX' or board_name[position] == 'YY':
            return False
        else:
            board_name[position] = value
            return True
    
    def zeroth_board_set(self,position,value):   #set the main tictactoe
        if self.zeroth[position] != 'XX' and self.zeroth[position] != 'YY':
            self.zeroth[position] = value

def main():
    count = 81                 #set total chances
    game = tictactoeten()      #initialize board
    last_pos = 100             #set for first entry
    while count:
        game.full_board_print()       #print board
        lower_limit,upper_limit = game.get_insertion_position(last_pos)     #get limits to print for player
        if count % 2 == 1:
            player_no = '1'                                                  #set limit as per even odd
            val = 'XX'              #set value as per player
        else:
            player_no = '2'
            val = 'YY'
        print("player {} enter position for {} between {} and {}".format(player_no,val,lower_limit,upper_limit))
        board_pos = int(input("enter position now"))        #take input
        if board_pos<10 or board_pos>90:                    #check for first entry
            print("Error: enter valid position between 10 to 90")
            continue
        insert_pos,sub_tictactoe,zeroth_pos,pos_check_flag = game.position_check(last_pos,board_pos)      #get all parameters to make insert
        if pos_check_flag == False:
            clear_screen()
            if last_pos is not 100:
                print("player {} entered {}".format(player_no,board_pos))
            print("Error: enter between {} and {}".format(lower_limit,upper_limit))         #print error with corect limits
            continue
        set_board = game.board_set(sub_tictactoe,insert_pos,val)          #set value if allowed
        if set_board == True:
            clear_screen()
            if last_pos is not 100:
                print("player {} entered {}".format(player_no,board_pos))
            print("Success: position set")
            last_pos = insert_pos       #set last position to insert for next player
            lower_limit,upper_limit = game.get_insertion_position(last_pos)     #update lower and upper limits
            sub_win = game.board_check(sub_tictactoe)           #check for sub tictactoe
            if sub_win == True:
                print("won this small one")
                game.zeroth_board_set(zeroth_pos,val)           #if sub tictactoe is won then set for main tictactoe
                main_win = game.board_check(game.zeroth)        #if sub tictactoe is won then check for main tictactoe
                if main_win == True:
                    if count % 2 == 1:
                        print("************player 1 wins***********")       #if main tictactoe is won then declare winner
                        game.full_board_print()
                        return
                    else:
                        print("************player 2 wins***********")
                        game.full_board_print()
                        return
        else:
            clear_screen()
            if last_pos is not 100:
                print("player {} entered {}".format(player_no,board_pos))
            print("Error: position already set")        #if position is not set
            continue
        count = count-1         #update all chance
        # print(count)
    print("no result")          #if all chances are finished
    game.full_board_print()

if __name__ == "__main__":
    main()
