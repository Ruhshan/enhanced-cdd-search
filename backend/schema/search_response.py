from typing import List

from pydantic import BaseModel

from backend.schema.cd_entry import CdEntry


class SearchResponse(BaseModel):
    count: int
    data: List[CdEntry]

