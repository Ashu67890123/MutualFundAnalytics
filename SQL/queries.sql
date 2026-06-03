SELECT * FROM fund_master;

SELECT COUNT(*) FROM fund_master;

SELECT category, COUNT(*)
FROM fund_master
GROUP BY category;

SELECT fund_house, COUNT(*)
FROM fund_master
GROUP BY fund_house;