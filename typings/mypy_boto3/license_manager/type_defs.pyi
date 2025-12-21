"""
Type annotations for license-manager service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_license_manager.type_defs import AcceptGrantRequestTypeDef

    data: AcceptGrantRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ActivationOverrideBehaviorType,
    AllowedOperationType,
    CheckoutTypeType,
    EntitlementDataUnitType,
    EntitlementUnitType,
    GrantStatusType,
    InventoryFilterConditionType,
    LicenseAssetGroupStatusType,
    LicenseConfigurationStatusType,
    LicenseConversionTaskStatusType,
    LicenseCountingTypeType,
    LicenseDeletionStatusType,
    LicenseStatusType,
    ReceivedStatusType,
    RenewTypeType,
    ReportFrequencyTypeType,
    ReportTypeType,
    ResourceTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AcceptGrantRequestTypeDef",
    "AcceptGrantResponseTypeDef",
    "AndRuleStatementOutputTypeDef",
    "AndRuleStatementTypeDef",
    "AndRuleStatementUnionTypeDef",
    "AssetTypeDef",
    "AutomatedDiscoveryInformationTypeDef",
    "BorrowConfigurationTypeDef",
    "CheckInLicenseRequestTypeDef",
    "CheckoutBorrowLicenseRequestTypeDef",
    "CheckoutBorrowLicenseResponseTypeDef",
    "CheckoutLicenseRequestTypeDef",
    "CheckoutLicenseResponseTypeDef",
    "ConsumedLicenseSummaryTypeDef",
    "ConsumptionConfigurationTypeDef",
    "CreateGrantRequestTypeDef",
    "CreateGrantResponseTypeDef",
    "CreateGrantVersionRequestTypeDef",
    "CreateGrantVersionResponseTypeDef",
    "CreateLicenseAssetGroupRequestTypeDef",
    "CreateLicenseAssetGroupResponseTypeDef",
    "CreateLicenseAssetRulesetRequestTypeDef",
    "CreateLicenseAssetRulesetResponseTypeDef",
    "CreateLicenseConfigurationRequestTypeDef",
    "CreateLicenseConfigurationResponseTypeDef",
    "CreateLicenseConversionTaskForResourceRequestTypeDef",
    "CreateLicenseConversionTaskForResourceResponseTypeDef",
    "CreateLicenseManagerReportGeneratorRequestTypeDef",
    "CreateLicenseManagerReportGeneratorResponseTypeDef",
    "CreateLicenseRequestTypeDef",
    "CreateLicenseResponseTypeDef",
    "CreateLicenseVersionRequestTypeDef",
    "CreateLicenseVersionResponseTypeDef",
    "CreateTokenRequestTypeDef",
    "CreateTokenResponseTypeDef",
    "CrossAccountDiscoveryServiceStatusTypeDef",
    "CrossRegionDiscoveryStatusTypeDef",
    "DatetimeRangeTypeDef",
    "DeleteGrantRequestTypeDef",
    "DeleteGrantResponseTypeDef",
    "DeleteLicenseAssetGroupRequestTypeDef",
    "DeleteLicenseAssetGroupResponseTypeDef",
    "DeleteLicenseAssetRulesetRequestTypeDef",
    "DeleteLicenseConfigurationRequestTypeDef",
    "DeleteLicenseManagerReportGeneratorRequestTypeDef",
    "DeleteLicenseRequestTypeDef",
    "DeleteLicenseResponseTypeDef",
    "DeleteTokenRequestTypeDef",
    "EntitlementDataTypeDef",
    "EntitlementTypeDef",
    "EntitlementUsageTypeDef",
    "ExtendLicenseConsumptionRequestTypeDef",
    "ExtendLicenseConsumptionResponseTypeDef",
    "FilterTypeDef",
    "GetAccessTokenRequestTypeDef",
    "GetAccessTokenResponseTypeDef",
    "GetGrantRequestTypeDef",
    "GetGrantResponseTypeDef",
    "GetLicenseAssetGroupRequestTypeDef",
    "GetLicenseAssetGroupResponseTypeDef",
    "GetLicenseAssetRulesetRequestTypeDef",
    "GetLicenseAssetRulesetResponseTypeDef",
    "GetLicenseConfigurationRequestTypeDef",
    "GetLicenseConfigurationResponseTypeDef",
    "GetLicenseConversionTaskRequestTypeDef",
    "GetLicenseConversionTaskResponseTypeDef",
    "GetLicenseManagerReportGeneratorRequestTypeDef",
    "GetLicenseManagerReportGeneratorResponseTypeDef",
    "GetLicenseRequestTypeDef",
    "GetLicenseResponseTypeDef",
    "GetLicenseUsageRequestTypeDef",
    "GetLicenseUsageResponseTypeDef",
    "GetServiceSettingsResponseTypeDef",
    "GrantTypeDef",
    "GrantedLicenseTypeDef",
    "InstanceRuleStatementOutputTypeDef",
    "InstanceRuleStatementTypeDef",
    "InstanceRuleStatementUnionTypeDef",
    "InventoryFilterTypeDef",
    "IssuerDetailsTypeDef",
    "IssuerTypeDef",
    "LicenseAssetGroupConfigurationTypeDef",
    "LicenseAssetGroupPropertyTypeDef",
    "LicenseAssetGroupTypeDef",
    "LicenseAssetRuleOutputTypeDef",
    "LicenseAssetRuleTypeDef",
    "LicenseAssetRuleUnionTypeDef",
    "LicenseAssetRulesetTypeDef",
    "LicenseConfigurationAssociationTypeDef",
    "LicenseConfigurationRuleStatementOutputTypeDef",
    "LicenseConfigurationRuleStatementTypeDef",
    "LicenseConfigurationRuleStatementUnionTypeDef",
    "LicenseConfigurationTypeDef",
    "LicenseConfigurationUsageTypeDef",
    "LicenseConversionContextOutputTypeDef",
    "LicenseConversionContextTypeDef",
    "LicenseConversionContextUnionTypeDef",
    "LicenseConversionTaskTypeDef",
    "LicenseOperationFailureTypeDef",
    "LicenseRuleStatementOutputTypeDef",
    "LicenseRuleStatementTypeDef",
    "LicenseRuleStatementUnionTypeDef",
    "LicenseSpecificationTypeDef",
    "LicenseTypeDef",
    "LicenseUsageTypeDef",
    "ListAssetsForLicenseAssetGroupRequestTypeDef",
    "ListAssetsForLicenseAssetGroupResponseTypeDef",
    "ListAssociationsForLicenseConfigurationRequestPaginateTypeDef",
    "ListAssociationsForLicenseConfigurationRequestTypeDef",
    "ListAssociationsForLicenseConfigurationResponseTypeDef",
    "ListDistributedGrantsRequestTypeDef",
    "ListDistributedGrantsResponseTypeDef",
    "ListFailuresForLicenseConfigurationOperationsRequestTypeDef",
    "ListFailuresForLicenseConfigurationOperationsResponseTypeDef",
    "ListLicenseAssetGroupsRequestTypeDef",
    "ListLicenseAssetGroupsResponseTypeDef",
    "ListLicenseAssetRulesetsRequestTypeDef",
    "ListLicenseAssetRulesetsResponseTypeDef",
    "ListLicenseConfigurationsForOrganizationRequestTypeDef",
    "ListLicenseConfigurationsForOrganizationResponseTypeDef",
    "ListLicenseConfigurationsRequestPaginateTypeDef",
    "ListLicenseConfigurationsRequestTypeDef",
    "ListLicenseConfigurationsResponseTypeDef",
    "ListLicenseConversionTasksRequestTypeDef",
    "ListLicenseConversionTasksResponseTypeDef",
    "ListLicenseManagerReportGeneratorsRequestTypeDef",
    "ListLicenseManagerReportGeneratorsResponseTypeDef",
    "ListLicenseSpecificationsForResourceRequestPaginateTypeDef",
    "ListLicenseSpecificationsForResourceRequestTypeDef",
    "ListLicenseSpecificationsForResourceResponseTypeDef",
    "ListLicenseVersionsRequestTypeDef",
    "ListLicenseVersionsResponseTypeDef",
    "ListLicensesRequestTypeDef",
    "ListLicensesResponseTypeDef",
    "ListReceivedGrantsForOrganizationRequestTypeDef",
    "ListReceivedGrantsForOrganizationResponseTypeDef",
    "ListReceivedGrantsRequestTypeDef",
    "ListReceivedGrantsResponseTypeDef",
    "ListReceivedLicensesForOrganizationRequestTypeDef",
    "ListReceivedLicensesForOrganizationResponseTypeDef",
    "ListReceivedLicensesRequestTypeDef",
    "ListReceivedLicensesResponseTypeDef",
    "ListResourceInventoryRequestPaginateTypeDef",
    "ListResourceInventoryRequestTypeDef",
    "ListResourceInventoryResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTokensRequestTypeDef",
    "ListTokensResponseTypeDef",
    "ListUsageForLicenseConfigurationRequestPaginateTypeDef",
    "ListUsageForLicenseConfigurationRequestTypeDef",
    "ListUsageForLicenseConfigurationResponseTypeDef",
    "ManagedResourceSummaryTypeDef",
    "MatchingRuleStatementOutputTypeDef",
    "MatchingRuleStatementTypeDef",
    "MatchingRuleStatementUnionTypeDef",
    "MetadataTypeDef",
    "OptionsTypeDef",
    "OrRuleStatementOutputTypeDef",
    "OrRuleStatementTypeDef",
    "OrRuleStatementUnionTypeDef",
    "OrganizationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ProductCodeListItemTypeDef",
    "ProductInformationFilterOutputTypeDef",
    "ProductInformationFilterTypeDef",
    "ProductInformationFilterUnionTypeDef",
    "ProductInformationOutputTypeDef",
    "ProductInformationTypeDef",
    "ProductInformationUnionTypeDef",
    "ProvisionalConfigurationTypeDef",
    "ReceivedMetadataTypeDef",
    "RegionStatusTypeDef",
    "RejectGrantRequestTypeDef",
    "RejectGrantResponseTypeDef",
    "ReportContextOutputTypeDef",
    "ReportContextTypeDef",
    "ReportContextUnionTypeDef",
    "ReportFrequencyTypeDef",
    "ReportGeneratorTypeDef",
    "ResourceInventoryTypeDef",
    "ResponseMetadataTypeDef",
    "RuleStatementOutputTypeDef",
    "RuleStatementTypeDef",
    "RuleStatementUnionTypeDef",
    "S3LocationTypeDef",
    "ScriptRuleStatementTypeDef",
    "ServiceStatusTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "TokenDataTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateLicenseAssetGroupRequestTypeDef",
    "UpdateLicenseAssetGroupResponseTypeDef",
    "UpdateLicenseAssetRulesetRequestTypeDef",
    "UpdateLicenseAssetRulesetResponseTypeDef",
    "UpdateLicenseConfigurationRequestTypeDef",
    "UpdateLicenseManagerReportGeneratorRequestTypeDef",
    "UpdateLicenseSpecificationsForResourceRequestTypeDef",
    "UpdateServiceSettingsRequestTypeDef",
)

class AcceptGrantRequestTypeDef(TypedDict):
    GrantArn: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class MatchingRuleStatementOutputTypeDef(TypedDict):
    KeyToMatch: str
    Constraint: str
    ValueToMatch: List[str]

class ScriptRuleStatementTypeDef(TypedDict):
    KeyToMatch: str
    Script: str

class AssetTypeDef(TypedDict):
    AssetArn: NotRequired[str]
    LatestAssetDiscoveryTime: NotRequired[datetime]

class AutomatedDiscoveryInformationTypeDef(TypedDict):
    LastRunTime: NotRequired[datetime]

class BorrowConfigurationTypeDef(TypedDict):
    AllowEarlyCheckIn: bool
    MaxTimeToLiveInMinutes: int

class CheckInLicenseRequestTypeDef(TypedDict):
    LicenseConsumptionToken: str
    Beneficiary: NotRequired[str]

class EntitlementDataTypeDef(TypedDict):
    Name: str
    Unit: EntitlementDataUnitType
    Value: NotRequired[str]

class MetadataTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[str]

class ConsumedLicenseSummaryTypeDef(TypedDict):
    ResourceType: NotRequired[ResourceTypeType]
    ConsumedLicenses: NotRequired[int]

class ProvisionalConfigurationTypeDef(TypedDict):
    MaxTimeToLiveInMinutes: int

class TagTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class OptionsTypeDef(TypedDict):
    ActivationOverrideBehavior: NotRequired[ActivationOverrideBehaviorType]

class LicenseAssetGroupConfigurationTypeDef(TypedDict):
    UsageDimension: NotRequired[str]

class LicenseAssetGroupPropertyTypeDef(TypedDict):
    Key: str
    Value: str

class ReportFrequencyTypeDef(TypedDict):
    value: NotRequired[int]
    period: NotRequired[ReportFrequencyTypeType]

class DatetimeRangeTypeDef(TypedDict):
    Begin: str
    End: NotRequired[str]

class EntitlementTypeDef(TypedDict):
    Name: str
    Unit: EntitlementUnitType
    Value: NotRequired[str]
    MaxCount: NotRequired[int]
    Overage: NotRequired[bool]
    AllowCheckIn: NotRequired[bool]

class IssuerTypeDef(TypedDict):
    Name: str
    SignKey: NotRequired[str]

class CreateTokenRequestTypeDef(TypedDict):
    LicenseArn: str
    ClientToken: str
    RoleArns: NotRequired[Sequence[str]]
    ExpirationInDays: NotRequired[int]
    TokenProperties: NotRequired[Sequence[str]]

class CrossAccountDiscoveryServiceStatusTypeDef(TypedDict):
    Message: NotRequired[str]

class RegionStatusTypeDef(TypedDict):
    Status: NotRequired[str]

class DeleteGrantRequestTypeDef(TypedDict):
    GrantArn: str
    Version: str
    StatusReason: NotRequired[str]

class DeleteLicenseAssetGroupRequestTypeDef(TypedDict):
    LicenseAssetGroupArn: str

class DeleteLicenseAssetRulesetRequestTypeDef(TypedDict):
    LicenseAssetRulesetArn: str

class DeleteLicenseConfigurationRequestTypeDef(TypedDict):
    LicenseConfigurationArn: str

class DeleteLicenseManagerReportGeneratorRequestTypeDef(TypedDict):
    LicenseManagerReportGeneratorArn: str

class DeleteLicenseRequestTypeDef(TypedDict):
    LicenseArn: str
    SourceVersion: str

class DeleteTokenRequestTypeDef(TypedDict):
    TokenId: str

class EntitlementUsageTypeDef(TypedDict):
    Name: str
    ConsumedValue: str
    Unit: EntitlementDataUnitType
    MaxCount: NotRequired[str]

class ExtendLicenseConsumptionRequestTypeDef(TypedDict):
    LicenseConsumptionToken: str
    DryRun: NotRequired[bool]

class FilterTypeDef(TypedDict):
    Name: NotRequired[str]
    Values: NotRequired[Sequence[str]]

class GetAccessTokenRequestTypeDef(TypedDict):
    Token: str
    TokenProperties: NotRequired[Sequence[str]]

class GetGrantRequestTypeDef(TypedDict):
    GrantArn: str
    Version: NotRequired[str]

class GetLicenseAssetGroupRequestTypeDef(TypedDict):
    LicenseAssetGroupArn: str

class GetLicenseAssetRulesetRequestTypeDef(TypedDict):
    LicenseAssetRulesetArn: str

class GetLicenseConfigurationRequestTypeDef(TypedDict):
    LicenseConfigurationArn: str

class ManagedResourceSummaryTypeDef(TypedDict):
    ResourceType: NotRequired[ResourceTypeType]
    AssociationCount: NotRequired[int]

class GetLicenseConversionTaskRequestTypeDef(TypedDict):
    LicenseConversionTaskId: str

class GetLicenseManagerReportGeneratorRequestTypeDef(TypedDict):
    LicenseManagerReportGeneratorArn: str

class GetLicenseRequestTypeDef(TypedDict):
    LicenseArn: str
    Version: NotRequired[str]

class GetLicenseUsageRequestTypeDef(TypedDict):
    LicenseArn: str

class OrganizationConfigurationTypeDef(TypedDict):
    EnableIntegration: bool

class IssuerDetailsTypeDef(TypedDict):
    Name: NotRequired[str]
    SignKey: NotRequired[str]
    KeyFingerprint: NotRequired[str]

class ReceivedMetadataTypeDef(TypedDict):
    ReceivedStatus: NotRequired[ReceivedStatusType]
    ReceivedStatusReason: NotRequired[str]
    AllowedOperations: NotRequired[List[AllowedOperationType]]

class InventoryFilterTypeDef(TypedDict):
    Name: str
    Condition: InventoryFilterConditionType
    Value: NotRequired[str]

class LicenseConfigurationAssociationTypeDef(TypedDict):
    ResourceArn: NotRequired[str]
    ResourceType: NotRequired[ResourceTypeType]
    ResourceOwnerId: NotRequired[str]
    AssociationTime: NotRequired[datetime]
    AmiAssociationScope: NotRequired[str]

class LicenseConfigurationUsageTypeDef(TypedDict):
    ResourceArn: NotRequired[str]
    ResourceType: NotRequired[ResourceTypeType]
    ResourceStatus: NotRequired[str]
    ResourceOwnerId: NotRequired[str]
    AssociationTime: NotRequired[datetime]
    ConsumedLicenses: NotRequired[int]

class ProductCodeListItemTypeDef(TypedDict):
    ProductCodeId: str
    ProductCodeType: Literal["marketplace"]

class LicenseSpecificationTypeDef(TypedDict):
    LicenseConfigurationArn: str
    AmiAssociationScope: NotRequired[str]

class ListAssetsForLicenseAssetGroupRequestTypeDef(TypedDict):
    LicenseAssetGroupArn: str
    AssetType: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAssociationsForLicenseConfigurationRequestTypeDef(TypedDict):
    LicenseConfigurationArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListFailuresForLicenseConfigurationOperationsRequestTypeDef(TypedDict):
    LicenseConfigurationArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListLicenseSpecificationsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListLicenseVersionsRequestTypeDef(TypedDict):
    LicenseArn: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ResourceInventoryTypeDef(TypedDict):
    ResourceId: NotRequired[str]
    ResourceType: NotRequired[ResourceTypeType]
    ResourceArn: NotRequired[str]
    Platform: NotRequired[str]
    PlatformVersion: NotRequired[str]
    ResourceOwningAccountId: NotRequired[str]
    MarketplaceProductCodes: NotRequired[List[str]]
    UsageOperation: NotRequired[str]
    AmiId: NotRequired[str]
    HostId: NotRequired[str]
    Region: NotRequired[str]
    InstanceType: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class TokenDataTypeDef(TypedDict):
    TokenId: NotRequired[str]
    TokenType: NotRequired[str]
    LicenseArn: NotRequired[str]
    ExpirationTime: NotRequired[str]
    TokenProperties: NotRequired[List[str]]
    RoleArns: NotRequired[List[str]]
    Status: NotRequired[str]

class MatchingRuleStatementTypeDef(TypedDict):
    KeyToMatch: str
    Constraint: str
    ValueToMatch: Sequence[str]

class ProductInformationFilterOutputTypeDef(TypedDict):
    ProductInformationFilterName: str
    ProductInformationFilterComparator: str
    ProductInformationFilterValue: NotRequired[List[str]]

class ProductInformationFilterTypeDef(TypedDict):
    ProductInformationFilterName: str
    ProductInformationFilterComparator: str
    ProductInformationFilterValue: NotRequired[Sequence[str]]

class RejectGrantRequestTypeDef(TypedDict):
    GrantArn: str

class ReportContextOutputTypeDef(TypedDict):
    licenseConfigurationArns: NotRequired[List[str]]
    licenseAssetGroupArns: NotRequired[List[str]]
    reportStartDate: NotRequired[datetime]
    reportEndDate: NotRequired[datetime]

TimestampTypeDef = Union[datetime, str]

class S3LocationTypeDef(TypedDict):
    bucket: NotRequired[str]
    keyPrefix: NotRequired[str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class AcceptGrantResponseTypeDef(TypedDict):
    GrantArn: str
    Status: GrantStatusType
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGrantResponseTypeDef(TypedDict):
    GrantArn: str
    Status: GrantStatusType
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGrantVersionResponseTypeDef(TypedDict):
    GrantArn: str
    Status: GrantStatusType
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLicenseAssetGroupResponseTypeDef(TypedDict):
    LicenseAssetGroupArn: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLicenseAssetRulesetResponseTypeDef(TypedDict):
    LicenseAssetRulesetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLicenseConfigurationResponseTypeDef(TypedDict):
    LicenseConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLicenseConversionTaskForResourceResponseTypeDef(TypedDict):
    LicenseConversionTaskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLicenseManagerReportGeneratorResponseTypeDef(TypedDict):
    LicenseManagerReportGeneratorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLicenseResponseTypeDef(TypedDict):
    LicenseArn: str
    Status: LicenseStatusType
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLicenseVersionResponseTypeDef(TypedDict):
    LicenseArn: str
    Version: str
    Status: LicenseStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTokenResponseTypeDef(TypedDict):
    TokenId: str
    TokenType: Literal["REFRESH_TOKEN"]
    Token: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGrantResponseTypeDef(TypedDict):
    GrantArn: str
    Status: GrantStatusType
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLicenseAssetGroupResponseTypeDef(TypedDict):
    Status: LicenseAssetGroupStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLicenseResponseTypeDef(TypedDict):
    Status: LicenseDeletionStatusType
    DeletionDate: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExtendLicenseConsumptionResponseTypeDef(TypedDict):
    LicenseConsumptionToken: str
    Expiration: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessTokenResponseTypeDef(TypedDict):
    AccessToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RejectGrantResponseTypeDef(TypedDict):
    GrantArn: str
    Status: GrantStatusType
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLicenseAssetGroupResponseTypeDef(TypedDict):
    LicenseAssetGroupArn: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLicenseAssetRulesetResponseTypeDef(TypedDict):
    LicenseAssetRulesetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AndRuleStatementOutputTypeDef(TypedDict):
    MatchingRuleStatements: NotRequired[List[MatchingRuleStatementOutputTypeDef]]
    ScriptRuleStatements: NotRequired[List[ScriptRuleStatementTypeDef]]

class OrRuleStatementOutputTypeDef(TypedDict):
    MatchingRuleStatements: NotRequired[List[MatchingRuleStatementOutputTypeDef]]
    ScriptRuleStatements: NotRequired[List[ScriptRuleStatementTypeDef]]

class ListAssetsForLicenseAssetGroupResponseTypeDef(TypedDict):
    Assets: List[AssetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CheckoutLicenseRequestTypeDef(TypedDict):
    ProductSKU: str
    CheckoutType: CheckoutTypeType
    KeyFingerprint: str
    Entitlements: Sequence[EntitlementDataTypeDef]
    ClientToken: str
    Beneficiary: NotRequired[str]
    NodeId: NotRequired[str]

class CheckoutLicenseResponseTypeDef(TypedDict):
    CheckoutType: CheckoutTypeType
    LicenseConsumptionToken: str
    EntitlementsAllowed: List[EntitlementDataTypeDef]
    SignedToken: str
    NodeId: str
    IssuedAt: str
    Expiration: str
    LicenseArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CheckoutBorrowLicenseRequestTypeDef(TypedDict):
    LicenseArn: str
    Entitlements: Sequence[EntitlementDataTypeDef]
    DigitalSignatureMethod: Literal["JWT_PS384"]
    ClientToken: str
    NodeId: NotRequired[str]
    CheckoutMetadata: NotRequired[Sequence[MetadataTypeDef]]

class CheckoutBorrowLicenseResponseTypeDef(TypedDict):
    LicenseArn: str
    LicenseConsumptionToken: str
    EntitlementsAllowed: List[EntitlementDataTypeDef]
    NodeId: str
    SignedToken: str
    IssuedAt: str
    Expiration: str
    CheckoutMetadata: List[MetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LicenseOperationFailureTypeDef(TypedDict):
    ResourceArn: NotRequired[str]
    ResourceType: NotRequired[ResourceTypeType]
    ErrorMessage: NotRequired[str]
    FailureTime: NotRequired[datetime]
    OperationName: NotRequired[str]
    ResourceOwnerId: NotRequired[str]
    OperationRequestedBy: NotRequired[str]
    MetadataList: NotRequired[List[MetadataTypeDef]]

class ConsumptionConfigurationTypeDef(TypedDict):
    RenewType: NotRequired[RenewTypeType]
    ProvisionalConfiguration: NotRequired[ProvisionalConfigurationTypeDef]
    BorrowConfiguration: NotRequired[BorrowConfigurationTypeDef]

class CreateGrantRequestTypeDef(TypedDict):
    ClientToken: str
    GrantName: str
    LicenseArn: str
    Principals: Sequence[str]
    HomeRegion: str
    AllowedOperations: Sequence[AllowedOperationType]
    Tags: NotRequired[Sequence[TagTypeDef]]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateGrantVersionRequestTypeDef(TypedDict):
    ClientToken: str
    GrantArn: str
    GrantName: NotRequired[str]
    AllowedOperations: NotRequired[Sequence[AllowedOperationType]]
    Status: NotRequired[GrantStatusType]
    StatusReason: NotRequired[str]
    SourceVersion: NotRequired[str]
    Options: NotRequired[OptionsTypeDef]

class GrantTypeDef(TypedDict):
    GrantArn: str
    GrantName: str
    ParentArn: str
    LicenseArn: str
    GranteePrincipalArn: str
    HomeRegion: str
    GrantStatus: GrantStatusType
    Version: str
    GrantedOperations: List[AllowedOperationType]
    StatusReason: NotRequired[str]
    Options: NotRequired[OptionsTypeDef]

class CreateLicenseAssetGroupRequestTypeDef(TypedDict):
    Name: str
    LicenseAssetGroupConfigurations: Sequence[LicenseAssetGroupConfigurationTypeDef]
    AssociatedLicenseAssetRulesetARNs: Sequence[str]
    ClientToken: str
    Description: NotRequired[str]
    Properties: NotRequired[Sequence[LicenseAssetGroupPropertyTypeDef]]
    Tags: NotRequired[Sequence[TagTypeDef]]

class LicenseAssetGroupTypeDef(TypedDict):
    Name: str
    AssociatedLicenseAssetRulesetARNs: List[str]
    LicenseAssetGroupArn: str
    Status: LicenseAssetGroupStatusType
    Description: NotRequired[str]
    LicenseAssetGroupConfigurations: NotRequired[List[LicenseAssetGroupConfigurationTypeDef]]
    Properties: NotRequired[List[LicenseAssetGroupPropertyTypeDef]]
    StatusMessage: NotRequired[str]
    LatestUsageAnalysisTime: NotRequired[datetime]
    LatestResourceDiscoveryTime: NotRequired[datetime]

class UpdateLicenseAssetGroupRequestTypeDef(TypedDict):
    AssociatedLicenseAssetRulesetARNs: Sequence[str]
    LicenseAssetGroupArn: str
    ClientToken: str
    Name: NotRequired[str]
    Description: NotRequired[str]
    LicenseAssetGroupConfigurations: NotRequired[Sequence[LicenseAssetGroupConfigurationTypeDef]]
    Properties: NotRequired[Sequence[LicenseAssetGroupPropertyTypeDef]]
    Status: NotRequired[LicenseAssetGroupStatusType]

class CrossRegionDiscoveryStatusTypeDef(TypedDict):
    Message: NotRequired[Dict[str, RegionStatusTypeDef]]

class LicenseUsageTypeDef(TypedDict):
    EntitlementUsages: NotRequired[List[EntitlementUsageTypeDef]]

class ListDistributedGrantsRequestTypeDef(TypedDict):
    GrantArns: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListLicenseAssetGroupsRequestTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListLicenseAssetRulesetsRequestTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    ShowAWSManagedLicenseAssetRulesets: NotRequired[bool]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListLicenseConfigurationsForOrganizationRequestTypeDef(TypedDict):
    LicenseConfigurationArns: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class ListLicenseConfigurationsRequestTypeDef(TypedDict):
    LicenseConfigurationArns: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class ListLicenseConversionTasksRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class ListLicenseManagerReportGeneratorsRequestTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListLicensesRequestTypeDef(TypedDict):
    LicenseArns: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListReceivedGrantsForOrganizationRequestTypeDef(TypedDict):
    LicenseArn: str
    Filters: NotRequired[Sequence[FilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListReceivedGrantsRequestTypeDef(TypedDict):
    GrantArns: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListReceivedLicensesForOrganizationRequestTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListReceivedLicensesRequestTypeDef(TypedDict):
    LicenseArns: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListTokensRequestTypeDef(TypedDict):
    TokenIds: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListUsageForLicenseConfigurationRequestTypeDef(TypedDict):
    LicenseConfigurationArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class UpdateServiceSettingsRequestTypeDef(TypedDict):
    S3BucketArn: NotRequired[str]
    SnsTopicArn: NotRequired[str]
    OrganizationConfiguration: NotRequired[OrganizationConfigurationTypeDef]
    EnableCrossAccountsDiscovery: NotRequired[bool]
    EnabledDiscoverySourceRegions: NotRequired[Sequence[str]]

class ListResourceInventoryRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Filters: NotRequired[Sequence[InventoryFilterTypeDef]]

class ListAssociationsForLicenseConfigurationResponseTypeDef(TypedDict):
    LicenseConfigurationAssociations: List[LicenseConfigurationAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListUsageForLicenseConfigurationResponseTypeDef(TypedDict):
    LicenseConfigurationUsageList: List[LicenseConfigurationUsageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class LicenseConversionContextOutputTypeDef(TypedDict):
    UsageOperation: NotRequired[str]
    ProductCodes: NotRequired[List[ProductCodeListItemTypeDef]]

class LicenseConversionContextTypeDef(TypedDict):
    UsageOperation: NotRequired[str]
    ProductCodes: NotRequired[Sequence[ProductCodeListItemTypeDef]]

class ListLicenseSpecificationsForResourceResponseTypeDef(TypedDict):
    LicenseSpecifications: List[LicenseSpecificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateLicenseSpecificationsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    AddLicenseSpecifications: NotRequired[Sequence[LicenseSpecificationTypeDef]]
    RemoveLicenseSpecifications: NotRequired[Sequence[LicenseSpecificationTypeDef]]

class ListAssociationsForLicenseConfigurationRequestPaginateTypeDef(TypedDict):
    LicenseConfigurationArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLicenseConfigurationsRequestPaginateTypeDef(TypedDict):
    LicenseConfigurationArns: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLicenseSpecificationsForResourceRequestPaginateTypeDef(TypedDict):
    ResourceArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceInventoryRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[InventoryFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListUsageForLicenseConfigurationRequestPaginateTypeDef(TypedDict):
    LicenseConfigurationArn: str
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceInventoryResponseTypeDef(TypedDict):
    ResourceInventoryList: List[ResourceInventoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTokensResponseTypeDef(TypedDict):
    Tokens: List[TokenDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

MatchingRuleStatementUnionTypeDef = Union[
    MatchingRuleStatementTypeDef, MatchingRuleStatementOutputTypeDef
]

class ProductInformationOutputTypeDef(TypedDict):
    ResourceType: str
    ProductInformationFilterList: List[ProductInformationFilterOutputTypeDef]

ProductInformationFilterUnionTypeDef = Union[
    ProductInformationFilterTypeDef, ProductInformationFilterOutputTypeDef
]

class ReportContextTypeDef(TypedDict):
    licenseConfigurationArns: NotRequired[Sequence[str]]
    licenseAssetGroupArns: NotRequired[Sequence[str]]
    reportStartDate: NotRequired[TimestampTypeDef]
    reportEndDate: NotRequired[TimestampTypeDef]

class ReportGeneratorTypeDef(TypedDict):
    ReportGeneratorName: NotRequired[str]
    ReportType: NotRequired[List[ReportTypeType]]
    ReportContext: NotRequired[ReportContextOutputTypeDef]
    ReportFrequency: NotRequired[ReportFrequencyTypeDef]
    LicenseManagerReportGeneratorArn: NotRequired[str]
    LastRunStatus: NotRequired[str]
    LastRunFailureReason: NotRequired[str]
    LastReportGenerationTime: NotRequired[str]
    ReportCreatorAccount: NotRequired[str]
    Description: NotRequired[str]
    S3Location: NotRequired[S3LocationTypeDef]
    CreateTime: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]

class InstanceRuleStatementOutputTypeDef(TypedDict):
    AndRuleStatement: NotRequired[AndRuleStatementOutputTypeDef]
    OrRuleStatement: NotRequired[OrRuleStatementOutputTypeDef]
    MatchingRuleStatement: NotRequired[MatchingRuleStatementOutputTypeDef]
    ScriptRuleStatement: NotRequired[ScriptRuleStatementTypeDef]

class LicenseConfigurationRuleStatementOutputTypeDef(TypedDict):
    AndRuleStatement: NotRequired[AndRuleStatementOutputTypeDef]
    OrRuleStatement: NotRequired[OrRuleStatementOutputTypeDef]
    MatchingRuleStatement: NotRequired[MatchingRuleStatementOutputTypeDef]

class LicenseRuleStatementOutputTypeDef(TypedDict):
    AndRuleStatement: NotRequired[AndRuleStatementOutputTypeDef]
    OrRuleStatement: NotRequired[OrRuleStatementOutputTypeDef]
    MatchingRuleStatement: NotRequired[MatchingRuleStatementOutputTypeDef]

class ListFailuresForLicenseConfigurationOperationsResponseTypeDef(TypedDict):
    LicenseOperationFailureList: List[LicenseOperationFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateLicenseRequestTypeDef(TypedDict):
    LicenseName: str
    ProductName: str
    ProductSKU: str
    Issuer: IssuerTypeDef
    HomeRegion: str
    Validity: DatetimeRangeTypeDef
    Entitlements: Sequence[EntitlementTypeDef]
    Beneficiary: str
    ConsumptionConfiguration: ConsumptionConfigurationTypeDef
    ClientToken: str
    LicenseMetadata: NotRequired[Sequence[MetadataTypeDef]]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateLicenseVersionRequestTypeDef(TypedDict):
    LicenseArn: str
    LicenseName: str
    ProductName: str
    Issuer: IssuerTypeDef
    HomeRegion: str
    Validity: DatetimeRangeTypeDef
    Entitlements: Sequence[EntitlementTypeDef]
    ConsumptionConfiguration: ConsumptionConfigurationTypeDef
    Status: LicenseStatusType
    ClientToken: str
    LicenseMetadata: NotRequired[Sequence[MetadataTypeDef]]
    SourceVersion: NotRequired[str]

class GrantedLicenseTypeDef(TypedDict):
    LicenseArn: NotRequired[str]
    LicenseName: NotRequired[str]
    ProductName: NotRequired[str]
    ProductSKU: NotRequired[str]
    Issuer: NotRequired[IssuerDetailsTypeDef]
    HomeRegion: NotRequired[str]
    Status: NotRequired[LicenseStatusType]
    Validity: NotRequired[DatetimeRangeTypeDef]
    Beneficiary: NotRequired[str]
    Entitlements: NotRequired[List[EntitlementTypeDef]]
    ConsumptionConfiguration: NotRequired[ConsumptionConfigurationTypeDef]
    LicenseMetadata: NotRequired[List[MetadataTypeDef]]
    CreateTime: NotRequired[str]
    Version: NotRequired[str]
    ReceivedMetadata: NotRequired[ReceivedMetadataTypeDef]

class LicenseTypeDef(TypedDict):
    LicenseArn: NotRequired[str]
    LicenseName: NotRequired[str]
    ProductName: NotRequired[str]
    ProductSKU: NotRequired[str]
    Issuer: NotRequired[IssuerDetailsTypeDef]
    HomeRegion: NotRequired[str]
    Status: NotRequired[LicenseStatusType]
    Validity: NotRequired[DatetimeRangeTypeDef]
    Beneficiary: NotRequired[str]
    Entitlements: NotRequired[List[EntitlementTypeDef]]
    ConsumptionConfiguration: NotRequired[ConsumptionConfigurationTypeDef]
    LicenseMetadata: NotRequired[List[MetadataTypeDef]]
    CreateTime: NotRequired[str]
    Version: NotRequired[str]

class GetGrantResponseTypeDef(TypedDict):
    Grant: GrantTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDistributedGrantsResponseTypeDef(TypedDict):
    Grants: List[GrantTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListReceivedGrantsForOrganizationResponseTypeDef(TypedDict):
    Grants: List[GrantTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListReceivedGrantsResponseTypeDef(TypedDict):
    Grants: List[GrantTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetLicenseAssetGroupResponseTypeDef(TypedDict):
    LicenseAssetGroup: LicenseAssetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLicenseAssetGroupsResponseTypeDef(TypedDict):
    LicenseAssetGroups: List[LicenseAssetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ServiceStatusTypeDef(TypedDict):
    CrossAccountDiscovery: NotRequired[CrossAccountDiscoveryServiceStatusTypeDef]
    CrossRegionDiscovery: NotRequired[CrossRegionDiscoveryStatusTypeDef]

class GetLicenseUsageResponseTypeDef(TypedDict):
    LicenseUsage: LicenseUsageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLicenseConversionTaskResponseTypeDef(TypedDict):
    LicenseConversionTaskId: str
    ResourceArn: str
    SourceLicenseContext: LicenseConversionContextOutputTypeDef
    DestinationLicenseContext: LicenseConversionContextOutputTypeDef
    StatusMessage: str
    Status: LicenseConversionTaskStatusType
    StartTime: datetime
    LicenseConversionTime: datetime
    EndTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class LicenseConversionTaskTypeDef(TypedDict):
    LicenseConversionTaskId: NotRequired[str]
    ResourceArn: NotRequired[str]
    SourceLicenseContext: NotRequired[LicenseConversionContextOutputTypeDef]
    DestinationLicenseContext: NotRequired[LicenseConversionContextOutputTypeDef]
    Status: NotRequired[LicenseConversionTaskStatusType]
    StatusMessage: NotRequired[str]
    StartTime: NotRequired[datetime]
    LicenseConversionTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]

LicenseConversionContextUnionTypeDef = Union[
    LicenseConversionContextTypeDef, LicenseConversionContextOutputTypeDef
]

class AndRuleStatementTypeDef(TypedDict):
    MatchingRuleStatements: NotRequired[Sequence[MatchingRuleStatementUnionTypeDef]]
    ScriptRuleStatements: NotRequired[Sequence[ScriptRuleStatementTypeDef]]

class OrRuleStatementTypeDef(TypedDict):
    MatchingRuleStatements: NotRequired[Sequence[MatchingRuleStatementUnionTypeDef]]
    ScriptRuleStatements: NotRequired[Sequence[ScriptRuleStatementTypeDef]]

class GetLicenseConfigurationResponseTypeDef(TypedDict):
    LicenseConfigurationId: str
    LicenseConfigurationArn: str
    Name: str
    Description: str
    LicenseCountingType: LicenseCountingTypeType
    LicenseRules: List[str]
    LicenseCount: int
    LicenseCountHardLimit: bool
    ConsumedLicenses: int
    Status: str
    OwnerAccountId: str
    ConsumedLicenseSummaryList: List[ConsumedLicenseSummaryTypeDef]
    ManagedResourceSummaryList: List[ManagedResourceSummaryTypeDef]
    Tags: List[TagTypeDef]
    ProductInformationList: List[ProductInformationOutputTypeDef]
    AutomatedDiscoveryInformation: AutomatedDiscoveryInformationTypeDef
    DisassociateWhenNotFound: bool
    LicenseExpiry: int
    ResponseMetadata: ResponseMetadataTypeDef

class LicenseConfigurationTypeDef(TypedDict):
    LicenseConfigurationId: NotRequired[str]
    LicenseConfigurationArn: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    LicenseCountingType: NotRequired[LicenseCountingTypeType]
    LicenseRules: NotRequired[List[str]]
    LicenseCount: NotRequired[int]
    LicenseCountHardLimit: NotRequired[bool]
    DisassociateWhenNotFound: NotRequired[bool]
    ConsumedLicenses: NotRequired[int]
    Status: NotRequired[str]
    OwnerAccountId: NotRequired[str]
    ConsumedLicenseSummaryList: NotRequired[List[ConsumedLicenseSummaryTypeDef]]
    ManagedResourceSummaryList: NotRequired[List[ManagedResourceSummaryTypeDef]]
    ProductInformationList: NotRequired[List[ProductInformationOutputTypeDef]]
    AutomatedDiscoveryInformation: NotRequired[AutomatedDiscoveryInformationTypeDef]
    LicenseExpiry: NotRequired[int]

class ProductInformationTypeDef(TypedDict):
    ResourceType: str
    ProductInformationFilterList: Sequence[ProductInformationFilterUnionTypeDef]

ReportContextUnionTypeDef = Union[ReportContextTypeDef, ReportContextOutputTypeDef]

class GetLicenseManagerReportGeneratorResponseTypeDef(TypedDict):
    ReportGenerator: ReportGeneratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLicenseManagerReportGeneratorsResponseTypeDef(TypedDict):
    ReportGenerators: List[ReportGeneratorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class RuleStatementOutputTypeDef(TypedDict):
    LicenseConfigurationRuleStatement: NotRequired[LicenseConfigurationRuleStatementOutputTypeDef]
    LicenseRuleStatement: NotRequired[LicenseRuleStatementOutputTypeDef]
    InstanceRuleStatement: NotRequired[InstanceRuleStatementOutputTypeDef]

class ListReceivedLicensesForOrganizationResponseTypeDef(TypedDict):
    Licenses: List[GrantedLicenseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListReceivedLicensesResponseTypeDef(TypedDict):
    Licenses: List[GrantedLicenseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetLicenseResponseTypeDef(TypedDict):
    License: LicenseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLicenseVersionsResponseTypeDef(TypedDict):
    Licenses: List[LicenseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListLicensesResponseTypeDef(TypedDict):
    Licenses: List[LicenseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetServiceSettingsResponseTypeDef(TypedDict):
    S3BucketArn: str
    SnsTopicArn: str
    OrganizationConfiguration: OrganizationConfigurationTypeDef
    EnableCrossAccountsDiscovery: bool
    LicenseManagerResourceShareArn: str
    CrossRegionDiscoveryHomeRegion: str
    CrossRegionDiscoverySourceRegions: List[str]
    ServiceStatus: ServiceStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLicenseConversionTasksResponseTypeDef(TypedDict):
    LicenseConversionTasks: List[LicenseConversionTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateLicenseConversionTaskForResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    SourceLicenseContext: LicenseConversionContextUnionTypeDef
    DestinationLicenseContext: LicenseConversionContextUnionTypeDef

AndRuleStatementUnionTypeDef = Union[AndRuleStatementTypeDef, AndRuleStatementOutputTypeDef]
OrRuleStatementUnionTypeDef = Union[OrRuleStatementTypeDef, OrRuleStatementOutputTypeDef]

class ListLicenseConfigurationsForOrganizationResponseTypeDef(TypedDict):
    LicenseConfigurations: List[LicenseConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListLicenseConfigurationsResponseTypeDef(TypedDict):
    LicenseConfigurations: List[LicenseConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

ProductInformationUnionTypeDef = Union[ProductInformationTypeDef, ProductInformationOutputTypeDef]
CreateLicenseManagerReportGeneratorRequestTypeDef = TypedDict(
    "CreateLicenseManagerReportGeneratorRequestTypeDef",
    {
        "ReportGeneratorName": str,
        "Type": Sequence[ReportTypeType],
        "ReportContext": ReportContextUnionTypeDef,
        "ReportFrequency": ReportFrequencyTypeDef,
        "ClientToken": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateLicenseManagerReportGeneratorRequestTypeDef = TypedDict(
    "UpdateLicenseManagerReportGeneratorRequestTypeDef",
    {
        "LicenseManagerReportGeneratorArn": str,
        "ReportGeneratorName": str,
        "Type": Sequence[ReportTypeType],
        "ReportContext": ReportContextUnionTypeDef,
        "ReportFrequency": ReportFrequencyTypeDef,
        "ClientToken": str,
        "Description": NotRequired[str],
    },
)

class LicenseAssetRuleOutputTypeDef(TypedDict):
    RuleStatement: RuleStatementOutputTypeDef

class InstanceRuleStatementTypeDef(TypedDict):
    AndRuleStatement: NotRequired[AndRuleStatementUnionTypeDef]
    OrRuleStatement: NotRequired[OrRuleStatementUnionTypeDef]
    MatchingRuleStatement: NotRequired[MatchingRuleStatementUnionTypeDef]
    ScriptRuleStatement: NotRequired[ScriptRuleStatementTypeDef]

class LicenseConfigurationRuleStatementTypeDef(TypedDict):
    AndRuleStatement: NotRequired[AndRuleStatementUnionTypeDef]
    OrRuleStatement: NotRequired[OrRuleStatementUnionTypeDef]
    MatchingRuleStatement: NotRequired[MatchingRuleStatementUnionTypeDef]

class LicenseRuleStatementTypeDef(TypedDict):
    AndRuleStatement: NotRequired[AndRuleStatementUnionTypeDef]
    OrRuleStatement: NotRequired[OrRuleStatementUnionTypeDef]
    MatchingRuleStatement: NotRequired[MatchingRuleStatementUnionTypeDef]

class CreateLicenseConfigurationRequestTypeDef(TypedDict):
    Name: str
    LicenseCountingType: LicenseCountingTypeType
    Description: NotRequired[str]
    LicenseCount: NotRequired[int]
    LicenseCountHardLimit: NotRequired[bool]
    LicenseRules: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    DisassociateWhenNotFound: NotRequired[bool]
    ProductInformationList: NotRequired[Sequence[ProductInformationUnionTypeDef]]
    LicenseExpiry: NotRequired[int]

class UpdateLicenseConfigurationRequestTypeDef(TypedDict):
    LicenseConfigurationArn: str
    LicenseConfigurationStatus: NotRequired[LicenseConfigurationStatusType]
    LicenseRules: NotRequired[Sequence[str]]
    LicenseCount: NotRequired[int]
    LicenseCountHardLimit: NotRequired[bool]
    Name: NotRequired[str]
    Description: NotRequired[str]
    ProductInformationList: NotRequired[Sequence[ProductInformationUnionTypeDef]]
    DisassociateWhenNotFound: NotRequired[bool]
    LicenseExpiry: NotRequired[int]

class LicenseAssetRulesetTypeDef(TypedDict):
    Name: str
    Rules: List[LicenseAssetRuleOutputTypeDef]
    LicenseAssetRulesetArn: str
    Description: NotRequired[str]

InstanceRuleStatementUnionTypeDef = Union[
    InstanceRuleStatementTypeDef, InstanceRuleStatementOutputTypeDef
]
LicenseConfigurationRuleStatementUnionTypeDef = Union[
    LicenseConfigurationRuleStatementTypeDef, LicenseConfigurationRuleStatementOutputTypeDef
]
LicenseRuleStatementUnionTypeDef = Union[
    LicenseRuleStatementTypeDef, LicenseRuleStatementOutputTypeDef
]

class GetLicenseAssetRulesetResponseTypeDef(TypedDict):
    LicenseAssetRuleset: LicenseAssetRulesetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLicenseAssetRulesetsResponseTypeDef(TypedDict):
    LicenseAssetRulesets: List[LicenseAssetRulesetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class RuleStatementTypeDef(TypedDict):
    LicenseConfigurationRuleStatement: NotRequired[LicenseConfigurationRuleStatementUnionTypeDef]
    LicenseRuleStatement: NotRequired[LicenseRuleStatementUnionTypeDef]
    InstanceRuleStatement: NotRequired[InstanceRuleStatementUnionTypeDef]

RuleStatementUnionTypeDef = Union[RuleStatementTypeDef, RuleStatementOutputTypeDef]

class LicenseAssetRuleTypeDef(TypedDict):
    RuleStatement: RuleStatementUnionTypeDef

LicenseAssetRuleUnionTypeDef = Union[LicenseAssetRuleTypeDef, LicenseAssetRuleOutputTypeDef]

class CreateLicenseAssetRulesetRequestTypeDef(TypedDict):
    Name: str
    Rules: Sequence[LicenseAssetRuleUnionTypeDef]
    ClientToken: str
    Description: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class UpdateLicenseAssetRulesetRequestTypeDef(TypedDict):
    Rules: Sequence[LicenseAssetRuleUnionTypeDef]
    LicenseAssetRulesetArn: str
    ClientToken: str
    Name: NotRequired[str]
    Description: NotRequired[str]
