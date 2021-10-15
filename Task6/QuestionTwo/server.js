const SERVER_PORT = 8080
const KEYSIZE = 512/8
const express = require("express")
const app = express()
const CryptoJS = require("crypto-js")
const jwt = require("jsonwebtoken")
//NEVER store a secret this way, this is just for simplifying the task. In production use a .env file
const TOKEN_SECRET = "227ffdfdf0bf4fcfc0f173f39a5cdba7326e04dfb3be43a04072440c68940ee21335efee290bb2ad3ae37338e6a8d0b13ab2aee50a4249f2e26cd840be62445e"

const getHash = (pass, salt) =>  CryptoJS.PBKDF2(pass, salt, {keySize: KEYSIZE, iterations: 2048}).toString()

const createUser = (username, password) => {
    let salt = CryptoJS.lib.WordArray.random(KEYSIZE)
    let hash = getHash(password, salt)
    return {
        username: username,
        salt: salt,
        hash: hash
    }
} 

const users = []

app.use(express.static(__dirname))
app.use(express.urlencoded({
    extended:true}))

app.use(express.json())

app.get("/", (req, res) => {
    res.status(200, {"Content-Type": "text/html" })
    res.sendFile("./index.html", {root: __dirname})
})

app.post("/users", (req, res) => {
    //if user already exists
    if (users.includes(u => u.username === req.body["username"])){
        res.status(409)
        res.send()
        return
    }
    users.push(createUser(req.body["username"], req.body["password"]))
    res.status(201)
    res.send()
})

app.post("/login", (req, res) => {
    let user = users.find(u => u.username = req.body["username"])
    if(user){
        let hash = getHash(req.body["password"], user.salt)
        if(hash == user.hash){
            res.status(201)
            res.json({token: jwt.sign(user.username, TOKEN_SECRET)})
            return
        }
    }
    res.status(401)
    res.send()
})

app.listen(SERVER_PORT, "localhost", () => {console.log(`Server started at port: ${SERVER_PORT}`)})