-- Program 037: select null safe equality
-- MySQL 8. Execute in a clean practice schema.
SELECT NULL <=> NULL AS both_null, 1 <=> NULL AS one_null;
