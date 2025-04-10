# Проект: API приложение по управлению библиотекой
# Описание
Приложение API предоставляет возможности для управления книгами, авторами и пользователями,
а также отслеживает выдачу и возврат книг пользователям. Зарегистрированные пользователи могут просматривать
книги и авторов, добавлять их. При занесении пользователя в группу модераторов у них добавляются права на
редактирование и удаление, а также осуществление процесса выдачи и сдачи книг.

# Стек технологий
* Django: основной фреймворк для разработки веб-приложения.
* DRF: реализация бэкенд-части. 
* PostgreSQL: база данных для хранения информации о пользователях, продуктах и статьях.
* drf-yasg: документация
* JWT
* Docker
* Docker-compose
# Установка: 
1. клонировать репозитарий https://github.com/RVBelyaevsky/Book-Service.git
2. установить Docker с официального сайта https://www.docker.com/.
3. заполнить .env на основе файла .env.sample
4. запустить запустить Doker контейнер командой docker-compose up -d --build,
предварительно перейдя в директорию приложения.
5. Убедиться в работоспособности db-1 контейнера docker
6. Запустить приложение web-1 (предварительно остановив службу PostgeSQL, если она была запущенна локально)
7. После развертывания в браузере перейти по ссылке http://localhost:8000/
# Документация
**http://127.0.0.1:8000/docs/swagger/** - локально
