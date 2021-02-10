"""
Main interface for license-manager service type definitions.

Usage::

    ```python
    from mypy_boto3_license_manager.type_defs import AutomatedDiscoveryInformationTypeDef

    data: AutomatedDiscoveryInformationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AutomatedDiscoveryInformationTypeDef",
    "BorrowConfigurationTypeDef",
    "ConsumedLicenseSummaryTypeDef",
    "ConsumptionConfigurationTypeDef",
    "DatetimeRangeTypeDef",
    "EntitlementDataTypeDef",
    "EntitlementTypeDef",
    "EntitlementUsageTypeDef",
    "GrantTypeDef",
    "GrantedLicenseTypeDef",
    "IssuerDetailsTypeDef",
    "LicenseConfigurationAssociationTypeDef",
    "LicenseConfigurationTypeDef",
    "LicenseConfigurationUsageTypeDef",
    "LicenseOperationFailureTypeDef",
    "LicenseSpecificationTypeDef",
    "LicenseTypeDef",
    "LicenseUsageTypeDef",
    "ManagedResourceSummaryTypeDef",
    "MetadataTypeDef",
    "OrganizationConfigurationTypeDef",
    "ProductInformationFilterTypeDef",
    "ProductInformationTypeDef",
    "ProvisionalConfigurationTypeDef",
    "ReceivedMetadataTypeDef",
    "ResourceInventoryTypeDef",
    "TagTypeDef",
    "TokenDataTypeDef",
    "AcceptGrantResponseTypeDef",
    "CheckoutBorrowLicenseResponseTypeDef",
    "CheckoutLicenseResponseTypeDef",
    "CreateGrantResponseTypeDef",
    "CreateGrantVersionResponseTypeDef",
    "CreateLicenseConfigurationResponseTypeDef",
    "CreateLicenseResponseTypeDef",
    "CreateLicenseVersionResponseTypeDef",
    "CreateTokenResponseTypeDef",
    "DeleteGrantResponseTypeDef",
    "DeleteLicenseResponseTypeDef",
    "ExtendLicenseConsumptionResponseTypeDef",
    "FilterTypeDef",
    "GetAccessTokenResponseTypeDef",
    "GetGrantResponseTypeDef",
    "GetLicenseConfigurationResponseTypeDef",
    "GetLicenseResponseTypeDef",
    "GetLicenseUsageResponseTypeDef",
    "GetServiceSettingsResponseTypeDef",
    "InventoryFilterTypeDef",
    "IssuerTypeDef",
    "ListAssociationsForLicenseConfigurationResponseTypeDef",
    "ListDistributedGrantsResponseTypeDef",
    "ListFailuresForLicenseConfigurationOperationsResponseTypeDef",
    "ListLicenseConfigurationsResponseTypeDef",
    "ListLicenseSpecificationsForResourceResponseTypeDef",
    "ListLicenseVersionsResponseTypeDef",
    "ListLicensesResponseTypeDef",
    "ListReceivedGrantsResponseTypeDef",
    "ListReceivedLicensesResponseTypeDef",
    "ListResourceInventoryResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTokensResponseTypeDef",
    "ListUsageForLicenseConfigurationResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RejectGrantResponseTypeDef",
)

AutomatedDiscoveryInformationTypeDef = TypedDict(
    "AutomatedDiscoveryInformationTypeDef", {"LastRunTime": datetime}, total=False
)

BorrowConfigurationTypeDef = TypedDict(
    "BorrowConfigurationTypeDef", {"AllowEarlyCheckIn": bool, "MaxTimeToLiveInMinutes": int}
)

ConsumedLicenseSummaryTypeDef = TypedDict(
    "ConsumedLicenseSummaryTypeDef",
    {
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ConsumedLicenses": int,
    },
    total=False,
)

ConsumptionConfigurationTypeDef = TypedDict(
    "ConsumptionConfigurationTypeDef",
    {
        "RenewType": Literal["None", "Weekly", "Monthly"],
        "ProvisionalConfiguration": "ProvisionalConfigurationTypeDef",
        "BorrowConfiguration": "BorrowConfigurationTypeDef",
    },
    total=False,
)

_RequiredDatetimeRangeTypeDef = TypedDict("_RequiredDatetimeRangeTypeDef", {"Begin": str})
_OptionalDatetimeRangeTypeDef = TypedDict(
    "_OptionalDatetimeRangeTypeDef", {"End": str}, total=False
)


class DatetimeRangeTypeDef(_RequiredDatetimeRangeTypeDef, _OptionalDatetimeRangeTypeDef):
    pass


_RequiredEntitlementDataTypeDef = TypedDict(
    "_RequiredEntitlementDataTypeDef",
    {
        "Name": str,
        "Unit": Literal[
            "Count",
            "None",
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
        ],
    },
)
_OptionalEntitlementDataTypeDef = TypedDict(
    "_OptionalEntitlementDataTypeDef", {"Value": str}, total=False
)


class EntitlementDataTypeDef(_RequiredEntitlementDataTypeDef, _OptionalEntitlementDataTypeDef):
    pass


_RequiredEntitlementTypeDef = TypedDict(
    "_RequiredEntitlementTypeDef",
    {
        "Name": str,
        "Unit": Literal[
            "Count",
            "None",
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
        ],
    },
)
_OptionalEntitlementTypeDef = TypedDict(
    "_OptionalEntitlementTypeDef",
    {"Value": str, "MaxCount": int, "Overage": bool, "AllowCheckIn": bool},
    total=False,
)


class EntitlementTypeDef(_RequiredEntitlementTypeDef, _OptionalEntitlementTypeDef):
    pass


_RequiredEntitlementUsageTypeDef = TypedDict(
    "_RequiredEntitlementUsageTypeDef",
    {
        "Name": str,
        "ConsumedValue": str,
        "Unit": Literal[
            "Count",
            "None",
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
        ],
    },
)
_OptionalEntitlementUsageTypeDef = TypedDict(
    "_OptionalEntitlementUsageTypeDef", {"MaxCount": str}, total=False
)


class EntitlementUsageTypeDef(_RequiredEntitlementUsageTypeDef, _OptionalEntitlementUsageTypeDef):
    pass


_RequiredGrantTypeDef = TypedDict(
    "_RequiredGrantTypeDef",
    {
        "GrantArn": str,
        "GrantName": str,
        "ParentArn": str,
        "LicenseArn": str,
        "GranteePrincipalArn": str,
        "HomeRegion": str,
        "GrantStatus": Literal[
            "PENDING_WORKFLOW",
            "PENDING_ACCEPT",
            "REJECTED",
            "ACTIVE",
            "FAILED_WORKFLOW",
            "DELETED",
            "PENDING_DELETE",
            "DISABLED",
        ],
        "Version": str,
        "GrantedOperations": List[
            Literal[
                "CreateGrant",
                "CheckoutLicense",
                "CheckoutBorrowLicense",
                "CheckInLicense",
                "ExtendConsumptionLicense",
                "ListPurchasedLicenses",
                "CreateToken",
            ]
        ],
    },
)
_OptionalGrantTypeDef = TypedDict("_OptionalGrantTypeDef", {"StatusReason": str}, total=False)


class GrantTypeDef(_RequiredGrantTypeDef, _OptionalGrantTypeDef):
    pass


GrantedLicenseTypeDef = TypedDict(
    "GrantedLicenseTypeDef",
    {
        "LicenseArn": str,
        "LicenseName": str,
        "ProductName": str,
        "ProductSKU": str,
        "Issuer": "IssuerDetailsTypeDef",
        "HomeRegion": str,
        "Status": Literal[
            "AVAILABLE",
            "PENDING_AVAILABLE",
            "DEACTIVATED",
            "SUSPENDED",
            "EXPIRED",
            "PENDING_DELETE",
            "DELETED",
        ],
        "Validity": "DatetimeRangeTypeDef",
        "Beneficiary": str,
        "Entitlements": List["EntitlementTypeDef"],
        "ConsumptionConfiguration": "ConsumptionConfigurationTypeDef",
        "LicenseMetadata": List["MetadataTypeDef"],
        "CreateTime": str,
        "Version": str,
        "ReceivedMetadata": "ReceivedMetadataTypeDef",
    },
    total=False,
)

IssuerDetailsTypeDef = TypedDict(
    "IssuerDetailsTypeDef", {"Name": str, "SignKey": str, "KeyFingerprint": str}, total=False
)

LicenseConfigurationAssociationTypeDef = TypedDict(
    "LicenseConfigurationAssociationTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ResourceOwnerId": str,
        "AssociationTime": datetime,
        "AmiAssociationScope": str,
    },
    total=False,
)

LicenseConfigurationTypeDef = TypedDict(
    "LicenseConfigurationTypeDef",
    {
        "LicenseConfigurationId": str,
        "LicenseConfigurationArn": str,
        "Name": str,
        "Description": str,
        "LicenseCountingType": Literal["vCPU", "Instance", "Core", "Socket"],
        "LicenseRules": List[str],
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "DisassociateWhenNotFound": bool,
        "ConsumedLicenses": int,
        "Status": str,
        "OwnerAccountId": str,
        "ConsumedLicenseSummaryList": List["ConsumedLicenseSummaryTypeDef"],
        "ManagedResourceSummaryList": List["ManagedResourceSummaryTypeDef"],
        "ProductInformationList": List["ProductInformationTypeDef"],
        "AutomatedDiscoveryInformation": "AutomatedDiscoveryInformationTypeDef",
    },
    total=False,
)

LicenseConfigurationUsageTypeDef = TypedDict(
    "LicenseConfigurationUsageTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ResourceStatus": str,
        "ResourceOwnerId": str,
        "AssociationTime": datetime,
        "ConsumedLicenses": int,
    },
    total=False,
)

LicenseOperationFailureTypeDef = TypedDict(
    "LicenseOperationFailureTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ErrorMessage": str,
        "FailureTime": datetime,
        "OperationName": str,
        "ResourceOwnerId": str,
        "OperationRequestedBy": str,
        "MetadataList": List["MetadataTypeDef"],
    },
    total=False,
)

_RequiredLicenseSpecificationTypeDef = TypedDict(
    "_RequiredLicenseSpecificationTypeDef", {"LicenseConfigurationArn": str}
)
_OptionalLicenseSpecificationTypeDef = TypedDict(
    "_OptionalLicenseSpecificationTypeDef", {"AmiAssociationScope": str}, total=False
)


class LicenseSpecificationTypeDef(
    _RequiredLicenseSpecificationTypeDef, _OptionalLicenseSpecificationTypeDef
):
    pass


LicenseTypeDef = TypedDict(
    "LicenseTypeDef",
    {
        "LicenseArn": str,
        "LicenseName": str,
        "ProductName": str,
        "ProductSKU": str,
        "Issuer": "IssuerDetailsTypeDef",
        "HomeRegion": str,
        "Status": Literal[
            "AVAILABLE",
            "PENDING_AVAILABLE",
            "DEACTIVATED",
            "SUSPENDED",
            "EXPIRED",
            "PENDING_DELETE",
            "DELETED",
        ],
        "Validity": "DatetimeRangeTypeDef",
        "Beneficiary": str,
        "Entitlements": List["EntitlementTypeDef"],
        "ConsumptionConfiguration": "ConsumptionConfigurationTypeDef",
        "LicenseMetadata": List["MetadataTypeDef"],
        "CreateTime": str,
        "Version": str,
    },
    total=False,
)

LicenseUsageTypeDef = TypedDict(
    "LicenseUsageTypeDef", {"EntitlementUsages": List["EntitlementUsageTypeDef"]}, total=False
)

ManagedResourceSummaryTypeDef = TypedDict(
    "ManagedResourceSummaryTypeDef",
    {
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "AssociationCount": int,
    },
    total=False,
)

MetadataTypeDef = TypedDict("MetadataTypeDef", {"Name": str, "Value": str}, total=False)

OrganizationConfigurationTypeDef = TypedDict(
    "OrganizationConfigurationTypeDef", {"EnableIntegration": bool}
)

ProductInformationFilterTypeDef = TypedDict(
    "ProductInformationFilterTypeDef",
    {
        "ProductInformationFilterName": str,
        "ProductInformationFilterValue": List[str],
        "ProductInformationFilterComparator": str,
    },
)

ProductInformationTypeDef = TypedDict(
    "ProductInformationTypeDef",
    {"ResourceType": str, "ProductInformationFilterList": List["ProductInformationFilterTypeDef"]},
)

ProvisionalConfigurationTypeDef = TypedDict(
    "ProvisionalConfigurationTypeDef", {"MaxTimeToLiveInMinutes": int}
)

ReceivedMetadataTypeDef = TypedDict(
    "ReceivedMetadataTypeDef",
    {
        "ReceivedStatus": Literal[
            "PENDING_WORKFLOW",
            "PENDING_ACCEPT",
            "REJECTED",
            "ACTIVE",
            "FAILED_WORKFLOW",
            "DELETED",
            "DISABLED",
        ],
        "AllowedOperations": List[
            Literal[
                "CreateGrant",
                "CheckoutLicense",
                "CheckoutBorrowLicense",
                "CheckInLicense",
                "ExtendConsumptionLicense",
                "ListPurchasedLicenses",
                "CreateToken",
            ]
        ],
    },
    total=False,
)

ResourceInventoryTypeDef = TypedDict(
    "ResourceInventoryTypeDef",
    {
        "ResourceId": str,
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ResourceArn": str,
        "Platform": str,
        "PlatformVersion": str,
        "ResourceOwningAccountId": str,
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

TokenDataTypeDef = TypedDict(
    "TokenDataTypeDef",
    {
        "TokenId": str,
        "TokenType": str,
        "LicenseArn": str,
        "ExpirationTime": str,
        "TokenProperties": List[str],
        "RoleArns": List[str],
        "Status": str,
    },
    total=False,
)

AcceptGrantResponseTypeDef = TypedDict(
    "AcceptGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": Literal[
            "PENDING_WORKFLOW",
            "PENDING_ACCEPT",
            "REJECTED",
            "ACTIVE",
            "FAILED_WORKFLOW",
            "DELETED",
            "PENDING_DELETE",
            "DISABLED",
        ],
        "Version": str,
    },
    total=False,
)

CheckoutBorrowLicenseResponseTypeDef = TypedDict(
    "CheckoutBorrowLicenseResponseTypeDef",
    {
        "LicenseArn": str,
        "LicenseConsumptionToken": str,
        "EntitlementsAllowed": List["EntitlementDataTypeDef"],
        "NodeId": str,
        "SignedToken": str,
        "IssuedAt": str,
        "Expiration": str,
        "CheckoutMetadata": List["MetadataTypeDef"],
    },
    total=False,
)

CheckoutLicenseResponseTypeDef = TypedDict(
    "CheckoutLicenseResponseTypeDef",
    {
        "CheckoutType": Literal["PROVISIONAL"],
        "LicenseConsumptionToken": str,
        "EntitlementsAllowed": List["EntitlementDataTypeDef"],
        "SignedToken": str,
        "NodeId": str,
        "IssuedAt": str,
        "Expiration": str,
    },
    total=False,
)

CreateGrantResponseTypeDef = TypedDict(
    "CreateGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": Literal[
            "PENDING_WORKFLOW",
            "PENDING_ACCEPT",
            "REJECTED",
            "ACTIVE",
            "FAILED_WORKFLOW",
            "DELETED",
            "PENDING_DELETE",
            "DISABLED",
        ],
        "Version": str,
    },
    total=False,
)

CreateGrantVersionResponseTypeDef = TypedDict(
    "CreateGrantVersionResponseTypeDef",
    {
        "GrantArn": str,
        "Status": Literal[
            "PENDING_WORKFLOW",
            "PENDING_ACCEPT",
            "REJECTED",
            "ACTIVE",
            "FAILED_WORKFLOW",
            "DELETED",
            "PENDING_DELETE",
            "DISABLED",
        ],
        "Version": str,
    },
    total=False,
)

CreateLicenseConfigurationResponseTypeDef = TypedDict(
    "CreateLicenseConfigurationResponseTypeDef", {"LicenseConfigurationArn": str}, total=False
)

CreateLicenseResponseTypeDef = TypedDict(
    "CreateLicenseResponseTypeDef",
    {
        "LicenseArn": str,
        "Status": Literal[
            "AVAILABLE",
            "PENDING_AVAILABLE",
            "DEACTIVATED",
            "SUSPENDED",
            "EXPIRED",
            "PENDING_DELETE",
            "DELETED",
        ],
        "Version": str,
    },
    total=False,
)

CreateLicenseVersionResponseTypeDef = TypedDict(
    "CreateLicenseVersionResponseTypeDef",
    {
        "LicenseArn": str,
        "Version": str,
        "Status": Literal[
            "AVAILABLE",
            "PENDING_AVAILABLE",
            "DEACTIVATED",
            "SUSPENDED",
            "EXPIRED",
            "PENDING_DELETE",
            "DELETED",
        ],
    },
    total=False,
)

CreateTokenResponseTypeDef = TypedDict(
    "CreateTokenResponseTypeDef",
    {"TokenId": str, "TokenType": Literal["REFRESH_TOKEN"], "Token": str},
    total=False,
)

DeleteGrantResponseTypeDef = TypedDict(
    "DeleteGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": Literal[
            "PENDING_WORKFLOW",
            "PENDING_ACCEPT",
            "REJECTED",
            "ACTIVE",
            "FAILED_WORKFLOW",
            "DELETED",
            "PENDING_DELETE",
            "DISABLED",
        ],
        "Version": str,
    },
    total=False,
)

DeleteLicenseResponseTypeDef = TypedDict(
    "DeleteLicenseResponseTypeDef",
    {"Status": Literal["PENDING_DELETE", "DELETED"], "DeletionDate": str},
    total=False,
)

ExtendLicenseConsumptionResponseTypeDef = TypedDict(
    "ExtendLicenseConsumptionResponseTypeDef",
    {"LicenseConsumptionToken": str, "Expiration": str},
    total=False,
)

FilterTypeDef = TypedDict("FilterTypeDef", {"Name": str, "Values": List[str]}, total=False)

GetAccessTokenResponseTypeDef = TypedDict(
    "GetAccessTokenResponseTypeDef", {"AccessToken": str}, total=False
)

GetGrantResponseTypeDef = TypedDict(
    "GetGrantResponseTypeDef", {"Grant": "GrantTypeDef"}, total=False
)

GetLicenseConfigurationResponseTypeDef = TypedDict(
    "GetLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationId": str,
        "LicenseConfigurationArn": str,
        "Name": str,
        "Description": str,
        "LicenseCountingType": Literal["vCPU", "Instance", "Core", "Socket"],
        "LicenseRules": List[str],
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "ConsumedLicenses": int,
        "Status": str,
        "OwnerAccountId": str,
        "ConsumedLicenseSummaryList": List["ConsumedLicenseSummaryTypeDef"],
        "ManagedResourceSummaryList": List["ManagedResourceSummaryTypeDef"],
        "Tags": List["TagTypeDef"],
        "ProductInformationList": List["ProductInformationTypeDef"],
        "AutomatedDiscoveryInformation": "AutomatedDiscoveryInformationTypeDef",
        "DisassociateWhenNotFound": bool,
    },
    total=False,
)

GetLicenseResponseTypeDef = TypedDict(
    "GetLicenseResponseTypeDef", {"License": "LicenseTypeDef"}, total=False
)

GetLicenseUsageResponseTypeDef = TypedDict(
    "GetLicenseUsageResponseTypeDef", {"LicenseUsage": "LicenseUsageTypeDef"}, total=False
)

GetServiceSettingsResponseTypeDef = TypedDict(
    "GetServiceSettingsResponseTypeDef",
    {
        "S3BucketArn": str,
        "SnsTopicArn": str,
        "OrganizationConfiguration": "OrganizationConfigurationTypeDef",
        "EnableCrossAccountsDiscovery": bool,
        "LicenseManagerResourceShareArn": str,
    },
    total=False,
)

_RequiredInventoryFilterTypeDef = TypedDict(
    "_RequiredInventoryFilterTypeDef",
    {"Name": str, "Condition": Literal["EQUALS", "NOT_EQUALS", "BEGINS_WITH", "CONTAINS"]},
)
_OptionalInventoryFilterTypeDef = TypedDict(
    "_OptionalInventoryFilterTypeDef", {"Value": str}, total=False
)


class InventoryFilterTypeDef(_RequiredInventoryFilterTypeDef, _OptionalInventoryFilterTypeDef):
    pass


_RequiredIssuerTypeDef = TypedDict("_RequiredIssuerTypeDef", {"Name": str})
_OptionalIssuerTypeDef = TypedDict("_OptionalIssuerTypeDef", {"SignKey": str}, total=False)


class IssuerTypeDef(_RequiredIssuerTypeDef, _OptionalIssuerTypeDef):
    pass


ListAssociationsForLicenseConfigurationResponseTypeDef = TypedDict(
    "ListAssociationsForLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationAssociations": List["LicenseConfigurationAssociationTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListDistributedGrantsResponseTypeDef = TypedDict(
    "ListDistributedGrantsResponseTypeDef",
    {"Grants": List["GrantTypeDef"], "NextToken": str},
    total=False,
)

ListFailuresForLicenseConfigurationOperationsResponseTypeDef = TypedDict(
    "ListFailuresForLicenseConfigurationOperationsResponseTypeDef",
    {"LicenseOperationFailureList": List["LicenseOperationFailureTypeDef"], "NextToken": str},
    total=False,
)

ListLicenseConfigurationsResponseTypeDef = TypedDict(
    "ListLicenseConfigurationsResponseTypeDef",
    {"LicenseConfigurations": List["LicenseConfigurationTypeDef"], "NextToken": str},
    total=False,
)

ListLicenseSpecificationsForResourceResponseTypeDef = TypedDict(
    "ListLicenseSpecificationsForResourceResponseTypeDef",
    {"LicenseSpecifications": List["LicenseSpecificationTypeDef"], "NextToken": str},
    total=False,
)

ListLicenseVersionsResponseTypeDef = TypedDict(
    "ListLicenseVersionsResponseTypeDef",
    {"Licenses": List["LicenseTypeDef"], "NextToken": str},
    total=False,
)

ListLicensesResponseTypeDef = TypedDict(
    "ListLicensesResponseTypeDef",
    {"Licenses": List["LicenseTypeDef"], "NextToken": str},
    total=False,
)

ListReceivedGrantsResponseTypeDef = TypedDict(
    "ListReceivedGrantsResponseTypeDef",
    {"Grants": List["GrantTypeDef"], "NextToken": str},
    total=False,
)

ListReceivedLicensesResponseTypeDef = TypedDict(
    "ListReceivedLicensesResponseTypeDef",
    {"Licenses": List["GrantedLicenseTypeDef"], "NextToken": str},
    total=False,
)

ListResourceInventoryResponseTypeDef = TypedDict(
    "ListResourceInventoryResponseTypeDef",
    {"ResourceInventoryList": List["ResourceInventoryTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)

ListTokensResponseTypeDef = TypedDict(
    "ListTokensResponseTypeDef", {"Tokens": List["TokenDataTypeDef"], "NextToken": str}, total=False
)

ListUsageForLicenseConfigurationResponseTypeDef = TypedDict(
    "ListUsageForLicenseConfigurationResponseTypeDef",
    {"LicenseConfigurationUsageList": List["LicenseConfigurationUsageTypeDef"], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RejectGrantResponseTypeDef = TypedDict(
    "RejectGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": Literal[
            "PENDING_WORKFLOW",
            "PENDING_ACCEPT",
            "REJECTED",
            "ACTIVE",
            "FAILED_WORKFLOW",
            "DELETED",
            "PENDING_DELETE",
            "DISABLED",
        ],
        "Version": str,
    },
    total=False,
)
