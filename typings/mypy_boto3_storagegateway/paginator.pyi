# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for storagegateway service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_storagegateway import StorageGatewayClient
    from mypy_boto3_storagegateway.paginator import (
        DescribeTapeArchivesPaginator,
        DescribeTapeRecoveryPointsPaginator,
        DescribeTapesPaginator,
        DescribeVTLDevicesPaginator,
        ListFileSharesPaginator,
        ListGatewaysPaginator,
        ListTagsForResourcePaginator,
        ListTapePoolsPaginator,
        ListTapesPaginator,
        ListVolumesPaginator,
    )

    client: StorageGatewayClient = boto3.client("storagegateway")

    describe_tape_archives_paginator: DescribeTapeArchivesPaginator = client.get_paginator("describe_tape_archives")
    describe_tape_recovery_points_paginator: DescribeTapeRecoveryPointsPaginator = client.get_paginator("describe_tape_recovery_points")
    describe_tapes_paginator: DescribeTapesPaginator = client.get_paginator("describe_tapes")
    describe_vtl_devices_paginator: DescribeVTLDevicesPaginator = client.get_paginator("describe_vtl_devices")
    list_file_shares_paginator: ListFileSharesPaginator = client.get_paginator("list_file_shares")
    list_gateways_paginator: ListGatewaysPaginator = client.get_paginator("list_gateways")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    list_tape_pools_paginator: ListTapePoolsPaginator = client.get_paginator("list_tape_pools")
    list_tapes_paginator: ListTapesPaginator = client.get_paginator("list_tapes")
    list_volumes_paginator: ListVolumesPaginator = client.get_paginator("list_volumes")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_storagegateway.type_defs import (
    DescribeTapeArchivesOutputTypeDef,
    DescribeTapeRecoveryPointsOutputTypeDef,
    DescribeTapesOutputTypeDef,
    DescribeVTLDevicesOutputTypeDef,
    ListFileSharesOutputTypeDef,
    ListGatewaysOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListTapePoolsOutputTypeDef,
    ListTapesOutputTypeDef,
    ListVolumesOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeTapeArchivesPaginator",
    "DescribeTapeRecoveryPointsPaginator",
    "DescribeTapesPaginator",
    "DescribeVTLDevicesPaginator",
    "ListFileSharesPaginator",
    "ListGatewaysPaginator",
    "ListTagsForResourcePaginator",
    "ListTapePoolsPaginator",
    "ListTapesPaginator",
    "ListVolumesPaginator",
)


class DescribeTapeArchivesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTapeArchives documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeArchives)
    """

    def paginate(
        self, TapeARNs: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTapeArchivesOutputTypeDef]:
        """
        [DescribeTapeArchives.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeArchives.paginate)
        """


class DescribeTapeRecoveryPointsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTapeRecoveryPoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeRecoveryPoints)
    """

    def paginate(
        self, GatewayARN: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTapeRecoveryPointsOutputTypeDef]:
        """
        [DescribeTapeRecoveryPoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeRecoveryPoints.paginate)
        """


class DescribeTapesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTapes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapes)
    """

    def paginate(
        self,
        GatewayARN: str,
        TapeARNs: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeTapesOutputTypeDef]:
        """
        [DescribeTapes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapes.paginate)
        """


class DescribeVTLDevicesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVTLDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeVTLDevices)
    """

    def paginate(
        self,
        GatewayARN: str,
        VTLDeviceARNs: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeVTLDevicesOutputTypeDef]:
        """
        [DescribeVTLDevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeVTLDevices.paginate)
        """


class ListFileSharesPaginator(Boto3Paginator):
    """
    [Paginator.ListFileShares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.ListFileShares)
    """

    def paginate(
        self, GatewayARN: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFileSharesOutputTypeDef]:
        """
        [ListFileShares.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.ListFileShares.paginate)
        """


class ListGatewaysPaginator(Boto3Paginator):
    """
    [Paginator.ListGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.ListGateways)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGatewaysOutputTypeDef]:
        """
        [ListGateways.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.ListGateways.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.ListTagsForResource)
    """

    def paginate(
        self, ResourceARN: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceOutputTypeDef]:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.ListTagsForResource.paginate)
        """


class ListTapePoolsPaginator(Boto3Paginator):
    """
    [Paginator.ListTapePools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.ListTapePools)
    """

    def paginate(
        self, PoolARNs: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTapePoolsOutputTypeDef]:
        """
        [ListTapePools.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.ListTapePools.paginate)
        """


class ListTapesPaginator(Boto3Paginator):
    """
    [Paginator.ListTapes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.ListTapes)
    """

    def paginate(
        self, TapeARNs: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTapesOutputTypeDef]:
        """
        [ListTapes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.ListTapes.paginate)
        """


class ListVolumesPaginator(Boto3Paginator):
    """
    [Paginator.ListVolumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.ListVolumes)
    """

    def paginate(
        self, GatewayARN: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVolumesOutputTypeDef]:
        """
        [ListVolumes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/storagegateway.html#StorageGateway.Paginator.ListVolumes.paginate)
        """
