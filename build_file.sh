pip install -r requirements.txt
python manage.py tailwind install --no-input
python manage.py tailwind build
python manage.py collectstatic --no-input