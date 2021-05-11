# This class defines a package containing characteristics of a package
class package:
    def __init__(self, id, address, city, state, zip, deadline, mass, notes, timestamp):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
        self.timestamp = timestamp