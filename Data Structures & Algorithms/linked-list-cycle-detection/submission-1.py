# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        tail = head
        while tail:
            if tail in visited:
                return True
            else:
                visited.add(tail)
                tail = tail.next
        
        return False
        