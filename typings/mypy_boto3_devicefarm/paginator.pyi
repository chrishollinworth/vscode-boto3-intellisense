"""
Type annotations for devicefarm service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_devicefarm.client import DeviceFarmClient
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

    session = Session()
    client: DeviceFarmClient = session.client("devicefarm")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetOfferingStatusRequestPaginateTypeDef,
    GetOfferingStatusResultTypeDef,
    ListArtifactsRequestPaginateTypeDef,
    ListArtifactsResultTypeDef,
    ListDeviceInstancesRequestPaginateTypeDef,
    ListDeviceInstancesResultTypeDef,
    ListDevicePoolsRequestPaginateTypeDef,
    ListDevicePoolsResultTypeDef,
    ListDevicesRequestPaginateTypeDef,
    ListDevicesResultTypeDef,
    ListInstanceProfilesRequestPaginateTypeDef,
    ListInstanceProfilesResultTypeDef,
    ListJobsRequestPaginateTypeDef,
    ListJobsResultTypeDef,
    ListNetworkProfilesRequestPaginateTypeDef,
    ListNetworkProfilesResultTypeDef,
    ListOfferingPromotionsRequestPaginateTypeDef,
    ListOfferingPromotionsResultTypeDef,
    ListOfferingsRequestPaginateTypeDef,
    ListOfferingsResultTypeDef,
    ListOfferingTransactionsRequestPaginateTypeDef,
    ListOfferingTransactionsResultTypeDef,
    ListProjectsRequestPaginateTypeDef,
    ListProjectsResultTypeDef,
    ListRemoteAccessSessionsRequestPaginateTypeDef,
    ListRemoteAccessSessionsResultTypeDef,
    ListRunsRequestPaginateTypeDef,
    ListRunsResultTypeDef,
    ListSamplesRequestPaginateTypeDef,
    ListSamplesResultTypeDef,
    ListSuitesRequestPaginateTypeDef,
    ListSuitesResultTypeDef,
    ListTestsRequestPaginateTypeDef,
    ListTestsResultTypeDef,
    ListUniqueProblemsRequestPaginateTypeDef,
    ListUniqueProblemsResultTypeDef,
    ListUploadsRequestPaginateTypeDef,
    ListUploadsResultTypeDef,
    ListVPCEConfigurationsRequestPaginateTypeDef,
    ListVPCEConfigurationsResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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

if TYPE_CHECKING:
    _GetOfferingStatusPaginatorBase = Paginator[GetOfferingStatusResultTypeDef]
else:
    _GetOfferingStatusPaginatorBase = Paginator  # type: ignore[assignment]

class GetOfferingStatusPaginator(_GetOfferingStatusPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/GetOfferingStatus.html#DeviceFarm.Paginator.GetOfferingStatus)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#getofferingstatuspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetOfferingStatusRequestPaginateTypeDef]
    ) -> PageIterator[GetOfferingStatusResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/GetOfferingStatus.html#DeviceFarm.Paginator.GetOfferingStatus.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#getofferingstatuspaginator)
        """

if TYPE_CHECKING:
    _ListArtifactsPaginatorBase = Paginator[ListArtifactsResultTypeDef]
else:
    _ListArtifactsPaginatorBase = Paginator  # type: ignore[assignment]

class ListArtifactsPaginator(_ListArtifactsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListArtifacts.html#DeviceFarm.Paginator.ListArtifacts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listartifactspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListArtifactsRequestPaginateTypeDef]
    ) -> PageIterator[ListArtifactsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListArtifacts.html#DeviceFarm.Paginator.ListArtifacts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listartifactspaginator)
        """

if TYPE_CHECKING:
    _ListDeviceInstancesPaginatorBase = Paginator[ListDeviceInstancesResultTypeDef]
else:
    _ListDeviceInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDeviceInstancesPaginator(_ListDeviceInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListDeviceInstances.html#DeviceFarm.Paginator.ListDeviceInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listdeviceinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDeviceInstancesRequestPaginateTypeDef]
    ) -> PageIterator[ListDeviceInstancesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListDeviceInstances.html#DeviceFarm.Paginator.ListDeviceInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listdeviceinstancespaginator)
        """

if TYPE_CHECKING:
    _ListDevicePoolsPaginatorBase = Paginator[ListDevicePoolsResultTypeDef]
else:
    _ListDevicePoolsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDevicePoolsPaginator(_ListDevicePoolsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListDevicePools.html#DeviceFarm.Paginator.ListDevicePools)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listdevicepoolspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDevicePoolsRequestPaginateTypeDef]
    ) -> PageIterator[ListDevicePoolsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListDevicePools.html#DeviceFarm.Paginator.ListDevicePools.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listdevicepoolspaginator)
        """

if TYPE_CHECKING:
    _ListDevicesPaginatorBase = Paginator[ListDevicesResultTypeDef]
else:
    _ListDevicesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDevicesPaginator(_ListDevicesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListDevices.html#DeviceFarm.Paginator.ListDevices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listdevicespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDevicesRequestPaginateTypeDef]
    ) -> PageIterator[ListDevicesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListDevices.html#DeviceFarm.Paginator.ListDevices.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listdevicespaginator)
        """

if TYPE_CHECKING:
    _ListInstanceProfilesPaginatorBase = Paginator[ListInstanceProfilesResultTypeDef]
else:
    _ListInstanceProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class ListInstanceProfilesPaginator(_ListInstanceProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListInstanceProfiles.html#DeviceFarm.Paginator.ListInstanceProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listinstanceprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInstanceProfilesRequestPaginateTypeDef]
    ) -> PageIterator[ListInstanceProfilesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListInstanceProfiles.html#DeviceFarm.Paginator.ListInstanceProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listinstanceprofilespaginator)
        """

if TYPE_CHECKING:
    _ListJobsPaginatorBase = Paginator[ListJobsResultTypeDef]
else:
    _ListJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListJobsPaginator(_ListJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListJobs.html#DeviceFarm.Paginator.ListJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListJobsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListJobs.html#DeviceFarm.Paginator.ListJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listjobspaginator)
        """

if TYPE_CHECKING:
    _ListNetworkProfilesPaginatorBase = Paginator[ListNetworkProfilesResultTypeDef]
else:
    _ListNetworkProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class ListNetworkProfilesPaginator(_ListNetworkProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListNetworkProfiles.html#DeviceFarm.Paginator.ListNetworkProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listnetworkprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListNetworkProfilesRequestPaginateTypeDef]
    ) -> PageIterator[ListNetworkProfilesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListNetworkProfiles.html#DeviceFarm.Paginator.ListNetworkProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listnetworkprofilespaginator)
        """

if TYPE_CHECKING:
    _ListOfferingPromotionsPaginatorBase = Paginator[ListOfferingPromotionsResultTypeDef]
else:
    _ListOfferingPromotionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOfferingPromotionsPaginator(_ListOfferingPromotionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListOfferingPromotions.html#DeviceFarm.Paginator.ListOfferingPromotions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listofferingpromotionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOfferingPromotionsRequestPaginateTypeDef]
    ) -> PageIterator[ListOfferingPromotionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListOfferingPromotions.html#DeviceFarm.Paginator.ListOfferingPromotions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listofferingpromotionspaginator)
        """

if TYPE_CHECKING:
    _ListOfferingTransactionsPaginatorBase = Paginator[ListOfferingTransactionsResultTypeDef]
else:
    _ListOfferingTransactionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOfferingTransactionsPaginator(_ListOfferingTransactionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListOfferingTransactions.html#DeviceFarm.Paginator.ListOfferingTransactions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listofferingtransactionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOfferingTransactionsRequestPaginateTypeDef]
    ) -> PageIterator[ListOfferingTransactionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListOfferingTransactions.html#DeviceFarm.Paginator.ListOfferingTransactions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listofferingtransactionspaginator)
        """

if TYPE_CHECKING:
    _ListOfferingsPaginatorBase = Paginator[ListOfferingsResultTypeDef]
else:
    _ListOfferingsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOfferingsPaginator(_ListOfferingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListOfferings.html#DeviceFarm.Paginator.ListOfferings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listofferingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOfferingsRequestPaginateTypeDef]
    ) -> PageIterator[ListOfferingsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListOfferings.html#DeviceFarm.Paginator.ListOfferings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listofferingspaginator)
        """

if TYPE_CHECKING:
    _ListProjectsPaginatorBase = Paginator[ListProjectsResultTypeDef]
else:
    _ListProjectsPaginatorBase = Paginator  # type: ignore[assignment]

class ListProjectsPaginator(_ListProjectsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListProjects.html#DeviceFarm.Paginator.ListProjects)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listprojectspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProjectsRequestPaginateTypeDef]
    ) -> PageIterator[ListProjectsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListProjects.html#DeviceFarm.Paginator.ListProjects.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listprojectspaginator)
        """

if TYPE_CHECKING:
    _ListRemoteAccessSessionsPaginatorBase = Paginator[ListRemoteAccessSessionsResultTypeDef]
else:
    _ListRemoteAccessSessionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRemoteAccessSessionsPaginator(_ListRemoteAccessSessionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListRemoteAccessSessions.html#DeviceFarm.Paginator.ListRemoteAccessSessions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listremoteaccesssessionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRemoteAccessSessionsRequestPaginateTypeDef]
    ) -> PageIterator[ListRemoteAccessSessionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListRemoteAccessSessions.html#DeviceFarm.Paginator.ListRemoteAccessSessions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listremoteaccesssessionspaginator)
        """

if TYPE_CHECKING:
    _ListRunsPaginatorBase = Paginator[ListRunsResultTypeDef]
else:
    _ListRunsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRunsPaginator(_ListRunsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListRuns.html#DeviceFarm.Paginator.ListRuns)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listrunspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRunsRequestPaginateTypeDef]
    ) -> PageIterator[ListRunsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListRuns.html#DeviceFarm.Paginator.ListRuns.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listrunspaginator)
        """

if TYPE_CHECKING:
    _ListSamplesPaginatorBase = Paginator[ListSamplesResultTypeDef]
else:
    _ListSamplesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSamplesPaginator(_ListSamplesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListSamples.html#DeviceFarm.Paginator.ListSamples)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listsamplespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSamplesRequestPaginateTypeDef]
    ) -> PageIterator[ListSamplesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListSamples.html#DeviceFarm.Paginator.ListSamples.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listsamplespaginator)
        """

if TYPE_CHECKING:
    _ListSuitesPaginatorBase = Paginator[ListSuitesResultTypeDef]
else:
    _ListSuitesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSuitesPaginator(_ListSuitesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListSuites.html#DeviceFarm.Paginator.ListSuites)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listsuitespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSuitesRequestPaginateTypeDef]
    ) -> PageIterator[ListSuitesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListSuites.html#DeviceFarm.Paginator.ListSuites.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listsuitespaginator)
        """

if TYPE_CHECKING:
    _ListTestsPaginatorBase = Paginator[ListTestsResultTypeDef]
else:
    _ListTestsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTestsPaginator(_ListTestsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListTests.html#DeviceFarm.Paginator.ListTests)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listtestspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTestsRequestPaginateTypeDef]
    ) -> PageIterator[ListTestsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListTests.html#DeviceFarm.Paginator.ListTests.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listtestspaginator)
        """

if TYPE_CHECKING:
    _ListUniqueProblemsPaginatorBase = Paginator[ListUniqueProblemsResultTypeDef]
else:
    _ListUniqueProblemsPaginatorBase = Paginator  # type: ignore[assignment]

class ListUniqueProblemsPaginator(_ListUniqueProblemsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListUniqueProblems.html#DeviceFarm.Paginator.ListUniqueProblems)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listuniqueproblemspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUniqueProblemsRequestPaginateTypeDef]
    ) -> PageIterator[ListUniqueProblemsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListUniqueProblems.html#DeviceFarm.Paginator.ListUniqueProblems.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listuniqueproblemspaginator)
        """

if TYPE_CHECKING:
    _ListUploadsPaginatorBase = Paginator[ListUploadsResultTypeDef]
else:
    _ListUploadsPaginatorBase = Paginator  # type: ignore[assignment]

class ListUploadsPaginator(_ListUploadsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListUploads.html#DeviceFarm.Paginator.ListUploads)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listuploadspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListUploadsRequestPaginateTypeDef]
    ) -> PageIterator[ListUploadsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListUploads.html#DeviceFarm.Paginator.ListUploads.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listuploadspaginator)
        """

if TYPE_CHECKING:
    _ListVPCEConfigurationsPaginatorBase = Paginator[ListVPCEConfigurationsResultTypeDef]
else:
    _ListVPCEConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListVPCEConfigurationsPaginator(_ListVPCEConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListVPCEConfigurations.html#DeviceFarm.Paginator.ListVPCEConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listvpceconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListVPCEConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[ListVPCEConfigurationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devicefarm/paginator/ListVPCEConfigurations.html#DeviceFarm.Paginator.ListVPCEConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/paginators/#listvpceconfigurationspaginator)
        """
