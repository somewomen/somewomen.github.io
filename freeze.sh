 #!/bin/bash

python=python3.9

if [ -d ".venv" ]
then
    source .venv/bin/activate
    pip install -r requirements.txt
    $python freeze.py
else
    $python -m venv .venv
    source .venv/bin/activate
    $python -m pip install --upgrade pip
    pip install -r requirements.txt
    $python  freeze.py
fi

