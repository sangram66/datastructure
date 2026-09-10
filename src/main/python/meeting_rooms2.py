'''
https://leetcode.com/problems/meeting-rooms-ii/
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
'''

'''
Time O(N log N), space O(N)

'''

class Solution:
    def minMeetingRooms(self, intervals) :
        times = []
        for start, end in intervals:
            times.append((start, 1))
            times.append((end, -1))
        print (sorted(times))
        rooms = max_rooms = 0        
        for _, indicator in sorted(times):
            rooms += indicator
            max_rooms = max(max_rooms, rooms)
            
        return max_rooms
    
print(Solution().minMeetingRooms(intervals = [[0,30],[5,10],[15,20]]))