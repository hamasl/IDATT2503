const CryptoJS = require("crypto-js")
const axiosModule = require("axios")
const axios = axiosModule.create(null)
//Using localhost as domain part of frontend salt since this is educational and will therefore only run on localhost
const SALT_CONST = "localhost"
const KEY_SIZE = 512/8
const ITERATIONS = 2048

const signupUsername = document.querySelector("#signup-name")
const signupPassword = document.querySelector("#signup-pass")
const signupBtn = document.querySelector("#signup-btn")
const signupMsg = document.querySelector("#signup-msg")

const loginUsername = document.querySelector("#login-name")
const loginPassword = document.querySelector("#login-pass")
const loginBtn = document.querySelector("#login-btn")
const loginMsg = document.querySelector("#login-msg")

const getHash = (pass, salt) => CryptoJS.PBKDF2(pass, salt, {keySize: KEY_SIZE, iterations: ITERATIONS}).toString()

signupBtn.addEventListener("click", async () => {
    signupMsg.innerHTML = "Loading..."
    let hashed = getHash(signupPassword.value, signupUsername.value + SALT_CONST)
    try{
        let res = await axios.post("./users", {
            username: signupUsername.value,
            password: hashed
        })
        if(res.status === 201){
            signupMsg.innerHTML = "User created. You can now log in."
            return
        }
    }catch(err){
        if(err.response.status === 409){
            signupMsg.innerHTML = "Username is already taken."
        }
    }
    signupMsg.innerHTML = "Could not create user"
})

loginBtn.addEventListener("click", async () => {
    loginMsg.innerHTML = "Loading.."
    //For the case if this Task localhost is the domain name, therefore combining username and domain name as a client salt
    let hashed = getHash(loginPassword.value, loginUsername.value + SALT_CONST)
    try{
        let res = await axios.post("./login", {
            username: loginUsername.value,
            password: hashed
        })
        if(res.status === 201){
            loginMsg.innerHTML = "Logged in."
            axios.defaults.headers["Authorization"] = "Bearer " + res.data.token
            return
        }
    } catch(err){
        if(err.response.status === 401){
            loginMsg.innerHTML = "Invalid username or password."
            return
        }
    }
    loginMsg.innerHTML = "An error occured."  

})
    