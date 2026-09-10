'''
https://www.hackerrank.com/challenges/text-wrap/problem
important catch here is result in line 16 is printed .. so at the end of word seperation, last pass needs to be send to line 16 so that it get's printed and code ends,
else None will be printed
'''

def wrap(string, max_width):
    for i in range(0,len(string)+1,max_width):
        result=string[i:i+max_width]
        if len(result)==max_width:
            print (result)
        else:
            return (result)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print (result)