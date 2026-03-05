# kicka5h.github.io

Personal portfolio site built as a browser-based desktop OS.

Live site: [kicka5h.github.io](https://kicka5h.github.io)

---

## Building for GitHub Pages

Run this before pushing to generate the static `index.html` served by GitHub Pages:

```bash
python build.py
```

This writes `index.html` to the repo root. Commit and push that file to deploy.

---

## Running with Docker

### Using Docker Compose (recommended)

```bash
docker compose up --build
```

The site will be available at [http://localhost:5000](http://localhost:5000).

To run in the background:

```bash
docker compose up --build -d
```

To stop:

```bash
docker compose down
```

### Using Docker directly

```bash
docker build -t portfolio .
docker run -p 5000:5000 portfolio
```
