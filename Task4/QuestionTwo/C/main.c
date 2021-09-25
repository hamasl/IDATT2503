#include <string.h>
#include <stdio.h>

int find_substr(const char* const haystack, const char* const needle, const int start_index){
    for (int i = start_index; i < strlen(haystack)-strlen(needle); ++i){
        int count = 0;
        for(int j = 0; j < strlen(needle); ++j){
            if(haystack[i+j] == needle[j]){
                count++;
            }
        }
        if(count == strlen(needle)){
            return i;
        }
    }
    return -1;
}

//TODO fix that address of local variable is returned
char* substr(const char* const input, int start, int end){
    char str[end-start+1];
    for(int i = start; i < end; ++i){
        str[i-start] = input[i];
    }
    str[end-start] = '\0';
    return str;
}

char* replace_sign(const char* const input, const char* const to_be_replaced, const char* const replace_with){
    char* str;
    strcpy(str, input);

    int index = 0;
    while(index < strlen(str)){
        index = find_substr(str, to_be_replaced, index);
        if(index == -1) index = strlen(str); //breaks while loop condition
        else {
            char* start = substr(str, 0, index);
            //last substring goes from str.length() to str.length() in case the last character is a charcater to be replaced
            //however substr returns an empty string if the start index is equal to the strings length, therefore this does not matter
            str = strcat(strcat(start, replace_with), substr(str, strlen(to_be_replaced)+index, strlen(str)));
            //Increasing (or decreasing) by the difference of the number of characters to be inserted and the number to be removed
            index += strlen(replace_with) - strlen(to_be_replaced);
        }
    }
    return str;
}

char* convert(const char* input){
    return replace_sign(replace_sign(replace_sign(input, "&", "&amp"), "<", "&lt"), ">", "&gt");
}

int main(){
    char *input = "&lorem ip&sum < > <zx>";
    printf("%s has been converted to %s", input, convert(input));
    return 0;
}