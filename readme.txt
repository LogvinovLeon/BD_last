1. Klonujemy repo
2. Tworzymy nowego virtualenv'a: virtualenv venv
3. Aktywujemy virtualenv'a: . venv/bin/activate
4. Wchodzimy do folderu z projektem: cd BD_last/BD_polls
5. Wpisujemy "pip install -r requirements.txt"
6. Wchodzimy do folderu DB_project i robimy:
export PYTHONPATH=$PYTHONPATH:$(pwd)
8. Zmieniamy plik settings.py. Tam trzeba podmienić ustawienia bazy.
7. wychodzimy z tego folderu.
8. Odpalamy migracje: ./manage.py migrate
9. Synchronizujemy bazę: ./manage.py syncdb
10. Odpalamy server: ./manage.py runserver 0.0.0.0:8042
11. Czytamy tutki do Django-cms user-side.
11. Jeśli chcemy dodać raporty, to tworzymy stronę, wchodzimy do ustawień adwanced i dodajemy appk'e raporty.
12. Jesteśmy szczęśliwi.
