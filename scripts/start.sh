#!/bin/bash
# Run from project root.

pip install -r requirements.txt
export FLASK_ENV=production
export PYTHONPATH="${PYTHONPATH}:/Users/danielgran/Projects/yearsinpixels_api/venv/lib/python3.9/site-packages"
export PYTHONPATH="${PYTHONPATH}:/Users/danielgran/Projects/yearsinpixels_api/src"
python -c "import sys; print(sys.path)"

./venv/bin/python ./src/yearsinpixels_api/Main/Main.py