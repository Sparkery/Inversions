Inversions
==========

Counts the number of inversions in an array.

This program calculates the number of inversions in an array in time bounded by O(n log n) by using a divide-and-conquer algorithm. By using a derivation of the merge sort algorithm, this program is able to count the number of inversions in similar time, as well as sort the array if needed.

A count of inversions is essentially how far away an array is from being sorted. Mathematically, it is the number of cases in array A and indices i and j where i < j and A[i] > A[j]. The merge sort algorithm can be put to great use in this case.

Bisecting the array, the number of inversions is the inversions in the left half, the inversions in the right half, and the inversions between the two, called split inversions.

Split inversions are found when the merge method finds the next element in the right subarray. The number of split inversions that element creates is exactly equal to the number of unread elemnents in the left subarray.
