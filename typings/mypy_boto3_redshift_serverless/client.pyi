"""
Type annotations for redshift-serverless service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_redshift_serverless import RedshiftServerlessClient

    client: RedshiftServerlessClient = boto3.client("redshift-serverless")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    LogExportType,
    UsageLimitBreachActionType,
    UsageLimitPeriodType,
    UsageLimitUsageTypeType,
)
from .paginator import (
    ListEndpointAccessPaginator,
    ListNamespacesPaginator,
    ListRecoveryPointsPaginator,
    ListSnapshotsPaginator,
    ListUsageLimitsPaginator,
    ListWorkgroupsPaginator,
)
from .type_defs import (
    ConfigParameterTypeDef,
    ConvertRecoveryPointToSnapshotResponseTypeDef,
    CreateEndpointAccessResponseTypeDef,
    CreateNamespaceResponseTypeDef,
    CreateSnapshotResponseTypeDef,
    CreateUsageLimitResponseTypeDef,
    CreateWorkgroupResponseTypeDef,
    DeleteEndpointAccessResponseTypeDef,
    DeleteNamespaceResponseTypeDef,
    DeleteSnapshotResponseTypeDef,
    DeleteUsageLimitResponseTypeDef,
    DeleteWorkgroupResponseTypeDef,
    GetCredentialsResponseTypeDef,
    GetEndpointAccessResponseTypeDef,
    GetNamespaceResponseTypeDef,
    GetRecoveryPointResponseTypeDef,
    GetResourcePolicyResponseTypeDef,
    GetSnapshotResponseTypeDef,
    GetUsageLimitResponseTypeDef,
    GetWorkgroupResponseTypeDef,
    ListEndpointAccessResponseTypeDef,
    ListNamespacesResponseTypeDef,
    ListRecoveryPointsResponseTypeDef,
    ListSnapshotsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUsageLimitsResponseTypeDef,
    ListWorkgroupsResponseTypeDef,
    PutResourcePolicyResponseTypeDef,
    RestoreFromRecoveryPointResponseTypeDef,
    RestoreFromSnapshotResponseTypeDef,
    TagTypeDef,
    UpdateEndpointAccessResponseTypeDef,
    UpdateNamespaceResponseTypeDef,
    UpdateSnapshotResponseTypeDef,
    UpdateUsageLimitResponseTypeDef,
    UpdateWorkgroupResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("RedshiftServerlessClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InsufficientCapacityException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidPaginationException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class RedshiftServerlessClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        RedshiftServerlessClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#close)
        """
    def convert_recovery_point_to_snapshot(
        self, *, recoveryPointId: str, snapshotName: str, retentionPeriod: int = None
    ) -> ConvertRecoveryPointToSnapshotResponseTypeDef:
        """
        Converts a recovery point to a snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.convert_recovery_point_to_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#convert_recovery_point_to_snapshot)
        """
    def create_endpoint_access(
        self,
        *,
        endpointName: str,
        subnetIds: List[str],
        workgroupName: str,
        vpcSecurityGroupIds: List[str] = None
    ) -> CreateEndpointAccessResponseTypeDef:
        """
        Creates an Amazon Redshift Serverless managed VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.create_endpoint_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#create_endpoint_access)
        """
    def create_namespace(
        self,
        *,
        namespaceName: str,
        adminUserPassword: str = None,
        adminUsername: str = None,
        dbName: str = None,
        defaultIamRoleArn: str = None,
        iamRoles: List[str] = None,
        kmsKeyId: str = None,
        logExports: List[LogExportType] = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateNamespaceResponseTypeDef:
        """
        Creates a namespace in Amazon Redshift Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.create_namespace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#create_namespace)
        """
    def create_snapshot(
        self, *, namespaceName: str, snapshotName: str, retentionPeriod: int = None
    ) -> CreateSnapshotResponseTypeDef:
        """
        Creates a snapshot of all databases in a namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.create_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#create_snapshot)
        """
    def create_usage_limit(
        self,
        *,
        amount: int,
        resourceArn: str,
        usageType: UsageLimitUsageTypeType,
        breachAction: UsageLimitBreachActionType = None,
        period: UsageLimitPeriodType = None
    ) -> CreateUsageLimitResponseTypeDef:
        """
        Creates a usage limit for a specified Amazon Redshift Serverless usage type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.create_usage_limit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#create_usage_limit)
        """
    def create_workgroup(
        self,
        *,
        namespaceName: str,
        workgroupName: str,
        baseCapacity: int = None,
        configParameters: List["ConfigParameterTypeDef"] = None,
        enhancedVpcRouting: bool = None,
        publiclyAccessible: bool = None,
        securityGroupIds: List[str] = None,
        subnetIds: List[str] = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateWorkgroupResponseTypeDef:
        """
        Creates an workgroup in Amazon Redshift Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.create_workgroup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#create_workgroup)
        """
    def delete_endpoint_access(self, *, endpointName: str) -> DeleteEndpointAccessResponseTypeDef:
        """
        Deletes an Amazon Redshift Serverless managed VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.delete_endpoint_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#delete_endpoint_access)
        """
    def delete_namespace(
        self,
        *,
        namespaceName: str,
        finalSnapshotName: str = None,
        finalSnapshotRetentionPeriod: int = None
    ) -> DeleteNamespaceResponseTypeDef:
        """
        Deletes a namespace from Amazon Redshift Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.delete_namespace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#delete_namespace)
        """
    def delete_resource_policy(self, *, resourceArn: str) -> Dict[str, Any]:
        """
        Deletes the specified resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#delete_resource_policy)
        """
    def delete_snapshot(self, *, snapshotName: str) -> DeleteSnapshotResponseTypeDef:
        """
        Deletes a snapshot from Amazon Redshift Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.delete_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#delete_snapshot)
        """
    def delete_usage_limit(self, *, usageLimitId: str) -> DeleteUsageLimitResponseTypeDef:
        """
        Deletes a usage limit from Amazon Redshift Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.delete_usage_limit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#delete_usage_limit)
        """
    def delete_workgroup(self, *, workgroupName: str) -> DeleteWorkgroupResponseTypeDef:
        """
        Deletes a workgroup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.delete_workgroup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#delete_workgroup)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#generate_presigned_url)
        """
    def get_credentials(
        self, *, workgroupName: str, dbName: str = None, durationSeconds: int = None
    ) -> GetCredentialsResponseTypeDef:
        """
        Returns a database user name and temporary password with temporary authorization
        to log in to Amazon Redshift Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.get_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#get_credentials)
        """
    def get_endpoint_access(self, *, endpointName: str) -> GetEndpointAccessResponseTypeDef:
        """
        Returns information, such as the name, about a VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.get_endpoint_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#get_endpoint_access)
        """
    def get_namespace(self, *, namespaceName: str) -> GetNamespaceResponseTypeDef:
        """
        Returns information about a namespace in Amazon Redshift Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.get_namespace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#get_namespace)
        """
    def get_recovery_point(self, *, recoveryPointId: str) -> GetRecoveryPointResponseTypeDef:
        """
        Returns information about a recovery point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.get_recovery_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#get_recovery_point)
        """
    def get_resource_policy(self, *, resourceArn: str) -> GetResourcePolicyResponseTypeDef:
        """
        Returns a resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.get_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#get_resource_policy)
        """
    def get_snapshot(
        self, *, ownerAccount: str = None, snapshotArn: str = None, snapshotName: str = None
    ) -> GetSnapshotResponseTypeDef:
        """
        Returns information about a specific snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.get_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#get_snapshot)
        """
    def get_usage_limit(self, *, usageLimitId: str) -> GetUsageLimitResponseTypeDef:
        """
        Returns information about a usage limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.get_usage_limit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#get_usage_limit)
        """
    def get_workgroup(self, *, workgroupName: str) -> GetWorkgroupResponseTypeDef:
        """
        Returns information about a specific workgroup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.get_workgroup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#get_workgroup)
        """
    def list_endpoint_access(
        self,
        *,
        maxResults: int = None,
        nextToken: str = None,
        vpcId: str = None,
        workgroupName: str = None
    ) -> ListEndpointAccessResponseTypeDef:
        """
        Returns an array of `EndpointAccess` objects and relevant information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.list_endpoint_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#list_endpoint_access)
        """
    def list_namespaces(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListNamespacesResponseTypeDef:
        """
        Returns information about a list of specified namespaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.list_namespaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#list_namespaces)
        """
    def list_recovery_points(
        self,
        *,
        endTime: Union[datetime, str] = None,
        maxResults: int = None,
        namespaceName: str = None,
        nextToken: str = None,
        startTime: Union[datetime, str] = None
    ) -> ListRecoveryPointsResponseTypeDef:
        """
        Returns an array of recovery points.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.list_recovery_points)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#list_recovery_points)
        """
    def list_snapshots(
        self,
        *,
        endTime: Union[datetime, str] = None,
        maxResults: int = None,
        namespaceArn: str = None,
        namespaceName: str = None,
        nextToken: str = None,
        ownerAccount: str = None,
        startTime: Union[datetime, str] = None
    ) -> ListSnapshotsResponseTypeDef:
        """
        Returns a list of snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.list_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#list_snapshots)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags assigned to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#list_tags_for_resource)
        """
    def list_usage_limits(
        self,
        *,
        maxResults: int = None,
        nextToken: str = None,
        resourceArn: str = None,
        usageType: UsageLimitUsageTypeType = None
    ) -> ListUsageLimitsResponseTypeDef:
        """
        Lists all usage limits within Amazon Redshift Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.list_usage_limits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#list_usage_limits)
        """
    def list_workgroups(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListWorkgroupsResponseTypeDef:
        """
        Returns information about a list of specified workgroups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.list_workgroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#list_workgroups)
        """
    def put_resource_policy(
        self, *, policy: str, resourceArn: str
    ) -> PutResourcePolicyResponseTypeDef:
        """
        Creates or updates a resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#put_resource_policy)
        """
    def restore_from_recovery_point(
        self, *, namespaceName: str, recoveryPointId: str, workgroupName: str
    ) -> RestoreFromRecoveryPointResponseTypeDef:
        """
        Restore the data from a recovery point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.restore_from_recovery_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#restore_from_recovery_point)
        """
    def restore_from_snapshot(
        self,
        *,
        namespaceName: str,
        workgroupName: str,
        ownerAccount: str = None,
        snapshotArn: str = None,
        snapshotName: str = None
    ) -> RestoreFromSnapshotResponseTypeDef:
        """
        Restores a namespace from a snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.restore_from_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#restore_from_snapshot)
        """
    def tag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Assigns one or more tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag or set of tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#untag_resource)
        """
    def update_endpoint_access(
        self, *, endpointName: str, vpcSecurityGroupIds: List[str] = None
    ) -> UpdateEndpointAccessResponseTypeDef:
        """
        Updates an Amazon Redshift Serverless managed endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.update_endpoint_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#update_endpoint_access)
        """
    def update_namespace(
        self,
        *,
        namespaceName: str,
        adminUserPassword: str = None,
        adminUsername: str = None,
        defaultIamRoleArn: str = None,
        iamRoles: List[str] = None,
        kmsKeyId: str = None,
        logExports: List[LogExportType] = None
    ) -> UpdateNamespaceResponseTypeDef:
        """
        Updates a namespace with the specified settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.update_namespace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#update_namespace)
        """
    def update_snapshot(
        self, *, snapshotName: str, retentionPeriod: int = None
    ) -> UpdateSnapshotResponseTypeDef:
        """
        Updates a snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.update_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#update_snapshot)
        """
    def update_usage_limit(
        self,
        *,
        usageLimitId: str,
        amount: int = None,
        breachAction: UsageLimitBreachActionType = None
    ) -> UpdateUsageLimitResponseTypeDef:
        """
        Update a usage limit in Amazon Redshift Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.update_usage_limit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#update_usage_limit)
        """
    def update_workgroup(
        self,
        *,
        workgroupName: str,
        baseCapacity: int = None,
        configParameters: List["ConfigParameterTypeDef"] = None,
        enhancedVpcRouting: bool = None,
        publiclyAccessible: bool = None,
        securityGroupIds: List[str] = None,
        subnetIds: List[str] = None
    ) -> UpdateWorkgroupResponseTypeDef:
        """
        Updates a workgroup with the specified configuration settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Client.update_workgroup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/client.html#update_workgroup)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_endpoint_access"]
    ) -> ListEndpointAccessPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListEndpointAccess)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators.html#listendpointaccesspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_namespaces"]) -> ListNamespacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListNamespaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators.html#listnamespacespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_recovery_points"]
    ) -> ListRecoveryPointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListRecoveryPoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators.html#listrecoverypointspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_snapshots"]) -> ListSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListSnapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators.html#listsnapshotspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_usage_limits"]
    ) -> ListUsageLimitsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListUsageLimits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators.html#listusagelimitspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_workgroups"]) -> ListWorkgroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-serverless.html#RedshiftServerless.Paginator.ListWorkgroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/paginators.html#listworkgroupspaginator)
        """
