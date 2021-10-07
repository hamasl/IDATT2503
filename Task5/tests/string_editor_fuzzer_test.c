#include <assert.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include "string_editor.h"

int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size){
    size_t input_size = sizeof(char)*size +1;
    char *input = (char *)malloc(input_size);
    memcpy(input, data, size);
    input[size] = '\0';
    size_t length = 4*input_size;
    char output[length];
    edit(input, output);

    free(input);


    return 0;
}