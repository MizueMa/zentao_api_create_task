#python
#!/usr/bin/python3
# Filename: 

from excel_deal import  excel_deal
from zentao_api import zentao_api
from structs import ProductStorie
from structs import TaskStruct
import sys
class AppPersonInfo(object):
    def __init__(self) -> None:
        self.assigned_pre_=""
        self.assigned_list_=["A","B","C","D","E"]
        pass
    def IsAppAuth(self,name):
        for x in self.assigned_list_:
            if x==name:
                return True
        return False
    def GetRightAssigne(self,name):
        msg = str(name)
        if msg!="None":
            self.assigned_pre_=msg
        return self.assigned_pre_
    def GetEstimate(self,estimate):
        estimat = str(estimate).replace("h","")
        return float(estimat)


if __name__ == "__main__": 
    person=AppPersonInfo()
#禅道信息   
    zentao_ = zentao_api("http://zentao_url:8080",
    "test",
    "pwd") 
    zentao_.SetExecutionsId(550)
    zentao_.SetProductId(71)
    ProName = "装置"
#EXCEL信息
    pro = ProductStorie()
    taskStruct = TaskStruct()
    exlce_ = excel_deal("月度需求计划-5月") 
       
    for x in range(1,exlce_.GetExcelRowsNum()):
        bResult,pro,taskStruct = exlce_.GetNextRow() 
        if bResult and pro.product==ProName : 
            taskStruct.assignedTo = person.GetRightAssigne(taskStruct.assignedTo)
            if person.IsAppAuth(taskStruct.assignedTo):
                taskStruct.estimate = person.GetEstimate(taskStruct.estimate)
                print("满足需求 x=%d pro.title = %s;taskStruct:name %s ;assignedTo:%s GetEstimate:%f" 
                   % (x,pro.title,taskStruct.name,taskStruct.assignedTo,taskStruct.estimate))
                id = zentao_.CreateStories(pro)
                taskStruct.story =  id 
                zentao_.CreateTask(taskStruct)
                  
