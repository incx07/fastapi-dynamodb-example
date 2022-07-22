import uvicorn
from fastapi import FastAPI

from app.internal.db import initialize_db

from app.domain.announcement import AnnouncementDomain
from app.repository.announcement import AnnouncementRepository
from app.routers.announcement import AnnouncementRouter


app = FastAPI()

db = initialize_db()
announcement_repository = AnnouncementRepository(db)
announcement_domain = AnnouncementDomain(announcement_repository)
announcement_router = AnnouncementRouter(announcement_domain)

app.include_router(announcement_router.router)


@app.get('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    uvicorn.run("app.main:app", host="0.0.0.0", port=5000, log_level="info", reload=True)
