#include <string>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <openssl/evp.h>

std::string pbkdf2(const std::string &password, const std::string &salt, int keylen){
    std::string hash;
    // Sha1 uses bytes
    hash.resize(keylen);
    PKCS5_PBKDF2_HMAC_SHA1((const char *)&password[0], password.size(), (const unsigned char *)&salt[0], salt.size()
        ,2048, keylen,(unsigned char *)&hash[0]);
    return hash;
}

std::string hex(const std::string &input){
    std::stringstream hex_stream;
    hex_stream << std::hex << std::internal << std::setfill('0');
    for (auto &byte : input){
        hex_stream << std::setw(2) << (int)(unsigned char)byte;
    }
    return hex_stream.str();
}

//TODO maybe use &attempt
std::string recursive_crack(const std::string &hash, const std::string &salt, int max_len, int current_len, std::string attempt){

    //Using unsigned short to be able to make c 256 to break for loop, started at 31 for first normal char
    //for(unsigned short c = 31; c < 256; ++c){
    for(unsigned short c = 65; c < 123; ++c){
        attempt[current_len-1] = (unsigned char) c;
        if(current_len < max_len){
           
            std::string res = recursive_crack(hash, salt, max_len, current_len + 1, attempt);
            if(res != "") return res;
        }
        else {
            std::cout << attempt << std::endl;
            if(hex(pbkdf2(attempt, salt, 20)) == hash){
                    return attempt;
            }
        }
    }
    return "";
}

std::string crack_pass_v3(const std::string &hash, const std::string &salt, int max_len){
    std::string attempt;
    for(int i = 1; i <= max_len; ++i){
        attempt = "";
        attempt.resize(i);
        std::string res = recursive_crack(hash, salt, i, 1, attempt);
        if(res != "") return res;
    }
    return "";
}



int main(){

    const std::string hash = "ab29d7b5c589e18b52261ecba1d3a7e7cbf212c6";
    const std::string salt = "Saltet til Ola";
    //sha1 uses 20 as size
    
    std::cout << "Password is: " << crack_pass_v3(hash, salt, 7) << std::endl;

    return 0;
}