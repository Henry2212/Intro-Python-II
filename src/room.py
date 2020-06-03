# Implement a class to hold room information. This should have name and
# description attributes.from item import Item
from typing import List

class Room:
   class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

    def get_name(self):
        return f"{self.name}"

    def get_description(self):
        return f"{self.description}"