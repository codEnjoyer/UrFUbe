from datetime import datetime
from pydantic import BaseModel, HttpUrl
from videos.models import ReactionType


class VideoRead(BaseModel):
    video_id: int
    name: str
    description: str
    upload_at: datetime
    count_reactions: int
    count_likes: int
    count_dislikes: int
    count_views: int
    video_url: HttpUrl
    preview_url: HttpUrl
    reaction_type_id: int
    username: str
    user_id: int


class CommentRead(BaseModel):
    video_id: int
    user_id: int
    username: str
    create_at: datetime
    text: str


class ReactionRead(BaseModel):
    user_id: int
    video_id: int
    reaction_type: ReactionType


