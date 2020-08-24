# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for devicefarm service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_devicefarm import DeviceFarmClient
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
        ListOfferingTransactionsPaginator,
        ListOfferingsPaginator,
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

    client: DeviceFarmClient = boto3.client("devicefarm")

    get_offering_status_paginator: GetOfferingStatusPaginator = client.get_paginator("get_offering_status")
    list_artifacts_paginator: ListArtifactsPaginator = client.get_paginator("list_artifacts")
    list_device_instances_paginator: ListDeviceInstancesPaginator = client.get_paginator("list_device_instances")
    list_device_pools_paginator: ListDevicePoolsPaginator = client.get_paginator("list_device_pools")
    list_devices_paginator: ListDevicesPaginator = client.get_paginator("list_devices")
    list_instance_profiles_paginator: ListInstanceProfilesPaginator = client.get_paginator("list_instance_profiles")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    list_network_profiles_paginator: ListNetworkProfilesPaginator = client.get_paginator("list_network_profiles")
    list_offering_promotions_paginator: ListOfferingPromotionsPaginator = client.get_paginator("list_offering_promotions")
    list_offering_transactions_paginator: ListOfferingTransactionsPaginator = client.get_paginator("list_offering_transactions")
    list_offerings_paginator: ListOfferingsPaginator = client.get_paginator("list_offerings")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    list_remote_access_sessions_paginator: ListRemoteAccessSessionsPaginator = client.get_paginator("list_remote_access_sessions")
    list_runs_paginator: ListRunsPaginator = client.get_paginator("list_runs")
    list_samples_paginator: ListSamplesPaginator = client.get_paginator("list_samples")
    list_suites_paginator: ListSuitesPaginator = client.get_paginator("list_suites")
    list_tests_paginator: ListTestsPaginator = client.get_paginator("list_tests")
    list_unique_problems_paginator: ListUniqueProblemsPaginator = client.get_paginator("list_unique_problems")
    list_uploads_paginator: ListUploadsPaginator = client.get_paginator("list_uploads")
    list_vpce_configurations_paginator: ListVPCEConfigurationsPaginator = client.get_paginator("list_vpce_configurations")
    ```
"""
import sys
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_devicefarm.type_defs import (
    DeviceFilterTypeDef,
    GetOfferingStatusResultTypeDef,
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
    ListTestsResultTypeDef,
    ListUniqueProblemsResultTypeDef,
    ListUploadsResultTypeDef,
    ListVPCEConfigurationsResultTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetOfferingStatusPaginator",
    "ListArtifactsPaginator",
    "ListDeviceInstancesPaginator",
    "ListDevicePoolsPaginator",
    "ListDevicesPaginator",
    "ListInstanceProfilesPaginator",
    "ListJobsPaginator",
    "ListNetworkProfilesPaginator",
    "ListOfferingPromotionsPaginator",
    "ListOfferingTransactionsPaginator",
    "ListOfferingsPaginator",
    "ListProjectsPaginator",
    "ListRemoteAccessSessionsPaginator",
    "ListRunsPaginator",
    "ListSamplesPaginator",
    "ListSuitesPaginator",
    "ListTestsPaginator",
    "ListUniqueProblemsPaginator",
    "ListUploadsPaginator",
    "ListVPCEConfigurationsPaginator",
)


class GetOfferingStatusPaginator(Boto3Paginator):
    """
    [Paginator.GetOfferingStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.GetOfferingStatus)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetOfferingStatusResultTypeDef]:
        """
        [GetOfferingStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.GetOfferingStatus.paginate)
        """


class ListArtifactsPaginator(Boto3Paginator):
    """
    [Paginator.ListArtifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListArtifacts)
    """

    def paginate(
        self,
        arn: str,
        type: Literal["SCREENSHOT", "FILE", "LOG"],
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListArtifactsResultTypeDef]:
        """
        [ListArtifacts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListArtifacts.paginate)
        """


class ListDeviceInstancesPaginator(Boto3Paginator):
    """
    [Paginator.ListDeviceInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDeviceInstances)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeviceInstancesResultTypeDef]:
        """
        [ListDeviceInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDeviceInstances.paginate)
        """


class ListDevicePoolsPaginator(Boto3Paginator):
    """
    [Paginator.ListDevicePools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDevicePools)
    """

    def paginate(
        self,
        arn: str,
        type: Literal["CURATED", "PRIVATE"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDevicePoolsResultTypeDef]:
        """
        [ListDevicePools.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDevicePools.paginate)
        """


class ListDevicesPaginator(Boto3Paginator):
    """
    [Paginator.ListDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDevices)
    """

    def paginate(
        self,
        arn: str = None,
        filters: List["DeviceFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDevicesResultTypeDef]:
        """
        [ListDevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListDevices.paginate)
        """


class ListInstanceProfilesPaginator(Boto3Paginator):
    """
    [Paginator.ListInstanceProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListInstanceProfiles)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstanceProfilesResultTypeDef]:
        """
        [ListInstanceProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListInstanceProfiles.paginate)
        """


class ListJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListJobs)
    """

    def paginate(
        self, arn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobsResultTypeDef]:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListJobs.paginate)
        """


class ListNetworkProfilesPaginator(Boto3Paginator):
    """
    [Paginator.ListNetworkProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListNetworkProfiles)
    """

    def paginate(
        self,
        arn: str,
        type: Literal["CURATED", "PRIVATE"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListNetworkProfilesResultTypeDef]:
        """
        [ListNetworkProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListNetworkProfiles.paginate)
        """


class ListOfferingPromotionsPaginator(Boto3Paginator):
    """
    [Paginator.ListOfferingPromotions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferingPromotions)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOfferingPromotionsResultTypeDef]:
        """
        [ListOfferingPromotions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferingPromotions.paginate)
        """


class ListOfferingTransactionsPaginator(Boto3Paginator):
    """
    [Paginator.ListOfferingTransactions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferingTransactions)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOfferingTransactionsResultTypeDef]:
        """
        [ListOfferingTransactions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferingTransactions.paginate)
        """


class ListOfferingsPaginator(Boto3Paginator):
    """
    [Paginator.ListOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferings)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOfferingsResultTypeDef]:
        """
        [ListOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListOfferings.paginate)
        """


class ListProjectsPaginator(Boto3Paginator):
    """
    [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListProjects)
    """

    def paginate(
        self, arn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectsResultTypeDef]:
        """
        [ListProjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListProjects.paginate)
        """


class ListRemoteAccessSessionsPaginator(Boto3Paginator):
    """
    [Paginator.ListRemoteAccessSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListRemoteAccessSessions)
    """

    def paginate(
        self, arn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRemoteAccessSessionsResultTypeDef]:
        """
        [ListRemoteAccessSessions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListRemoteAccessSessions.paginate)
        """


class ListRunsPaginator(Boto3Paginator):
    """
    [Paginator.ListRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListRuns)
    """

    def paginate(
        self, arn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRunsResultTypeDef]:
        """
        [ListRuns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListRuns.paginate)
        """


class ListSamplesPaginator(Boto3Paginator):
    """
    [Paginator.ListSamples documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListSamples)
    """

    def paginate(
        self, arn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSamplesResultTypeDef]:
        """
        [ListSamples.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListSamples.paginate)
        """


class ListSuitesPaginator(Boto3Paginator):
    """
    [Paginator.ListSuites documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListSuites)
    """

    def paginate(
        self, arn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSuitesResultTypeDef]:
        """
        [ListSuites.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListSuites.paginate)
        """


class ListTestsPaginator(Boto3Paginator):
    """
    [Paginator.ListTests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListTests)
    """

    def paginate(
        self, arn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTestsResultTypeDef]:
        """
        [ListTests.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListTests.paginate)
        """


class ListUniqueProblemsPaginator(Boto3Paginator):
    """
    [Paginator.ListUniqueProblems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListUniqueProblems)
    """

    def paginate(
        self, arn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListUniqueProblemsResultTypeDef]:
        """
        [ListUniqueProblems.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListUniqueProblems.paginate)
        """


class ListUploadsPaginator(Boto3Paginator):
    """
    [Paginator.ListUploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListUploads)
    """

    def paginate(
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
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListUploadsResultTypeDef]:
        """
        [ListUploads.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListUploads.paginate)
        """


class ListVPCEConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.ListVPCEConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListVPCEConfigurations)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVPCEConfigurationsResultTypeDef]:
        """
        [ListVPCEConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/devicefarm.html#DeviceFarm.Paginator.ListVPCEConfigurations.paginate)
        """
