from tkinter import Tk, Button, Entry, Label, Text, DISABLED, NORMAL, END
from tkinter.messagebox import showinfo

class LinkedListNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def potato_game(n, k):
    if n < 1:
        return -1
    if n == 1:
        return 0

    head = LinkedListNode(0)
    cur = head
    for i in range(1, n):
        cur.next = LinkedListNode(i)
        cur = cur.next

    cur.next = head

    cur = head
    while cur.next != cur:
        for _ in range(k - 2):
            cur = cur.next

        print(f"{cur.next.value} is eliminated")
        cur.next = cur.next.next
        cur = cur.next

    return cur.value


class PotatoGame: #GUI Application for the game
    def __init__(self, master):
        self.master = master
        master.title('Potato Game')

        self.label_n = Label(master, text='N (Number of player):')
        self.label_n.pack()

        self.entry_n = Entry(master)
        self.entry_n.pack()

        self.label_k = Label(master, text='K (Count to eliminate):')
        self.label_k.pack()

        self.entry_k = Entry(master)
        self.entry_k.pack()

        self.start_button = Button(master, text='Start', command=self.start_game)
        self.start_button.pack()

        self.eliminate_button = Button(master, text='Eliminate', command=self.eliminate_player, state=DISABLED)
        self.eliminate_button.pack()

        self.text_widget = Text(master, height= 10, width=50)
        self.text_widget.pack()

        self.players = []
        self.current_player = None

    def input(self): #Input fot n and k
        try:
            n = int(self.entry_n.get())
            k = int(self.entry_k.get())
            if n<2 or n>=12 or k<=1:
                raise ValueError
            return n, k
        except ValueError: #Pop up windows if the input values not satisfy
            showinfo(message='Invalid Input')
            showinfo(message='Please enter valid N (1<N<12) and K (K>1) values.')
            return None

    def start_game(self):
        values = self.input()
        if values is None:
            return
        n, self.k = values #Turn k into a var so can be access thoughout the entire class instance
        self.players = list(range(n))
        self.text_widget.insert('end', f'Game started. N = {n} K = {self.k}\n')
        self.current_player = 0
        self.eliminate_button['state'] = NORMAL # set the eliminate button state as active to use

    def eliminate_player(self):
        if len(self.players) > 1:
            self.current_player = (self.current_player + self.k - 1) % len(self.players)
            eliminated = self.players.pop(self.current_player)
            self.text_widget.insert(END, f'Player {eliminated} eliminated.\n') # Text widget to show which player got eliminated
            if len(self.players) == 1:
                self.display_winner()
        else:
            self.display_winner()

    def display_winner(self):
        winner = self.players[0]
        showinfo(message=f'The winner is player {winner}')
        self.text_widget.delete(1.0, END) #Clear all the text widget varilble that displayed
        self.eliminate_button['state'] = DISABLED #Disable eliminate button when show winner

if __name__ == '__main__':
    root = Tk()
    app = PotatoGame(root)
    root.mainloop()