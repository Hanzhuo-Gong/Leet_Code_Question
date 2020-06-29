# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #Find out the length of the linked list
        current = head
        totalLength = 0
        while current:
            totalLength += 1
            current = current.next
            
        middlePoint = ceil(totalLength/2)
        
        #Return the middle node of the linked list
        result = head
        index = 0
        while index != middlePoint:
            result = result.next
            index += 1
        return result

