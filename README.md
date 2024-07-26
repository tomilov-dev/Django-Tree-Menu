# Инструкции по запуску проекта

Перед запуском проекта следует выполнить несколько действий:
1. **Создайте .env файл по примеру example.env**

2. **Создайте виртуальное окружение**
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install -r requirements.txt
    ```

3. **Выполните миграции:**
    ```sh
    cd test_menu
    python3 -m manage migrate
    ```

4. **Добавьте данные:**
    2.1. Можно через специальную команду (я подготовил данные):
    ```sh
    python3 -m manage create_testdata
    ```
    2.2. Можно вручную - через админку. Предварительно создайте супер-юзера:
    ```sh
    python3 -m manage createsuperuser
    ```

5. **Запустите локальный сервер**
    ```sh
    python3 -m manage runserver
    ```

6. **Перейдите на локальный хост**