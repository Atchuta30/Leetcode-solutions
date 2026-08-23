class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = {}
        list1 = {}
        list2 = {}

        currentl1 = l1
        currentl2 = l2
        
        n1 = 0
        while currentl1 is not None:
            list1[n1] = currentl1.val
            currentl1 = currentl1.next
            n1 = n1 + 1

        n2 = 0
        while currentl2 is not None:
            list2[n2] = currentl2.val
            currentl2 = currentl2.next
            n2 = n2 + 1

        lenl1 = len(list1)
        lenl2 = len(list2)
        
       
        max_len = max(lenl1, lenl2)
        carry = 0

        for i in range(max_len):

            val1 = list1.get(i, 0)
            val2 = list2.get(i, 0)
            
            digsum = val1 + val2 + carry
            
            if digsum < 10:
                output[i] = digsum
                carry = 0
            else:
                output[i] = digsum % 10
                carry = 1
                
        if carry > 0:
            output[max_len] = carry

        dummy = ListNode(0)
        current = dummy

      
        for val in output.values():
            current.next = ListNode(val)  
            current = current.next           

        return dummy.next 
