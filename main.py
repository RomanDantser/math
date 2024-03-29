import algorithms.kadane
import data_strucutres.linked_list as ll

# Some testing on linked list
'''
test = ll.LinkedList()
test.create_from_list([1, 2, 3, 4, 5])
print(test.length())
test.print_list()
test.insert_at_start(0)
test.print_list()
test.insert_after_value(3, 3.5)
test.print_list()
test.insert_after_value(6, 7)
test.delete_at_start()
test.print_list()
test.delete_node(3.5)
print(test.length())
test.print_list()
test.delete_node(1)
test.print_list()
test.delete_node(5)
test.print_list()
test.delete_node(6)
print(test.length())
test.reverse()
test.print_list()
test1 = ll.LinkedList()
test1.create_from_list([1,2,3,4,5,6,7,8,9,10])
test1.reverse()
test1.print_list()
'''
print(algorithms.kadane.max_subarray([-2,1,-3,4,-1,2,1,-5,4]))

