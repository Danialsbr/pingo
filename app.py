from flask import Flask, render_template, jsonify, request
import subprocess
import datetime
import sqlite3
import os

app = Flask(__name__)
DB_NAME = 'log.db'

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            ip_address TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def ping_device(ip_address):
    result = subprocess.run(['ping', '-n', '1', '-w', '1000', ip_address], stdout=subprocess.PIPE)

    if result.returncode == 0:
        output = result.stdout.decode('utf-8')
        time_index = output.find('Average = ')
        if time_index != -1:
            time_start = time_index + 10
            time_end = output.find('ms', time_start)
            response_time = output[time_start:time_end]
            status = f'Reachable ({response_time} ms)'
        else:
            status = 'Reachable'
    else:
        status = 'Unreachable'

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('INSERT INTO logs (timestamp, ip_address, status) VALUES (?, ?, ?)',
                   (timestamp, ip_address, status))

    conn.commit()
    conn.close()

    return status

def read_devices():
    devices = {}
    file_path = os.path.join(os.path.dirname(__file__), 'devices.txt')

    with open(file_path, 'r') as file:
        for line in file:
            ip, name = line.strip().split(',')
            devices[ip] = name

            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()

            cursor.execute('INSERT INTO logs (timestamp, ip_address, status) VALUES (?, ?, ?)',
                           (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ip, 'Unknown'))

            conn.commit()
            conn.close()

    return devices

def get_device_logs(ip_address):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT timestamp, status FROM logs WHERE ip_address = ? ORDER BY timestamp ASC', (ip_address,))
    logs = cursor.fetchall()

    conn.close()

    return logs

@app.route('/')
def index():
    devices = read_devices()
    status_list = []

    for ip, name in devices.items():
        status = ping_device(ip)
        status_list.append({'name': name, 'ip': ip, 'status': status})

    status_list.sort(key=lambda x: 'Unreachable' in x['status'], reverse=True)

    return render_template('index.html', status_list=status_list)

@app.route('/status')
def status():
    devices = read_devices()
    status_list = []

    for ip, name in devices.items():
        status = ping_device(ip)
        status_list.append({'name': name, 'ip': ip, 'status': status})

    status_list.sort(key=lambda x: 'Unreachable' in x['status'], reverse=True)

    return render_template('status.html', status_list=status_list)

@app.route('/logs/<ip_address>')
def logs(ip_address):
    logs = get_device_logs(ip_address)
    return render_template('logs.html', ip_address=ip_address, logs=logs)

@app.route('/scanning', methods=['GET', 'POST'])
def scanning():
    if request.method == 'POST':
        start_ip = request.form['start_ip']
        end_ip = request.form['end_ip']
        ip_range = f"{start_ip}-{end_ip}"
        
        # Perform network scanning and discovery using the provided IP range
        # Implement your scanning logic here

        return render_template('scanning.html', ip_range=ip_range)

    return render_template('scanning.html')

if __name__ == '__main__':
    create_table()
    app.run(debug=True, port=5000)
