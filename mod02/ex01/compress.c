#include <time.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdio.h>

# define TO_ASCII 48
# define DECIMAL 10

void    reverse(char *buffer, char *ref) {
    char holder;

    *buffer = 0;
    while (buffer-- > ref) {
        holder = *ref;
        *ref = *buffer;
        *buffer = holder;
        ref++;
    }
}

void itoa(int num, char *buffer) {
    char    holder;
    char    *ref;

    ref = buffer;
    while (num) {
        *buffer = (num % DECIMAL) + TO_ASCII;
        num /= 10;
        buffer++;
    }
    reverse(buffer, ref);
}

typedef struct s_compress
{
    char    num_buffer[100];
    char    *num_ref;
    char    *in_ref;
    char    *out_ref;
    char    *out_str;
    char    holder;
    int     counter;
    size_t  len;

}   t_compress;

void set_out_str(t_compress *comp) {
    *comp->out_str++ = comp->holder;
    itoa(comp->counter, comp->num_ref);
    while (*comp->num_ref)
        *comp->out_str++ = *comp->num_ref++;
    comp->num_ref = comp->num_buffer;
}

void init_compress(t_compress *comp, char *in_str) {
    comp->len = strlen(in_str);
    comp->out_str = (char *)malloc(comp->len);

    comp->num_ref = comp->num_buffer;
    comp->out_ref = comp->out_str;
    comp->in_ref = in_str;
    comp->holder = *in_str;
    comp->counter = 0;
}

char *compress(char *in_str)
{
    t_compress  comp;

    if (in_str == NULL || *in_str == 0)
        return NULL;

    if (!isalpha(*in_str))
        return NULL;

    init_compress(&comp, in_str);
    for (size_t i = 0; i < comp.len; i++)
    {
        if (comp.holder != *in_str)
            set_out_str(&comp);
        comp.counter++;
    }
    set_out_str(&comp);
    *comp.out_str = 0;
    return comp.out_ref;
}

int main(int argc, char *argvp[])
{
    char test[] = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    char *out_buffer;
    clock_t start, end;
    double cpu_time_used;

    start = clock();

    for (int i = 0; i < 10000; i++)
        out_buffer = compress(test);
    printf("BUFFER: %s", out_buffer);

    end = clock();

    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    printf("Function took %f seconds to execute \n", cpu_time_used);

    free(out_buffer);
    return 0;
}