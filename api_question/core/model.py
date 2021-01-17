"""
Models
"""
from typing import List, Dict

from pydantic import BaseModel

class CustomModel(BaseModel):
    j_fields: List[Dict[str, str]]