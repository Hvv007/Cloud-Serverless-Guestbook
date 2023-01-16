# Деплой и создание инфраструктуры

1. Выставить переменную окружения `FOLDER_ID`
2. Выставить переменные окружения `token`, `cloud_id` и `folder_id` в файле `provider.tf`
3. `terraform init`
4. `terraform apply`
5. Начальное создание элементов инфрастуктуры `./begin.sh`
6. Выставить переменные окружения значениями, которые вывел скрипт
`APP_SERVICE_ACCOUNT_ID`, `DOCUMENT_API_ENDPOINT`, `GUESTBOOK_API_REPOSITORY_NAME`, `GUESTBOOK_API_CONTAINER_ID`, `AWS_ACCESS_KEY_ID` и `AWS_SECRET_ACCESS_KEY`
7. Выдать все необходимые права сервисному аккаунту `./permissions.sh`
8. Поменять в `Backend/openapi.yaml` и `frontend/openapi.yaml` заглушки `APP_SERVICE_ACCOUNT_ID` и `GUESTBOOK_API_CONTAINER_ID` на реальные значения
9. Создаём gateway API `terraform apply -target=yandex_ydb_database_serverless.guestbook_api_gateway`
10. Выставляем переменную окружения `GUESTBOOK_API_GATEWAY` 
11. Вписываем `AWS_ACCESS_KEY_ID` и `AWS_SECRET_ACCESS_KEY` в `object-storage.tf`
12. Создаём бакеты `terraform apply` или `terraform apply -target=yandex_storage_bucket.guestbook_frontend_bucket` 
13. Выставляем переменную окружения `GUESTBOOK_WEBSITE_BUCKET` с соответсвующим значением и в `frontend/openapi.yaml`
14. Создаём gateway для Frontend `terraform apply -target=yandex_api_gateway.guestbook_frontend_gateway`, вывод - ссылка для фронта
15. Создаём таблицы, для этого в папке `Backend` исполняем python скрипт `init_tables.py` 
16. В файле`frontend/src/api.js` указываем значение `GUESTBOOK_API_GATEWAY` 
17. Для деплоя исполняем `Backend/deploy.sh` и `frontend/deploy.sh` 
