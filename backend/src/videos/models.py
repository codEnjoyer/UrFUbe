from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from database import Base
from enum import IntEnum
from auth.models import User


class Video(Base):
    __tablename__ = 'video'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    uploaded_at = Column(TIMESTAMP, default=datetime.utcnow)
    count_reactions = Column(Integer, default=0)
    count_views = Column(Integer, default=0)
    video_url = Column(String, nullable=False)
    preview_url = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    user = relationship("User", back_populates="videos", lazy='subquery')
    reaction = relationship("Reaction", back_populates="video")


class Reaction(Base):
    __tablename__ = "reaction"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    video_id = Column(Integer, ForeignKey("video.id"), nullable=False)
    reaction_type_id = Column(Integer, nullable=False)
    user = relationship("User", back_populates="reaction")
    video = relationship("Video", back_populates="reaction")


class ReactionType(IntEnum):
    like = 0
    dislike = 1
    facepalm = 2
