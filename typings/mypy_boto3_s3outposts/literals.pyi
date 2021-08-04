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

__all__ = ("EndpointAccessTypeType", "EndpointStatusType", "ListEndpointsPaginatorName")

EndpointAccessTypeType = Literal["CustomerOwnedIp", "Private"]
EndpointStatusType = Literal["Available", "Deleting", "Pending"]
ListEndpointsPaginatorName = Literal["list_endpoints"]
