from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

majors = ["Computer Science", "Mathematics", "Chemistry", "Biology", "History", "Telecom Engineering", "Civil Engineering", "Computer Engineering", "Geomatic Engineering", "Material Engineering"]
courses = {
    "Computer Science": ["CS101", "CS102", "CS203", "CS256", "CS321"],
    "Mathematics": ["MATH101", "MATH102", "MATH251", "MATH261", "MATH270"],
    "Chemistry": ["CHEM103", "CHEM213", "CHEM224", "CHEM256", "CHEM261"],
    "Biology": ["BIO112", "BIO212", "BIO222", "BIO312", "BIO322", "BIO361"],
    "History": ["HIST101", "HIST111", "HIST121", "HIST221", "HIST311", "HIST321"],
    "Telecom Engineering": ["TE101", "TE102", "TE201", "TE301", "TE302"],
    "Civil Engineering": ["CE101", "CE102", "CE201", "CE301", "CE302"],
    "Computer Engineering": ["CPE101", "CPE102", "CPE201", "CPE301", "CPE302"],
    "Geomatic Engineering": ["GE101", "GE102", "GE201", "GE301", "GE302"],
    "Material Engineering": ["ME101", "ME102", "ME201", "ME301", "ME302"]
}

selected_major = None
available_courses = None
selected_courses = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    email = request.form['email']
    # Save user info to database (REMOVED. Try adding the analytics)
    return redirect(url_for('main'))

@app.route('/main', methods=['GET', 'POST'])
def main():
    global selected_major, available_courses, selected_courses
    if request.method == 'POST':
        selected_major = request.form['major']
        available_courses = courses.get(selected_major, [])
        selected_courses = []
    return render_template('main.html', majors=majors, available_courses=available_courses, selected_major=selected_major, selected_courses=selected_courses)

@app.route('/select_major', methods=['POST'])
def select_major():
    global selected_major, available_courses
    selected_major = request.form['major']
    available_courses = courses.get(selected_major, [])
    return redirect(url_for('main'))

@app.route('/add_courses', methods=['POST'])
def add_courses():
    global selected_courses
    course = request.form['course']
    if course in available_courses and course not in selected_courses:
        selected_courses.append(course)
    return redirect(url_for('main'))

@app.route('/submit_courses', methods=['POST'])
def submit_courses():
    return redirect(url_for('congrats'))

@app.route('/congrats')
def congrats():
    global selected_courses
    return render_template('congrats.html', selected_courses=selected_courses)

if __name__ == "__main__":
    app.run(debug=True)
