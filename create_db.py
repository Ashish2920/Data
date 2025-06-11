import sqlite3
import pandas as pd

# Step 1: Load your CSV into a pandas DataFrame
csv_file = 'titanic.csv'    # Replace with your file path
df = pd.read_csv(csv_file)

# Step 2: Connect to SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('titanic.db')    # Replace with your database name
cursor = conn.cursor()

# Step 3: Create a table (optional, if you don't want to overwrite an existing table)
# If the table exists, you can skip this step or use a DROP TABLE statement to clear it.
cursor.execute('''
CREATE TABLE titanic (
    "Survived" BIGINT,
    "Pclass" BIGINT,
    "Name" TEXT,
    "Sex" TEXT,
    "Age" FLOAT,
    "Siblings/Spouses Aboard" BIGINT,
    "Parents/Children Aboard" BIGINT,
    "Fare" FLOAT
)
''')

# Step 4: Insert Data from the DataFrame into the SQLite Table
df.to_sql('titanic', conn, if_exists='replace', index=False)

# Step 5: Commit the transaction and close the connection
conn.commit()

#3. Query Data
cursor.execute('SELECT * FROM titanic')
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()

print("CSV data has been successfully stored in SQLite database.")