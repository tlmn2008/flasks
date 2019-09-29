from flask import Flask, render_template, request
import time

app = Flask(__name__)

def write_file(teacher_name, result):
    with open('./data/{}_{}.txt'.format(teacher_name, time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))), 'w') as f:
        f.write(str(result))

@app.route('/investigation4TengQi/teacher-liu', methods=['GET', 'POST'])
def teacher_liu():
    if request.method == 'GET':
        return render_template('base.html')
    else:
        result = request.form.to_dict()
        print(request.form.to_dict())
        write_file('teacher_liu', result)
        return render_template("base.html")

@app.route('/investigation4TengQi/teacher-meng', methods=['GET', 'POST'])
def teacher_meng():
    if request.method == 'GET':
        return render_template('base.html')
    else:
        result = request.form.to_dict()
        print(request.form.to_dict())
        write_file('teacher_meng', result)
        return render_template("base.html")

@app.route('/investigation4TengQi/teacher-li', methods=['GET', 'POST'])
def teacher_li():
    if request.method == 'GET':
        return render_template('base.html')
    else:
        result = request.form.to_dict()
        print(request.form.to_dict())
        write_file('teacher_li', result)
        return render_template("base.html")

app.run(host='0.0.0.0', port='11234')



