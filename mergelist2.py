from typing import Optional



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))        

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # initialize the result linked list
        dummy = ListNode(0)
        tail = dummy
        
        # merge the two lists
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # append the remaining nodes from list1 or list2
        tail.next = list1 or list2
        
        # return the result linked list
        return dummy.next
    
instance = Solution()
print (instance.mergeTwoLists(list1 , list2))    