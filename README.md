## Quickstart

```
poetry install

source .venv/bin/activate.bash
```

## Testing

```
poetry run python3 src/procedures/fetch/fetch.py
```

## Installing

(On Snowflake Console)
```
ALTER GIT REPOSITORY snowflake_extensions FETCH;

LS @snowflake_extensions/branches/main;

CREATE OR REPLACE PROCEDURE FETCH(
    table_name VARCHAR
)
  RETURNS TABLE
  LANGUAGE PYTHON
  RUNTIME_VERSION = '3.11'
  PACKAGES = ('snowflake-snowpark-python')
  IMPORTS = ('@snowflake_extensions/branches/main/src/procedures/fetch/fetch.py')
  HANDLER = 'fetch.fetch';

CALL FETCH('TEST_TABLE')
```
