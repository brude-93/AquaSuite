import datetime
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def display_aquaSuite():
    applicationTitle = "Aqua Suite - Sensor Monitoring System"
    version = "0.1"
    date = str(datetime.datetime.now())
    name = "Ben"
    temperature = "69"
    return render_template(
      'index.html',
      applicationTitle=applicationTitle,
      name=name,
      version=version,
      date=date,
      temperature=temperature)

if __name__ == "__main__":
    app.run()
