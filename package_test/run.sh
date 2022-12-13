python -m venv .venv
source .venv/bin/activate
pip install .
echo '{"state":"package_test"}' > config.json
python package_test/main.py
