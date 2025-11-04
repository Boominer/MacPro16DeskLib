""""
Problem Name: Model Deployment Log Analyzer
Difficulty: Medium
Focus areas: log parsing, streaming analytics, percentile estimation, resource monitoring, ML Ops quality-gate logic
Background
When you roll out a new model version in production, you gate the rollout on three real-time service-level indicators (SLIs):
Metric	Pass Criterion
Success Rate	≥ 99 % of requests return SUCCESS
P95 Latency	≤ 200 ms
Peak Memory	≤ 4096 MB
 
Your task is to write a utility that consumes one continuous log stream covering several model versions and decides, for each version, whether it is safe to proceed or if it must be rolled back.
Input Format

An integer N (1 ≤ N ≤ 10<sup>5</sup>) – the number of log lines.
N subsequent lines, each with five space-separated fields:
luaCopyEdittimestamp  model_version  latency_ms  status  memory_mb
timestamp   Integer UNIX epoch milliseconds. Lines are already ordered by timestamp.
model_version  String without spaces (e.g. v3.2.1).
latency_ms   Integer 0 ≤ latency_ms ≤ 10 000.
status       Either SUCCESS or ERROR.
memory_mb     Integer 1 ≤ memory_mb ≤ 32 768.
A model version may appear in multiple contiguous blocks (e.g. canary, full deploy) but never interleaved with another version.
Output Format
For each distinct model_version in the order it first appears, print one line:
scssCopyEditmodel_version  verdict  success_rate(%)  p95_latency(ms)  peak_memory(MB)
verdict is DEPLOY if all three pass criteria are met, otherwise ROLLBACK.
Percentages and latencies are integers, rounded down.

14
1620000000010 v1.0 180 SUCCESS 3100
1620000000020 v1.0 190 SUCCESS 3200
1620000000030 v1.0 250 ERROR   3200
1620000000040 v1.0 170 SUCCESS 3300
1620000000050 v2.0 150 SUCCESS 3500
1620000000060 v2.0 210 SUCCESS 3600
1620000000070 v2.0 190 SUCCESS 3600
1620000000080 v2.0 205 ERROR   3700
1620000000090 v2.0 180 SUCCESS 3800
1620000000100 v2.0 195 SUCCESS 3850
1620000000110 v3.0 160 SUCCESS 2400
1620000000120 v3.0 170 SUCCESS 2500
1620000000130 v3.0 165 SUCCESS 2500
1620000000140 v3.0 180 SUCCESS 2600
 
Sample Output:
v1.0 ROLLBACK 75  250 3300
v2.0 ROLLBACK 80  210 3850
v3.0 DEPLOY   100 170 2600
 
Constraints & Expectations
Time limit: 2 s  Memory limit: 256 MB
Don’t load the entire log into memory if you can stream; but an N=10^5 array fits easily.
Any valid O(N log N) or O(N) percentile computation is acceptable. A textbook P² algorithm or bucket-counting works fine at this size.
Use only the standard library.
 

"""


class logSystem:


def parse_log_line(line):
    parts = line.strip().split()
    if len(parts) != 5:
        return None  # or raise an error
    return {
        "event_id": parts[0],
        "version": parts[1],
        "duration": int(parts[2]),
        "status": parts[3],
        "response_code": int(parts[4])
    }


# Example input (multi-line string)
log_data = """
1620000000010 v1.0 180 SUCCESS 3100
1620000000020 v1.0 190 SUCCESS 3200
1620000000030 v1.0 250 ERROR   3200
1620000000040 v1.0 170 SUCCESS 3300
1620000000050 v2.0 150 SUCCESS 3500
1620000000060 v2.0 210 SUCCESS 3600
1620000000070 v2.0 190 SUCCESS 3600
1620000000080 v2.0 205 ERROR   3700
1620000000090 v2.0 180 SUCCESS 3800
1620000000100 v2.0 195 SUCCESS 3850
1620000000110 v3.0 160 SUCCESS 2400
1620000000120 v3.0 170 SUCCESS 2500
1620000000130 v3.0 165 SUCCESS 2500
1620000000140 v3.0 180 SUCCESS 2600
"""

# Parse all lines
log_lines = log_data.strip().split('\n')
parsed_logs = [parse_log_line(line) for line in log_lines]
print(parsed_logs)




-- Shelf,  shelf information - fixture level, item level, position level  -- SQL Server
-- Sales, BQ, CA_WM_VM - SKU_DILY_SALE, Wkly --
