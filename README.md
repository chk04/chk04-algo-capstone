Deskripsi: (Contoh Dokumentasi)
API ini dinominasikan sebagai capstone project yang berguna untuk mengirimkan data kepada user. Proses wrangling dilakukan sesuai endpoint-endpoint yang dimaksud. Base url dari aplikasi ini adalah https://algo-capstone.herokuapp.com

Endpoints: 
    1. / , method = GET
    Merupakan endpoint home, dan akan mengembalikan nilai berupa string selamat datang

    2. /data/get/<data_name> , method = GET
    Mengembalikan data <data_name> dalam bentuk JSON. Beberapa data yang tersedia adalah : 
        - books_c.csv
        - pulsar_stars.csv (tidak digunakan, hanya contoh saja)

    3. /data/get/equal/<data_name>/<column>/<value>
    Mengembalikan <data_name> yang telah di filter dimana nilai pada <column> = <value>
