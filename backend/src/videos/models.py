from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from database import Base
from enum import IntEnum

# WARNING: Не удалять импорт User'а
from auth.models import User


class ReactionType(IntEnum):
    like = 0
    dislike = 1
    facepalm = 2


class VideoSortType(IntEnum):
    count_reactions = 1
    count_likes = 2
    count_dislikes = 3
    count_views = 4
    upload_at = 5


class Video(Base):
    __tablename__ = 'video'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=50), nullable=False)
    description = Column(String(length=150))
    uploaded_at = Column(TIMESTAMP, default=datetime.utcnow)
    count_reactions = Column(Integer, default=0)
    count_likes = Column(Integer, default=0)
    count_dislikes = Column(Integer, default=0)
    count_views = Column(Integer, default=0)
    video_url = Column(String, nullable=False)
    preview_url = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    user = relationship("User", back_populates="videos", lazy='subquery')
    reaction = relationship("Reaction", back_populates="video", cascade="all, delete-orphan")
    comment = relationship("Comment", back_populates='video', cascade="all, delete-orphan")

    def add_reaction(self, reaction_type: ReactionType, count_reaction: int):
        self.count_reactions += count_reaction
        if reaction_type == ReactionType.like:
            self.count_likes += count_reaction
        elif reaction_type == ReactionType.dislike:
            self.count_dislikes += count_reaction


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    video_id = Column(Integer, ForeignKey("video.id"), nullable=False)
    text = Column(String(length=150), nullable=False)
    create_at = Column(TIMESTAMP, default=datetime.utcnow)

    user = relationship("User", back_populates="comment")
    video = relationship("Video", back_populates="comment")


class Reaction(Base):
    __tablename__ = "reaction"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    video_id = Column(Integer, ForeignKey("video.id"), nullable=False)
    reaction_type_id = Column(Integer, nullable=False)

    user = relationship("User", back_populates="reaction")
    video = relationship("Video", back_populates="reaction")

