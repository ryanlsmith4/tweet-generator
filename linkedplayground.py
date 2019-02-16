mylist = LinkedList()

mylist.append('a')
mylist.append('b')
mylist.append('c')

mylist.head.data  # => 'a'
mylist.tail.data  # => 'c'
mylist.find(lambda data: data > 'b')  # => 'c'
mylist.delete('a')
mylist.head.data  # => 'b'

print(mylist)
