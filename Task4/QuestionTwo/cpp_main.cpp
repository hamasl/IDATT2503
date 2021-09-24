#include <iostream>

std::string replace_sign(std::string input, std::string to_be_replaced, std::string replace_with){
    std::string str = input;
    size_t index = 0;
    while(index < str.length()){
        index = str.find(to_be_replaced, (index > 0) ? index+1 : index);
        if(index == std::string::npos) index = str.length(); //brekas while loop condition
        else {
            str = str.substr(0, index) + replace_with + str.substr(to_be_replaced.length()+index-1, str.length());
        }
        std::cout << index << std::endl;
        std::cout << str.length() << std::endl;
    }
    return str;
}

std::string convert(std::string input){
    return replace_sign(replace_sign(replace_sign(input, "&", "&amp"), "<", "&lt"), ">", "&gt");
}

int main(){
    std::string input = "lorem ip&sum < > <zx";
    std::cout << input << " converted to: " <<  convert(input) << std::endl;
    return 0;
}