# ozgursozluk

![](https://img.shields.io/badge/python-3.8%2B-blue)
![](https://img.shields.io/badge/code%20style-black-black)
![](https://img.shields.io/github/v/release/beucismis/ozgursozluk)
![](https://img.shields.io/github/actions/workflow/status/beucismis/ozgursozluk/tests.yml?label=tests)

A free and open source alternative Ekşi Sözlük front-end. Does not use the API, only scrapes the web. Offical instance: https://ozgursozluk.freedns.rocks

## Features
- No JavaScript
- Docker support
- Topic searching
- Viewing topic, entry and author
- Gündem and debe page support
- Optional displaying author nickname
- 8 different theme support
- Self-hosted, ad-free, simple and fast
- Responsive support for small screens

## Installing and Running
Clone the repository:
```
git clone https://github.com/beucismis/ozgursozluk
cd ozgursozluk/
```

Normal running:
```
pip3 install -r requirements.txt
gunicorn
```
Deploy using a different port: `gunicorn --bind 127.0.0.1:3131`

Running with Docker:
```
docker build -t ozgursozluk .
docker run -p 3131:80 ozgursozluk
```

## Redirection
[Redirector](https://einaregilsson.com/redirector) browser extension is recommended for use. Configuration:
```
Description: Ekşi Sözlük to özgürsözlük
Example URL: https://eksisozluk.com/linux--32084
Include pattern: ^https?://(?:.*\.)*(?<!link.)eksisozluk\.com(/.*)?$
Redirect to: https://ozgursozluk.freedns.rocks$1
Pattern type: Regular Expression
Example result: https://ozgursozluk.freedns.rocks/linux--32084
```

## Preview
<table>
  <tbody>
    <tr>
      <td><img src="https://github.com/beucismis/ozgursozluk/assets/40023234/b3505c9f-61f9-4596-89dc-ebfafcfbb373"></td>
      <td><img src="https://github.com/beucismis/ozgursozluk/assets/40023234/f4821a5c-8522-4ffb-8cf5-01620924ef1a"></td>
      <td><img src="https://github.com/beucismis/ozgursozluk/assets/40023234/11516669-da4b-4732-9413-d77e889167a0"></td>
    </tr>
  </tbody>
</table>

## License
This project lisanced under WTFPL for details check [LICENSE](LICENSE) file.
