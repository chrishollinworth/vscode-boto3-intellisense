# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for worklink service client

Usage::

    ```python
    import boto3
    from mypy_boto3_worklink import WorkLinkClient

    client: WorkLinkClient = boto3.client("worklink")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_worklink.type_defs import (
    AssociateWebsiteAuthorizationProviderResponseTypeDef,
    AssociateWebsiteCertificateAuthorityResponseTypeDef,
    CreateFleetResponseTypeDef,
    DescribeAuditStreamConfigurationResponseTypeDef,
    DescribeCompanyNetworkConfigurationResponseTypeDef,
    DescribeDevicePolicyConfigurationResponseTypeDef,
    DescribeDeviceResponseTypeDef,
    DescribeDomainResponseTypeDef,
    DescribeFleetMetadataResponseTypeDef,
    DescribeIdentityProviderConfigurationResponseTypeDef,
    DescribeWebsiteCertificateAuthorityResponseTypeDef,
    ListDevicesResponseTypeDef,
    ListDomainsResponseTypeDef,
    ListFleetsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWebsiteAuthorizationProvidersResponseTypeDef,
    ListWebsiteCertificateAuthoritiesResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("WorkLinkClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]


class WorkLinkClient:
    """
    [WorkLink.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_domain(
        self, FleetArn: str, DomainName: str, AcmCertificateArn: str, DisplayName: str = None
    ) -> Dict[str, Any]:
        """
        [Client.associate_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.associate_domain)
        """

    def associate_website_authorization_provider(
        self, FleetArn: str, AuthorizationProviderType: Literal["SAML"], DomainName: str = None
    ) -> AssociateWebsiteAuthorizationProviderResponseTypeDef:
        """
        [Client.associate_website_authorization_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.associate_website_authorization_provider)
        """

    def associate_website_certificate_authority(
        self, FleetArn: str, Certificate: str, DisplayName: str = None
    ) -> AssociateWebsiteCertificateAuthorityResponseTypeDef:
        """
        [Client.associate_website_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.associate_website_certificate_authority)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.can_paginate)
        """

    def create_fleet(
        self,
        FleetName: str,
        DisplayName: str = None,
        OptimizeForEndUserLocation: bool = None,
        Tags: Dict[str, str] = None,
    ) -> CreateFleetResponseTypeDef:
        """
        [Client.create_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.create_fleet)
        """

    def delete_fleet(self, FleetArn: str) -> Dict[str, Any]:
        """
        [Client.delete_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.delete_fleet)
        """

    def describe_audit_stream_configuration(
        self, FleetArn: str
    ) -> DescribeAuditStreamConfigurationResponseTypeDef:
        """
        [Client.describe_audit_stream_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.describe_audit_stream_configuration)
        """

    def describe_company_network_configuration(
        self, FleetArn: str
    ) -> DescribeCompanyNetworkConfigurationResponseTypeDef:
        """
        [Client.describe_company_network_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.describe_company_network_configuration)
        """

    def describe_device(self, FleetArn: str, DeviceId: str) -> DescribeDeviceResponseTypeDef:
        """
        [Client.describe_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.describe_device)
        """

    def describe_device_policy_configuration(
        self, FleetArn: str
    ) -> DescribeDevicePolicyConfigurationResponseTypeDef:
        """
        [Client.describe_device_policy_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.describe_device_policy_configuration)
        """

    def describe_domain(self, FleetArn: str, DomainName: str) -> DescribeDomainResponseTypeDef:
        """
        [Client.describe_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.describe_domain)
        """

    def describe_fleet_metadata(self, FleetArn: str) -> DescribeFleetMetadataResponseTypeDef:
        """
        [Client.describe_fleet_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.describe_fleet_metadata)
        """

    def describe_identity_provider_configuration(
        self, FleetArn: str
    ) -> DescribeIdentityProviderConfigurationResponseTypeDef:
        """
        [Client.describe_identity_provider_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.describe_identity_provider_configuration)
        """

    def describe_website_certificate_authority(
        self, FleetArn: str, WebsiteCaId: str
    ) -> DescribeWebsiteCertificateAuthorityResponseTypeDef:
        """
        [Client.describe_website_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.describe_website_certificate_authority)
        """

    def disassociate_domain(self, FleetArn: str, DomainName: str) -> Dict[str, Any]:
        """
        [Client.disassociate_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.disassociate_domain)
        """

    def disassociate_website_authorization_provider(
        self, FleetArn: str, AuthorizationProviderId: str
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_website_authorization_provider documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.disassociate_website_authorization_provider)
        """

    def disassociate_website_certificate_authority(
        self, FleetArn: str, WebsiteCaId: str
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_website_certificate_authority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.disassociate_website_certificate_authority)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.generate_presigned_url)
        """

    def list_devices(
        self, FleetArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDevicesResponseTypeDef:
        """
        [Client.list_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.list_devices)
        """

    def list_domains(
        self, FleetArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDomainsResponseTypeDef:
        """
        [Client.list_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.list_domains)
        """

    def list_fleets(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListFleetsResponseTypeDef:
        """
        [Client.list_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.list_fleets)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.list_tags_for_resource)
        """

    def list_website_authorization_providers(
        self, FleetArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListWebsiteAuthorizationProvidersResponseTypeDef:
        """
        [Client.list_website_authorization_providers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.list_website_authorization_providers)
        """

    def list_website_certificate_authorities(
        self, FleetArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListWebsiteCertificateAuthoritiesResponseTypeDef:
        """
        [Client.list_website_certificate_authorities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.list_website_certificate_authorities)
        """

    def restore_domain_access(self, FleetArn: str, DomainName: str) -> Dict[str, Any]:
        """
        [Client.restore_domain_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.restore_domain_access)
        """

    def revoke_domain_access(self, FleetArn: str, DomainName: str) -> Dict[str, Any]:
        """
        [Client.revoke_domain_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.revoke_domain_access)
        """

    def sign_out_user(self, FleetArn: str, Username: str) -> Dict[str, Any]:
        """
        [Client.sign_out_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.sign_out_user)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.untag_resource)
        """

    def update_audit_stream_configuration(
        self, FleetArn: str, AuditStreamArn: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_audit_stream_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.update_audit_stream_configuration)
        """

    def update_company_network_configuration(
        self, FleetArn: str, VpcId: str, SubnetIds: List[str], SecurityGroupIds: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.update_company_network_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.update_company_network_configuration)
        """

    def update_device_policy_configuration(
        self, FleetArn: str, DeviceCaCertificate: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_device_policy_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.update_device_policy_configuration)
        """

    def update_domain_metadata(
        self, FleetArn: str, DomainName: str, DisplayName: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_domain_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.update_domain_metadata)
        """

    def update_fleet_metadata(
        self, FleetArn: str, DisplayName: str = None, OptimizeForEndUserLocation: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.update_fleet_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.update_fleet_metadata)
        """

    def update_identity_provider_configuration(
        self,
        FleetArn: str,
        IdentityProviderType: Literal["SAML"],
        IdentityProviderSamlMetadata: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_identity_provider_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/worklink.html#WorkLink.Client.update_identity_provider_configuration)
        """
