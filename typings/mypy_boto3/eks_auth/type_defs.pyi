"""
Type annotations for eks-auth service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks_auth/type_defs.html)

Usage::

    ```python
    from mypy_boto3_eks_auth.type_defs import AssumeRoleForPodIdentityRequestRequestTypeDef

    data: AssumeRoleForPodIdentityRequestRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AssumeRoleForPodIdentityRequestRequestTypeDef",
    "AssumeRoleForPodIdentityResponseTypeDef",
    "AssumedRoleUserTypeDef",
    "CredentialsTypeDef",
    "PodIdentityAssociationTypeDef",
    "ResponseMetadataTypeDef",
    "SubjectTypeDef",
)

AssumeRoleForPodIdentityRequestRequestTypeDef = TypedDict(
    "AssumeRoleForPodIdentityRequestRequestTypeDef",
    {
        "clusterName": str,
        "token": str,
    },
)

AssumeRoleForPodIdentityResponseTypeDef = TypedDict(
    "AssumeRoleForPodIdentityResponseTypeDef",
    {
        "subject": "SubjectTypeDef",
        "audience": str,
        "podIdentityAssociation": "PodIdentityAssociationTypeDef",
        "assumedRoleUser": "AssumedRoleUserTypeDef",
        "credentials": "CredentialsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssumedRoleUserTypeDef = TypedDict(
    "AssumedRoleUserTypeDef",
    {
        "arn": str,
        "assumeRoleId": str,
    },
)

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "sessionToken": str,
        "secretAccessKey": str,
        "accessKeyId": str,
        "expiration": datetime,
    },
)

PodIdentityAssociationTypeDef = TypedDict(
    "PodIdentityAssociationTypeDef",
    {
        "associationArn": str,
        "associationId": str,
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

SubjectTypeDef = TypedDict(
    "SubjectTypeDef",
    {
        "namespace": str,
        "serviceAccount": str,
    },
)
