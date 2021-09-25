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

/// NOTE function is unsafe does not check for the capacity of the output string
char* substr(const char* const input, char * const output, int start, int end){
    for(int i = start; i < end; ++i){
        output[i-start] = input[i];
    }
    output[end-start] = '\0';
    return output;
}

char* replace_sign(const char* const input, char* output, const char* const to_be_replaced, const char* const replace_with){
    int index = 0;
    while(index < strlen(output)){
        index = find_substr(output, to_be_replaced, index);
        if(index == -1) index = strlen(output); //breaks while loop condition
        else {
            char start[index];
            substr(output, start, 0, index);
            //last substring goes from str.length() to str.length() in case the last character is a charcater to be replaced
            //however substr returns an empty string if the start index is equal to the strings length, therefore this does not matter
            char end[strlen(output)-strlen(to_be_replaced)+index];
            substr(output, end, strlen(to_be_replaced)+index, strlen(output));
            output = strcat(strcat(start, replace_with), end);
            //Increasing (or decreasing) by the difference of the number of characters to be inserted and the number to be removed
            index += strlen(replace_with) - strlen(to_be_replaced);
        }
    }
    return output;
}

char* convert(const char* input, char* output){
    strcpy(output, input);
    //Need to do & first to not trigger on tem apersand in &lt and &gt
    replace_sign(input, output ,"&", "&amp");
    char temp[strlen(output)];
    strcpy(temp, output);
    replace_sign(temp, output, "<", "&lt");
    strcpy(temp, output);
    replace_sign(temp, output, ">", "&gt");
    return output;
}

int main(){
    char *input = "&lorem ip&sum < > <zx>";
    //Worct case is every sign is &, and will be replaced with &amp which is four times as much
    char output[4*strlen(input)];
    printf("%s has been converted to %s", input, convert(input, output));
    return 0;
}