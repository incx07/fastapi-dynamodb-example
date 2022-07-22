from fastapi import APIRouter
from fastapi import HTTPException

from app.domain.announcement import AnnouncementDomain, AnnouncementModel


class AnnouncementRouter:
    def __init__(self, announcement_domain: AnnouncementDomain) -> None:
        self.__announcement_domain = announcement_domain

    @property
    def router(self):
        api_router = APIRouter(prefix='/announcements', tags=['announcement'])
        
        @api_router.get('/')
        def index_route():
            return 'Hello! Welcome to announcement index route'
        
        @api_router.get('/all')
        def get_all():
            return self.__announcement_domain.get_all()
        
        @api_router.post('/create')
        def create_announcemen(announcemen_model: AnnouncementModel):
            return self.__announcement_domain.create_announcement(announcemen_model)

        @api_router.get('/get/{announcement_uid}')
        def get_announcement(announcement_uid: str):
            try:
                return self.__announcement_domain.get_announcement(announcement_uid)
            except KeyError:
                raise HTTPException(status_code=400, detail='No announcement found')

        @api_router.put('/update')
        def update_announcement(announcement_model: AnnouncementModel):
            return self.__announcement_domain.update_announcement(announcement_model)

        @api_router.delete('/delete/{announcement_uid}')
        def delete_announcement(announcement_uid: str):
            return self.__announcement_domain.delete_recipe(announcement_uid)

        return api_router
