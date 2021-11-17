#!/bin/zsh
# Run from project root.

python3 -m pip install --upgrade pip

mkdir build
pip wheel --wheel-dir ./build .
rm -rf ./src/yearsinpixels_api.egg-info