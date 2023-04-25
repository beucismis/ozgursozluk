# ozgursozluk

![](https://img.shields.io/badge/python-3.8%2B-blue)
![](https://img.shields.io/badge/style-black-black)
![](https://img.shields.io/github/actions/workflow/status/beucismis/ozgursozluk/tests.yml)
![](https://img.shields.io/website?url=http%3A%2F%2Fozgursozluk.freedns.rocks)

Free alternative simple ekşi sözlük front-end. Offical instance: http://ozgursozluk.freedns.rocks

## Features
- No JavaScript
- Topic search
- View topic and entry
- Gündem and debe page support
- Optioanl dispay author nickname
- Ad-free, simple and fast
- Light and dark theme support
- Responsive support for small screens

## Installing
```
git clone https://github.com/beucismis/ozgursozluk
cd ozgursozluk/
pip3 install -r requirements.txt
gunicorn # or gunicorn --bind 0.0.0.0:3131
```

## Preview
<p>
  <img src="https://user-images.githubusercontent.com/40023234/234410466-fe1b77fc-875f-4e28-b11e-872c362fb3ae.png" width="400">
  <img src="https://user-images.githubusercontent.com/40023234/234410618-c7bc4ba0-e375-4d49-b86a-231f2536d828.png" width="400">
</p>

## ToDo
- [ ] API endpoint
- [ ] Docker support
- [x] Page support for debe
- [x] Display optional author nickname
- [ ] Sorthing for entries today and all
- [ ] URL change support for alternative front-ends (e.g: twitter to nitter)
