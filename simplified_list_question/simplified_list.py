"""
Simplified List question
"""
from typing import List


class SimplifiedList(list):
    """
    Simplified List Description
    """

    def __init__(self, cls_type = None):
        """
        Init a list with support of non conventional types
        :param cls_type: Type of element to support in list
        """
        self.cls_type = cls_type

    def __setitem__(self, key, value):
        """
        Overrides parent behavior.
        If trying to add an item to a index which doesnt exist yet and it is the next index - allow to add it by
        appending it.
        :param key:
        :param value:
        :return:
        """
        try:
            if self.cls_type:
                temp_obj = self.cls_type(value)
                super(SimplifiedList, self).__setitem__(key, temp_obj)
            else:
                super(SimplifiedList, self).__setitem__(key, value)

        except Exception as e:
            len: int = super(SimplifiedList, self).__len__()
            if key == len:
                if self.cls_type:
                    super(SimplifiedList, self).append(self.cls_type(value))
                else:
                    super(SimplifiedList, self).append(value)
            else:
                raise IndexError('list index out of range')
