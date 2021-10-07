#include <string.h>
#include <stdio.h>
#include "string_editor.h"


int main(){
    char *input = "&lorem ip&sum < > <zx> gfde";
    //Worst case is every sign is &, and will be replaced with &amp which is four times as much
    char output[4*strlen(input)];

    char *input2 = "if 2 < 1 && 3 > 4"; 
    char output2[4*strlen(input2)];

    char *input3 = "else is 1<10 && 23 > 8";  
    char output3[4*strlen(input3)];

    size_t changed = edit(input, output);
    printf("%s has been converted to %s by changing %zu characters\n", input, output, changed);
    changed = edit(input2, output2);
    printf("%s has been converted to %s by changing %zu characters\n", input2, output2, changed);
    changed = edit(input3, output3);
    printf("%s has been converted to %s by changing %zu characters\n", input3, output3, changed);
    return 0;
}