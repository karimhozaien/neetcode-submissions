# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while slow and fast:
            print(slow.val)
            print(fast.val)
            slow = slow.next
            fast = fast.next.next
            if not fast or not slow:
                return False
            if slow.val == fast.val:
                return True

        