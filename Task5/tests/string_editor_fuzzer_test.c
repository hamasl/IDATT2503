#include <assert.h>
#include <stdint.h>
#include <stdlib.h>
#include "string_editor.h"

int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size){
    char *input = (char *)malloc(sizeof(char)*size +1);
    memcpy(input, data, size);
    input[size] = '\0';
    char output[4*strlen(input)];
    edit(input, output);

    free(input);


    return 0;
}