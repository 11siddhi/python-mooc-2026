# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.shortest_height = 0
        self.person_dict = {}
    
    def add(self, person: Person):
        self.person_dict[person] = person.height
    
    def is_empty(self):
        return not self.person_dict
    
    def print_contents(self):
        if self.person_dict:
            print(f"There are {len(self.person_dict)} persons in the room, and their combined height is {sum(self.person_dict.values())} cm")
            for person in self.person_dict:
                print(f"{person.name} ({person.height} cm)")

    
    def shortest(self):
        if self.person_dict:
            shortest = min(self.person_dict.values())
            for person, height in self.person_dict.items():
                if height == shortest:
                    return person 
        return None

    def remove_shortest(self):
        if self.person_dict:
            shortest_person = self.shortest()
            self.person_dict.pop(self.shortest()) 
            return shortest_person
        return None

if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()      