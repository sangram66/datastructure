//
//nums = Array(1,2,3), k = 3
//
//Step	Num	Prefix Sum	Check (prefixSum - k)	Found Subarrays	HashMap Updates
//1	1	1	-2 (Not found)	0	{0 → 1, **1 → 1**}
//2	2	3	0 (Found!) ✅	1	{0 → 1, 1 → 1, **3 → 1**}
//3	3	6	3 (Found!) ✅	2	{0 → 1, 1 → 1, 3 → 1, **6 → 1**}
//
//
//Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
//
//A subarray is a contiguous non-empty sequence of elements within an array.
//
//
//
//  Example 1:
//
//  Input: nums = [1,1,1], k = 2
//Output: 2
//Example 2:
//
//  Input: nums = [1,2,3], k = 3
//Output: 2
//
//
//Constraints:
//
//  1 <= nums.length <= 2 * 104
//-1000 <= nums[i] <= 1000
//-107 <= k <= 107

//🔹 Explanation
//1️⃣ Optimized Approach (Prefix Sum + HashMap)
//
//Use a HashMap to store prefix sum frequencies.
//Key formula:
//  If
//(prefix_sum − k ) exists in HashMap, then a valid subarray exists
//If (prefix_sum−k) exists in HashMap, then a valid subarray exists
//Iterate through the array and keep track of prefix sums.
//Check if (prefixSum - k) exists in the HashMap.
//If found, increase the count by the number of times (prefixSum - k) appeared.
//Store/update prefixSum in the HashMap.

import scala.collection.mutable

object Solution1 {
  def subarraySum(nums: Array[Int], k: Int): Int = {
    var count = 0
    var prefixSum = 0
    val prefixCount = mutable.Map[Int, Int]().withDefaultValue(0)

    prefixCount(0) = 1 // Base case: prefix sum of 0 occurs once

    for (num <- nums) {
      prefixSum += num  // Update running sum

      // Check if (prefixSum - k) exists in the hashmap
      if (prefixCount.contains(prefixSum - k)) {
        count += prefixCount(prefixSum - k)
      }

      // Update prefix sum count in hashmap
      prefixCount(prefixSum) += 1
    }

    count
  }

  // Example Test Cases
  def main(args: Array[String]): Unit = {
    println(subarraySum(Array(1,1,1), 2))  // Output: 2
    println(subarraySum(Array(1,2,3), 3))  // Output: 2
  }
}