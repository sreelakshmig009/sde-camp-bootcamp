# combination sum 2 - leetcode
def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        dp = [set() for _ in range(target + 1)]
        dp[0].add(())

        for candidate in candidates:
            for i in range(target, candidate - 1, -1):
                dp[i].update((*comb, candidate) for comb in dp[i - candidate])

        return dp[-1]