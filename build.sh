# exit on error
set -o errexit

# poetry install -r requirements.txt
# pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate --noinput
