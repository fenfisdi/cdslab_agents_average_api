import re
from os import environ
from typing import List
from uuid import UUID

from google.cloud import storage


class ListBucketFile:
    bucket_name = environ.get("GCP_BUCKET_NAME")
    storage_client = storage.Client()

    @classmethod
    def handle(cls, conf_uuid: UUID) -> List:
        path_list = cls.__list_path_files(conf_uuid)
        return cls.__filter_list(path_list)

    @classmethod
    def __list_path_files(cls, conf_uuid: UUID) -> List[str]:
        blob_name = f'{"/".join([str(conf_uuid), "out"])}/'
        blobs = cls.storage_client.list_blobs(cls.bucket_name, prefix=blob_name)
        return [str(blob.name) for blob in blobs]

    @classmethod
    def __filter_list(cls, path_list: List) -> List[str]:
        regex = re.compile(".*csv")
        return list(filter(regex.match, path_list))
