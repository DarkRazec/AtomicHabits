# Settings without docker
#python3 -m venv env
#source env/bin/activate
#pip3 install -r requirements.txt
#python3 manage.py migrate
#python3 manage.py collectstatic --no-input
#deactivate

# Settings with docker
docker compose up --build -d
docker compose exec app python manage.py migrate