#!/bin/bash
which python
cd /home/pi/label_printer
pwd
activate() {
    . /home/pi/label_printer/venv/bin/activate
}
activate
which python
flask --debug run --host=0.0.0.0