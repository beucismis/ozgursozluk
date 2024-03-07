<img src="https://github.com/beucismis/ozgursozluk/assets/40023234/4f145030-2376-4d2d-acb0-39167212793f" width="350">

![](https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square&labelColor=black&color=%237FBE4A)
![](https://img.shields.io/pypi/v/ozgursozluk?style=flat-square&labelColor=black&color=%237FBE4A)
![](https://img.shields.io/badge/code%20style-black-black?style=flat-square&labelColor=black&color=%237FBE4A))
![](https://img.shields.io/github/actions/workflow/status/beucismis/ozgursozluk/tests.yml?label=tests&style=flat-square&labelColor=black&color=%237FBE4A)
![](https://img.shields.io/github/actions/workflow/status/beucismis/ozgursozluk/publish.yml?label=publish&style=flat-square&labelColor=black&color=%237FBE4A)

A free and open source alternative ekşi sözlük front-end. Does not use the API, only scrapes the web.

Official instance: (offline) https://ozgursozluk.freedns.rocks </br>
Donate: (offline) https://ozgursozluk.freedns.rocks/donate

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

## Installation

Install from the `pip`:
```
pip3 install ozgursozluk
```

Install from the repo:
```
pip3 install git+https://github.com/beucismis/ozgursozluk.git
```

Updating:
```
pip3 install ozgursozluk --upgrade
```

## Deploying

```
flask --app ozgursozluk run
# or
gunicorn ozgursozluk:app
```

Alternatively, with Docker:
```
git clone https://github.com/beucismis/ozgursozluk
cd ozgursozluk
docker build -t ozgursozluk .
docker run -p 8080:80 ozgursozluk
```

See also, https://github.com/beucismis/ozgursozluk/wiki/Main

## Environment Variables

| Key | Type | Default Value |
| - | - | - |
| `SECRET_KEY` | `str` |  random |
| `FLASK_RUN_HOST` | `str` | `127.0.0.1` |
| `FLASK_RUN_PORT` | `str` | `5000` |
| `EKSI_SOZLUK_BASE_URL` | `str` | `https://eksisozluk.com` |

## Preview

<table>
  <tbody>
    <tr>
      <td><img src="https://github.com/beucismis/ozgursozluk/assets/40023234/47ba12c6-e67c-43c7-9f99-652769db7c88"></td>
      <td><img src="https://github.com/beucismis/ozgursozluk/assets/40023234/7bbe9de7-0165-4bc4-aba3-b2b306396372"></td>
      <td><img src="https://github.com/beucismis/ozgursozluk/assets/40023234/d7621df4-9f74-4186-b633-d801a676176d"></td>
      <td><img src="https://github.com/beucismis/ozgursozluk/assets/40023234/bc444a11-4b89-4ef0-9fc6-4d5f6318b626"></td>
      <td><img src="https://github.com/beucismis/ozgursozluk/assets/40023234/78fde617-b634-4bb0-adf8-193159709c25"></td>
    </tr>
  </tbody>
</table>

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

## License

This project is licensed under WTFPL for details, check [LICENSE](LICENSE) file.
