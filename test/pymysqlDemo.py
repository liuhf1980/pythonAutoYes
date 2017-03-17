import pymysql.cursors
con = pymysql.connect(host='172.168.101.85',port=3306,user='ces',passwd='WY68Yud',db='yws',charset='utf8')
cur = con.cursor()
cur.execute("select *  from crm_student  where name ='1对1排课测试小时'")
con.commit()
con.close()