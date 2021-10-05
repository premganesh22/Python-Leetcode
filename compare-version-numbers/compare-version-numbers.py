class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split('.')]
        v2 = [int(i) for i in version2.split('.')]
        for x in range(max(len(v1),len(v2))):
            ver1 = v1[x] if x < len(v1) else 0
            ver2 = v2[x] if x < len(v2) else 0
            if ver1 > ver2:
                return 1
            elif ver1 < ver2:
                return -1
        return 0
        