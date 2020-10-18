# How to Run it?
Must have matplotlib installed
download the code.
cd into sortginVisualizer directory
pip install -r requirements.txt
For rectangle visualization
python3 "src/rectvisualizer.py"
For color wheel visualizer
python3 "src/circlevisualizerv.py"
The program has 3 command line arguments, -f -n -i (--function --number --interval)
-f tells sorting function, -n tells size of the array, -i tells how to sort (1000 is 1 second)
EXAMPLE:
python3 src/circvisualizer -f merge_sort -n 200 -i 1000
In the example, e are asking for a Circle visualization over merge sorting sorting an an array of 200 and at a speed of 1000 milliseconds (1 second).


# Python Sorting Algorithm Visualizer

This visualizes sorting algorithms using either a color wheel or rectangles.
# Min Max Selection Sort (Double Selection Sort)
Double Selection Sort grabs the minimum and maximum for each iteration of the array.
The array that we are iterating through will decrease by two for each iteration.
(This is because we found the correct spot for the current biggest and current smallest element and have placed them in the right position.)
# Selection Sort
Selection sort grabs the smallest element for each iteration of the array. And then place it at the bottom of the array.
The array that we are iterating through will decrease by one for each iteration.
(This is because we found the correct spot for the smallest element and there is no need to loop through that element again)
# Bubble Sort
Bubble Sort will loop through the array andswitch elements if the element to the right is smaller than the element on the left. The amount of elements we have to loop through will decrease by one because the current smallest element will be at the furthest left it can be, so there is no point in comparing it again.
# Quick Sort
Divide And Conquer algorithm
Will have a pivot value
All elements smaller than the pivot will be on its left and elements greater will be on its right
Repeats this process until the array is sorted
# Merge Sort
Divide and Conquer Algorithm
Will divide the array into two evenly cut arrays,
    Divide those two arrays into evenly cut arrays again,
    repeat until the size of a cut array is 1 or 0
Iterate through the evenly cut arrays and whichever element is smaller, add it back to the new array.
    AKA. Merge the two arrays together but in a sorted manner
# Insertion Sort
Will grab and element and then iterate backwards (leftward) and then insert the element in its correct position.
# Heap Sort
Creates a max heap (A binary tree with a parent that is smaller than its children)
    Places the root node at the back of the tree (or array) because it is the largest
    Turn the array back into a max heap
    repeat step number two
Equation to get a parent's children in an array is 
left = parent_index * 2 + 1 and right = parent_index * 2 + 2

