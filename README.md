

# django-pymongo
To show how we can connect django projects to mongodb using pymongo driver

## Django and MongoDB Setup

To get the integration working, you should have a Django and MongoDB setup. If you have Python on your machine, you can install Django using pip. If you wish to install Django in a specific environment, instead of the whole system, you can create a virtual environment. Use pip/pip3 depending on your Python version: 


### Install:

Windows:
```bash
pip install virtualenvwrapper-win
```

Mac OS / Linux:
```bash
pip install virtualenvwrapper
```

### Create:

Windows:
```bash
mkvirtualenv MyProjectEnvt
```

Mac OS / Linux:
```bash
virtualenv MyProjectEnvt
```

### Activate:

Mac OS / Linux:
```bash
source MyProjectEnvt/bin/activate
```

Windows:
```bash
workon MyProjectEnvt
```

To deactivate the virtual environment, you can just type the command deactivate


Now install Django using pip install Django
To start a Django project, go to the folder where you want to start the project and use 
django-admin startproject <project_name>. 


For example,
```bash
C:\Users\myuser\project_files>django-admin startproject MyFirstDjangoProj
C:\Users\myuser\project_files>cd MyFirstDjangoProj
```

To create an app, use the command, 
```bash
python manage.py startapp myfirstapp
```

If you are using the Python version >= 3.0, replace python with python3 in your commands.
Inside the app, we can have many models that will be mapped to the collections and documents in MongoDB.
Once you start the project, all the files will be available in the project folder. Start the server using the python manage.py runserver command

That’s about our Django setup.
If you don’t already have a MongoDB setup, use MongoDB Atlas, to make the most of cloud hosting. Atlas works seamlessly with all the major cloud providers.

## Connect Django and MongoDB using PyMongo

PyMongo is the official Python driver for MongoDB. It is very efficient for writing JSON data to MongoDB and you can use MongoDB queries in the Python code itself. We can retrieve data in a dictionary like syntax using PyMongo.
Install PyMongo easily using the pip/pip3 command:
pip install pymongo[snappy,gssapi,srv,tls]


If you are using a virtual environment (which you are!), you have to install pymongo in ..\venv\Lib\site-packages folder.
Also install dnspython for using mongodb+srv:// URIs with the command:
pip install dnspython


Using PyMongo, we can concurrently run multiple databases, by specifying the right database name to the connection instance.
Let us create a sample pymongo session. There are two approaches for this:
We can create a client in the utils file that can be used by any view that wants to interact with MongoDB. Create a utils.py file in your project folder (same location as manage.py) and instantiate the client:

```python
from pymongo import MongoClient
def get_db_handle(db_name, host, port, username, password):

    client = MongoClient(host=host,
                         port=int(port),
                         username=username,
                         password=password
                        )
    db_handle = client['db_name']
    return db_handle, client
```

This method can then bebe used in ./myfirstapp/view.py. 
Another approach to get the connection is to use the connection_string:
```python
from pymongo import MongoClient
client = pymongo.MongoClient('connection_string')
db = client['db_name']
```
where,
```python
connection_string = mongodb+srv://<username>:<password>@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majoritymongodb+srv://<username>:<password>@<ip-address>:<port>/<database_name>
```


For example,
```python
makemytrip_db = client['makemytrip']
#collection object
trips_collection = makemytrip_db['trips']
```

You may have seen the ‘Connection’ class being used in other code samples or tutorials – Connection has been deprecated, so don’t use it. 
If you are on a default port and host, simply call MongoClient(). To connect to localhost, we can specify host and port explicitly as: MongoClient(‘localhost’, 27017) or use the URL format MongoClient(‘mongodb://localhost: 27017/’)
Since we have created the client here, we need to comment the DATABASES section in settings.py file. Comment the same using triple quotes.

## Django and MongoDB Tutorial 
In this quick tutorial, we will demonstrate how to use pymongo to do simple CRUD operations. For this, let’s create a pymongo session:

```python
import pymongo
connect_string = 'mongodb+srv://<username>:<password>@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majority' 

from django.conf import settings
my_client = pymongo.MongoClient(connect_string)

Define the database name
dbname = my_client['sample_medicines']

Get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
collection_name = dbname["medicinedetails"]

Create two documents
medicine_1 = {
    "medicine_id": "RR000123456",
    "common_name" : "Paracetamol",
    "scientific_name" : "",
    "available" : "Y",
    "category": "fever"
}
medicine_2 = {
    "medicine_id": "RR000342522",
    "common_name" : "Metformin",
    "scientific_name" : "",
    "available" : "Y",
    "category" : "type 2 diabetes"
}


Insert the documents
collection_name.insert_many([medicine_1,medicine_2])


Check the count
count = collection_name.count()
print(count)

Read the documents
med_details = collection_name.find({})


Print on the terminal
for r in med_details:
    print(r["common_name"])


Update one document
update_data = collection_name.update_one({'medicine_id':'RR000123456'}, {'$set':{'common_name':'Paracetamol 500'}})

Delete one document
delete_data = collection_name.delete_one({'medicine_id':'RR000123456'})
```
Connect to your MongoDB Atlas cluster to see the changes.

README.md
Displaying README.md.
