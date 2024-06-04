"""
Type annotations for s3outposts service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/literals.html)

Usage::

    ```python
    from mypy_boto3_s3outposts.literals import EndpointAccessTypeType

    data: EndpointAccessTypeType = "CustomerOwnedIp"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "EndpointAccessTypeType",
    "EndpointStatusType",
    "ListEndpointsPaginatorName",
    "ListOutpostsWithS3PaginatorName",
    "ListSharedEndpointsPaginatorName",
)

EndpointAccessTypeType = Literal["CustomerOwnedIp", "Private"]
EndpointStatusType = Literal["Available", "Create_Failed", "Delete_Failed", "Deleting", "Pending"]
ListEndpointsPaginatorName = Literal["list_endpoints"]
ListOutpostsWithS3PaginatorName = Literal["list_outposts_with_s3"]
ListSharedEndpointsPaginatorName = Literal["list_shared_endpoints"]
