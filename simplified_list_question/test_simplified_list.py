"""
Test Simlified List
"""

from simplified_list_question.simplified_list import SimplifiedList
from simplified_list_question.person import Person

my_list: SimplifiedList = SimplifiedList()
my_list[0] = 5
print(my_list)
my_list[1] = 6
print(my_list)

my_list2: SimplifiedList = SimplifiedList(Person)
my_list2[0] = 5
print(my_list2)
my_list2[1] = 6
print(my_list2)
