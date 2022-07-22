from uuid import uuid4
from pydantic import Field
from pydantic import BaseModel
from datetime import date as dtdate
from typing import Optional
from app.repository.announcement import AnnouncementRepository


class AnnouncementModel(BaseModel):
    uid: Optional[str] = None
    title: str = Field(..., example='Announcement Title')
    description: Optional[str] = Field(..., example='Detailed description of the event')
    date: Optional[dtdate] = Field(..., example='YYYY-MM-DD')


class AnnouncementDomain():
    def __init__(self, repository: AnnouncementRepository) -> None:
        self.__repository = repository

    def get_all(self):
        return self.__repository.get_all()

    def get_announcement(self, uid: str):
        return self.__repository.get_announcement(uid)

    def create_announcement(self, announcement: AnnouncementModel):
        announcement.uid = str(uuid4())
        return self.__repository.create_announcement(announcement.dict())

    def update_announcement(self, announcement: AnnouncementModel):
        return self.__repository.update_announcement(announcement.dict())

    def delete_announcement(self, uid: str):
        return self.__repository.delete_announcement(uid)
