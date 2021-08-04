"""
Type annotations for mediastore-data service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore_data/literals.html)

Usage::

    ```python
    from mypy_boto3_mediastore_data.literals import ItemTypeType

    data: ItemTypeType = "FOLDER"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ItemTypeType", "ListItemsPaginatorName", "StorageClassType", "UploadAvailabilityType")

ItemTypeType = Literal["FOLDER", "OBJECT"]
ListItemsPaginatorName = Literal["list_items"]
StorageClassType = Literal["TEMPORAL"]
UploadAvailabilityType = Literal["STANDARD", "STREAMING"]
