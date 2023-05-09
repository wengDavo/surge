# SURGE  

## PROJECT DESCRIPTION  
What does Surge hope to achieve, it strives to reduce the difficulty which arises when trying to gather ***detailed*** information on a cryptocurrency
<br>
<br>
Using **Django** and its related technologies to provide a secure and maintainable website for our users
<br>
This wasn't an easy task, as I had a lot to tackle along the way, there are also a lot of features I would love to implement in the future, especially with the User design and Itnerface
<br><br><br>

## Installation and Setup
### Requrements
-  *PYTHON* - make sure you have python installed and configured appropriately  
- *GIT* - make sure you have git installed on your local machine
- A working knowledge of the Python-Django library 
- NOTE - `ALL THE COMMANDS HIGHLIGHTED SHOULD BE RUN IN THE ROOT OF THE FOLDER`
### Setup
- Clone the Project From Github to a new folder  
`git cloone <repository-url>`  

- Inspect the file to make sure they are all present  

- Creat a new virtual Environment  
`py -m venv my_venv`  

- Activate newly created virtual Environment  
`my_venv\Scripts\activate`  

- Install all dependencies using pip  
`pip install -r requirements.txt`  

- List all the dependecies  
`pip freeze > requirements.txt`  

- Create A Secret Key in    
```
my_site\settings.py
```    
look for this line  
```
SECRET_KEY = env('SECRET_KEY')
```  
insert your secret key, you could generate this with Djecrety  
```
SECRET_KEY = your_secret_key
```` 

- Create A Database -> we need to install a databse to handle the data, however I won't be going over this step seeing as there are diffrent types of Databases, you can choose the database that you are comfortable with

- Once You have properly Configured The Databse  
```
my_site\settings.py
```  
look for this portion of code and configure according to your database 
``` 
DATABASES = {  
    'default': {   
        'ENGINE': 'django.db.backends.your_databse',   
        'NAME': 'your_db_name',  
        'USER':'your_username',  
        'PASSWORD':'your_password'  
    }  
}
```    
- Migrate Project To Databse  
`python manage.py makemigrations`  
`python manage.py migrate`  

- Populate the Database by running this script->this might take a while   
`python manage.py runscript populate`

- Run The Project  
`python manage.py runserver`  

Hopefully everything went well and there were no errors  
Open http://127.0.0.1:8000 on a web browser and you should the landing page  

<br><br><br>
## Brief Overview  
### The Landing Page
![screenshot landing page](static\pictures\screenshot-landing.png)
![screenshot-landing](https://user-images.githubusercontent.com/107735530/237018445-a94b25ea-8bc8-4711-8895-1205c86b2279.png)


From the landing page users can Signup or Login, this is required to get acces to the application
<br>
### The Login Page
![screenshot login page](static\pictures\screenshot-login.png) 
![screenshot-login](https://user-images.githubusercontent.com/107735530/237018731-8e1375e9-a3b4-4345-aa59-66370b7517f4.png)


<br>
### The signup Page
![screenshot signup page](static\pictures\screenshot-signup.png)   
![screenshot-signup](https://user-images.githubusercontent.com/107735530/237018575-2d251d1b-86ba-4a79-a2e5-00ac6765ecb9.png)


<br>
### The Crypto Page  
![screenshot signup page](static\pictures\screenshot-all.png)  
![screenshot-all](https://user-images.githubusercontent.com/107735530/237018805-fc73c057-ad9b-4316-b783-8199330c5cde.png)


<br><br>
As stated this was just a brief overview of the whole application, You could check the live project or clone the project  

<br>

## Credits  
Weng Davo (me)
