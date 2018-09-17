import numpy as np


class Person(object):
    """
    Base class for our player character
    """

    def __init__():
        self.hp = 100
        self.holding = []
        self.maxholding = 3

        self.on_fire = False
        self.tripped_alarm = False

    def pickup(self, object):
        if len(self.holding) < self.maxholding:
            self.holding.append(object)
            return True
        else:
            print("You can't carry anything more.")
            return False



class Room(object):
    """
    Base rooom class for the Space Game
    """
    def __init__():
        self.visited=0
        self.firsttext = ""
        self.text = ""
        self.name = "Generic Room"
        self.actions = {}
        self.inroom = {}

    def action(self,person,actionstring):
        self.actions[actionstring]

    def moveroom(self,roomstr):
        return "move", roomstr

    def pickup(self,person,objstring):
        if person.pickup(objstring):
            del self.inroom[objstring]



class CryoRoom(Room):
    """
    The Cryo Room (first room)
    """
    def __init__():
        # first grab all generic room setup items
        Room.__init__()
        self.firsttext = """BEEP BEEP BEEP. Is something backing up? No, wait. That's not the sound.
        That's an alarm klaxon. That's a bad sound. That's not what you want to
        hear when you're coming out of hypersleep. How long has it been beeping?
        How long have you been regaining consciousness?

        You stagger out of your pod, vaguely aware that someone was supposed to
        be there to help you get out of your tube. But nobody helped.
        Actually, there's nobody there. No movement. At all.

        You squint to shield yourself from the bright lights of the cryo chamber
        only to realize that there are no lights- just a blazing red light
        pulsing in time to the klaxon blaring at you. What happened?
        """
        self.text = """The Cryo room contains the sleeping crew of the Discovery. It contains a computer terminal,
        and has access to the medical bay at one end, and corridor 3B on the other end."""

        self.inroom = {"cryo computer": "The cryo computer sits on the far wall.",
                        "wrench": "There is a wrench lying on the floor.",
                        "lockers": "Crew lockers line the port wall of the room.",
                        "cryo tubes": "Cryo tubes line the starboard wall of the room. \nThey are all full, except for yours... and Captain Phillips'."
                        }
        self.actions = {"corridor 3B": self.moveroom(person,'corridor_3B'),
                        "medical bay": self.moveroom(person,'medical_bay'),
                        "lockers": self.lockers(person),
                        "tubes": self.tubes(person),
                        "computer": self.computer(person),
                        "wrench": self.pickup(person,'wrench')}
