#python
#!/usr/bin/python3
# Filename: 
import requests
import json 
from structs import ProductStorie
from structs import TaskStruct
class zentao_api(object):
    def __init__(self,url,account,pwd):
        # 禅道API地址
        self.zentao_url = url +"/zentao/api.php/v1"
        # 禅道登录账号和密码
        self.account = account
        self.password = pwd 
        self.GetToken() 
        self.GetDirctProjects()
        self.GetDirctProducts()
        self.this_storises=[]
        self.dict_storie_id_ = dict()
        self.last_stroie_id_=-1 

    def GetToken(self):
        body = {"account":self.account, "password": self.password} 
        url = self.zentao_url + "/tokens"
        res = requests.post(url=url, json=body)#参数传递需用json格式，否则返回{‘error’: ‘登录失败，请检查您的用户名或密码是否填写正确。’} 
        self.token = (res.json())['token']
#        print("Token:"+self.token)
        return self.token 

    def PostInfo(self,type,body):
        url=self.zentao_url +"/"+ type
        header = {"token":self.token}
        res = requests.post(url=url,headers=header,json=body)  
        return res.json()   

    def GetInfo(self,type,body):
        url=self.zentao_url +"/"+ type
        header = {"token":self.token}
        res = requests.get(url=url,headers=header,json=body) 
        return res.json()

#   获取项目 直接使用数据字典          
    def GetDirctProjects(self):
        res=self.GetInfo("projects?limit=500","")
        self.product_dict=dict()
        for x in res["projects"]:
            self.product_dict[x["id"]]=x["name"]
#            print("id:%d name:%s" % (x["id"],x["name"]))

#   获取产品 直接使用数据字典
    def GetDirctProducts(self):
        res=self.GetInfo("products?limit=1000","")
        self.product_dict=dict()
        for x in res["products"]:
            self.product_dict[x["id"]]=x["name"]
            print("id:%d name:%s" % (x["id"],x["name"]))

    def GetProductId(self,product_name):
        for item in self.product_dict.items(): 
            if item[1]==product_name:
                return item[0]

#  执行ID
    def SetExecutionsId(self,exection_id):
        self.exection_id_= exection_id
#   设置产品ID
    def SetProductId(self,product_id):
        self.product_id_= product_id

    def IsAddedStorise(self,title,id=-1):
        if str(title)=="None":
            return False
        try:
            for x in self.dict_storie_id_:
                if x[0]==title:
                    return True
        except:
            pass    
        self.dict_storie_id_[title]=id
        return False


# 需求相关
#   创建需求
# 只能创建GM7的项目 ID为：482
    def CreateStories(self,ProductStorie):
        title = ProductStorie.title
        if str(title)=="None":
            return self.last_stroie_id_
        if self.IsAddedStorise(title):
            return self.dict_storie_id_[title]
        self.this_storises.append(title)
        body ={
            "title": title,
            "spec": ProductStorie.spec,
            "pri": ProductStorie.pri,
            "product": self.product_id_,
            "category": ProductStorie.category,
            "verify": ProductStorie.verify,
            "status": ProductStorie.status
        }   
        print(body)
        res = self.PostInfo("stories",body) 
        print(res)
        try:
            id = res["id"]
            self.dict_storie_id_[title]=id
            self.last_stroie_id_=id
            return id
        except:
            return -1

#   删除需求
    def DeleteStories(self):
        for x in range(4853,4900):
            url=self.zentao_url +"/stories/"+ str(x)
            header = {"token":self.token}
            res = requests.delete(url=url,headers=header) 
            print(str(x) +"delete result:"+res.json()["message"])

# 创建任务
    def CreateTask(self,task_info):
        body ={
            "name": str(task_info.name),
            "type": str(task_info.type),
            "story": task_info.story,
            "assignedTo": [str(task_info.assignedTo)],
            "pri": task_info.pri,
            "estimate": str(task_info.estimate),
            "estStarted": str(task_info.estStarted),
            "deadline": str(task_info.deadline),
        }   
        url = "executions/"+str(self.exection_id_)+"/tasks" 
        print(body)
        res = self.PostInfo(url,body) 
        try:
            return res["id"]
        except:
            print("CreateTask fail!name:%s  assignedTo:%s res:%s" 
                %(task_info.name,task_info.assignedTo,res))
            return -1

#   删除任务
    def DeleteTask(self,index_s,index_e):
        for x in range(index_s,index_e):
            url=self.zentao_url +"/tasks/"+ str(x)
            header = {"token":self.token}
            res = requests.delete(url=url,headers=header) 
            print(str(x) +"delete result:"+res.json()["message"])


if __name__ == "__main__":
    cli = zentao_api("http://zentao_url:8080",
    "test",
    "word") 
    cli.SetProductId(266)
    cli.SetExecutionsId(402)
    productStorie=ProductStorie("代码测试需求",
    "代码测试",
    266,
    1,
    "feature"
    ,"验收标注"
    ,"active") 
#    productStorie = ProductStorie()
#    productStorie.title = "代码测试需求2" 
#    productStorie.spec = "代码测试描述2"
#    productStorie.product = 266
#    productStorie.pri = 1
#    productStorie.category = "feature"
#    productStorie.verify = "代码验收"
    id = cli.CreateStories(productStorie)
#    print(id)


#    taskStruct = TaskStruct(
#        "测试任务名称2","devel",402,4878,"maruijiang",1,22.5,
#        "2021-12-01","2021-12-31",""
#    )
#    id2=cli.CreateTask(taskStruct)
##    print(id2)
#    cli.DeleteTask(8495,8500)
    cli.DeleteStories()
