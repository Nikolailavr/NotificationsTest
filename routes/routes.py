from typing import Annotated

from bson import ObjectId
from fastapi import APIRouter, Request, Body, BackgroundTasks, Query
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from database.models import Notification, NotificationKey
from env.env import EMAIL_TO
from misc.email import send_email
from schemas.notifications import notes_list

router = APIRouter()


ObjectIdAnnotated = Annotated[str, Query(length=24)]


@router.get('/list')
async def get_list(request: Request,
                   user_id: ObjectIdAnnotated,
                   skip: int = None,
                   limit: int = None):

    notes = notes_list(request.app.database[user_id].find())
    if skip is None:
        skip = 0
    if limit is None:
        limit = len(notes)
    new_mess = 0
    for note in notes:
        new_mess += 1 if note['is_new'] else 0
    return JSONResponse(
        status_code=200,
        content={
            "success": True,
            "data": {
                "elements": len(notes),
                "new": new_mess,
                "request": {
                    "user_id": user_id,
                    "skip": skip,
                    "limit": limit,
                },
                "list": notes[skip:skip + limit]
            }
        }
    )


@router.post('/create', status_code=201)
async def post_create(request: Request,
                      background_tasks: BackgroundTasks,
                      note: Annotated[Notification, Body()]):
    if note.key != NotificationKey.registration:
        request.app.database[note.user_id].insert_one(jsonable_encoder(note))
    if note.key == NotificationKey.registration or \
            note.key == NotificationKey.new_login:
        send_email(
            background_tasks=background_tasks,
            subject=note.key.value,
            email_to=EMAIL_TO,
            body={'key': note.key.value}
        )
    return JSONResponse(status_code=201, content={'success': True})


@router.post('/read')
async def post_read(request: Request,
                    user_id: ObjectIdAnnotated,
                    id: ObjectIdAnnotated):
    request.app.database[user_id].find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": {'is_new': False}}
    )
    return JSONResponse(status_code=200, content={'success': True})
