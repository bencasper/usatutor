# usatutor

- .mwb database schema file opened by mysql workbench
- [python manage.py inspectdb](https://docs.djangoproject.com/en/3.0/howto/legacy-databases/)
- [fullcalendar](https://fullcalendar.io/docs)
- ./manage.py initCourse
- ./manage.py migrate --fake yourapp zero

## pre install
- [python3.7.7](https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/)
- [python3.7 -venv](https://docs.python.org/3/library/venv.html)
- [django-suit](https://django-suit.readthedocs.io/en/v2/install.html)
- ##### install suit dev version
    ```shell script
        pip install https://github.com/darklow/django-suit/tarball/v2
    ```
 
- ##### install python mysql essential
    ```shell script
        apt-get install python3-mysqldb libmysqlclient-dev python-dev
    ```
- [mysql8](https://www.tecmint.com/install-mysql-8-in-ubuntu/)
- ufw

## some tools
- ##### del pycahce files
    ```shell script
    find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf  
    ```


