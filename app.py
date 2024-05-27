from flask import Flask,render_template,jsonify


app=Flask(__name__)
JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru,India',
    'salary':'Rs.10,00,000',
  },
  {
    'id':1,
    'title':'Data Scintist',
    'location':'London,U.k',
    'salary':'£.15,00,000',
  },
    {
    'id':3,
    'title':'Frontened Engineer',
    'location':'Delhi,India',
    # 'salary':'Rs.9,00,000',
  },
  {
    'id':1,
    'title':'Backned Engineer',
    'location':'Dishpur,India',
    'salary':'Rs.12,00,000',
  }


]


@app.route("/")
def hello():
  return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_job():
  return jsonify(JOBS)

if __name__=="__main__":
  app.run(host="0.0.0.0",port=8080,debug=True)