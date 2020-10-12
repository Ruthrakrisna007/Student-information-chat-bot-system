from connection import *



def stdSave(name,degree,phone,address):
	mycursor = conn.cursor()
	sql = "INSERT INTO student (name, degree,phone,address) VALUES (%s, %s, %s, %s)"
	val = (name,degree,phone,address)
	mycursor.execute(sql, val)
	conn.commit()
	
def insertInvaild(qus,date):
	mycursor = conn.cursor()
	sql = "INSERT INTO invaildquestion (question,date) VALUES (%s, %s)"
	val = (qus,date)
	mycursor.execute(sql, val)
	conn.commit()

	
def getInvaild():
	mycursor = conn.cursor()
	mycursor.execute("SELECT * FROM invaildquestion")
	myresult = mycursor.fetchall()
	return myresult
		
def getstudent():
	mycursor = conn.cursor()
	mycursor.execute("SELECT * FROM student")
	myresult = mycursor.fetchall()
	return myresult
	
def getLogin(username,passwrd):
	mycursor = conn.cursor()
	query="SELECT * FROM login where username='"+username+"'  and passwrd='"+passwrd+"' "
	print(query)
	mycursor.execute(query)
	myresult = mycursor.fetchall()
	#print("-------------------------"+myresult[0])
	for x in myresult:
		print(x)  
	return myresult
	
	
def newStudent(name,password,degree,year,rollnum):
	mycursor = conn.cursor()
	sql = "INSERT INTO student (name,password,degree,year,rollnum) VALUES (%s, %s, %s, %s, %s)"
	val = (name,password,degree,year,rollnum)
	mycursor.execute(sql, val)
	conn.commit()
	loginSave(rollnum,password,"student","active")
	
def newQuestion(name,visible,answer,date):
	name = name.lower()
	mycursor = conn.cursor()
	sql = "INSERT INTO question (name,visible,answer,date) VALUES (%s, %s, %s, %s)"
	val = (name,visible,answer,date)
	mycursor.execute(sql, val)
	conn.commit()
	
def getQuestions():
	mycursor = conn.cursor()
	mycursor.execute("SELECT * FROM question")
	myresult = mycursor.fetchall()
	return myresult

def loginSave(username,password,uRole,status):
	mycursor = conn.cursor()
	sql = "INSERT INTO login (username,passwrd,urole,status) VALUES (%s, %s, %s, %s)"
	val = (username,password,uRole,status)
	mycursor.execute(sql, val)
	conn.commit()

def getchat(msg):
	query=""
	mycursor = conn.cursor()
	msg = msg.lower()
	query = "select answer from question where name::text like '%"+msg+"%';"
	mycursor.execute(query)
	myresult = mycursor.fetchall()
	#print("-------------------------"+myresult[0])
	for x in myresult:
		print(x)  
	return myresult
	
def insertFeedback(name,email,message,date):
	mycursor = conn.cursor()
	sql = "INSERT INTO feedback (name,email,msg,date) VALUES (%s, %s, %s,%s)"
	val = (name,email,message,date)
	mycursor.execute(sql, val)
	conn.commit()

def getFeedback():
	mycursor = conn.cursor()
	mycursor.execute("SELECT * FROM feedback")
	myresult = mycursor.fetchall()
	return myresult
	
	
def insertParent(fname,lname,userId,email,username,password):
	mycursor = conn.cursor()
	sql = "INSERT INTO parent (fname,lname,userId,email,username) VALUES (%s, %s, %s,%s,%s)"
	val = (fname,lname,userId,email,username)
	mycursor.execute(sql, val)
	conn.commit()
	loginSave(username,password,"parent","active")
	
def getMyaccount(username):
	mycursor = conn.cursor()
	mycursor.execute("SELECT id,rollnum,degree,year FROM student where rollnum='"+username+"'")
	myresult = mycursor.fetchone()
	return myresult
	
def insertHoistory(username,qus,answer,date):
	print("----------answer----",answer)
	mycursor = conn.cursor()
	sql = "INSERT INTO history (username,qus,answer,date) VALUES (%s, %s, %s,%s)"
	val = (username,qus,answer,date)
	mycursor.execute(sql, val)
	conn.commit()
	
def getHistory(username):
	mycursor = conn.cursor()
	mycursor.execute("SELECT * FROM history where username='"+username+"'")
	myresult = mycursor.fetchall()
	return myresult
	
