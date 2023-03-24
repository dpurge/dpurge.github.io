# Data manipulations

## CVS data

Example data in `data.csv`:

```csv
index, code, name
1, EX1, Example 1
2, EX2, Example 2
3, EX3, Example 3
```

Start new database:

```sh
sqlite3 data.db
```

Load data into table and delete headers in sqlite shell:

```sh
create table data (index, code, name);
.mode csv
.headers ON
.separator ,
.import data.csv data

delete from data where index = 'index';

select * from data limit 60;
```
