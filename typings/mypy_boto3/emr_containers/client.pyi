"""
Type annotations for emr-containers service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_emr_containers import EMRContainersClient

    client: EMRContainersClient = boto3.client("emr-containers")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import EndpointStateType, JobRunStateType, VirtualClusterStateType
from .paginator import (
    ListJobRunsPaginator,
    ListManagedEndpointsPaginator,
    ListVirtualClustersPaginator,
)
from .type_defs import (
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

class EMRContainersClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-containers.html#EMRContainers.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        EMRContainersClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-containers.html#EMRContainers.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#can_paginate)
        """
    def cancel_job_run(self, *, id: str, virtualClusterId: str) -> CancelJobRunResponseTypeDef:
        """
        Cancels a job run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-containers.html#EMRContainers.Client.cancel_job_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#cancel_job_run)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-containers.html#EMRContainers.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#close)
        """
    def create_managed_endpoint(
        self,
        *,
        name: str,
        virtualClusterId: str,
        type: str,
        releaseLabel: str,
        executionRoleArn: str,
        clientToken: str,
        certificateArn: str = None,
        configurationOverrides: "ConfigurationOverridesTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateManagedEndpointResponseTypeDef:
        """
        Creates a managed endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-containers.html#EMRContainers.Client.create_managed_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#create_managed_endpoint)
        """
    def create_virtual_cluster(
        self,
        *,
        name: str,
        containerProvider: "ContainerProviderTypeDef",
        clientToken: str,
        tags: Dict[str, str] = None
    ) -> CreateVirtualClusterResponseTypeDef:
        """
        Creates a virtual cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-containers.html#EMRContainers.Client.create_virtual_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#create_virtual_cluster)
        """
    def delete_managed_endpoint(
        self, *, id: str, virtualClusterId: str
    ) -> DeleteManagedEndpointResponseTypeDef:
        """
        Deletes a managed endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-containers.html#EMRContainers.Client.delete_managed_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#delete_managed_endpoint)
        """
    def delete_virtual_cluster(self, *, id: str) -> DeleteVirtualClusterResponseTypeDef:
        """
        Deletes a virtual cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-containers.html#EMRContainers.Client.delete_virtual_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#delete_virtual_cluster)
        """
    def describe_job_run(self, *, id: str, virtualClusterId: str) -> DescribeJobRunResponseTypeDef:
        """
        Displays detailed information about a job run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-containers.html#EMRContainers.Client.describe_job_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#describe_job_run)
        """
    def describe_managed_endpoint(
        self, *, id: str, virtualClusterId: str
    ) -> DescribeManagedEndpointResponseTypeDef:
        """
        Displays detailed information about a managed endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-containers.html#EMRContainers.Client.describe_managed_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#describe_managed_endpoint)
        """
    def describe_virtual_cluster(self, *, id: str) -> DescribeVirtualClusterResponseTypeDef:
        """
        Displays detailed information about a specified virtual cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-containers.html#EMRContainers.Client.describe_virtual_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#describe_virtual_cluster)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-containers.html#EMRContainers.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#generate_presigned_url)
        """
    def list_job_runs(
        self,
        *,
        virtualClusterId: str,
        createdBefore: Union[datetime, str] = None,
        createdAfter: Union[datetime, str] = None,
        name: str = None,
        states: List[JobRunStateType] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListJobRunsResponseTypeDef:
        """
        Lists job runs based on a set of parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-containers.html#EMRContainers.Client.list_job_runs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#list_job_runs)
        """
    def list_managed_endpoints(
        self,
        *,
        virtualClusterId: str,
        createdBefore: Union[datetime, str] = None,
        createdAfter: Union[datetime, str] = None,
        types: List[str] = None,
        states: List[EndpointStateType] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListManagedEndpointsResponseTypeDef:
        """
        Lists managed endpoints based on a set of parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-containers.html#EMRContainers.Client.list_managed_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#list_managed_endpoints)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags assigned to the resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-containers.html#EMRContainers.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#list_tags_for_resource)
        """
    def list_virtual_clusters(
        self,
        *,
        containerProviderId: str = None,
        containerProviderType: Literal["EKS"] = None,
        createdAfter: Union[datetime, str] = None,
        createdBefore: Union[datetime, str] = None,
        states: List[VirtualClusterStateType] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListVirtualClustersResponseTypeDef:
        """
        Lists information about the specified virtual cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-containers.html#EMRContainers.Client.list_virtual_clusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#list_virtual_clusters)
        """
    def start_job_run(
        self,
        *,
        virtualClusterId: str,
        clientToken: str,
        executionRoleArn: str,
        releaseLabel: str,
        jobDriver: "JobDriverTypeDef",
        name: str = None,
        configurationOverrides: "ConfigurationOverridesTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> StartJobRunResponseTypeDef:
        """
        Starts a job run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-containers.html#EMRContainers.Client.start_job_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#start_job_run)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Assigns tags to resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-containers.html#EMRContainers.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-containers.html#EMRContainers.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#untag_resource)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_job_runs"]) -> ListJobRunsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-containers.html#EMRContainers.Paginator.ListJobRuns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators.html#listjobrunspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_managed_endpoints"]
    ) -> ListManagedEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-containers.html#EMRContainers.Paginator.ListManagedEndpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators.html#listmanagedendpointspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_virtual_clusters"]
    ) -> ListVirtualClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-containers.html#EMRContainers.Paginator.ListVirtualClusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators.html#listvirtualclusterspaginator)
        """
