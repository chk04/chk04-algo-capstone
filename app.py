from flask import Flask, request 
import pandas as pd 
app = Flask(__name__) 

@app.route('/api-help')
def home():
    return 'Hello World'


# mendapatkan data dengan filter nilai <value> pada kolom <column>
@app.route('/data/<data_name>/<column>/<value>', methods=['GET']) 
def get_data_csv_1arg(data_name, column, value): 
    data = pd.read_csv('data/' + str(data_name))
    mask = data[column] == value
    data = data[mask]
    return (data.to_json())

# mendapatkan data dengan filter nilai <value> pada kolom <column>
@app.route('/rice', methods=['GET']) 
def get_data_beras(): 
    data = pd.read_csv('data/rice.csv')
    data['purchase_time'] = data['purchase_time'].astype('datetime64')
    return (data.to_json())

@app.route('/rice/<store>', methods=['GET']) 
def get_data_beras_store(store): 
    data = pd.read_csv('data/rice.csv')
    data['purchase_time'] = data['purchase_time'].astype('datetime64')
    mask = data['store'] == store
    data = data[mask]
    return (data.to_json())

@app.route('/rice/purchasemonth/<month>', methods=['GET']) 
def get_data_beras_mpurchase(month): 
    data = pd.read_csv('data/rice.csv')
    data['purchase_time'] = data['purchase_time'].astype('datetime64')
    data['purchase_time_month'] = data['purchase_time'].dt.month_name()
    mask = data['purchase_time_month'] == month
    data = data[mask]
    return (data.to_json())

@app.route('/rice/purchasemonth', methods=['GET', 'POST']) #allow both GET and POST requests
def form():
    if request.method == 'POST':  # Hanya akan tampil setelah melakukan POST (submit) form
        key1 = 'year'
        key2 = 'month'
        year = request.form.get(key1)
        month = request.form[key2]
        data = pd.read_csv('data/rice.csv')
        data['purchase_time'] = data['purchase_time'].astype('datetime64')
        data['purchase_time_year'] = data['purchase_time'].dt.year
        data['purchase_time_month'] = data['purchase_time'].dt.month
        mask1 = data['purchase_time_year'] == int(year)
        mask2 = data['purchase_time_month'] == int(month)
        data = data[mask1 & mask2]
        return (data.to_json())
    return '''<form method="POST">
                  Year: <input type="text" name="year"><br>
                  Month: <input type="text" name="month"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''


if __name__ == '__main__':
    app.run(debug=True, port=5000) 