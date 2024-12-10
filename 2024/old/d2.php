/* 
Input: List of reports (a report is a list of levels), a level is an integer
Output: Count of safe reports (a report is safe if all levels are either increasing/decreasing and 
        any two adjacent levels differ by at least one and at most three)
Example:
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
Output: 2 reports are safe (first and last report)
*/

<?php
function checkCondition(&$report) {
    $lastLevel = NULL;
    $lastDifference = NULL;
    $minDistance = 1;
    $maxDistance = 3;
    $index = 0;
    foreach ($report as $level) {
        if (empty($lastLevel)) {
            $lastLevel = $level;
            continue;
        }

        $difference = $lastLevel - $level;
        // Checks distance and whether it's ordered either ascending or descending (2nd condition checks if order changed compared to last)
        if (!($minDistance <= abs($difference) && abs($difference) <= $maxDistance) || !empty($lastDifference) && $difference * $lastDifference <= 0) {
            return $index;
        }

        $lastLevel = $level;
        $lastDifference = $difference;
        $index++;
    }
    return -1;
}

$data = file_get_contents('./data/day2.txt');

$lineSeparator = "\r\n";
$inlineSeperator = " ";
$lines = explode($lineSeparator, $data);
$reports = array();
$safeCount = 0;
foreach ($lines as $line) {
    $report = explode($inlineSeperator, $line);
    $newReport = array();
    foreach ($report as $level) {
        $newReport[] = (int) $level;
    }
    $reports[] = $newReport;
    
    if (checkCondition($newReport) === -1) {
        $safeCount++;
    }
}

echo sprintf("Number of safe report: %d\n", $safeCount);

// Part 2 <------------------------>
/* 
Same input and output, but now there can be one single bad level
-> If the report would be safe if this bad level didn't exist then, the report is now safe, too
*/

function recheckCondition(&$report, $index) {
    unset($report[$index]);
    $index =  checkCondition($report);
    return $index === -1 ? true : false;
}

$safeCount = 0;
foreach ($reports as $report) {
    $index = checkCondition($report);
    // report unsafe
    if ($index !== -1) {
        // create copy and try again without the left adjacent level
        $reportCopy = $report;
        if ($index - 1 >= 0 && recheckCondition($reportCopy, $index - 1) === true) {
            $safeCount++;
            continue;
        }
        // create copy and try again without the level itself where the condition check failed
        $reportCopy = $report;
        if (recheckCondition($reportCopy, $index) === true) {
            $safeCount++;
            continue;
        }
        // create copy and try again without the right adjacent level
        $reportCopy = $report;
        if ($index + 1 < count($report) && recheckCondition($reportCopy, $index + 1) === true) {
            $safeCount++;
            continue;
        }
    }
    else {
        $safeCount++;
    }
}

echo sprintf("Number of safe report: %d\n", $safeCount);
?>