"""
Type annotations for iotfleethub service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleethub/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_iotfleethub.type_defs import ApplicationSummaryTypeDef

    data: ApplicationSummaryTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

from .literals import ApplicationStateType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ApplicationSummaryTypeDef",
    "CreateApplicationRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "DeleteApplicationRequestTypeDef",
    "DescribeApplicationRequestTypeDef",
    "DescribeApplicationResponseTypeDef",
    "ListApplicationsRequestPaginateTypeDef",
    "ListApplicationsRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateApplicationRequestTypeDef",
)

class ApplicationSummaryTypeDef(TypedDict):
    applicationId: str
    applicationName: str
    applicationUrl: str
    applicationDescription: NotRequired[str]
    applicationCreationDate: NotRequired[int]
    applicationLastUpdateDate: NotRequired[int]
    applicationState: NotRequired[ApplicationStateType]

class CreateApplicationRequestTypeDef(TypedDict):
    applicationName: str
    roleArn: str
    applicationDescription: NotRequired[str]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteApplicationRequestTypeDef(TypedDict):
    applicationId: str
    clientToken: NotRequired[str]

class DescribeApplicationRequestTypeDef(TypedDict):
    applicationId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListApplicationsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateApplicationRequestTypeDef(TypedDict):
    applicationId: str
    applicationName: NotRequired[str]
    applicationDescription: NotRequired[str]
    clientToken: NotRequired[str]

class CreateApplicationResponseTypeDef(TypedDict):
    applicationId: str
    applicationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicationResponseTypeDef(TypedDict):
    applicationId: str
    applicationArn: str
    applicationName: str
    applicationDescription: str
    applicationUrl: str
    applicationState: ApplicationStateType
    applicationCreationDate: int
    applicationLastUpdateDate: int
    roleArn: str
    ssoClientId: str
    errorMessage: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsResponseTypeDef(TypedDict):
    applicationSummaries: List[ApplicationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]
