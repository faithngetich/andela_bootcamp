class BinarySearch(list):
    def __init__(self, a, b, *args):#class constructor that creates list of elements
        list.__init__(self, *args)
        self.list_length = a
        self.step = b
        list_ending = self.list_length * self.step
        for x in range(self.step, list_ending + 1, self.step):
            self.append(x)

    #A function that returns the length of the list
    def length(self):
        return len(self)

     #A function that execute the binary search algorithim
    def search(self, item_in_list, first_value=0, last_value=None, val_interval=0):
        if not last_value:# reduces the length of the list by one
            last_value = self.length - 1
        elif item_in_list == self[first_value]:
            return {'index': first_value, 'count': val_interval}#returns a key value pair of the dictionary created
        elif item_in_list == self[last_value]:
            return {'index': last_value, 'count': val_interval}
        center_val = (first_value + last_value) // 2 #starts to split the list into two and checks the half in which the value is
        elif item_in_list == self[center_val]:#returns a key value pair if the item being searched is the middle item
            return {'index': center_val, 'count': val_interval}
        elif item_in_list > self[center_val]:
            first_value = center_val + 1
        elif item_in_list < self[center_val]:
            last_value = center_val - 1
        elif first_value >= last_value:
            return {'index': -1, 'count': val_interval}
        val_interval += 1
        else:
        	pass
        return self.search(item_in_list, first_value, last_value, val_interval)

