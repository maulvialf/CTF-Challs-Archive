from sqlalchemy.sql import text
from fastapi import HTTPException, status

def prepare_query(string: str, type: str):
    if type == 'get-photo':
        query = text(f"select name, image_path, description from gallery where lower(name) like lower('%{string}%');")
    elif type == 'super_admin':
        query = text(f"{string}")
    else:
        raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail="something happen!",
            )
    return query