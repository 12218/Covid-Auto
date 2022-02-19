import sqlite3
import time
from datetime import date, timedelta
import covid

cx = sqlite3.connect("./db.sqlite3")

cu = cx.cursor()

cu.execute("select * from task_task where on_or_off = 1")
task_data = cu.fetchall() # 读数据库取出数据

cu.execute("select * from task_info")
user_data = cu.fetchall()

for data in task_data:
    # print(data)
    for user in user_data:
        if data[5] == user[10]:
            # print(user, data)
            task_title = data[2]
            task_province = data[3]
            task_city = data[4]
            task_coordinate = data[6]
            task_username = user[1]
            task_stu_id = user[2]
            task_phone = user[3]
            task_institution = user[4]
            task_form_id = user[5]

            vjuid = user[6]
            vjvd = user[7]
            vt = user[8]
            UUkey = user[9]

            task = covid.post(task_province, task_city, task_coordinate, task_username,
                task_stu_id, task_phone, task_institution, task_form_id,
                vjuid, vjvd, vt, UUkey)
            status_code = task.locate()
            print(task.task_username, task.clock_in()['m'], task.data['riqi'], task.data['tiwen'], task.data['tiwen1'], task.data['tiwen2'], '定位:' + status_code)

# for data in user_data:
#     print(data)