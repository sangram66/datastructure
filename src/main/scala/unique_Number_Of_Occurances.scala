//
//
//1207. Unique Number of Occurrences
//Solved
//Easy
//
//Topics
//
//Companies
//
//Hint
//Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
//
//
//
//Example 1:
//
//  Input: arr = [1,2,2,1,1,3]
//Output: true
//Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
//Example 2:
//
//  Input: arr = [1,2]
//Output: false
//Example 3:
//
//  Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
//Output: true

import scala.collection.mutable
object Solution {
  def uniqueOccurrences(arr: Array[Int]): Boolean = {
    val countMap = mutable.Map[Int,Int]()
    for (num <- arr) {
      countMap(num) = countMap.getOrElse(num,0)+1
    }

    val occurances = countMap.values.toSet
    occurances.size == countMap.size

  }
  def main(args: Array[String]): Unit = {
    println(uniqueOccurrences(Array(1, 2, 2, 1, 1, 3)))  // Output: true
    println(uniqueOccurrences(Array(1, 2, 2, 1, 3, 3)))  // Output: false
    println(uniqueOccurrences(Array(1, 2, 3, 4, 5)))      // Output: true
  }


}