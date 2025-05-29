

# Persons Module for Odoo 16

## Инструкция по запуску проекта

### 1. Подготовка `.env` файла

Создайте файл `.env` в корне проекта (не добавляйте его в git) с содержимым:

```
POSTGRES_DB=postgres
POSTGRES_USER=odoo
POSTGRES_PASSWORD=odoo
```

Этот файл содержит параметры для запуска контейнера базы данных PostgreSQL.

---

### 2. Запуск Docker-контейнеров

Запустите контейнеры с помощью docker-compose:

```bash
docker-compose up -d --build
```

Это запустит два контейнера: базу данных `Postgres` и `Odoo`.

---

### 3. Подключение и настройка Odoo

- Перейдите в браузере на `http://localhost:8069`
- Создайте новую базу данных (например, `test_persons`).
- Авторизуйтесь как администратор.

---

### 4. Обновление списка модулей

- Включите режим разработчика (Developer mode).
- Перейдите в меню **Приложения (Apps)**.
- Нажмите кнопку **Обновить список модулей**.

---

### 5. Установка модуля `Persons`

- Найдите модуль с названием `Persons` в списке приложений.
- Нажмите **Установить**.

---

### 6. Проверка работоспособности

- В веб-интерфейсе Odoo появится меню **Website → Persons** с формами и списками.
- Перейдите по URL `http://localhost:8069/persons` для просмотра последних 5 записей.
- Перейдите по URL `http://localhost:8069/persons/add` для добавления новой записи через веб-форму.

---

## Пример создания записи через веб-форму

1. Откройте `http://localhost:8069/persons/add`
2. Заполните поля:
   - First Name: `Ivan`
   - Last Name: `Petrov`
   - Birthday: `1990-01-01`
   - Sex: `male`
3. Нажмите кнопку "Create".
4. Запись появится в списке по адресу `http://localhost:8069/persons`.

---

## Структура проекта

```
persons/
├── controllers/
│   └── main.py
├── models/
│   └── person.py
├── views/
│   ├── person_views.xml
│   └── person_templates.xml
├── __manifest__.py
├── __init__.py
docker-compose.yml
.env.example
README.md
```

---

