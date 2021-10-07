#include <assert.h>
#include <string.h>
#include "string_editor.h"

int main(){
    char *input = "< & > test";
    size_t length = 4*strlen(input);
    char output[length];
    edit(input, output/*, length*/);
    assert(strcmp(output, "&lt &amp &gt test") == 0);


    char *input2 = "hei hallo";
    size_t length2 = 4*strlen(input2);
    char output2[length2];
    edit(input2, output2/*, length2*/);
    assert(strcmp(input2, output2) == 0);

    char *input3 = ">>";
    size_t length3 = 4*strlen(input3);
    char output3[length3];
    edit(input3, output3/*, length3*/);
    assert(strcmp(output3, "&gt&gt") == 0);
    return 0;
}