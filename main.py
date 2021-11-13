# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
class Cell:
    def __init__(self, is_living):
        self.is_living = is_living

    def update_state(self, neighbours):
        self.is_living = False
        if neighbours == 2:
            self.is_living = True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
