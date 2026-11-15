# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head,head
        
        while slow and fast:
            print(fast.val)
            print(slow.val)
            slow = slow.next
            fast = fast.next
            if not slow or not fast:
                return False
            fast = fast.next

            if slow and fast and slow == fast:
                return True
        return False
            

        
        