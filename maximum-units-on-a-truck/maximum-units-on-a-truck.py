class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        units = 0 
        size = 0
        for box,unit in boxTypes:
            if box+size <= truckSize:
                units+= box*unit
                size+=box
            else:
                units+= (truckSize-size)*unit
                return units
        return units
        