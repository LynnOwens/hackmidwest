WORKING_DIR=$PWD
apt install node-js npm python3
if [[ ! -f get-pip.py ]]; then
  wget https://bootstrap.pypa.io/get-pip.py
  python3 get-pip.py
fi
pip install -r requirements.txt
cd twitter-client || exit
npm install
cd "$WORKING_DIR" || exit


