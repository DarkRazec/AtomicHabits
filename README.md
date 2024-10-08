# AtomicHabits

Данный проект представляет из себя бэкенд часть SPA веб-приложения "трекер полезных привычек"

Приложение, используя чат-бота, отправляет пользователю в телеграмм напоминания этих привычек в формате:

"Я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]"

Для запуска проекта на удаленном сервере (linux) необходимо:

- установить следующие пакеты:
  - nginx
  - docker
  - docker-compose (или docker compose)

- скопировать проект из репозитория

- настроить демон:

# /etc/systemd/system/back.service *back - произвольное название файла
[Unit]
Description=fan_service daemon
After=network.target

[Service]
User=gitlab-runner
Group=www-data
WorkingDirectory=/workdir/project/
ExecStart=/workdir/project/env/bin/gunicorn --access-logfile - 
--workers 3 --bind unix:/workdir/project/project.sock project.wsgi

[Install]
WantedBy=multi-user.target

- настроить nginx:

# /etc/nginx/sites-available/project *project - произвольное название файла
server {
    listen 80;
    server_name oscar-studio.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /workdir/project;
    }

    location /media/ {
        root /workdir/project/;
    }


    location / {
        include proxy_params;
        proxy_pass http://unix:/workdir/project/project.sock;
    }
}

- создать ссылку на данный файл настроек для site-enabled: ln -s /path/to/site-enabled

- запустить само приложение через docker-compose up --build -d (docker compose up --build -d), либо через pipeline gitlab