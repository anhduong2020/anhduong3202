str = """This was a great help.
I applied this method to similiar problem
and rather than concat a SELECT statement
I created an event scheduled every couple
hours to rebuild a view that pivots n amount
of rows from one table into n columns on the other.
It is a big help because before I was rebuilding
the query using PHP on every execution of the SELECT.
Even though views can not leverage Indexes,
I am thinking filtering performance will not
be an issue as the pivoted rows->columns
represent types of training employees at a
franchise have so the view will not ever break
a few thousand rows."""

str = str.replace("\n", "")
arr = str.split(" ")
arr1 = []
table = {}

for i in arr:
    val = i[0]
    val = val.upper()
    arr1.append(val)
    arr1.sort()

for i in arr1:
    tmp = table.get(i)
    if tmp == None:
        table[i] = 1
    else:
        table[i] = table[i] + 1

print("히스토그램을 그립니다")
for item in table.items():
    print(item[0], "-" * item[1])
print()
