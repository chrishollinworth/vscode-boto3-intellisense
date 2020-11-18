# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for medialive service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_medialive import MediaLiveClient
    from mypy_boto3_medialive.paginator import (
        DescribeSchedulePaginator,
        ListChannelsPaginator,
        ListInputDeviceTransfersPaginator,
        ListInputDevicesPaginator,
        ListInputSecurityGroupsPaginator,
        ListInputsPaginator,
        ListMultiplexProgramsPaginator,
        ListMultiplexesPaginator,
        ListOfferingsPaginator,
        ListReservationsPaginator,
    )

    client: MediaLiveClient = boto3.client("medialive")

    describe_schedule_paginator: DescribeSchedulePaginator = client.get_paginator("describe_schedule")
    list_channels_paginator: ListChannelsPaginator = client.get_paginator("list_channels")
    list_input_device_transfers_paginator: ListInputDeviceTransfersPaginator = client.get_paginator("list_input_device_transfers")
    list_input_devices_paginator: ListInputDevicesPaginator = client.get_paginator("list_input_devices")
    list_input_security_groups_paginator: ListInputSecurityGroupsPaginator = client.get_paginator("list_input_security_groups")
    list_inputs_paginator: ListInputsPaginator = client.get_paginator("list_inputs")
    list_multiplex_programs_paginator: ListMultiplexProgramsPaginator = client.get_paginator("list_multiplex_programs")
    list_multiplexes_paginator: ListMultiplexesPaginator = client.get_paginator("list_multiplexes")
    list_offerings_paginator: ListOfferingsPaginator = client.get_paginator("list_offerings")
    list_reservations_paginator: ListReservationsPaginator = client.get_paginator("list_reservations")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_medialive.type_defs import (
    DescribeScheduleResponseTypeDef,
    ListChannelsResponseTypeDef,
    ListInputDevicesResponseTypeDef,
    ListInputDeviceTransfersResponseTypeDef,
    ListInputSecurityGroupsResponseTypeDef,
    ListInputsResponseTypeDef,
    ListMultiplexesResponseTypeDef,
    ListMultiplexProgramsResponseTypeDef,
    ListOfferingsResponseTypeDef,
    ListReservationsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeSchedulePaginator",
    "ListChannelsPaginator",
    "ListInputDeviceTransfersPaginator",
    "ListInputDevicesPaginator",
    "ListInputSecurityGroupsPaginator",
    "ListInputsPaginator",
    "ListMultiplexProgramsPaginator",
    "ListMultiplexesPaginator",
    "ListOfferingsPaginator",
    "ListReservationsPaginator",
)


class DescribeSchedulePaginator(Boto3Paginator):
    """
    [Paginator.DescribeSchedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.DescribeSchedule)
    """

    def paginate(
        self, ChannelId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeScheduleResponseTypeDef]:
        """
        [DescribeSchedule.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.DescribeSchedule.paginate)
        """


class ListChannelsPaginator(Boto3Paginator):
    """
    [Paginator.ListChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListChannels)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListChannelsResponseTypeDef]:
        """
        [ListChannels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListChannels.paginate)
        """


class ListInputDeviceTransfersPaginator(Boto3Paginator):
    """
    [Paginator.ListInputDeviceTransfers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListInputDeviceTransfers)
    """

    def paginate(
        self, TransferType: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInputDeviceTransfersResponseTypeDef]:
        """
        [ListInputDeviceTransfers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListInputDeviceTransfers.paginate)
        """


class ListInputDevicesPaginator(Boto3Paginator):
    """
    [Paginator.ListInputDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListInputDevices)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInputDevicesResponseTypeDef]:
        """
        [ListInputDevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListInputDevices.paginate)
        """


class ListInputSecurityGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListInputSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListInputSecurityGroups)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInputSecurityGroupsResponseTypeDef]:
        """
        [ListInputSecurityGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListInputSecurityGroups.paginate)
        """


class ListInputsPaginator(Boto3Paginator):
    """
    [Paginator.ListInputs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListInputs)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInputsResponseTypeDef]:
        """
        [ListInputs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListInputs.paginate)
        """


class ListMultiplexProgramsPaginator(Boto3Paginator):
    """
    [Paginator.ListMultiplexPrograms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexPrograms)
    """

    def paginate(
        self, MultiplexId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMultiplexProgramsResponseTypeDef]:
        """
        [ListMultiplexPrograms.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexPrograms.paginate)
        """


class ListMultiplexesPaginator(Boto3Paginator):
    """
    [Paginator.ListMultiplexes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexes)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMultiplexesResponseTypeDef]:
        """
        [ListMultiplexes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexes.paginate)
        """


class ListOfferingsPaginator(Boto3Paginator):
    """
    [Paginator.ListOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListOfferings)
    """

    def paginate(
        self,
        ChannelClass: str = None,
        ChannelConfiguration: str = None,
        Codec: str = None,
        Duration: str = None,
        MaximumBitrate: str = None,
        MaximumFramerate: str = None,
        Resolution: str = None,
        ResourceType: str = None,
        SpecialFeature: str = None,
        VideoQuality: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListOfferingsResponseTypeDef]:
        """
        [ListOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListOfferings.paginate)
        """


class ListReservationsPaginator(Boto3Paginator):
    """
    [Paginator.ListReservations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListReservations)
    """

    def paginate(
        self,
        ChannelClass: str = None,
        Codec: str = None,
        MaximumBitrate: str = None,
        MaximumFramerate: str = None,
        Resolution: str = None,
        ResourceType: str = None,
        SpecialFeature: str = None,
        VideoQuality: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListReservationsResponseTypeDef]:
        """
        [ListReservations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListReservations.paginate)
        """
