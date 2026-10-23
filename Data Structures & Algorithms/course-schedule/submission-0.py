class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visitSet = set()
        
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            else:
                visitSet.add(crs)
                for pre in preMap[crs]:
                    if not dfs(pre): return False
                visitSet.remove(crs)
                preMap[crs] = []
                return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True