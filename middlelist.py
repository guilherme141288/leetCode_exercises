
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
    
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        return slow

instance = Solution()
print (instance.middleNode(head))