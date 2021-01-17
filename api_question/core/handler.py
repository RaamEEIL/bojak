"""
Handles the execution of logic
"""
from typing import Dict

from api_question.core.model import CustomModel


class Handler(object):

    @classmethod
    def process_fields(cls, fields: CustomModel) -> Dict[str, str]:
        fields_dict=fields.j_fields
        response_dict: Dict[str, str] = {}
        for field in fields_dict:
            name: str = field['name']
            field.__delitem__('name')
            for field_member_key, field_member_value in field.items():
                if 'Val' in field_member_key:
                    value: str = field_member_value
                    break

            response_dict[name] = value

        return response_dict




