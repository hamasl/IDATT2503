#include <iostream>

std::string replace_sign(std::string input, std::string to_be_replaced, std::string replace_with){
    std::string str = input;
    size_t index = 0;
    while(index < str.length()){
        index = str.find(to_be_replaced, /*(index > 0) ? index+1 :*/ index);
        if(index == std::string::npos) index = str.length(); //breaks while loop condition
        else {
            //last substring goes from str.length() to str.length() in case the last character is a charcater to be replaced
            //however substr returns an empty string if the start index is equal to the strings length, therefore this does not matter
            str = str.substr(0, index) + replace_with + str.substr(to_be_replaced.length()+index, str.length());
            //Increasing (or decreasing) by the difference of the number of characters to be inserted and the number to be removed
            index += replace_with.length() - to_be_replaced.length();
        }
    }
    return str;
}

std::string convert(std::string input){
    return replace_sign(replace_sign(replace_sign(input, "&", "&amp"), "<", "&lt"), ">", "&gt");
}

int main(){
    std::string input = "&lorem ip&sum < > <zx>";
    std::cout << input << " converted to: " <<  convert(input) << std::endl;
    return 0;
}


