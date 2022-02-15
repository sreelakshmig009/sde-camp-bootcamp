# combinations sum 1 - leetcode
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        for index in range(len(candidates)):
            if target - candidates[index] == 0:
                answer.append([candidates[index]])
            elif target - candidates[index] >= min(candidates[index:]):
                for i in self.combinationSum(candidates[index:], target - candidates[index]):
                    answer.append([candidates[index]] + i)
        return answer