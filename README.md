### Project DJ
===
## Papar Information
- Title:  `Project DJ`
- Authors:  `veeeelme`

## Dependences
- python
- django

### Install 

- Install Django 4.2.4 or above
  ```
  pip install django
  ```
- Clone this repo
- Jump to repository folder

## Use

- Run django server:
  ```
  python(3) manage.py runserver
  ```
- Go to http://127.0.0.1:8000/

## Directory Hierarchy
```
|—— .DS_Store
|—— Pipfile.lock
|—— api
|    |—— __init__.py
|    |—— __pycache__
|        |—— __init__.cpython-310.pyc
|        |—— authentication.cpython-310.pyc
|        |—— models.cpython-310.pyc
|        |—— urls.cpython-310.pyc
|    |—— admin.py
|    |—— apps.py
|    |—— authentication.py
|    |—— migrations
|        |—— __init__.py
|    |—— models.py
|    |—— tests.py
|    |—— urls.py
|    |—— views.py
|—— base
|    |—— .DS_Store
|    |—— __init__.py
|    |—— __pycache__
|        |—— __init__.cpython-310.pyc
|        |—— settings.cpython-310.pyc
|        |—— urls.cpython-310.pyc
|        |—— wsgi.cpython-310.pyc
|    |—— asgi.py
|    |—— settings.py
|    |—— urls.py
|    |—— wsgi.py
|—— db.sqlite3
|—— manage.py
|—— shop
|    |—— __init__.py
|    |—— __pycache__
|        |—— __init__.cpython-310.pyc
|        |—— admin.cpython-310.pyc
|        |—— apps.cpython-310.pyc
|        |—— models.cpython-310.pyc
|        |—— urls.cpython-310.pyc
|        |—— views.cpython-310.pyc
|    |—— admin.py
|    |—— apps.py
|    |—— migrations
|        |—— 0001_initial.py
|        |—— 0002_alter_course_title.py
|        |—— __init__.py
|        |—— __pycache__
|            |—— 0001_initial.cpython-310.pyc
|            |—— 0002_alter_course_title.cpython-310.pyc
|            |—— __init__.cpython-310.pyc
|    |—— models.py
|    |—— tests.py
|    |—— urls.py
|    |—— views.py
|—— templates
|    |—— base.html
|    |—— shop
|        |—— courses.html
|        |—— single_course.html
```
### Tested Platform
- software
  ```
  OS: macOS Monterey 12.6.6
  Python: 3.10.10
  Django: 4.2.4

  ```
- hardware
  ```
  CPU: Intel Core i5 (2 core, 2,9 GHz)
  GPU: Intel Iris Graphics 6100 1536 MB
  ```
  
## License

MIT License

Copyright (c) 2023 veeeelme

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.