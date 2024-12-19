
class Connect4Logic():
    def __init__(self):
        self.position = []
        self.rows = 6
        self.columns = 7
        self.has_winner = False
        self.winner = None
        
    def check_for_available_slots(self):
        available_slots = []
        for i in range(1,8):
            if self.position.count(i) < 6:
                available_slots.append(i)
        return available_slots

    def place_marker(self, position):
        if position in self.check_for_available_slots():
            self.position.append(position)
        else:
            raise ValueError('Illegal move')

    def check_for_winner(self):
        # create list of sequences that show the rows, columns, and diagnals of the board
        # search each of the list of sequences for 4 consecutive markers 
        
        row_check = ['', '', '', '', '', '']
        column_check = ['', '', '', '', '', '', '']

        for i in range(0,len(self.position)):
            marker = 'A' if i % 2 == 0 else 'B'
            column_check[self.position[i] - 1] += marker
        
        for i in range(0,7):
            column_check[i] = column_check[i].ljust(6,'O')

        for column in column_check:
            for row in range(0,len(column)):
                row_check[row] += column[row]


        for i in row_check:
            if 'AAAA' in i:
                self.has_winner = True
                return 'A'
            if 'BBBB' in i:
                self.has_winner = True
                return 'B'

        for i in column_check:
            if 'AAAA' in i:
                self.has_winner = True
                return 'A'
            if 'BBBB' in i:
                self.has_winner = True
                return 'B'

        for i in range(0,4):
            for j in range(0,3):
                try:
                    if column_check[i][j] == column_check[i+1][j+1] == column_check[i+2][j+2] == column_check[i+3][j+3] != 'O':
                        self.has_winner = True
                        return column_check[i][j]
                    if column_check[i][6-j] == column_check[i+1][6-(j+1)] == column_check[i+2][6-(j+2)] == column_check[i+3][6-(j+3)] != 'O':
                        self.has_winner = True
                        return column_check[i][6-j]
                except:
                    pass

    def execute_turn(self, position):
        self.place_marker(position)
        self.winner = self.check_for_winner()


