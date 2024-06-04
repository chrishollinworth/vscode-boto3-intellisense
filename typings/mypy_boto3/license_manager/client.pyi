"""
Type annotations for license-manager service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_license_manager import LicenseManagerClient

    client: LicenseManagerClient = boto3.client("license-manager")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AllowedOperationType,
    CheckoutTypeType,
    GrantStatusType,
    LicenseConfigurationStatusType,
    LicenseCountingTypeType,
    LicenseStatusType,
    ReportTypeType,
)
from .paginator import (
    ListAssociationsForLicenseConfigurationPaginator,
    ListLicenseConfigurationsPaginator,
    ListLicenseSpecificationsForResourcePaginator,
    ListResourceInventoryPaginator,
    ListUsageForLicenseConfigurationPaginator,
)
from .type_defs import (
    AcceptGrantResponseTypeDef,
    CheckoutBorrowLicenseResponseTypeDef,
    CheckoutLicenseResponseTypeDef,
    ConsumptionConfigurationTypeDef,
    CreateGrantResponseTypeDef,
    CreateGrantVersionResponseTypeDef,
    CreateLicenseConfigurationResponseTypeDef,
    CreateLicenseConversionTaskForResourceResponseTypeDef,
    CreateLicenseManagerReportGeneratorResponseTypeDef,
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
    GetLicenseConversionTaskResponseTypeDef,
    GetLicenseManagerReportGeneratorResponseTypeDef,
    GetLicenseResponseTypeDef,
    GetLicenseUsageResponseTypeDef,
    GetServiceSettingsResponseTypeDef,
    InventoryFilterTypeDef,
    IssuerTypeDef,
    LicenseConversionContextTypeDef,
    LicenseSpecificationTypeDef,
    ListAssociationsForLicenseConfigurationResponseTypeDef,
    ListDistributedGrantsResponseTypeDef,
    ListFailuresForLicenseConfigurationOperationsResponseTypeDef,
    ListLicenseConfigurationsResponseTypeDef,
    ListLicenseConversionTasksResponseTypeDef,
    ListLicenseManagerReportGeneratorsResponseTypeDef,
    ListLicenseSpecificationsForResourceResponseTypeDef,
    ListLicensesResponseTypeDef,
    ListLicenseVersionsResponseTypeDef,
    ListReceivedGrantsForOrganizationResponseTypeDef,
    ListReceivedGrantsResponseTypeDef,
    ListReceivedLicensesForOrganizationResponseTypeDef,
    ListReceivedLicensesResponseTypeDef,
    ListResourceInventoryResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTokensResponseTypeDef,
    ListUsageForLicenseConfigurationResponseTypeDef,
    MetadataTypeDef,
    OptionsTypeDef,
    OrganizationConfigurationTypeDef,
    ProductInformationTypeDef,
    RejectGrantResponseTypeDef,
    ReportContextTypeDef,
    ReportFrequencyTypeDef,
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

class LicenseManagerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LicenseManagerClient exceptions.
        """

    def accept_grant(self, *, GrantArn: str) -> AcceptGrantResponseTypeDef:
        """
        Accepts the specified grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.accept_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#accept_grant)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#can_paginate)
        """

    def check_in_license(
        self, *, LicenseConsumptionToken: str, Beneficiary: str = None
    ) -> Dict[str, Any]:
        """
        Checks in the specified license.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.check_in_license)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#check_in_license)
        """

    def checkout_borrow_license(
        self,
        *,
        LicenseArn: str,
        Entitlements: List["EntitlementDataTypeDef"],
        DigitalSignatureMethod: Literal["JWT_PS384"],
        ClientToken: str,
        NodeId: str = None,
        CheckoutMetadata: List["MetadataTypeDef"] = None
    ) -> CheckoutBorrowLicenseResponseTypeDef:
        """
        Checks out the specified license for offline use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.checkout_borrow_license)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#checkout_borrow_license)
        """

    def checkout_license(
        self,
        *,
        ProductSKU: str,
        CheckoutType: CheckoutTypeType,
        KeyFingerprint: str,
        Entitlements: List["EntitlementDataTypeDef"],
        ClientToken: str,
        Beneficiary: str = None,
        NodeId: str = None
    ) -> CheckoutLicenseResponseTypeDef:
        """
        Checks out the specified license.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.checkout_license)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#checkout_license)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#close)
        """

    def create_grant(
        self,
        *,
        ClientToken: str,
        GrantName: str,
        LicenseArn: str,
        Principals: List[str],
        HomeRegion: str,
        AllowedOperations: List[AllowedOperationType]
    ) -> CreateGrantResponseTypeDef:
        """
        Creates a grant for the specified license.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.create_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#create_grant)
        """

    def create_grant_version(
        self,
        *,
        ClientToken: str,
        GrantArn: str,
        GrantName: str = None,
        AllowedOperations: List[AllowedOperationType] = None,
        Status: GrantStatusType = None,
        StatusReason: str = None,
        SourceVersion: str = None,
        Options: "OptionsTypeDef" = None
    ) -> CreateGrantVersionResponseTypeDef:
        """
        Creates a new version of the specified grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.create_grant_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#create_grant_version)
        """

    def create_license(
        self,
        *,
        LicenseName: str,
        ProductName: str,
        ProductSKU: str,
        Issuer: "IssuerTypeDef",
        HomeRegion: str,
        Validity: "DatetimeRangeTypeDef",
        Entitlements: List["EntitlementTypeDef"],
        Beneficiary: str,
        ConsumptionConfiguration: "ConsumptionConfigurationTypeDef",
        ClientToken: str,
        LicenseMetadata: List["MetadataTypeDef"] = None
    ) -> CreateLicenseResponseTypeDef:
        """
        Creates a license.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.create_license)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#create_license)
        """

    def create_license_configuration(
        self,
        *,
        Name: str,
        LicenseCountingType: LicenseCountingTypeType,
        Description: str = None,
        LicenseCount: int = None,
        LicenseCountHardLimit: bool = None,
        LicenseRules: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        DisassociateWhenNotFound: bool = None,
        ProductInformationList: List["ProductInformationTypeDef"] = None
    ) -> CreateLicenseConfigurationResponseTypeDef:
        """
        Creates a license configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.create_license_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#create_license_configuration)
        """

    def create_license_conversion_task_for_resource(
        self,
        *,
        ResourceArn: str,
        SourceLicenseContext: "LicenseConversionContextTypeDef",
        DestinationLicenseContext: "LicenseConversionContextTypeDef"
    ) -> CreateLicenseConversionTaskForResourceResponseTypeDef:
        """
        Creates a new license conversion task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.create_license_conversion_task_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#create_license_conversion_task_for_resource)
        """

    def create_license_manager_report_generator(
        self,
        *,
        ReportGeneratorName: str,
        Type: List[ReportTypeType],
        ReportContext: "ReportContextTypeDef",
        ReportFrequency: "ReportFrequencyTypeDef",
        ClientToken: str,
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateLicenseManagerReportGeneratorResponseTypeDef:
        """
        Creates a report generator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.create_license_manager_report_generator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#create_license_manager_report_generator)
        """

    def create_license_version(
        self,
        *,
        LicenseArn: str,
        LicenseName: str,
        ProductName: str,
        Issuer: "IssuerTypeDef",
        HomeRegion: str,
        Validity: "DatetimeRangeTypeDef",
        Entitlements: List["EntitlementTypeDef"],
        ConsumptionConfiguration: "ConsumptionConfigurationTypeDef",
        Status: LicenseStatusType,
        ClientToken: str,
        LicenseMetadata: List["MetadataTypeDef"] = None,
        SourceVersion: str = None
    ) -> CreateLicenseVersionResponseTypeDef:
        """
        Creates a new version of the specified license.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.create_license_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#create_license_version)
        """

    def create_token(
        self,
        *,
        LicenseArn: str,
        ClientToken: str,
        RoleArns: List[str] = None,
        ExpirationInDays: int = None,
        TokenProperties: List[str] = None
    ) -> CreateTokenResponseTypeDef:
        """
        Creates a long-lived token.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.create_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#create_token)
        """

    def delete_grant(
        self, *, GrantArn: str, Version: str, StatusReason: str = None
    ) -> DeleteGrantResponseTypeDef:
        """
        Deletes the specified grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.delete_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#delete_grant)
        """

    def delete_license(
        self, *, LicenseArn: str, SourceVersion: str
    ) -> DeleteLicenseResponseTypeDef:
        """
        Deletes the specified license.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.delete_license)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#delete_license)
        """

    def delete_license_configuration(self, *, LicenseConfigurationArn: str) -> Dict[str, Any]:
        """
        Deletes the specified license configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.delete_license_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#delete_license_configuration)
        """

    def delete_license_manager_report_generator(
        self, *, LicenseManagerReportGeneratorArn: str
    ) -> Dict[str, Any]:
        """
        Deletes the specified report generator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.delete_license_manager_report_generator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#delete_license_manager_report_generator)
        """

    def delete_token(self, *, TokenId: str) -> Dict[str, Any]:
        """
        Deletes the specified token.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.delete_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#delete_token)
        """

    def extend_license_consumption(
        self, *, LicenseConsumptionToken: str, DryRun: bool = None
    ) -> ExtendLicenseConsumptionResponseTypeDef:
        """
        Extends the expiration date for license consumption.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.extend_license_consumption)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#extend_license_consumption)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#generate_presigned_url)
        """

    def get_access_token(
        self, *, Token: str, TokenProperties: List[str] = None
    ) -> GetAccessTokenResponseTypeDef:
        """
        Gets a temporary access token to use with AssumeRoleWithWebIdentity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.get_access_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#get_access_token)
        """

    def get_grant(self, *, GrantArn: str, Version: str = None) -> GetGrantResponseTypeDef:
        """
        Gets detailed information about the specified grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.get_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#get_grant)
        """

    def get_license(self, *, LicenseArn: str, Version: str = None) -> GetLicenseResponseTypeDef:
        """
        Gets detailed information about the specified license.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.get_license)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#get_license)
        """

    def get_license_configuration(
        self, *, LicenseConfigurationArn: str
    ) -> GetLicenseConfigurationResponseTypeDef:
        """
        Gets detailed information about the specified license configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.get_license_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#get_license_configuration)
        """

    def get_license_conversion_task(
        self, *, LicenseConversionTaskId: str
    ) -> GetLicenseConversionTaskResponseTypeDef:
        """
        Gets information about the specified license type conversion task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.get_license_conversion_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#get_license_conversion_task)
        """

    def get_license_manager_report_generator(
        self, *, LicenseManagerReportGeneratorArn: str
    ) -> GetLicenseManagerReportGeneratorResponseTypeDef:
        """
        Gets information about the specified report generator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.get_license_manager_report_generator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#get_license_manager_report_generator)
        """

    def get_license_usage(self, *, LicenseArn: str) -> GetLicenseUsageResponseTypeDef:
        """
        Gets detailed information about the usage of the specified license.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.get_license_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#get_license_usage)
        """

    def get_service_settings(self) -> GetServiceSettingsResponseTypeDef:
        """
        Gets the License Manager settings for the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.get_service_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#get_service_settings)
        """

    def list_associations_for_license_configuration(
        self, *, LicenseConfigurationArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAssociationsForLicenseConfigurationResponseTypeDef:
        """
        Lists the resource associations for the specified license configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.list_associations_for_license_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list_associations_for_license_configuration)
        """

    def list_distributed_grants(
        self,
        *,
        GrantArns: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListDistributedGrantsResponseTypeDef:
        """
        Lists the grants distributed for the specified license.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.list_distributed_grants)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list_distributed_grants)
        """

    def list_failures_for_license_configuration_operations(
        self, *, LicenseConfigurationArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListFailuresForLicenseConfigurationOperationsResponseTypeDef:
        """
        Lists the license configuration operations that failed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.list_failures_for_license_configuration_operations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list_failures_for_license_configuration_operations)
        """

    def list_license_configurations(
        self,
        *,
        LicenseConfigurationArns: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["FilterTypeDef"] = None
    ) -> ListLicenseConfigurationsResponseTypeDef:
        """
        Lists the license configurations for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.list_license_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list_license_configurations)
        """

    def list_license_conversion_tasks(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None
    ) -> ListLicenseConversionTasksResponseTypeDef:
        """
        Lists the license type conversion tasks for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.list_license_conversion_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list_license_conversion_tasks)
        """

    def list_license_manager_report_generators(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListLicenseManagerReportGeneratorsResponseTypeDef:
        """
        Lists the report generators for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.list_license_manager_report_generators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list_license_manager_report_generators)
        """

    def list_license_specifications_for_resource(
        self, *, ResourceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListLicenseSpecificationsForResourceResponseTypeDef:
        """
        Describes the license configurations for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.list_license_specifications_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list_license_specifications_for_resource)
        """

    def list_license_versions(
        self, *, LicenseArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListLicenseVersionsResponseTypeDef:
        """
        Lists all versions of the specified license.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.list_license_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list_license_versions)
        """

    def list_licenses(
        self,
        *,
        LicenseArns: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListLicensesResponseTypeDef:
        """
        Lists the licenses for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.list_licenses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list_licenses)
        """

    def list_received_grants(
        self,
        *,
        GrantArns: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListReceivedGrantsResponseTypeDef:
        """
        Lists grants that are received.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.list_received_grants)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list_received_grants)
        """

    def list_received_grants_for_organization(
        self,
        *,
        LicenseArn: str,
        Filters: List["FilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListReceivedGrantsForOrganizationResponseTypeDef:
        """
        Lists the grants received for all accounts in the organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.list_received_grants_for_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list_received_grants_for_organization)
        """

    def list_received_licenses(
        self,
        *,
        LicenseArns: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListReceivedLicensesResponseTypeDef:
        """
        Lists received licenses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.list_received_licenses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list_received_licenses)
        """

    def list_received_licenses_for_organization(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListReceivedLicensesForOrganizationResponseTypeDef:
        """
        Lists the licenses received for all accounts in the organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.list_received_licenses_for_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list_received_licenses_for_organization)
        """

    def list_resource_inventory(
        self,
        *,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["InventoryFilterTypeDef"] = None
    ) -> ListResourceInventoryResponseTypeDef:
        """
        Lists resources managed using Systems Manager inventory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.list_resource_inventory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list_resource_inventory)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified license configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list_tags_for_resource)
        """

    def list_tokens(
        self,
        *,
        TokenIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListTokensResponseTypeDef:
        """
        Lists your tokens.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.list_tokens)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list_tokens)
        """

    def list_usage_for_license_configuration(
        self,
        *,
        LicenseConfigurationArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["FilterTypeDef"] = None
    ) -> ListUsageForLicenseConfigurationResponseTypeDef:
        """
        Lists all license usage records for a license configuration, displaying license
        consumption details by resource at a selected point in time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.list_usage_for_license_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list_usage_for_license_configuration)
        """

    def reject_grant(self, *, GrantArn: str) -> RejectGrantResponseTypeDef:
        """
        Rejects the specified grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.reject_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#reject_grant)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified license configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified license configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#untag_resource)
        """

    def update_license_configuration(
        self,
        *,
        LicenseConfigurationArn: str,
        LicenseConfigurationStatus: LicenseConfigurationStatusType = None,
        LicenseRules: List[str] = None,
        LicenseCount: int = None,
        LicenseCountHardLimit: bool = None,
        Name: str = None,
        Description: str = None,
        ProductInformationList: List["ProductInformationTypeDef"] = None,
        DisassociateWhenNotFound: bool = None
    ) -> Dict[str, Any]:
        """
        Modifies the attributes of an existing license configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.update_license_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#update_license_configuration)
        """

    def update_license_manager_report_generator(
        self,
        *,
        LicenseManagerReportGeneratorArn: str,
        ReportGeneratorName: str,
        Type: List[ReportTypeType],
        ReportContext: "ReportContextTypeDef",
        ReportFrequency: "ReportFrequencyTypeDef",
        ClientToken: str,
        Description: str = None
    ) -> Dict[str, Any]:
        """
        Updates a report generator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.update_license_manager_report_generator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#update_license_manager_report_generator)
        """

    def update_license_specifications_for_resource(
        self,
        *,
        ResourceArn: str,
        AddLicenseSpecifications: List["LicenseSpecificationTypeDef"] = None,
        RemoveLicenseSpecifications: List["LicenseSpecificationTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Adds or removes the specified license configurations for the specified Amazon
        Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.update_license_specifications_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#update_license_specifications_for_resource)
        """

    def update_service_settings(
        self,
        *,
        S3BucketArn: str = None,
        SnsTopicArn: str = None,
        OrganizationConfiguration: "OrganizationConfigurationTypeDef" = None,
        EnableCrossAccountsDiscovery: bool = None
    ) -> Dict[str, Any]:
        """
        Updates License Manager settings for the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Client.update_service_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#update_service_settings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_associations_for_license_configuration"]
    ) -> ListAssociationsForLicenseConfigurationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Paginator.ListAssociationsForLicenseConfiguration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/paginators.html#listassociationsforlicenseconfigurationpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_license_configurations"]
    ) -> ListLicenseConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseConfigurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/paginators.html#listlicenseconfigurationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_license_specifications_for_resource"]
    ) -> ListLicenseSpecificationsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseSpecificationsForResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/paginators.html#listlicensespecificationsforresourcepaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_inventory"]
    ) -> ListResourceInventoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Paginator.ListResourceInventory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/paginators.html#listresourceinventorypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_usage_for_license_configuration"]
    ) -> ListUsageForLicenseConfigurationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/license-manager.html#LicenseManager.Paginator.ListUsageForLicenseConfiguration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/paginators.html#listusageforlicenseconfigurationpaginator)
        """
