from dataclasses import dataclass


@dataclass
class BucketMessages:
    valid: str = 'Bucket information will process'
    empty: str = 'Bucket is empty'
