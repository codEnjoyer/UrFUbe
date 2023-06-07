from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey, MetaData, Table
from datetime import datetime
from sqlalchemy.orm import relationship
from database import Base


class Video(Base):
    __tablename__ = 'video'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)
    uploaded_at = Column(TIMESTAMP, default=datetime.utcnow)
    count_likes = Column(Integer, default=0)
    count_dislikes = Column(Integer, default=0)
    count_views = Column(Integer, default=0)
    video_url = Column(String, nullable=False)
    preview_url = Column(String)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("user", back_populates="videos")

