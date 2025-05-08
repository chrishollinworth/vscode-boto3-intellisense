"""
Type annotations for launch-wizard service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_launch_wizard.client import LaunchWizardClient

    session = Session()
    client: LaunchWizardClient = session.client("launch-wizard")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListDeploymentEventsPaginator,
    ListDeploymentsPaginator,
    ListWorkloadDeploymentPatternsPaginator,
    ListWorkloadsPaginator,
)
from .type_defs import (
    CreateDeploymentInputTypeDef,
    CreateDeploymentOutputTypeDef,
    DeleteDeploymentInputTypeDef,
    DeleteDeploymentOutputTypeDef,
    GetDeploymentInputTypeDef,
    GetDeploymentOutputTypeDef,
    GetWorkloadDeploymentPatternInputTypeDef,
    GetWorkloadDeploymentPatternOutputTypeDef,
    GetWorkloadInputTypeDef,
    GetWorkloadOutputTypeDef,
    ListDeploymentEventsInputTypeDef,
    ListDeploymentEventsOutputTypeDef,
    ListDeploymentsInputTypeDef,
    ListDeploymentsOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListWorkloadDeploymentPatternsInputTypeDef,
    ListWorkloadDeploymentPatternsOutputTypeDef,
    ListWorkloadsInputTypeDef,
    ListWorkloadsOutputTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
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

__all__ = ("LaunchWizardClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceLimitException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class LaunchWizardClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LaunchWizardClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard.html#LaunchWizard.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client/#generate_presigned_url)
        """

    def create_deployment(
        self, **kwargs: Unpack[CreateDeploymentInputTypeDef]
    ) -> CreateDeploymentOutputTypeDef:
        """
        Creates a deployment for the given workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/client/create_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client/#create_deployment)
        """

    def delete_deployment(
        self, **kwargs: Unpack[DeleteDeploymentInputTypeDef]
    ) -> DeleteDeploymentOutputTypeDef:
        """
        Deletes a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/client/delete_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client/#delete_deployment)
        """

    def get_deployment(
        self, **kwargs: Unpack[GetDeploymentInputTypeDef]
    ) -> GetDeploymentOutputTypeDef:
        """
        Returns information about the deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/client/get_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client/#get_deployment)
        """

    def get_workload(self, **kwargs: Unpack[GetWorkloadInputTypeDef]) -> GetWorkloadOutputTypeDef:
        """
        Returns information about a workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/client/get_workload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client/#get_workload)
        """

    def get_workload_deployment_pattern(
        self, **kwargs: Unpack[GetWorkloadDeploymentPatternInputTypeDef]
    ) -> GetWorkloadDeploymentPatternOutputTypeDef:
        """
        Returns details for a given workload and deployment pattern, including the
        available specifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/client/get_workload_deployment_pattern.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client/#get_workload_deployment_pattern)
        """

    def list_deployment_events(
        self, **kwargs: Unpack[ListDeploymentEventsInputTypeDef]
    ) -> ListDeploymentEventsOutputTypeDef:
        """
        Lists the events of a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/client/list_deployment_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client/#list_deployment_events)
        """

    def list_deployments(
        self, **kwargs: Unpack[ListDeploymentsInputTypeDef]
    ) -> ListDeploymentsOutputTypeDef:
        """
        Lists the deployments that have been created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/client/list_deployments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client/#list_deployments)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Lists the tags associated with a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client/#list_tags_for_resource)
        """

    def list_workload_deployment_patterns(
        self, **kwargs: Unpack[ListWorkloadDeploymentPatternsInputTypeDef]
    ) -> ListWorkloadDeploymentPatternsOutputTypeDef:
        """
        Lists the workload deployment patterns for a given workload name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/client/list_workload_deployment_patterns.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client/#list_workload_deployment_patterns)
        """

    def list_workloads(
        self, **kwargs: Unpack[ListWorkloadsInputTypeDef]
    ) -> ListWorkloadsOutputTypeDef:
        """
        Lists the available workload names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/client/list_workloads.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client/#list_workloads)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Adds the specified tags to the given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified tags from the given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client/#untag_resource)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_deployment_events"]
    ) -> ListDeploymentEventsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_deployments"]
    ) -> ListDeploymentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workload_deployment_patterns"]
    ) -> ListWorkloadDeploymentPatternsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workloads"]
    ) -> ListWorkloadsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/launch-wizard/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client/#get_paginator)
        """
