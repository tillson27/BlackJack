class Card():


    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value}"

    def get_value(self):
        list = self.value.split()
        if list[0] == "Two":
            return 2
        elif list[0] == "Three":
            return 3
        elif list[0] == "Four":
            return 4
        elif list[0] == "Five":
            return 5
        elif list[0] == "Six":
            return 6
        elif list[0] == "Seven":
            return 7
        elif list[0] == "Eight":
            return 8
        elif list[0] == "Nine":
            return 9
        elif list[0] == "King" or list[0] == "Queen" or list[0] == "Jack" or list[0] == "Ten":
            return 10
        else:
            return 0
        print(list)

card = Card(value = "Seven of Clubs")
print(card.get_value())
