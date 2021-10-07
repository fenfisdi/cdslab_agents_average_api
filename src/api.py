from uuid import UUID

from fastapi import FastAPI
from starlette.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR

from src.use_case import ListBucketFile
from src.utils.messages import BucketMessages
from src.utils.response import UJSONResponse

app = FastAPI()


@app.post("/configuration/{conf_uuid}")
def process_bucket_information(
    conf_uuid: UUID
):
    try:
        result = ListBucketFile.handle(conf_uuid)

        return UJSONResponse(BucketMessages.valid, HTTP_200_OK)
    except Exception as error:
        return UJSONResponse(str(error), HTTP_500_INTERNAL_SERVER_ERROR)
