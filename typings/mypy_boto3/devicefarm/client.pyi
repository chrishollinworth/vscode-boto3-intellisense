"""
Type annotations for devicefarm service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_devicefarm import DeviceFarmClient

    client: DeviceFarmClient = boto3.client("devicefarm")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ArtifactCategoryType,
    DevicePoolTypeType,
    InteractionModeType,
    NetworkProfileTypeType,
    TestGridSessionArtifactCategoryType,
    TestGridSessionStatusType,
    TestTypeType,
    UploadTypeType,
)
from .paginator import (
    GetOfferingStatusPaginator,
    ListArtifactsPaginator,
    ListDeviceInstancesPaginator,
    ListDevicePoolsPaginator,
    ListDevicesPaginator,
    ListInstanceProfilesPaginator,
    ListJobsPaginator,
    ListNetworkProfilesPaginator,
    ListOfferingPromotionsPaginator,
    ListOfferingsPaginator,
    ListOfferingTransactionsPaginator,
    ListProjectsPaginator,
    ListRemoteAccessSessionsPaginator,
    ListRunsPaginator,
    ListSamplesPaginator,
    ListSuitesPaginator,
    ListTestsPaginator,
    ListUniqueProblemsPaginator,
    ListUploadsPaginator,
    ListVPCEConfigurationsPaginator,
)
from .type_defs import (
    CreateDevicePoolResultTypeDef,
    CreateInstanceProfileResultTypeDef,
    CreateNetworkProfileResultTypeDef,
    CreateProjectResultTypeDef,
    CreateRemoteAccessSessionConfigurationTypeDef,
    CreateRemoteAccessSessionResultTypeDef,
    CreateTestGridProjectResultTypeDef,
    CreateTestGridUrlResultTypeDef,
    CreateUploadResultTypeDef,
    CreateVPCEConfigurationResultTypeDef,
    DeviceFilterTypeDef,
    DeviceSelectionConfigurationTypeDef,
    ExecutionConfigurationTypeDef,
    GetAccountSettingsResultTypeDef,
    GetDeviceInstanceResultTypeDef,
    GetDevicePoolCompatibilityResultTypeDef,
    GetDevicePoolResultTypeDef,
    GetDeviceResultTypeDef,
    GetInstanceProfileResultTypeDef,
    GetJobResultTypeDef,
    GetNetworkProfileResultTypeDef,
    GetOfferingStatusResultTypeDef,
    GetProjectResultTypeDef,
    GetRemoteAccessSessionResultTypeDef,
    GetRunResultTypeDef,
    GetSuiteResultTypeDef,
    GetTestGridProjectResultTypeDef,
    GetTestGridSessionResultTypeDef,
    GetTestResultTypeDef,
    GetUploadResultTypeDef,
    GetVPCEConfigurationResultTypeDef,
    InstallToRemoteAccessSessionResultTypeDef,
    ListArtifactsResultTypeDef,
    ListDeviceInstancesResultTypeDef,
    ListDevicePoolsResultTypeDef,
    ListDevicesResultTypeDef,
    ListInstanceProfilesResultTypeDef,
    ListJobsResultTypeDef,
    ListNetworkProfilesResultTypeDef,
    ListOfferingPromotionsResultTypeDef,
    ListOfferingsResultTypeDef,
    ListOfferingTransactionsResultTypeDef,
    ListProjectsResultTypeDef,
    ListRemoteAccessSessionsResultTypeDef,
    ListRunsResultTypeDef,
    ListSamplesResultTypeDef,
    ListSuitesResultTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTestGridProjectsResultTypeDef,
    ListTestGridSessionActionsResultTypeDef,
    ListTestGridSessionArtifactsResultTypeDef,
    ListTestGridSessionsResultTypeDef,
    ListTestsResultTypeDef,
    ListUniqueProblemsResultTypeDef,
    ListUploadsResultTypeDef,
    ListVPCEConfigurationsResultTypeDef,
    PurchaseOfferingResultTypeDef,
    RenewOfferingResultTypeDef,
    RuleTypeDef,
    ScheduleRunConfigurationTypeDef,
    ScheduleRunResultTypeDef,
    ScheduleRunTestTypeDef,
    StopJobResultTypeDef,
    StopRemoteAccessSessionResultTypeDef,
    StopRunResultTypeDef,
    TagTypeDef,
    TestGridVpcConfigTypeDef,
    UpdateDeviceInstanceResultTypeDef,
    UpdateDevicePoolResultTypeDef,
    UpdateInstanceProfileResultTypeDef,
    UpdateNetworkProfileResultTypeDef,
    UpdateProjectResultTypeDef,
    UpdateTestGridProjectResultTypeDef,
    UpdateUploadResultTypeDef,
    UpdateVPCEConfigurationResultTypeDef,
    VpcConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("DeviceFarmClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ArgumentException: Type[BotocoreClientError]
    CannotDeleteException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    IdempotencyException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidOperationException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotEligibleException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceAccountException: Type[BotocoreClientError]
    TagOperationException: Type[BotocoreClientError]
    TagPolicyException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]

class DeviceFarmClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DeviceFarmClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#close)
        """
    def create_device_pool(
        self,
        *,
        projectArn: str,
        name: str,
        rules: List["RuleTypeDef"],
        description: str = None,
        maxDevices: int = None
    ) -> CreateDevicePoolResultTypeDef:
        """
        Creates a device pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.create_device_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#create_device_pool)
        """
    def create_instance_profile(
        self,
        *,
        name: str,
        description: str = None,
        packageCleanup: bool = None,
        excludeAppPackagesFromCleanup: List[str] = None,
        rebootAfterUse: bool = None
    ) -> CreateInstanceProfileResultTypeDef:
        """
        Creates a profile that can be applied to one or more private fleet device
        instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.create_instance_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#create_instance_profile)
        """
    def create_network_profile(
        self,
        *,
        projectArn: str,
        name: str,
        description: str = None,
        type: NetworkProfileTypeType = None,
        uplinkBandwidthBits: int = None,
        downlinkBandwidthBits: int = None,
        uplinkDelayMs: int = None,
        downlinkDelayMs: int = None,
        uplinkJitterMs: int = None,
        downlinkJitterMs: int = None,
        uplinkLossPercent: int = None,
        downlinkLossPercent: int = None
    ) -> CreateNetworkProfileResultTypeDef:
        """
        Creates a network profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.create_network_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#create_network_profile)
        """
    def create_project(
        self,
        *,
        name: str,
        defaultJobTimeoutMinutes: int = None,
        vpcConfig: "VpcConfigTypeDef" = None
    ) -> CreateProjectResultTypeDef:
        """
        Creates a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.create_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#create_project)
        """
    def create_remote_access_session(
        self,
        *,
        projectArn: str,
        deviceArn: str,
        instanceArn: str = None,
        sshPublicKey: str = None,
        remoteDebugEnabled: bool = None,
        remoteRecordEnabled: bool = None,
        remoteRecordAppArn: str = None,
        name: str = None,
        clientId: str = None,
        configuration: "CreateRemoteAccessSessionConfigurationTypeDef" = None,
        interactionMode: InteractionModeType = None,
        skipAppResign: bool = None
    ) -> CreateRemoteAccessSessionResultTypeDef:
        """
        Specifies and starts a remote access session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.create_remote_access_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#create_remote_access_session)
        """
    def create_test_grid_project(
        self, *, name: str, description: str = None, vpcConfig: "TestGridVpcConfigTypeDef" = None
    ) -> CreateTestGridProjectResultTypeDef:
        """
        Creates a Selenium testing project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.create_test_grid_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#create_test_grid_project)
        """
    def create_test_grid_url(
        self, *, projectArn: str, expiresInSeconds: int
    ) -> CreateTestGridUrlResultTypeDef:
        """
        Creates a signed, short-term URL that can be passed to a Selenium
        `RemoteWebDriver` constructor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.create_test_grid_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#create_test_grid_url)
        """
    def create_upload(
        self, *, projectArn: str, name: str, type: UploadTypeType, contentType: str = None
    ) -> CreateUploadResultTypeDef:
        """
        Uploads an app or test scripts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.create_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#create_upload)
        """
    def create_vpce_configuration(
        self,
        *,
        vpceConfigurationName: str,
        vpceServiceName: str,
        serviceDnsName: str,
        vpceConfigurationDescription: str = None
    ) -> CreateVPCEConfigurationResultTypeDef:
        """
        Creates a configuration record in Device Farm for your Amazon Virtual Private
        Cloud (VPC) endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.create_vpce_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#create_vpce_configuration)
        """
    def delete_device_pool(self, *, arn: str) -> Dict[str, Any]:
        """
        Deletes a device pool given the pool ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.delete_device_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#delete_device_pool)
        """
    def delete_instance_profile(self, *, arn: str) -> Dict[str, Any]:
        """
        Deletes a profile that can be applied to one or more private device instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.delete_instance_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#delete_instance_profile)
        """
    def delete_network_profile(self, *, arn: str) -> Dict[str, Any]:
        """
        Deletes a network profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.delete_network_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#delete_network_profile)
        """
    def delete_project(self, *, arn: str) -> Dict[str, Any]:
        """
        Deletes an AWS Device Farm project, given the project ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.delete_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#delete_project)
        """
    def delete_remote_access_session(self, *, arn: str) -> Dict[str, Any]:
        """
        Deletes a completed remote access session and its results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.delete_remote_access_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#delete_remote_access_session)
        """
    def delete_run(self, *, arn: str) -> Dict[str, Any]:
        """
        Deletes the run, given the run ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.delete_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#delete_run)
        """
    def delete_test_grid_project(self, *, projectArn: str) -> Dict[str, Any]:
        """
        Deletes a Selenium testing project and all content generated under it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.delete_test_grid_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#delete_test_grid_project)
        """
    def delete_upload(self, *, arn: str) -> Dict[str, Any]:
        """
        Deletes an upload given the upload ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.delete_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#delete_upload)
        """
    def delete_vpce_configuration(self, *, arn: str) -> Dict[str, Any]:
        """
        Deletes a configuration for your Amazon Virtual Private Cloud (VPC) endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.delete_vpce_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#delete_vpce_configuration)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#generate_presigned_url)
        """
    def get_account_settings(self) -> GetAccountSettingsResultTypeDef:
        """
        Returns the number of unmetered iOS or unmetered Android devices that have been
        purchased by the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.get_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#get_account_settings)
        """
    def get_device(self, *, arn: str) -> GetDeviceResultTypeDef:
        """
        Gets information about a unique device type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.get_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#get_device)
        """
    def get_device_instance(self, *, arn: str) -> GetDeviceInstanceResultTypeDef:
        """
        Returns information about a device instance that belongs to a private device
        fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.get_device_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#get_device_instance)
        """
    def get_device_pool(self, *, arn: str) -> GetDevicePoolResultTypeDef:
        """
        Gets information about a device pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.get_device_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#get_device_pool)
        """
    def get_device_pool_compatibility(
        self,
        *,
        devicePoolArn: str,
        appArn: str = None,
        testType: TestTypeType = None,
        test: "ScheduleRunTestTypeDef" = None,
        configuration: "ScheduleRunConfigurationTypeDef" = None
    ) -> GetDevicePoolCompatibilityResultTypeDef:
        """
        Gets information about compatibility with a device pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.get_device_pool_compatibility)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#get_device_pool_compatibility)
        """
    def get_instance_profile(self, *, arn: str) -> GetInstanceProfileResultTypeDef:
        """
        Returns information about the specified instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.get_instance_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#get_instance_profile)
        """
    def get_job(self, *, arn: str) -> GetJobResultTypeDef:
        """
        Gets information about a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.get_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#get_job)
        """
    def get_network_profile(self, *, arn: str) -> GetNetworkProfileResultTypeDef:
        """
        Returns information about a network profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.get_network_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#get_network_profile)
        """
    def get_offering_status(self, *, nextToken: str = None) -> GetOfferingStatusResultTypeDef:
        """
        Gets the current status and future status of all offerings purchased by an AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.get_offering_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#get_offering_status)
        """
    def get_project(self, *, arn: str) -> GetProjectResultTypeDef:
        """
        Gets information about a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.get_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#get_project)
        """
    def get_remote_access_session(self, *, arn: str) -> GetRemoteAccessSessionResultTypeDef:
        """
        Returns a link to a currently running remote access session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.get_remote_access_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#get_remote_access_session)
        """
    def get_run(self, *, arn: str) -> GetRunResultTypeDef:
        """
        Gets information about a run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.get_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#get_run)
        """
    def get_suite(self, *, arn: str) -> GetSuiteResultTypeDef:
        """
        Gets information about a suite.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.get_suite)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#get_suite)
        """
    def get_test(self, *, arn: str) -> GetTestResultTypeDef:
        """
        Gets information about a test.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.get_test)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#get_test)
        """
    def get_test_grid_project(self, *, projectArn: str) -> GetTestGridProjectResultTypeDef:
        """
        Retrieves information about a Selenium testing project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.get_test_grid_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#get_test_grid_project)
        """
    def get_test_grid_session(
        self, *, projectArn: str = None, sessionId: str = None, sessionArn: str = None
    ) -> GetTestGridSessionResultTypeDef:
        """
        A session is an instance of a browser created through a `RemoteWebDriver` with
        the URL from  CreateTestGridUrlResult$url.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.get_test_grid_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#get_test_grid_session)
        """
    def get_upload(self, *, arn: str) -> GetUploadResultTypeDef:
        """
        Gets information about an upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.get_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#get_upload)
        """
    def get_vpce_configuration(self, *, arn: str) -> GetVPCEConfigurationResultTypeDef:
        """
        Returns information about the configuration settings for your Amazon Virtual
        Private Cloud (VPC) endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.get_vpce_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#get_vpce_configuration)
        """
    def install_to_remote_access_session(
        self, *, remoteAccessSessionArn: str, appArn: str
    ) -> InstallToRemoteAccessSessionResultTypeDef:
        """
        Installs an application to the device in a remote access session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.install_to_remote_access_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#install_to_remote_access_session)
        """
    def list_artifacts(
        self, *, arn: str, type: ArtifactCategoryType, nextToken: str = None
    ) -> ListArtifactsResultTypeDef:
        """
        Gets information about artifacts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_artifacts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_artifacts)
        """
    def list_device_instances(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListDeviceInstancesResultTypeDef:
        """
        Returns information about the private device instances associated with one or
        more AWS accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_device_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_device_instances)
        """
    def list_device_pools(
        self, *, arn: str, type: DevicePoolTypeType = None, nextToken: str = None
    ) -> ListDevicePoolsResultTypeDef:
        """
        Gets information about device pools.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_device_pools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_device_pools)
        """
    def list_devices(
        self, *, arn: str = None, nextToken: str = None, filters: List["DeviceFilterTypeDef"] = None
    ) -> ListDevicesResultTypeDef:
        """
        Gets information about unique device types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_devices)
        """
    def list_instance_profiles(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListInstanceProfilesResultTypeDef:
        """
        Returns information about all the instance profiles in an AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_instance_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_instance_profiles)
        """
    def list_jobs(self, *, arn: str, nextToken: str = None) -> ListJobsResultTypeDef:
        """
        Gets information about jobs for a given test run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_jobs)
        """
    def list_network_profiles(
        self, *, arn: str, type: NetworkProfileTypeType = None, nextToken: str = None
    ) -> ListNetworkProfilesResultTypeDef:
        """
        Returns the list of available network profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_network_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_network_profiles)
        """
    def list_offering_promotions(
        self, *, nextToken: str = None
    ) -> ListOfferingPromotionsResultTypeDef:
        """
        Returns a list of offering promotions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_offering_promotions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_offering_promotions)
        """
    def list_offering_transactions(
        self, *, nextToken: str = None
    ) -> ListOfferingTransactionsResultTypeDef:
        """
        Returns a list of all historical purchases, renewals, and system renewal
        transactions for an AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_offering_transactions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_offering_transactions)
        """
    def list_offerings(self, *, nextToken: str = None) -> ListOfferingsResultTypeDef:
        """
        Returns a list of products or offerings that the user can manage through the
        API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_offerings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_offerings)
        """
    def list_projects(self, *, arn: str = None, nextToken: str = None) -> ListProjectsResultTypeDef:
        """
        Gets information about projects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_projects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_projects)
        """
    def list_remote_access_sessions(
        self, *, arn: str, nextToken: str = None
    ) -> ListRemoteAccessSessionsResultTypeDef:
        """
        Returns a list of all currently running remote access sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_remote_access_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_remote_access_sessions)
        """
    def list_runs(self, *, arn: str, nextToken: str = None) -> ListRunsResultTypeDef:
        """
        Gets information about runs, given an AWS Device Farm project ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_runs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_runs)
        """
    def list_samples(self, *, arn: str, nextToken: str = None) -> ListSamplesResultTypeDef:
        """
        Gets information about samples, given an AWS Device Farm job ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_samples)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_samples)
        """
    def list_suites(self, *, arn: str, nextToken: str = None) -> ListSuitesResultTypeDef:
        """
        Gets information about test suites for a given job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_suites)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_suites)
        """
    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        List the tags for an AWS Device Farm resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_tags_for_resource)
        """
    def list_test_grid_projects(
        self, *, maxResult: int = None, nextToken: str = None
    ) -> ListTestGridProjectsResultTypeDef:
        """
        Gets a list of all Selenium testing projects in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_test_grid_projects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_test_grid_projects)
        """
    def list_test_grid_session_actions(
        self, *, sessionArn: str, maxResult: int = None, nextToken: str = None
    ) -> ListTestGridSessionActionsResultTypeDef:
        """
        Returns a list of the actions taken in a  TestGridSession.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_test_grid_session_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_test_grid_session_actions)
        """
    def list_test_grid_session_artifacts(
        self,
        *,
        sessionArn: str,
        type: TestGridSessionArtifactCategoryType = None,
        maxResult: int = None,
        nextToken: str = None
    ) -> ListTestGridSessionArtifactsResultTypeDef:
        """
        Retrieves a list of artifacts created during the session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_test_grid_session_artifacts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_test_grid_session_artifacts)
        """
    def list_test_grid_sessions(
        self,
        *,
        projectArn: str,
        status: TestGridSessionStatusType = None,
        creationTimeAfter: Union[datetime, str] = None,
        creationTimeBefore: Union[datetime, str] = None,
        endTimeAfter: Union[datetime, str] = None,
        endTimeBefore: Union[datetime, str] = None,
        maxResult: int = None,
        nextToken: str = None
    ) -> ListTestGridSessionsResultTypeDef:
        """
        Retrieves a list of sessions for a  TestGridProject.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_test_grid_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_test_grid_sessions)
        """
    def list_tests(self, *, arn: str, nextToken: str = None) -> ListTestsResultTypeDef:
        """
        Gets information about tests in a given test suite.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_tests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_tests)
        """
    def list_unique_problems(
        self, *, arn: str, nextToken: str = None
    ) -> ListUniqueProblemsResultTypeDef:
        """
        Gets information about unique problems, such as exceptions or crashes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_unique_problems)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_unique_problems)
        """
    def list_uploads(
        self, *, arn: str, type: UploadTypeType = None, nextToken: str = None
    ) -> ListUploadsResultTypeDef:
        """
        Gets information about uploads, given an AWS Device Farm project ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_uploads)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_uploads)
        """
    def list_vpce_configurations(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListVPCEConfigurationsResultTypeDef:
        """
        Returns information about all Amazon Virtual Private Cloud (VPC) endpoint
        configurations in the AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.list_vpce_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#list_vpce_configurations)
        """
    def purchase_offering(
        self, *, offeringId: str, quantity: int, offeringPromotionId: str = None
    ) -> PurchaseOfferingResultTypeDef:
        """
        Immediately purchases offerings for an AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.purchase_offering)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#purchase_offering)
        """
    def renew_offering(self, *, offeringId: str, quantity: int) -> RenewOfferingResultTypeDef:
        """
        Explicitly sets the quantity of devices to renew for an offering, starting from
        the `effectiveDate` of the next period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.renew_offering)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#renew_offering)
        """
    def schedule_run(
        self,
        *,
        projectArn: str,
        test: "ScheduleRunTestTypeDef",
        appArn: str = None,
        devicePoolArn: str = None,
        deviceSelectionConfiguration: "DeviceSelectionConfigurationTypeDef" = None,
        name: str = None,
        configuration: "ScheduleRunConfigurationTypeDef" = None,
        executionConfiguration: "ExecutionConfigurationTypeDef" = None
    ) -> ScheduleRunResultTypeDef:
        """
        Schedules a run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.schedule_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#schedule_run)
        """
    def stop_job(self, *, arn: str) -> StopJobResultTypeDef:
        """
        Initiates a stop request for the current job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.stop_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#stop_job)
        """
    def stop_remote_access_session(self, *, arn: str) -> StopRemoteAccessSessionResultTypeDef:
        """
        Ends a specified remote access session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.stop_remote_access_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#stop_remote_access_session)
        """
    def stop_run(self, *, arn: str) -> StopRunResultTypeDef:
        """
        Initiates a stop request for the current test run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.stop_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#stop_run)
        """
    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Associates the specified tags to a resource with the specified `resourceArn`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Deletes the specified tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#untag_resource)
        """
    def update_device_instance(
        self, *, arn: str, profileArn: str = None, labels: List[str] = None
    ) -> UpdateDeviceInstanceResultTypeDef:
        """
        Updates information about a private device instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.update_device_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#update_device_instance)
        """
    def update_device_pool(
        self,
        *,
        arn: str,
        name: str = None,
        description: str = None,
        rules: List["RuleTypeDef"] = None,
        maxDevices: int = None,
        clearMaxDevices: bool = None
    ) -> UpdateDevicePoolResultTypeDef:
        """
        Modifies the name, description, and rules in a device pool given the attributes
        and the pool ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.update_device_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#update_device_pool)
        """
    def update_instance_profile(
        self,
        *,
        arn: str,
        name: str = None,
        description: str = None,
        packageCleanup: bool = None,
        excludeAppPackagesFromCleanup: List[str] = None,
        rebootAfterUse: bool = None
    ) -> UpdateInstanceProfileResultTypeDef:
        """
        Updates information about an existing private device instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.update_instance_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#update_instance_profile)
        """
    def update_network_profile(
        self,
        *,
        arn: str,
        name: str = None,
        description: str = None,
        type: NetworkProfileTypeType = None,
        uplinkBandwidthBits: int = None,
        downlinkBandwidthBits: int = None,
        uplinkDelayMs: int = None,
        downlinkDelayMs: int = None,
        uplinkJitterMs: int = None,
        downlinkJitterMs: int = None,
        uplinkLossPercent: int = None,
        downlinkLossPercent: int = None
    ) -> UpdateNetworkProfileResultTypeDef:
        """
        Updates the network profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.update_network_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#update_network_profile)
        """
    def update_project(
        self,
        *,
        arn: str,
        name: str = None,
        defaultJobTimeoutMinutes: int = None,
        vpcConfig: "VpcConfigTypeDef" = None
    ) -> UpdateProjectResultTypeDef:
        """
        Modifies the specified project name, given the project ARN and a new name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.update_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#update_project)
        """
    def update_test_grid_project(
        self,
        *,
        projectArn: str,
        name: str = None,
        description: str = None,
        vpcConfig: "TestGridVpcConfigTypeDef" = None
    ) -> UpdateTestGridProjectResultTypeDef:
        """
        Change details of a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.update_test_grid_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#update_test_grid_project)
        """
    def update_upload(
        self, *, arn: str, name: str = None, contentType: str = None, editContent: bool = None
    ) -> UpdateUploadResultTypeDef:
        """
        Updates an uploaded test spec.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.update_upload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#update_upload)
        """
    def update_vpce_configuration(
        self,
        *,
        arn: str,
        vpceConfigurationName: str = None,
        vpceServiceName: str = None,
        serviceDnsName: str = None,
        vpceConfigurationDescription: str = None
    ) -> UpdateVPCEConfigurationResultTypeDef:
        """
        Updates information about an Amazon Virtual Private Cloud (VPC) endpoint
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Client.update_vpce_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client.html#update_vpce_configuration)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_offering_status"]
    ) -> GetOfferingStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Paginator.GetOfferingStatus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators.html#getofferingstatuspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_artifacts"]) -> ListArtifactsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Paginator.ListArtifacts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators.html#listartifactspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_instances"]
    ) -> ListDeviceInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDeviceInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators.html#listdeviceinstancespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_pools"]
    ) -> ListDevicePoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDevicePools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators.html#listdevicepoolspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_devices"]) -> ListDevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDevices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators.html#listdevicespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_profiles"]
    ) -> ListInstanceProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Paginator.ListInstanceProfiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators.html#listinstanceprofilespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Paginator.ListJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators.html#listjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_network_profiles"]
    ) -> ListNetworkProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Paginator.ListNetworkProfiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators.html#listnetworkprofilespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_offering_promotions"]
    ) -> ListOfferingPromotionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferingPromotions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators.html#listofferingpromotionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_offering_transactions"]
    ) -> ListOfferingTransactionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferingTransactions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators.html#listofferingtransactionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_offerings"]) -> ListOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators.html#listofferingspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Paginator.ListProjects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators.html#listprojectspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_remote_access_sessions"]
    ) -> ListRemoteAccessSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Paginator.ListRemoteAccessSessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators.html#listremoteaccesssessionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_runs"]) -> ListRunsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Paginator.ListRuns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators.html#listrunspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_samples"]) -> ListSamplesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Paginator.ListSamples)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators.html#listsamplespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_suites"]) -> ListSuitesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Paginator.ListSuites)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators.html#listsuitespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_tests"]) -> ListTestsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Paginator.ListTests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators.html#listtestspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_unique_problems"]
    ) -> ListUniqueProblemsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Paginator.ListUniqueProblems)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators.html#listuniqueproblemspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_uploads"]) -> ListUploadsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Paginator.ListUploads)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators.html#listuploadspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_vpce_configurations"]
    ) -> ListVPCEConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/devicefarm.html#DeviceFarm.Paginator.ListVPCEConfigurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators.html#listvpceconfigurationspaginator)
        """
