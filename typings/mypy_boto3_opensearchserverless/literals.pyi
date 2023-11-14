"""
Type annotations for opensearchserverless service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/literals.html)

Usage::

    ```python
    from mypy_boto3_opensearchserverless.literals import AccessPolicyTypeType

    data: AccessPolicyTypeType = "data"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccessPolicyTypeType",
    "CollectionStatusType",
    "CollectionTypeType",
    "LifecyclePolicyTypeType",
    "ResourceTypeType",
    "SecurityConfigTypeType",
    "SecurityPolicyTypeType",
    "VpcEndpointStatusType",
)

AccessPolicyTypeType = Literal["data"]
CollectionStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]
CollectionTypeType = Literal["SEARCH", "TIMESERIES", "VECTORSEARCH"]
LifecyclePolicyTypeType = Literal["retention"]
ResourceTypeType = Literal["index"]
SecurityConfigTypeType = Literal["saml"]
SecurityPolicyTypeType = Literal["encryption", "network"]
VpcEndpointStatusType = Literal["ACTIVE", "DELETING", "FAILED", "PENDING"]
