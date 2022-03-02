# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists and len(lists) == 0:
            return None
        while len(lists)>1:
            
            merged_list = []
            for index in range(0,len(lists),2):
                l1 = lists[index]
                l2 = lists[index+1] if index+1 < len(lists) else None
                
                temp = self.merge_sort(l1,l2)
                merged_list.append(temp)
            lists = merged_list
        return lists[0]
    
    def merge_sort(self,l1,l2):
        temp = ListNode()
        curnode = temp
        
        while l1 and l2:
            if l1.val <= l2.val:
                curnode.next = l1
                l1 = l1.next
            else:
                curnode.next = l2
                l2 = l2.next
            curnode = curnode.next
            
        while l1:
            curnode.next = l1
            l1 = l1.next
            curnode = curnode.next
        
        while l2:
            curnode.next = l2
            l2 = l2.next
            curnode = curnode.next
        return temp.next
            
        