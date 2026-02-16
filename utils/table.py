# #1. The class Seat represents a seat in a larger system, perhaps for a theater, airplane, 
# or similar setting where each seat can be occupied or vacant.
class Seat:
# 2. Constructor (__init__ method):
# #The __init__ method is the constructor for the class, which runs when a new instance of 
# Seat is created.
#self.free = True: This sets the seat to be free when it's first created 
# (no one has occupied it).
#self.occupant = None: Initially, the seat has no occupant, so it is set to None.   
    def __init__(self):
        self.free = True  # Seat starts as free
        self.occupant = None  # No one occupies the seat initially
        
# 3.Method to Set an Occupant: set_occupant :
#This method allows you to set the occupant of the seat.
# It first checks if the seat is free (self.free is True). If so:
# It assigns the given name to self.occupant, indicating who is occupying the seat.
# It sets self.free to False, marking the seat as occupied.
#If the seat is already occupied (self.free is False), it raises an exception with the 
# message "Seat is already occupied.".
    def set_occupant(self, name):
        if self.free:
            self.occupant = name
            self.free = False
        else:
            raise Exception("Seat is already occupied.")
        
# 4) Method to Remove an Occupant: remove_occupant:
# This method allows you to remove an occupant from the seat.
# It first checks if the seat is occupied (self.free is False). If so:
# It stores the current occupant's name in occupant_name.
# It then sets self.occupant to None, indicating the seat is now unoccupied.
# It sets self.free back to True, making the seat available again.
# It returns the name of the person who was removed from the seat.
# If the seat is already empty (self.free is True), it raises an exception with the message "Seat is already empty.".
    def remove_occupant(self):
        if not self.free:
            occupant_name = self.occupant
            self.occupant = None
            self.free = True
            return occupant_name
        else:
            raise Exception("Seat is already empty.")

#Summary
#Seat is a class that models a seat with two properties: whether it's free and the occupant's name.
# set_occupant(name) assigns a person to the seat if it’s available.
# remove_occupant() removes the person from the seat if it’s occupied.
# Exceptions are raised if you try to assign an occupant to an already occupied seat or remove an occupant from an already empty seat.

class Table:
#1. __init__(self, capacity) method:
#This is the constructor for the Table class, which gets called when you create a new Table object.
# capacity: 
# This is the number of seats that the table can accommodate. 
# It is passed as an argument when you create a new table.
# self.seats: 
# This creates a list of Seat objects, where each Seat is initialized with Seat(). 
# The number of seats is equal to the capacity of the table.
# For example, if the capacity is 4, self.seats will be a list of 4 Seat objects: 
# [Seat(), Seat(), Seat(), Seat()].
    def __init__(self, capacity):
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]
 
#2. has_free_spot(self) method:
# This method checks if there are any free seats available at the table.
# any(seat.free for seat in self.seats): This is a Python generator expression that
# iterates through all the Seat objects in self.seats and checks whether the free attribute
# of any seat is True.

#seat.free: 
# Assumes that the Seat class has an attribute called free that is True if the seat is 
# unoccupied and False if it is occupied.
# If at least one seat is free, any() will return True, indicating that there is a free
# spot available. Otherwise, it will return False.   
    
    def has_free_spot(self):
        return any(seat.free for seat in self.seats)
    
#3. assign_seat(self, name) method:
#This method attempts to assign a seat to a person (given by their name).
# It loops over all the Seat objects in self.seats (using a for loop).
# For each seat, it checks if seat.free is True (i.e., the seat is unoccupied).
# If it finds a free seat, it calls seat.set_occupant(name), which presumably assigns 
# the name to the seat's occupant. (This assumes the Seat class has a method called 
# set_occupant that sets the name of the person sitting in the seat.)
# After assigning the seat, the method immediately returns True to indicate that the
# assignment was successful.
# If the loop finishes and no seat is found to be free (i.e., all seats are occupied), 
# it returns False, indicating that no seat was available.   
    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        return False
 # 4. left_capacity(self) method: 
 # This method calculates how many seats are still free at the table.
 # It uses a list comprehension to create a list of all the seats that are free (i.e., where seat.free is True). 
 # len([seat for seat in self.seats if seat.free]): 
# This counts the number of free seats by taking the length of the list created by the 
# list comprehension.
    def left_capacity(self):
        return len([seat for seat in self.seats if seat.free])
#Summary:
# The Table class manages a collection of Seat objects, keeping track of their capacity
# and the free/occupied status of each seat.
# Methods like has_free_spot() and assign_seat() provide functionality for checking 
# availability and assigning seats.
# The logic flows logically from creating a table with seats to checking seat availability,
# assigning seats, and counting free seats.