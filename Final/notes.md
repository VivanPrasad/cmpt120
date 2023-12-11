# CMPT120 Final Notes
*These are just some of the simple final notes I am putting together in preparation for tomorrow's final exam, worth 40%!*

### Exam Practices
* Complete Practice Exam **6**
* Complete Practice Exam **7**
* Complete Practice Exam **8**
---
# Big Topics

## Binary and Data Storage
* Binary to Number/ASCII/UNICODE conversion
##
* 
## Search and Sort Algorithms
* Linear (Sequential) Search vs Binary Search
  - Linear Search is time complexity n (best case C(1), worst case C(n))
  - Binary Search requires SORTED, but is much faster C(log2n) 
* Selection Sort vs Merge Sort
  - Selection Sort is slower, but more space efficient!
    * Set index n to lowest, keep comparing and setting. 
    * Then, set n+1 index and compare the ones after it (now comparing 1 less), and so on.
  - Merge sort = divide and conquer, selection sort = smallest to largest
    * Split the list until there is one element each. 
    * Then, *recursively* merge previous sorted lists.

## Complexity Analysis and Big-O Notation
* time complexity (processing) and space complexity (memory)
* which algorithm is faster/more efficient?
* Order of an algorithm = number of comparisons
* Know the Order from the reference categories
  * i.e. const, log, lin, log-lin, quad, cub, exponential
  * is O(c), O(log2 n), O(n), O(nlog2n), O(n²), O(n³), O(c^n), O(n!)
---
## General Programs to Know
* Know the recursive stars and reverse strings programs (PE6)

