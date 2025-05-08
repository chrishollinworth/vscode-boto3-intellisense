"""
Type annotations for devicefarm service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_devicefarm.client import DeviceFarmClient

    session = Session()
    client: DeviceFarmClient = session.client("devicefarm")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

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
    CreateDevicePoolRequestTypeDef,
    CreateDevicePoolResultTypeDef,
    CreateInstanceProfileRequestTypeDef,
    CreateInstanceProfileResultTypeDef,
    CreateNetworkProfileRequestTypeDef,
    CreateNetworkProfileResultTypeDef,
    CreateProjectRequestTypeDef,
    CreateProjectResultTypeDef,
    CreateRemoteAccessSessionRequestTypeDef,
    CreateRemoteAccessSessionResultTypeDef,
    CreateTestGridProjectRequestTypeDef,
    CreateTestGridProjectResultTypeDef,
    CreateTestGridUrlRequestTypeDef,
    CreateTestGridUrlResultTypeDef,
    CreateUploadRequestTypeDef,
    CreateUploadResultTypeDef,
    CreateVPCEConfigurationRequestTypeDef,
    CreateVPCEConfigurationResultTypeDef,
    DeleteDevicePoolRequestTypeDef,
    DeleteInstanceProfileRequestTypeDef,
    DeleteNetworkProfileRequestTypeDef,
    DeleteProjectRequestTypeDef,
    DeleteRemoteAccessSessionRequestTypeDef,
    DeleteRunRequestTypeDef,
    DeleteTestGridProjectRequestTypeDef,
    DeleteUploadRequestTypeDef,
    DeleteVPCEConfigurationRequestTypeDef,
    GetAccountSettingsResultTypeDef,
    GetDeviceInstanceRequestTypeDef,
    GetDeviceInstanceResultTypeDef,
    GetDevicePoolCompatibilityRequestTypeDef,
    GetDevicePoolCompatibilityResultTypeDef,
    GetDevicePoolRequestTypeDef,
    GetDevicePoolResultTypeDef,
    GetDeviceRequestTypeDef,
    GetDeviceResultTypeDef,
    GetInstanceProfileRequestTypeDef,
    GetInstanceProfileResultTypeDef,
    GetJobRequestTypeDef,
    GetJobResultTypeDef,
    GetNetworkProfileRequestTypeDef,
    GetNetworkProfileResultTypeDef,
    GetOfferingStatusRequestTypeDef,
    GetOfferingStatusResultTypeDef,
    GetProjectRequestTypeDef,
    GetProjectResultTypeDef,
    GetRemoteAccessSessionRequestTypeDef,
    GetRemoteAccessSessionResultTypeDef,
    GetRunRequestTypeDef,
    GetRunResultTypeDef,
    GetSuiteRequestTypeDef,
    GetSuiteResultTypeDef,
    GetTestGridProjectRequestTypeDef,
    GetTestGridProjectResultTypeDef,
    GetTestGridSessionRequestTypeDef,
    GetTestGridSessionResultTypeDef,
    GetTestRequestTypeDef,
    GetTestResultTypeDef,
    GetUploadRequestTypeDef,
    GetUploadResultTypeDef,
    GetVPCEConfigurationRequestTypeDef,
    GetVPCEConfigurationResultTypeDef,
    InstallToRemoteAccessSessionRequestTypeDef,
    InstallToRemoteAccessSessionResultTypeDef,
    ListArtifactsRequestTypeDef,
    ListArtifactsResultTypeDef,
    ListDeviceInstancesRequestTypeDef,
    ListDeviceInstancesResultTypeDef,
    ListDevicePoolsRequestTypeDef,
    ListDevicePoolsResultTypeDef,
    ListDevicesRequestTypeDef,
    ListDevicesResultTypeDef,
    ListInstanceProfilesRequestTypeDef,
    ListInstanceProfilesResultTypeDef,
    ListJobsRequestTypeDef,
    ListJobsResultTypeDef,
    ListNetworkProfilesRequestTypeDef,
    ListNetworkProfilesResultTypeDef,
    ListOfferingPromotionsRequestTypeDef,
    ListOfferingPromotionsResultTypeDef,
    ListOfferingsRequestTypeDef,
    ListOfferingsResultTypeDef,
    ListOfferingTransactionsRequestTypeDef,
    ListOfferingTransactionsResultTypeDef,
    ListProjectsRequestTypeDef,
    ListProjectsResultTypeDef,
    ListRemoteAccessSessionsRequestTypeDef,
    ListRemoteAccessSessionsResultTypeDef,
    ListRunsRequestTypeDef,
    ListRunsResultTypeDef,
    ListSamplesRequestTypeDef,
    ListSamplesResultTypeDef,
    ListSuitesRequestTypeDef,
    ListSuitesResultTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTestGridProjectsRequestTypeDef,
    ListTestGridProjectsResultTypeDef,
    ListTestGridSessionActionsRequestTypeDef,
    ListTestGridSessionActionsResultTypeDef,
    ListTestGridSessionArtifactsRequestTypeDef,
    ListTestGridSessionArtifactsResultTypeDef,
    ListTestGridSessionsRequestTypeDef,
    ListTestGridSessionsResultTypeDef,
    ListTestsRequestTypeDef,
    ListTestsResultTypeDef,
    ListUniqueProblemsRequestTypeDef,
    ListUniqueProblemsResultTypeDef,
    ListUploadsRequestTypeDef,
    ListUploadsResultTypeDef,
    ListVPCEConfigurationsRequestTypeDef,
    ListVPCEConfigurationsResultTypeDef,
    PurchaseOfferingRequestTypeDef,
    PurchaseOfferingResultTypeDef,
    RenewOfferingRequestTypeDef,
    RenewOfferingResultTypeDef,
    ScheduleRunRequestTypeDef,
    ScheduleRunResultTypeDef,
    StopJobRequestTypeDef,
    StopJobResultTypeDef,
    StopRemoteAccessSessionRequestTypeDef,
    StopRemoteAccessSessionResultTypeDef,
    StopRunRequestTypeDef,
    StopRunResultTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateDeviceInstanceRequestTypeDef,
    UpdateDeviceInstanceResultTypeDef,
    UpdateDevicePoolRequestTypeDef,
    UpdateDevicePoolResultTypeDef,
    UpdateInstanceProfileRequestTypeDef,
    UpdateInstanceProfileResultTypeDef,
    UpdateNetworkProfileRequestTypeDef,
    UpdateNetworkProfileResultTypeDef,
    UpdateProjectRequestTypeDef,
    UpdateProjectResultTypeDef,
    UpdateTestGridProjectRequestTypeDef,
    UpdateTestGridProjectResultTypeDef,
    UpdateUploadRequestTypeDef,
    UpdateUploadResultTypeDef,
    UpdateVPCEConfigurationRequestTypeDef,
    UpdateVPCEConfigurationResultTypeDef,
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

__all__ = ("DeviceFarmClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DeviceFarmClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm.html#DeviceFarm.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#generate_presigned_url)
        """

    def create_device_pool(
        self, **kwargs: Unpack[CreateDevicePoolRequestTypeDef]
    ) -> CreateDevicePoolResultTypeDef:
        """
        Creates a device pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/create_device_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#create_device_pool)
        """

    def create_instance_profile(
        self, **kwargs: Unpack[CreateInstanceProfileRequestTypeDef]
    ) -> CreateInstanceProfileResultTypeDef:
        """
        Creates a profile that can be applied to one or more private fleet device
        instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/create_instance_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#create_instance_profile)
        """

    def create_network_profile(
        self, **kwargs: Unpack[CreateNetworkProfileRequestTypeDef]
    ) -> CreateNetworkProfileResultTypeDef:
        """
        Creates a network profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/create_network_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#create_network_profile)
        """

    def create_project(
        self, **kwargs: Unpack[CreateProjectRequestTypeDef]
    ) -> CreateProjectResultTypeDef:
        """
        Creates a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/create_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#create_project)
        """

    def create_remote_access_session(
        self, **kwargs: Unpack[CreateRemoteAccessSessionRequestTypeDef]
    ) -> CreateRemoteAccessSessionResultTypeDef:
        """
        Specifies and starts a remote access session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/create_remote_access_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#create_remote_access_session)
        """

    def create_test_grid_project(
        self, **kwargs: Unpack[CreateTestGridProjectRequestTypeDef]
    ) -> CreateTestGridProjectResultTypeDef:
        """
        Creates a Selenium testing project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/create_test_grid_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#create_test_grid_project)
        """

    def create_test_grid_url(
        self, **kwargs: Unpack[CreateTestGridUrlRequestTypeDef]
    ) -> CreateTestGridUrlResultTypeDef:
        """
        Creates a signed, short-term URL that can be passed to a Selenium
        <code>RemoteWebDriver</code> constructor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/create_test_grid_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#create_test_grid_url)
        """

    def create_upload(
        self, **kwargs: Unpack[CreateUploadRequestTypeDef]
    ) -> CreateUploadResultTypeDef:
        """
        Uploads an app or test scripts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/create_upload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#create_upload)
        """

    def create_vpce_configuration(
        self, **kwargs: Unpack[CreateVPCEConfigurationRequestTypeDef]
    ) -> CreateVPCEConfigurationResultTypeDef:
        """
        Creates a configuration record in Device Farm for your Amazon Virtual Private
        Cloud (VPC) endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/create_vpce_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#create_vpce_configuration)
        """

    def delete_device_pool(
        self, **kwargs: Unpack[DeleteDevicePoolRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a device pool given the pool ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/delete_device_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#delete_device_pool)
        """

    def delete_instance_profile(
        self, **kwargs: Unpack[DeleteInstanceProfileRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a profile that can be applied to one or more private device instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/delete_instance_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#delete_instance_profile)
        """

    def delete_network_profile(
        self, **kwargs: Unpack[DeleteNetworkProfileRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a network profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/delete_network_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#delete_network_profile)
        """

    def delete_project(self, **kwargs: Unpack[DeleteProjectRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an AWS Device Farm project, given the project ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/delete_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#delete_project)
        """

    def delete_remote_access_session(
        self, **kwargs: Unpack[DeleteRemoteAccessSessionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a completed remote access session and its results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/delete_remote_access_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#delete_remote_access_session)
        """

    def delete_run(self, **kwargs: Unpack[DeleteRunRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the run, given the run ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/delete_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#delete_run)
        """

    def delete_test_grid_project(
        self, **kwargs: Unpack[DeleteTestGridProjectRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a Selenium testing project and all content generated under it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/delete_test_grid_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#delete_test_grid_project)
        """

    def delete_upload(self, **kwargs: Unpack[DeleteUploadRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an upload given the upload ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/delete_upload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#delete_upload)
        """

    def delete_vpce_configuration(
        self, **kwargs: Unpack[DeleteVPCEConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a configuration for your Amazon Virtual Private Cloud (VPC) endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/delete_vpce_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#delete_vpce_configuration)
        """

    def get_account_settings(self) -> GetAccountSettingsResultTypeDef:
        """
        Returns the number of unmetered iOS or unmetered Android devices that have been
        purchased by the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_account_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_account_settings)
        """

    def get_device(self, **kwargs: Unpack[GetDeviceRequestTypeDef]) -> GetDeviceResultTypeDef:
        """
        Gets information about a unique device type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_device)
        """

    def get_device_instance(
        self, **kwargs: Unpack[GetDeviceInstanceRequestTypeDef]
    ) -> GetDeviceInstanceResultTypeDef:
        """
        Returns information about a device instance that belongs to a private device
        fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_device_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_device_instance)
        """

    def get_device_pool(
        self, **kwargs: Unpack[GetDevicePoolRequestTypeDef]
    ) -> GetDevicePoolResultTypeDef:
        """
        Gets information about a device pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_device_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_device_pool)
        """

    def get_device_pool_compatibility(
        self, **kwargs: Unpack[GetDevicePoolCompatibilityRequestTypeDef]
    ) -> GetDevicePoolCompatibilityResultTypeDef:
        """
        Gets information about compatibility with a device pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_device_pool_compatibility.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_device_pool_compatibility)
        """

    def get_instance_profile(
        self, **kwargs: Unpack[GetInstanceProfileRequestTypeDef]
    ) -> GetInstanceProfileResultTypeDef:
        """
        Returns information about the specified instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_instance_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_instance_profile)
        """

    def get_job(self, **kwargs: Unpack[GetJobRequestTypeDef]) -> GetJobResultTypeDef:
        """
        Gets information about a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_job)
        """

    def get_network_profile(
        self, **kwargs: Unpack[GetNetworkProfileRequestTypeDef]
    ) -> GetNetworkProfileResultTypeDef:
        """
        Returns information about a network profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_network_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_network_profile)
        """

    def get_offering_status(
        self, **kwargs: Unpack[GetOfferingStatusRequestTypeDef]
    ) -> GetOfferingStatusResultTypeDef:
        """
        Gets the current status and future status of all offerings purchased by an AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_offering_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_offering_status)
        """

    def get_project(self, **kwargs: Unpack[GetProjectRequestTypeDef]) -> GetProjectResultTypeDef:
        """
        Gets information about a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_project)
        """

    def get_remote_access_session(
        self, **kwargs: Unpack[GetRemoteAccessSessionRequestTypeDef]
    ) -> GetRemoteAccessSessionResultTypeDef:
        """
        Returns a link to a currently running remote access session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_remote_access_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_remote_access_session)
        """

    def get_run(self, **kwargs: Unpack[GetRunRequestTypeDef]) -> GetRunResultTypeDef:
        """
        Gets information about a run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_run)
        """

    def get_suite(self, **kwargs: Unpack[GetSuiteRequestTypeDef]) -> GetSuiteResultTypeDef:
        """
        Gets information about a suite.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_suite.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_suite)
        """

    def get_test(self, **kwargs: Unpack[GetTestRequestTypeDef]) -> GetTestResultTypeDef:
        """
        Gets information about a test.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_test.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_test)
        """

    def get_test_grid_project(
        self, **kwargs: Unpack[GetTestGridProjectRequestTypeDef]
    ) -> GetTestGridProjectResultTypeDef:
        """
        Retrieves information about a Selenium testing project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_test_grid_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_test_grid_project)
        """

    def get_test_grid_session(
        self, **kwargs: Unpack[GetTestGridSessionRequestTypeDef]
    ) -> GetTestGridSessionResultTypeDef:
        """
        A session is an instance of a browser created through a
        <code>RemoteWebDriver</code> with the URL from
        <a>CreateTestGridUrlResult$url</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_test_grid_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_test_grid_session)
        """

    def get_upload(self, **kwargs: Unpack[GetUploadRequestTypeDef]) -> GetUploadResultTypeDef:
        """
        Gets information about an upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_upload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_upload)
        """

    def get_vpce_configuration(
        self, **kwargs: Unpack[GetVPCEConfigurationRequestTypeDef]
    ) -> GetVPCEConfigurationResultTypeDef:
        """
        Returns information about the configuration settings for your Amazon Virtual
        Private Cloud (VPC) endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_vpce_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_vpce_configuration)
        """

    def install_to_remote_access_session(
        self, **kwargs: Unpack[InstallToRemoteAccessSessionRequestTypeDef]
    ) -> InstallToRemoteAccessSessionResultTypeDef:
        """
        Installs an application to the device in a remote access session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/install_to_remote_access_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#install_to_remote_access_session)
        """

    def list_artifacts(
        self, **kwargs: Unpack[ListArtifactsRequestTypeDef]
    ) -> ListArtifactsResultTypeDef:
        """
        Gets information about artifacts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_artifacts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_artifacts)
        """

    def list_device_instances(
        self, **kwargs: Unpack[ListDeviceInstancesRequestTypeDef]
    ) -> ListDeviceInstancesResultTypeDef:
        """
        Returns information about the private device instances associated with one or
        more AWS accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_device_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_device_instances)
        """

    def list_device_pools(
        self, **kwargs: Unpack[ListDevicePoolsRequestTypeDef]
    ) -> ListDevicePoolsResultTypeDef:
        """
        Gets information about device pools.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_device_pools.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_device_pools)
        """

    def list_devices(self, **kwargs: Unpack[ListDevicesRequestTypeDef]) -> ListDevicesResultTypeDef:
        """
        Gets information about unique device types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_devices.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_devices)
        """

    def list_instance_profiles(
        self, **kwargs: Unpack[ListInstanceProfilesRequestTypeDef]
    ) -> ListInstanceProfilesResultTypeDef:
        """
        Returns information about all the instance profiles in an AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_instance_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_instance_profiles)
        """

    def list_jobs(self, **kwargs: Unpack[ListJobsRequestTypeDef]) -> ListJobsResultTypeDef:
        """
        Gets information about jobs for a given test run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_jobs)
        """

    def list_network_profiles(
        self, **kwargs: Unpack[ListNetworkProfilesRequestTypeDef]
    ) -> ListNetworkProfilesResultTypeDef:
        """
        Returns the list of available network profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_network_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_network_profiles)
        """

    def list_offering_promotions(
        self, **kwargs: Unpack[ListOfferingPromotionsRequestTypeDef]
    ) -> ListOfferingPromotionsResultTypeDef:
        """
        Returns a list of offering promotions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_offering_promotions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_offering_promotions)
        """

    def list_offering_transactions(
        self, **kwargs: Unpack[ListOfferingTransactionsRequestTypeDef]
    ) -> ListOfferingTransactionsResultTypeDef:
        """
        Returns a list of all historical purchases, renewals, and system renewal
        transactions for an AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_offering_transactions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_offering_transactions)
        """

    def list_offerings(
        self, **kwargs: Unpack[ListOfferingsRequestTypeDef]
    ) -> ListOfferingsResultTypeDef:
        """
        Returns a list of products or offerings that the user can manage through the
        API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_offerings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_offerings)
        """

    def list_projects(
        self, **kwargs: Unpack[ListProjectsRequestTypeDef]
    ) -> ListProjectsResultTypeDef:
        """
        Gets information about projects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_projects.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_projects)
        """

    def list_remote_access_sessions(
        self, **kwargs: Unpack[ListRemoteAccessSessionsRequestTypeDef]
    ) -> ListRemoteAccessSessionsResultTypeDef:
        """
        Returns a list of all currently running remote access sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_remote_access_sessions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_remote_access_sessions)
        """

    def list_runs(self, **kwargs: Unpack[ListRunsRequestTypeDef]) -> ListRunsResultTypeDef:
        """
        Gets information about runs, given an AWS Device Farm project ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_runs)
        """

    def list_samples(self, **kwargs: Unpack[ListSamplesRequestTypeDef]) -> ListSamplesResultTypeDef:
        """
        Gets information about samples, given an AWS Device Farm job ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_samples.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_samples)
        """

    def list_suites(self, **kwargs: Unpack[ListSuitesRequestTypeDef]) -> ListSuitesResultTypeDef:
        """
        Gets information about test suites for a given job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_suites.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_suites)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        List the tags for an AWS Device Farm resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_tags_for_resource)
        """

    def list_test_grid_projects(
        self, **kwargs: Unpack[ListTestGridProjectsRequestTypeDef]
    ) -> ListTestGridProjectsResultTypeDef:
        """
        Gets a list of all Selenium testing projects in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_test_grid_projects.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_test_grid_projects)
        """

    def list_test_grid_session_actions(
        self, **kwargs: Unpack[ListTestGridSessionActionsRequestTypeDef]
    ) -> ListTestGridSessionActionsResultTypeDef:
        """
        Returns a list of the actions taken in a <a>TestGridSession</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_test_grid_session_actions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_test_grid_session_actions)
        """

    def list_test_grid_session_artifacts(
        self, **kwargs: Unpack[ListTestGridSessionArtifactsRequestTypeDef]
    ) -> ListTestGridSessionArtifactsResultTypeDef:
        """
        Retrieves a list of artifacts created during the session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_test_grid_session_artifacts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_test_grid_session_artifacts)
        """

    def list_test_grid_sessions(
        self, **kwargs: Unpack[ListTestGridSessionsRequestTypeDef]
    ) -> ListTestGridSessionsResultTypeDef:
        """
        Retrieves a list of sessions for a <a>TestGridProject</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_test_grid_sessions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_test_grid_sessions)
        """

    def list_tests(self, **kwargs: Unpack[ListTestsRequestTypeDef]) -> ListTestsResultTypeDef:
        """
        Gets information about tests in a given test suite.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_tests.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_tests)
        """

    def list_unique_problems(
        self, **kwargs: Unpack[ListUniqueProblemsRequestTypeDef]
    ) -> ListUniqueProblemsResultTypeDef:
        """
        Gets information about unique problems, such as exceptions or crashes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_unique_problems.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_unique_problems)
        """

    def list_uploads(self, **kwargs: Unpack[ListUploadsRequestTypeDef]) -> ListUploadsResultTypeDef:
        """
        Gets information about uploads, given an AWS Device Farm project ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_uploads.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_uploads)
        """

    def list_vpce_configurations(
        self, **kwargs: Unpack[ListVPCEConfigurationsRequestTypeDef]
    ) -> ListVPCEConfigurationsResultTypeDef:
        """
        Returns information about all Amazon Virtual Private Cloud (VPC) endpoint
        configurations in the AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/list_vpce_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#list_vpce_configurations)
        """

    def purchase_offering(
        self, **kwargs: Unpack[PurchaseOfferingRequestTypeDef]
    ) -> PurchaseOfferingResultTypeDef:
        """
        Immediately purchases offerings for an AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/purchase_offering.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#purchase_offering)
        """

    def renew_offering(
        self, **kwargs: Unpack[RenewOfferingRequestTypeDef]
    ) -> RenewOfferingResultTypeDef:
        """
        Explicitly sets the quantity of devices to renew for an offering, starting from
        the <code>effectiveDate</code> of the next period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/renew_offering.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#renew_offering)
        """

    def schedule_run(self, **kwargs: Unpack[ScheduleRunRequestTypeDef]) -> ScheduleRunResultTypeDef:
        """
        Schedules a run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/schedule_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#schedule_run)
        """

    def stop_job(self, **kwargs: Unpack[StopJobRequestTypeDef]) -> StopJobResultTypeDef:
        """
        Initiates a stop request for the current job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/stop_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#stop_job)
        """

    def stop_remote_access_session(
        self, **kwargs: Unpack[StopRemoteAccessSessionRequestTypeDef]
    ) -> StopRemoteAccessSessionResultTypeDef:
        """
        Ends a specified remote access session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/stop_remote_access_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#stop_remote_access_session)
        """

    def stop_run(self, **kwargs: Unpack[StopRunRequestTypeDef]) -> StopRunResultTypeDef:
        """
        Initiates a stop request for the current test run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/stop_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#stop_run)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Associates the specified tags to a resource with the specified
        <code>resourceArn</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#untag_resource)
        """

    def update_device_instance(
        self, **kwargs: Unpack[UpdateDeviceInstanceRequestTypeDef]
    ) -> UpdateDeviceInstanceResultTypeDef:
        """
        Updates information about a private device instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/update_device_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#update_device_instance)
        """

    def update_device_pool(
        self, **kwargs: Unpack[UpdateDevicePoolRequestTypeDef]
    ) -> UpdateDevicePoolResultTypeDef:
        """
        Modifies the name, description, and rules in a device pool given the attributes
        and the pool ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/update_device_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#update_device_pool)
        """

    def update_instance_profile(
        self, **kwargs: Unpack[UpdateInstanceProfileRequestTypeDef]
    ) -> UpdateInstanceProfileResultTypeDef:
        """
        Updates information about an existing private device instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/update_instance_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#update_instance_profile)
        """

    def update_network_profile(
        self, **kwargs: Unpack[UpdateNetworkProfileRequestTypeDef]
    ) -> UpdateNetworkProfileResultTypeDef:
        """
        Updates the network profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/update_network_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#update_network_profile)
        """

    def update_project(
        self, **kwargs: Unpack[UpdateProjectRequestTypeDef]
    ) -> UpdateProjectResultTypeDef:
        """
        Modifies the specified project name, given the project ARN and a new name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/update_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#update_project)
        """

    def update_test_grid_project(
        self, **kwargs: Unpack[UpdateTestGridProjectRequestTypeDef]
    ) -> UpdateTestGridProjectResultTypeDef:
        """
        Change details of a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/update_test_grid_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#update_test_grid_project)
        """

    def update_upload(
        self, **kwargs: Unpack[UpdateUploadRequestTypeDef]
    ) -> UpdateUploadResultTypeDef:
        """
        Updates an uploaded test spec.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/update_upload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#update_upload)
        """

    def update_vpce_configuration(
        self, **kwargs: Unpack[UpdateVPCEConfigurationRequestTypeDef]
    ) -> UpdateVPCEConfigurationResultTypeDef:
        """
        Updates information about an Amazon Virtual Private Cloud (VPC) endpoint
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/update_vpce_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#update_vpce_configuration)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_offering_status"]
    ) -> GetOfferingStatusPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_artifacts"]
    ) -> ListArtifactsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_device_instances"]
    ) -> ListDeviceInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_device_pools"]
    ) -> ListDevicePoolsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_devices"]
    ) -> ListDevicesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_instance_profiles"]
    ) -> ListInstanceProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_jobs"]
    ) -> ListJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_network_profiles"]
    ) -> ListNetworkProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_offering_promotions"]
    ) -> ListOfferingPromotionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_offering_transactions"]
    ) -> ListOfferingTransactionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_offerings"]
    ) -> ListOfferingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_projects"]
    ) -> ListProjectsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_remote_access_sessions"]
    ) -> ListRemoteAccessSessionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_runs"]
    ) -> ListRunsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_samples"]
    ) -> ListSamplesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_suites"]
    ) -> ListSuitesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tests"]
    ) -> ListTestsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_unique_problems"]
    ) -> ListUniqueProblemsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_uploads"]
    ) -> ListUploadsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_vpce_configurations"]
    ) -> ListVPCEConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/client/#get_paginator)
        """
