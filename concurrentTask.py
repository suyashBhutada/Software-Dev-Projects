import asyncio

class TaskRunner():
    def __init__(self, capacity):
        self.capacity = capacity
        self.taskQueue = []
        self._currentActive = 0
        
    async def execute(self,delay):
        self._currentActive += 1
        print("delay of ", delay, " secs")
        await asyncio.sleep(delay)
        self._currentActive -=1
        while(self.taskQueue):
            newDelay = self.taskQueue.pop(0)
            await self.execute(newDelay)
        return delay
    
    async def add(self,delay):
        if self._currentActive < self.capacity:
            return await self.execute(delay)
        else:
            self.taskQueue.append(delay)
        return 

        

async def main():
    mytask = TaskRunner(1)
    r = await asyncio.gather(mytask.add(7),mytask.add(1),mytask.add(1),mytask.add(1),mytask.add(1))
    await asyncio.sleep(2)
    r1 = await asyncio.create_task(mytask.add(1))

asyncio.run(main())