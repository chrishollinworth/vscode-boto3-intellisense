"""
Type annotations for license-manager-user-subscriptions service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/type_defs.html)

Usage::

    ```python
    from mypy_boto3_license_manager_user_subscriptions.type_defs import ActiveDirectoryIdentityProviderTypeDef

    data: ActiveDirectoryIdentityProviderTypeDef = {...}
    ```
"""

import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ActiveDirectoryIdentityProviderTypeDef",
    "AssociateUserRequestRequestTypeDef",
    "AssociateUserResponseTypeDef",
    "DeregisterIdentityProviderRequestRequestTypeDef",
    "DeregisterIdentityProviderResponseTypeDef",
    "DisassociateUserRequestRequestTypeDef",
    "DisassociateUserResponseTypeDef",
    "FilterTypeDef",
    "IdentityProviderSummaryTypeDef",
    "IdentityProviderTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceUserSummaryTypeDef",
    "ListIdentityProvidersRequestRequestTypeDef",
    "ListIdentityProvidersResponseTypeDef",
    "ListInstancesRequestRequestTypeDef",
    "ListInstancesResponseTypeDef",
    "ListProductSubscriptionsRequestRequestTypeDef",
    "ListProductSubscriptionsResponseTypeDef",
    "ListUserAssociationsRequestRequestTypeDef",
    "ListUserAssociationsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ProductUserSummaryTypeDef",
    "RegisterIdentityProviderRequestRequestTypeDef",
    "RegisterIdentityProviderResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SettingsTypeDef",
    "StartProductSubscriptionRequestRequestTypeDef",
    "StartProductSubscriptionResponseTypeDef",
    "StopProductSubscriptionRequestRequestTypeDef",
    "StopProductSubscriptionResponseTypeDef",
    "UpdateIdentityProviderSettingsRequestRequestTypeDef",
    "UpdateIdentityProviderSettingsResponseTypeDef",
    "UpdateSettingsTypeDef",
)

ActiveDirectoryIdentityProviderTypeDef = TypedDict(
    "ActiveDirectoryIdentityProviderTypeDef",
    {
        "DirectoryId": str,
    },
    total=False,
)

_RequiredAssociateUserRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateUserRequestRequestTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeDef",
        "InstanceId": str,
        "Username": str,
    },
)
_OptionalAssociateUserRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateUserRequestRequestTypeDef",
    {
        "Domain": str,
    },
    total=False,
)

class AssociateUserRequestRequestTypeDef(
    _RequiredAssociateUserRequestRequestTypeDef, _OptionalAssociateUserRequestRequestTypeDef
):
    pass

AssociateUserResponseTypeDef = TypedDict(
    "AssociateUserResponseTypeDef",
    {
        "InstanceUserSummary": "InstanceUserSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterIdentityProviderRequestRequestTypeDef = TypedDict(
    "DeregisterIdentityProviderRequestRequestTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeDef",
        "Product": str,
    },
)

DeregisterIdentityProviderResponseTypeDef = TypedDict(
    "DeregisterIdentityProviderResponseTypeDef",
    {
        "IdentityProviderSummary": "IdentityProviderSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateUserRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateUserRequestRequestTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeDef",
        "InstanceId": str,
        "Username": str,
    },
)
_OptionalDisassociateUserRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateUserRequestRequestTypeDef",
    {
        "Domain": str,
    },
    total=False,
)

class DisassociateUserRequestRequestTypeDef(
    _RequiredDisassociateUserRequestRequestTypeDef, _OptionalDisassociateUserRequestRequestTypeDef
):
    pass

DisassociateUserResponseTypeDef = TypedDict(
    "DisassociateUserResponseTypeDef",
    {
        "InstanceUserSummary": "InstanceUserSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Attribute": str,
        "Operation": str,
        "Value": str,
    },
    total=False,
)

_RequiredIdentityProviderSummaryTypeDef = TypedDict(
    "_RequiredIdentityProviderSummaryTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeDef",
        "Product": str,
        "Settings": "SettingsTypeDef",
        "Status": str,
    },
)
_OptionalIdentityProviderSummaryTypeDef = TypedDict(
    "_OptionalIdentityProviderSummaryTypeDef",
    {
        "FailureMessage": str,
    },
    total=False,
)

class IdentityProviderSummaryTypeDef(
    _RequiredIdentityProviderSummaryTypeDef, _OptionalIdentityProviderSummaryTypeDef
):
    pass

IdentityProviderTypeDef = TypedDict(
    "IdentityProviderTypeDef",
    {
        "ActiveDirectoryIdentityProvider": "ActiveDirectoryIdentityProviderTypeDef",
    },
    total=False,
)

_RequiredInstanceSummaryTypeDef = TypedDict(
    "_RequiredInstanceSummaryTypeDef",
    {
        "InstanceId": str,
        "Products": List[str],
        "Status": str,
    },
)
_OptionalInstanceSummaryTypeDef = TypedDict(
    "_OptionalInstanceSummaryTypeDef",
    {
        "LastStatusCheckDate": str,
        "StatusMessage": str,
    },
    total=False,
)

class InstanceSummaryTypeDef(_RequiredInstanceSummaryTypeDef, _OptionalInstanceSummaryTypeDef):
    pass

_RequiredInstanceUserSummaryTypeDef = TypedDict(
    "_RequiredInstanceUserSummaryTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeDef",
        "InstanceId": str,
        "Status": str,
        "Username": str,
    },
)
_OptionalInstanceUserSummaryTypeDef = TypedDict(
    "_OptionalInstanceUserSummaryTypeDef",
    {
        "AssociationDate": str,
        "DisassociationDate": str,
        "Domain": str,
        "StatusMessage": str,
    },
    total=False,
)

class InstanceUserSummaryTypeDef(
    _RequiredInstanceUserSummaryTypeDef, _OptionalInstanceUserSummaryTypeDef
):
    pass

ListIdentityProvidersRequestRequestTypeDef = TypedDict(
    "ListIdentityProvidersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListIdentityProvidersResponseTypeDef = TypedDict(
    "ListIdentityProvidersResponseTypeDef",
    {
        "IdentityProviderSummaries": List["IdentityProviderSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstancesRequestRequestTypeDef = TypedDict(
    "ListInstancesRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListInstancesResponseTypeDef = TypedDict(
    "ListInstancesResponseTypeDef",
    {
        "InstanceSummaries": List["InstanceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProductSubscriptionsRequestRequestTypeDef = TypedDict(
    "_RequiredListProductSubscriptionsRequestRequestTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeDef",
        "Product": str,
    },
)
_OptionalListProductSubscriptionsRequestRequestTypeDef = TypedDict(
    "_OptionalListProductSubscriptionsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListProductSubscriptionsRequestRequestTypeDef(
    _RequiredListProductSubscriptionsRequestRequestTypeDef,
    _OptionalListProductSubscriptionsRequestRequestTypeDef,
):
    pass

ListProductSubscriptionsResponseTypeDef = TypedDict(
    "ListProductSubscriptionsResponseTypeDef",
    {
        "NextToken": str,
        "ProductUserSummaries": List["ProductUserSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUserAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredListUserAssociationsRequestRequestTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeDef",
        "InstanceId": str,
    },
)
_OptionalListUserAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalListUserAssociationsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListUserAssociationsRequestRequestTypeDef(
    _RequiredListUserAssociationsRequestRequestTypeDef,
    _OptionalListUserAssociationsRequestRequestTypeDef,
):
    pass

ListUserAssociationsResponseTypeDef = TypedDict(
    "ListUserAssociationsResponseTypeDef",
    {
        "InstanceUserSummaries": List["InstanceUserSummaryTypeDef"],
        "NextToken": str,
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

_RequiredProductUserSummaryTypeDef = TypedDict(
    "_RequiredProductUserSummaryTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeDef",
        "Product": str,
        "Status": str,
        "Username": str,
    },
)
_OptionalProductUserSummaryTypeDef = TypedDict(
    "_OptionalProductUserSummaryTypeDef",
    {
        "Domain": str,
        "StatusMessage": str,
        "SubscriptionEndDate": str,
        "SubscriptionStartDate": str,
    },
    total=False,
)

class ProductUserSummaryTypeDef(
    _RequiredProductUserSummaryTypeDef, _OptionalProductUserSummaryTypeDef
):
    pass

_RequiredRegisterIdentityProviderRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterIdentityProviderRequestRequestTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeDef",
        "Product": str,
    },
)
_OptionalRegisterIdentityProviderRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterIdentityProviderRequestRequestTypeDef",
    {
        "Settings": "SettingsTypeDef",
    },
    total=False,
)

class RegisterIdentityProviderRequestRequestTypeDef(
    _RequiredRegisterIdentityProviderRequestRequestTypeDef,
    _OptionalRegisterIdentityProviderRequestRequestTypeDef,
):
    pass

RegisterIdentityProviderResponseTypeDef = TypedDict(
    "RegisterIdentityProviderResponseTypeDef",
    {
        "IdentityProviderSummary": "IdentityProviderSummaryTypeDef",
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

SettingsTypeDef = TypedDict(
    "SettingsTypeDef",
    {
        "SecurityGroupId": str,
        "Subnets": List[str],
    },
)

_RequiredStartProductSubscriptionRequestRequestTypeDef = TypedDict(
    "_RequiredStartProductSubscriptionRequestRequestTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeDef",
        "Product": str,
        "Username": str,
    },
)
_OptionalStartProductSubscriptionRequestRequestTypeDef = TypedDict(
    "_OptionalStartProductSubscriptionRequestRequestTypeDef",
    {
        "Domain": str,
    },
    total=False,
)

class StartProductSubscriptionRequestRequestTypeDef(
    _RequiredStartProductSubscriptionRequestRequestTypeDef,
    _OptionalStartProductSubscriptionRequestRequestTypeDef,
):
    pass

StartProductSubscriptionResponseTypeDef = TypedDict(
    "StartProductSubscriptionResponseTypeDef",
    {
        "ProductUserSummary": "ProductUserSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStopProductSubscriptionRequestRequestTypeDef = TypedDict(
    "_RequiredStopProductSubscriptionRequestRequestTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeDef",
        "Product": str,
        "Username": str,
    },
)
_OptionalStopProductSubscriptionRequestRequestTypeDef = TypedDict(
    "_OptionalStopProductSubscriptionRequestRequestTypeDef",
    {
        "Domain": str,
    },
    total=False,
)

class StopProductSubscriptionRequestRequestTypeDef(
    _RequiredStopProductSubscriptionRequestRequestTypeDef,
    _OptionalStopProductSubscriptionRequestRequestTypeDef,
):
    pass

StopProductSubscriptionResponseTypeDef = TypedDict(
    "StopProductSubscriptionResponseTypeDef",
    {
        "ProductUserSummary": "ProductUserSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateIdentityProviderSettingsRequestRequestTypeDef = TypedDict(
    "UpdateIdentityProviderSettingsRequestRequestTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeDef",
        "Product": str,
        "UpdateSettings": "UpdateSettingsTypeDef",
    },
)

UpdateIdentityProviderSettingsResponseTypeDef = TypedDict(
    "UpdateIdentityProviderSettingsResponseTypeDef",
    {
        "IdentityProviderSummary": "IdentityProviderSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSettingsTypeDef = TypedDict(
    "_RequiredUpdateSettingsTypeDef",
    {
        "AddSubnets": List[str],
        "RemoveSubnets": List[str],
    },
)
_OptionalUpdateSettingsTypeDef = TypedDict(
    "_OptionalUpdateSettingsTypeDef",
    {
        "SecurityGroupId": str,
    },
    total=False,
)

class UpdateSettingsTypeDef(_RequiredUpdateSettingsTypeDef, _OptionalUpdateSettingsTypeDef):
    pass
