# This class defines the hashtable which stores all of the packages
class hashtable:
    
    # Initialize the hash table of size 40 with empty bucket list entries
    def __init__(self, initial_capacity=40):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Complexity is O(1)
    # Hash function for determining which bucket to insert item
    def hash(self, key):
    
        return int(key) % len(self.table)

    # Complexity is O(1)
    # Stores a key pair value into table using hash function
    def insert(self, key, item):

        hashpair = item
        bucket_list = self.table[self.hash(key)]

        bucket_list.append(hashpair)

    # Complexity is O(1)
    # Returns a package given a key
    def get_package(self, key):
        
        bucket = hash(key)
        if self.table[hash(key)] != None:
            return self.table[bucket][0]
        else:
            return None

    # Complexity is O(1)
    # Updates a package with new value given key
    def update(self, key, value):

        bucket = self.hash(key)
        if self.table[bucket] != None:
            self.table[bucket][0] = value

    # Complexity is O(1)
    # Removes a package given a key
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        if key in bucket_list:
            bucket_list.remove(key)
    
    # Complexity is O(1)
    # Returns a package given a key
    def lookup(self, key):
        
        bucket = self.hash(key)
        if self.table[bucket] != None:
           
            return self.table[bucket][0]
        else:
            return None