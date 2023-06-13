from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from database import Base
from enum import IntEnum


class Video(Base):
    __tablename__ = 'video'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=50), nullable=False)
    uploaded_at = Column(TIMESTAMP, default=datetime.utcnow)
    count_reactions = Column(Integer, default=0)
    count_views = Column(Integer, default=0)
    video_url = Column(String, nullable=False)
    preview_url = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    user = relationship("User", back_populates="videos", lazy='subquery')
    reaction = relationship("Reaction", back_populates="video")
    comment = relationship("Comment", back_populates='video')


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


class ReactionType(IntEnum):
    like = 0
    dislike = 1
    facepalm = 2
