from datetime import datetime
from pydantic import BaseModel
from videos.models import ReactionType


class VideoRead(BaseModel):
    video_id: int
    name: str
    username: str
    video_url: str
    preview_url: str
    count_reactions: int
    upload_at: datetime


class CommentRead(BaseModel):
    comment_id: int
    video_id: int
    username: str
    create_at: datetime
    text: str


class ReactionRead(BaseModel):
    user_id: int
    video_id: int
    reaction_type: ReactionType


