# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
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
    CreateLicenseConfigurationResponseTypeDef,
    FilterTypeDef,
    GetLicenseConfigurationResponseTypeDef,
    GetServiceSettingsResponseTypeDef,
    InventoryFilterTypeDef,
    LicenseSpecificationTypeDef,
    ListAssociationsForLicenseConfigurationResponseTypeDef,
    ListFailuresForLicenseConfigurationOperationsResponseTypeDef,
    ListLicenseConfigurationsResponseTypeDef,
    ListLicenseSpecificationsForResourceResponseTypeDef,
    ListResourceInventoryResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUsageForLicenseConfigurationResponseTypeDef,
    OrganizationConfigurationTypeDef,
    ProductInformationTypeDef,
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
    FailedDependencyException: Type[BotocoreClientError]
    FilterLimitExceededException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidResourceStateException: Type[BotocoreClientError]
    LicenseUsageException: Type[BotocoreClientError]
    RateLimitExceededException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ServerInternalException: Type[BotocoreClientError]


class LicenseManagerClient:
    """
    [LicenseManager.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Client.can_paginate)
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
        ProductInformationList: List["ProductInformationTypeDef"] = None,
    ) -> CreateLicenseConfigurationResponseTypeDef:
        """
        [Client.create_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Client.create_license_configuration)
        """

    def delete_license_configuration(self, LicenseConfigurationArn: str) -> Dict[str, Any]:
        """
        [Client.delete_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Client.delete_license_configuration)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Client.generate_presigned_url)
        """

    def get_license_configuration(
        self, LicenseConfigurationArn: str
    ) -> GetLicenseConfigurationResponseTypeDef:
        """
        [Client.get_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Client.get_license_configuration)
        """

    def get_service_settings(self) -> GetServiceSettingsResponseTypeDef:
        """
        [Client.get_service_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Client.get_service_settings)
        """

    def list_associations_for_license_configuration(
        self, LicenseConfigurationArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAssociationsForLicenseConfigurationResponseTypeDef:
        """
        [Client.list_associations_for_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Client.list_associations_for_license_configuration)
        """

    def list_failures_for_license_configuration_operations(
        self, LicenseConfigurationArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListFailuresForLicenseConfigurationOperationsResponseTypeDef:
        """
        [Client.list_failures_for_license_configuration_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Client.list_failures_for_license_configuration_operations)
        """

    def list_license_configurations(
        self,
        LicenseConfigurationArns: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
    ) -> ListLicenseConfigurationsResponseTypeDef:
        """
        [Client.list_license_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Client.list_license_configurations)
        """

    def list_license_specifications_for_resource(
        self, ResourceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListLicenseSpecificationsForResourceResponseTypeDef:
        """
        [Client.list_license_specifications_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Client.list_license_specifications_for_resource)
        """

    def list_resource_inventory(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[InventoryFilterTypeDef] = None,
    ) -> ListResourceInventoryResponseTypeDef:
        """
        [Client.list_resource_inventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Client.list_resource_inventory)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Client.list_tags_for_resource)
        """

    def list_usage_for_license_configuration(
        self,
        LicenseConfigurationArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
    ) -> ListUsageForLicenseConfigurationResponseTypeDef:
        """
        [Client.list_usage_for_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Client.list_usage_for_license_configuration)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Client.untag_resource)
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
    ) -> Dict[str, Any]:
        """
        [Client.update_license_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Client.update_license_configuration)
        """

    def update_license_specifications_for_resource(
        self,
        ResourceArn: str,
        AddLicenseSpecifications: List["LicenseSpecificationTypeDef"] = None,
        RemoveLicenseSpecifications: List["LicenseSpecificationTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_license_specifications_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Client.update_license_specifications_for_resource)
        """

    def update_service_settings(
        self,
        S3BucketArn: str = None,
        SnsTopicArn: str = None,
        OrganizationConfiguration: "OrganizationConfigurationTypeDef" = None,
        EnableCrossAccountsDiscovery: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_service_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Client.update_service_settings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_associations_for_license_configuration"]
    ) -> ListAssociationsForLicenseConfigurationPaginator:
        """
        [Paginator.ListAssociationsForLicenseConfiguration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Paginator.ListAssociationsForLicenseConfiguration)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_license_configurations"]
    ) -> ListLicenseConfigurationsPaginator:
        """
        [Paginator.ListLicenseConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseConfigurations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_license_specifications_for_resource"]
    ) -> ListLicenseSpecificationsForResourcePaginator:
        """
        [Paginator.ListLicenseSpecificationsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseSpecificationsForResource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_inventory"]
    ) -> ListResourceInventoryPaginator:
        """
        [Paginator.ListResourceInventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Paginator.ListResourceInventory)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_usage_for_license_configuration"]
    ) -> ListUsageForLicenseConfigurationPaginator:
        """
        [Paginator.ListUsageForLicenseConfiguration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/license-manager.html#LicenseManager.Paginator.ListUsageForLicenseConfiguration)
        """
