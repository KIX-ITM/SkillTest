from decimal import Decimal

from pydantic import BaseModel


class AiAnalysisLogSchema(BaseModel):
    image_path: str
    success: str
    message: str
    img_class: int | None = None
    confidence: Decimal | None = None
    request_timestamp: int
    response_timestamp: int

