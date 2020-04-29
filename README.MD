## Printer helper for window os
If you don't need to use web browser preview before printing

## Prerequisites

Need to install these sofwares/library

```
pdf reader (foxit reader for eg)

wkhtmltopdf (html to pdf)

python3
pip
pipenv
```

## Installation

Mandatory sofwares:

- Need to install pdf reader

- [Link](https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox-0.12.5-1.msvc2015-win64.exe) to download `wkhtmltopdf`

Then install to path `WKHTMLTOPDF_PATH` same as `app.ini` file

**Notice:** Need to map `PrinterLabel` and `PrinterPaper` to local printer name 
```
[default]
WKHTMLTOPDF_PATH = C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe
PrinterLabel = TSC TE200
PrinterPaper = BrotherHL-L2320D-series
```

Open CMD, run these command to install
```
pipenv install
pipenv shell
python socket_server.py
```

## Client

Sample html file

```
<!DOCTYPE html>
<html>
<head>
    <title>WebSocket demo</title>
    <script src="https://code.jquery.com/jquery-3.5.0.min.js" integrity="sha256-xNzN2a4ltkB44Mc/Jz3pT4iU1cmeR0FkXs4pru/JxaQ=" crossorigin="anonymous"></script>
</head>
<body>
<script>
    var ws = new WebSocket("ws://127.0.0.1:2377/");

    ws.onmessage = function (event) {
        data = event.data;
        console.log(data);
    };

    $(document).ready(function() {
        $("#click").on('click', function(){
            ws.send(
                JSON.stringify(
                    {
                        content: "PGh0bWw+CjwhLS0gVGV4dCBiZXR3ZWVuIGFuZ2xlIGJyYWNrZXRzIGlzIGFuIEhUTUwgdGFnIGFuZCBpcyBub3QgZGlzcGxheWVkLgpNb3N0IHRhZ3MsIHN1Y2ggYXMgdGhlIEhUTUwgYW5kIC9IVE1MIHRhZ3MgdGhhdCBzdXJyb3VuZCB0aGUgY29udGVudHMgb2YKYSBwYWdlLCBjb21lIGluIHBhaXJzOyBzb21lIHRhZ3MsIGxpa2UgSFIsIGZvciBhIGhvcml6b250YWwgcnVsZSwgc3RhbmQgCmFsb25lLiBDb21tZW50cywgc3VjaCBhcyB0aGUgdGV4dCB5b3UncmUgcmVhZGluZywgYXJlIG5vdCBkaXNwbGF5ZWQgd2hlbgp0aGUgV2ViIHBhZ2UgaXMgc2hvd24uIFRoZSBpbmZvcm1hdGlvbiBiZXR3ZWVuIHRoZSBIRUFEIGFuZCAvSEVBRCB0YWdzIGlzIApub3QgZGlzcGxheWVkLiBUaGUgaW5mb3JtYXRpb24gYmV0d2VlbiB0aGUgQk9EWSBhbmQgL0JPRFkgdGFncyBpcyBkaXNwbGF5ZWQuLS0+CjxoZWFkPgo8dGl0bGU+RW50ZXIgYSB0aXRsZSwgZGlzcGxheWVkIGF0IHRoZSB0b3Agb2YgdGhlIHdpbmRvdy48L3RpdGxlPgo8L2hlYWQ+CjwhLS0gVGhlIGluZm9ybWF0aW9uIGJldHdlZW4gdGhlIEJPRFkgYW5kIC9CT0RZIHRhZ3MgaXMgZGlzcGxheWVkLi0tPgo8Ym9keT4KPGgxPkVudGVyIHRoZSBtYWluIGhlYWRpbmcsIHVzdWFsbHkgdGhlIHNhbWUgYXMgdGhlIHRpdGxlLjwvaDE+CjxwPkJlIDxiPmJvbGQ8L2I+IGluIHN0YXRpbmcgeW91ciBrZXkgcG9pbnRzLiBQdXQgdGhlbSBpbiBhIGxpc3Q6IDwvcD4KPHVsPgo8bGk+VGhlIGZpcnN0IGl0ZW0gaW4geW91ciBsaXN0PC9saT4KPGxpPlRoZSBzZWNvbmQgaXRlbTsgPGk+aXRhbGljaXplPC9pPiBrZXkgd29yZHM8L2xpPgo8L3VsPgo8cD5JbXByb3ZlIHlvdXIgaW1hZ2UgYnkgaW5jbHVkaW5nIGFuIGltYWdlLiA8L3A+CjxwPjxpbWcgc3JjPSJodHRwOi8vd3d3Lm15Z2lmcy5jb20vQ292ZXJJbWFnZS5naWYiIGFsdD0iQSBHcmVhdCBIVE1MIFJlc291cmNlIj48L3A+CjxwPkFkZCBhIGxpbmsgdG8geW91ciBmYXZvcml0ZSA8YSBocmVmPSJodHRwczovL3d3dy5kdW1taWVzLmNvbS8iPldlYiBzaXRlPC9hPi4KQnJlYWsgdXAgeW91ciBwYWdlIHdpdGggYSBob3Jpem9udGFsIHJ1bGUgb3IgdHdvLiA8L3A+Cjxocj4KPHA+RmluYWxseSwgbGluayB0byA8YSBocmVmPSJwYWdlMi5odG1sIj5hbm90aGVyIHBhZ2U8L2E+IGluIHlvdXIgb3duIFdlYiBzaXRlLjwvcD4KPCEtLSBBbmQgYWRkIGEgY29weXJpZ2h0IG5vdGljZS4tLT4KPHA+JiMxNjk7IFdpbGV5IFB1Ymxpc2hpbmcsIDIwMTE8L3A+CjwvYm9keT4KPC9odG1sPg==",
                        printer_name: $("#printer").val()

                    }
                )
            );
            window.location.reload();
        })
    });

</script>
<select id="printer" >
    <option value="PrinterLabel">PrinterLabel</option>
    <option value="PrinterPaper">PrinterPaper</option>
</select>
<button id="click">print</button>
</body>
</html>
```
Then open it to select to the printer, then click on `print` button to test

## Trace log

You can check log via `app.log` file
