#!/usr/bin/python3
# Filename: structs.py
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

    