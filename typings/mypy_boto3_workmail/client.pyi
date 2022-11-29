"""
Type annotations for workmail service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_workmail import WorkMailClient

    client: WorkMailClient = boto3.client("workmail")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AccessControlRuleEffectType,
    ImpersonationRoleTypeType,
    MobileDeviceAccessRuleEffectType,
    PermissionTypeType,
    ResourceTypeType,
)
from .paginator import (
    ListAliasesPaginator,
    ListAvailabilityConfigurationsPaginator,
    ListGroupMembersPaginator,
    ListGroupsPaginator,
    ListMailboxPermissionsPaginator,
    ListOrganizationsPaginator,
    ListResourceDelegatesPaginator,
    ListResourcesPaginator,
    ListUsersPaginator,
)
from .type_defs import (
    AssumeImpersonationRoleResponseTypeDef,
    BookingOptionsTypeDef,
    CreateGroupResponseTypeDef,
    CreateImpersonationRoleResponseTypeDef,
    CreateMobileDeviceAccessRuleResponseTypeDef,
    CreateOrganizationResponseTypeDef,
    CreateResourceResponseTypeDef,
    CreateUserResponseTypeDef,
    DeleteOrganizationResponseTypeDef,
    DescribeEmailMonitoringConfigurationResponseTypeDef,
    DescribeGroupResponseTypeDef,
    DescribeInboundDmarcSettingsResponseTypeDef,
    DescribeMailboxExportJobResponseTypeDef,
    DescribeOrganizationResponseTypeDef,
    DescribeResourceResponseTypeDef,
    DescribeUserResponseTypeDef,
    DomainTypeDef,
    EwsAvailabilityProviderTypeDef,
    FolderConfigurationTypeDef,
    GetAccessControlEffectResponseTypeDef,
    GetDefaultRetentionPolicyResponseTypeDef,
    GetImpersonationRoleEffectResponseTypeDef,
    GetImpersonationRoleResponseTypeDef,
    GetMailboxDetailsResponseTypeDef,
    GetMailDomainResponseTypeDef,
    GetMobileDeviceAccessEffectResponseTypeDef,
    GetMobileDeviceAccessOverrideResponseTypeDef,
    ImpersonationRuleTypeDef,
    LambdaAvailabilityProviderTypeDef,
    ListAccessControlRulesResponseTypeDef,
    ListAliasesResponseTypeDef,
    ListAvailabilityConfigurationsResponseTypeDef,
    ListGroupMembersResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListImpersonationRolesResponseTypeDef,
    ListMailboxExportJobsResponseTypeDef,
    ListMailboxPermissionsResponseTypeDef,
    ListMailDomainsResponseTypeDef,
    ListMobileDeviceAccessOverridesResponseTypeDef,
    ListMobileDeviceAccessRulesResponseTypeDef,
    ListOrganizationsResponseTypeDef,
    ListResourceDelegatesResponseTypeDef,
    ListResourcesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUsersResponseTypeDef,
    StartMailboxExportJobResponseTypeDef,
    TagTypeDef,
    TestAvailabilityConfigurationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("WorkMailClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    DirectoryInUseException: Type[BotocoreClientError]
    DirectoryServiceAuthenticationFailedException: Type[BotocoreClientError]
    DirectoryUnavailableException: Type[BotocoreClientError]
    EmailAddressInUseException: Type[BotocoreClientError]
    EntityAlreadyRegisteredException: Type[BotocoreClientError]
    EntityNotFoundException: Type[BotocoreClientError]
    EntityStateException: Type[BotocoreClientError]
    InvalidConfigurationException: Type[BotocoreClientError]
    InvalidCustomSesConfigurationException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidPasswordException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MailDomainInUseException: Type[BotocoreClientError]
    MailDomainNotFoundException: Type[BotocoreClientError]
    MailDomainStateException: Type[BotocoreClientError]
    NameAvailabilityException: Type[BotocoreClientError]
    OrganizationNotFoundException: Type[BotocoreClientError]
    OrganizationStateException: Type[BotocoreClientError]
    ReservedNameException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]

class WorkMailClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        WorkMailClient exceptions.
        """
    def associate_delegate_to_resource(
        self, *, OrganizationId: str, ResourceId: str, EntityId: str
    ) -> Dict[str, Any]:
        """
        Adds a member (user or group) to the resource's set of delegates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.associate_delegate_to_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#associate_delegate_to_resource)
        """
    def associate_member_to_group(
        self, *, OrganizationId: str, GroupId: str, MemberId: str
    ) -> Dict[str, Any]:
        """
        Adds a member (user or group) to the group's set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.associate_member_to_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#associate_member_to_group)
        """
    def assume_impersonation_role(
        self, *, OrganizationId: str, ImpersonationRoleId: str
    ) -> AssumeImpersonationRoleResponseTypeDef:
        """
        Assumes an impersonation role for the given WorkMail organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.assume_impersonation_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#assume_impersonation_role)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#can_paginate)
        """
    def cancel_mailbox_export_job(
        self, *, ClientToken: str, JobId: str, OrganizationId: str
    ) -> Dict[str, Any]:
        """
        Cancels a mailbox export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.cancel_mailbox_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#cancel_mailbox_export_job)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#close)
        """
    def create_alias(self, *, OrganizationId: str, EntityId: str, Alias: str) -> Dict[str, Any]:
        """
        Adds an alias to the set of a given member (user or group) of WorkMail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.create_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#create_alias)
        """
    def create_availability_configuration(
        self,
        *,
        OrganizationId: str,
        DomainName: str,
        ClientToken: str = None,
        EwsProvider: "EwsAvailabilityProviderTypeDef" = None,
        LambdaProvider: "LambdaAvailabilityProviderTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Creates an `AvailabilityConfiguration` for the given WorkMail organization and
        domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.create_availability_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#create_availability_configuration)
        """
    def create_group(self, *, OrganizationId: str, Name: str) -> CreateGroupResponseTypeDef:
        """
        Creates a group that can be used in WorkMail by calling the  RegisterToWorkMail
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.create_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#create_group)
        """
    def create_impersonation_role(
        self,
        *,
        OrganizationId: str,
        Name: str,
        Type: ImpersonationRoleTypeType,
        Rules: List["ImpersonationRuleTypeDef"],
        ClientToken: str = None,
        Description: str = None
    ) -> CreateImpersonationRoleResponseTypeDef:
        """
        Creates an impersonation role for the given WorkMail organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.create_impersonation_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#create_impersonation_role)
        """
    def create_mobile_device_access_rule(
        self,
        *,
        OrganizationId: str,
        Name: str,
        Effect: MobileDeviceAccessRuleEffectType,
        ClientToken: str = None,
        Description: str = None,
        DeviceTypes: List[str] = None,
        NotDeviceTypes: List[str] = None,
        DeviceModels: List[str] = None,
        NotDeviceModels: List[str] = None,
        DeviceOperatingSystems: List[str] = None,
        NotDeviceOperatingSystems: List[str] = None,
        DeviceUserAgents: List[str] = None,
        NotDeviceUserAgents: List[str] = None
    ) -> CreateMobileDeviceAccessRuleResponseTypeDef:
        """
        Creates a new mobile device access rule for the specified WorkMail organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.create_mobile_device_access_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#create_mobile_device_access_rule)
        """
    def create_organization(
        self,
        *,
        Alias: str,
        DirectoryId: str = None,
        ClientToken: str = None,
        Domains: List["DomainTypeDef"] = None,
        KmsKeyArn: str = None,
        EnableInteroperability: bool = None
    ) -> CreateOrganizationResponseTypeDef:
        """
        Creates a new WorkMail organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.create_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#create_organization)
        """
    def create_resource(
        self, *, OrganizationId: str, Name: str, Type: ResourceTypeType
    ) -> CreateResourceResponseTypeDef:
        """
        Creates a new WorkMail resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.create_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#create_resource)
        """
    def create_user(
        self, *, OrganizationId: str, Name: str, DisplayName: str, Password: str
    ) -> CreateUserResponseTypeDef:
        """
        Creates a user who can be used in WorkMail by calling the  RegisterToWorkMail
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.create_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#create_user)
        """
    def delete_access_control_rule(self, *, OrganizationId: str, Name: str) -> Dict[str, Any]:
        """
        Deletes an access control rule for the specified WorkMail organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.delete_access_control_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#delete_access_control_rule)
        """
    def delete_alias(self, *, OrganizationId: str, EntityId: str, Alias: str) -> Dict[str, Any]:
        """
        Remove one or more specified aliases from a set of aliases for a given user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.delete_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#delete_alias)
        """
    def delete_availability_configuration(
        self, *, OrganizationId: str, DomainName: str
    ) -> Dict[str, Any]:
        """
        Deletes the `AvailabilityConfiguration` for the given WorkMail organization and
        domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.delete_availability_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#delete_availability_configuration)
        """
    def delete_email_monitoring_configuration(self, *, OrganizationId: str) -> Dict[str, Any]:
        """
        Deletes the email monitoring configuration for a specified organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.delete_email_monitoring_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#delete_email_monitoring_configuration)
        """
    def delete_group(self, *, OrganizationId: str, GroupId: str) -> Dict[str, Any]:
        """
        Deletes a group from WorkMail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.delete_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#delete_group)
        """
    def delete_impersonation_role(
        self, *, OrganizationId: str, ImpersonationRoleId: str
    ) -> Dict[str, Any]:
        """
        Deletes an impersonation role for the given WorkMail organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.delete_impersonation_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#delete_impersonation_role)
        """
    def delete_mailbox_permissions(
        self, *, OrganizationId: str, EntityId: str, GranteeId: str
    ) -> Dict[str, Any]:
        """
        Deletes permissions granted to a member (user or group).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.delete_mailbox_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#delete_mailbox_permissions)
        """
    def delete_mobile_device_access_override(
        self, *, OrganizationId: str, UserId: str, DeviceId: str
    ) -> Dict[str, Any]:
        """
        Deletes the mobile device access override for the given WorkMail organization,
        user, and device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.delete_mobile_device_access_override)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#delete_mobile_device_access_override)
        """
    def delete_mobile_device_access_rule(
        self, *, OrganizationId: str, MobileDeviceAccessRuleId: str
    ) -> Dict[str, Any]:
        """
        Deletes a mobile device access rule for the specified WorkMail organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.delete_mobile_device_access_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#delete_mobile_device_access_rule)
        """
    def delete_organization(
        self, *, OrganizationId: str, DeleteDirectory: bool, ClientToken: str = None
    ) -> DeleteOrganizationResponseTypeDef:
        """
        Deletes an WorkMail organization and all underlying AWS resources managed by
        WorkMail as part of the organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.delete_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#delete_organization)
        """
    def delete_resource(self, *, OrganizationId: str, ResourceId: str) -> Dict[str, Any]:
        """
        Deletes the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.delete_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#delete_resource)
        """
    def delete_retention_policy(self, *, OrganizationId: str, Id: str) -> Dict[str, Any]:
        """
        Deletes the specified retention policy from the specified organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.delete_retention_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#delete_retention_policy)
        """
    def delete_user(self, *, OrganizationId: str, UserId: str) -> Dict[str, Any]:
        """
        Deletes a user from WorkMail and all subsequent systems.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.delete_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#delete_user)
        """
    def deregister_from_work_mail(self, *, OrganizationId: str, EntityId: str) -> Dict[str, Any]:
        """
        Mark a user, group, or resource as no longer used in WorkMail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.deregister_from_work_mail)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#deregister_from_work_mail)
        """
    def deregister_mail_domain(self, *, OrganizationId: str, DomainName: str) -> Dict[str, Any]:
        """
        Removes a domain from WorkMail, stops email routing to WorkMail, and removes the
        authorization allowing WorkMail use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.deregister_mail_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#deregister_mail_domain)
        """
    def describe_email_monitoring_configuration(
        self, *, OrganizationId: str
    ) -> DescribeEmailMonitoringConfigurationResponseTypeDef:
        """
        Describes the current email monitoring configuration for a specified
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.describe_email_monitoring_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#describe_email_monitoring_configuration)
        """
    def describe_group(self, *, OrganizationId: str, GroupId: str) -> DescribeGroupResponseTypeDef:
        """
        Returns the data available for the group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.describe_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#describe_group)
        """
    def describe_inbound_dmarc_settings(
        self, *, OrganizationId: str
    ) -> DescribeInboundDmarcSettingsResponseTypeDef:
        """
        Lists the settings in a DMARC policy for a specified organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.describe_inbound_dmarc_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#describe_inbound_dmarc_settings)
        """
    def describe_mailbox_export_job(
        self, *, JobId: str, OrganizationId: str
    ) -> DescribeMailboxExportJobResponseTypeDef:
        """
        Describes the current status of a mailbox export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.describe_mailbox_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#describe_mailbox_export_job)
        """
    def describe_organization(self, *, OrganizationId: str) -> DescribeOrganizationResponseTypeDef:
        """
        Provides more information regarding a given organization based on its
        identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.describe_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#describe_organization)
        """
    def describe_resource(
        self, *, OrganizationId: str, ResourceId: str
    ) -> DescribeResourceResponseTypeDef:
        """
        Returns the data available for the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.describe_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#describe_resource)
        """
    def describe_user(self, *, OrganizationId: str, UserId: str) -> DescribeUserResponseTypeDef:
        """
        Provides information regarding the user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.describe_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#describe_user)
        """
    def disassociate_delegate_from_resource(
        self, *, OrganizationId: str, ResourceId: str, EntityId: str
    ) -> Dict[str, Any]:
        """
        Removes a member from the resource's set of delegates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.disassociate_delegate_from_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#disassociate_delegate_from_resource)
        """
    def disassociate_member_from_group(
        self, *, OrganizationId: str, GroupId: str, MemberId: str
    ) -> Dict[str, Any]:
        """
        Removes a member from a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.disassociate_member_from_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#disassociate_member_from_group)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#generate_presigned_url)
        """
    def get_access_control_effect(
        self,
        *,
        OrganizationId: str,
        IpAddress: str,
        Action: str,
        UserId: str = None,
        ImpersonationRoleId: str = None
    ) -> GetAccessControlEffectResponseTypeDef:
        """
        Gets the effects of an organization's access control rules as they apply to a
        specified IPv4 address, access protocol action, and user ID or impersonation
        role ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.get_access_control_effect)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#get_access_control_effect)
        """
    def get_default_retention_policy(
        self, *, OrganizationId: str
    ) -> GetDefaultRetentionPolicyResponseTypeDef:
        """
        Gets the default retention policy details for the specified organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.get_default_retention_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#get_default_retention_policy)
        """
    def get_impersonation_role(
        self, *, OrganizationId: str, ImpersonationRoleId: str
    ) -> GetImpersonationRoleResponseTypeDef:
        """
        Gets the impersonation role details for the given WorkMail organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.get_impersonation_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#get_impersonation_role)
        """
    def get_impersonation_role_effect(
        self, *, OrganizationId: str, ImpersonationRoleId: str, TargetUser: str
    ) -> GetImpersonationRoleEffectResponseTypeDef:
        """
        Tests whether the given impersonation role can impersonate a target user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.get_impersonation_role_effect)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#get_impersonation_role_effect)
        """
    def get_mail_domain(
        self, *, OrganizationId: str, DomainName: str
    ) -> GetMailDomainResponseTypeDef:
        """
        Gets details for a mail domain, including domain records required to configure
        your domain with recommended security.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.get_mail_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#get_mail_domain)
        """
    def get_mailbox_details(
        self, *, OrganizationId: str, UserId: str
    ) -> GetMailboxDetailsResponseTypeDef:
        """
        Requests a user's mailbox details for a specified organization and user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.get_mailbox_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#get_mailbox_details)
        """
    def get_mobile_device_access_effect(
        self,
        *,
        OrganizationId: str,
        DeviceType: str = None,
        DeviceModel: str = None,
        DeviceOperatingSystem: str = None,
        DeviceUserAgent: str = None
    ) -> GetMobileDeviceAccessEffectResponseTypeDef:
        """
        Simulates the effect of the mobile device access rules for the given attributes
        of a sample access event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.get_mobile_device_access_effect)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#get_mobile_device_access_effect)
        """
    def get_mobile_device_access_override(
        self, *, OrganizationId: str, UserId: str, DeviceId: str
    ) -> GetMobileDeviceAccessOverrideResponseTypeDef:
        """
        Gets the mobile device access override for the given WorkMail organization,
        user, and device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.get_mobile_device_access_override)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#get_mobile_device_access_override)
        """
    def list_access_control_rules(
        self, *, OrganizationId: str
    ) -> ListAccessControlRulesResponseTypeDef:
        """
        Lists the access control rules for the specified organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.list_access_control_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#list_access_control_rules)
        """
    def list_aliases(
        self, *, OrganizationId: str, EntityId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAliasesResponseTypeDef:
        """
        Creates a paginated call to list the aliases associated with a given entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.list_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#list_aliases)
        """
    def list_availability_configurations(
        self, *, OrganizationId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAvailabilityConfigurationsResponseTypeDef:
        """
        List all the `AvailabilityConfiguration` 's for the given WorkMail organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.list_availability_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#list_availability_configurations)
        """
    def list_group_members(
        self, *, OrganizationId: str, GroupId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListGroupMembersResponseTypeDef:
        """
        Returns an overview of the members of a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.list_group_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#list_group_members)
        """
    def list_groups(
        self, *, OrganizationId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListGroupsResponseTypeDef:
        """
        Returns summaries of the organization's groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.list_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#list_groups)
        """
    def list_impersonation_roles(
        self, *, OrganizationId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListImpersonationRolesResponseTypeDef:
        """
        Lists all the impersonation roles for the given WorkMail organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.list_impersonation_roles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#list_impersonation_roles)
        """
    def list_mail_domains(
        self, *, OrganizationId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListMailDomainsResponseTypeDef:
        """
        Lists the mail domains in a given WorkMail organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.list_mail_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#list_mail_domains)
        """
    def list_mailbox_export_jobs(
        self, *, OrganizationId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListMailboxExportJobsResponseTypeDef:
        """
        Lists the mailbox export jobs started for the specified organization within the
        last seven days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.list_mailbox_export_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#list_mailbox_export_jobs)
        """
    def list_mailbox_permissions(
        self, *, OrganizationId: str, EntityId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListMailboxPermissionsResponseTypeDef:
        """
        Lists the mailbox permissions associated with a user, group, or resource
        mailbox.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.list_mailbox_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#list_mailbox_permissions)
        """
    def list_mobile_device_access_overrides(
        self,
        *,
        OrganizationId: str,
        UserId: str = None,
        DeviceId: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListMobileDeviceAccessOverridesResponseTypeDef:
        """
        Lists all the mobile device access overrides for any given combination of
        WorkMail organization, user, or device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.list_mobile_device_access_overrides)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#list_mobile_device_access_overrides)
        """
    def list_mobile_device_access_rules(
        self, *, OrganizationId: str
    ) -> ListMobileDeviceAccessRulesResponseTypeDef:
        """
        Lists the mobile device access rules for the specified WorkMail organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.list_mobile_device_access_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#list_mobile_device_access_rules)
        """
    def list_organizations(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListOrganizationsResponseTypeDef:
        """
        Returns summaries of the customer's organizations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.list_organizations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#list_organizations)
        """
    def list_resource_delegates(
        self, *, OrganizationId: str, ResourceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListResourceDelegatesResponseTypeDef:
        """
        Lists the delegates associated with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.list_resource_delegates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#list_resource_delegates)
        """
    def list_resources(
        self, *, OrganizationId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListResourcesResponseTypeDef:
        """
        Returns summaries of the organization's resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.list_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#list_resources)
        """
    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags applied to an WorkMail organization resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#list_tags_for_resource)
        """
    def list_users(
        self, *, OrganizationId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListUsersResponseTypeDef:
        """
        Returns summaries of the organization's users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.list_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#list_users)
        """
    def put_access_control_rule(
        self,
        *,
        Name: str,
        Effect: AccessControlRuleEffectType,
        Description: str,
        OrganizationId: str,
        IpRanges: List[str] = None,
        NotIpRanges: List[str] = None,
        Actions: List[str] = None,
        NotActions: List[str] = None,
        UserIds: List[str] = None,
        NotUserIds: List[str] = None,
        ImpersonationRoleIds: List[str] = None,
        NotImpersonationRoleIds: List[str] = None
    ) -> Dict[str, Any]:
        """
        Adds a new access control rule for the specified organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.put_access_control_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#put_access_control_rule)
        """
    def put_email_monitoring_configuration(
        self, *, OrganizationId: str, RoleArn: str, LogGroupArn: str
    ) -> Dict[str, Any]:
        """
        Creates or updates the email monitoring configuration for a specified
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.put_email_monitoring_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#put_email_monitoring_configuration)
        """
    def put_inbound_dmarc_settings(self, *, OrganizationId: str, Enforced: bool) -> Dict[str, Any]:
        """
        Enables or disables a DMARC policy for a given organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.put_inbound_dmarc_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#put_inbound_dmarc_settings)
        """
    def put_mailbox_permissions(
        self,
        *,
        OrganizationId: str,
        EntityId: str,
        GranteeId: str,
        PermissionValues: List[PermissionTypeType]
    ) -> Dict[str, Any]:
        """
        Sets permissions for a user, group, or resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.put_mailbox_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#put_mailbox_permissions)
        """
    def put_mobile_device_access_override(
        self,
        *,
        OrganizationId: str,
        UserId: str,
        DeviceId: str,
        Effect: MobileDeviceAccessRuleEffectType,
        Description: str = None
    ) -> Dict[str, Any]:
        """
        Creates or updates a mobile device access override for the given WorkMail
        organization, user, and device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.put_mobile_device_access_override)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#put_mobile_device_access_override)
        """
    def put_retention_policy(
        self,
        *,
        OrganizationId: str,
        Name: str,
        FolderConfigurations: List["FolderConfigurationTypeDef"],
        Id: str = None,
        Description: str = None
    ) -> Dict[str, Any]:
        """
        Puts a retention policy to the specified organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.put_retention_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#put_retention_policy)
        """
    def register_mail_domain(
        self, *, OrganizationId: str, DomainName: str, ClientToken: str = None
    ) -> Dict[str, Any]:
        """
        Registers a new domain in WorkMail and SES, and configures it for use by
        WorkMail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.register_mail_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#register_mail_domain)
        """
    def register_to_work_mail(
        self, *, OrganizationId: str, EntityId: str, Email: str
    ) -> Dict[str, Any]:
        """
        Registers an existing and disabled user, group, or resource for WorkMail use by
        associating a mailbox and calendaring capabilities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.register_to_work_mail)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#register_to_work_mail)
        """
    def reset_password(self, *, OrganizationId: str, UserId: str, Password: str) -> Dict[str, Any]:
        """
        Allows the administrator to reset the password for a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.reset_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#reset_password)
        """
    def start_mailbox_export_job(
        self,
        *,
        ClientToken: str,
        OrganizationId: str,
        EntityId: str,
        RoleArn: str,
        KmsKeyArn: str,
        S3BucketName: str,
        S3Prefix: str,
        Description: str = None
    ) -> StartMailboxExportJobResponseTypeDef:
        """
        Starts a mailbox export job to export MIME-format email messages and calendar
        items from the specified mailbox to the specified Amazon Simple Storage Service
        (Amazon S3) bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.start_mailbox_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#start_mailbox_export_job)
        """
    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Applies the specified tags to the specified WorkMailorganization resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#tag_resource)
        """
    def test_availability_configuration(
        self,
        *,
        OrganizationId: str,
        DomainName: str = None,
        EwsProvider: "EwsAvailabilityProviderTypeDef" = None,
        LambdaProvider: "LambdaAvailabilityProviderTypeDef" = None
    ) -> TestAvailabilityConfigurationResponseTypeDef:
        """
        Performs a test on an availability provider to ensure that access is allowed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.test_availability_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#test_availability_configuration)
        """
    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Untags the specified tags from the specified WorkMail organization resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#untag_resource)
        """
    def update_availability_configuration(
        self,
        *,
        OrganizationId: str,
        DomainName: str,
        EwsProvider: "EwsAvailabilityProviderTypeDef" = None,
        LambdaProvider: "LambdaAvailabilityProviderTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates an existing `AvailabilityConfiguration` for the given WorkMail
        organization and domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.update_availability_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#update_availability_configuration)
        """
    def update_default_mail_domain(self, *, OrganizationId: str, DomainName: str) -> Dict[str, Any]:
        """
        Updates the default mail domain for an organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.update_default_mail_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#update_default_mail_domain)
        """
    def update_impersonation_role(
        self,
        *,
        OrganizationId: str,
        ImpersonationRoleId: str,
        Name: str,
        Type: ImpersonationRoleTypeType,
        Rules: List["ImpersonationRuleTypeDef"],
        Description: str = None
    ) -> Dict[str, Any]:
        """
        Updates an impersonation role for the given WorkMail organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.update_impersonation_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#update_impersonation_role)
        """
    def update_mailbox_quota(
        self, *, OrganizationId: str, UserId: str, MailboxQuota: int
    ) -> Dict[str, Any]:
        """
        Updates a user's current mailbox quota for a specified organization and user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.update_mailbox_quota)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#update_mailbox_quota)
        """
    def update_mobile_device_access_rule(
        self,
        *,
        OrganizationId: str,
        MobileDeviceAccessRuleId: str,
        Name: str,
        Effect: MobileDeviceAccessRuleEffectType,
        Description: str = None,
        DeviceTypes: List[str] = None,
        NotDeviceTypes: List[str] = None,
        DeviceModels: List[str] = None,
        NotDeviceModels: List[str] = None,
        DeviceOperatingSystems: List[str] = None,
        NotDeviceOperatingSystems: List[str] = None,
        DeviceUserAgents: List[str] = None,
        NotDeviceUserAgents: List[str] = None
    ) -> Dict[str, Any]:
        """
        Updates a mobile device access rule for the specified WorkMail organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.update_mobile_device_access_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#update_mobile_device_access_rule)
        """
    def update_primary_email_address(
        self, *, OrganizationId: str, EntityId: str, Email: str
    ) -> Dict[str, Any]:
        """
        Updates the primary email for a user, group, or resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.update_primary_email_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#update_primary_email_address)
        """
    def update_resource(
        self,
        *,
        OrganizationId: str,
        ResourceId: str,
        Name: str = None,
        BookingOptions: "BookingOptionsTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates data for the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Client.update_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/client.html#update_resource)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_aliases"]) -> ListAliasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Paginator.ListAliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators.html#listaliasespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_availability_configurations"]
    ) -> ListAvailabilityConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Paginator.ListAvailabilityConfigurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators.html#listavailabilityconfigurationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_group_members"]
    ) -> ListGroupMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Paginator.ListGroupMembers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators.html#listgroupmemberspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_groups"]) -> ListGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Paginator.ListGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators.html#listgroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_mailbox_permissions"]
    ) -> ListMailboxPermissionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Paginator.ListMailboxPermissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators.html#listmailboxpermissionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_organizations"]
    ) -> ListOrganizationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Paginator.ListOrganizations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators.html#listorganizationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_delegates"]
    ) -> ListResourceDelegatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Paginator.ListResourceDelegates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators.html#listresourcedelegatespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_resources"]) -> ListResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Paginator.ListResources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators.html#listresourcespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_users"]) -> ListUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/workmail.html#WorkMail.Paginator.ListUsers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators.html#listuserspaginator)
        """
