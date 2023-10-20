from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Python Developer',
    'location': 'New York',
    'salary': '$100,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'San Francisco',
    'salary': '$120,000'
  },
  {
    'id': 3,
    'title': 'Software Engineer',
    'location': 'Chicago'
    
  },
  {
    'id': 4,
    'title': 'Data Analyst',
    'location': 'Los Angeles',
    'salary': '$90,000'
  }
]

@app.route('/')
def hello_world():
  return render_template("home.html",
                         jobs = JOBS,
                        comp_name = "Amazing")

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)



if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True, port=8080)
