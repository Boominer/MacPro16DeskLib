""""
The Theater Stage Scheduling Problem
You are managing private stages at a theater. Each group that comes in needs one private stage for the entire time of their show.

You are given a list of shows. Each show has a start time (when the group arrives) and an end time (when they leave). Your job is to figure out the minimum number of stages needed so that no two groups use the same stage at the same time.

A stage becomes free as soon as a group’s show ends.
Each group must have their own stage during their show.
Input:
A list of shows, like this:

[[10:00, 10:30], [10:05, 10:10], [10:15, 10:20]]
Output:
A single number — the minimum number of stages needed.

Example 1:
Input: [[10:00, 10:30], [10:05, 10:10], [10:15, 10:20]]
Output: 2
Explanation:

At 10:00, one show starts → 1 stage used.
At 10:05, another show starts → 2 stages used.
At 10:10, one show ends → 1 stage used.
At 10:15, another show starts → still 2 stages used.
The most stages used at the same time is 2.

Example 2 (Unsorted shows with exact end/start match):
Input: [[11:00, 11:30], [11:30, 12:00], [11:15, 11:45]]
Output: 2
Explanation:

At 11:00, one show starts → 1 stage used.
At 11:15, another show starts → 2 stages used.
At 11:30, the first show ends and a new one starts at the same time → still 2 stages used.
At 11:45, one show ends → 1 stage used.
At 12:00, the last show ends → 0 stages used.
The most stages used at the same time is 2.

Constraints:
The number of shows is between 1 and 10⁴.
Show times are given in 24-hour format as strings (e.g., "10:00").
Each show has a start time strictly less than its end time.
Shows may be unsorted.
No two shows have the exact same start and end time.
A show can start at the exact time another ends — this does not count as an overlap.
"""