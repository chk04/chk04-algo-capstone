from flask import Flask, request 
import pandas as pd 
app = Flask(__name__) 

@app.route('/help')
def home():
    return '''
        <p>Deskripsi: (Contoh Dokumentasi)</p>
        <p>API ini dinominasikan sebagai capstone project yang berguna untuk mengirimkan data kepada user. Proses wrangling dilakukan sesuai endpoint-endpoint yang dimaksud. Base url dari aplikasi ini adalah https://chk04-capstone.herokuapp.com/</p>
        <p><br></p>
        <p>Endpoints:&nbsp;</p>
        <p>1. / help, method = GET</p>
        <p style="margin-left: 20px;">Merupakan endpoint home, dan akan mengembalikan nilai berupa string selamat datang</p>
        <p style="margin-left: 20px;"><br></p>
        <p>2. /data/&lt;data_name&gt;/&lt;column&gt;/&lt;value&gt;&apos;, methods=GET</p>
        <p style="margin-left: 20px;">Mengambil data &lt;data_name&gt; dengan filter pada kolom &lt;column&gt; spesifik pada &lt;value&gt;.&nbsp;</p>
        <p style="margin-left: 20px;"><span style='color: rgb(0, 0, 0); font-family: "Times New Roman"; font-size: medium; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'>Return: .json</span>&nbsp;</p>
        <p style="margin-left: 20px;">Data yang tersedia: rice.csv</p>
        <p style="margin-left: 20px;">Coloum yang tersedia:<br>receipt_id, receipts_item_id, purchase_time category, sub_category, store, unit_price, discount, quantity, yearmonth</p>
        <p style="margin-left: 20px;">contoh:&nbsp;</p>
        <p style="margin-left: 20px;"><span style='color: rgb(0, 0, 0); font-family: "Times New Roman"; font-size: medium; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'>a. https://chk04-capstone.herokuapp.com/data/rice.csv/store/minimarket</span></p>
        <p style="margin-left: 20px;"><span style='color: rgb(0, 0, 0); font-family: "Times New Roman"; font-size: medium; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'>b. https://chk04-capstone.herokuapp.com/data/rice.csv/store/supermarket</span></p>
        <p>&nbsp; &nbsp;</p>
        <p>3. /rice, <span style='color: rgb(0, 0, 0); font-family: "Times New Roman"; font-size: medium; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'>methods=GET</span></p>
        <p style="margin-left: 20px;"><span style='color: rgb(0, 0, 0); font-family: "Times New Roman"; font-size: medium; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'>Mengambil data pada data rice.csv dengan</span></p>
        <p style="margin-left: 20px;"><span style='color: rgb(0, 0, 0); font-family: "Times New Roman"; font-size: medium; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'>Return: .json</span>&nbsp;</p>
        <p style="margin-left: 20px;"><br></p>
        <p>4. /rice/&lt;store&gt;, <span style='color: rgb(0, 0, 0); font-family: "Times New Roman"; font-size: medium; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'>methods=GET</span>&nbsp;</p>
        <p style="margin-left: 20px;">Mengambil data dari rice.csv dengan filter pada tipe penjualan &lt;store&gt; &nbsp;</p>
        <p style="margin-left: 20px;"><span style='color: rgb(0, 0, 0); font-family: "Times New Roman"; font-size: medium; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'>Return: .json</span>&nbsp;</p>
        <p style="margin-left: 20px;">Data yang tersedia: rice.csv</p>
        <p style="margin-left: 20px;">Tipe penjualan yang tersedia: minimarket, supermarket, hypermarket</p>
        <p style="margin-left: 20px;">contoh:&nbsp;</p>
        <p style="margin-left: 20px;"><span style='color: rgb(0, 0, 0); font-family: "Times New Roman"; font-size: medium; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'>a. https://chk04-capstone.herokuapp.com/rice/minimarket</span></p>
        <p style="margin-left: 20px;"><span style='color: rgb(0, 0, 0); font-family: "Times New Roman"; font-size: medium; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'>b. https://chk04-capstone.herokuapp.com/rice/supermarket</span></p>
        <p style="margin-left: 20px;"><span style='color: rgb(0, 0, 0); font-family: "Times New Roman"; font-size: medium; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'>b. <a href="https://chk04-capstone.herokuapp.com/rice/hypermarket">https://chk04-capstone.herokuapp.com/rice/hypermarket</a></span></p>
        <p style="margin-left: 20px;"><br></p>
        <p><span style='color: rgb(0, 0, 0); font-family: "Times New Roman"; font-size: medium; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'>5. /rice/purchasemonth/&lt;month&gt;&apos;, methods=GET</span></p>
        <p style="margin-left: 20px;">Mengambil data dari rice.csv dengan filter pada bulan penjualan &lt;month&gt; &nbsp;</p>
        <p style="margin-left: 20px;"><span style='color: rgb(0, 0, 0); font-family: "Times New Roman"; font-size: medium; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'>Return: .json</span>&nbsp;</p>
        <p style="margin-left: 20px;">Data yang tersedia: rice.csv</p>
        <p style="margin-left: 20px;">contoh:&nbsp;</p>
        <p style="margin-left: 20px;"><span style='color: rgb(0, 0, 0); font-family: "Times New Roman"; font-size: medium; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'>a. <a data-fr-linked="true" href="https://chk04-capstone.herokuapp.com/rice/purchasemonth/November">https://chk04-capstone.herokuapp.com/rice/purchasemonth/November</a></span></p>
        <p style="margin-left: 20px;"><br></p>
        <p><span style='color: rgb(0, 0, 0); font-family: "Times New Roman"; font-size: medium; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;'>6. /rice/purchase, method=GET,PUSH</span></p>
        <p style="margin-left: 20px;">Mengambil data dari rice.csv dengan filter pada tahun dan bulan penjualan, dengan GUI</p>
        <p style="margin-left: 20px;">Return: .json</p>
        <p style="margin-left: 20px;">url: httos://chk04-capstone.herokuapp.com/purchasedate</p>
        <p style="margin-left: 20px;"><br></p>
        <p style="margin-left: 20px;"><br></p>
    '''


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

@app.route('/rice/purchasedate', methods=['GET', 'POST']) #allow both GET and POST requests
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
