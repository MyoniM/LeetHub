class Solution:
#     def mostPoints(self, questions: List[List[int]]) -> int:
#         maxPtsEarned = 0
#         visitedQuestions = {}
#         return self.getPointsEarned(0, questions, visitedQuestions)
    
#     def getPointsEarned(self, startIdx, questions, visitedQuestions):
#         if startIdx >= len(questions): return 0
#         key = self.getKey(questions, startIdx)

#         if key in visitedQuestions:
#             return visitedQuestions[key]
        
#         maxPtsEarned = 0
#         for i in range(startIdx, len(questions)):
#             question = questions[i]
#             possibleStartIdx = question[1] + i + 1
#             nextStartIdx = possibleStartIdx if possibleStartIdx < len(questions) else len(questions)
#             pointsEarned = question[0] + self.getPointsEarned(nextStartIdx, questions, visitedQuestions)
#             maxPtsEarned = max(maxPtsEarned, pointsEarned)
        
#         visitedQuestions[key] = maxPtsEarned
#         return visitedQuestions[key]
    
#     def getKey(self, questions, idx):
#         return '{}-{}-{}'.format(questions[idx][0], questions[idx][1], idx)

    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * (len(questions) + 1) 
        for i in range(len(questions) - 1, -1, -1):
            points, jump = questions[i][0], questions[i][1]
            dp[i] = max(points + dp[min(jump + i + 1, len(questions))], dp[i + 1])
        return dp[0];