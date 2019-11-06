-- -- SQLite




-- UPDATE DATA
-- SET Company_Name = REPLACE(Company_Name,'','');



SELECT company_name from DATA
where company_name like '%TECH'
ORDER BY company_name;
SELECT Company_Name from COMPANIES
where company_name like '%TECH'
ORDER BY company_name;
SELECT Company_Name from CONFIRMED_ID
where company_name like '%TECH'
ORDER BY company_name;



-- SELECT company_name FROM DATA
-- ORDER BY company_name;