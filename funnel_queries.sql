-- Overall Funnel Analysis
SELECT 
    stage,
    COUNT(*) as users_reached,
    COUNT(CASE WHEN success = 1 THEN 1 END) as successful,
    ROUND(100.0 * COUNT(CASE WHEN success = 1 THEN 1 END) / NULLIF(LAG(COUNT(*)) OVER (ORDER BY MIN(timestamp)), 0), 2) as conversion_pct
FROM events
GROUP BY stage
ORDER BY MIN(timestamp);

-- Drop-off by Device and School Type
SELECT 
    device,
    school_type,
    stage,
    COUNT(*) as count
FROM events e
JOIN students s ON e.student_id = s.student_id
GROUP BY device, school_type, stage;
