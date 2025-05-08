"""
Type annotations for observabilityadmin service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_observabilityadmin/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_observabilityadmin.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

from .literals import ResourceTypeType, StatusType, TelemetryStateType, TelemetryTypeType

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
    "EmptyResponseMetadataTypeDef",
    "GetTelemetryEvaluationStatusForOrganizationOutputTypeDef",
    "GetTelemetryEvaluationStatusOutputTypeDef",
    "ListResourceTelemetryForOrganizationInputPaginateTypeDef",
    "ListResourceTelemetryForOrganizationInputTypeDef",
    "ListResourceTelemetryForOrganizationOutputTypeDef",
    "ListResourceTelemetryInputPaginateTypeDef",
    "ListResourceTelemetryInputTypeDef",
    "ListResourceTelemetryOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TelemetryConfigurationTypeDef",
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListResourceTelemetryForOrganizationInputTypeDef(TypedDict):
    AccountIdentifiers: NotRequired[Sequence[str]]
    ResourceIdentifierPrefix: NotRequired[str]
    ResourceTypes: NotRequired[Sequence[ResourceTypeType]]
    TelemetryConfigurationState: NotRequired[Mapping[TelemetryTypeType, TelemetryStateType]]
    ResourceTags: NotRequired[Mapping[str, str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class TelemetryConfigurationTypeDef(TypedDict):
    AccountIdentifier: NotRequired[str]
    TelemetryConfigurationState: NotRequired[Dict[TelemetryTypeType, TelemetryStateType]]
    ResourceType: NotRequired[ResourceTypeType]
    ResourceIdentifier: NotRequired[str]
    ResourceTags: NotRequired[Dict[str, str]]
    LastUpdateTimeStamp: NotRequired[int]

class ListResourceTelemetryInputTypeDef(TypedDict):
    ResourceIdentifierPrefix: NotRequired[str]
    ResourceTypes: NotRequired[Sequence[ResourceTypeType]]
    TelemetryConfigurationState: NotRequired[Mapping[TelemetryTypeType, TelemetryStateType]]
    ResourceTags: NotRequired[Mapping[str, str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetTelemetryEvaluationStatusForOrganizationOutputTypeDef(TypedDict):
    Status: StatusType
    FailureReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTelemetryEvaluationStatusOutputTypeDef(TypedDict):
    Status: StatusType
    FailureReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceTelemetryForOrganizationInputPaginateTypeDef(TypedDict):
    AccountIdentifiers: NotRequired[Sequence[str]]
    ResourceIdentifierPrefix: NotRequired[str]
    ResourceTypes: NotRequired[Sequence[ResourceTypeType]]
    TelemetryConfigurationState: NotRequired[Mapping[TelemetryTypeType, TelemetryStateType]]
    ResourceTags: NotRequired[Mapping[str, str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceTelemetryInputPaginateTypeDef(TypedDict):
    ResourceIdentifierPrefix: NotRequired[str]
    ResourceTypes: NotRequired[Sequence[ResourceTypeType]]
    TelemetryConfigurationState: NotRequired[Mapping[TelemetryTypeType, TelemetryStateType]]
    ResourceTags: NotRequired[Mapping[str, str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceTelemetryForOrganizationOutputTypeDef(TypedDict):
    TelemetryConfigurations: List[TelemetryConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListResourceTelemetryOutputTypeDef(TypedDict):
    TelemetryConfigurations: List[TelemetryConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
