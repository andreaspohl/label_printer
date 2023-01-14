from flask import Flask, render_template, request
import subprocess, os

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == "POST":
        text = request.form.get("text")
        convert(text)
        return render_template("plot.html", forward_message=text)

    return render_template('index.html')

def convert(text):
    with open('/home/pi/label_printer/data/in.txt', 'w', encoding='utf-8') as f:
        f.write(text)
        f.close()
        subprocess.run(['./text_to_gcode.py', '--input', '../data/in.txt', '--output', '../data/out.nc', '--line-length', '3000', '--line-spacing', '10', '--padding', '0.5'], cwd='/home/pi/label_printer/text-to-gcode/')

if __name__ == '__main__':
    convert("blabla")