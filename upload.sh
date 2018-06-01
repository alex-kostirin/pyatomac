#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
sudo rm -rf ${DIR}/dist
sudo rm -rf ${DIR}/build
sudo rm -rf ${DIR}/atomac.egg-info

python setup.py sdist
python setup.py bdist_wheel
python3 setup.py bdist_wheel
twine upload dist/*