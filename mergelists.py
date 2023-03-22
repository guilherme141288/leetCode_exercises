
from typing import Optional

list1 = [1,2,4]
list2 = [1,3,4]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:



        merged_list = list1 + list2  # merge the two lists
        merged_list.sort()  # sort the merged list in increasing order
        return merged_list
    
instance = Solution()
print (instance.mergeTwoLists(ListNode (list1 ,ListNode (list2))))