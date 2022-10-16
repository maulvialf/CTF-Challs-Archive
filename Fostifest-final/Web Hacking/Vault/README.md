# Vault [500 pts]

**Category:** Web Hacking
**Solves:** 0

## Description
>b"I guess its just a normal vault, eh?"

## Service
http://103.13.207.16:10012

#### Hint
* ```py\nwith zipfile.ZipFile(temp_dir) as z:\n  for spec in z.infolist():\n    filename = spec.filename\n    basename = os.path.basename(filename)\n\n    if basename:\n      with db.engine.connect() as connection:\n        storage_id = str(uuid.uuid4())\n        user_id = session.get(\id\)\n        pathname = os.urandom(16).hex()\n\n        result = connection.execute(text(\n          f"""INSERT INTO user_storages (\n              id, filename, pathname, user_id\n            )\n            VALUES (\n              \{storage_id}\, \{basename}\,\n              \{pathname}\, \{user_id}\\n            )\n           """\n        ))\n```

## Solution

## Flag

