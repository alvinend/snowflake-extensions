import os

from snowflake.snowpark import Session, Table


def fetch(session: Session, table_name: str) -> Table:
    return session.table(table_name).select(["id"]).limit(10)

if __name__== "__main__":
    from snowflake.snowpark import Session

    session = Session.builder.configs({
        "account": os.getenv("SNOWFLAKE__ACCOUNT"),
        "user": os.getenv("SNOWFLAKE__USER"),
        "password": os.getenv("SNOWFLAKE__PASSWORD"),
        "role": os.getenv("SNOWFLAKE__ROLE"),
        "warehouse": os.getenv("SNOWFLAKE__WAREHOUSE"),
        "database": os.getenv("SNOWFLAKE__DATABASE"),
        "schema": os.getenv("SNOWFLAKE__SCHEMA"),
    }).create()

    table = fetch(
        session=session,
        table_name="TEST_TABLE",
    )

    print(table.collect())
