# ozgursozluk

![](https://img.shields.io/badge/python-3.8%2B-blue)
![](https://img.shields.io/badge/code%20style-black-black)
![](https://img.shields.io/github/v/release/beucismis/ozgursozluk)
![](https://img.shields.io/github/actions/workflow/status/beucismis/ozgursozluk/tests.yml?label=tests)

A free and open source alternative Ekşi Sözlük front-end. Offical instance: https://ozgursozluk.freedns.rocks

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

## Preview
<table>
  <tbody>
    <tr>
      <td><img src="https://user-images.githubusercontent.com/40023234/236811059-a328bda0-78e7-44ba-b125-3d782ad9582c.png"></td>
      <td><img src="https://user-images.githubusercontent.com/40023234/236811259-474f43ce-fd4b-4fcb-bf1e-7b241f9a9384.png"></td>
      <td><img src="https://user-images.githubusercontent.com/40023234/236811430-aae679cb-211c-4ac5-a67c-e69550295460.png"></td>
    </tr>
  </tbody>
</table>

## License
This project lisanced under WTFPL for details check [LICENSE](LICENSE) file.
