"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #1 (25 points)
Filename: shoppers.py

An item has an item code (e.g. "ABCD-1234"), a name (e.g. "Silky Camisole"), 
and a price (e.g. $24). 
A partially completed item class has been provided to you below. You must 
complete the class by making the following enhancements:
- Write accessors for all fields.
- Two items are considered equal if they have the same item code.
- Items should be capable of being used with hashing data structures.
- The string representation of an item is its its code, name, and price
  seperated by commmas in a parenthesis, e.g. "(ABCD-1234, Silky Camisole, 24)"
- Items can be sorted based on the item code.
Write down the manual test by creating at least two items.
"""

class Item:
    __slots__ = ["__code", "__name", "__price"]

    def __init__(self, code, name, price):
        self.__code = code
        self.__name = name
        self.__price = price
    
    def get_code(self):
        return self.__code
    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    
    def __eq__(self, other):
        if type(self) == type(other):
            return self.__code == other.__code
        else:
            raise TypeError("Cannot compare Item with non-Item")
    
    def __hash__(self):
        return hash((self.__code, self.__name, self.__price))
    
    def __repr__(self):
        return f"({self.__code}, {self.__name}, {self.__price})"
    def __str__(self):
        return f"({self.__code}, {self.__name}, {self.__price})"

# manual test from main() method

#Test V sort function
def sort_by_code(item):
    return item.get_code()

def main():
    item1 = Item("FTAW-5231", "Apple", 5)
    item2 = Item("GPRL-1985", "Grape", 3)
    item3 = Item("FTAW-5231", "Evil Apple", 10)

    #Test I
    print("Test I")
    print(item1.get_code())
    print(item1.get_name())
    print(item1.get_price())
    print()
    #Test II
    print("Test II")
    print(item1 == item2) #Should be False
    print(item1 == item3) #Should be True
    print()
    #Test III
    print("Test III")
    new_set = set()
    new_set.add(item1)
    new_set.add(item2)
    print(new_set)
    print(item1 in new_set) #Should be True
    print(item3 in new_set) #Should be False
    print()
    #Test IV
    print("Test IV")
    print(item1)
    print(str(item1))
    print()
    #Test V
    print("Test V")
    list_to_sort = [item1, item2, item3]
    print(list_to_sort) #Unsorted list
    print(sorted(list_to_sort, key=sort_by_code)) #Sorted list



if __name__ == "__main__":    main()