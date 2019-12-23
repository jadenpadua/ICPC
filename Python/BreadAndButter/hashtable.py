#HashMap Implentation
class HashMap:
    def __init__(self):
        self.size = 6 # sets the size of the array to store key index pairs
        self.map = [None] * self.size #Constructs a list that has a fixed length of none
    
    def _get_hash(self,key):
        hash = 0 #calculates and returns an index calculated by that key
        for char in str(key):
            hash += ord(char)
        return hash % self.size
    
    def add(self,key,value):
        key_hash = self._get_hash(key) #gets hash defined in method above
        key_value = [key, value] #basically a list of the key and valuer we passed in

        #check if that cell is empty or will have a collision
        if self.map[key_hash] is None:
            #if none then add to the index of key hash a list containing another list of the key_value variable
            self.map[key_hash] = list([key_value])
            return True
        else:
            #Case where the array is not empty, we need to check if the key is already existing
            for pair in self.map[key_hash]:
                #Checks if that key value pair is already in our hashtable, if it does match then simply update the value
                if pair[0] == key:
                    pair[1] == value
                    return True
            #if not currently existing, then append it to our index that already has a previous value
            self.map[key_hash].append(key_value)

    #get method gets the hash given the key, then locate the cell and finds value that matches that key then return it
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            #iterates through all our pairs in that index trying to find if pair[0] = key passed in
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    #Deletye a key value pair
    def delete(self, key):
        key_hash = self._get_hash(key)
        #If that index is not populated, then nothing to delete
        if self.map[key_hash] is None:
            return False
        # Iterates through length of hashmap checking if the key is equal
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                #pops item off of list
                self.map[key_hash].pop(i)
        return True

    def print(self):
        print('===PHONEBOOK===')
        for item in self.map:
            if item is not None:
                print(str(item))
