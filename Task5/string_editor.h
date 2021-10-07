#pragma once

#include <string.h>

void replace(char * const str, const size_t start_index, const char * const replace_with){
    for (size_t i = 0; i < strlen(replace_with); ++i)
    {
        str[start_index+i] = replace_with[i];
    }
}

/// Note: returns amount of signs changed
size_t edit(const char* const input, char * const output){
    size_t count = 0;
    size_t output_index = 0;
    for(size_t i = 0; i <= strlen(input); ++i){
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