"""
Type annotations for license-manager service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_license_manager.client import LicenseManagerClient

    session = Session()
    client: LicenseManagerClient = session.client("license-manager")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAssociationsForLicenseConfigurationPaginator,
    ListLicenseConfigurationsPaginator,
    ListLicenseSpecificationsForResourcePaginator,
    ListResourceInventoryPaginator,
    ListUsageForLicenseConfigurationPaginator,
)
from .type_defs import (
    AcceptGrantRequestTypeDef,
    AcceptGrantResponseTypeDef,
    CheckInLicenseRequestTypeDef,
    CheckoutBorrowLicenseRequestTypeDef,
    CheckoutBorrowLicenseResponseTypeDef,
    CheckoutLicenseRequestTypeDef,
    CheckoutLicenseResponseTypeDef,
    CreateGrantRequestTypeDef,
    CreateGrantResponseTypeDef,
    CreateGrantVersionRequestTypeDef,
    CreateGrantVersionResponseTypeDef,
    CreateLicenseConfigurationRequestTypeDef,
    CreateLicenseConfigurationResponseTypeDef,
    CreateLicenseConversionTaskForResourceRequestTypeDef,
    CreateLicenseConversionTaskForResourceResponseTypeDef,
    CreateLicenseManagerReportGeneratorRequestTypeDef,
    CreateLicenseManagerReportGeneratorResponseTypeDef,
    CreateLicenseRequestTypeDef,
    CreateLicenseResponseTypeDef,
    CreateLicenseVersionRequestTypeDef,
    CreateLicenseVersionResponseTypeDef,
    CreateTokenRequestTypeDef,
    CreateTokenResponseTypeDef,
    DeleteGrantRequestTypeDef,
    DeleteGrantResponseTypeDef,
    DeleteLicenseConfigurationRequestTypeDef,
    DeleteLicenseManagerReportGeneratorRequestTypeDef,
    DeleteLicenseRequestTypeDef,
    DeleteLicenseResponseTypeDef,
    DeleteTokenRequestTypeDef,
    ExtendLicenseConsumptionRequestTypeDef,
    ExtendLicenseConsumptionResponseTypeDef,
    GetAccessTokenRequestTypeDef,
    GetAccessTokenResponseTypeDef,
    GetGrantRequestTypeDef,
    GetGrantResponseTypeDef,
    GetLicenseConfigurationRequestTypeDef,
    GetLicenseConfigurationResponseTypeDef,
    GetLicenseConversionTaskRequestTypeDef,
    GetLicenseConversionTaskResponseTypeDef,
    GetLicenseManagerReportGeneratorRequestTypeDef,
    GetLicenseManagerReportGeneratorResponseTypeDef,
    GetLicenseRequestTypeDef,
    GetLicenseResponseTypeDef,
    GetLicenseUsageRequestTypeDef,
    GetLicenseUsageResponseTypeDef,
    GetServiceSettingsResponseTypeDef,
    ListAssociationsForLicenseConfigurationRequestTypeDef,
    ListAssociationsForLicenseConfigurationResponseTypeDef,
    ListDistributedGrantsRequestTypeDef,
    ListDistributedGrantsResponseTypeDef,
    ListFailuresForLicenseConfigurationOperationsRequestTypeDef,
    ListFailuresForLicenseConfigurationOperationsResponseTypeDef,
    ListLicenseConfigurationsRequestTypeDef,
    ListLicenseConfigurationsResponseTypeDef,
    ListLicenseConversionTasksRequestTypeDef,
    ListLicenseConversionTasksResponseTypeDef,
    ListLicenseManagerReportGeneratorsRequestTypeDef,
    ListLicenseManagerReportGeneratorsResponseTypeDef,
    ListLicenseSpecificationsForResourceRequestTypeDef,
    ListLicenseSpecificationsForResourceResponseTypeDef,
    ListLicensesRequestTypeDef,
    ListLicensesResponseTypeDef,
    ListLicenseVersionsRequestTypeDef,
    ListLicenseVersionsResponseTypeDef,
    ListReceivedGrantsForOrganizationRequestTypeDef,
    ListReceivedGrantsForOrganizationResponseTypeDef,
    ListReceivedGrantsRequestTypeDef,
    ListReceivedGrantsResponseTypeDef,
    ListReceivedLicensesForOrganizationRequestTypeDef,
    ListReceivedLicensesForOrganizationResponseTypeDef,
    ListReceivedLicensesRequestTypeDef,
    ListReceivedLicensesResponseTypeDef,
    ListResourceInventoryRequestTypeDef,
    ListResourceInventoryResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTokensRequestTypeDef,
    ListTokensResponseTypeDef,
    ListUsageForLicenseConfigurationRequestTypeDef,
    ListUsageForLicenseConfigurationResponseTypeDef,
    RejectGrantRequestTypeDef,
    RejectGrantResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateLicenseConfigurationRequestTypeDef,
    UpdateLicenseManagerReportGeneratorRequestTypeDef,
    UpdateLicenseSpecificationsForResourceRequestTypeDef,
    UpdateServiceSettingsRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("LicenseManagerClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LicenseManagerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager.html#LicenseManager.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#generate_presigned_url)
        """

    def accept_grant(
        self, **kwargs: Unpack[AcceptGrantRequestTypeDef]
    ) -> AcceptGrantResponseTypeDef:
        """
        Accepts the specified grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/accept_grant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#accept_grant)
        """

    def check_in_license(self, **kwargs: Unpack[CheckInLicenseRequestTypeDef]) -> Dict[str, Any]:
        """
        Checks in the specified license.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/check_in_license.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#check_in_license)
        """

    def checkout_borrow_license(
        self, **kwargs: Unpack[CheckoutBorrowLicenseRequestTypeDef]
    ) -> CheckoutBorrowLicenseResponseTypeDef:
        """
        Checks out the specified license for offline use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/checkout_borrow_license.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#checkout_borrow_license)
        """

    def checkout_license(
        self, **kwargs: Unpack[CheckoutLicenseRequestTypeDef]
    ) -> CheckoutLicenseResponseTypeDef:
        """
        Checks out the specified license.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/checkout_license.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#checkout_license)
        """

    def create_grant(
        self, **kwargs: Unpack[CreateGrantRequestTypeDef]
    ) -> CreateGrantResponseTypeDef:
        """
        Creates a grant for the specified license.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/create_grant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#create_grant)
        """

    def create_grant_version(
        self, **kwargs: Unpack[CreateGrantVersionRequestTypeDef]
    ) -> CreateGrantVersionResponseTypeDef:
        """
        Creates a new version of the specified grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/create_grant_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#create_grant_version)
        """

    def create_license(
        self, **kwargs: Unpack[CreateLicenseRequestTypeDef]
    ) -> CreateLicenseResponseTypeDef:
        """
        Creates a license.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/create_license.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#create_license)
        """

    def create_license_configuration(
        self, **kwargs: Unpack[CreateLicenseConfigurationRequestTypeDef]
    ) -> CreateLicenseConfigurationResponseTypeDef:
        """
        Creates a license configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/create_license_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#create_license_configuration)
        """

    def create_license_conversion_task_for_resource(
        self, **kwargs: Unpack[CreateLicenseConversionTaskForResourceRequestTypeDef]
    ) -> CreateLicenseConversionTaskForResourceResponseTypeDef:
        """
        Creates a new license conversion task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/create_license_conversion_task_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#create_license_conversion_task_for_resource)
        """

    def create_license_manager_report_generator(
        self, **kwargs: Unpack[CreateLicenseManagerReportGeneratorRequestTypeDef]
    ) -> CreateLicenseManagerReportGeneratorResponseTypeDef:
        """
        Creates a report generator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/create_license_manager_report_generator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#create_license_manager_report_generator)
        """

    def create_license_version(
        self, **kwargs: Unpack[CreateLicenseVersionRequestTypeDef]
    ) -> CreateLicenseVersionResponseTypeDef:
        """
        Creates a new version of the specified license.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/create_license_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#create_license_version)
        """

    def create_token(
        self, **kwargs: Unpack[CreateTokenRequestTypeDef]
    ) -> CreateTokenResponseTypeDef:
        """
        Creates a long-lived token.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/create_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#create_token)
        """

    def delete_grant(
        self, **kwargs: Unpack[DeleteGrantRequestTypeDef]
    ) -> DeleteGrantResponseTypeDef:
        """
        Deletes the specified grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/delete_grant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#delete_grant)
        """

    def delete_license(
        self, **kwargs: Unpack[DeleteLicenseRequestTypeDef]
    ) -> DeleteLicenseResponseTypeDef:
        """
        Deletes the specified license.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/delete_license.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#delete_license)
        """

    def delete_license_configuration(
        self, **kwargs: Unpack[DeleteLicenseConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified license configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/delete_license_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#delete_license_configuration)
        """

    def delete_license_manager_report_generator(
        self, **kwargs: Unpack[DeleteLicenseManagerReportGeneratorRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified report generator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/delete_license_manager_report_generator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#delete_license_manager_report_generator)
        """

    def delete_token(self, **kwargs: Unpack[DeleteTokenRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified token.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/delete_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#delete_token)
        """

    def extend_license_consumption(
        self, **kwargs: Unpack[ExtendLicenseConsumptionRequestTypeDef]
    ) -> ExtendLicenseConsumptionResponseTypeDef:
        """
        Extends the expiration date for license consumption.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/extend_license_consumption.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#extend_license_consumption)
        """

    def get_access_token(
        self, **kwargs: Unpack[GetAccessTokenRequestTypeDef]
    ) -> GetAccessTokenResponseTypeDef:
        """
        Gets a temporary access token to use with AssumeRoleWithWebIdentity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/get_access_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#get_access_token)
        """

    def get_grant(self, **kwargs: Unpack[GetGrantRequestTypeDef]) -> GetGrantResponseTypeDef:
        """
        Gets detailed information about the specified grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/get_grant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#get_grant)
        """

    def get_license(self, **kwargs: Unpack[GetLicenseRequestTypeDef]) -> GetLicenseResponseTypeDef:
        """
        Gets detailed information about the specified license.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/get_license.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#get_license)
        """

    def get_license_configuration(
        self, **kwargs: Unpack[GetLicenseConfigurationRequestTypeDef]
    ) -> GetLicenseConfigurationResponseTypeDef:
        """
        Gets detailed information about the specified license configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/get_license_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#get_license_configuration)
        """

    def get_license_conversion_task(
        self, **kwargs: Unpack[GetLicenseConversionTaskRequestTypeDef]
    ) -> GetLicenseConversionTaskResponseTypeDef:
        """
        Gets information about the specified license type conversion task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/get_license_conversion_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#get_license_conversion_task)
        """

    def get_license_manager_report_generator(
        self, **kwargs: Unpack[GetLicenseManagerReportGeneratorRequestTypeDef]
    ) -> GetLicenseManagerReportGeneratorResponseTypeDef:
        """
        Gets information about the specified report generator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/get_license_manager_report_generator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#get_license_manager_report_generator)
        """

    def get_license_usage(
        self, **kwargs: Unpack[GetLicenseUsageRequestTypeDef]
    ) -> GetLicenseUsageResponseTypeDef:
        """
        Gets detailed information about the usage of the specified license.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/get_license_usage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#get_license_usage)
        """

    def get_service_settings(self) -> GetServiceSettingsResponseTypeDef:
        """
        Gets the License Manager settings for the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/get_service_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#get_service_settings)
        """

    def list_associations_for_license_configuration(
        self, **kwargs: Unpack[ListAssociationsForLicenseConfigurationRequestTypeDef]
    ) -> ListAssociationsForLicenseConfigurationResponseTypeDef:
        """
        Lists the resource associations for the specified license configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/list_associations_for_license_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#list_associations_for_license_configuration)
        """

    def list_distributed_grants(
        self, **kwargs: Unpack[ListDistributedGrantsRequestTypeDef]
    ) -> ListDistributedGrantsResponseTypeDef:
        """
        Lists the grants distributed for the specified license.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/list_distributed_grants.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#list_distributed_grants)
        """

    def list_failures_for_license_configuration_operations(
        self, **kwargs: Unpack[ListFailuresForLicenseConfigurationOperationsRequestTypeDef]
    ) -> ListFailuresForLicenseConfigurationOperationsResponseTypeDef:
        """
        Lists the license configuration operations that failed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/list_failures_for_license_configuration_operations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#list_failures_for_license_configuration_operations)
        """

    def list_license_configurations(
        self, **kwargs: Unpack[ListLicenseConfigurationsRequestTypeDef]
    ) -> ListLicenseConfigurationsResponseTypeDef:
        """
        Lists the license configurations for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/list_license_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#list_license_configurations)
        """

    def list_license_conversion_tasks(
        self, **kwargs: Unpack[ListLicenseConversionTasksRequestTypeDef]
    ) -> ListLicenseConversionTasksResponseTypeDef:
        """
        Lists the license type conversion tasks for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/list_license_conversion_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#list_license_conversion_tasks)
        """

    def list_license_manager_report_generators(
        self, **kwargs: Unpack[ListLicenseManagerReportGeneratorsRequestTypeDef]
    ) -> ListLicenseManagerReportGeneratorsResponseTypeDef:
        """
        Lists the report generators for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/list_license_manager_report_generators.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#list_license_manager_report_generators)
        """

    def list_license_specifications_for_resource(
        self, **kwargs: Unpack[ListLicenseSpecificationsForResourceRequestTypeDef]
    ) -> ListLicenseSpecificationsForResourceResponseTypeDef:
        """
        Describes the license configurations for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/list_license_specifications_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#list_license_specifications_for_resource)
        """

    def list_license_versions(
        self, **kwargs: Unpack[ListLicenseVersionsRequestTypeDef]
    ) -> ListLicenseVersionsResponseTypeDef:
        """
        Lists all versions of the specified license.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/list_license_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#list_license_versions)
        """

    def list_licenses(
        self, **kwargs: Unpack[ListLicensesRequestTypeDef]
    ) -> ListLicensesResponseTypeDef:
        """
        Lists the licenses for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/list_licenses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#list_licenses)
        """

    def list_received_grants(
        self, **kwargs: Unpack[ListReceivedGrantsRequestTypeDef]
    ) -> ListReceivedGrantsResponseTypeDef:
        """
        Lists grants that are received.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/list_received_grants.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#list_received_grants)
        """

    def list_received_grants_for_organization(
        self, **kwargs: Unpack[ListReceivedGrantsForOrganizationRequestTypeDef]
    ) -> ListReceivedGrantsForOrganizationResponseTypeDef:
        """
        Lists the grants received for all accounts in the organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/list_received_grants_for_organization.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#list_received_grants_for_organization)
        """

    def list_received_licenses(
        self, **kwargs: Unpack[ListReceivedLicensesRequestTypeDef]
    ) -> ListReceivedLicensesResponseTypeDef:
        """
        Lists received licenses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/list_received_licenses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#list_received_licenses)
        """

    def list_received_licenses_for_organization(
        self, **kwargs: Unpack[ListReceivedLicensesForOrganizationRequestTypeDef]
    ) -> ListReceivedLicensesForOrganizationResponseTypeDef:
        """
        Lists the licenses received for all accounts in the organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/list_received_licenses_for_organization.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#list_received_licenses_for_organization)
        """

    def list_resource_inventory(
        self, **kwargs: Unpack[ListResourceInventoryRequestTypeDef]
    ) -> ListResourceInventoryResponseTypeDef:
        """
        Lists resources managed using Systems Manager inventory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/list_resource_inventory.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#list_resource_inventory)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified license configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#list_tags_for_resource)
        """

    def list_tokens(self, **kwargs: Unpack[ListTokensRequestTypeDef]) -> ListTokensResponseTypeDef:
        """
        Lists your tokens.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/list_tokens.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#list_tokens)
        """

    def list_usage_for_license_configuration(
        self, **kwargs: Unpack[ListUsageForLicenseConfigurationRequestTypeDef]
    ) -> ListUsageForLicenseConfigurationResponseTypeDef:
        """
        Lists all license usage records for a license configuration, displaying license
        consumption details by resource at a selected point in time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/list_usage_for_license_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#list_usage_for_license_configuration)
        """

    def reject_grant(
        self, **kwargs: Unpack[RejectGrantRequestTypeDef]
    ) -> RejectGrantResponseTypeDef:
        """
        Rejects the specified grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/reject_grant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#reject_grant)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified license configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified license configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#untag_resource)
        """

    def update_license_configuration(
        self, **kwargs: Unpack[UpdateLicenseConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies the attributes of an existing license configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/update_license_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#update_license_configuration)
        """

    def update_license_manager_report_generator(
        self, **kwargs: Unpack[UpdateLicenseManagerReportGeneratorRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates a report generator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/update_license_manager_report_generator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#update_license_manager_report_generator)
        """

    def update_license_specifications_for_resource(
        self, **kwargs: Unpack[UpdateLicenseSpecificationsForResourceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds or removes the specified license configurations for the specified Amazon
        Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/update_license_specifications_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#update_license_specifications_for_resource)
        """

    def update_service_settings(
        self, **kwargs: Unpack[UpdateServiceSettingsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates License Manager settings for the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/update_service_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#update_service_settings)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_associations_for_license_configuration"]
    ) -> ListAssociationsForLicenseConfigurationPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_license_configurations"]
    ) -> ListLicenseConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_license_specifications_for_resource"]
    ) -> ListLicenseSpecificationsForResourcePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resource_inventory"]
    ) -> ListResourceInventoryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_usage_for_license_configuration"]
    ) -> ListUsageForLicenseConfigurationPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/license-manager/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client/#get_paginator)
        """
