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
//The passwords are what front end send, because the passwords are encrypted in frontend
//Password beloning to test is: password and password belonging to foo is: bar
let str = "345eba0e2a511d67014587747aa642fe0a8a05dc1b6bdfb3f8f5d22d73b5bfebe0984a8eb730f7ca776830e6c4d95ff1d952b3a3\
c568679897ced2ff230df0292f4956f40da2d54c610c61cba97285aac758683cb846eadac26aa2a1f76fc112a632fea8c72911ab6f69c051fcc8d5ea6e71\
b93b8ec1e81df7da577d103763b5a26695c266f845debaf63470e85dd5efd0b359e5dc1628203db563fcc7374284ec144770dc4b9fe8b53679346981a91d6\
d4295ea7ce82115b2a9f9129f207ddc1c1c25dc9ce3380b6788e899dd4b03a674f093b4edf4b47dd6b15b5165fc435c9cda83ea8cd0934839fbf8da9b63189\
835e11b4c9335eb576b7e657ee3f862d0"
const dummyUsers = [createUser("test", "8eaac8a161dc95c9f7e8c2ec5b5c2b4c9b4\
2078752651bf770a78e4c94f6de56656d057037f28d32fe9f5edd49973b6558ac499de4750e476fb28c8b423f24ad9326f5489f361b31a47ab3e8f8\
2c742abba994b681d29533f975512b68ffcd0c38925950b699286805eea821971a31a577421d270d32d63c47a12f35811d43b28dbb30e0bd97a07054\
cb256b3f13bddcd0fff6c54b89e80bd4832457e70c3945b9942673c504289d4f19f1d662457d5c38feb3ebe987b4d27b495b33ae9b9e609b99dc31629\
16366440efbe6fc96e5f9bd0000c5299e5ac1ea9640c37845c2082e3d32220249149094035e81c3555e243755c777ac9fc91e7efb7217d339d25a"),
createUser("foo", str)]

app.use(express.static(__dirname))
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
        console.log(str)
        console.log(req.body["password"])
        console.log(str === req.body["password"])
        if(hash == user.hash){
            console.log("hei")
            res.status(201)
            res.send()
            return
        }
    }
    res.status(401)
    res.send()
})

app.listen(SERVER_PORT, "localhost", () => {console.log(`Server started at port: ${SERVER_PORT}`)})