# hotel-management-system
Hotel Management System for ERP Final Project at IB IT&amp;B
## How to run the website locally

### Change directory to project folder (hotel-management-system)
```
cd path\to\the\project\folder
```

### Activate Virtual Environment
```
hms-venv\Scripts\activate
```

### Install pip package
```
pip install -r requirements.txt
```

### Change directory to backend folder
```
cd backend
```

### Run make migration
```
py manage.py makemigrations
```

### Run migration
```
py manage.py migrate
```

### Run project on the server
```
py manage.py runserver
```
