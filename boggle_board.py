import random # https://www.w3schools.com/python/module_random.asp
import string  # https://www.geeksforgeeks.org/python/python-string-module/ (gives us A–Z in uppercase)

class BoggleBoard:

    def __init__(self):
        self.line1 = ["_", "_", "_", "_"]
        self.line2 = ["_", "_", "_", "_"]
        self.line3 = ["_", "_", "_", "_"]
        self.line4 = ["_", "_", "_", "_"]

    def shake(self):
        # https://www.w3schools.com/python/module_random.asp
        # https://www.geeksforgeeks.org/python/python-string-module/ (gives us A–Z in uppercase)
        # https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
        # ------------------------------------------------------------------
        # self.line1 = [new_value for item in old_list]
        # replaces
        # ------------------------------------------------------------------
        # new_list = []
        # for _ in self.line1:
        #     new_list.append(random.choice(string.ascii_uppercase))
        # self.line1 = new_list
        # ------------------------------------------------------------------
        self.line1 = [random.choice(string.ascii_uppercase) for _ in self.line1] # [new_value for item in old_list]
        self.line2 = [random.choice(string.ascii_uppercase) for _ in self.line2] # https://www.analyticsvidhya.com/blog/2024/01/role-of-underscore-in-python/?utm_source=chatgpt.com
        self.line3 = [random.choice(string.ascii_uppercase) for _ in self.line3] # underscore _ is used, conventionally, as a placeholder variable name for the current item being looped.
        self.line4 = [random.choice(string.ascii_uppercase) for _ in self.line4]

    def __str__(self):
        return (
            " ".join(self.line1) + "\n" + # https://www.w3schools.com/python/ref_string_join.asp
            " ".join(self.line2) + "\n" + # https://www.w3schools.com/python/gloss_python_escape_characters.asp
            " ".join(self.line3) + "\n" +
            " ".join(self.line4)
        )

boggleboard1 = BoggleBoard()
print(boggleboard1)
boggleboard1.shake()
print(boggleboard1)