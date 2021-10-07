const CryptoJS = require("crypto-js")
const axios = require("axios")

const username = document.querySelector("#name")
const password = document.querySelector("#pass")
const btn = document.querySelector("#btn")
const msg = document.querySelector("#msg")

btn.addEventListener("click", () => {
    console.log(username.value)
    console.log(password.value)
    //For the case if this Task localhost is the domain name, therefore combining username and domain name as a client salt
    let hashed = CryptoJS.PBKDF2(password.value, username.value + "localhost", {keySize: 512/8})
    axios.post("./login", {
        username: username.value,
        password: hashed
    })
})
    