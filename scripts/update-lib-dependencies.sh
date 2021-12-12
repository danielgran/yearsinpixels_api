#!/bin/bash
# This file must get called out of the project root.
pip uninstall -y yearsinpixels-business
pip uninstall -y yearsinpixels-data

pip install ./lib/yearsinpixels_business-0.0.1-py3-none-any.whl
pip install ./lib/yearsinpixels_data-0.0.1-py3-none-any.whl
