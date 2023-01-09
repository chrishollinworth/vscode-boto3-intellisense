"""
Type annotations for license-manager-linux-subscriptions service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/type_defs.html)

Usage::

    ```python
    from mypy_boto3_license_manager_linux_subscriptions.type_defs import FilterTypeDef

    data: FilterTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    LinuxSubscriptionsDiscoveryType,
    OperatorType,
    OrganizationIntegrationType,
    StatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "FilterTypeDef",
    "GetServiceSettingsResponseTypeDef",
    "InstanceTypeDef",
    "LinuxSubscriptionsDiscoverySettingsTypeDef",
    "ListLinuxSubscriptionInstancesRequestRequestTypeDef",
    "ListLinuxSubscriptionInstancesResponseTypeDef",
    "ListLinuxSubscriptionsRequestRequestTypeDef",
    "ListLinuxSubscriptionsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SubscriptionTypeDef",
    "UpdateServiceSettingsRequestRequestTypeDef",
    "UpdateServiceSettingsResponseTypeDef",
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Operator": OperatorType,
        "Values": List[str],
    },
    total=False,
)

GetServiceSettingsResponseTypeDef = TypedDict(
    "GetServiceSettingsResponseTypeDef",
    {
        "HomeRegions": List[str],
        "LinuxSubscriptionsDiscovery": LinuxSubscriptionsDiscoveryType,
        "LinuxSubscriptionsDiscoverySettings": "LinuxSubscriptionsDiscoverySettingsTypeDef",
        "Status": StatusType,
        "StatusMessage": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "AccountID": str,
        "AmiId": str,
        "InstanceID": str,
        "InstanceType": str,
        "LastUpdatedTime": str,
        "ProductCode": List[str],
        "Region": str,
        "Status": str,
        "SubscriptionName": str,
        "UsageOperation": str,
    },
    total=False,
)

LinuxSubscriptionsDiscoverySettingsTypeDef = TypedDict(
    "LinuxSubscriptionsDiscoverySettingsTypeDef",
    {
        "OrganizationIntegration": OrganizationIntegrationType,
        "SourceRegions": List[str],
    },
)

ListLinuxSubscriptionInstancesRequestRequestTypeDef = TypedDict(
    "ListLinuxSubscriptionInstancesRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListLinuxSubscriptionInstancesResponseTypeDef = TypedDict(
    "ListLinuxSubscriptionInstancesResponseTypeDef",
    {
        "Instances": List["InstanceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLinuxSubscriptionsRequestRequestTypeDef = TypedDict(
    "ListLinuxSubscriptionsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListLinuxSubscriptionsResponseTypeDef = TypedDict(
    "ListLinuxSubscriptionsResponseTypeDef",
    {
        "NextToken": str,
        "Subscriptions": List["SubscriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
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

SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "InstanceCount": int,
        "Name": str,
        "Type": str,
    },
    total=False,
)

_RequiredUpdateServiceSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateServiceSettingsRequestRequestTypeDef",
    {
        "LinuxSubscriptionsDiscovery": LinuxSubscriptionsDiscoveryType,
        "LinuxSubscriptionsDiscoverySettings": "LinuxSubscriptionsDiscoverySettingsTypeDef",
    },
)
_OptionalUpdateServiceSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateServiceSettingsRequestRequestTypeDef",
    {
        "AllowUpdate": bool,
    },
    total=False,
)

class UpdateServiceSettingsRequestRequestTypeDef(
    _RequiredUpdateServiceSettingsRequestRequestTypeDef,
    _OptionalUpdateServiceSettingsRequestRequestTypeDef,
):
    pass

UpdateServiceSettingsResponseTypeDef = TypedDict(
    "UpdateServiceSettingsResponseTypeDef",
    {
        "HomeRegions": List[str],
        "LinuxSubscriptionsDiscovery": LinuxSubscriptionsDiscoveryType,
        "LinuxSubscriptionsDiscoverySettings": "LinuxSubscriptionsDiscoverySettingsTypeDef",
        "Status": StatusType,
        "StatusMessage": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
