# Пульт охраны банка / Bank Security Console

## Оглавление / Table of Contents

- [Русский](#русский)
- [English](#english)

---

## Русский

Этот репозиторий предназначен для сотрудников банка «Сияние». Если вы случайно попали сюда, обратите внимание, что без доступа к базе данных запустить проект не удастся. Вы можете изучить код вёрстки и то, как устроены запросы к базе данных.

Пульт охраны — это веб-приложение, которое интегрируется с удалённой базой данных банка. Оно предоставляет доступ к информации о визитах и пропускных карточках наших сотрудников, облегчая мониторинг и управление безопасностью.

### Как установить

1. Python3 должен быть уже установлен.
2. Создайте виртуальное окружение venv для изоляции зависимостей

    ```bash
    python -m venv .venv
    ```

    Активация виртуального окружения:
    - На Windows:
      ```bash
      .venv\Scripts\activate
      ```
    - На MacOS и Linux:
      ```bash
      source .venv/bin/activate
      ```

   Выполните команду:
   ```bash
   pip install -r requirements.txt
   ```

3. Это приложение использует файл .env для хранения конфиденциальных и конфигурируемых параметров настройки.

   В корневом каталоге проекта создайте файл «secret_set.env», каждая переменная среды указывается с новой строки в формате КЛЮЧ=значение. Пример:

   ```plaintext
   DB_ENGINE=***
   DB_HOST=***
   DB_PORT=***
   DB_NAME=***
   DB_USER=***
   DB_PASSWORD=***
   DEBUG=True
   SECRET_KEY=ваш_секретный_ключ
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

   Храните `.env` в безопасности: Убедитесь, что файл .env не попадает в систему контроля версий, как например Git, добавив его в .gitignore.

### Использование

Для запуска проекта используйте команду:

```bash
python manage.py runserver 0.0.0.0:8000
```

### Как проверить работоспособность

#### Логи и ошибки

Следите за выводом в терминале, где вы запустили сервер. Убедитесь, что там нет ошибок или предупреждений, которые могли бы указывать на проблемы с подключением или конфигурацией.

#### Дополнительные страницы

Попробуйте перейти на другие страницы приложения, используя панель навигации или прямые ссылки. Проверьте, что весь функционал работает, как описано в документации (например, доступ к информации о визитах, карточкам и т.д.).

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

---

## English

This is an internal repository for employees of the bank "Siyanie". If you got to this repository by accident, then you will not be able to launch it, because you do not have access to the database, but you can freely use the layout code or see how the queries to the database are implemented.

The security console is a site that can be connected to a remote database with visits and pass cards of our bank employees.

### How to install

1. Python3 should already be installed.
2. Create a virtual environment venv to isolate dependencies

    ```bash
    python -m venv .venv
    ```

    Activating the virtual environment:
    - On Windows:
      ```bash
      .venv\Scripts\activate
      ```
    - On MacOS and Linux:
      ```bash
      source .venv/bin/activate
      ```

   Run the command:
   ```bash
   pip install -r requirements.txt
   ```

3. This application uses a .env file to store sensitive and configurable settings.

   In the root directory of the project create a file "secret_set.env", each environment variable is specified on a new line in the format KEY=value. Example:

   ```plaintext
   DB_ENGINE=***
   DB_HOST=***
   DB_PORT=***
   DB_NAME=***
   DB_USER=***
   DB_PASSWORD=***
   DEBUG=True
   SECRET_KEY=your_secret_key
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

   Keep .env safe: Make sure that the .env file is not checked into a version control system like Git by adding it to .gitignore.

### Usage

To run the project, use the command:

```bash
python manage.py runserver 0.0.0.0:8000
```

### How to check if it works

#### Logs and errors

Monitor the output in the terminal where you started the server. Make sure there are no errors or warnings that could indicate connection or configuration issues.

#### Additional pages

Try to navigate to other pages of the application using the navigation bar or direct links. Check that all functionality works as described in the documentation (e.g. access to visit information, cards, etc.).

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).