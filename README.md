# dotenv-to-json

A single-file, dependency-free converter from `.env` to JSON.

```bash
python3 env2json.py .env config.json
```

- Skips comment lines (`#`) and empty lines.
- Strips surrounding quotes from values.
- Useful when an app expects config as JSON but your staging env uses dotenv files.
