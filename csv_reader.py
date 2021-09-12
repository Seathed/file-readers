class CSVFile:
    def __init__(self):
        self._headers = []
        self._data = []
        self._noColumns = 0
        self._noRows = 0

    def processCSVLine(line):
        tokens = []
        tokens = line.split(',')
        for i in range(len(tokens)):
            tokens[i] = tokens[i].strip()
            if(tokens[i][0] == "\""):
                print("OH OH")
                
        return tokens

    def readCSV(self, fileName):
        csv = open(fileName, 'r')
        self._headers = CSVFile.processCSVLine(csv.readline())

        for line in csv:
            self._data.append(CSVFile.processCSVLine(line))

        self._noColumns = len(self._headers)
        self._noRows = len(self._data)

    def getHeader(self, column):
        if(column < 1 or column > self._noColumns):
            return None
        column = column - 1
        return(self._headers[column])

    def getCell(self, column, row):
        if(column < 1 or row < 1 or column > self._noColumns or row > self._noRows):
            return None
        column = column - 1
        row = row - 1
        data = self._data
        return(data[row][column])

    def setCell(self, column, row, newData):
        if(column < 1 or row < 1 or column > self._noColumns or row > self._noRows):
            return None
        column = column - 1
        row = row - 1
        data = self._data
        data[row][column] = newData
        return(data[row][column])

    def getNoColumns(self):
        return self._noColumns

    def addRow(self, string):
        self._data.append(CSVFile.processCSVLine(string))

    def removeRow(self, row):
        if(row < 1 or row > self._noRows):
            del self._data[-1]
        else:
            row = row - 1
            del self._data[row]

    def writeToFile(self, fileName):
        fileName = fileName + ".csv"
        valid = False
        try:
            f = open(fileName, 'r')
        except:
            valid = True
            pass
        
        if(not valid):
            exit("File already exists")

        f = open(fileName, "a+")
        
        for i in range(len(self._headers)):
            if(i == len(self._headers) - 1):
                f.write(self._headers[i])
            else:
                f.write(self._headers[i] + ", ")
        f.write("\n")

        for datarow in self._data:
            for i in range(len(datarow)):
                if(i == len(datarow) - 1):
                    f.write(datarow[i])
                else:
                    f.write(datarow[i] + ", ")

            if(datarow != self._data[-1]):
                f.write("\n")

        f.close()

    def getNoRows(self):
        return self._noRows
    
    def printHeaders(self):
        for i in range(len(self._headers)):
            if(i == len(self._headers) - 1):
                print(self._headers[i])
            else:
                print(self._headers[i], end=", ")

    def printData(self):
        for datarow in self._data:
            for i in range(len(datarow)):
                if(i == len(datarow) - 1):
                    print(datarow[i], end=" ")
                else:
                    print(datarow[i], end=", ")
            print()

# Testing Driver
csv_file = CSVFile()
csv_file.readCSV("csvfile.csv")
#csv_file.printHeaders()
#csv_file.printData()
#print("Columns: ", csv_file.getNoColumns(), ", Rows: ", csv_file.getNoRows(), sep="")
#print(csv_file.getHeader(1))
#print(csv_file.getCell(2, 10))
csv_file.addRow("c11, 11")
csv_file.removeRow(11)
csv_file.writeToFile("new-csv")