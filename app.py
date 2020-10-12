
from flask import Flask,request,url_for,redirect,flash,session
from flask import render_template
import json 
from service import *
from datetime import date 
app = Flask(__name__) 
 



@app.route("/")
def index():
	return render_template("index.html") 
	


@app.route("/about.html")
def  about():
	return render_template("/about.html") 
	
	

@app.route("/contact.html")
def contact():
	return render_template("contact.html") 
	
@app.route("/studentreg.html")
def studentreg():
	return render_template("studentreg.html") 
	
	

@app.route("/previous.html")
def previous():
	if 'username' in session:
		username=session['username']
		result=getHistory(username)
		return render_template("previous.html",data=result) 
			
@app.route("/myaccount.html")
def myaccount():
	if 'username' in session:
		username=session['username']
		result=getMyaccount(username)
		return render_template("myaccount.html",data=result) 
	
	
@app.route("/viewfeedback.html")
def viewfeedback():
	result=getFeedback()
	return render_template("viewfeedback.html",data=result) 




@app.route("/parentreg.html")
def parentreg():
	return render_template("parentreg.html") 
	
@app.route("/invalid_questions.html")
def invalid_questions():
	result=getInvaild()
	return render_template("invalid_questions.html",data=result) 

@app.route("/logout")
def logout():
	return redirect("/") 
	
@app.route("/admin_home.html")
def adminHome():
	return render_template("admin_home.html") 

@app.route("/feedback_from.html")
def feedback():
	return render_template("feedback_from.html") 
	

@app.route("/home.html")
def home():
	return render_template("home.html") 
	
@app.route("/userpage.html")
def userPage():
	return render_template("userpage.html") 


		
@app.route("/adminlogin.html")
def admin():
	return render_template("adminlogin.html") 




@app.route("/add_question.html")
def add_question():
	return render_template("add_question.html") 


@app.route("/addstudent.html")
def addstudentHtml():
	return render_template("addstudent.html") 
	
@app.route("/student_home.html")
def student_home():
	return render_template("student_home.html") 

@app.route("/studentlogin.html")
def studentlogin():
	return render_template("studentlogin.html") 




@app.route("/studentchatbot.html")
def studentchatbot():
	return render_template("studentchatbot.html") 
	
	



@app.route("/parentchatbot.html")
def parentchatbot():
	return render_template("parentchatbot.html") 
	
	
@app.route("/parentlogin.html")
def parentlogin():
	return render_template("parentlogin.html") 
	

@app.route("/parent_home.html")
def parent_home():
	return render_template("parent_home.html") 

@app.route("/asked_question.html",methods=['POST','GET'])
def asked_question():
	if request.method == "GET":
		result=getQuestions()
		return render_template("asked_question.html",data=result) 


@app.route("/adminlogin",methods=['POST','GET'])
def adminlogin():
	if request.method == "POST":
		username=request.form['username']
		passwrd=request.form['password']
		if username=="admin@gmail.com":
			if passwrd=="admin":
				session["user_id"]=1
				session["username"]="admin@gmail.com"
				session["role"]="admin"
				return redirect("/admin_home.html")				
		result=getLogin(username,passwrd)
		print(len(result))
		if(len(result)>0):	
			session["userObj"]=result
			for x in result:
				print(x)
				session["user_id"]=x[0]
				session["username"]=x[1]
				session["role"]=x[4]
				print("------------------------role-------"+x[2])
				if(x[4]=="admin"):
					return redirect("/admin_home.html")					
		return render_template("adminlogin.html",status="username or password is wrong")
	


@app.route("/studentLogin",methods=['POST','GET'])
def studentLogin():
	if request.method == "POST":
		username=request.form['username']
		passwrd=request.form['password']	
		result=getLogin(username,passwrd)
		print(len(result))
		if(len(result)>0):			
			session["userObj"]=result
			for x in result:
				print(x)
				session["user_id"]=x[0]
				session["username"]=x[1]
				session["role"]=x[4]
				print("------------------------role-------"+x[2])
			return redirect("/student_home.html")
								
		return render_template("studentlogin.html",status="username or password is wrong")
	


@app.route("/parentLogin",methods=['POST','GET'])
def parentLogin():
	if request.method == "POST":
		username=request.form['username']
		passwrd=request.form['password']	
		if username=="parent@gmail.com":
			if passwrd=="parent":
				session["user_id"]=1
				session["username"]="parent@gmail.com"
				session["role"]="parent"
				return redirect("/parent_home.html")		
		result=getLogin(username,passwrd)
		print(len(result))
		if(len(result)>0):			
			session["userObj"]=result
			for x in result:
				print(x)
				session["user_id"]=x[0]
				session["username"]=x[1]
				session["role"]=x[4]
				print("------------------------role-------"+x[2])
			return redirect("/parent_home.html")
								
		return render_template("parentlogin.html",status="username or password is wrong")
	



@app.route("/register",methods=['POST','GET'])
def addStudent():
	if request.method == "POST":
		name=request.form['name']		
		rollnum=request.form['rollnum']
		password=request.form['password']
		degree=request.form['degree']		
		year=request.form['year']
		newStudent(name,password,degree,year,rollnum)
	return redirect("/admin_home.html")


@app.route("/addQuestion",methods=['POST','GET'])
def addQuestion():
	if request.method == "POST":
		name=request.form['name']		
		visible=request.form['visible']
		answer=request.form['answer']
		newQuestion(name,visible,answer,date.today())
	return redirect("/admin_home.html")



@app.route("/StudentSave",methods=['POST','GET'])
def StudentSave():
	if request.method == "POST":
		name=request.form['name']
		degree=request.form['degree']
		phone=request.form['phone']
		address=request.form['address']
		stdSave(name,degree,phone,address)
	return render_template("index.html")
	

@app.route("/parentreg",methods=['POST','GET'])
def addParent():
	if request.method == "POST":
		fname=request.form['fname']
		lname=request.form['lname']
		userId=request.form['userId']
		email=request.form['email']
		username=request.form['username']
		password=request.form['password']
		insertParent(fname,lname,userId,email,username,password)
		return redirect("/")

@app.route("/getchat")
def query_example():
	if request.method == "GET":
		msg = request.args.get('msg')
		data=getchat(msg)
		return json.dumps({'result':data});

@app.route("/feedBack",methods=['POST','GET'])
def feedBack():
	if request.method == "POST":
		name=request.form['name']
		email=request.form['email']
		message=request.form['message']
		insertFeedback(name,email,message,date.today())
		return redirect("/feedback_from.html")
	return redirect("/")
				
		
@app.route("/invaildQus")
def addInvaild():
	if request.method == "GET":
		qus = request.args.get('question')
		if insertInvaild(qus,date.today()):
			return json.dumps({'result':True});
		return json.dumps({'result':False});

@app.route("/studentget",methods=['POST','GET'])
def studentget():
	result = None
	if request.method == "GET":
		result=getstudent()
	
	return json.dumps({'result':result});
	

@app.route("/stuHistory")
def stuHistory():
	if request.method == "GET":
		if 'username' in session:
			username=session['username']
			qus = request.args['question']
			answer = request.args['answer']			
			insertHoistory(username,qus,answer,date.today())
			return json.dumps({'result':True});
		return json.dumps({'result':False});


if __name__=="__main__":
	app.secret_key = "abc"  
	app.run(debug=True)
