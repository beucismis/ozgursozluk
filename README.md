<p align="left" width="100%">
<img height="50" src="https://github.com/user-attachments/assets/4893d92e-7077-4e2f-b1d4-ec809123d6ee" alt="ozgursozluk-logo" />
</p>

This project is free alternative Ekşi Sözlük front-end focused on privacy and performance. Made with <3 on the T61. Contributions are most welcome! Offical instance: [https://ozgursozluk.org](https://ozgursozluk.org)

![PyPI - Version](https://img.shields.io/pypi/v/ozgursozluk)
![PyPI - Version](https://img.shields.io/pypi/v/limoon?label=limoon)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ozgursozluk)
![GitHub License](https://img.shields.io/github/license/beucismis/ozgursozluk)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/beucismis/ozgursozluk/publish.yml)
![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fozgursozluk.org%2Fapi%2Fhealtcheck&query=status&label=offical%20instance)

## Features

- No JavaScript Required – works perfectly without JS
- Docker Support – easy deployment and setup
- Topic Search – quickly find relevant discussions
- View Topics, Entries & Authors – browse content and contributors
- Gündem & Debe Page Support – full support for special pages
- Hide Displaying – favorite count, author and entry date
- Entry Images - display images directly from the source
- 10+ Built-in Themes – customize the look with 10+ themes
- Self-Hosted, Ad-Free & Lightweight – fast, simple, and private on your server
- Responsive Design – optimized for mobile and small screens

## Preview

<table>
  <tbody>
    <tr>
      <td><img src="https://github.com/user-attachments/assets/f8dbb7d6-51cb-4f21-85ca-f3e14f0b4a4b"></td>
      <td><img src="https://github.com/user-attachments/assets/2027ac48-0610-4f94-b633-4fe5e78fd123"></td>
      <td><img src="https://github.com/user-attachments/assets/2d932b95-dba8-4ee7-a0bb-a892f5969972"></td>
      <td><img src="https://github.com/user-attachments/assets/9466a1cb-d362-4e6a-9fb9-fbfa0f0aadb4"></td>
      <td><img src="https://github.com/user-attachments/assets/41d75da0-4290-47d2-a0db-88b385fc10fc"></td>
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
docker run -d -p 5000:5000 --name ozgursozluk ozgursozluk
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

## Development

This project uses [Hatch](https://hatch.pypa.io/latest/) for project management.

1.  Install dependencies:
    
    ```
    pip install hatch
    hatch env create
    ```

2.  Run development server: (with hot-reloading)
    
    ```
    hatch run dev
    ```

3.  Format code:
    
    ```
    hatch run format
    ```

## Redirection

[Redirector](https://einaregilsson.com/redirector) browser extension is recommended for use. Configuration:
```
Description: Redirector
Example URL: https://eksisozluk.com/linux--32084
Include pattern: https://eksisozluk.com/*
Redirect to: https://ozgursozluk.org/$1
Pattern type: Wildcard
Pattern Description: https://ozgursozluk.org/linux--32084
Example result: https://ozgursozluk.org/linux--32084
```

## License

This project is licensed under WTFPL for details, check [LICENSE](LICENSE) file.
