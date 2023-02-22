import openpyxl

#해당 루트에 있는 엑셀파일을 오픈하여 WB에 로드함
#WB = openpyxl.load_workbook("C:\Users\moonho.choi\PycharmProjects\python_exceltest\Test.xlsx")
WB = openpyxl.load_workbook("C:\Test.xlsx")

# WB에 로드한 엑셀 파일 내부에 있는 워크 시트 Test를 WS에 로드 함
WS = WB["Test"]

# 엑셀 워크쉬트 Test를 로드한 WS의 칼럼 B2에 문자 Test를 입력
WS["B2"] = "Choi Moon Ho"

# WB로 로드한 엑셀 쉬트를 다른 이름으로 저장
#WB.save("C:\Users\moonho.choi\PycharmProjects\python_exceltest\SaveTest.xlsx")
WB.save("C:\SaveTest.xlsx")

print("fdsfdsfdsfds"*10)
'test'.join