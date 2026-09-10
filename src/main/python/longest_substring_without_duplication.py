#time : o(n)
#space: o(min(n,a))  , n= number of letters, a= number of unique letters
def longestSubstringWithoutDuplication(string):
    # Write your code here.
    lastseen={}
    longest=[0,1]
    startIdx=0
    for i,char in enumerate(string):
        print (lastseen)
        if char in lastseen:
            startIdx = max(startIdx,lastseen[char]+1)

        if longest[1] - longest[0] < i+1 - startIdx:
            longest = [startIdx, i+1]
        lastseen[char]=i
    return string[longest[0]:longest[1]]

print (longestSubstringWithoutDuplication("GEEKSFORGEEKS"))

