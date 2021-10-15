# Question two

## Task
Create a server and a client, were the client authenticates against the server via PBKDF2. Both the client and server should hash the password.
Using HTTPS was not necessary. It was possible to pretend that it was in use which I did.
Voluntarily a token can be returned from the authentication.

## Prerequisites
* npm
* node

## Packages in use
* express
* CryptoJS
* browserify
* axios
* jsonwebtoken

## Run
To install the packages in use, use the command:
```
make install
```
After tha packages have been installed the serve can be run through:
```
make run
```

When the server has been started go to the browser and enter localhost:8080 to see the webpage