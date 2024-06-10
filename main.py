from flask import Flask, render_template, request, redirect
from extractors.remoteok import get_jobs

app = Flask("JobScrapper")


@app.route("/")
def home():
  return render_template("home.html", name="nico")


db = {}


@app.route("/search")
def hello():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/") 
  if keyword in db:
    jobs = db[keyword]
  else:
    jobs = get_jobs(keyword)
    db[keyword] = jobs

  return render_template("search.html", keyword=keyword, jobs=jobs)


app.run("0.0.0.0")
