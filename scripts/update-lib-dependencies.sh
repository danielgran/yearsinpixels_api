#!/bin/bash
# This file must get called out of the project root.
pip uninstall -y ./lib/yearsinpixels_business-0.0.1-py3-none-any.whl
pip uninstall -y ./lib/yearsinpixels_data-0.0.1-py3-none-any.whl

pip install ./lib/yearsinpixels_business-0.0.1-py3-none-any.whl
pip install ./lib/yearsinpixels_data-0.0.1-py3-none-any.whl
