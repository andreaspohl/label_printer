from flask import Flask, render_template, request
import subprocess, os
import label_printer as lp

app = Flask(__name__)
label_printer = lp.Label_printer()

home_dir = '/home/pi/label_printer/'
txt_file = 'label.txt'
nc_file = 'label.nc'
tst_file = 'test_data.nc'

@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == "POST":
        text = request.form.get("text")
        convert(text)
        return render_template("plot.html", forward_message=text)

    return render_template('index.html')

def convert(text):
    with open(home_dir +  'data/' + txt_file, 'w', encoding='utf-8') as f:
        f.write(text)
        f.close()
        subprocess.run(['./text_to_gcode.py', '--input', '../data/' + txt_file, '--output', '../data/' + nc_file, '--line-length', '3000', '--line-spacing', '10', '--padding', '0.5'], cwd=home_dir + 'text-to-gcode/')
        label_printer.plot_label(home_dir + 'data/' + tst_file)


if __name__ == '__main__':
    convert("Schach matt!")