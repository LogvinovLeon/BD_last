cd BD_last
virtualenv venv
. venv/bin/activate
cd BD_polls
pip install -r requirements.txt
export PYTHONPATH=$PYTHONPATH:$(pwd)/DB_project
./manage.py makemigrations
./manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell
./manage.py runserver 0.0.0.0:8000
