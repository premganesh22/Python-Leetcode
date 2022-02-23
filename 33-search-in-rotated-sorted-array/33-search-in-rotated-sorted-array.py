class Solution:
    def search(self, lista: List[int], key: int) -> int:
            start = 0
            end = len(lista)-1
            while start <= end:

                mid = start + (end-start)//2
                if lista[mid] == key:
                    return mid

                #Left Portion
                if lista[start] <= lista[mid]:
                    if lista[mid] < key or lista[start] > key:
                        start = mid+1
                    else:
                        end = mid-1

                #Right Portion
                else:
                    if lista[mid] > key or lista[end] < key:
                        end = mid-1
                    else:
                        start = mid+1
            return -1
