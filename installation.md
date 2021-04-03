# Как развернуть RusNLP локально?

## Установка

1. Установить все необходимые библиотеки из [списка](requirements.txt). Можно сделать пакетно через 
   ```pip install -r requirements.txt```
   Для установки gensim может понадобиться Microsoft Visual C++ 14.0. Для этого надо скачать [Build Tools for Visual Studio](https://visualstudio.microsoft.com/downloads/) и выбрать в появившемя окне "Рабочие нагрузки средства сборки" (Visual С++ build tools). И ждать :)
   
   _Решение этой проблемы на [StackOverFlow](https://stackoverflow.com/questions/44951456/pip-error-microsoft-visual-c-14-0-is-required))

1. В code/web положить папку models, которую можно скачать по [ссылке](https://yadi.sk/d/zTBhpXE-M4Nviw).

   #### Содержание code/web/models:
   
   | model | description|
   |-------|------------| 
   | cross_muse_ext.bin | Объединённые в одну модель очищенные от мусора русские и английские эмбеддинги [MUSE](https://github.com/facebookresearch/MUSE), которые мы пополнили векторами слов из текстов статей |
   | common_tok_muse_ext_<версия>*.bin | Вектора всех текстов статей из [базы](https://github.com/rusnlp/rusnlp/blob/master/code/web/data/rus_nlp_20201124.db) и задач из [NLPub.tsv](https://github.com/rusnlp/rusnlp/blob/master/code/web/data/nlpub.tsv) (начинаются с TASK::)|

   Допускаются следующие форматы моделей:
   * .bin(.gz)
   * .vec(.gz), txt(.gz)
   * gensim native
   
1. Указать используемую версию [базы данных] в [rusnlp.cfg](code/web/rusnlp.cfg) и названия моделей векторов в [models.tsv](code/web/models.tsv).

1. В code/web/run_nlp.py заменить static_url_path на абсолютный путь к папке code/web/data (в начале поставить ```/```).

### Запуск

1. Запустите сервер через ```python code/web/nlp_server.py```
2. Запустите веб-интерфейс через ```python code/web/run_nlp.py```
   Совет: можно указать ```debug=True``` в параметрах ```app_rusnlp.run()```, чтобы изменения подгружались автоматически.