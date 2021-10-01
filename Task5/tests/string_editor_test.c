#include "string_editor.h"
#include <assert.h>
#include <string.h>

int main(){
    char *input = "< & > test";
    char output[4*strlen(input)];
    edit(input, output);
    assert(strcmp(output, "&lt &amp &gt test") == 0);

    input = "hei hallo";
    memset(output, 0, sizeof(output));
    edit(input, output);
    assert(strcmp(input, output) == 0);
    return 0;
}