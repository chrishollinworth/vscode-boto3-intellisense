"""
Type annotations for emr-containers service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_emr_containers.client import EMRContainersClient

    session = Session()
    client: EMRContainersClient = session.client("emr-containers")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListJobRunsPaginator,
    ListJobTemplatesPaginator,
    ListManagedEndpointsPaginator,
    ListSecurityConfigurationsPaginator,
    ListVirtualClustersPaginator,
)
from .type_defs import (
    CancelJobRunRequestTypeDef,
    CancelJobRunResponseTypeDef,
    CreateJobTemplateRequestTypeDef,
    CreateJobTemplateResponseTypeDef,
    CreateManagedEndpointRequestTypeDef,
    CreateManagedEndpointResponseTypeDef,
    CreateSecurityConfigurationRequestTypeDef,
    CreateSecurityConfigurationResponseTypeDef,
    CreateVirtualClusterRequestTypeDef,
    CreateVirtualClusterResponseTypeDef,
    DeleteJobTemplateRequestTypeDef,
    DeleteJobTemplateResponseTypeDef,
    DeleteManagedEndpointRequestTypeDef,
    DeleteManagedEndpointResponseTypeDef,
    DeleteVirtualClusterRequestTypeDef,
    DeleteVirtualClusterResponseTypeDef,
    DescribeJobRunRequestTypeDef,
    DescribeJobRunResponseTypeDef,
    DescribeJobTemplateRequestTypeDef,
    DescribeJobTemplateResponseTypeDef,
    DescribeManagedEndpointRequestTypeDef,
    DescribeManagedEndpointResponseTypeDef,
    DescribeSecurityConfigurationRequestTypeDef,
    DescribeSecurityConfigurationResponseTypeDef,
    DescribeVirtualClusterRequestTypeDef,
    DescribeVirtualClusterResponseTypeDef,
    GetManagedEndpointSessionCredentialsRequestTypeDef,
    GetManagedEndpointSessionCredentialsResponseTypeDef,
    ListJobRunsRequestTypeDef,
    ListJobRunsResponseTypeDef,
    ListJobTemplatesRequestTypeDef,
    ListJobTemplatesResponseTypeDef,
    ListManagedEndpointsRequestTypeDef,
    ListManagedEndpointsResponseTypeDef,
    ListSecurityConfigurationsRequestTypeDef,
    ListSecurityConfigurationsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListVirtualClustersRequestTypeDef,
    ListVirtualClustersResponseTypeDef,
    StartJobRunRequestTypeDef,
    StartJobRunResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
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

__all__ = ("EMRContainersClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    EKSRequestThrottledException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    RequestThrottledException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class EMRContainersClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        EMRContainersClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers.html#EMRContainers.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#generate_presigned_url)
        """

    def cancel_job_run(
        self, **kwargs: Unpack[CancelJobRunRequestTypeDef]
    ) -> CancelJobRunResponseTypeDef:
        """
        Cancels a job run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/cancel_job_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#cancel_job_run)
        """

    def create_job_template(
        self, **kwargs: Unpack[CreateJobTemplateRequestTypeDef]
    ) -> CreateJobTemplateResponseTypeDef:
        """
        Creates a job template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/create_job_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#create_job_template)
        """

    def create_managed_endpoint(
        self, **kwargs: Unpack[CreateManagedEndpointRequestTypeDef]
    ) -> CreateManagedEndpointResponseTypeDef:
        """
        Creates a managed endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/create_managed_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#create_managed_endpoint)
        """

    def create_security_configuration(
        self, **kwargs: Unpack[CreateSecurityConfigurationRequestTypeDef]
    ) -> CreateSecurityConfigurationResponseTypeDef:
        """
        Creates a security configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/create_security_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#create_security_configuration)
        """

    def create_virtual_cluster(
        self, **kwargs: Unpack[CreateVirtualClusterRequestTypeDef]
    ) -> CreateVirtualClusterResponseTypeDef:
        """
        Creates a virtual cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/create_virtual_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#create_virtual_cluster)
        """

    def delete_job_template(
        self, **kwargs: Unpack[DeleteJobTemplateRequestTypeDef]
    ) -> DeleteJobTemplateResponseTypeDef:
        """
        Deletes a job template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/delete_job_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#delete_job_template)
        """

    def delete_managed_endpoint(
        self, **kwargs: Unpack[DeleteManagedEndpointRequestTypeDef]
    ) -> DeleteManagedEndpointResponseTypeDef:
        """
        Deletes a managed endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/delete_managed_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#delete_managed_endpoint)
        """

    def delete_virtual_cluster(
        self, **kwargs: Unpack[DeleteVirtualClusterRequestTypeDef]
    ) -> DeleteVirtualClusterResponseTypeDef:
        """
        Deletes a virtual cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/delete_virtual_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#delete_virtual_cluster)
        """

    def describe_job_run(
        self, **kwargs: Unpack[DescribeJobRunRequestTypeDef]
    ) -> DescribeJobRunResponseTypeDef:
        """
        Displays detailed information about a job run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/describe_job_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#describe_job_run)
        """

    def describe_job_template(
        self, **kwargs: Unpack[DescribeJobTemplateRequestTypeDef]
    ) -> DescribeJobTemplateResponseTypeDef:
        """
        Displays detailed information about a specified job template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/describe_job_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#describe_job_template)
        """

    def describe_managed_endpoint(
        self, **kwargs: Unpack[DescribeManagedEndpointRequestTypeDef]
    ) -> DescribeManagedEndpointResponseTypeDef:
        """
        Displays detailed information about a managed endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/describe_managed_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#describe_managed_endpoint)
        """

    def describe_security_configuration(
        self, **kwargs: Unpack[DescribeSecurityConfigurationRequestTypeDef]
    ) -> DescribeSecurityConfigurationResponseTypeDef:
        """
        Displays detailed information about a specified security configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/describe_security_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#describe_security_configuration)
        """

    def describe_virtual_cluster(
        self, **kwargs: Unpack[DescribeVirtualClusterRequestTypeDef]
    ) -> DescribeVirtualClusterResponseTypeDef:
        """
        Displays detailed information about a specified virtual cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/describe_virtual_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#describe_virtual_cluster)
        """

    def get_managed_endpoint_session_credentials(
        self, **kwargs: Unpack[GetManagedEndpointSessionCredentialsRequestTypeDef]
    ) -> GetManagedEndpointSessionCredentialsResponseTypeDef:
        """
        Generate a session token to connect to a managed endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/get_managed_endpoint_session_credentials.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#get_managed_endpoint_session_credentials)
        """

    def list_job_runs(
        self, **kwargs: Unpack[ListJobRunsRequestTypeDef]
    ) -> ListJobRunsResponseTypeDef:
        """
        Lists job runs based on a set of parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/list_job_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#list_job_runs)
        """

    def list_job_templates(
        self, **kwargs: Unpack[ListJobTemplatesRequestTypeDef]
    ) -> ListJobTemplatesResponseTypeDef:
        """
        Lists job templates based on a set of parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/list_job_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#list_job_templates)
        """

    def list_managed_endpoints(
        self, **kwargs: Unpack[ListManagedEndpointsRequestTypeDef]
    ) -> ListManagedEndpointsResponseTypeDef:
        """
        Lists managed endpoints based on a set of parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/list_managed_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#list_managed_endpoints)
        """

    def list_security_configurations(
        self, **kwargs: Unpack[ListSecurityConfigurationsRequestTypeDef]
    ) -> ListSecurityConfigurationsResponseTypeDef:
        """
        Lists security configurations based on a set of parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/list_security_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#list_security_configurations)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags assigned to the resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#list_tags_for_resource)
        """

    def list_virtual_clusters(
        self, **kwargs: Unpack[ListVirtualClustersRequestTypeDef]
    ) -> ListVirtualClustersResponseTypeDef:
        """
        Lists information about the specified virtual cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/list_virtual_clusters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#list_virtual_clusters)
        """

    def start_job_run(
        self, **kwargs: Unpack[StartJobRunRequestTypeDef]
    ) -> StartJobRunResponseTypeDef:
        """
        Starts a job run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/start_job_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#start_job_run)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Assigns tags to resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#untag_resource)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_job_runs"]
    ) -> ListJobRunsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_job_templates"]
    ) -> ListJobTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_managed_endpoints"]
    ) -> ListManagedEndpointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_security_configurations"]
    ) -> ListSecurityConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_virtual_clusters"]
    ) -> ListVirtualClustersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client/#get_paginator)
        """
