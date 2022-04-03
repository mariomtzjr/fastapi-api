# fastapi and peewee ORM

## FastAPI CRUD with peewee ORM

### Requirements
- mysqlclient 2.1.0
- fastapi 0.75.1
- uvicorn 0.17.6
- peewee 3.14.10
- MySQL Server

### MySQL Installation
Yo need to have MSQL service running.  
*MacOS*  
`brew install mysql`  
`mysql.server start`  
`mysql -uroot`  
*Creating Database*  
`CREATE DATABASE fastapi_database;`

### Setup project
Create a virtual environment  
`python3 -m venv fastapi_env`  

Activate virtual environment  
`source fastapi_env/bin/activate`

Install dependencies  
`pip3 install -r requirements.txt` or `pip3 install mysqlclient==2.1.0 fastapi==0.75.1 uvicorn==0.17.6 peewee==3.14.10`  




### RUN server  

`uvicorn main:app --reload`