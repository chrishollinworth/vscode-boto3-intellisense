"""
Type annotations for greengrassv2 service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_greengrassv2 import GreengrassV2Client

    client: GreengrassV2Client = boto3.client("greengrassv2")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import (
    ComponentVisibilityScopeType,
    CoreDeviceStatusType,
    DeploymentHistoryFilterType,
    RecipeOutputFormatType,
)
from .paginator import (
    ListClientDevicesAssociatedWithCoreDevicePaginator,
    ListComponentsPaginator,
    ListComponentVersionsPaginator,
    ListCoreDevicesPaginator,
    ListDeploymentsPaginator,
    ListEffectiveDeploymentsPaginator,
    ListInstalledComponentsPaginator,
)
from .type_defs import (
    AssociateClientDeviceWithCoreDeviceEntryTypeDef,
    AssociateServiceRoleToAccountResponseTypeDef,
    BatchAssociateClientDeviceWithCoreDeviceResponseTypeDef,
    BatchDisassociateClientDeviceFromCoreDeviceResponseTypeDef,
    CancelDeploymentResponseTypeDef,
    ComponentCandidateTypeDef,
    ComponentDeploymentSpecificationTypeDef,
    ComponentPlatformTypeDef,
    ConnectivityInfoTypeDef,
    CreateComponentVersionResponseTypeDef,
    CreateDeploymentResponseTypeDef,
    DeploymentIoTJobConfigurationTypeDef,
    DeploymentPoliciesTypeDef,
    DescribeComponentResponseTypeDef,
    DisassociateClientDeviceFromCoreDeviceEntryTypeDef,
    DisassociateServiceRoleFromAccountResponseTypeDef,
    GetComponentResponseTypeDef,
    GetComponentVersionArtifactResponseTypeDef,
    GetConnectivityInfoResponseTypeDef,
    GetCoreDeviceResponseTypeDef,
    GetDeploymentResponseTypeDef,
    GetServiceRoleForAccountResponseTypeDef,
    LambdaFunctionRecipeSourceTypeDef,
    ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef,
    ListComponentsResponseTypeDef,
    ListComponentVersionsResponseTypeDef,
    ListCoreDevicesResponseTypeDef,
    ListDeploymentsResponseTypeDef,
    ListEffectiveDeploymentsResponseTypeDef,
    ListInstalledComponentsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ResolveComponentCandidatesResponseTypeDef,
    UpdateConnectivityInfoResponseTypeDef,
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
    RequestAlreadyInProgressException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class GreengrassV2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        GreengrassV2Client exceptions.
        """
    def associate_service_role_to_account(
        self, *, roleArn: str
    ) -> AssociateServiceRoleToAccountResponseTypeDef:
        """
        Associates a Greengrass service role with IoT Greengrass for your Amazon Web
        Services account in this Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.associate_service_role_to_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#associate_service_role_to_account)
        """
    def batch_associate_client_device_with_core_device(
        self,
        *,
        coreDeviceThingName: str,
        entries: List["AssociateClientDeviceWithCoreDeviceEntryTypeDef"] = None
    ) -> BatchAssociateClientDeviceWithCoreDeviceResponseTypeDef:
        """
        Associates a list of client devices with a core device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.batch_associate_client_device_with_core_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#batch_associate_client_device_with_core_device)
        """
    def batch_disassociate_client_device_from_core_device(
        self,
        *,
        coreDeviceThingName: str,
        entries: List["DisassociateClientDeviceFromCoreDeviceEntryTypeDef"] = None
    ) -> BatchDisassociateClientDeviceFromCoreDeviceResponseTypeDef:
        """
        Disassociates a list of client devices from a core device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.batch_disassociate_client_device_from_core_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#batch_disassociate_client_device_from_core_device)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#can_paginate)
        """
    def cancel_deployment(self, *, deploymentId: str) -> CancelDeploymentResponseTypeDef:
        """
        Cancels a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.cancel_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#cancel_deployment)
        """
    def create_component_version(
        self,
        *,
        inlineRecipe: Union[bytes, IO[bytes], StreamingBody] = None,
        lambdaFunction: "LambdaFunctionRecipeSourceTypeDef" = None,
        tags: Dict[str, str] = None,
        clientToken: str = None
    ) -> CreateComponentVersionResponseTypeDef:
        """
        Creates a component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.create_component_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#create_component_version)
        """
    def create_deployment(
        self,
        *,
        targetArn: str,
        deploymentName: str = None,
        components: Dict[str, "ComponentDeploymentSpecificationTypeDef"] = None,
        iotJobConfiguration: "DeploymentIoTJobConfigurationTypeDef" = None,
        deploymentPolicies: "DeploymentPoliciesTypeDef" = None,
        tags: Dict[str, str] = None,
        clientToken: str = None
    ) -> CreateDeploymentResponseTypeDef:
        """
        Creates a continuous deployment for a target, which is a Greengrass core device
        or group of core devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.create_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#create_deployment)
        """
    def delete_component(self, *, arn: str) -> None:
        """
        Deletes a version of a component from IoT Greengrass.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.delete_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#delete_component)
        """
    def delete_core_device(self, *, coreDeviceThingName: str) -> None:
        """
        Deletes a Greengrass core device, which is an IoT thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.delete_core_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#delete_core_device)
        """
    def delete_deployment(self, *, deploymentId: str) -> None:
        """
        Deletes a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.delete_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#delete_deployment)
        """
    def describe_component(self, *, arn: str) -> DescribeComponentResponseTypeDef:
        """
        Retrieves metadata for a version of a component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.describe_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#describe_component)
        """
    def disassociate_service_role_from_account(
        self,
    ) -> DisassociateServiceRoleFromAccountResponseTypeDef:
        """
        Disassociates the Greengrass service role from IoT Greengrass for your Amazon
        Web Services account in this Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.disassociate_service_role_from_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#disassociate_service_role_from_account)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#generate_presigned_url)
        """
    def get_component(
        self, *, arn: str, recipeOutputFormat: RecipeOutputFormatType = None
    ) -> GetComponentResponseTypeDef:
        """
        Gets the recipe for a version of a component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.get_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#get_component)
        """
    def get_component_version_artifact(
        self, *, arn: str, artifactName: str
    ) -> GetComponentVersionArtifactResponseTypeDef:
        """
        Gets the pre-signed URL to download a public or a Lambda component artifact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.get_component_version_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#get_component_version_artifact)
        """
    def get_connectivity_info(self, *, thingName: str) -> GetConnectivityInfoResponseTypeDef:
        """
        Retrieves connectivity information for a Greengrass core device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.get_connectivity_info)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#get_connectivity_info)
        """
    def get_core_device(self, *, coreDeviceThingName: str) -> GetCoreDeviceResponseTypeDef:
        """
        Retrieves metadata for a Greengrass core device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.get_core_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#get_core_device)
        """
    def get_deployment(self, *, deploymentId: str) -> GetDeploymentResponseTypeDef:
        """
        Gets a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.get_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#get_deployment)
        """
    def get_service_role_for_account(self) -> GetServiceRoleForAccountResponseTypeDef:
        """
        Gets the service role associated with IoT Greengrass for your Amazon Web
        Services account in this Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.get_service_role_for_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#get_service_role_for_account)
        """
    def list_client_devices_associated_with_core_device(
        self, *, coreDeviceThingName: str, maxResults: int = None, nextToken: str = None
    ) -> ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef:
        """
        Retrieves a paginated list of client devices that are associated with a core
        device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.list_client_devices_associated_with_core_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#list_client_devices_associated_with_core_device)
        """
    def list_component_versions(
        self, *, arn: str, maxResults: int = None, nextToken: str = None
    ) -> ListComponentVersionsResponseTypeDef:
        """
        Retrieves a paginated list of all versions for a component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.list_component_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#list_component_versions)
        """
    def list_components(
        self,
        *,
        scope: ComponentVisibilityScopeType = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListComponentsResponseTypeDef:
        """
        Retrieves a paginated list of component summaries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.list_components)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#list_components)
        """
    def list_core_devices(
        self,
        *,
        thingGroupArn: str = None,
        status: CoreDeviceStatusType = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListCoreDevicesResponseTypeDef:
        """
        Retrieves a paginated list of Greengrass core devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.list_core_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#list_core_devices)
        """
    def list_deployments(
        self,
        *,
        targetArn: str = None,
        historyFilter: DeploymentHistoryFilterType = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListDeploymentsResponseTypeDef:
        """
        Retrieves a paginated list of deployments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.list_deployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#list_deployments)
        """
    def list_effective_deployments(
        self, *, coreDeviceThingName: str, maxResults: int = None, nextToken: str = None
    ) -> ListEffectiveDeploymentsResponseTypeDef:
        """
        Retrieves a paginated list of deployment jobs that IoT Greengrass sends to
        Greengrass core devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.list_effective_deployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#list_effective_deployments)
        """
    def list_installed_components(
        self, *, coreDeviceThingName: str, maxResults: int = None, nextToken: str = None
    ) -> ListInstalledComponentsResponseTypeDef:
        """
        Retrieves a paginated list of the components that a Greengrass core device runs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.list_installed_components)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#list_installed_components)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the list of tags for an IoT Greengrass resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#list_tags_for_resource)
        """
    def resolve_component_candidates(
        self,
        *,
        platform: "ComponentPlatformTypeDef" = None,
        componentCandidates: List["ComponentCandidateTypeDef"] = None
    ) -> ResolveComponentCandidatesResponseTypeDef:
        """
        Retrieves a list of components that meet the component, version, and platform
        requirements of a deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.resolve_component_candidates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#resolve_component_candidates)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds tags to an IoT Greengrass resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag from an IoT Greengrass resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#untag_resource)
        """
    def update_connectivity_info(
        self, *, thingName: str, connectivityInfo: List["ConnectivityInfoTypeDef"]
    ) -> UpdateConnectivityInfoResponseTypeDef:
        """
        Updates connectivity information for a Greengrass core device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Client.update_connectivity_info)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/client.html#update_connectivity_info)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_client_devices_associated_with_core_device"]
    ) -> ListClientDevicesAssociatedWithCoreDevicePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListClientDevicesAssociatedWithCoreDevice)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators.html#listclientdevicesassociatedwithcoredevicepaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_component_versions"]
    ) -> ListComponentVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListComponentVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators.html#listcomponentversionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_components"]) -> ListComponentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListComponents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators.html#listcomponentspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_core_devices"]
    ) -> ListCoreDevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListCoreDevices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators.html#listcoredevicespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployments"]
    ) -> ListDeploymentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListDeployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators.html#listdeploymentspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_effective_deployments"]
    ) -> ListEffectiveDeploymentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListEffectiveDeployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators.html#listeffectivedeploymentspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_installed_components"]
    ) -> ListInstalledComponentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/greengrassv2.html#GreengrassV2.Paginator.ListInstalledComponents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/paginators.html#listinstalledcomponentspaginator)
        """
