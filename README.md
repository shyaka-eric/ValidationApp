### setting app
## Step 1
install requirements by running ```pip install requirements.txt```
## Step 2
create.env file in root directory 
add ```DJANGO_SECRET = 'XXXXXXXXXXXXXXX' ``` replace xxx with your SECRET_KEY value
## step 3
add the following codes in settings.py 
````
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.environ.get("DJANGO_SECRET")
````
## Step 4
run ``` python manage.py makemigrations``` and then run ```python manage.py migrate```
## Finally run 
```python manage.py runserver```
