'''
virtualenv -p python
flask\Scripts\activate
python app.py

'''
from flask import Flask, request, render_template

import routines as r
import json

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return '''
        <h1>Web Server</h1>

        <hr>

        <ol>
          <li><a href='/unique-users'>Unique Website Users</a></li>
          <li><a href='/loyal-users'>Loyal Website Users</a></li>
        </ol>
    '''

@app.route('/unique-users', methods = ['GET', 'POST'])
def unique_users():
    fn = 'data.csv'
    df = r.import_csv_data(fn)   
    device = request.args.get('device')
    os = request.args.get('os')
        
    if device and os :
        device_array = device.split(',')
        os_array = os.split(',')
        pd = r.parse_data_by_device_id(df, device_array) 
        ppd = r.parse_data_by_os_id(pd, os_array)
        unique_visitors = r.get_unique_visitors(ppd)
    elif device :
        device_array = device.split(',')
        pd = r.parse_data_by_device_id(df, device_array) 
        unique_visitors = r.get_unique_visitors(pd)
    elif  os:
        os_array = os.split(',')
        pd = r.parse_data_by_os_id(pd, os_array)
        unique_visitors = r.get_unique_visitors(pd)
    else:
        unique_visitors = r.get_unique_visitors(df)

    json_data = json.dumps({'count': unique_visitors.size}, sort_keys=True,
                  indent=2, separators=(',', ': '))


    if request.method == 'GET':
        return '''
            {}
        '''.format(json_data)


@app.route('/loyal-users', methods = ['GET', 'POST'])
def loyal_users():
    fn = 'data.csv'
    df = r.import_csv_data(fn)    
    device = request.args.get('device')
    os = request.args.get('os')
  
    if device and os :
        device_array = device.split(',')
        os_array = os.split(',')
        pd = r.parse_data_by_device_id(df, device_array) 
        ppd = r.parse_data_by_os_id(pd, os_array)
        loyal_visitors_number = r.get_number_of_loyal_visitors(ppd)
    elif device:
        device_array = device.split(',')
        pd = r.parse_data_by_device_id(df, device_array) 
        loyal_visitors_number = r.get_number_of_loyal_visitors(pd)    
    elif  os:
        os_array = os.split(',')
        pd = r.parse_data_by_os_id(pd, os_array) 
        loyal_visitors_number = r.get_number_of_loyal_visitors(pd)    
    else: 
        loyal_visitors_number = r.get_number_of_loyal_visitors(df)

    json_data = json.dumps({'count': loyal_visitors_number}, sort_keys=True,
                  indent=2, separators=(',', ': '))    

    if request.method == 'GET':
        return '''
             {}
        '''.format(json_data)


if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)


