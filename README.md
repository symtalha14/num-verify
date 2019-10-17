# num-verify
A simple REST API in Django 2.2 used for verification of phone numbers across the World.

For a detailed Documentation , visit [Num-Verify Docs](https://num-verify.herokuapp.com/docs)

Request Parameters:
```
NUM : phone number that needs to be checked 
NUM_PRE : phone number prefix  
```

**URL to the API :**
 https://num-verify.herokuapp.com/

Making Requests ,
Routes:

```
GET: api/fetch/all
```
This will fetch all the records from the database , if used with hosted version.

```
POST: api/fetch/
```
Send data in the form of JSON,x-www-form-urlencoded,html to this POST route.

*If you want to download this repo and use it as a stand-alone app in your project , please refer to the docs before proceeding , for information on how to initiate the database , [Docs](https://num-verify.herokuapp.com/docs)*
