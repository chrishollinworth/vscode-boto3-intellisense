# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for fms service client

Usage::

    ```python
    import boto3
    from mypy_boto3_fms import FMSClient

    client: FMSClient = boto3.client("fms")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_fms.paginator import (
    ListComplianceStatusPaginator,
    ListMemberAccountsPaginator,
    ListPoliciesPaginator,
)
from mypy_boto3_fms.type_defs import (
    AppsListDataTypeDef,
    GetAdminAccountResponseTypeDef,
    GetAppsListResponseTypeDef,
    GetComplianceDetailResponseTypeDef,
    GetNotificationChannelResponseTypeDef,
    GetPolicyResponseTypeDef,
    GetProtectionStatusResponseTypeDef,
    GetProtocolsListResponseTypeDef,
    GetViolationDetailsResponseTypeDef,
    ListAppsListsResponseTypeDef,
    ListComplianceStatusResponseTypeDef,
    ListMemberAccountsResponseTypeDef,
    ListPoliciesResponseTypeDef,
    ListProtocolsListsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PolicyTypeDef,
    ProtocolsListDataTypeDef,
    PutAppsListResponseTypeDef,
    PutPolicyResponseTypeDef,
    PutProtocolsListResponseTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("FMSClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    InternalErrorException: Type[Boto3ClientError]
    InvalidInputException: Type[Boto3ClientError]
    InvalidOperationException: Type[Boto3ClientError]
    InvalidTypeException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]


class FMSClient:
    """
    [FMS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client)
    """

    exceptions: Exceptions

    def associate_admin_account(self, AdminAccount: str) -> None:
        """
        [Client.associate_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.associate_admin_account)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.can_paginate)
        """

    def delete_apps_list(self, ListId: str) -> None:
        """
        [Client.delete_apps_list documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.delete_apps_list)
        """

    def delete_notification_channel(self) -> None:
        """
        [Client.delete_notification_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.delete_notification_channel)
        """

    def delete_policy(self, PolicyId: str, DeleteAllPolicyResources: bool = None) -> None:
        """
        [Client.delete_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.delete_policy)
        """

    def delete_protocols_list(self, ListId: str) -> None:
        """
        [Client.delete_protocols_list documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.delete_protocols_list)
        """

    def disassociate_admin_account(self) -> None:
        """
        [Client.disassociate_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.disassociate_admin_account)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.generate_presigned_url)
        """

    def get_admin_account(self) -> GetAdminAccountResponseTypeDef:
        """
        [Client.get_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.get_admin_account)
        """

    def get_apps_list(self, ListId: str, DefaultList: bool = None) -> GetAppsListResponseTypeDef:
        """
        [Client.get_apps_list documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.get_apps_list)
        """

    def get_compliance_detail(
        self, PolicyId: str, MemberAccount: str
    ) -> GetComplianceDetailResponseTypeDef:
        """
        [Client.get_compliance_detail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.get_compliance_detail)
        """

    def get_notification_channel(self) -> GetNotificationChannelResponseTypeDef:
        """
        [Client.get_notification_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.get_notification_channel)
        """

    def get_policy(self, PolicyId: str) -> GetPolicyResponseTypeDef:
        """
        [Client.get_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.get_policy)
        """

    def get_protection_status(
        self,
        PolicyId: str,
        MemberAccountId: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetProtectionStatusResponseTypeDef:
        """
        [Client.get_protection_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.get_protection_status)
        """

    def get_protocols_list(
        self, ListId: str, DefaultList: bool = None
    ) -> GetProtocolsListResponseTypeDef:
        """
        [Client.get_protocols_list documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.get_protocols_list)
        """

    def get_violation_details(
        self, PolicyId: str, MemberAccount: str, ResourceId: str, ResourceType: str
    ) -> GetViolationDetailsResponseTypeDef:
        """
        [Client.get_violation_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.get_violation_details)
        """

    def list_apps_lists(
        self, MaxResults: int, DefaultLists: bool = None, NextToken: str = None
    ) -> ListAppsListsResponseTypeDef:
        """
        [Client.list_apps_lists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.list_apps_lists)
        """

    def list_compliance_status(
        self, PolicyId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListComplianceStatusResponseTypeDef:
        """
        [Client.list_compliance_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.list_compliance_status)
        """

    def list_member_accounts(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListMemberAccountsResponseTypeDef:
        """
        [Client.list_member_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.list_member_accounts)
        """

    def list_policies(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListPoliciesResponseTypeDef:
        """
        [Client.list_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.list_policies)
        """

    def list_protocols_lists(
        self, MaxResults: int, DefaultLists: bool = None, NextToken: str = None
    ) -> ListProtocolsListsResponseTypeDef:
        """
        [Client.list_protocols_lists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.list_protocols_lists)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.list_tags_for_resource)
        """

    def put_apps_list(
        self, AppsList: "AppsListDataTypeDef", TagList: List["TagTypeDef"] = None
    ) -> PutAppsListResponseTypeDef:
        """
        [Client.put_apps_list documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.put_apps_list)
        """

    def put_notification_channel(self, SnsTopicArn: str, SnsRoleName: str) -> None:
        """
        [Client.put_notification_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.put_notification_channel)
        """

    def put_policy(
        self, Policy: "PolicyTypeDef", TagList: List["TagTypeDef"] = None
    ) -> PutPolicyResponseTypeDef:
        """
        [Client.put_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.put_policy)
        """

    def put_protocols_list(
        self, ProtocolsList: "ProtocolsListDataTypeDef", TagList: List["TagTypeDef"] = None
    ) -> PutProtocolsListResponseTypeDef:
        """
        [Client.put_protocols_list documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.put_protocols_list)
        """

    def tag_resource(self, ResourceArn: str, TagList: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Client.untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_compliance_status"]
    ) -> ListComplianceStatusPaginator:
        """
        [Paginator.ListComplianceStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Paginator.ListComplianceStatus)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_member_accounts"]
    ) -> ListMemberAccountsPaginator:
        """
        [Paginator.ListMemberAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Paginator.ListMemberAccounts)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_policies"]) -> ListPoliciesPaginator:
        """
        [Paginator.ListPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/fms.html#FMS.Paginator.ListPolicies)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
