#!/usr/bin/env python3
""".env -> JSON converter. Handles comments, empty lines and quoted values."""

import json
import sys


def parse_env(path: str) -> dict:
    result = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: python3 env2json.py <.env-file> [output.json]", file=sys.stderr)
        return 1
    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) > 2 else "env.json"
    data = parse_env(src)
    with open(dst, "w") as f:
        json.dump(data, f, indent=2)
    print(f"{len(data)} variables -> {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
