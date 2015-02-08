How to install:

sudo apt-get install -y git
git clone https://github.com/LogvinovLeon/BD_last.git
. BD_last/install.sh

If your port 8000 is used you need to run:
./manage.py runserver 0.0.0.0:PORT
Where PORT is an unused port.
