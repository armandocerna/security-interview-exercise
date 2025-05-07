import os
import sys
import time

import psycopg

while True:
    targets = sys.argv[1]

    if targets is None:
        raise RuntimeError("targets should be provided as argument")

    names = sys.argv[2]

    if names is None:
        raise RuntimeError("names should be provided as argument")

    postgres_host = os.getenv("PG_HOST")

    if postgres_host is None:
        raise RuntimeError("postgres host should be provided")

    postgresUser = os.getenv("PG_USER")

    if postgresUser is None:
        raise RuntimeError("postgres user should be provided")

    postgresPassword = os.getenv("PG_PASS")

    if postgresPassword is None:
        raise RuntimeError("postgres password should be provided")

    namesList = names.split(',')

    validated_names = []
    for name in namesList:
        if len(name) < 50:
            if "-" not in name and "_" not in name:
                if not name.startswith("internal"):
                    validated_names.append(name)

    for name in validated_names:
        connection_string = f"postgresql://{postgresUser}:{postgresPassword}@{postgres_host}:5455/postgresDB"
        print(f"Connecting to {connection_string}")
        try:
            c = psycopg.connect(connection_string)
            cur = c.cursor()
            cur.execute(f"INSERT INTO name_targets VALUES ('{name}','{targets}')")
            c.commit()
        except:
            pass

    print("Completed loop")
