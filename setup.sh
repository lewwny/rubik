#!/usr/bin/env bash

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip -q

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt -q
elif [ -f "pyproject.toml" ]; then
    pip install -e . -q
fi

exec "$SHELL"