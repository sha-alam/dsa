def knapsack(W, wt, val, n):
	dp = [0 for i in range(W+1)]
	for i in range(1, n+1):
		for w in range(W, 0, -1):
			if wt[i-1] <= w:
				dp[w] = max(dp[w], dp[w-wt[i-1]]+val[i-1])

	return dp[W]


p = [15, 25, 13, 23]
wo = [2, 6, 12, 9]
c = 20
no = 4
print(knapsack(c, wo, p, no))
