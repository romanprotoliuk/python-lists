from locale import currency


class Node: 
  # constructor
  def __init__(self,data,next):
      self.data = data
      self.next = next
  def __str__(self): # tells python how to print this node 
    return str(self.data) 

class LinkedList: 
  # constructor 
  def __init__(self):
      self.head = None
      self.tail = None
      self.size = 0

  def __str__(self):
    if self.size == 0:
      return '[]'
    
    current = self.head 
    result = str(current) # result is the string version of current 
    while current.next: # while there exists a next node 
      result += f', {str(current.next)}'
      current = current.next 
    return f'[{result}]'

  # returns length of list 
  def __len__(self):
    return self.size

  # same as append 
  def insert_end(self, data):
    if self.size == 0: 
      self.head = Node(data, None)
      self.tail = self.head
    else: 
      # new_node = Node(data, None)
      # self.tail.next = new_node
      # self.tail = new_node
      temp = self.tail
      self.tail = Node(data, None) # Creates new node and assigns it to tail 
      temp.next = self.tail # set the old tail to point to new tail 
    self.size += 1

  def remove(self, data):
    if self.size == 0: # case 1, empty list
      return 'List is already empty.'
    elif self.size == 1:
      if self.head.data == data:
        self.head = None
        self.tail = None
        self.size = 0
      else:
        return 'Item not found'
    else: # case 3, 2+ nodes in the list
      if self.head.data == data: # delete the head 
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.size -= 1
      else: # delete anything ohter than the head
        current = self.head
        while current.next:
          if current.next.data == data: # we've found the node to be deleted  
            node_to_delete = current.next
            current.next = node_to_delete.next
            node_to_delete.next = None
            if current.next is None:
              self.size -= 1
          else: # continue the loop because we did'nt fint it yet
            current = current.next 
      return 'Item is not found' # finished loop, didn't find it 

my_list = LinkedList()
my_list.insert_end('Taylor')
my_list.insert_end('Jason')
my_list.insert_end('April')
my_list.insert_end('Weston')
my_list.remove('Jason')
print(my_list)