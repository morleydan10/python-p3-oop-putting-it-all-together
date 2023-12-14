#!/usr/bin/env python3

class Shoe:

    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
    
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        self._brand = brand
        print(f"Brand: {brand}")
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
            print(f"Size: {size}")
        else:
            print("size must be an integer")

# can add an attribute to a class through a method ⬇️

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")



stan_smith = Shoe("Adidas", 9)
# condition = Shoe(condition = "New")

