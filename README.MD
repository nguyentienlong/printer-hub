## prerequisite

```
python3
pip
pipenv
```

## install

[Link](https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox-0.12.5-1.msvc2015-win64.exe) to download `wkhtmltopdf`

Then install to path same as `app.ini` file

```
[default]
WKHTMLTOPDF_PATH = C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe

```

Open CMD, run these command to install
```
pipenv install
python main.py
```
output
```
(printer-hub) C:\printer-hub>python main.py
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```


## client

`a27ed5ba.ngrok.io` can be changed

**notice: `data` must be in json, `content` in data should be in base 64 encoded**

```
curl --location --request POST 'http://a27ed5ba.ngrok.io/printer/print' \
--header 'Content-Type: application/json' \
--data-raw '{
    "content": "PCFET0NUWVBFIGh0bWw+IDxodG1sPiA8Ym9keT4gPGgxIHN0eWxlPSJjb2xvcjpibHVlOyI+VGhpcyBpcyBhIEJsdWUgSGVhZGluZzwvaDE+IDwvYm9keT4gPC9odG1sPg==",
    "options": {
        "page-size": "A4",
        "margin-top": "20",
        "margin-right": "10",
        "margin-left": "10",
        "margin-bottom": "0",
        "zoom": "1",
        "encoding": "UTF-8"
    },
    "printer_name": "default"
}'
```

## Trace log

You can check log via `app.log` file
