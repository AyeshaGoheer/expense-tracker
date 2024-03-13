-- SELECT * FROM expense_transaction ORDER BY date ASC;

WITH LedgerCTE AS (
  SELECT
    t.id,
    t.date,
    t.description,
    t.amount,
    t.transaction_type,
    c.name as category_name,
    u.username as user_username
  FROM
    expense_transaction t
  JOIN
    auth_user u ON t.user_id = u.id
  JOIN
    expense_category c ON t.category_id = c.id
  ORDER BY
    t.date
)
SELECT
  id,
  date,
  description,
  amount,
  transaction_type,
  category_name,
  user_username,
  SUM(CASE WHEN transaction_type = 'income' THEN amount ELSE -amount END)
      OVER (ORDER BY date, id) AS running_balance
FROM
  LedgerCTE
ORDER BY
  date, id;
