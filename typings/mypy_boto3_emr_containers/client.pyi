"""
Main interface for emr-containers service client

Usage::

    ```python
    import boto3
    from mypy_boto3_emr_containers import EMRContainersClient

    client: EMRContainersClient = boto3.client("emr-containers")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_emr_containers.paginator import (
    ListJobRunsPaginator,
    ListManagedEndpointsPaginator,
    ListVirtualClustersPaginator,
)
from mypy_boto3_emr_containers.type_defs import (
    CancelJobRunResponseTypeDef,
    ConfigurationOverridesTypeDef,
    ContainerProviderTypeDef,
    CreateManagedEndpointResponseTypeDef,
    CreateVirtualClusterResponseTypeDef,
    DeleteManagedEndpointResponseTypeDef,
    DeleteVirtualClusterResponseTypeDef,
    DescribeJobRunResponseTypeDef,
    DescribeManagedEndpointResponseTypeDef,
    DescribeVirtualClusterResponseTypeDef,
    JobDriverTypeDef,
    ListJobRunsResponseTypeDef,
    ListManagedEndpointsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListVirtualClustersResponseTypeDef,
    StartJobRunResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("EMRContainersClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class EMRContainersClient:
    """
    [EMRContainers.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Client.can_paginate)
        """

    def cancel_job_run(self, id: str, virtualClusterId: str) -> CancelJobRunResponseTypeDef:
        """
        [Client.cancel_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Client.cancel_job_run)
        """

    def create_managed_endpoint(
        self,
        name: str,
        virtualClusterId: str,
        type: str,
        releaseLabel: str,
        executionRoleArn: str,
        certificateArn: str,
        clientToken: str,
        configurationOverrides: "ConfigurationOverridesTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> CreateManagedEndpointResponseTypeDef:
        """
        [Client.create_managed_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Client.create_managed_endpoint)
        """

    def create_virtual_cluster(
        self,
        name: str,
        containerProvider: "ContainerProviderTypeDef",
        clientToken: str,
        tags: Dict[str, str] = None,
    ) -> CreateVirtualClusterResponseTypeDef:
        """
        [Client.create_virtual_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Client.create_virtual_cluster)
        """

    def delete_managed_endpoint(
        self, id: str, virtualClusterId: str
    ) -> DeleteManagedEndpointResponseTypeDef:
        """
        [Client.delete_managed_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Client.delete_managed_endpoint)
        """

    def delete_virtual_cluster(self, id: str) -> DeleteVirtualClusterResponseTypeDef:
        """
        [Client.delete_virtual_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Client.delete_virtual_cluster)
        """

    def describe_job_run(self, id: str, virtualClusterId: str) -> DescribeJobRunResponseTypeDef:
        """
        [Client.describe_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Client.describe_job_run)
        """

    def describe_managed_endpoint(
        self, id: str, virtualClusterId: str
    ) -> DescribeManagedEndpointResponseTypeDef:
        """
        [Client.describe_managed_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Client.describe_managed_endpoint)
        """

    def describe_virtual_cluster(self, id: str) -> DescribeVirtualClusterResponseTypeDef:
        """
        [Client.describe_virtual_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Client.describe_virtual_cluster)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Client.generate_presigned_url)
        """

    def list_job_runs(
        self,
        virtualClusterId: str,
        createdBefore: datetime = None,
        createdAfter: datetime = None,
        name: str = None,
        states: List[
            Literal[
                "PENDING",
                "SUBMITTED",
                "RUNNING",
                "FAILED",
                "CANCELLED",
                "CANCEL_PENDING",
                "COMPLETED",
            ]
        ] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListJobRunsResponseTypeDef:
        """
        [Client.list_job_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Client.list_job_runs)
        """

    def list_managed_endpoints(
        self,
        virtualClusterId: str,
        createdBefore: datetime = None,
        createdAfter: datetime = None,
        types: List[str] = None,
        states: List[
            Literal["CREATING", "ACTIVE", "TERMINATING", "TERMINATED", "TERMINATED_WITH_ERRORS"]
        ] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListManagedEndpointsResponseTypeDef:
        """
        [Client.list_managed_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Client.list_managed_endpoints)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Client.list_tags_for_resource)
        """

    def list_virtual_clusters(
        self,
        containerProviderId: str = None,
        containerProviderType: Literal["EKS"] = None,
        createdAfter: datetime = None,
        createdBefore: datetime = None,
        states: List[Literal["RUNNING", "TERMINATING", "TERMINATED", "ARRESTED"]] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListVirtualClustersResponseTypeDef:
        """
        [Client.list_virtual_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Client.list_virtual_clusters)
        """

    def start_job_run(
        self,
        virtualClusterId: str,
        clientToken: str,
        executionRoleArn: str,
        releaseLabel: str,
        jobDriver: "JobDriverTypeDef",
        name: str = None,
        configurationOverrides: "ConfigurationOverridesTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> StartJobRunResponseTypeDef:
        """
        [Client.start_job_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Client.start_job_run)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Client.untag_resource)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_job_runs"]) -> ListJobRunsPaginator:
        """
        [Paginator.ListJobRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Paginator.ListJobRuns)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_managed_endpoints"]
    ) -> ListManagedEndpointsPaginator:
        """
        [Paginator.ListManagedEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Paginator.ListManagedEndpoints)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_virtual_clusters"]
    ) -> ListVirtualClustersPaginator:
        """
        [Paginator.ListVirtualClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Paginator.ListVirtualClusters)
        """
