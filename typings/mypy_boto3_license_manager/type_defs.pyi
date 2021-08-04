"""
Type annotations for license-manager service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/type_defs.html)

Usage::

    ```python
    from mypy_boto3_license_manager.type_defs import AcceptGrantRequestRequestTypeDef

    data: AcceptGrantRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AllowedOperationType,
    EntitlementDataUnitType,
    EntitlementUnitType,
    GrantStatusType,
    InventoryFilterConditionType,
    LicenseConfigurationStatusType,
    LicenseCountingTypeType,
    LicenseDeletionStatusType,
    LicenseStatusType,
    ReceivedStatusType,
    RenewTypeType,
    ReportFrequencyTypeType,
    ReportTypeType,
    ResourceTypeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AcceptGrantRequestRequestTypeDef",
    "AcceptGrantResponseTypeDef",
    "AutomatedDiscoveryInformationTypeDef",
    "BorrowConfigurationTypeDef",
    "CheckInLicenseRequestRequestTypeDef",
    "CheckoutBorrowLicenseRequestRequestTypeDef",
    "CheckoutBorrowLicenseResponseTypeDef",
    "CheckoutLicenseRequestRequestTypeDef",
    "CheckoutLicenseResponseTypeDef",
    "ConsumedLicenseSummaryTypeDef",
    "ConsumptionConfigurationTypeDef",
    "CreateGrantRequestRequestTypeDef",
    "CreateGrantResponseTypeDef",
    "CreateGrantVersionRequestRequestTypeDef",
    "CreateGrantVersionResponseTypeDef",
    "CreateLicenseConfigurationRequestRequestTypeDef",
    "CreateLicenseConfigurationResponseTypeDef",
    "CreateLicenseManagerReportGeneratorRequestRequestTypeDef",
    "CreateLicenseManagerReportGeneratorResponseTypeDef",
    "CreateLicenseRequestRequestTypeDef",
    "CreateLicenseResponseTypeDef",
    "CreateLicenseVersionRequestRequestTypeDef",
    "CreateLicenseVersionResponseTypeDef",
    "CreateTokenRequestRequestTypeDef",
    "CreateTokenResponseTypeDef",
    "DatetimeRangeTypeDef",
    "DeleteGrantRequestRequestTypeDef",
    "DeleteGrantResponseTypeDef",
    "DeleteLicenseConfigurationRequestRequestTypeDef",
    "DeleteLicenseManagerReportGeneratorRequestRequestTypeDef",
    "DeleteLicenseRequestRequestTypeDef",
    "DeleteLicenseResponseTypeDef",
    "DeleteTokenRequestRequestTypeDef",
    "EntitlementDataTypeDef",
    "EntitlementTypeDef",
    "EntitlementUsageTypeDef",
    "ExtendLicenseConsumptionRequestRequestTypeDef",
    "ExtendLicenseConsumptionResponseTypeDef",
    "FilterTypeDef",
    "GetAccessTokenRequestRequestTypeDef",
    "GetAccessTokenResponseTypeDef",
    "GetGrantRequestRequestTypeDef",
    "GetGrantResponseTypeDef",
    "GetLicenseConfigurationRequestRequestTypeDef",
    "GetLicenseConfigurationResponseTypeDef",
    "GetLicenseManagerReportGeneratorRequestRequestTypeDef",
    "GetLicenseManagerReportGeneratorResponseTypeDef",
    "GetLicenseRequestRequestTypeDef",
    "GetLicenseResponseTypeDef",
    "GetLicenseUsageRequestRequestTypeDef",
    "GetLicenseUsageResponseTypeDef",
    "GetServiceSettingsResponseTypeDef",
    "GrantTypeDef",
    "GrantedLicenseTypeDef",
    "InventoryFilterTypeDef",
    "IssuerDetailsTypeDef",
    "IssuerTypeDef",
    "LicenseConfigurationAssociationTypeDef",
    "LicenseConfigurationTypeDef",
    "LicenseConfigurationUsageTypeDef",
    "LicenseOperationFailureTypeDef",
    "LicenseSpecificationTypeDef",
    "LicenseTypeDef",
    "LicenseUsageTypeDef",
    "ListAssociationsForLicenseConfigurationRequestRequestTypeDef",
    "ListAssociationsForLicenseConfigurationResponseTypeDef",
    "ListDistributedGrantsRequestRequestTypeDef",
    "ListDistributedGrantsResponseTypeDef",
    "ListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef",
    "ListFailuresForLicenseConfigurationOperationsResponseTypeDef",
    "ListLicenseConfigurationsRequestRequestTypeDef",
    "ListLicenseConfigurationsResponseTypeDef",
    "ListLicenseManagerReportGeneratorsRequestRequestTypeDef",
    "ListLicenseManagerReportGeneratorsResponseTypeDef",
    "ListLicenseSpecificationsForResourceRequestRequestTypeDef",
    "ListLicenseSpecificationsForResourceResponseTypeDef",
    "ListLicenseVersionsRequestRequestTypeDef",
    "ListLicenseVersionsResponseTypeDef",
    "ListLicensesRequestRequestTypeDef",
    "ListLicensesResponseTypeDef",
    "ListReceivedGrantsRequestRequestTypeDef",
    "ListReceivedGrantsResponseTypeDef",
    "ListReceivedLicensesRequestRequestTypeDef",
    "ListReceivedLicensesResponseTypeDef",
    "ListResourceInventoryRequestRequestTypeDef",
    "ListResourceInventoryResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTokensRequestRequestTypeDef",
    "ListTokensResponseTypeDef",
    "ListUsageForLicenseConfigurationRequestRequestTypeDef",
    "ListUsageForLicenseConfigurationResponseTypeDef",
    "ManagedResourceSummaryTypeDef",
    "MetadataTypeDef",
    "OrganizationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ProductInformationFilterTypeDef",
    "ProductInformationTypeDef",
    "ProvisionalConfigurationTypeDef",
    "ReceivedMetadataTypeDef",
    "RejectGrantRequestRequestTypeDef",
    "RejectGrantResponseTypeDef",
    "ReportContextTypeDef",
    "ReportFrequencyTypeDef",
    "ReportGeneratorTypeDef",
    "ResourceInventoryTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TokenDataTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateLicenseConfigurationRequestRequestTypeDef",
    "UpdateLicenseManagerReportGeneratorRequestRequestTypeDef",
    "UpdateLicenseSpecificationsForResourceRequestRequestTypeDef",
    "UpdateServiceSettingsRequestRequestTypeDef",
)

AcceptGrantRequestRequestTypeDef = TypedDict(
    "AcceptGrantRequestRequestTypeDef",
    {
        "GrantArn": str,
    },
)

AcceptGrantResponseTypeDef = TypedDict(
    "AcceptGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AutomatedDiscoveryInformationTypeDef = TypedDict(
    "AutomatedDiscoveryInformationTypeDef",
    {
        "LastRunTime": datetime,
    },
    total=False,
)

BorrowConfigurationTypeDef = TypedDict(
    "BorrowConfigurationTypeDef",
    {
        "AllowEarlyCheckIn": bool,
        "MaxTimeToLiveInMinutes": int,
    },
)

_RequiredCheckInLicenseRequestRequestTypeDef = TypedDict(
    "_RequiredCheckInLicenseRequestRequestTypeDef",
    {
        "LicenseConsumptionToken": str,
    },
)
_OptionalCheckInLicenseRequestRequestTypeDef = TypedDict(
    "_OptionalCheckInLicenseRequestRequestTypeDef",
    {
        "Beneficiary": str,
    },
    total=False,
)

class CheckInLicenseRequestRequestTypeDef(
    _RequiredCheckInLicenseRequestRequestTypeDef, _OptionalCheckInLicenseRequestRequestTypeDef
):
    pass

_RequiredCheckoutBorrowLicenseRequestRequestTypeDef = TypedDict(
    "_RequiredCheckoutBorrowLicenseRequestRequestTypeDef",
    {
        "LicenseArn": str,
        "Entitlements": List["EntitlementDataTypeDef"],
        "DigitalSignatureMethod": Literal["JWT_PS384"],
        "ClientToken": str,
    },
)
_OptionalCheckoutBorrowLicenseRequestRequestTypeDef = TypedDict(
    "_OptionalCheckoutBorrowLicenseRequestRequestTypeDef",
    {
        "NodeId": str,
        "CheckoutMetadata": List["MetadataTypeDef"],
    },
    total=False,
)

class CheckoutBorrowLicenseRequestRequestTypeDef(
    _RequiredCheckoutBorrowLicenseRequestRequestTypeDef,
    _OptionalCheckoutBorrowLicenseRequestRequestTypeDef,
):
    pass

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCheckoutLicenseRequestRequestTypeDef = TypedDict(
    "_RequiredCheckoutLicenseRequestRequestTypeDef",
    {
        "ProductSKU": str,
        "CheckoutType": Literal["PROVISIONAL"],
        "KeyFingerprint": str,
        "Entitlements": List["EntitlementDataTypeDef"],
        "ClientToken": str,
    },
)
_OptionalCheckoutLicenseRequestRequestTypeDef = TypedDict(
    "_OptionalCheckoutLicenseRequestRequestTypeDef",
    {
        "Beneficiary": str,
        "NodeId": str,
    },
    total=False,
)

class CheckoutLicenseRequestRequestTypeDef(
    _RequiredCheckoutLicenseRequestRequestTypeDef, _OptionalCheckoutLicenseRequestRequestTypeDef
):
    pass

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConsumedLicenseSummaryTypeDef = TypedDict(
    "ConsumedLicenseSummaryTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "ConsumedLicenses": int,
    },
    total=False,
)

ConsumptionConfigurationTypeDef = TypedDict(
    "ConsumptionConfigurationTypeDef",
    {
        "RenewType": RenewTypeType,
        "ProvisionalConfiguration": "ProvisionalConfigurationTypeDef",
        "BorrowConfiguration": "BorrowConfigurationTypeDef",
    },
    total=False,
)

CreateGrantRequestRequestTypeDef = TypedDict(
    "CreateGrantRequestRequestTypeDef",
    {
        "ClientToken": str,
        "GrantName": str,
        "LicenseArn": str,
        "Principals": List[str],
        "HomeRegion": str,
        "AllowedOperations": List[AllowedOperationType],
    },
)

CreateGrantResponseTypeDef = TypedDict(
    "CreateGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGrantVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateGrantVersionRequestRequestTypeDef",
    {
        "ClientToken": str,
        "GrantArn": str,
    },
)
_OptionalCreateGrantVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateGrantVersionRequestRequestTypeDef",
    {
        "GrantName": str,
        "AllowedOperations": List[AllowedOperationType],
        "Status": GrantStatusType,
        "StatusReason": str,
        "SourceVersion": str,
    },
    total=False,
)

class CreateGrantVersionRequestRequestTypeDef(
    _RequiredCreateGrantVersionRequestRequestTypeDef,
    _OptionalCreateGrantVersionRequestRequestTypeDef,
):
    pass

CreateGrantVersionResponseTypeDef = TypedDict(
    "CreateGrantVersionResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLicenseConfigurationRequestRequestTypeDef",
    {
        "Name": str,
        "LicenseCountingType": LicenseCountingTypeType,
    },
)
_OptionalCreateLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLicenseConfigurationRequestRequestTypeDef",
    {
        "Description": str,
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "LicenseRules": List[str],
        "Tags": List["TagTypeDef"],
        "DisassociateWhenNotFound": bool,
        "ProductInformationList": List["ProductInformationTypeDef"],
    },
    total=False,
)

class CreateLicenseConfigurationRequestRequestTypeDef(
    _RequiredCreateLicenseConfigurationRequestRequestTypeDef,
    _OptionalCreateLicenseConfigurationRequestRequestTypeDef,
):
    pass

CreateLicenseConfigurationResponseTypeDef = TypedDict(
    "CreateLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLicenseManagerReportGeneratorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLicenseManagerReportGeneratorRequestRequestTypeDef",
    {
        "ReportGeneratorName": str,
        "Type": List[ReportTypeType],
        "ReportContext": "ReportContextTypeDef",
        "ReportFrequency": "ReportFrequencyTypeDef",
        "ClientToken": str,
    },
)
_OptionalCreateLicenseManagerReportGeneratorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLicenseManagerReportGeneratorRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateLicenseManagerReportGeneratorRequestRequestTypeDef(
    _RequiredCreateLicenseManagerReportGeneratorRequestRequestTypeDef,
    _OptionalCreateLicenseManagerReportGeneratorRequestRequestTypeDef,
):
    pass

CreateLicenseManagerReportGeneratorResponseTypeDef = TypedDict(
    "CreateLicenseManagerReportGeneratorResponseTypeDef",
    {
        "LicenseManagerReportGeneratorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLicenseRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLicenseRequestRequestTypeDef",
    {
        "LicenseName": str,
        "ProductName": str,
        "ProductSKU": str,
        "Issuer": "IssuerTypeDef",
        "HomeRegion": str,
        "Validity": "DatetimeRangeTypeDef",
        "Entitlements": List["EntitlementTypeDef"],
        "Beneficiary": str,
        "ConsumptionConfiguration": "ConsumptionConfigurationTypeDef",
        "ClientToken": str,
    },
)
_OptionalCreateLicenseRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLicenseRequestRequestTypeDef",
    {
        "LicenseMetadata": List["MetadataTypeDef"],
    },
    total=False,
)

class CreateLicenseRequestRequestTypeDef(
    _RequiredCreateLicenseRequestRequestTypeDef, _OptionalCreateLicenseRequestRequestTypeDef
):
    pass

CreateLicenseResponseTypeDef = TypedDict(
    "CreateLicenseResponseTypeDef",
    {
        "LicenseArn": str,
        "Status": LicenseStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLicenseVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLicenseVersionRequestRequestTypeDef",
    {
        "LicenseArn": str,
        "LicenseName": str,
        "ProductName": str,
        "Issuer": "IssuerTypeDef",
        "HomeRegion": str,
        "Validity": "DatetimeRangeTypeDef",
        "Entitlements": List["EntitlementTypeDef"],
        "ConsumptionConfiguration": "ConsumptionConfigurationTypeDef",
        "Status": LicenseStatusType,
        "ClientToken": str,
    },
)
_OptionalCreateLicenseVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLicenseVersionRequestRequestTypeDef",
    {
        "LicenseMetadata": List["MetadataTypeDef"],
        "SourceVersion": str,
    },
    total=False,
)

class CreateLicenseVersionRequestRequestTypeDef(
    _RequiredCreateLicenseVersionRequestRequestTypeDef,
    _OptionalCreateLicenseVersionRequestRequestTypeDef,
):
    pass

CreateLicenseVersionResponseTypeDef = TypedDict(
    "CreateLicenseVersionResponseTypeDef",
    {
        "LicenseArn": str,
        "Version": str,
        "Status": LicenseStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTokenRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTokenRequestRequestTypeDef",
    {
        "LicenseArn": str,
        "ClientToken": str,
    },
)
_OptionalCreateTokenRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTokenRequestRequestTypeDef",
    {
        "RoleArns": List[str],
        "ExpirationInDays": int,
        "TokenProperties": List[str],
    },
    total=False,
)

class CreateTokenRequestRequestTypeDef(
    _RequiredCreateTokenRequestRequestTypeDef, _OptionalCreateTokenRequestRequestTypeDef
):
    pass

CreateTokenResponseTypeDef = TypedDict(
    "CreateTokenResponseTypeDef",
    {
        "TokenId": str,
        "TokenType": Literal["REFRESH_TOKEN"],
        "Token": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDatetimeRangeTypeDef = TypedDict(
    "_RequiredDatetimeRangeTypeDef",
    {
        "Begin": str,
    },
)
_OptionalDatetimeRangeTypeDef = TypedDict(
    "_OptionalDatetimeRangeTypeDef",
    {
        "End": str,
    },
    total=False,
)

class DatetimeRangeTypeDef(_RequiredDatetimeRangeTypeDef, _OptionalDatetimeRangeTypeDef):
    pass

_RequiredDeleteGrantRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteGrantRequestRequestTypeDef",
    {
        "GrantArn": str,
        "Version": str,
    },
)
_OptionalDeleteGrantRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteGrantRequestRequestTypeDef",
    {
        "StatusReason": str,
    },
    total=False,
)

class DeleteGrantRequestRequestTypeDef(
    _RequiredDeleteGrantRequestRequestTypeDef, _OptionalDeleteGrantRequestRequestTypeDef
):
    pass

DeleteGrantResponseTypeDef = TypedDict(
    "DeleteGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteLicenseConfigurationRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)

DeleteLicenseManagerReportGeneratorRequestRequestTypeDef = TypedDict(
    "DeleteLicenseManagerReportGeneratorRequestRequestTypeDef",
    {
        "LicenseManagerReportGeneratorArn": str,
    },
)

DeleteLicenseRequestRequestTypeDef = TypedDict(
    "DeleteLicenseRequestRequestTypeDef",
    {
        "LicenseArn": str,
        "SourceVersion": str,
    },
)

DeleteLicenseResponseTypeDef = TypedDict(
    "DeleteLicenseResponseTypeDef",
    {
        "Status": LicenseDeletionStatusType,
        "DeletionDate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTokenRequestRequestTypeDef = TypedDict(
    "DeleteTokenRequestRequestTypeDef",
    {
        "TokenId": str,
    },
)

_RequiredEntitlementDataTypeDef = TypedDict(
    "_RequiredEntitlementDataTypeDef",
    {
        "Name": str,
        "Unit": EntitlementDataUnitType,
    },
)
_OptionalEntitlementDataTypeDef = TypedDict(
    "_OptionalEntitlementDataTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class EntitlementDataTypeDef(_RequiredEntitlementDataTypeDef, _OptionalEntitlementDataTypeDef):
    pass

_RequiredEntitlementTypeDef = TypedDict(
    "_RequiredEntitlementTypeDef",
    {
        "Name": str,
        "Unit": EntitlementUnitType,
    },
)
_OptionalEntitlementTypeDef = TypedDict(
    "_OptionalEntitlementTypeDef",
    {
        "Value": str,
        "MaxCount": int,
        "Overage": bool,
        "AllowCheckIn": bool,
    },
    total=False,
)

class EntitlementTypeDef(_RequiredEntitlementTypeDef, _OptionalEntitlementTypeDef):
    pass

_RequiredEntitlementUsageTypeDef = TypedDict(
    "_RequiredEntitlementUsageTypeDef",
    {
        "Name": str,
        "ConsumedValue": str,
        "Unit": EntitlementDataUnitType,
    },
)
_OptionalEntitlementUsageTypeDef = TypedDict(
    "_OptionalEntitlementUsageTypeDef",
    {
        "MaxCount": str,
    },
    total=False,
)

class EntitlementUsageTypeDef(_RequiredEntitlementUsageTypeDef, _OptionalEntitlementUsageTypeDef):
    pass

_RequiredExtendLicenseConsumptionRequestRequestTypeDef = TypedDict(
    "_RequiredExtendLicenseConsumptionRequestRequestTypeDef",
    {
        "LicenseConsumptionToken": str,
    },
)
_OptionalExtendLicenseConsumptionRequestRequestTypeDef = TypedDict(
    "_OptionalExtendLicenseConsumptionRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ExtendLicenseConsumptionRequestRequestTypeDef(
    _RequiredExtendLicenseConsumptionRequestRequestTypeDef,
    _OptionalExtendLicenseConsumptionRequestRequestTypeDef,
):
    pass

ExtendLicenseConsumptionResponseTypeDef = TypedDict(
    "ExtendLicenseConsumptionResponseTypeDef",
    {
        "LicenseConsumptionToken": str,
        "Expiration": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
    total=False,
)

_RequiredGetAccessTokenRequestRequestTypeDef = TypedDict(
    "_RequiredGetAccessTokenRequestRequestTypeDef",
    {
        "Token": str,
    },
)
_OptionalGetAccessTokenRequestRequestTypeDef = TypedDict(
    "_OptionalGetAccessTokenRequestRequestTypeDef",
    {
        "TokenProperties": List[str],
    },
    total=False,
)

class GetAccessTokenRequestRequestTypeDef(
    _RequiredGetAccessTokenRequestRequestTypeDef, _OptionalGetAccessTokenRequestRequestTypeDef
):
    pass

GetAccessTokenResponseTypeDef = TypedDict(
    "GetAccessTokenResponseTypeDef",
    {
        "AccessToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetGrantRequestRequestTypeDef = TypedDict(
    "_RequiredGetGrantRequestRequestTypeDef",
    {
        "GrantArn": str,
    },
)
_OptionalGetGrantRequestRequestTypeDef = TypedDict(
    "_OptionalGetGrantRequestRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)

class GetGrantRequestRequestTypeDef(
    _RequiredGetGrantRequestRequestTypeDef, _OptionalGetGrantRequestRequestTypeDef
):
    pass

GetGrantResponseTypeDef = TypedDict(
    "GetGrantResponseTypeDef",
    {
        "Grant": "GrantTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "GetLicenseConfigurationRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)

GetLicenseConfigurationResponseTypeDef = TypedDict(
    "GetLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationId": str,
        "LicenseConfigurationArn": str,
        "Name": str,
        "Description": str,
        "LicenseCountingType": LicenseCountingTypeType,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLicenseManagerReportGeneratorRequestRequestTypeDef = TypedDict(
    "GetLicenseManagerReportGeneratorRequestRequestTypeDef",
    {
        "LicenseManagerReportGeneratorArn": str,
    },
)

GetLicenseManagerReportGeneratorResponseTypeDef = TypedDict(
    "GetLicenseManagerReportGeneratorResponseTypeDef",
    {
        "ReportGenerator": "ReportGeneratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLicenseRequestRequestTypeDef = TypedDict(
    "_RequiredGetLicenseRequestRequestTypeDef",
    {
        "LicenseArn": str,
    },
)
_OptionalGetLicenseRequestRequestTypeDef = TypedDict(
    "_OptionalGetLicenseRequestRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)

class GetLicenseRequestRequestTypeDef(
    _RequiredGetLicenseRequestRequestTypeDef, _OptionalGetLicenseRequestRequestTypeDef
):
    pass

GetLicenseResponseTypeDef = TypedDict(
    "GetLicenseResponseTypeDef",
    {
        "License": "LicenseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLicenseUsageRequestRequestTypeDef = TypedDict(
    "GetLicenseUsageRequestRequestTypeDef",
    {
        "LicenseArn": str,
    },
)

GetLicenseUsageResponseTypeDef = TypedDict(
    "GetLicenseUsageResponseTypeDef",
    {
        "LicenseUsage": "LicenseUsageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceSettingsResponseTypeDef = TypedDict(
    "GetServiceSettingsResponseTypeDef",
    {
        "S3BucketArn": str,
        "SnsTopicArn": str,
        "OrganizationConfiguration": "OrganizationConfigurationTypeDef",
        "EnableCrossAccountsDiscovery": bool,
        "LicenseManagerResourceShareArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGrantTypeDef = TypedDict(
    "_RequiredGrantTypeDef",
    {
        "GrantArn": str,
        "GrantName": str,
        "ParentArn": str,
        "LicenseArn": str,
        "GranteePrincipalArn": str,
        "HomeRegion": str,
        "GrantStatus": GrantStatusType,
        "Version": str,
        "GrantedOperations": List[AllowedOperationType],
    },
)
_OptionalGrantTypeDef = TypedDict(
    "_OptionalGrantTypeDef",
    {
        "StatusReason": str,
    },
    total=False,
)

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
        "Status": LicenseStatusType,
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

_RequiredInventoryFilterTypeDef = TypedDict(
    "_RequiredInventoryFilterTypeDef",
    {
        "Name": str,
        "Condition": InventoryFilterConditionType,
    },
)
_OptionalInventoryFilterTypeDef = TypedDict(
    "_OptionalInventoryFilterTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class InventoryFilterTypeDef(_RequiredInventoryFilterTypeDef, _OptionalInventoryFilterTypeDef):
    pass

IssuerDetailsTypeDef = TypedDict(
    "IssuerDetailsTypeDef",
    {
        "Name": str,
        "SignKey": str,
        "KeyFingerprint": str,
    },
    total=False,
)

_RequiredIssuerTypeDef = TypedDict(
    "_RequiredIssuerTypeDef",
    {
        "Name": str,
    },
)
_OptionalIssuerTypeDef = TypedDict(
    "_OptionalIssuerTypeDef",
    {
        "SignKey": str,
    },
    total=False,
)

class IssuerTypeDef(_RequiredIssuerTypeDef, _OptionalIssuerTypeDef):
    pass

LicenseConfigurationAssociationTypeDef = TypedDict(
    "LicenseConfigurationAssociationTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": ResourceTypeType,
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
        "LicenseCountingType": LicenseCountingTypeType,
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
        "ResourceType": ResourceTypeType,
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
        "ResourceType": ResourceTypeType,
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
    "_RequiredLicenseSpecificationTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)
_OptionalLicenseSpecificationTypeDef = TypedDict(
    "_OptionalLicenseSpecificationTypeDef",
    {
        "AmiAssociationScope": str,
    },
    total=False,
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
        "Status": LicenseStatusType,
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
    "LicenseUsageTypeDef",
    {
        "EntitlementUsages": List["EntitlementUsageTypeDef"],
    },
    total=False,
)

_RequiredListAssociationsForLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredListAssociationsForLicenseConfigurationRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)
_OptionalListAssociationsForLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalListAssociationsForLicenseConfigurationRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAssociationsForLicenseConfigurationRequestRequestTypeDef(
    _RequiredListAssociationsForLicenseConfigurationRequestRequestTypeDef,
    _OptionalListAssociationsForLicenseConfigurationRequestRequestTypeDef,
):
    pass

ListAssociationsForLicenseConfigurationResponseTypeDef = TypedDict(
    "ListAssociationsForLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationAssociations": List["LicenseConfigurationAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDistributedGrantsRequestRequestTypeDef = TypedDict(
    "ListDistributedGrantsRequestRequestTypeDef",
    {
        "GrantArns": List[str],
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDistributedGrantsResponseTypeDef = TypedDict(
    "ListDistributedGrantsResponseTypeDef",
    {
        "Grants": List["GrantTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef = TypedDict(
    "_RequiredListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)
_OptionalListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef = TypedDict(
    "_OptionalListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef(
    _RequiredListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef,
    _OptionalListFailuresForLicenseConfigurationOperationsRequestRequestTypeDef,
):
    pass

ListFailuresForLicenseConfigurationOperationsResponseTypeDef = TypedDict(
    "ListFailuresForLicenseConfigurationOperationsResponseTypeDef",
    {
        "LicenseOperationFailureList": List["LicenseOperationFailureTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLicenseConfigurationsRequestRequestTypeDef = TypedDict(
    "ListLicenseConfigurationsRequestRequestTypeDef",
    {
        "LicenseConfigurationArns": List[str],
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

ListLicenseConfigurationsResponseTypeDef = TypedDict(
    "ListLicenseConfigurationsResponseTypeDef",
    {
        "LicenseConfigurations": List["LicenseConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLicenseManagerReportGeneratorsRequestRequestTypeDef = TypedDict(
    "ListLicenseManagerReportGeneratorsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListLicenseManagerReportGeneratorsResponseTypeDef = TypedDict(
    "ListLicenseManagerReportGeneratorsResponseTypeDef",
    {
        "ReportGenerators": List["ReportGeneratorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLicenseSpecificationsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListLicenseSpecificationsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListLicenseSpecificationsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListLicenseSpecificationsForResourceRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListLicenseSpecificationsForResourceRequestRequestTypeDef(
    _RequiredListLicenseSpecificationsForResourceRequestRequestTypeDef,
    _OptionalListLicenseSpecificationsForResourceRequestRequestTypeDef,
):
    pass

ListLicenseSpecificationsForResourceResponseTypeDef = TypedDict(
    "ListLicenseSpecificationsForResourceResponseTypeDef",
    {
        "LicenseSpecifications": List["LicenseSpecificationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLicenseVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListLicenseVersionsRequestRequestTypeDef",
    {
        "LicenseArn": str,
    },
)
_OptionalListLicenseVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListLicenseVersionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListLicenseVersionsRequestRequestTypeDef(
    _RequiredListLicenseVersionsRequestRequestTypeDef,
    _OptionalListLicenseVersionsRequestRequestTypeDef,
):
    pass

ListLicenseVersionsResponseTypeDef = TypedDict(
    "ListLicenseVersionsResponseTypeDef",
    {
        "Licenses": List["LicenseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLicensesRequestRequestTypeDef = TypedDict(
    "ListLicensesRequestRequestTypeDef",
    {
        "LicenseArns": List[str],
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListLicensesResponseTypeDef = TypedDict(
    "ListLicensesResponseTypeDef",
    {
        "Licenses": List["LicenseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReceivedGrantsRequestRequestTypeDef = TypedDict(
    "ListReceivedGrantsRequestRequestTypeDef",
    {
        "GrantArns": List[str],
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListReceivedGrantsResponseTypeDef = TypedDict(
    "ListReceivedGrantsResponseTypeDef",
    {
        "Grants": List["GrantTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReceivedLicensesRequestRequestTypeDef = TypedDict(
    "ListReceivedLicensesRequestRequestTypeDef",
    {
        "LicenseArns": List[str],
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListReceivedLicensesResponseTypeDef = TypedDict(
    "ListReceivedLicensesResponseTypeDef",
    {
        "Licenses": List["GrantedLicenseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceInventoryRequestRequestTypeDef = TypedDict(
    "ListResourceInventoryRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["InventoryFilterTypeDef"],
    },
    total=False,
)

ListResourceInventoryResponseTypeDef = TypedDict(
    "ListResourceInventoryResponseTypeDef",
    {
        "ResourceInventoryList": List["ResourceInventoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTokensRequestRequestTypeDef = TypedDict(
    "ListTokensRequestRequestTypeDef",
    {
        "TokenIds": List[str],
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListTokensResponseTypeDef = TypedDict(
    "ListTokensResponseTypeDef",
    {
        "Tokens": List["TokenDataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsageForLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredListUsageForLicenseConfigurationRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)
_OptionalListUsageForLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalListUsageForLicenseConfigurationRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

class ListUsageForLicenseConfigurationRequestRequestTypeDef(
    _RequiredListUsageForLicenseConfigurationRequestRequestTypeDef,
    _OptionalListUsageForLicenseConfigurationRequestRequestTypeDef,
):
    pass

ListUsageForLicenseConfigurationResponseTypeDef = TypedDict(
    "ListUsageForLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationUsageList": List["LicenseConfigurationUsageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ManagedResourceSummaryTypeDef = TypedDict(
    "ManagedResourceSummaryTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "AssociationCount": int,
    },
    total=False,
)

MetadataTypeDef = TypedDict(
    "MetadataTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

OrganizationConfigurationTypeDef = TypedDict(
    "OrganizationConfigurationTypeDef",
    {
        "EnableIntegration": bool,
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

_RequiredProductInformationFilterTypeDef = TypedDict(
    "_RequiredProductInformationFilterTypeDef",
    {
        "ProductInformationFilterName": str,
        "ProductInformationFilterComparator": str,
    },
)
_OptionalProductInformationFilterTypeDef = TypedDict(
    "_OptionalProductInformationFilterTypeDef",
    {
        "ProductInformationFilterValue": List[str],
    },
    total=False,
)

class ProductInformationFilterTypeDef(
    _RequiredProductInformationFilterTypeDef, _OptionalProductInformationFilterTypeDef
):
    pass

ProductInformationTypeDef = TypedDict(
    "ProductInformationTypeDef",
    {
        "ResourceType": str,
        "ProductInformationFilterList": List["ProductInformationFilterTypeDef"],
    },
)

ProvisionalConfigurationTypeDef = TypedDict(
    "ProvisionalConfigurationTypeDef",
    {
        "MaxTimeToLiveInMinutes": int,
    },
)

ReceivedMetadataTypeDef = TypedDict(
    "ReceivedMetadataTypeDef",
    {
        "ReceivedStatus": ReceivedStatusType,
        "ReceivedStatusReason": str,
        "AllowedOperations": List[AllowedOperationType],
    },
    total=False,
)

RejectGrantRequestRequestTypeDef = TypedDict(
    "RejectGrantRequestRequestTypeDef",
    {
        "GrantArn": str,
    },
)

RejectGrantResponseTypeDef = TypedDict(
    "RejectGrantResponseTypeDef",
    {
        "GrantArn": str,
        "Status": GrantStatusType,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReportContextTypeDef = TypedDict(
    "ReportContextTypeDef",
    {
        "licenseConfigurationArns": List[str],
    },
)

ReportFrequencyTypeDef = TypedDict(
    "ReportFrequencyTypeDef",
    {
        "value": int,
        "period": ReportFrequencyTypeType,
    },
    total=False,
)

ReportGeneratorTypeDef = TypedDict(
    "ReportGeneratorTypeDef",
    {
        "ReportGeneratorName": str,
        "ReportType": List[ReportTypeType],
        "ReportContext": "ReportContextTypeDef",
        "ReportFrequency": "ReportFrequencyTypeDef",
        "LicenseManagerReportGeneratorArn": str,
        "LastRunStatus": str,
        "LastRunFailureReason": str,
        "LastReportGenerationTime": str,
        "ReportCreatorAccount": str,
        "Description": str,
        "S3Location": "S3LocationTypeDef",
        "CreateTime": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ResourceInventoryTypeDef = TypedDict(
    "ResourceInventoryTypeDef",
    {
        "ResourceId": str,
        "ResourceType": ResourceTypeType,
        "ResourceArn": str,
        "Platform": str,
        "PlatformVersion": str,
        "ResourceOwningAccountId": str,
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

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "keyPrefix": str,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

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

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLicenseConfigurationRequestRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
)
_OptionalUpdateLicenseConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLicenseConfigurationRequestRequestTypeDef",
    {
        "LicenseConfigurationStatus": LicenseConfigurationStatusType,
        "LicenseRules": List[str],
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "Name": str,
        "Description": str,
        "ProductInformationList": List["ProductInformationTypeDef"],
        "DisassociateWhenNotFound": bool,
    },
    total=False,
)

class UpdateLicenseConfigurationRequestRequestTypeDef(
    _RequiredUpdateLicenseConfigurationRequestRequestTypeDef,
    _OptionalUpdateLicenseConfigurationRequestRequestTypeDef,
):
    pass

_RequiredUpdateLicenseManagerReportGeneratorRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLicenseManagerReportGeneratorRequestRequestTypeDef",
    {
        "LicenseManagerReportGeneratorArn": str,
        "ReportGeneratorName": str,
        "Type": List[ReportTypeType],
        "ReportContext": "ReportContextTypeDef",
        "ReportFrequency": "ReportFrequencyTypeDef",
        "ClientToken": str,
    },
)
_OptionalUpdateLicenseManagerReportGeneratorRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLicenseManagerReportGeneratorRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateLicenseManagerReportGeneratorRequestRequestTypeDef(
    _RequiredUpdateLicenseManagerReportGeneratorRequestRequestTypeDef,
    _OptionalUpdateLicenseManagerReportGeneratorRequestRequestTypeDef,
):
    pass

_RequiredUpdateLicenseSpecificationsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLicenseSpecificationsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalUpdateLicenseSpecificationsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLicenseSpecificationsForResourceRequestRequestTypeDef",
    {
        "AddLicenseSpecifications": List["LicenseSpecificationTypeDef"],
        "RemoveLicenseSpecifications": List["LicenseSpecificationTypeDef"],
    },
    total=False,
)

class UpdateLicenseSpecificationsForResourceRequestRequestTypeDef(
    _RequiredUpdateLicenseSpecificationsForResourceRequestRequestTypeDef,
    _OptionalUpdateLicenseSpecificationsForResourceRequestRequestTypeDef,
):
    pass

UpdateServiceSettingsRequestRequestTypeDef = TypedDict(
    "UpdateServiceSettingsRequestRequestTypeDef",
    {
        "S3BucketArn": str,
        "SnsTopicArn": str,
        "OrganizationConfiguration": "OrganizationConfigurationTypeDef",
        "EnableCrossAccountsDiscovery": bool,
    },
    total=False,
)
