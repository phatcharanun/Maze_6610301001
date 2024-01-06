import os
import keyboard
import time

class maze:
    def __init__(self) -> None:
        self.maze = [
                    ["X", "X", "X", "X", "X", "X", "X"],
                    ["X", " ", " ", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", " "],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", " ", " ", "X"],
                    ["X", " ", "X", "X", "X", "X", "X"],
                    ]
        self.ply = pos(5, 1)
        self.end = pos(2, 6)
        self.maze[self.ply.y][self.ply.x] = "B"
        self.maze[self.end.y][self.end.x] = "E"
    
    def isInBound(self, y, x):
        if y>=0 and x>=0 and y<len(self.maze) and x<len(self.maze[0]):
            return True
        else:
            return False
    
    def print(self):
        os.system("cls")
        print("\n\n\n")
        for row in self.maze:
            for col in row:
                print(col," ", end="")
            print("")
        print("\n\n\n")
    
    def printEND(self):
        os.system("cls")
        print("\n\n\n")
        print(">>>>> Congraturation!!! <<<<<")
        print("\n\n\n")
        keyboard.wait("")

    def move_up(self):
        next_move = pos(self.ply.y-1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "B"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True
    
    def move_down(self):
        next_move = pos(self.ply.y+1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "B"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_left(self):
        next_move = pos(self.ply.y, self.ply.x-1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "B"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_right(self):
        next_move = pos(self.ply.y, self.ply.x+1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "B"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

class pos:
    def __init__(self) -> None:
        self.y = None
        self.x = None
    
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

class Stack:

    def __init__(self):
        self._top = None
        self._size = 0

    def isEmpty(self):
        return self._top is None
    
    def __len__(self):
        return self._size
    
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._top.item

    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        node = self._top
        self._top = self._top.next
        self._size = self._size - 1
        return node.item

    def push(self, item):
        self._top = _StackNode(item, self._top)
        self._size = self._size + 1

class _StackNode:

    def __init__(self, item, link):
        self.item = item
        self.next = link

if __name__ == '__main__':

    m = maze()
    s = Stack()
    m.print()
    sn = _StackNode
    # m.move_up()
    #m.print()
    #s.push((m.ply.x,m.ply.y))
    
    # while True:
    #     if m.isInBound():
    while True:
        s.push((m.ply.y,m.ply.x))
        #m.move_up()
        # print(m.ply.x, m.ply.y)

        if m.maze[m.ply.y-1][m.ply.x] == " ":#เช้คตำแหน่ง
            m.move_up()
            a = s.peek()
            m.maze[a[0]][a[1]]= 'u'
           
            m.print()
            s.push((m.ply.y,m.ply.x))
            #m.maze[m.ply.y][m.ply.x]= 'O'
            
            m.print()

        
        # elif m.maze[m.ply.y-1][m.ply.x] == "X":
        #     m.move_down()
        #     m.print()
        # elif m.maze[m.ply.y][m.ply.x-1] == "X ":
        #             m.move_left()
        #             m.print()
        elif m.maze[m.ply.y][m.ply.x+1] == " " :
            m.move_right()
            a = s.peek()
            m.maze[a[0]][a[1]]= 'r'
            m.print()
        elif m.maze[m.ply.y-1][m.ply.x+1] == "X":
            m.move_down()
            a = s.peek()
            m.maze[a[0]][a[1]]= 'd'
            m.print() 
        elif m.maze[m.ply.y][m.ply.x-1] == "X ":
            m.move_left()
            a = s.peek()
            m.maze[a[0]][a[1]]= 'l'
            m.print()
        # elif m.maze[m.ply.y][m.ply.x] =="E" :
        #     m.printEND()


        