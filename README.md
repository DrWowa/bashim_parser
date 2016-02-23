# Testign task #
> 1. Парсер bash.im с сохранением результатов в БД
> 2. Веб морда для просмотра результатов и обновления БД

## Install ##
* Create and activate virtualenv: `virtualenv -p python3 env && source env/bin/activate`
* Install dependencies: `pip install -r reqirements.txt`
* Create and adjust settings. For dev: `cd app && ln -s settings_dev.py settings.py`
* Create database: `./manage.py migrate`
* Create admin: `./manage.py createsuperuser`
