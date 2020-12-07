#https://www.acmicpc.net/problem/1309

def main(n):
	dp = [1,1,1]
	for _ in range(n-1):
		tmp = [(dp[1]+dp[2])%9901, (dp[0]+dp[2]%9901), (dp[0]+dp[1]+dp[2])%9901]
		dp = tmp
	print(sum(dp)%9901)
	
if __name__ == '__main__':
    main(int(input()))
