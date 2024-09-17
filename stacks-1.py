class Stack:
    def __init__(self):
        self.top = -1
        user_input = input("Choose between the options:\n1. Push \n2. Pop \n 3. Top \n 4. Size \n 5. Is Empty? \n 0. Exit")
        while (user_input != "0"):
            if (user_input == "1"):
                val = input("Enter a number")
                self.push(self, val)
            elif (user_input == "2"):
                self.pop(self)
            elif (user_input == "3"):
                self.top(self)
            elif (user_input == "4"):
                self.size(self)
            elif (user_input == "5"):
                self.is_empty(self)
            else:
                print("Invalid input try again")


    def push(value, self):
        self.top= self.top + 1
        self.value = value
        print("inserted " + self.value + " at " + self.top)

    def pop(self):
        print("removing "+ self.top + " element")
        self.top = self.top - 1

    def top(self):
        print(self.value)

    def size(self):
        print("Top: " + self.top + "\n")

    def is_empty(self):
        if (self.top == -1):
            print("Yes, stack is empty \n")
        else:
            print("No stack is not empty\n")
