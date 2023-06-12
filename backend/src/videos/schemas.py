from datetime import datetime

from auth.schemas import UserRead
from pydantic import HttpUrl


class Video:
    id: int
    name: str
    uploaded_at: datetime
    count_likes: int
    count_dislikes: int
    count_views: int
    video_url: HttpUrl
    preview_url: str
    user: UserRead
