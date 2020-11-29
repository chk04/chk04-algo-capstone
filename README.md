Deskripsi: ini merupakan dokumentasi dari Capstone Project DA - @Algorit.ma 
        API ini dinominasikan sebagai capstone project yang berguna untuk mengirimkan data kepada user. Proses wrangling dilakukan sesuai endpoint-endpoint yang dimaksud. Base url dari aplikasi ini adalah https://chk04-capstone.herokuapp.com/
        
        Endpoints: 
        1. /, method = GET
        Merupakan endpoint home, dan akan mengembalikan Dokumentasi
        
        2. /data/<data_name>/<column>/<value>', methods=GET
        Mengambil data <data_name> dengan filter pada kolom <column> spesifik pada <value>. 
        Return: .json 
        Data yang tersedia: rice.csv
        Coloum yang tersedia:receipt_id, receipts_item_id, purchase_time category, sub_category, store, unit_price, discount, quantity, yearmonth
        contoh: 
        a. https://chk04-capstone.herokuapp.com/data/rice.csv/store/minimarket
        b. https://chk04-capstone.herokuapp.com/data/rice.csv/store/supermarket
           
        3. /rice, methods=GET
        Mengambil data pada data rice.csv dengan
        Return: .json 
        
        4. /rice/<store>, methods=GET 
        Mengambil data dari rice.csv dengan filter pada tipe penjualan <store>  
        Return: .json 
        Data yang tersedia: rice.csv
        Tipe penjualan yang tersedia: minimarket, supermarket, hypermarket
        contoh: 
        a. https://chk04-capstone.herokuapp.com/rice/minimarket
        b. https://chk04-capstone.herokuapp.com/rice/supermarket
        b. https://chk04-capstone.herokuapp.com/rice/hypermarket
        
        5. /rice/purchasemonth/<month>', methods=GET
        Mengambil data dari rice.csv dengan filter pada bulan penjualan <month>  
        Return: .json 
        Data yang tersedia: rice.csv
        contoh: 
        a. https://chk04-capstone.herokuapp.com/rice/purchasemonth/November
        
        6. /rice/purchase, method=GET,PUSH
        Mengambil data dari rice.csv dengan filter pada tahun dan bulan penjualan, dengan GUI, dengan input angka
        Return: .json
        url: https://chk04-capstone.herokuapp.com/rice/purchasedate
