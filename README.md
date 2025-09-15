<p align="center" width="100%">
<img height="128" src="https://github.com/user-attachments/assets/4893d92e-7077-4e2f-b1d4-ec809123d6ee" alt="ozgursozluk-logo" />
</p>

This project is free alternative Ekşi Sözlük front-end focused on privacy and performance. Made with <3 on the T61. Contributions are most welcome!

## Features

- No JavaScript Required – works perfectly without JS
- Docker Support – easy deployment and setup
- Topic Search – quickly find relevant discussions
- View Topics, Entries & Authors – browse content and contributors
- Gündem & Debe Page Support – full support for special pages
- Hide Displaying – favorite count, author and entry date
- 8 Built-in Themes – customize the look with 8 themes
- Self-Hosted, Ad-Free & Lightweight – fast, simple, and private on your server
- Responsive Design – optimized for mobile and small screens

## Preview

<table>
  <tbody>
    <tr>
      <td><img src="https://github.com/user-attachments/assets/9bd8801f-f66f-46ea-869f-160d5f927d3d"></td>
      <td><img src="https://github.com/user-attachments/assets/8ce49590-1d76-4033-98ae-8778546fc2a0"></td>
      <td><img src="https://github.com/user-attachments/assets/b3d8ab01-a36c-4077-913d-33c843a56389"></td>
      <td><img src="https://github.com/user-attachments/assets/33f691a5-609c-46b2-bce1-7ba783a8a2b2"></td>
      <td><img src="https://github.com/user-attachments/assets/93937a24-3e35-4aba-b291-4d4d53dcbfc4"></td>
    </tr>
  </tbody>
</table>

## Running

```
git clone https://github.com/beucismis/ozgursozluk
cd ozgursozluk/
pip install .
flask --app ozgursozluk.main:app run
```

## Running with Docker

```
git clone https://github.com/beucismis/ozgursozluk
cd ozgursozluk/
docker build -t ozgursozluk .
docker run -p 5000:5000 ozgursozluk
```

See also, https://github.com/beucismis/ozgursozluk/wiki/Main

## Usage

Once the service is running, you can access the API at `http://localhost:5000`.

## Environment Variables

| Variable               | Default Value            |
|------------------------|--------------------------|
| `SECRET_KEY`           | `token_hex(24)`          |
| `FLASK_RUN_HOST`       |  `127.0.0.1`             |
| `FLASK_RUN_PORT`       | `5000`                   |
| `EKSI_SOZLUK_BASE_URL` | `https://eksisozluk.com` |

## Developer Notes

- The ASGI app is defined as `app` in `src/ozgursozluk/main.py`.
- When installed as a package, you can launch it using `gunicorn`, `uvicorn`, `hypercorn` or any compatible ASGI tool.

## Redirection

[Redirector](https://einaregilsson.com/redirector) browser extension is recommended for use. Configuration:
```
Description: Redirector
Example URL: https://eksisozluk.com/linux--32084
Include pattern: ^https?://(?:.*\.)*(?<!link.)eksisozluk(.*)\.com(/.*)?$
Redirect to: https://DOMAIN$1
Pattern type: Regular Expression
Example result: https://DOMAIN/linux--32084
```

## License

This project is licensed under WTFPL for details, check [LICENSE](LICENSE) file.
