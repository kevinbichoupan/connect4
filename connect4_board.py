


class Connect4():
    def __init__(self):
        self.position = []
        self.rows = 6
        self.columns = 7
        
    def check_for_available_slots(self):
        available_slots = []
        for i in range(1,7):
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
        
        row_check = [[],[],[],[],[],[]]
        column_check = [[],[],[],[],[],[],[]]
        #diagonal check

        for i in range(0,len(self.position)):
            marker = 'A' if i % 2 == 0 else 'B'
            column_check[self.position[i]].append(marker)
        
        for column in column_check:
            for row in range(0,len(column)):
                row_check[row].append(column[row])

        print(row_check)
        print(column_check)

    def execute_turn(self, position):
        self.place_marker(self, position)
        self.check_for_winner()

a = Connect4()
for i in [1, 2, 3, 4, 1, 2, 3, 4]:
    a.place_marker(i)
a.check_for_winner()