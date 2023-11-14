"""
Type annotations for launch-wizard service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_launch_wizard import LaunchWizardClient

    client: LaunchWizardClient = boto3.client("launch-wizard")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListDeploymentEventsPaginator,
    ListDeploymentsPaginator,
    ListWorkloadDeploymentPatternsPaginator,
    ListWorkloadsPaginator,
)
from .type_defs import (
    CreateDeploymentOutputTypeDef,
    DeleteDeploymentOutputTypeDef,
    DeploymentFilterTypeDef,
    GetDeploymentOutputTypeDef,
    GetWorkloadOutputTypeDef,
    ListDeploymentEventsOutputTypeDef,
    ListDeploymentsOutputTypeDef,
    ListWorkloadDeploymentPatternsOutputTypeDef,
    ListWorkloadsOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("LaunchWizardClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceLimitException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class LaunchWizardClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/launch-wizard.html#LaunchWizard.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LaunchWizardClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/launch-wizard.html#LaunchWizard.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/launch-wizard.html#LaunchWizard.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client.html#close)
        """
    def create_deployment(
        self,
        *,
        deploymentPatternName: str,
        name: str,
        specifications: Dict[str, str],
        workloadName: str,
        dryRun: bool = None
    ) -> CreateDeploymentOutputTypeDef:
        """
        Creates a deployment for the given workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/launch-wizard.html#LaunchWizard.Client.create_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client.html#create_deployment)
        """
    def delete_deployment(self, *, deploymentId: str) -> DeleteDeploymentOutputTypeDef:
        """
        Deletes a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/launch-wizard.html#LaunchWizard.Client.delete_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client.html#delete_deployment)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/launch-wizard.html#LaunchWizard.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client.html#generate_presigned_url)
        """
    def get_deployment(self, *, deploymentId: str) -> GetDeploymentOutputTypeDef:
        """
        Returns information about the deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/launch-wizard.html#LaunchWizard.Client.get_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client.html#get_deployment)
        """
    def get_workload(self, *, workloadName: str) -> GetWorkloadOutputTypeDef:
        """
        Returns information about a workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/launch-wizard.html#LaunchWizard.Client.get_workload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client.html#get_workload)
        """
    def list_deployment_events(
        self, *, deploymentId: str, maxResults: int = None, nextToken: str = None
    ) -> ListDeploymentEventsOutputTypeDef:
        """
        Lists the events of a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/launch-wizard.html#LaunchWizard.Client.list_deployment_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client.html#list_deployment_events)
        """
    def list_deployments(
        self,
        *,
        filters: List["DeploymentFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListDeploymentsOutputTypeDef:
        """
        Lists the deployments that have been created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/launch-wizard.html#LaunchWizard.Client.list_deployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client.html#list_deployments)
        """
    def list_workload_deployment_patterns(
        self, *, workloadName: str, maxResults: int = None, nextToken: str = None
    ) -> ListWorkloadDeploymentPatternsOutputTypeDef:
        """
        Lists the workload deployment patterns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/launch-wizard.html#LaunchWizard.Client.list_workload_deployment_patterns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client.html#list_workload_deployment_patterns)
        """
    def list_workloads(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListWorkloadsOutputTypeDef:
        """
        Lists the workloads.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/launch-wizard.html#LaunchWizard.Client.list_workloads)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/client.html#list_workloads)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployment_events"]
    ) -> ListDeploymentEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/launch-wizard.html#LaunchWizard.Paginator.ListDeploymentEvents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/paginators.html#listdeploymenteventspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployments"]
    ) -> ListDeploymentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/launch-wizard.html#LaunchWizard.Paginator.ListDeployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/paginators.html#listdeploymentspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_workload_deployment_patterns"]
    ) -> ListWorkloadDeploymentPatternsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/launch-wizard.html#LaunchWizard.Paginator.ListWorkloadDeploymentPatterns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/paginators.html#listworkloaddeploymentpatternspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_workloads"]) -> ListWorkloadsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/launch-wizard.html#LaunchWizard.Paginator.ListWorkloads)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_launch_wizard/paginators.html#listworkloadspaginator)
        """
