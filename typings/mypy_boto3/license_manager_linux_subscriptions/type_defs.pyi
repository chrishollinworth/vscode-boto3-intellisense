"""
Type annotations for license-manager-linux-subscriptions service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_license_manager_linux_subscriptions.type_defs import DeregisterSubscriptionProviderRequestTypeDef

    data: DeregisterSubscriptionProviderRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import Union

from .literals import (
    LinuxSubscriptionsDiscoveryType,
    OperatorType,
    OrganizationIntegrationType,
    StatusType,
    SubscriptionProviderStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "DeregisterSubscriptionProviderRequestTypeDef",
    "FilterTypeDef",
    "GetRegisteredSubscriptionProviderRequestTypeDef",
    "GetRegisteredSubscriptionProviderResponseTypeDef",
    "GetServiceSettingsResponseTypeDef",
    "InstanceTypeDef",
    "LinuxSubscriptionsDiscoverySettingsOutputTypeDef",
    "LinuxSubscriptionsDiscoverySettingsTypeDef",
    "LinuxSubscriptionsDiscoverySettingsUnionTypeDef",
    "ListLinuxSubscriptionInstancesRequestPaginateTypeDef",
    "ListLinuxSubscriptionInstancesRequestTypeDef",
    "ListLinuxSubscriptionInstancesResponseTypeDef",
    "ListLinuxSubscriptionsRequestPaginateTypeDef",
    "ListLinuxSubscriptionsRequestTypeDef",
    "ListLinuxSubscriptionsResponseTypeDef",
    "ListRegisteredSubscriptionProvidersRequestPaginateTypeDef",
    "ListRegisteredSubscriptionProvidersRequestTypeDef",
    "ListRegisteredSubscriptionProvidersResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterSubscriptionProviderRequestTypeDef",
    "RegisterSubscriptionProviderResponseTypeDef",
    "RegisteredSubscriptionProviderTypeDef",
    "ResponseMetadataTypeDef",
    "SubscriptionTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateServiceSettingsRequestTypeDef",
    "UpdateServiceSettingsResponseTypeDef",
)

class DeregisterSubscriptionProviderRequestTypeDef(TypedDict):
    SubscriptionProviderArn: str

class FilterTypeDef(TypedDict):
    Name: NotRequired[str]
    Operator: NotRequired[OperatorType]
    Values: NotRequired[Sequence[str]]

class GetRegisteredSubscriptionProviderRequestTypeDef(TypedDict):
    SubscriptionProviderArn: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class LinuxSubscriptionsDiscoverySettingsOutputTypeDef(TypedDict):
    OrganizationIntegration: OrganizationIntegrationType
    SourceRegions: List[str]

class InstanceTypeDef(TypedDict):
    AccountID: NotRequired[str]
    AmiId: NotRequired[str]
    DualSubscription: NotRequired[str]
    InstanceID: NotRequired[str]
    InstanceType: NotRequired[str]
    LastUpdatedTime: NotRequired[str]
    OsVersion: NotRequired[str]
    ProductCode: NotRequired[List[str]]
    Region: NotRequired[str]
    RegisteredWithSubscriptionProvider: NotRequired[str]
    Status: NotRequired[str]
    SubscriptionName: NotRequired[str]
    SubscriptionProviderCreateTime: NotRequired[str]
    SubscriptionProviderUpdateTime: NotRequired[str]
    UsageOperation: NotRequired[str]

class LinuxSubscriptionsDiscoverySettingsTypeDef(TypedDict):
    OrganizationIntegration: OrganizationIntegrationType
    SourceRegions: Sequence[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "InstanceCount": NotRequired[int],
        "Name": NotRequired[str],
        "Type": NotRequired[str],
    },
)

class ListRegisteredSubscriptionProvidersRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    SubscriptionProviderSources: NotRequired[Sequence[Literal["RedHat"]]]

class RegisteredSubscriptionProviderTypeDef(TypedDict):
    LastSuccessfulDataRetrievalTime: NotRequired[str]
    SecretArn: NotRequired[str]
    SubscriptionProviderArn: NotRequired[str]
    SubscriptionProviderSource: NotRequired[Literal["RedHat"]]
    SubscriptionProviderStatus: NotRequired[SubscriptionProviderStatusType]
    SubscriptionProviderStatusMessage: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class RegisterSubscriptionProviderRequestTypeDef(TypedDict):
    SecretArn: str
    SubscriptionProviderSource: Literal["RedHat"]
    Tags: NotRequired[Mapping[str, str]]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class ListLinuxSubscriptionInstancesRequestTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListLinuxSubscriptionsRequestTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GetRegisteredSubscriptionProviderResponseTypeDef(TypedDict):
    LastSuccessfulDataRetrievalTime: str
    SecretArn: str
    SubscriptionProviderArn: str
    SubscriptionProviderSource: Literal["RedHat"]
    SubscriptionProviderStatus: SubscriptionProviderStatusType
    SubscriptionProviderStatusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterSubscriptionProviderResponseTypeDef(TypedDict):
    SubscriptionProviderArn: str
    SubscriptionProviderSource: Literal["RedHat"]
    SubscriptionProviderStatus: SubscriptionProviderStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceSettingsResponseTypeDef(TypedDict):
    HomeRegions: List[str]
    LinuxSubscriptionsDiscovery: LinuxSubscriptionsDiscoveryType
    LinuxSubscriptionsDiscoverySettings: LinuxSubscriptionsDiscoverySettingsOutputTypeDef
    Status: StatusType
    StatusMessage: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceSettingsResponseTypeDef(TypedDict):
    HomeRegions: List[str]
    LinuxSubscriptionsDiscovery: LinuxSubscriptionsDiscoveryType
    LinuxSubscriptionsDiscoverySettings: LinuxSubscriptionsDiscoverySettingsOutputTypeDef
    Status: StatusType
    StatusMessage: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListLinuxSubscriptionInstancesResponseTypeDef(TypedDict):
    Instances: List[InstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

LinuxSubscriptionsDiscoverySettingsUnionTypeDef = Union[
    LinuxSubscriptionsDiscoverySettingsTypeDef, LinuxSubscriptionsDiscoverySettingsOutputTypeDef
]

class ListLinuxSubscriptionInstancesRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLinuxSubscriptionsRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRegisteredSubscriptionProvidersRequestPaginateTypeDef(TypedDict):
    SubscriptionProviderSources: NotRequired[Sequence[Literal["RedHat"]]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLinuxSubscriptionsResponseTypeDef(TypedDict):
    Subscriptions: List[SubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListRegisteredSubscriptionProvidersResponseTypeDef(TypedDict):
    RegisteredSubscriptionProviders: List[RegisteredSubscriptionProviderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateServiceSettingsRequestTypeDef(TypedDict):
    LinuxSubscriptionsDiscovery: LinuxSubscriptionsDiscoveryType
    LinuxSubscriptionsDiscoverySettings: LinuxSubscriptionsDiscoverySettingsUnionTypeDef
    AllowUpdate: NotRequired[bool]
