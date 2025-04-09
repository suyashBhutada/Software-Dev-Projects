class ExamRoom():
    def __init__(self, n: int):
        self.sitting = [0]*n
        self.seats = n

    def seat(self) -> int:
        nearestAray = [0] * self.seats
        if(sum(self.sitting) == 0):
            self.sitting[0] = 1
            return 0
        for seatIndex in range(0,self.seats):
            if self.sitting[seatIndex]:
                break
            
        for i in range(0, self.seats):
            if(i <= seatIndex):
                nearestAray[i] = seatIndex-i
                continue
            if self.sitting[i]:
                nearestAray[i] = 0
            else:
                nearestAray[i] = nearestAray[i-1] +1
            
        
        for bSeatIndex in range(self.seats-1, seatIndex,-1):
            if self.sitting[bSeatIndex]:
                break
        
        if self.sitting[bSeatIndex]:
            for i in range(self.seats-1, seatIndex,-1):
                if(i >= bSeatIndex):
                    nearestAray[i] = min(nearestAray[i], i-bSeatIndex)
                    continue
                if self.sitting[i]:
                    nearestAray[i] = 0
                else:
                    nearestAray[i] = min(nearestAray[i],nearestAray[i+1] +1)
        
        minval = max(nearestAray)
        print(nearestAray)
        for i,v in enumerate(nearestAray):
            if(v == minval):
                self.sitting[i] = 1
                return i
        

    def leave(self, p: int) -> None:
        self.sitting[p] = 0
        
e = ExamRoom(4)
print(e.seat(), "\n\n")
print(e.seat(), "\n\n")

print(e.seat(), "\n\n")

print(e.seat(), "\n\n")

print(e.leave(1))

print(e.leave(3))

print(e.seat(), "\n\n")

