# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for devicefarm service client

Usage::

    ```python
    import boto3
    from mypy_boto3_devicefarm import DeviceFarmClient

    client: DeviceFarmClient = boto3.client("devicefarm")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_devicefarm.paginator import (
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
from mypy_boto3_devicefarm.type_defs import (
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
    UpdateDeviceInstanceResultTypeDef,
    UpdateDevicePoolResultTypeDef,
    UpdateInstanceProfileResultTypeDef,
    UpdateNetworkProfileResultTypeDef,
    UpdateProjectResultTypeDef,
    UpdateTestGridProjectResultTypeDef,
    UpdateUploadResultTypeDef,
    UpdateVPCEConfigurationResultTypeDef,
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


class DeviceFarmClient:
    """
    [DeviceFarm.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.can_paginate)
        """

    def create_device_pool(
        self,
        projectArn: str,
        name: str,
        rules: List["RuleTypeDef"],
        description: str = None,
        maxDevices: int = None,
    ) -> CreateDevicePoolResultTypeDef:
        """
        [Client.create_device_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.create_device_pool)
        """

    def create_instance_profile(
        self,
        name: str,
        description: str = None,
        packageCleanup: bool = None,
        excludeAppPackagesFromCleanup: List[str] = None,
        rebootAfterUse: bool = None,
    ) -> CreateInstanceProfileResultTypeDef:
        """
        [Client.create_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.create_instance_profile)
        """

    def create_network_profile(
        self,
        projectArn: str,
        name: str,
        description: str = None,
        type: Literal["CURATED", "PRIVATE"] = None,
        uplinkBandwidthBits: int = None,
        downlinkBandwidthBits: int = None,
        uplinkDelayMs: int = None,
        downlinkDelayMs: int = None,
        uplinkJitterMs: int = None,
        downlinkJitterMs: int = None,
        uplinkLossPercent: int = None,
        downlinkLossPercent: int = None,
    ) -> CreateNetworkProfileResultTypeDef:
        """
        [Client.create_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.create_network_profile)
        """

    def create_project(
        self, name: str, defaultJobTimeoutMinutes: int = None
    ) -> CreateProjectResultTypeDef:
        """
        [Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.create_project)
        """

    def create_remote_access_session(
        self,
        projectArn: str,
        deviceArn: str,
        instanceArn: str = None,
        sshPublicKey: str = None,
        remoteDebugEnabled: bool = None,
        remoteRecordEnabled: bool = None,
        remoteRecordAppArn: str = None,
        name: str = None,
        clientId: str = None,
        configuration: CreateRemoteAccessSessionConfigurationTypeDef = None,
        interactionMode: Literal["INTERACTIVE", "NO_VIDEO", "VIDEO_ONLY"] = None,
        skipAppResign: bool = None,
    ) -> CreateRemoteAccessSessionResultTypeDef:
        """
        [Client.create_remote_access_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.create_remote_access_session)
        """

    def create_test_grid_project(
        self, name: str, description: str = None
    ) -> CreateTestGridProjectResultTypeDef:
        """
        [Client.create_test_grid_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.create_test_grid_project)
        """

    def create_test_grid_url(
        self, projectArn: str, expiresInSeconds: int
    ) -> CreateTestGridUrlResultTypeDef:
        """
        [Client.create_test_grid_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.create_test_grid_url)
        """

    def create_upload(
        self,
        projectArn: str,
        name: str,
        type: Literal[
            "ANDROID_APP",
            "IOS_APP",
            "WEB_APP",
            "EXTERNAL_DATA",
            "APPIUM_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_PYTHON_TEST_PACKAGE",
            "APPIUM_NODE_TEST_PACKAGE",
            "APPIUM_RUBY_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_WEB_PYTHON_TEST_PACKAGE",
            "APPIUM_WEB_NODE_TEST_PACKAGE",
            "APPIUM_WEB_RUBY_TEST_PACKAGE",
            "CALABASH_TEST_PACKAGE",
            "INSTRUMENTATION_TEST_PACKAGE",
            "UIAUTOMATION_TEST_PACKAGE",
            "UIAUTOMATOR_TEST_PACKAGE",
            "XCTEST_TEST_PACKAGE",
            "XCTEST_UI_TEST_PACKAGE",
            "APPIUM_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_PYTHON_TEST_SPEC",
            "APPIUM_NODE_TEST_SPEC",
            "APPIUM_RUBY_TEST_SPEC",
            "APPIUM_WEB_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_WEB_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_WEB_PYTHON_TEST_SPEC",
            "APPIUM_WEB_NODE_TEST_SPEC",
            "APPIUM_WEB_RUBY_TEST_SPEC",
            "INSTRUMENTATION_TEST_SPEC",
            "XCTEST_UI_TEST_SPEC",
        ],
        contentType: str = None,
    ) -> CreateUploadResultTypeDef:
        """
        [Client.create_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.create_upload)
        """

    def create_vpce_configuration(
        self,
        vpceConfigurationName: str,
        vpceServiceName: str,
        serviceDnsName: str,
        vpceConfigurationDescription: str = None,
    ) -> CreateVPCEConfigurationResultTypeDef:
        """
        [Client.create_vpce_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.create_vpce_configuration)
        """

    def delete_device_pool(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_device_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.delete_device_pool)
        """

    def delete_instance_profile(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.delete_instance_profile)
        """

    def delete_network_profile(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.delete_network_profile)
        """

    def delete_project(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.delete_project)
        """

    def delete_remote_access_session(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_remote_access_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.delete_remote_access_session)
        """

    def delete_run(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.delete_run)
        """

    def delete_test_grid_project(self, projectArn: str) -> Dict[str, Any]:
        """
        [Client.delete_test_grid_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.delete_test_grid_project)
        """

    def delete_upload(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.delete_upload)
        """

    def delete_vpce_configuration(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_vpce_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.delete_vpce_configuration)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.generate_presigned_url)
        """

    def get_account_settings(self) -> GetAccountSettingsResultTypeDef:
        """
        [Client.get_account_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.get_account_settings)
        """

    def get_device(self, arn: str) -> GetDeviceResultTypeDef:
        """
        [Client.get_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.get_device)
        """

    def get_device_instance(self, arn: str) -> GetDeviceInstanceResultTypeDef:
        """
        [Client.get_device_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.get_device_instance)
        """

    def get_device_pool(self, arn: str) -> GetDevicePoolResultTypeDef:
        """
        [Client.get_device_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.get_device_pool)
        """

    def get_device_pool_compatibility(
        self,
        devicePoolArn: str,
        appArn: str = None,
        testType: Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ] = None,
        test: ScheduleRunTestTypeDef = None,
        configuration: ScheduleRunConfigurationTypeDef = None,
    ) -> GetDevicePoolCompatibilityResultTypeDef:
        """
        [Client.get_device_pool_compatibility documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.get_device_pool_compatibility)
        """

    def get_instance_profile(self, arn: str) -> GetInstanceProfileResultTypeDef:
        """
        [Client.get_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.get_instance_profile)
        """

    def get_job(self, arn: str) -> GetJobResultTypeDef:
        """
        [Client.get_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.get_job)
        """

    def get_network_profile(self, arn: str) -> GetNetworkProfileResultTypeDef:
        """
        [Client.get_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.get_network_profile)
        """

    def get_offering_status(self, nextToken: str = None) -> GetOfferingStatusResultTypeDef:
        """
        [Client.get_offering_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.get_offering_status)
        """

    def get_project(self, arn: str) -> GetProjectResultTypeDef:
        """
        [Client.get_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.get_project)
        """

    def get_remote_access_session(self, arn: str) -> GetRemoteAccessSessionResultTypeDef:
        """
        [Client.get_remote_access_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.get_remote_access_session)
        """

    def get_run(self, arn: str) -> GetRunResultTypeDef:
        """
        [Client.get_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.get_run)
        """

    def get_suite(self, arn: str) -> GetSuiteResultTypeDef:
        """
        [Client.get_suite documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.get_suite)
        """

    def get_test(self, arn: str) -> GetTestResultTypeDef:
        """
        [Client.get_test documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.get_test)
        """

    def get_test_grid_project(self, projectArn: str) -> GetTestGridProjectResultTypeDef:
        """
        [Client.get_test_grid_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.get_test_grid_project)
        """

    def get_test_grid_session(
        self, projectArn: str = None, sessionId: str = None, sessionArn: str = None
    ) -> GetTestGridSessionResultTypeDef:
        """
        [Client.get_test_grid_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.get_test_grid_session)
        """

    def get_upload(self, arn: str) -> GetUploadResultTypeDef:
        """
        [Client.get_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.get_upload)
        """

    def get_vpce_configuration(self, arn: str) -> GetVPCEConfigurationResultTypeDef:
        """
        [Client.get_vpce_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.get_vpce_configuration)
        """

    def install_to_remote_access_session(
        self, remoteAccessSessionArn: str, appArn: str
    ) -> InstallToRemoteAccessSessionResultTypeDef:
        """
        [Client.install_to_remote_access_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.install_to_remote_access_session)
        """

    def list_artifacts(
        self, arn: str, type: Literal["SCREENSHOT", "FILE", "LOG"], nextToken: str = None
    ) -> ListArtifactsResultTypeDef:
        """
        [Client.list_artifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_artifacts)
        """

    def list_device_instances(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListDeviceInstancesResultTypeDef:
        """
        [Client.list_device_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_device_instances)
        """

    def list_device_pools(
        self, arn: str, type: Literal["CURATED", "PRIVATE"] = None, nextToken: str = None
    ) -> ListDevicePoolsResultTypeDef:
        """
        [Client.list_device_pools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_device_pools)
        """

    def list_devices(
        self, arn: str = None, nextToken: str = None, filters: List["DeviceFilterTypeDef"] = None
    ) -> ListDevicesResultTypeDef:
        """
        [Client.list_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_devices)
        """

    def list_instance_profiles(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListInstanceProfilesResultTypeDef:
        """
        [Client.list_instance_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_instance_profiles)
        """

    def list_jobs(self, arn: str, nextToken: str = None) -> ListJobsResultTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_jobs)
        """

    def list_network_profiles(
        self, arn: str, type: Literal["CURATED", "PRIVATE"] = None, nextToken: str = None
    ) -> ListNetworkProfilesResultTypeDef:
        """
        [Client.list_network_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_network_profiles)
        """

    def list_offering_promotions(
        self, nextToken: str = None
    ) -> ListOfferingPromotionsResultTypeDef:
        """
        [Client.list_offering_promotions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_offering_promotions)
        """

    def list_offering_transactions(
        self, nextToken: str = None
    ) -> ListOfferingTransactionsResultTypeDef:
        """
        [Client.list_offering_transactions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_offering_transactions)
        """

    def list_offerings(self, nextToken: str = None) -> ListOfferingsResultTypeDef:
        """
        [Client.list_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_offerings)
        """

    def list_projects(self, arn: str = None, nextToken: str = None) -> ListProjectsResultTypeDef:
        """
        [Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_projects)
        """

    def list_remote_access_sessions(
        self, arn: str, nextToken: str = None
    ) -> ListRemoteAccessSessionsResultTypeDef:
        """
        [Client.list_remote_access_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_remote_access_sessions)
        """

    def list_runs(self, arn: str, nextToken: str = None) -> ListRunsResultTypeDef:
        """
        [Client.list_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_runs)
        """

    def list_samples(self, arn: str, nextToken: str = None) -> ListSamplesResultTypeDef:
        """
        [Client.list_samples documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_samples)
        """

    def list_suites(self, arn: str, nextToken: str = None) -> ListSuitesResultTypeDef:
        """
        [Client.list_suites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_suites)
        """

    def list_tags_for_resource(self, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_tags_for_resource)
        """

    def list_test_grid_projects(
        self, maxResult: int = None, nextToken: str = None
    ) -> ListTestGridProjectsResultTypeDef:
        """
        [Client.list_test_grid_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_test_grid_projects)
        """

    def list_test_grid_session_actions(
        self, sessionArn: str, maxResult: int = None, nextToken: str = None
    ) -> ListTestGridSessionActionsResultTypeDef:
        """
        [Client.list_test_grid_session_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_test_grid_session_actions)
        """

    def list_test_grid_session_artifacts(
        self,
        sessionArn: str,
        type: Literal["VIDEO", "LOG"] = None,
        maxResult: int = None,
        nextToken: str = None,
    ) -> ListTestGridSessionArtifactsResultTypeDef:
        """
        [Client.list_test_grid_session_artifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_test_grid_session_artifacts)
        """

    def list_test_grid_sessions(
        self,
        projectArn: str,
        status: Literal["ACTIVE", "CLOSED", "ERRORED"] = None,
        creationTimeAfter: datetime = None,
        creationTimeBefore: datetime = None,
        endTimeAfter: datetime = None,
        endTimeBefore: datetime = None,
        maxResult: int = None,
        nextToken: str = None,
    ) -> ListTestGridSessionsResultTypeDef:
        """
        [Client.list_test_grid_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_test_grid_sessions)
        """

    def list_tests(self, arn: str, nextToken: str = None) -> ListTestsResultTypeDef:
        """
        [Client.list_tests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_tests)
        """

    def list_unique_problems(
        self, arn: str, nextToken: str = None
    ) -> ListUniqueProblemsResultTypeDef:
        """
        [Client.list_unique_problems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_unique_problems)
        """

    def list_uploads(
        self,
        arn: str,
        type: Literal[
            "ANDROID_APP",
            "IOS_APP",
            "WEB_APP",
            "EXTERNAL_DATA",
            "APPIUM_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_PYTHON_TEST_PACKAGE",
            "APPIUM_NODE_TEST_PACKAGE",
            "APPIUM_RUBY_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_WEB_PYTHON_TEST_PACKAGE",
            "APPIUM_WEB_NODE_TEST_PACKAGE",
            "APPIUM_WEB_RUBY_TEST_PACKAGE",
            "CALABASH_TEST_PACKAGE",
            "INSTRUMENTATION_TEST_PACKAGE",
            "UIAUTOMATION_TEST_PACKAGE",
            "UIAUTOMATOR_TEST_PACKAGE",
            "XCTEST_TEST_PACKAGE",
            "XCTEST_UI_TEST_PACKAGE",
            "APPIUM_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_PYTHON_TEST_SPEC",
            "APPIUM_NODE_TEST_SPEC",
            "APPIUM_RUBY_TEST_SPEC",
            "APPIUM_WEB_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_WEB_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_WEB_PYTHON_TEST_SPEC",
            "APPIUM_WEB_NODE_TEST_SPEC",
            "APPIUM_WEB_RUBY_TEST_SPEC",
            "INSTRUMENTATION_TEST_SPEC",
            "XCTEST_UI_TEST_SPEC",
        ] = None,
        nextToken: str = None,
    ) -> ListUploadsResultTypeDef:
        """
        [Client.list_uploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_uploads)
        """

    def list_vpce_configurations(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListVPCEConfigurationsResultTypeDef:
        """
        [Client.list_vpce_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.list_vpce_configurations)
        """

    def purchase_offering(
        self, offeringId: str = None, quantity: int = None, offeringPromotionId: str = None
    ) -> PurchaseOfferingResultTypeDef:
        """
        [Client.purchase_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.purchase_offering)
        """

    def renew_offering(
        self, offeringId: str = None, quantity: int = None
    ) -> RenewOfferingResultTypeDef:
        """
        [Client.renew_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.renew_offering)
        """

    def schedule_run(
        self,
        projectArn: str,
        test: ScheduleRunTestTypeDef,
        appArn: str = None,
        devicePoolArn: str = None,
        deviceSelectionConfiguration: DeviceSelectionConfigurationTypeDef = None,
        name: str = None,
        configuration: ScheduleRunConfigurationTypeDef = None,
        executionConfiguration: ExecutionConfigurationTypeDef = None,
    ) -> ScheduleRunResultTypeDef:
        """
        [Client.schedule_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.schedule_run)
        """

    def stop_job(self, arn: str) -> StopJobResultTypeDef:
        """
        [Client.stop_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.stop_job)
        """

    def stop_remote_access_session(self, arn: str) -> StopRemoteAccessSessionResultTypeDef:
        """
        [Client.stop_remote_access_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.stop_remote_access_session)
        """

    def stop_run(self, arn: str) -> StopRunResultTypeDef:
        """
        [Client.stop_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.stop_run)
        """

    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.untag_resource)
        """

    def update_device_instance(
        self, arn: str, profileArn: str = None, labels: List[str] = None
    ) -> UpdateDeviceInstanceResultTypeDef:
        """
        [Client.update_device_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.update_device_instance)
        """

    def update_device_pool(
        self,
        arn: str,
        name: str = None,
        description: str = None,
        rules: List["RuleTypeDef"] = None,
        maxDevices: int = None,
        clearMaxDevices: bool = None,
    ) -> UpdateDevicePoolResultTypeDef:
        """
        [Client.update_device_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.update_device_pool)
        """

    def update_instance_profile(
        self,
        arn: str,
        name: str = None,
        description: str = None,
        packageCleanup: bool = None,
        excludeAppPackagesFromCleanup: List[str] = None,
        rebootAfterUse: bool = None,
    ) -> UpdateInstanceProfileResultTypeDef:
        """
        [Client.update_instance_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.update_instance_profile)
        """

    def update_network_profile(
        self,
        arn: str,
        name: str = None,
        description: str = None,
        type: Literal["CURATED", "PRIVATE"] = None,
        uplinkBandwidthBits: int = None,
        downlinkBandwidthBits: int = None,
        uplinkDelayMs: int = None,
        downlinkDelayMs: int = None,
        uplinkJitterMs: int = None,
        downlinkJitterMs: int = None,
        uplinkLossPercent: int = None,
        downlinkLossPercent: int = None,
    ) -> UpdateNetworkProfileResultTypeDef:
        """
        [Client.update_network_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.update_network_profile)
        """

    def update_project(
        self, arn: str, name: str = None, defaultJobTimeoutMinutes: int = None
    ) -> UpdateProjectResultTypeDef:
        """
        [Client.update_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.update_project)
        """

    def update_test_grid_project(
        self, projectArn: str, name: str = None, description: str = None
    ) -> UpdateTestGridProjectResultTypeDef:
        """
        [Client.update_test_grid_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.update_test_grid_project)
        """

    def update_upload(
        self, arn: str, name: str = None, contentType: str = None, editContent: bool = None
    ) -> UpdateUploadResultTypeDef:
        """
        [Client.update_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.update_upload)
        """

    def update_vpce_configuration(
        self,
        arn: str,
        vpceConfigurationName: str = None,
        vpceServiceName: str = None,
        serviceDnsName: str = None,
        vpceConfigurationDescription: str = None,
    ) -> UpdateVPCEConfigurationResultTypeDef:
        """
        [Client.update_vpce_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Client.update_vpce_configuration)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_offering_status"]
    ) -> GetOfferingStatusPaginator:
        """
        [Paginator.GetOfferingStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Paginator.GetOfferingStatus)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_artifacts"]) -> ListArtifactsPaginator:
        """
        [Paginator.ListArtifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Paginator.ListArtifacts)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_instances"]
    ) -> ListDeviceInstancesPaginator:
        """
        [Paginator.ListDeviceInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDeviceInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_pools"]
    ) -> ListDevicePoolsPaginator:
        """
        [Paginator.ListDevicePools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDevicePools)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_devices"]) -> ListDevicesPaginator:
        """
        [Paginator.ListDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDevices)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_profiles"]
    ) -> ListInstanceProfilesPaginator:
        """
        [Paginator.ListInstanceProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Paginator.ListInstanceProfiles)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Paginator.ListJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_network_profiles"]
    ) -> ListNetworkProfilesPaginator:
        """
        [Paginator.ListNetworkProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Paginator.ListNetworkProfiles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_offering_promotions"]
    ) -> ListOfferingPromotionsPaginator:
        """
        [Paginator.ListOfferingPromotions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferingPromotions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_offering_transactions"]
    ) -> ListOfferingTransactionsPaginator:
        """
        [Paginator.ListOfferingTransactions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferingTransactions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_offerings"]) -> ListOfferingsPaginator:
        """
        [Paginator.ListOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferings)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Paginator.ListProjects)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_remote_access_sessions"]
    ) -> ListRemoteAccessSessionsPaginator:
        """
        [Paginator.ListRemoteAccessSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Paginator.ListRemoteAccessSessions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_runs"]) -> ListRunsPaginator:
        """
        [Paginator.ListRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Paginator.ListRuns)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_samples"]) -> ListSamplesPaginator:
        """
        [Paginator.ListSamples documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Paginator.ListSamples)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_suites"]) -> ListSuitesPaginator:
        """
        [Paginator.ListSuites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Paginator.ListSuites)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tests"]) -> ListTestsPaginator:
        """
        [Paginator.ListTests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Paginator.ListTests)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_unique_problems"]
    ) -> ListUniqueProblemsPaginator:
        """
        [Paginator.ListUniqueProblems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Paginator.ListUniqueProblems)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_uploads"]) -> ListUploadsPaginator:
        """
        [Paginator.ListUploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Paginator.ListUploads)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_vpce_configurations"]
    ) -> ListVPCEConfigurationsPaginator:
        """
        [Paginator.ListVPCEConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/devicefarm.html#DeviceFarm.Paginator.ListVPCEConfigurations)
        """
