from flask import Flask,render_template,request
import psycopg2 #pip install psycopg2 
import psycopg2.extras
from psycopg2 import Error

app = Flask(__name__)
     
app.secret_key = "SRK_Enterprises"
      
DB_HOST = "localhost"
DB_NAME = "University"
DB_USER = "postgres"
DB_PASS = "postgre"
          
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/student")
def student():
    return render_template("Student.html")
  
@app.route("/studentquery1",methods=["POST","GET"])
def Squery1():
    try:
        if request.method == "POST":
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            user = request.form['depname']
            user2 = request.form['credits']
            title2 = 'Student ID, First Name, Department and Total Credits of Students in {} Department OR Total Credits less than {}.'.format(user, user2)
            cursor.execute("""SELECT s_ID,first_name,dept,total_credits FROM Student_T 
            WHERE dept = %(value1)s OR total_credits > %(value2)s""", {"value1": user, "value2": user2})
            employeelist = cursor.fetchall()
            return render_template("StudentOutput.html", value=employeelist, title2=title2, column3='Department', column4='Total Credits')

    except Exception as e:
        print(e)
    finally:
        cursor.close() 

@app.route("/studentquery2",methods=["POST","GET"])
def Squery2():
    try:
        if request.method == "POST":
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            user = request.form['year1']
            user2 = request.form['year2']
            title2 = 'Student ID, First Name, Last Name and Date of Birth of Students born between year {} AND year {}.'.format(user, user2)
            cursor.execute("""SELECT s_ID,first_name,last_name,DOB FROM Student_T WHERE EXTRACT(YEAR FROM DOB) > %(value1)s AND EXTRACT(YEAR FROM DOB) < %(value2)s""", {"value1": user, "value2": user2})
            employeelist = cursor.fetchall()
            return render_template("StudentOutput.html", value=employeelist, title2=title2, column3='Last Name', column4='Date of Birth')

    except Exception as e:
        print(e)
    finally:
        cursor.close() 

@app.route("/department")
def department():
    return render_template("Department.html")
  
@app.route("/departmentquery1",methods=["POST","GET"])
def Dquery1():
    try:
        if request.method == "POST":
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            user = request.form['depname']
            user2 = request.form['buildname']
            title2 = 'Department and Building name of {} department AND {} building.'.format(user, user2)           
            cursor.execute("""SELECT * FROM Department_T WHERE dept_name = %(value1)s AND building = %(value2)s""", {"value1": user, "value2": user2})
            employeelist = cursor.fetchall()
            return render_template("DepartmentOutput.html",title2=title2, value=employeelist)

    except Exception as e:
        print(e)

@app.route("/departmentquery2",methods=["POST","GET"])
def Dquery2():
    try:
        if request.method == "POST":
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            user = request.form['depname']
            user2 = request.form['buildname']
            title2 = 'Department and Building name of {} department OR {} building.'.format(user, user2)
            cursor.execute("""SELECT * FROM Department_T WHERE dept_name = %(value1)s OR building = %(value2)s""", {"value1": user, "value2": user2})
            employeelist = cursor.fetchall()
            return render_template("DepartmentOutput.html", title2=title2, value=employeelist)

    except Exception as e:
        print(e)

@app.route("/instructor")
def instructor():
    return render_template("Instructor.html")
  
@app.route("/instructorquery1",methods=["POST","GET"])
def Iquery1():
    try:
        if request.method == "POST":
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            user = request.form['lname']
            user2 = request.form['dob']
            title2 = 'Instructor ID, First Name, Last Name and Date of Birth of Instructors with Last name {} OR born before year {}.'.format(user, user2)
            cursor.execute("""SELECT * FROM Instructor_T WHERE last_name = %(value1)s OR EXTRACT(YEAR FROM DOB) < %(value2)s""", {"value1": user, "value2": user2})
            employeelist = cursor.fetchall()
            return render_template("InstructorOutput.html", title2=title2, value=employeelist)

    except Exception as e:
        print(e)

@app.route("/instructorquery2",methods=["POST","GET"])
def Iquery2():
    try:
        if request.method == "POST":
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            user = request.form['year1']
            user2 = request.form['year2']
            title2 = 'Instructor ID, First Name, Last Name and Date of Birth of Instructors born between year {} AND year {}.'.format(user, user2)
            cursor.execute("""SELECT * FROM Instructor_T WHERE EXTRACT(YEAR FROM DOB) > %(value1)s AND EXTRACT(YEAR FROM DOB) < %(value2)s""", {"value1": user, "value2": user2})
            employeelist = cursor.fetchall()
            return render_template("InstructorOutput.html", title2=title2 ,value=employeelist)

    except Exception as e:
        print(e)

@app.route("/permanent")
def permanent():
    return render_template("Permanent.html")
  
@app.route("/permanentquery1",methods=["POST","GET"])
def Pquery1():
    try:
        if request.method == "POST":
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            user = request.form['buildname']
            user2 = request.form['room']
            title2 = 'Instructors with office in {} building OR office room {}.'.format(user, user2)
            cursor.execute("""SELECT * FROM Permanent_T WHERE office_building = %(value1)s OR office_room = %(value2)s""", {"value1": user, "value2": user2})
            employeelist = cursor.fetchall()
            return render_template("PermanentOutput.html", title2=title2, value=employeelist)

    except Exception as e:
        print(e)

@app.route("/permanentquery2",methods=["POST","GET"])
def Pquery2():
    try:
        if request.method == "POST":
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            user = request.form['buildname']
            user2 = request.form['salary']
            title2 = 'Instructors with office in {} building OR salary greater than {}.'.format(user, user2)
            cursor.execute("""SELECT * FROM Permanent_T WHERE office_building = %(value1)s OR salary > %(value2)s""", {"value1": user, "value2": user2})
            employeelist = cursor.fetchall()
            return render_template("PermanentOutput.html", title2=title2, value=employeelist)

    except Exception as e:
        print(e)

@app.route("/visiting")
def visiting():
    return render_template("Visiting.html")
  
@app.route("/visitingquery1",methods=["POST","GET"])
def Vquery1():
    try:
        if request.method == "POST":
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            user = request.form['wage']
            title2 = 'Instructor ID with hourly wage less than ${}.'.format(user)
            cursor.execute("""SELECT * FROM Visiting_T WHERE hourly_wage < %(value1)s""", {"value1": user})
            employeelist = cursor.fetchall()
            return render_template("VisitingOutput.html", title2=title2, value=employeelist)

    except Exception as e:
        print(e)

@app.route("/visitingquery2",methods=["POST","GET"])
def Vquery2():
    try:
        if request.method == "POST":
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            user = request.form['wage']
            title2 = 'Instructor ID with hourly wage greater than ${}.'.format(user)
            cursor.execute("""SELECT * FROM Visiting_T WHERE hourly_wage > %(value1)s""", {"value1": user})
            employeelist = cursor.fetchall()
            return render_template("VisitingOutput.html", title2=title2, value=employeelist)

    except Exception as e:
        print(e)

@app.route("/complex")
def complex():
    return render_template("Complex.html")
  
@app.route("/complexquery1",methods=["POST","GET"])
def Cquery1():
    try:
        if request.method == "POST":
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            user = request.form['credits']
            user2 = request.form['buildname']
            title2 = 'Student ID, First Name, Department and Total Credits of Students with total credits more than {} AND have department in {} building.'.format(user, user2)
            cursor.execute("""SELECT S_ID, first_name, dept, total_credits FROM Student_T WHERE total_credits > %(value1)s AND dept IN 
            (SELECT dept_name FROM Department_T WHERE building = %(value2)s)""", {"value1": user, "value2": user2})
            employeelist = cursor.fetchall()
            return render_template("ComplexOutput.html", value=employeelist, title2=title2, column1 = 'Student ID',
            column2 = 'First Name', column3 = 'Department', column4 = 'Credits')

    except Exception as e:
        print(e)

@app.route("/complexquery2",methods=["POST","GET"])
def Cquery2():
    try:
        if request.method == "POST":
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            user = request.form['credits']
            if user=='max':
                title2 = 'Student ID, First Name, Department and Total Credits of Students with MAX credits in each department'
                cursor.execute("""SELECT S_ID, first_name, dept, total_credits AS max_credit_students FROM Student_T WHERE total_credits
                IN (SELECT MAX(total_credits) FROM Student_T GROUP BY dept)""", {"value1": user})
            elif user=='min':
                title2 = 'Student ID, First Name, Department and Total Credits of Students with MIN credits in each department'
                cursor.execute("""SELECT S_ID, first_name, dept, total_credits AS min_credit_students FROM Student_T WHERE total_credits
                IN (SELECT MIN(total_credits) FROM Student_T GROUP BY dept)""", {"value1": user})
            else:
                title2 = 'INVLAID INPUT !!!'
                return render_template("ComplexOutput.html",title2=title2)
            employeelist = cursor.fetchall()
            return render_template("ComplexOutput.html", value=employeelist, title2=title2, column1 = 'Student ID',
            column2 = 'First Name', column3 = 'Department', column4 = 'Credits')

    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
