# A file of different sorting algorithms.
import pygame
def draw_list(draw_info, color_positions={}, clear_bg=False):
    if clear_bg == True:
        clear_rect = (draw_info.side_padding // 2, draw_info.top_padding, draw_info.width - draw_info.side_padding, draw_info.height - draw_info.top_padding)
        pygame.draw.rect(draw_info.window, draw_info.background_color, clear_rect)
    lst = draw_info.lst
    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - ((val - draw_info.min_val) * draw_info.block_height)
        color = draw_info.gradients[i % 3]
        if i in color_positions:
           color =  color_positions[i]
        pygame.draw.rect(draw_info.window, color, (x,y,draw_info.block_width,draw_info.height))
    if clear_bg:
        pygame.display.update()


# Bubble sort algorithm
def bubble_sort(draw_info): 
    lst = draw_info.lst
    length = len(lst)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if num1 > num2:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                draw_list(draw_info, {j: draw_info.green,
                                      j+1: draw_info.red}, True)
                yield True
    return lst

# Insertion Sort Algorithm
def insertion_sort(draw_info):
    lst = draw_info.lst
    length = len(lst)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if lst[j - 1] > lst[j]:
                lst[j-1],lst[j] = lst[j], lst[j-1]
                draw_list(draw_info, {j-1: draw_info.green,
                                      j: draw_info.red}, True)
                yield True
    return lst
def mult(a, b):
    return(a + b + 100)
    
# Quick_sort_range is used to recurse on the divided lists.
def quick_sort_range(draw_info, lst, first, last):
    if (last <= first):
        return lst
    pivot = lst[first]
    pos = last
    for i in range(last, first, -1):
        if (lst[i] > pivot):
            lst[pos],lst[i] = lst[i],lst[pos]
            draw_list(draw_info, {pos: draw_info.green,
                                      i: draw_info.red}, True)
            pos += -1
    lst[first],lst[pos] = lst[pos],lst[first]
    draw_list(draw_info, {pos: draw_info.green,
                                      i: draw_info.red}, True)
    quick_sort_range(draw_info,lst, first, pos - 1)
    quick_sort_range(draw_info,lst, pos + 1, last)

# Quick sort algorithm
def quicksort(draw_info):
    lst = draw_info.lst
    quick_sort_range(draw_info, lst, 0, len(lst) - 1)
    yield True
    return lst
# Merge Sort Algorithm
def mergesort(draw_info):
    yield True
    return mergesort_i(draw_info, draw_info.lst, 0, len(draw_info.lst) - 1)
def mergesort_i(draw_info, arr, l, r):
    if (l < r):
        m = l + (r - l) // 2
        mergesort_i(draw_info, arr, l, m)
        mergesort_i(draw_info, arr, m + 1, r)
        merge(draw_info, arr, l, m, r)
        return arr

def merge(draw_info, arr, start, mid, end):
    start2 = mid + 1
    if (arr[mid] <= arr[start2]):
        return arr
    while (start <= mid and start2 <= end):
        if (arr[start] <= arr[start2]):
            start += 1
        else:
            value = arr[start2]
            index = start2
            while (index != start):
                arr[index] = arr[index - 1]
                draw_list(draw_info, {index: draw_info.green,
                                      index - 1: draw_info.red}, True)
                index -= 1
 
            arr[start] = value
            draw_list(draw_info, {start: draw_info.green,
                                      start - 1: draw_info.red}, True)
            start += 1
            mid += 1
            start2 += 1

def shellsort(draw_info):
    arr = draw_info.lst
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap,n):
            temp = arr[i]
            j = i
            while  j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                draw_list(draw_info, {j: draw_info.green,
                                      j - gap: draw_info.red}, True)
                j -= gap
            arr[j] = temp
            draw_list(draw_info, {j: draw_info.green,
                                      gap: draw_info.red}, True)
        gap = gap // 2
    yield True
    return arr
