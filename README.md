# ozgursozluk

![](https://img.shields.io/badge/python-3.8%2B-blue)
![](https://img.shields.io/badge/style-black-black)
![](https://img.shields.io/github/v/release/beucismis/ozgursozluk)
![](https://img.shields.io/github/actions/workflow/status/beucismis/ozgursozluk/tests.yml)

A free and open source alternative Ekşi Sözlük front-end. Offical instance: https://ozgursozluk.freedns.rocks

## Features
- No JavaScript
- Docker support
- Topic searching
- Entry sorting options
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
Deploy using a different port: `gunicorn --bind 0.0.0.0:3131`

Running with Docker:
```
docker build -t ozgursozluk .
docker run -p 3131:80 ozgursozluk
```

## Preview
<table>
  <tbody>
    <tr>
      <td><img src="https://user-images.githubusercontent.com/40023234/234684246-de064e97-bd44-49b8-93ab-6c13706d6c3b.png"></td>
      <td><img src="https://user-images.githubusercontent.com/40023234/234684344-e77b4b1b-6aeb-44c4-840c-4cb4d01cd96e.png"></td>
      <td><img src="https://user-images.githubusercontent.com/40023234/234684430-092d27f0-7eed-4e7b-8ffc-78e916f7dc71.png"></td>
    </tr>
  </tbody>
</table>

## License
This project lisanced under WTFPL for details check [LICENSE](LICENSE) file.
