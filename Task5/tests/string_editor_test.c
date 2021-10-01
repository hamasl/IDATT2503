#include "string_editor.h"
#include <assert.h>
#include <string.h>

int main(){
    char *input = "< & > test";
    char output[4*strlen(input)];
    edit(input, output);
    assert(*output == "&lt &amp &gt test");

    input = "hei hallo";
    memset(output, 0, sizeof(output));
    edit(input, output);
    assert(*output == *input);
    return 0;
}