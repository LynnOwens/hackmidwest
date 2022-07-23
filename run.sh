WORKING_DIR=/repos/hackmidwest
apt install node-js npm python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
pip install -r requirements.txt
cd twitter-client || exit
npm install
cd $WORKING_DIR
cd website
python3 main.py 146.190.42.170 80

