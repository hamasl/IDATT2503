const CryptoJS = require("crypto-js")
const axios = require("axios")

const username = document.querySelector("#name")
const password = document.querySelector("#pass")
const btn = document.querySelector("#btn")
const msg = document.querySelector("#msg")

btn.addEventListener("click", async () => {
    console.log(username.value)
    console.log(password.value)
    //For the case if this Task localhost is the domain name, therefore combining username and domain name as a client salt
    let hashed = CryptoJS.PBKDF2(password.value, username.value + "localhost", {keySize: 512/8, iterations: 2048}).toString()
    try{
        let res = await axios.post("./login", {
            username: username.value,
            password: hashed
        })
        if(res.status == 201){
            msg.innerHTML = "Logged in."
            return
        }
    } catch(err){
        if(err.response.status === 401){
            msg.innerHTML = "Invalid username or password."
            return
        }
    }
    msg.innerHTML = "An error occured."  

})
    