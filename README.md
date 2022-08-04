# App for PSE Kominfo Data mining
Data Mining for PSE kominfo

Ini adalah aplikasi python untuk melakukan data mining di web PSE Kominfo.
Untuk menggunakan aplikasi ini anda memerlukan Python yang terinstall pada mesin anda.
Juga dependensi framework yang digunakan adalah `requests`,`Flask`, dan `flask_restful`.
Aplikasi ini berbasis RESTFull API, jika ingin menggunakannya cukup gunakan browser atau Postman.

# How to USE Activate
1. Install python
2. Instal Virtual environtment `pip install virtualenv`
3. Create Virtual environtment (in windows: `py -m venv venv`)
4. Activate Virtual environtment (in windows: `.\venv\Scripts\activate`)
4. Install dependencies `pip install request`, `pip install Flask`, and `pip install flask_restful`
5. Run main `python main.py`

# How to use
### For PSE lokal:
(GET) http://localhost:5000/pselokal/(First Page)/(Last Page)
### For PSE 
(GET) http://localhost:5000/pseasing/(First Page)/(Last Page)