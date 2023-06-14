<img src="https://github.com/beucismis/ozgursozluk/assets/40023234/4f145030-2376-4d2d-acb0-39167212793f" width="380">

![](https://img.shields.io/badge/python-3.8%2B-blue)
![](https://img.shields.io/badge/code%20style-black-black)
![](https://img.shields.io/github/v/release/beucismis/ozgursozluk)
![](https://img.shields.io/github/actions/workflow/status/beucismis/ozgursozluk/tests.yml?label=tests)

A free and open source alternative ekşi sözlük front-end. Does not use the API, only scrapes the web. Official instance: https://ozgursozluk.freedns.rocks

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

### Environment Variables

| Key | Type | Default Value |
| - | - | - |
| `SECRET_KEY` | `str` |  |
| `EKSI_SOZLUK_BASE_URL` | `str` | `https://eksisozluk1923.com` |

## Redirection
[Redirector](https://einaregilsson.com/redirector) browser extension is recommended for use. Configuration:
```
Description: ekşi sözlük to özgürsözlük
Example URL: https://eksisozluk.com/linux--32084
Include pattern: ^https?://(?:.*\.)*(?<!link.)eksisozluk(.*)\.com(/.*)?$
Redirect to: https://ozgursozluk.freedns.rocks$1
Pattern type: Regular Expression
Example result: https://ozgursozluk.freedns.rocks/linux--32084
```

## Preview
<table>
  <tbody>
    <tr>
      <td><img src="https://github.com/beucismis/ozgursozluk/assets/40023234/620558a0-f518-42c8-9b2a-cc67067f63f3"></td>
      <td><img src="https://github.com/beucismis/ozgursozluk/assets/40023234/2c4d2fc7-d5dc-4a20-bc09-03b8ea36caad"></td>
      <td><img src="https://github.com/beucismis/ozgursozluk/assets/40023234/8dfd442c-cddb-41cd-ac3c-d95f0436e2e5"></td>
    </tr>
  </tbody>
</table>

## License
This project is licensed under WTFPL for details, check [LICENSE](LICENSE) file.
