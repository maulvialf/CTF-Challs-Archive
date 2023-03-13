from sqlalchemy.sql import text
from fastapi import HTTPException, status

def prepare_query(string: str, type: str):
    if type == 'get-audio':
        query = text(f"select name, namauser from audio where namauser='{string}';")
    elif type == 'get-played':
        query = text("select name, played from audio;")
    else:
        raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail="something happen!",
            )
    return query