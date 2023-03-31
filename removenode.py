from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 2


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize two pointers
        first_ptr = second_ptr = head
        
        # Move second_ptr n nodes ahead of first_ptr
        for i in range(n):
            second_ptr = second_ptr.next
        
        # If second_ptr reaches the end of the linked list,
        # remove the head of the linked list
        if second_ptr is None:
            return head.next
        
        # Move both pointers together until second_ptr reaches the end
        while second_ptr.next is not None:
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next
        
        # Remove the nth node from the end
        first_ptr.next = first_ptr.next.next
        
        return head
    
instance = Solution()
print (instance.removeNthFromEnd(head , n))
