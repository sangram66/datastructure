'''
https://www.hackerrank.com/challenges/merge-the-tools/problem

Sample Input
STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3
Sample Output
AB
CA
AD

'''
def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        temp=string[i:i+k]
        #print (temp)
        vis={}
        fin=''
        for u in range(len(temp)):
            #print (temp[u])
            if temp[u] not in vis:
                fin+=temp[u]
                #print (fin)
                vis[temp[u]]=u
            else:
                vis[temp[u]]=u
                #print (vis)
        print (fin)
                
            
        

if __name__ == '__main__':
    string, k = 'AABCAAADA',3
    merge_the_tools(string, k)
    