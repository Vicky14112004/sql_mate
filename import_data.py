import os
import pandas as pd
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

# --------------------------------------------------
# MySQL connection
# --------------------------------------------------

conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "localhost"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database="IPL_ANALYTICS"
)

cursor = conn.cursor()

print("✅ Connected to IPL_ANALYTICS")


# --------------------------------------------------
# CSV → MySQL helper
# --------------------------------------------------

def import_csv(csv_file, table_name):

    print(f"\n📂 Loading {csv_file}...")

    df = pd.read_csv(csv_file)

    print(f"Rows found: {len(df)}")

    # Convert missing values to Python None
    # This makes them become SQL NULL in MySQL
    df = df.astype(object).where(pd.notnull(df), None)

    # Convert booleans to integers
    for column in df.columns:
        if df[column].dtype == "bool":
            df[column] = df[column].astype(int)

    # Drop table if it already exists
    cursor.execute(f"DROP TABLE IF EXISTS `{table_name}`")

    # Create table dynamically
    columns = []

    for column in df.columns:

        dtype = str(df[column].dtype)

        if "int" in dtype:
            sql_type = "INT"

        elif "float" in dtype:
            sql_type = "DOUBLE"

        elif "bool" in dtype:
            sql_type = "BOOLEAN"

        else:
            sql_type = "TEXT"

        columns.append(f"`{column}` {sql_type}")

    create_sql = f"""
    CREATE TABLE `{table_name}` (
        {', '.join(columns)}
    )
    """

    cursor.execute(create_sql)

    print(f"✅ Table `{table_name}` created")

    # Insert data
    column_names = ", ".join(
        f"`{column}`" for column in df.columns
    )

    placeholders = ", ".join(
        ["%s"] * len(df.columns)
    )

    insert_sql = f"""
    INSERT INTO `{table_name}`
    ({column_names})
    VALUES ({placeholders})
    """

    # Convert DataFrame to tuples
    data = [
        tuple(row)
        for row in df.itertuples(index=False, name=None)
    ]

    # Insert in batches
    batch_size = 5000

    for i in range(0, len(data), batch_size):

        batch = data[i:i + batch_size]

        cursor.executemany(insert_sql, batch)

        conn.commit()

        print(
            f"   Inserted {min(i + batch_size, len(data))}"
            f"/{len(data)}"
        )

    print(f"🎉 Finished importing `{table_name}`")


# --------------------------------------------------
# Import IPL datasets
# --------------------------------------------------

import_csv(
    "ball_by_ball_data.csv",
    "BALL_BY_BALL"
)

import_csv(
    "ipl_matches_data.csv",
    "IPL_MATCHES"
)

import_csv(
    "players-data-updated.csv",
    "PLAYERS"
)

import_csv(
    "teams_data.csv",
    "TEAMS"
)

import_csv(
    "team_aliases.csv",
    "TEAM_ALIASES"
)


# --------------------------------------------------
# Close connection
# --------------------------------------------------

cursor.close()
conn.close()

print("\n===================================")
print("🎉 ALL IPL DATA IMPORTED SUCCESSFULLY")
print("===================================")
