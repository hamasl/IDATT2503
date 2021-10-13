#include <string>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <openssl/evp.h>

std::string pbkdf2(const std::string &password, const std::string &salt, int keylen){
    std::string hash;
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

std::string recursive_crack(const std::string &hash, const std::string &salt, int max_len, int current_len, std::string attempt){

    //For the sake of runtime I guessed that the password would be in the range 65-122 which includes all english lower and upper case letters, and some more
    for(unsigned char c = 65; c < 123; ++c){
        attempt[current_len-1] = c;
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

std::string crack_pass(const std::string &hash, const std::string &salt, int max_len){
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
    std::string res = crack_pass(hash, salt, 7);
    std::cout << std::endl << "Password is: " << std::endl << res << std::endl;

    return 0;
}