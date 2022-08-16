"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emps = {emp.id: emp for emp in employees}
        res = [0]
        def dfs(ids):
            res[0] += emps[ids].importance
            for subordinate in emps[ids].subordinates:
                dfs(subordinate)
            return res[0]
        return dfs(id)