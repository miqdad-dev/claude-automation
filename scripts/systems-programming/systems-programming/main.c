#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX 10
int nums[MAX] = {7, 2, 1, 6, 8, 5, 3, 4, 9, 10};

typedef struct {
    int start, end;
} Params;

void merge(int start, int mid, int end) {
    int temp[MAX];
    int i = start, j = mid + 1, k = 0;

    while (i <= mid && j <= end) {
        if (nums[i] < nums[j])
            temp[k++] = nums[i++];
        else
            temp[k++] = nums[j++];
    }

    while (i <= mid)
        temp[k++] = nums[i++];

    while (j <= end)
        temp[k++] = nums[j++];

    for (i = start; i <= end; i++)
        nums[i] = temp[i - start];
}

void* merge_sort(void* arg) {
    Params* params = (Params*)arg;
    int mid;

    if (params->start < params->end) {
        mid = (params->start + params->end) / 2;

        Params left = {params->start, mid};
        Params right = {mid + 1, params->end};

        pthread_t tid1, tid2;
        pthread_create(&tid1, NULL, merge_sort, &left);
        pthread_create(&tid2, NULL, merge_sort, &right);

        pthread_join(tid1, NULL);
        pthread_join(tid2, NULL);

        merge(params->start, mid, params->end);
    }

    return NULL;
}

int main() {
    int i;
    pthread_t tid;
    Params params = {0, MAX - 1};

    pthread_create(&tid, NULL, merge_sort, &params);
    pthread_join(tid, NULL);

    for (i = 0; i < MAX; i++)
        printf("%d ", nums[i]);

    return 0;
}