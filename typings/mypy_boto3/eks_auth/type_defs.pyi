"""
Type annotations for eks-auth service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks_auth/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_eks_auth.type_defs import AssumeRoleForPodIdentityRequestTypeDef

    data: AssumeRoleForPodIdentityRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
else:
    from typing import Dict
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AssumeRoleForPodIdentityRequestTypeDef",
    "AssumeRoleForPodIdentityResponseTypeDef",
    "AssumedRoleUserTypeDef",
    "CredentialsTypeDef",
    "PodIdentityAssociationTypeDef",
    "ResponseMetadataTypeDef",
    "SubjectTypeDef",
)

class AssumeRoleForPodIdentityRequestTypeDef(TypedDict):
    clusterName: str
    token: str

class AssumedRoleUserTypeDef(TypedDict):
    arn: str
    assumeRoleId: str

class CredentialsTypeDef(TypedDict):
    sessionToken: str
    secretAccessKey: str
    accessKeyId: str
    expiration: datetime

class PodIdentityAssociationTypeDef(TypedDict):
    associationArn: str
    associationId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class SubjectTypeDef(TypedDict):
    namespace: str
    serviceAccount: str

class AssumeRoleForPodIdentityResponseTypeDef(TypedDict):
    subject: SubjectTypeDef
    audience: str
    podIdentityAssociation: PodIdentityAssociationTypeDef
    assumedRoleUser: AssumedRoleUserTypeDef
    credentials: CredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
