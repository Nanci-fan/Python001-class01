import pandas as pd 
# 1. SELECT * FROM data;
print(data)
# 2. SELECT * FROM data LIMIT(10);
print(data.loc[:10,:])
# 3. SELECT id FROM data;  //id 是 data 表的特定一列
print(data['C'])
# 4. SELECT COUNT(id) FROM data;
print(data['id'].count())
# 5. SELECT * FROM data WHERE id<1000 AND age>30;
print(data.loc[(data['id']<1000)&(data['age']>30),:])
# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
print(df2.groupby('id').aggregate({'order_id':'count'}))
# 7. SELECT * FROM table1 t1 INNER_JOIN table2 t2 ON t1.id = t2.id;
print(pd.merge(table1,table2,on='id',how='inner'))
# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
print(pd.concat([table1,table2]))
# 9. DELETE FROM table1 WHERE id=10;
table2 = table1.loc[table1['id']!=10,:]
print(table2)
# 10. ALTER TABLE table1 DROP COLUMN column_name;
table_columns = df2.columns
list_columns = list(table_columns)
list_columns2 = list_columns_two
print(table1[list_columns2])