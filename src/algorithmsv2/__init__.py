from .bubblesort import bubble_sort
from .insertionsort import insertion_sort
from .mergesort import merge_sort
from .quicksort import quick_sort, test_quick_sort
from .selectionsort import selection_sort, test_selection_sort
from .doubleselectionsort import double_selection_sort, test_double_selection_sort
from .heapsort import heap_sort

functions = {
    "bubble_sort": bubble_sort, 
"insertion_sort": insertion_sort, 
"merge_sort": merge_sort,
"quick_sort": quick_sort,
"selection_sort": selection_sort,
"double_selection_sort": double_selection_sort,
"heap_sort": heap_sort,
}