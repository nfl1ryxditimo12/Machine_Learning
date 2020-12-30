import win32com.client

class CpStockCode:
    def __init__(self):
        self.stocks = {'유한양행':'A000100'}

    def GetCount(self):
        return len(self.stocks)

    def NameToCode(self, name):
        return self.stocks[name]

instCpStockCode = CpStockCode()

print(instCpStockCode.GetCount())
print(instCpStockCode.NameToCode('유한양행'))

# explore = win32com.client.Dispatch("InternetExplorer.Application")
# explore.Visible = True
#
# word = win32com.client.Dispatch("Word.Application")
# word.Visible = True

# excel = win32com.client.Dispatch("Excel.Application")
# excel.Visible = True
#
# wb = excel.Workbooks.Add()
# ws = wb.Worksheets("Sheet1")
# ws.Cells(1, 1).Value = "hello world"
# wb.SaveAs('c:\\Users\\rlatj\\Desktop\\test.xlsx')
# excel.Quit()

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

wb = excel.Workbooks.Open('C:\\Users\\rlatj\\Desktop\\input.xlsx')
ws = wb.ActiveSheet

ws.Cells(1, 2).Value = "is"
ws.Range("C1").Value = "good"
ws.Range("C1").Interior.ColorIndex = 10