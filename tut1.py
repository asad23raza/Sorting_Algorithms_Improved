import pygame
import random
import math

from pygame.constants import TIMER_RESOLUTION
pygame.init()

# The GameVariables Class holds important information about the display. This includes
# the colors used, the background color, fonts, list elements etc.
class GameVariables:
    black = 0,0,0
    white = 255,255,255
    green = 0, 255, 0
    red = 255, 0, 0
    grey = 128,128,128
    background_color = white
    side_padding = 100
    top_padding = 150
    gradients = [grey, (160,160,160), (192,192,192)]
    font = pygame.font.SysFont('Georgia',24)
    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)
    def set_list(self, lst):
        self.lst = lst
        self.max_val = max(lst)
        self.min_val = min(lst)
        # the block width is measured by subtracting the padding from the side width
        # and dividing it by the number of bars
        self.block_width = round((self.width - self.side_padding) / len(lst))
        # this is the height of one block
        self.block_height = math.floor((self.height - self.top_padding) / (self.max_val - self.min_val))
        self.start_x = self.side_padding // 2

# List_generate produces a randomized list with n elements, with a range of min_val to max_val
def list_generate(n, min_val, max_val):
    lst = []
    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
    return lst

# Draw_list draws the current list in draw_info, with the colors given in the color positions dict. 
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
# Draw takes a GameVariables class as an input. (Note method background_colour is called)
def draw(draw_info, algo_name='Sorting Algorithms Visualized'):
    # the GameVariables object has a method for window (line 16)
    draw_info.window.fill(draw_info.background_color)
    title = draw_info.font.render(f"{algo_name}",2, (0,0,255))
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 5))

    controls = draw_info.font.render("R - Reset | SPACE - Start Sorting | I - Insertion Sort | M - Merge Sort ",1, draw_info.black)
    sortingAlgos = draw_info.font.render("B - Bubble Sort | Q - Quicksort | S - Shell Sort | K - Bucket Sort ",1, draw_info.black)
    draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, title.get_height() + 5))
    draw_info.window.blit(sortingAlgos, (draw_info.width / 2 - sortingAlgos.get_width() / 2, title.get_height() + 
    controls.get_height() + 6))
    draw_list(draw_info)
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

def main():
    run = True
    clock = pygame.time.Clock()
    # create variables for the list to change later
    n = 50
    min_val = 0
    max_val = 100
    lst = list_generate(n,min_val,max_val)
    initialize_board = GameVariables(800,800,lst)
    sorting = False
    sorting_algo = bubble_sort # this is the function
    title = 'Sorting Algorithms Visualized'
    sorting_gen = None
    while run:
        clock.tick(60) # 60 frames per second
        if sorting:
            try:
                next(sorting_gen)
            except StopIteration:
                sorting = False
        else:
            draw(initialize_board, title)
        #draw(initialize_board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                lst1 = list_generate(n,min_val,max_val)
                initialize_board.set_list(lst1)
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_gen = sorting_algo(initialize_board)
            elif event.key == pygame.K_b:
                sorting = True
                sorting_algo = bubble_sort
                title = 'Completed: Bubble Sort O(n)^2'
                sorting_gen = sorting_algo(initialize_board)
            elif event.key == pygame.K_i:
                sorting = True
                sorting_algo = insertion_sort
                title = 'Completed: Insertion sort O(n)^2'
                sorting_gen = sorting_algo(initialize_board)
            elif event.key == pygame.K_q:
                sorting = True
                sorting_algo = quicksort
                title = 'Completed: Quick sort O(n log n)'
                sorting_gen = sorting_algo(initialize_board)
            elif event.key == pygame.K_m:
                sorting = True
                sorting_algo = mergesort
                title = 'Completed: Merge Sort O(log n)'
                sorting_gen = sorting_algo(initialize_board)
            elif event.key == pygame.K_s:
                sorting = True
                sorting_algo = shellsort
                title = 'Completed: Shell Sort O(n^2)'
                sorting_gen = sorting_algo(initialize_board)
            
    pygame.quit()
if __name__ == '__main__':
    main()



 