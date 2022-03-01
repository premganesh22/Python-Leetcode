class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_sort(lista,start,end,k):
            if start>end:
                return

            #Lumoto Algo
            pivot = lista[start]
            smaller = start
            for bigger in range(start+1,end+1):
                if lista[bigger] < pivot:
                    smaller+=1
                    lista[smaller],lista[bigger] = lista[bigger],lista[smaller]

            lista[start],lista[smaller] = lista[smaller],lista[start]
            if smaller == k:
                return lista[smaller]
            elif smaller > k:
                return quick_sort(lista,start,smaller-1,k)
            else:
                return quick_sort(lista,smaller+1,end,k)

        return quick_sort(nums,0,len(nums)-1,len(nums)-k)

        