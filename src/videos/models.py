from sqlalchemy import MetaData, Column, Table, String, Integer, TIMESTAMP
from datetime import datetime

metadata = MetaData()

# TODO: перенести из ReadMe
video = Table(
    "video",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("uploaded_at", TIMESTAMP, default=datetime.utcnow),
    Column("count_likes", Integer, default=0),
    Column("url", String, nullable=False)
)
