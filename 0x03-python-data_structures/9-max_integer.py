#!/usr/bin/python3
# 9-max_integer.py


int max_integer(int *my_list, int size) 
{
    int max = my_list[0];
    int i;
    for (i = 1; i < size; i++)
    {
        if (my_list[i] > max)
        {
            max = my_list[i];
            }
    }
    return max;
}
