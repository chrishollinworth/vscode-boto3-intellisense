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
    "ConsumedLicenseSummaryTypeDef",
    "LicenseConfigurationAssociationTypeDef",
    "LicenseConfigurationTypeDef",
    "LicenseConfigurationUsageTypeDef",
    "LicenseOperationFailureTypeDef",
    "LicenseSpecificationTypeDef",
    "ManagedResourceSummaryTypeDef",
    "MetadataTypeDef",
    "OrganizationConfigurationTypeDef",
    "ProductInformationFilterTypeDef",
    "ProductInformationTypeDef",
    "ResourceInventoryTypeDef",
    "TagTypeDef",
    "CreateLicenseConfigurationResponseTypeDef",
    "FilterTypeDef",
    "GetLicenseConfigurationResponseTypeDef",
    "GetServiceSettingsResponseTypeDef",
    "InventoryFilterTypeDef",
    "ListAssociationsForLicenseConfigurationResponseTypeDef",
    "ListFailuresForLicenseConfigurationOperationsResponseTypeDef",
    "ListLicenseConfigurationsResponseTypeDef",
    "ListLicenseSpecificationsForResourceResponseTypeDef",
    "ListResourceInventoryResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUsageForLicenseConfigurationResponseTypeDef",
    "PaginatorConfigTypeDef",
)

AutomatedDiscoveryInformationTypeDef = TypedDict(
    "AutomatedDiscoveryInformationTypeDef", {"LastRunTime": datetime}, total=False
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

LicenseConfigurationAssociationTypeDef = TypedDict(
    "LicenseConfigurationAssociationTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": Literal[
            "EC2_INSTANCE", "EC2_HOST", "EC2_AMI", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
        ],
        "ResourceOwnerId": str,
        "AssociationTime": datetime,
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

LicenseSpecificationTypeDef = TypedDict(
    "LicenseSpecificationTypeDef", {"LicenseConfigurationArn": str}
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

CreateLicenseConfigurationResponseTypeDef = TypedDict(
    "CreateLicenseConfigurationResponseTypeDef", {"LicenseConfigurationArn": str}, total=False
)

FilterTypeDef = TypedDict("FilterTypeDef", {"Name": str, "Values": List[str]}, total=False)

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
    },
    total=False,
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


ListAssociationsForLicenseConfigurationResponseTypeDef = TypedDict(
    "ListAssociationsForLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationAssociations": List["LicenseConfigurationAssociationTypeDef"],
        "NextToken": str,
    },
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

ListResourceInventoryResponseTypeDef = TypedDict(
    "ListResourceInventoryResponseTypeDef",
    {"ResourceInventoryList": List["ResourceInventoryTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)

ListUsageForLicenseConfigurationResponseTypeDef = TypedDict(
    "ListUsageForLicenseConfigurationResponseTypeDef",
    {"LicenseConfigurationUsageList": List["LicenseConfigurationUsageTypeDef"], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
