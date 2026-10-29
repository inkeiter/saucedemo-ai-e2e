# saucedemo-ai-e2e

Небольшой E2E-тест для учебного сайта [Sauce Demo](https://www.saucedemo.com/),
написанный на Python, Playwright и pytest. Проект также демонстрирует использование AI
как помощника при создании и проверке автотестов.

## Цель теста

Проверить, что пользователь может войти с корректными данными и попасть на страницу товаров:

1. Открыть страницу входа.
2. Ввести логин `standard_user`.
3. Ввести пароль `secret_sauce`.
4. Нажать кнопку **Login**.
5. Проверить, что открылась страница товаров с заголовком `Products`.

## Технологии

- Python 3
- [Playwright для Python](https://playwright.dev/python/)
- [pytest](https://docs.pytest.org/) с плагином `pytest-playwright` (предоставляет фикстуру `page`)
- GitHub Actions для CI

## Требования к окружению

- macOS
- Python 3.9 или новее (`python3 --version`)
- Доступ в интернет (тест выполняется на публичном сайте Sauce Demo)

## Установка (macOS)

```bash
# 1. Создать виртуальное окружение
python3 -m venv .venv

# 2. Активировать его
source .venv/bin/activate

# 3. Установить зависимости
python -m pip install -r requirements.txt

# 4. Установить браузер Chromium для Playwright
python -m playwright install chromium
```

## Запуск теста

```bash
# Запуск теста (Chromium без окна)
python -m pytest

# Подробный вывод
python -m pytest -v

# Запуск с видимым браузером
python -m pytest --headed --slowmo 500
```

## Пример ожидаемого результата

Успешный запуск выглядит примерно так (версии, пути и время будут отличаться):

```text
tests/test_login.py::test_successful_login PASSED                        [100%]

============================== 1 passed in X.XXs ===============================
```

## Структура проекта

```text
saucedemo-ai-e2e/
├── tests/
│   └── test_login.py        # единственный E2E-тест
├── .github/workflows/
│   └── tests.yml            # CI: запускает pytest при push и pull request
├── requirements.txt         # зависимости Python
├── .gitignore
└── README.md
```

Page Object, `conftest.py` и конфигурационные файлы здесь сознательно не используются:
для одного сценария они добавили бы код без практической пользы.

## Что проверяют assertion

- `expect(page).to_have_url(...)` — браузер перешёл на `/inventory.html`,
  то есть вход был принят.
- `expect(page.locator(".title")).to_have_text("Products")` — на странице
  действительно страница товаров, а не просто похожий адрес.

Обе проверки используют автоматические ожидания Playwright (`expect`),
поэтому `sleep` не нужен.

## Ограничения

- Покрыт только успешный вход. Неверные данные, заблокированный пользователь
  и другие сценарии не проверяются.
- Тест работает с чужим публичным сайтом. Если сайт недоступен или изменил разметку,
  тест может упасть по причинам, не связанным с вашим кодом.
- Используется только Chromium.
- Зависимости заданы минимальными версиями, а не зафиксированы точно.
- Workflow GitHub Actions настроен, но ещё не запускался,
  поэтому бейджа статуса CI здесь нет.

## AI-assisted development

AI (Claude) использовался для подготовки теста, `requirements.txt`, workflow GitHub Actions
и этого README. Локаторы взяты из публично доступных примеров для Sauce Demo.
AI здесь только помощник при разработке: в рантайме теста никакой AI-модели нет,
а весь код нужно просмотреть и запустить человеку, прежде чем ему доверять.
