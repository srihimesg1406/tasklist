import psycopg2
db_name = "TasklistDB"
db_user = "tasklist_user"
db_pw = "welcome1"
db_host= "localhost"

def getTaskList():
    conn = psycopg2. connect(dbname=db_name, user=db_user, password=db_pw, host=db_host)
    cur = conn.cursor()
    cur.execute('SELECT task_name, is_active FROM public."TaskList"')
    tasklist = cur.fetchall()
    cur.close
    conn.close
    return tasklist