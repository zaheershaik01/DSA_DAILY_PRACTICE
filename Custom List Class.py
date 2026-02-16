import ctypes

class CustomList:
    def __init__(self):
        initialCapacity = 1
        self.capacity = initialCapacity
        self.size = 0
        self.array = self.__create_array(self.capacity)

    def __create_array(self, capacity):
        # Create a new referential array with given capacity
        return (capacity * ctypes.py_object)()
    
    def __resize(self, new_capacity):
        new_array = self.__create_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array                  ## Replace the old array
        self.capacity = new_capacity
    
    def append(self, item):
        if (self.size == self.capacity):
            self.__resize(2 * self.capacity)

        self.array[self.size] = item
        self.size += 1

    def __len__(self):
        return self.size
    
    def __str__(self):
        output = ''
        for i in range(self.size):
            output = output + str(self.array[i]) + ','

        return '[' + output[:-1] + ']'
    
    def pop(self):
        if(self.size == 0):
            return ('Empty List, IndexError: pop from empty list')
        
        popped_item = self.array[self.size-1]
        self.size = self.size - 1
        return popped_item
    

myList = CustomList()
myList.append(1)
myList.append(2)

print(myList)
print(myList.pop())
print(myList)
print(myList.pop())
print(myList)
print(myList.pop())