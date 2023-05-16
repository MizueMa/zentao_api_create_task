# zentao_api_create_task
# excel_deal 分析Excel中的任务，并筛选出自己关注的列
关注列：["项目名称",'需求', 
        '描述',
         '输出成果/验收标准', 
         '执行人',
         '优先级',
         "要求完成时间",
         "用户故事/任务",
         "初始规模",
         "计划完成时间"]
# structs关于禅道相关的结构体定义
禅道创建需求的状态不支持设置
`
# 需求结构

# title 需求名称 
# spec 需求描述
# product 需求所属产品  273
# pri 需求优先级 1为紧急  4为一般
# category 需求需求类型 
# --> feature 功能 | interface 接口 | performance 性能 | safe 安全 
# --> experience 体验 | improve 改进 | other 其他”
# verify 验收标准
class ProductStorie(object):
    def __init__(self
    ,title=""
    ,spec=""
    ,product=""
    ,pri=3
    ,category="feature"
    ,verify=""
    ,status=""):
        self.title = title      
        self.spec = spec
        self.product = product
        self.pri = pri
        self.category = category       
        self.verify = verify        
        # 状态(draft 草稿 | active 激活 | closed 已关闭 | changed 已变更) 无效
        self.status = status



#任务结构    

#      所属模块
# name 任务名称
# type任务类型 (design 设计 | devel 开发 | request 需求 | test 测试 | study 研究 | discuss 讨论 | ui 界面 | affair 事务 | misc 其他)
# executions_id 所属执行
# story 关联需求ID
# assignedTo 指派给
# pri 	优先级
# estimate 预计工时
# estStarted 	预计开始日期 "2021-12-01"
# deadline 预计结束日期 "2021-12-31"
# module  所属模块
class TaskStruct(object):
     def __init__(self
    ,name=""
    ,type="devel"
    ,executions_id=0
    ,story=0
    ,assignedTo=""
    ,pri=3
    ,estimate=""
    ,estStarted=""
    ,deadline=""
    ,module=""):
        self.name=name
        self.type=type
        self.executions_id=executions_id
        self.assignedTo=assignedTo
        self.story=story
        self.pri=pri
        self.estimate=estimate
        self.estStarted=estStarted
        self.deadline=deadline
        self.module=module    
`
# zentao_api禅道的API封装
1. 登录
2. 获取产品列表
3. 获取迭代执行列表
4. 创建需求
5. 创建任务
# main_pro 主体流程
`
读取Excel中的需求，并添加到禅道
读取excel中的执行，并添加到禅道
AppPersonInfo 筛选出excel中指定的人的任务   注意：这里的ABCD是登录禅道的账号  不是执行人
`
