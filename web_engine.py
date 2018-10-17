# -*- encoding:utf-8 -*-
import itertools
import json
import dataUtil
from bottle import static_file, request
from bottle import route
from bottle import view

@route('/')
def index():
    return static_file("index.html", root='./web/static/html')

# 图片访问地址
@route('/img/<filename>')
def get_img(filename):
    return static_file(filename,root='./web/static/img')
# css访问地址
@route('/static/bootstrap/css/<filename>')
def bt_css(filename):
    return static_file(filename,root='./web/static/bootstrap/css')
# js访问地址
@route('/static/bootstrap/js/<filename>')
def bt_js(filename):
    return static_file(filename,root='./web/static/bootstrap/js')
# fonts访问地址
@route('/static/bootstrap/fonts/<filename>')
def bt_fonts(filename):
    return static_file(filename,root='./web/static/bootstrap/fonts')
# css 访问地址
@route('/static/assets/css/<filename>')
def assets_css(filename):
    return static_file(filename,root='./web/static/assets/css')
# js 访问地址
@route('/static/assets/js/<filename>')
def assets_js(filename):
    return static_file(filename,root='./web/static/assets/js')

@route('/import_keywords', method='POST')
def importKeywords():
    key = request.forms.get('key')
    key = key.strip()
    words_group = request.forms.get('words_group')
    words_group = words_group.strip()

    returnData = {"status": False, "msg":""}
    if (key == '') | (words_group == ''):
        returnData['status'] = False
        returnData['msg'] = '代表词或关键词组为空'
    else:
        lines = words_group.split("\n")
        allData = [[w.strip() for w in line.split(" ") if w.strip() != ''] for line in lines]
        allData = [data for data in allData if len(data) > 0]
        words = [' '.join(item) for item in itertools.product(*allData)]
        wordsStr = json.dumps(words)

        status = dataUtil.insertKeywords(key, wordsStr)

        if not status:
            returnData['msg'] = '数据插入失败，请检查数据库配置'
        else:
            returnData['status'] = True
            returnData['msg'] = '数据插入成功'

    return returnData

@route('/show')
@view('web/views/show')
def show():
    data = dataUtil.getAllKeywords()
    return {"data":data}

@route('/delete', method="POST")
def deleteKeywords():
    returnData = {"status": False}
    id = request.forms.get('id')
    try:
        id = int(id)
        if(dataUtil.deleteKeywords(id)):
            returnData["status"] = True
    except Exception as e:
        print(e)

    return returnData

@route('/update', method='POST')
def updateData():
    returnData = {"status": False}
    id = request.forms.get('id')
    keyword = request.forms.get("keyword")
    group = request.forms.get("group")
    try:
        id = int(id)
        if (keyword == '') | (group == ''):
            returnData['status'] = False
            returnData['msg'] = '代表词或关键词组为空'
        else:
            lines = group.split("\n")
            allData = [[w.strip() for w in line.split(" ") if w.strip() != ''] for line in lines]
            allData = [data for data in allData if len(data) > 0]
            words = [' '.join(item) for item in itertools.product(*allData)]
            wordsStr = json.dumps(words)

            status = dataUtil.updateKeywords(id, keyword, wordsStr)

            if not status:
                returnData['msg'] = '数据更新失败'
            else:
                returnData['status'] = True
                returnData['msg'] = '数据更新成功'
    except Exception as e:
        print(e)

    return returnData

@route("/product")
def showCross():
    a = []

    allKeywords = dataUtil.getAllKeywords()
    data = [item for id, keyword, group in allKeywords  for item in group]


