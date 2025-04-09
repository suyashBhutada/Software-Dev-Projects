class ExcelSheet():
    # assuming only 26 columns
    def __init__(self):
        self.numRows  = 1
        self.valueMap = dict()
        self.impactingMap = dict()
        for id in range(65,91):
            self.valueMap[chr(id)] = dict()
            self.impactingMap[chr(id)] = dict()
    
    def setCellValue(self, row: int, col: str,value: int):
        self.valueMap[col][row] = value
        if(self.impactingMap[col] or len(self.impactingMap[col][row])):
            raise Exception("Sorry, not supported yet")

    def getCellValue(self, row: int, col: str):
        return self.valueMap[col][row]

    print

