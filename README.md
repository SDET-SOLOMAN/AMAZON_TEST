Нужно проверить вы находитесь в вертуальном окружении или нет
- открываем terminal и смотрим. Есои строка начинается с (venv)
- если нет то создаем вертуальное окружение https://habr.com/ru/articles/491916/
- также можете попробовать так:
- Создание виртуального окружения Pycharm
pip install virtualenv
install virtualenv venv  
pip install -r requirements.txt установка пакетов из файла
activate  venv\Scripts\activate


Команды для работы над репозиторием
1. git clone <> (клонируем репозиторий на локальную машину)
2. git checkout test (переключаемся на ветку test)
3. git pull (если клонировали репозиторий не только что)
4. git checkout -b <имя нашей ветки> (создаем новую ветку для работы из ветки test и сразу переключаемся на нее)
5. git add . (добавляем изменения в нашу ветку)
6. git commit -m "Описание изменений" (создаем коммит для нашей ветки)
7. git push -u origin <имя нашей ветки> (пушим нашу ветку в репозиторий)

запуск отдельного файла pytest -s -v имя файла:
pytest -s -v --setup-show файл покажит какие фиктуры и настройки запускаються

запуск файла с маркировкой "smoke", "regression":
pytest -s -v -m "smoke or regression" имя файла

Установка allure:
pip install allure-pytest

запуск файла с allure:
 имя файла (results - имя папки куда будут сохранятся отчеты. Можно называть как будет удобно)
pytest -s -v --alluredir results (создасться пака с директорией results)

Нужно быть в директории tests
pytest -s -v -m "smoke" --alluredir=login/test_login_page.py (запуск тескейсов test_login_page
                                                              с пометкой "smoke" c папки login )


запуск allure:
allure serve results (запуск отчетов с папки results)
Нужно быть в директории tests/login
Запуск отчетов с папки login/results
allure serve results

сгенерировать отчет allure для запуска в любом месте:
allure generate result
   
