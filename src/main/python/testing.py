# def validparenthesis(string):
#     open="[{("
#     close="]})"
#     pairs={"}":"{","]":"[",")":"("}
#     stack =[]
#     for char in string:
#         if char in open:
#             stack.append(char)
#         elif char in close:
#             if len(stack)==0:
#                 return False
#             elif stack[-1]== pairs[char]:
#                 stack.pop()
#             else :
#                 False
#     return len(stack)==0
#
# print (validparenthesis("[([])]"))

class solution():
    def twosum(self,arr,tgt):
        vis={}
        res=[]
        for i in arr:
            diff = tgt - i
            if diff in vis:
                res.append([i,diff])
            else:
                vis[i]=i
        print (vis)

        return (res)

a = [2,15,1,7]
t = 9
print(solution().twosum(a,t))





