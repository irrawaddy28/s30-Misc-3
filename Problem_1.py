'''
1011  Capacity to ship packages in D days
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

Example 1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

Example 2:
Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4

Example 3:
Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1

Constraints:
1 <= days <= weights.length <= 5 * 10^4
1 <= weights[i] <= 500

Solution:
1. Binary Search
We use binary search between the heaviest item and the total weight.
For each middle capacity, we simulate how many days it would take.
If it fits within the allowed days, we try smaller; otherwise, we go larger.
https://youtu.be/R1MN07ZWZ9I?t=2920
Time: O(N * log(sum(weights) - max(weights))), Space: O(1)
'''
from typing import List

def shipWithinDays(weights: List[int], days: int) -> int:
    def count_days_to_ship(weights, capacity):
        num_days = 0
        sum = 0
        for w in weights:
            if sum + w <= capacity:
                sum += w
            else:
                sum = 0
                sum += w
                num_days += 1
        return num_days + 1

    N = len(weights)
    sum, M = 0, 0
    for i in range(N):
        sum += weights[i]
        M = max(M, weights[i])

    low = M
    high = sum
    while low <= high:
        mid = low + (high - low) // 2
        num_days = count_days_to_ship(weights, mid)
        # if num_days == days: # don't do this!
        #     return mid
        if num_days <= days:
            # we don't return mid even if num_days == days because
            # we are trying to find the lowest possible capacity
            # satisying the num_days == days criterion (ship in 'days' time)
            high = mid - 1
        else:
            low = mid + 1
    return low

def run_shipWithinDays():
    tests = [([1,2,3,4,5,6,7,8,9,10], 5, 15),
             ([3,2,2,4,1,4], 3, 6),
             ([1,2,3,1,1], 4, 3)
    ]
    for test in tests:
        weights, days, ans = test[0], test[1], test[2]
        print(f"\nweights = {weights}")
        print(f"days = {days}")
        least_capacity = shipWithinDays(weights, days)
        print(f"Least weight capacity of the ship = {least_capacity}")
        success = (ans == least_capacity)
        print(f"Pass: {success}")
        if not success:
            print("Failed")
            return

run_shipWithinDays()