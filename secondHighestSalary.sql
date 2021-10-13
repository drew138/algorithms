-- problem: https://leetcode.com/problems/second-highest-salary/
-- Runtime: 211 ms, faster than 43.69% of MySQL online submissions for Second Highest Salary.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Second Highest Salary.

-- Write your MySQL query statement below
SELECT (
    SELECT DISTINCT salary FROM employee
    ORDER BY salary DESC LIMIT 1 OFFSET 1
) AS 'SecondHighestSalary';