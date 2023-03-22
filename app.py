from flask import Flask, render_template

app = Flask(__name__)
print(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Lahore, Pakistan',
    'salary': 'Rs. 15,00,00'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Lahore, Pakistan',
    'salary': 'Rs. 25,00,000'
  },
  {
    'id': 3,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': '$100,000'
  },
]


@app.route("/")
def hello_worl():
  return render_template('home.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
