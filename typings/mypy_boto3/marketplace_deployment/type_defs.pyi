"""
Type annotations for marketplace-deployment service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_deployment/type_defs.html)

Usage::

    ```python
    from mypy_boto3_marketplace_deployment.type_defs import DeploymentParameterInputTypeDef

    data: DeploymentParameterInputTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Union

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "DeploymentParameterInputTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutDeploymentParameterRequestRequestTypeDef",
    "PutDeploymentParameterResponseTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
)

DeploymentParameterInputTypeDef = TypedDict(
    "DeploymentParameterInputTypeDef",
    {
        "name": str,
        "secretString": str,
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutDeploymentParameterRequestRequestTypeDef = TypedDict(
    "_RequiredPutDeploymentParameterRequestRequestTypeDef",
    {
        "agreementId": str,
        "catalog": str,
        "deploymentParameter": "DeploymentParameterInputTypeDef",
        "productId": str,
    },
)
_OptionalPutDeploymentParameterRequestRequestTypeDef = TypedDict(
    "_OptionalPutDeploymentParameterRequestRequestTypeDef",
    {
        "clientToken": str,
        "expirationDate": Union[datetime, str],
        "tags": Dict[str, str],
    },
    total=False,
)

class PutDeploymentParameterRequestRequestTypeDef(
    _RequiredPutDeploymentParameterRequestRequestTypeDef,
    _OptionalPutDeploymentParameterRequestRequestTypeDef,
):
    pass

PutDeploymentParameterResponseTypeDef = TypedDict(
    "PutDeploymentParameterResponseTypeDef",
    {
        "agreementId": str,
        "deploymentParameterId": str,
        "resourceArn": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredTagResourceRequestRequestTypeDef = TypedDict(
    "_RequiredTagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalTagResourceRequestRequestTypeDef = TypedDict(
    "_OptionalTagResourceRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class TagResourceRequestRequestTypeDef(
    _RequiredTagResourceRequestRequestTypeDef, _OptionalTagResourceRequestRequestTypeDef
):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)
