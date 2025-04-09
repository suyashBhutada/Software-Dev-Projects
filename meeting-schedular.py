from datetime import *
import bisect


class Person():
    def __init__(self, emailId):
        self.emailId = emailId
        pass

class Meeting():
    def __init__(self,s:datetime,e:datetime,attendees:list[Person]):
        self.startTime = s
        self.endTime = e
        self.attendees = attendees

class MeetingRoom():
    def __init__(self, roomID,capacity):
        self.roomID = roomID
        self.capacity = capacity
        self.calendar = []# list of Meetings
        pass

    def isMeetingRoomEmpty(self,s:datetime,e:datetime) -> bool:
        def getStartTime(x:Meeting):
            return x.startTime
        self.calendar.sort(key=getStartTime)
        temp = [x.startTime for x in self.calendar]
        indexToPlace = bisect.bisect(temp, s)
        if(indexToPlace >0):
            if(self.calendar[indexToPlace-1].endTime>s):
                return -1
        if(indexToPlace < len(self.calendar)):
            if(self.calendar[indexToPlace].startTime<e):
                return -1
        return indexToPlace



class MeetingSchedular():
    def __init__(self,meetingRooms:list[MeetingRoom]):
        self.meetingRooms = meetingRooms
        pass
    
    def addMeetingRoom(self,meetingRoom:MeetingRoom):
        self.meetingRooms.append(meetingRoom)
        return
    
    def scheduleMeeting(self,s:datetime,e:datetime,atendees:list[Person]):
        if(len(atendees) == 0):
            return True
        for room in self.meetingRooms:
            if(room.capacity >= len(atendees)):
                if room.isMeetingRoomEmpty(s,e):
                    currentMeeting = Meeting(s,e,atendees)
                    room.calendar.append(currentMeeting)
                    #sendNotification with Room and s,e here
                    return True
        return False
                

from collections import defaultdict
def best(x):
    if(len(x) == 0):
        return 0
    dp = []
    dp.append(1)
    for i in range(1,len(x)):
        if x[i] == x[i-1]:
            dp.append(dp[i-1])
        else:
            dp.append(dp[i-1] + 1)
    print(dp)
    return(max(dp))


from itertools import combinations
def re(wood):
    wood.sort()
    sin = defaultdict(int)
    d = defaultdict(int)
    maxFreq = 0
    max_val = -1
    for i in range(0,len(wood)):
        sin[wood[i]] += 1
        if(sin[wood[i]] + d[wood[i]]>maxFreq):
            maxFreq = sin[wood[i]] + d[wood[i]]
            max_val = wood[i]
    used =set()

    for i in range(0,len(wood)):
        for j in range(i+1, len(wood)):
            #i is maxFreq
            if(i not in used and j not in used and wood[i] + wood[j]  == max_val):
                used.add(i)
                used.add(j)
                temp = wood[i] + wood[j]
                d[temp] +=1
                maxFreq +=1
    print(sin)
    print(d, "\n")
    return maxFreq

print(re([8,13,7,13,5,13,4,13,6,13]))




