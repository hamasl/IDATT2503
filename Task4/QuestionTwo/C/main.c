#include <string.h>
#include <stdio.h>

void move(char * const output, const int start_index, const int amount){
    char temp[amount];
    char temp_helper[amount];
    for (int i = start_index; i < strlen(output) + amount; i += amount)
    {
        if(i < start_index+amount){
            //Is the spacve that is going to be cleared
            for(int j = 0; j < amount; ++j){
                temp[j] = output[i+j];
            }
        } else{
            //Is when we need to move stuff
            for(int j = 0; j < amount; ++j){
                temp_helper[j] = output[i+j];
                output[i+j] = temp[j];
                temp[j] = temp_helper[j];
            }
        }
    }
    
}

void replace(char * const str, const int start_index, const char * const replace_with){
    move(str, start_index, strlen(replace_with));
    for (int i = 0; i < strlen(replace_with); ++i)
    {
        str[start_index+i] = replace_with[i];
    }
}

/// Note: returns amount of signs changed
int edit(const char* const input, char * const output){
    int count = 0;
    int output_index = 0;
    for(int i = 0; i < strlen(input); ++i){
        //printf("\n%d\n", (i+output_index));
        switch (input[i])
        {
        case '&':
            count++;
            const char* amp = "&amp";
            replace(output, i+output_index, amp);
            output_index += strlen(amp)-1;
            break;
        case '<':
            count++;
            const char* lt = "&lt";
            replace(output, i+output_index, lt);
            output_index += strlen(lt)-1;
            break;
        case '>':
            count++;
            const char* gt = "&gt";
            replace(output, i+output_index, gt);
            output_index += strlen(gt)-1;
            break;
        default:
            output[i+output_index] = input[i];
            break;
        }
    }
    return count;
}

int main(){
    char *input = "&lorem ip&sum < > <zx>";  
    //Worst case is every sign is &, and will be replaced with &amp which is four times as much
    char output[4*strlen(input)];

    char *input2 = "if 2 < 1 && 3 > 4";  
    char output2[4*strlen(input2)];

    char *input3 = "else is 1<10 && 23 > 8";  
    char output3[4*strlen(input3)];

    int changed = edit(input, output);
    printf("%s has been converted to %s by changing %d characters\n", input, output, changed);
    changed = edit(input2, output2);
    printf("%s has been converted to %s by changing %d characters\n", input2, output2, changed);
    changed = edit(input3, output3);
    printf("%s has been converted to %s by changing %d characters\n", input3, output3, changed);

    return 0;
}