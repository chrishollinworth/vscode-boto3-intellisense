"""
Main interface for greengrassv2 service client

Usage::

    ```python
    import boto3
    from mypy_boto3_greengrassv2 import GreengrassV2Client

    client: GreengrassV2Client = boto3.client("greengrassv2")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import ClientMeta

from mypy_boto3_greengrassv2.paginator import (
    ListComponentsPaginator,
    ListComponentVersionsPaginator,
    ListCoreDevicesPaginator,
    ListDeploymentsPaginator,
    ListEffectiveDeploymentsPaginator,
    ListInstalledComponentsPaginator,
)
from mypy_boto3_greengrassv2.type_defs import (
    CancelDeploymentResponseTypeDef,
    ComponentCandidateTypeDef,
    ComponentDeploymentSpecificationTypeDef,
    ComponentPlatformTypeDef,
    CreateComponentVersionResponseTypeDef,
    CreateDeploymentResponseTypeDef,
    DeploymentIoTJobConfigurationTypeDef,
    DeploymentPoliciesTypeDef,
    DescribeComponentResponseTypeDef,
    GetComponentResponseTypeDef,
    GetComponentVersionArtifactResponseTypeDef,
    GetCoreDeviceResponseTypeDef,
    GetDeploymentResponseTypeDef,
    LambdaFunctionRecipeSourceTypeDef,
    ListComponentsResponseTypeDef,
    ListComponentVersionsResponseTypeDef,
    ListCoreDevicesResponseTypeDef,
    ListDeploymentsResponseTypeDef,
    ListEffectiveDeploymentsResponseTypeDef,
    ListInstalledComponentsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ResolveComponentCandidatesResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GreengrassV2Client",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class GreengrassV2Client:
    """
    [GreengrassV2.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Client.can_paginate)
        """

    def cancel_deployment(self, deploymentId: str) -> CancelDeploymentResponseTypeDef:
        """
        [Client.cancel_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Client.cancel_deployment)
        """

    def create_component_version(
        self,
        inlineRecipe: Union[bytes, IO[bytes]] = None,
        lambdaFunction: LambdaFunctionRecipeSourceTypeDef = None,
        tags: Dict[str, str] = None,
    ) -> CreateComponentVersionResponseTypeDef:
        """
        [Client.create_component_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Client.create_component_version)
        """

    def create_deployment(
        self,
        targetArn: str,
        deploymentName: str = None,
        components: Dict[str, "ComponentDeploymentSpecificationTypeDef"] = None,
        iotJobConfiguration: "DeploymentIoTJobConfigurationTypeDef" = None,
        deploymentPolicies: "DeploymentPoliciesTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> CreateDeploymentResponseTypeDef:
        """
        [Client.create_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Client.create_deployment)
        """

    def delete_component(self, arn: str) -> None:
        """
        [Client.delete_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Client.delete_component)
        """

    def delete_core_device(self, coreDeviceThingName: str) -> None:
        """
        [Client.delete_core_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Client.delete_core_device)
        """

    def describe_component(self, arn: str) -> DescribeComponentResponseTypeDef:
        """
        [Client.describe_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Client.describe_component)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Client.generate_presigned_url)
        """

    def get_component(
        self, arn: str, recipeOutputFormat: Literal["JSON", "YAML"] = None
    ) -> GetComponentResponseTypeDef:
        """
        [Client.get_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Client.get_component)
        """

    def get_component_version_artifact(
        self, arn: str, artifactName: str
    ) -> GetComponentVersionArtifactResponseTypeDef:
        """
        [Client.get_component_version_artifact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Client.get_component_version_artifact)
        """

    def get_core_device(self, coreDeviceThingName: str) -> GetCoreDeviceResponseTypeDef:
        """
        [Client.get_core_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Client.get_core_device)
        """

    def get_deployment(self, deploymentId: str) -> GetDeploymentResponseTypeDef:
        """
        [Client.get_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Client.get_deployment)
        """

    def list_component_versions(
        self, arn: str, maxResults: int = None, nextToken: str = None
    ) -> ListComponentVersionsResponseTypeDef:
        """
        [Client.list_component_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Client.list_component_versions)
        """

    def list_components(
        self,
        scope: Literal["PRIVATE", "PUBLIC"] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListComponentsResponseTypeDef:
        """
        [Client.list_components documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Client.list_components)
        """

    def list_core_devices(
        self,
        thingGroupArn: str = None,
        status: Literal["HEALTHY", "UNHEALTHY"] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListCoreDevicesResponseTypeDef:
        """
        [Client.list_core_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Client.list_core_devices)
        """

    def list_deployments(
        self,
        targetArn: str = None,
        historyFilter: Literal["ALL", "LATEST_ONLY"] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListDeploymentsResponseTypeDef:
        """
        [Client.list_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Client.list_deployments)
        """

    def list_effective_deployments(
        self, coreDeviceThingName: str, maxResults: int = None, nextToken: str = None
    ) -> ListEffectiveDeploymentsResponseTypeDef:
        """
        [Client.list_effective_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Client.list_effective_deployments)
        """

    def list_installed_components(
        self, coreDeviceThingName: str, maxResults: int = None, nextToken: str = None
    ) -> ListInstalledComponentsResponseTypeDef:
        """
        [Client.list_installed_components documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Client.list_installed_components)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Client.list_tags_for_resource)
        """

    def resolve_component_candidates(
        self,
        platform: "ComponentPlatformTypeDef",
        componentCandidates: List[ComponentCandidateTypeDef],
    ) -> ResolveComponentCandidatesResponseTypeDef:
        """
        [Client.resolve_component_candidates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Client.resolve_component_candidates)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Client.untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_component_versions"]
    ) -> ListComponentVersionsPaginator:
        """
        [Paginator.ListComponentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListComponentVersions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_components"]) -> ListComponentsPaginator:
        """
        [Paginator.ListComponents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListComponents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_core_devices"]
    ) -> ListCoreDevicesPaginator:
        """
        [Paginator.ListCoreDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListCoreDevices)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployments"]
    ) -> ListDeploymentsPaginator:
        """
        [Paginator.ListDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListDeployments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_effective_deployments"]
    ) -> ListEffectiveDeploymentsPaginator:
        """
        [Paginator.ListEffectiveDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListEffectiveDeployments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_installed_components"]
    ) -> ListInstalledComponentsPaginator:
        """
        [Paginator.ListInstalledComponents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListInstalledComponents)
        """
