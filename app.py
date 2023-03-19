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
        line1 = request.form.get("line1")
        line2 = request.form.get("line2")
        text = line1
        if line2 != "":
            text = text + '\n' + line2
        convert(text)

    return render_template('index.html')

def convert(text):
    print('printing: ' + text)

    with open(home_dir +  'data/' + txt_file, 'w', encoding='utf-8') as f:
        f.write(text)
        f.close()
    
    subprocess.run(['./text_to_gcode.py', '--input', '../data/' + txt_file, '--output', '../data/' + nc_file, '--line-length', '75', '--line-spacing', '9', '--padding', '1.5'], cwd=home_dir + 'text-to-gcode/')

    with open(home_dir + 'data/' + nc_file, 'a') as f:
        f.write('\nG0 X0.0 Y0.0')
        f.write('')

    label_printer.plot_label(home_dir + 'data/' + nc_file)

if __name__ == '__main__':
    convert("::::::::::")
