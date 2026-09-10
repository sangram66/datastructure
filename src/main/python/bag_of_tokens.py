''''
https://leetcode.com/problems/bag-of-tokens/description/
948. Bag of Tokens
Solved
Medium

Topics
conpanies icon
Companies
You start with an initial power of power, an initial score of 0, and a bag of tokens given as an integer array tokens, where each tokens[i] denotes the value of tokeni.

Your goal is to maximize the total score by strategically playing these tokens. In one move, you can play an unplayed token in one of the two ways (but not both for the same token):

Face-up: If your current power is at least tokens[i], you may play tokeni, losing tokens[i] power and gaining 1 score.
Face-down: If your current score is at least 1, you may play tokeni, gaining tokens[i] power and losing 1 score.
Return the maximum possible score you can achieve after playing any number of tokens.
'''

class Solution:
    def bag_of_tokens(self, tokens, power):
        res=score=0
        l,r=0,len(tokens)-1

        while l<=r:
            if power>= tokens[l]:
                power-=tokens[l]
                score+=1
                res=max(res,score)
                l+=1
            elif score>0:
                power+=tokens[r]
                score-=1
                r-=1
            else:
                break
        return res

tokens = [100,200,300,400]
power = 200
print (Solution().bag_of_tokens(tokens,power))


