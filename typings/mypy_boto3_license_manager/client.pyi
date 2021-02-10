"""
Main interface for license-manager service client

Usage::

    ```python
    import boto3
    from mypy_boto3_license_manager import LicenseManagerClient

    client: LicenseManagerClient = boto3.client("license-manager")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_license_manager.paginator import (
    ListAssociationsForLicenseConfigurationPaginator,
    ListLicenseConfigurationsPaginator,
    ListLicenseSpecificationsForResourcePaginator,
    ListResourceInventoryPaginator,
    ListUsageForLicenseConfigurationPaginator,
)
from mypy_boto3_license_manager.type_defs import (
    AcceptGrantResponseTypeDef,
    CheckoutBorrowLicenseResponseTypeDef,
    CheckoutLicenseResponseTypeDef,
    ConsumptionConfigurationTypeDef,
    CreateGrantResponseTypeDef,
    CreateGrantVersionResponseTypeDef,
    CreateLicenseConfigurationResponseTypeDef,
    CreateLicenseResponseTypeDef,
    CreateLicenseVersionResponseTypeDef,
    CreateTokenResponseTypeDef,
    DatetimeRangeTypeDef,
    DeleteGrantResponseTypeDef,
    DeleteLicenseResponseTypeDef,
    EntitlementDataTypeDef,
    EntitlementTypeDef,
    ExtendLicenseConsumptionResponseTypeDef,
    FilterTypeDef,
    GetAccessTokenResponseTypeDef,
    GetGrantResponseTypeDef,
    GetLicenseConfigurationResponseTypeDef,
    GetLicenseResponseTypeDef,
    GetLicenseUsageResponseTypeDef,
    GetServiceSettingsResponseTypeDef,
    InventoryFilterTypeDef,
    IssuerTypeDef,
    LicenseSpecificationTypeDef,
    ListAssociationsForLicenseConfigurationResponseTypeDef,
    ListDistributedGrantsResponseTypeDef,
    ListFailuresForLicenseConfigurationOperationsResponseTypeDef,
    ListLicenseConfigurationsResponseTypeDef,
    ListLicenseSpecificationsForResourceResponseTypeDef,
    ListLicensesResponseTypeDef,
    ListLicenseVersionsResponseTypeDef,
    ListReceivedGrantsResponseTypeDef,
    ListReceivedLicensesResponseTypeDef,
    ListResourceInventoryResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTokensResponseTypeDef,
    ListUsageForLicenseConfigurationResponseTypeDef,
    MetadataTypeDef,
    OrganizationConfigurationTypeDef,
    ProductInformationTypeDef,
    RejectGrantResponseTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("LicenseManagerClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    AuthorizationException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    EntitlementNotAllowedException: Type[BotocoreClientError]
    FailedDependencyException: Type[BotocoreClientError]
    FilterLimitExceededException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidResourceStateException: Type[BotocoreClientError]
    LicenseUsageException: Type[BotocoreClientError]
    NoEntitlementsAllowedException: Type[BotocoreClientError]
    RateLimitExceededException: Type[BotocoreClientError]
    RedirectException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServerInternalException: Type[BotocoreClientError]
    UnsupportedDigitalSignatureMethodException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class LicenseManagerClient:
    """
    [LicenseManager.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_grant(self, GrantArn: str) -> AcceptGrantResponseTypeDef:
        """
        [Client.accept_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.accept_grant)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.can_paginate)
        """

    def check_in_license(
        self, LicenseConsumptionToken: str, Beneficiary: str = None
    ) -> Dict[str, Any]:
        """
        [Client.check_in_license documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.check_in_license)
        """

    def checkout_borrow_license(
        self,
        LicenseArn: str,
        Entitlements: List["EntitlementDataTypeDef"],
        DigitalSignatureMethod: Literal["JWT_PS384"],
        ClientToken: str,
        NodeId: str = None,
        CheckoutMetadata: List["MetadataTypeDef"] = None,
    ) -> CheckoutBorrowLicenseResponseTypeDef:
        """
        [Client.checkout_borrow_license documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.checkout_borrow_license)
        """

    def checkout_license(
        self,
        ProductSKU: str,
        CheckoutType: Literal["PROVISIONAL"],
        KeyFingerprint: str,
        Entitlements: List["EntitlementDataTypeDef"],
        ClientToken: str,
        Beneficiary: str = None,
        NodeId: str = None,
    ) -> CheckoutLicenseResponseTypeDef:
        """
        [Client.checkout_license documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.checkout_license)
        """

    def create_grant(
        self,
        ClientToken: str,
        GrantName: str,
        LicenseArn: str,
        Principals: List[str],
        HomeRegion: str,
        AllowedOperations: List[
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
    ) -> CreateGrantResponseTypeDef:
        """
        [Client.create_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.create_grant)
        """

    def create_grant_version(
        self,
        ClientToken: str,
        GrantArn: str,
        GrantName: str = None,
        AllowedOperations: List[
            Literal[
                "CreateGrant",
                "CheckoutLicense",
                "CheckoutBorrowLicense",
                "CheckInLicense",
                "ExtendConsumptionLicense",
                "ListPurchasedLicenses",
                "CreateToken",
            ]
        ] = None,
        Status: Literal[
            "PENDING_WORKFLOW",
            "PENDING_ACCEPT",
            "REJECTED",
            "ACTIVE",
            "FAILED_WORKFLOW",
            "DELETED",
            "PENDING_DELETE",
            "DISABLED",
        ] = None,
        SourceVersion: str = None,
    ) -> CreateGrantVersionResponseTypeDef:
        """
        [Client.create_grant_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.create_grant_version)
        """

    def create_license(
        self,
        LicenseName: str,
        ProductName: str,
        ProductSKU: str,
        Issuer: IssuerTypeDef,
        HomeRegion: str,
        Validity: "DatetimeRangeTypeDef",
        Entitlements: List["EntitlementTypeDef"],
        Beneficiary: str,
        ConsumptionConfiguration: "ConsumptionConfigurationTypeDef",
        ClientToken: str,
        LicenseMetadata: List["MetadataTypeDef"] = None,
    ) -> CreateLicenseResponseTypeDef:
        """
        [Client.create_license documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.create_license)
        """

    def create_license_configuration(
        self,
        Name: str,
        LicenseCountingType: Literal["vCPU", "Instance", "Core", "Socket"],
        Description: str = None,
        LicenseCount: int = None,
        LicenseCountHardLimit: bool = None,
        LicenseRules: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        DisassociateWhenNotFound: bool = None,
        ProductInformationList: List["ProductInformationTypeDef"] = None,
    ) -> CreateLicenseConfigurationResponseTypeDef:
        """
        [Client.create_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.create_license_configuration)
        """

    def create_license_version(
        self,
        LicenseArn: str,
        LicenseName: str,
        ProductName: str,
        Issuer: IssuerTypeDef,
        HomeRegion: str,
        Validity: "DatetimeRangeTypeDef",
        Entitlements: List["EntitlementTypeDef"],
        ConsumptionConfiguration: "ConsumptionConfigurationTypeDef",
        Status: Literal[
            "AVAILABLE",
            "PENDING_AVAILABLE",
            "DEACTIVATED",
            "SUSPENDED",
            "EXPIRED",
            "PENDING_DELETE",
            "DELETED",
        ],
        ClientToken: str,
        LicenseMetadata: List["MetadataTypeDef"] = None,
        SourceVersion: str = None,
    ) -> CreateLicenseVersionResponseTypeDef:
        """
        [Client.create_license_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.create_license_version)
        """

    def create_token(
        self,
        LicenseArn: str,
        ClientToken: str,
        RoleArns: List[str] = None,
        ExpirationInDays: int = None,
        TokenProperties: List[str] = None,
    ) -> CreateTokenResponseTypeDef:
        """
        [Client.create_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.create_token)
        """

    def delete_grant(self, GrantArn: str, Version: str) -> DeleteGrantResponseTypeDef:
        """
        [Client.delete_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.delete_grant)
        """

    def delete_license(self, LicenseArn: str, SourceVersion: str) -> DeleteLicenseResponseTypeDef:
        """
        [Client.delete_license documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.delete_license)
        """

    def delete_license_configuration(self, LicenseConfigurationArn: str) -> Dict[str, Any]:
        """
        [Client.delete_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.delete_license_configuration)
        """

    def delete_token(self, TokenId: str) -> Dict[str, Any]:
        """
        [Client.delete_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.delete_token)
        """

    def extend_license_consumption(
        self, LicenseConsumptionToken: str, DryRun: bool = None
    ) -> ExtendLicenseConsumptionResponseTypeDef:
        """
        [Client.extend_license_consumption documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.extend_license_consumption)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.generate_presigned_url)
        """

    def get_access_token(
        self, Token: str, TokenProperties: List[str] = None
    ) -> GetAccessTokenResponseTypeDef:
        """
        [Client.get_access_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.get_access_token)
        """

    def get_grant(self, GrantArn: str, Version: str = None) -> GetGrantResponseTypeDef:
        """
        [Client.get_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.get_grant)
        """

    def get_license(self, LicenseArn: str, Version: str = None) -> GetLicenseResponseTypeDef:
        """
        [Client.get_license documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.get_license)
        """

    def get_license_configuration(
        self, LicenseConfigurationArn: str
    ) -> GetLicenseConfigurationResponseTypeDef:
        """
        [Client.get_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.get_license_configuration)
        """

    def get_license_usage(self, LicenseArn: str) -> GetLicenseUsageResponseTypeDef:
        """
        [Client.get_license_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.get_license_usage)
        """

    def get_service_settings(self) -> GetServiceSettingsResponseTypeDef:
        """
        [Client.get_service_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.get_service_settings)
        """

    def list_associations_for_license_configuration(
        self, LicenseConfigurationArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAssociationsForLicenseConfigurationResponseTypeDef:
        """
        [Client.list_associations_for_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.list_associations_for_license_configuration)
        """

    def list_distributed_grants(
        self,
        GrantArns: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListDistributedGrantsResponseTypeDef:
        """
        [Client.list_distributed_grants documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.list_distributed_grants)
        """

    def list_failures_for_license_configuration_operations(
        self, LicenseConfigurationArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListFailuresForLicenseConfigurationOperationsResponseTypeDef:
        """
        [Client.list_failures_for_license_configuration_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.list_failures_for_license_configuration_operations)
        """

    def list_license_configurations(
        self,
        LicenseConfigurationArns: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
    ) -> ListLicenseConfigurationsResponseTypeDef:
        """
        [Client.list_license_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.list_license_configurations)
        """

    def list_license_specifications_for_resource(
        self, ResourceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListLicenseSpecificationsForResourceResponseTypeDef:
        """
        [Client.list_license_specifications_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.list_license_specifications_for_resource)
        """

    def list_license_versions(
        self, LicenseArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListLicenseVersionsResponseTypeDef:
        """
        [Client.list_license_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.list_license_versions)
        """

    def list_licenses(
        self,
        LicenseArns: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListLicensesResponseTypeDef:
        """
        [Client.list_licenses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.list_licenses)
        """

    def list_received_grants(
        self,
        GrantArns: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListReceivedGrantsResponseTypeDef:
        """
        [Client.list_received_grants documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.list_received_grants)
        """

    def list_received_licenses(
        self,
        LicenseArns: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListReceivedLicensesResponseTypeDef:
        """
        [Client.list_received_licenses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.list_received_licenses)
        """

    def list_resource_inventory(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[InventoryFilterTypeDef] = None,
    ) -> ListResourceInventoryResponseTypeDef:
        """
        [Client.list_resource_inventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.list_resource_inventory)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.list_tags_for_resource)
        """

    def list_tokens(
        self,
        TokenIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListTokensResponseTypeDef:
        """
        [Client.list_tokens documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.list_tokens)
        """

    def list_usage_for_license_configuration(
        self,
        LicenseConfigurationArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
    ) -> ListUsageForLicenseConfigurationResponseTypeDef:
        """
        [Client.list_usage_for_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.list_usage_for_license_configuration)
        """

    def reject_grant(self, GrantArn: str) -> RejectGrantResponseTypeDef:
        """
        [Client.reject_grant documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.reject_grant)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.untag_resource)
        """

    def update_license_configuration(
        self,
        LicenseConfigurationArn: str,
        LicenseConfigurationStatus: Literal["AVAILABLE", "DISABLED"] = None,
        LicenseRules: List[str] = None,
        LicenseCount: int = None,
        LicenseCountHardLimit: bool = None,
        Name: str = None,
        Description: str = None,
        ProductInformationList: List["ProductInformationTypeDef"] = None,
        DisassociateWhenNotFound: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.update_license_configuration)
        """

    def update_license_specifications_for_resource(
        self,
        ResourceArn: str,
        AddLicenseSpecifications: List["LicenseSpecificationTypeDef"] = None,
        RemoveLicenseSpecifications: List["LicenseSpecificationTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_license_specifications_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.update_license_specifications_for_resource)
        """

    def update_service_settings(
        self,
        S3BucketArn: str = None,
        SnsTopicArn: str = None,
        OrganizationConfiguration: "OrganizationConfigurationTypeDef" = None,
        EnableCrossAccountsDiscovery: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_service_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Client.update_service_settings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_associations_for_license_configuration"]
    ) -> ListAssociationsForLicenseConfigurationPaginator:
        """
        [Paginator.ListAssociationsForLicenseConfiguration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Paginator.ListAssociationsForLicenseConfiguration)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_license_configurations"]
    ) -> ListLicenseConfigurationsPaginator:
        """
        [Paginator.ListLicenseConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseConfigurations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_license_specifications_for_resource"]
    ) -> ListLicenseSpecificationsForResourcePaginator:
        """
        [Paginator.ListLicenseSpecificationsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseSpecificationsForResource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_inventory"]
    ) -> ListResourceInventoryPaginator:
        """
        [Paginator.ListResourceInventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Paginator.ListResourceInventory)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_usage_for_license_configuration"]
    ) -> ListUsageForLicenseConfigurationPaginator:
        """
        [Paginator.ListUsageForLicenseConfiguration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/license-manager.html#LicenseManager.Paginator.ListUsageForLicenseConfiguration)
        """
