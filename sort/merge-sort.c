#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <time.h>

void dump_arr(int *arr, int len)
{
    int i;
    printf("[");
    for (i = 0; i < len; i++)
        printf("%d%s", arr[i], i != len - 1 ? ", " : "]");
}

void merge_sort(int *arr, int *buffer, int len)
{
    if (len > 1) {
        int left_len = len / 2, right_len = len - left_len;
        int *left = arr, *right = arr + left_len;
        int *left_buffer = buffer, *right_buffer = buffer + left_len;

        merge_sort(left, left_buffer, left_len);
        merge_sort(right, right_buffer, right_len);

        int i = 0, l = 0, r = 0;
        while (l < left_len && r < right_len) {
            if (left[l] < right[r]) {
                buffer[i++] = left[l++];
            } else {
                buffer[i++] = right[r++];
            }
        }
        while (l < left_len) {
            buffer[i++] = left[l++];
        }
        while (r < right_len) {
            buffer[i++] = right[r++];
        }
        for (i = 0; i < len; i++) {
            arr[i] = buffer[i];
        }
    }
}

void init_rand_seed()
{
    int seed;
    FILE *fp = fopen("/dev/urandom", "rb");
    fread(&seed, sizeof(seed), 1, fp);
    fclose(fp);
    srand(time(NULL) ^ seed);
}

void test_merge_sort(int size)
{
    int i, *arr, *buffer;
    arr = (int *)malloc(size * sizeof(int));
    buffer = (int *)malloc(size * sizeof(int));
    FILE *fp = fopen("/dev/urandom", "rb");
    fread(arr, sizeof(int), size, fp);
    fclose(fp);
    // for (i = 0; i < size; i++)
    //     arr[i] = rand();
    merge_sort(arr, buffer, size);
    bool go = true;
    for (i = 1; go && i < size; i++)
        if (arr[i - 1] > arr[i])
            go = false;
    free(arr);
    free(buffer);

    printf("Test %d ... %s\n", size, go ? "pass" : "failed");
    fflush(stdout);
}

int main ()
{
    init_rand_seed();
    test_merge_sort(10);
    test_merge_sort(100);
    test_merge_sort(1000);
    test_merge_sort(10000);
    test_merge_sort(100000);
    test_merge_sort(1000000);
    return 0;
}
