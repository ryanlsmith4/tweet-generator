#!python

from linkedlist import LinkedList

# n = # of key-value entries
# b = # of buckets
#     # entries     n
#  l =  ------- = -----
#     # buckets     b


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        n = Number of items in data structure
        Running time: O(n) Dependent on amount of buckets"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n) Dependent on amount of buckets?"""
        all_values = []
        # Loop through all buckets
        for bucket in self.buckets:
            # Loop through key, value in all buckets
            for key, value in bucket.items():
                # add value to bucket
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n) Dependent on amount of buckets"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(n) Dependent on amount of buckets"""
        size = 0
        # Loop through all buckets
        for bucket in self.buckets: # b # of buckets
        # Count number of key-value entries in each bucket
            size += bucket.size # O(l)
        return size
        # Overall O(b * l) ---> O(n)


    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(1) If it exist or not"""
        # Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        entry = bucket.find(lambda key_value: key_value[0])
        # Check if key-value entry exists in bucket
        if entry is not None:
            return True
        else:
            return False


    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: O(n) where n is the length of the specific bucket"""
        # Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Check if key-value entry exists in bucket
        entry = bucket.find(lambda key_value: key_value[0] == key) # O(l) with l = bucket.length()
        # If found, return value associated with given key
        if entry is not None: # FOUND
            return entry[1] # entry = (key,value)
        # Otherwise, raise error to tell user get failed
        else:
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: Best condition O(1) worst condition O(l) which is actually
        O(2l) but we drop constants in linear time"""
        # Find bucket where given key belongs
        index = self._bucket_index(key) #O(1)
        bucket = self.buckets[index] #O(1)
        entry = bucket.find(lambda key_value: key_value[0] == key) # O(l)
        # Check if key-value entry exists in bucket
        if entry is not None:
        # If found, update value associated with given key
            bucket.delete(entry) # remove old key,value pair to append later
        # Otherwise, insert given key-value entry into bucket
        entry = (key, value) #O(1)
        bucket.append(entry) #O(1)


    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: O(l) Because dropping constants  """
        # Find bucket where given key belongs
        index = self._bucket_index(key) # O(1)
        bucket = self.buckets[index] # O(1)
        # entry is a tuple found using linkedList method find
        entry = bucket.find(lambda key_value: key_value[0] == key) # O(l)
        #  Check if key-value entry exists in bucket
        if entry is not None:
            bucket.delete(entry) # O(l)
        # If found, delete entry associated with given key
        else:
        # Otherwise, raise error to tell user delete failed
            raise KeyError('Key not found: {}'.format(key))




def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10), ('X', 12), ('G', 33)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
