# -*- coding:utf-8 -*-
import json
import numpy as np
import pymysql

HOST = '172.16.4.22'
USER = 'root'
PASSWORD = 'jcinfo@1995-2018'
DB = 'jcCrawler'
PORT = 3306

conn = pymysql.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    db=DB,
    port=PORT,
    charset="utf8")

def insertKeywords(key, words_group):
    try:
        conn.connect()
        conn.ping()
        cursor = conn.cursor()
        sql = 'insert into keywords(keyword, synonyms) VALUES (%s, %s)'
        cursor.execute(sql,[key, words_group])
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        return False

def updateKeywords(id, key, words_group):
    try:
        conn.connect()
        conn.ping()
        cursor = conn.cursor()
        sql = "update keywords set keyword=%s,synonyms=%s where id=%s"
        cursor.execute(sql, (key, words_group, id))
        rowCount = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()

        if(rowCount > 0):
            return True
        else:
            return False
    except Exception as e:
        return False

def deleteKeywords(id):
    try:
        conn.connect()
        conn.ping()
        cursor = conn.cursor()
        sql = 'delete from keywords where id =%s'
        cursor.execute(sql,id)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        return False

def getAllKeywords():
    returnData = []
    try:
        conn.connect()
        cursor = conn.cursor()
        sql = 'select id, keyword, synonyms from keywords'
        cursor.execute(sql)
        result = cursor.fetchall()
        for id, keyword, synonyms in result:
            try:
                wArr = json.loads(synonyms, encoding='utf-8')
                cross = []
                group = []
                groupLen = len(wArr[0].split(" "))
                for w in wArr:
                    cross.append(w.split(" "))
                npArr = np.array(cross)

                for i in range(groupLen):
                    item = list(set(npArr.T[i]))
                    group.append(' '.join(item))

                returnData.append({"id":id, "keyword":keyword, "group":group})

            except Exception as e:
                returnData.append({"id":id, "keyword":keyword, "group":""})
                # returnData.append((id, keyword, []))
                print(e)
    except Exception as e:
        print(e)
    return returnData

# if __name__ == '__main__':
#     data = getAllKeywords()
#     pass

