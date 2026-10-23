# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeLists(self, l1, l2):
        dummy = ListNode(0)
        head = dummy

        while l1 and l2:
            valOne = l1.val
            valTwo = l2.val

            if valOne <= valTwo:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        
        if l1:
            head.next = l1
        else:
            head.next = l2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                listOne = lists[i]
                listTwo = lists[i + 1] if i + 1 < len(lists) else None
                merged = self.mergeLists(listOne, listTwo)
                mergedLists.append(merged)

            lists = mergedLists 
        return lists[0]

    