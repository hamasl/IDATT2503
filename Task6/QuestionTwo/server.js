const SERVER_PORT = 8080
const KEYSIZE = 512/8
const express = require("express")
const app = express()
const CryptoJS = require("crypto-js")

const createUser = (username, password) => {
    let salt = CryptoJS.lib.WordArray.random(KEYSIZE)
    let hash = CryptoJS.PBKDF2(password, salt, {
        keySize: KEYSIZE,
        iterations: 2048
    }).toString()
    return {
        username: username,
        salt: salt,
        hash: hash
    }
} 

//DUMMY users
//Never do this in an actual application
const dummyUsers = [createUser("test", "password"), createUser("FOO", "BAR")]

app.use(express.urlencoded({
    extended:true}))

app.use(express.json())

app.get("/", (req, res) => {
    res.status(200, {"Content-Type": "text/html" })
    res.sendFile("./index.html", {root: __dirname})
})

app.post("/login", (req, res) => {
    let user = dummyUsers.find(u => u.username = req.body["username"])
    if(user){
        let hash = CryptoJS.PBKDF2(req.body["password"], user.salt, {
            keySize: KEYSIZE,
            iterations: 2048
        }).toString()
        if(hash == user.hash){
            res.status(200)
            res.send()
            return
        }
    }
    res.status(401)
    res.send()
})

app.listen(SERVER_PORT, "localhost", () => {console.log(`Server started at port: ${SERVER_PORT}`)})