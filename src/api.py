from uuid import UUID

from fastapi import BackgroundTasks, FastAPI
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR

from src.use_case import ListBucketFile, ProcessInformation
from src.utils.messages import BucketMessages
from src.utils.response import UJSONResponse

app = FastAPI()


@app.post("/configuration/{conf_uuid}")
def process_bucket_information(
    conf_uuid: UUID,
    background_task: BackgroundTasks
):
    try:
        paths = ListBucketFile.handle(conf_uuid)
        if not paths:
            return UJSONResponse(BucketMessages.empty, HTTP_400_BAD_REQUEST)

        background_task.add_task(ProcessInformation.handle, paths)

        return UJSONResponse(BucketMessages.valid, HTTP_200_OK)
    except Exception as error:
        return UJSONResponse(str(error), HTTP_500_INTERNAL_SERVER_ERROR)
