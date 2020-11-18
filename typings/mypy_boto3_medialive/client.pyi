# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for medialive service client

Usage::

    ```python
    import boto3
    from mypy_boto3_medialive import MediaLiveClient

    client: MediaLiveClient = boto3.client("medialive")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_medialive.paginator import (
    DescribeSchedulePaginator,
    ListChannelsPaginator,
    ListInputDevicesPaginator,
    ListInputDeviceTransfersPaginator,
    ListInputSecurityGroupsPaginator,
    ListInputsPaginator,
    ListMultiplexesPaginator,
    ListMultiplexProgramsPaginator,
    ListOfferingsPaginator,
    ListReservationsPaginator,
)
from mypy_boto3_medialive.type_defs import (
    BatchDeleteResponseTypeDef,
    BatchScheduleActionCreateRequestTypeDef,
    BatchScheduleActionDeleteRequestTypeDef,
    BatchStartResponseTypeDef,
    BatchStopResponseTypeDef,
    BatchUpdateScheduleResponseTypeDef,
    CdiInputSpecificationTypeDef,
    CreateChannelResponseTypeDef,
    CreateInputResponseTypeDef,
    CreateInputSecurityGroupResponseTypeDef,
    CreateMultiplexProgramResponseTypeDef,
    CreateMultiplexResponseTypeDef,
    DeleteChannelResponseTypeDef,
    DeleteMultiplexProgramResponseTypeDef,
    DeleteMultiplexResponseTypeDef,
    DeleteReservationResponseTypeDef,
    DescribeChannelResponseTypeDef,
    DescribeInputDeviceResponseTypeDef,
    DescribeInputDeviceThumbnailResponseTypeDef,
    DescribeInputResponseTypeDef,
    DescribeInputSecurityGroupResponseTypeDef,
    DescribeMultiplexProgramResponseTypeDef,
    DescribeMultiplexResponseTypeDef,
    DescribeOfferingResponseTypeDef,
    DescribeReservationResponseTypeDef,
    DescribeScheduleResponseTypeDef,
    EncoderSettingsTypeDef,
    InputAttachmentTypeDef,
    InputDestinationRequestTypeDef,
    InputDeviceConfigurableSettingsTypeDef,
    InputDeviceRequestTypeDef,
    InputDeviceSettingsTypeDef,
    InputSourceRequestTypeDef,
    InputSpecificationTypeDef,
    InputVpcRequestTypeDef,
    InputWhitelistRuleCidrTypeDef,
    ListChannelsResponseTypeDef,
    ListInputDevicesResponseTypeDef,
    ListInputDeviceTransfersResponseTypeDef,
    ListInputSecurityGroupsResponseTypeDef,
    ListInputsResponseTypeDef,
    ListMultiplexesResponseTypeDef,
    ListMultiplexProgramsResponseTypeDef,
    ListOfferingsResponseTypeDef,
    ListReservationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MediaConnectFlowRequestTypeDef,
    MultiplexProgramSettingsTypeDef,
    MultiplexSettingsTypeDef,
    OutputDestinationTypeDef,
    PurchaseOfferingResponseTypeDef,
    StartChannelResponseTypeDef,
    StartMultiplexResponseTypeDef,
    StopChannelResponseTypeDef,
    StopMultiplexResponseTypeDef,
    UpdateChannelClassResponseTypeDef,
    UpdateChannelResponseTypeDef,
    UpdateInputDeviceResponseTypeDef,
    UpdateInputResponseTypeDef,
    UpdateInputSecurityGroupResponseTypeDef,
    UpdateMultiplexProgramResponseTypeDef,
    UpdateMultiplexResponseTypeDef,
    UpdateReservationResponseTypeDef,
)
from mypy_boto3_medialive.waiter import (
    ChannelCreatedWaiter,
    ChannelDeletedWaiter,
    ChannelRunningWaiter,
    ChannelStoppedWaiter,
    InputAttachedWaiter,
    InputDeletedWaiter,
    InputDetachedWaiter,
    MultiplexCreatedWaiter,
    MultiplexDeletedWaiter,
    MultiplexRunningWaiter,
    MultiplexStoppedWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MediaLiveClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadGatewayException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    GatewayTimeoutException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnprocessableEntityException: Type[BotocoreClientError]


class MediaLiveClient:
    """
    [MediaLive.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_input_device_transfer(self, InputDeviceId: str) -> Dict[str, Any]:
        """
        [Client.accept_input_device_transfer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.accept_input_device_transfer)
        """

    def batch_delete(
        self,
        ChannelIds: List[str] = None,
        InputIds: List[str] = None,
        InputSecurityGroupIds: List[str] = None,
        MultiplexIds: List[str] = None,
    ) -> BatchDeleteResponseTypeDef:
        """
        [Client.batch_delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.batch_delete)
        """

    def batch_start(
        self, ChannelIds: List[str] = None, MultiplexIds: List[str] = None
    ) -> BatchStartResponseTypeDef:
        """
        [Client.batch_start documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.batch_start)
        """

    def batch_stop(
        self, ChannelIds: List[str] = None, MultiplexIds: List[str] = None
    ) -> BatchStopResponseTypeDef:
        """
        [Client.batch_stop documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.batch_stop)
        """

    def batch_update_schedule(
        self,
        ChannelId: str,
        Creates: BatchScheduleActionCreateRequestTypeDef = None,
        Deletes: BatchScheduleActionDeleteRequestTypeDef = None,
    ) -> BatchUpdateScheduleResponseTypeDef:
        """
        [Client.batch_update_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.batch_update_schedule)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.can_paginate)
        """

    def cancel_input_device_transfer(self, InputDeviceId: str) -> Dict[str, Any]:
        """
        [Client.cancel_input_device_transfer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.cancel_input_device_transfer)
        """

    def create_channel(
        self,
        CdiInputSpecification: "CdiInputSpecificationTypeDef" = None,
        ChannelClass: Literal["STANDARD", "SINGLE_PIPELINE"] = None,
        Destinations: List["OutputDestinationTypeDef"] = None,
        EncoderSettings: "EncoderSettingsTypeDef" = None,
        InputAttachments: List["InputAttachmentTypeDef"] = None,
        InputSpecification: "InputSpecificationTypeDef" = None,
        LogLevel: Literal["ERROR", "WARNING", "INFO", "DEBUG", "DISABLED"] = None,
        Name: str = None,
        RequestId: str = None,
        Reserved: str = None,
        RoleArn: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateChannelResponseTypeDef:
        """
        [Client.create_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.create_channel)
        """

    def create_input(
        self,
        Destinations: List[InputDestinationRequestTypeDef] = None,
        InputDevices: List["InputDeviceSettingsTypeDef"] = None,
        InputSecurityGroups: List[str] = None,
        MediaConnectFlows: List[MediaConnectFlowRequestTypeDef] = None,
        Name: str = None,
        RequestId: str = None,
        RoleArn: str = None,
        Sources: List[InputSourceRequestTypeDef] = None,
        Tags: Dict[str, str] = None,
        Type: Literal[
            "UDP_PUSH",
            "RTP_PUSH",
            "RTMP_PUSH",
            "RTMP_PULL",
            "URL_PULL",
            "MP4_FILE",
            "MEDIACONNECT",
            "INPUT_DEVICE",
            "AWS_CDI",
        ] = None,
        Vpc: InputVpcRequestTypeDef = None,
    ) -> CreateInputResponseTypeDef:
        """
        [Client.create_input documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.create_input)
        """

    def create_input_security_group(
        self,
        Tags: Dict[str, str] = None,
        WhitelistRules: List[InputWhitelistRuleCidrTypeDef] = None,
    ) -> CreateInputSecurityGroupResponseTypeDef:
        """
        [Client.create_input_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.create_input_security_group)
        """

    def create_multiplex(
        self,
        AvailabilityZones: List[str],
        MultiplexSettings: "MultiplexSettingsTypeDef",
        Name: str,
        RequestId: str,
        Tags: Dict[str, str] = None,
    ) -> CreateMultiplexResponseTypeDef:
        """
        [Client.create_multiplex documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.create_multiplex)
        """

    def create_multiplex_program(
        self,
        MultiplexId: str,
        MultiplexProgramSettings: "MultiplexProgramSettingsTypeDef",
        ProgramName: str,
        RequestId: str,
    ) -> CreateMultiplexProgramResponseTypeDef:
        """
        [Client.create_multiplex_program documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.create_multiplex_program)
        """

    def create_tags(self, ResourceArn: str, Tags: Dict[str, str] = None) -> None:
        """
        [Client.create_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.create_tags)
        """

    def delete_channel(self, ChannelId: str) -> DeleteChannelResponseTypeDef:
        """
        [Client.delete_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.delete_channel)
        """

    def delete_input(self, InputId: str) -> Dict[str, Any]:
        """
        [Client.delete_input documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.delete_input)
        """

    def delete_input_security_group(self, InputSecurityGroupId: str) -> Dict[str, Any]:
        """
        [Client.delete_input_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.delete_input_security_group)
        """

    def delete_multiplex(self, MultiplexId: str) -> DeleteMultiplexResponseTypeDef:
        """
        [Client.delete_multiplex documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.delete_multiplex)
        """

    def delete_multiplex_program(
        self, MultiplexId: str, ProgramName: str
    ) -> DeleteMultiplexProgramResponseTypeDef:
        """
        [Client.delete_multiplex_program documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.delete_multiplex_program)
        """

    def delete_reservation(self, ReservationId: str) -> DeleteReservationResponseTypeDef:
        """
        [Client.delete_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.delete_reservation)
        """

    def delete_schedule(self, ChannelId: str) -> Dict[str, Any]:
        """
        [Client.delete_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.delete_schedule)
        """

    def delete_tags(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.delete_tags)
        """

    def describe_channel(self, ChannelId: str) -> DescribeChannelResponseTypeDef:
        """
        [Client.describe_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.describe_channel)
        """

    def describe_input(self, InputId: str) -> DescribeInputResponseTypeDef:
        """
        [Client.describe_input documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.describe_input)
        """

    def describe_input_device(self, InputDeviceId: str) -> DescribeInputDeviceResponseTypeDef:
        """
        [Client.describe_input_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.describe_input_device)
        """

    def describe_input_device_thumbnail(
        self, InputDeviceId: str, Accept: Literal["image/jpeg"]
    ) -> DescribeInputDeviceThumbnailResponseTypeDef:
        """
        [Client.describe_input_device_thumbnail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.describe_input_device_thumbnail)
        """

    def describe_input_security_group(
        self, InputSecurityGroupId: str
    ) -> DescribeInputSecurityGroupResponseTypeDef:
        """
        [Client.describe_input_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.describe_input_security_group)
        """

    def describe_multiplex(self, MultiplexId: str) -> DescribeMultiplexResponseTypeDef:
        """
        [Client.describe_multiplex documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.describe_multiplex)
        """

    def describe_multiplex_program(
        self, MultiplexId: str, ProgramName: str
    ) -> DescribeMultiplexProgramResponseTypeDef:
        """
        [Client.describe_multiplex_program documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.describe_multiplex_program)
        """

    def describe_offering(self, OfferingId: str) -> DescribeOfferingResponseTypeDef:
        """
        [Client.describe_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.describe_offering)
        """

    def describe_reservation(self, ReservationId: str) -> DescribeReservationResponseTypeDef:
        """
        [Client.describe_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.describe_reservation)
        """

    def describe_schedule(
        self, ChannelId: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeScheduleResponseTypeDef:
        """
        [Client.describe_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.describe_schedule)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.generate_presigned_url)
        """

    def list_channels(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListChannelsResponseTypeDef:
        """
        [Client.list_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.list_channels)
        """

    def list_input_device_transfers(
        self, TransferType: str, MaxResults: int = None, NextToken: str = None
    ) -> ListInputDeviceTransfersResponseTypeDef:
        """
        [Client.list_input_device_transfers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.list_input_device_transfers)
        """

    def list_input_devices(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListInputDevicesResponseTypeDef:
        """
        [Client.list_input_devices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.list_input_devices)
        """

    def list_input_security_groups(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListInputSecurityGroupsResponseTypeDef:
        """
        [Client.list_input_security_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.list_input_security_groups)
        """

    def list_inputs(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListInputsResponseTypeDef:
        """
        [Client.list_inputs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.list_inputs)
        """

    def list_multiplex_programs(
        self, MultiplexId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListMultiplexProgramsResponseTypeDef:
        """
        [Client.list_multiplex_programs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.list_multiplex_programs)
        """

    def list_multiplexes(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListMultiplexesResponseTypeDef:
        """
        [Client.list_multiplexes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.list_multiplexes)
        """

    def list_offerings(
        self,
        ChannelClass: str = None,
        ChannelConfiguration: str = None,
        Codec: str = None,
        Duration: str = None,
        MaxResults: int = None,
        MaximumBitrate: str = None,
        MaximumFramerate: str = None,
        NextToken: str = None,
        Resolution: str = None,
        ResourceType: str = None,
        SpecialFeature: str = None,
        VideoQuality: str = None,
    ) -> ListOfferingsResponseTypeDef:
        """
        [Client.list_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.list_offerings)
        """

    def list_reservations(
        self,
        ChannelClass: str = None,
        Codec: str = None,
        MaxResults: int = None,
        MaximumBitrate: str = None,
        MaximumFramerate: str = None,
        NextToken: str = None,
        Resolution: str = None,
        ResourceType: str = None,
        SpecialFeature: str = None,
        VideoQuality: str = None,
    ) -> ListReservationsResponseTypeDef:
        """
        [Client.list_reservations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.list_reservations)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.list_tags_for_resource)
        """

    def purchase_offering(
        self,
        Count: int,
        OfferingId: str,
        Name: str = None,
        RequestId: str = None,
        Start: str = None,
        Tags: Dict[str, str] = None,
    ) -> PurchaseOfferingResponseTypeDef:
        """
        [Client.purchase_offering documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.purchase_offering)
        """

    def reject_input_device_transfer(self, InputDeviceId: str) -> Dict[str, Any]:
        """
        [Client.reject_input_device_transfer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.reject_input_device_transfer)
        """

    def start_channel(self, ChannelId: str) -> StartChannelResponseTypeDef:
        """
        [Client.start_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.start_channel)
        """

    def start_multiplex(self, MultiplexId: str) -> StartMultiplexResponseTypeDef:
        """
        [Client.start_multiplex documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.start_multiplex)
        """

    def stop_channel(self, ChannelId: str) -> StopChannelResponseTypeDef:
        """
        [Client.stop_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.stop_channel)
        """

    def stop_multiplex(self, MultiplexId: str) -> StopMultiplexResponseTypeDef:
        """
        [Client.stop_multiplex documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.stop_multiplex)
        """

    def transfer_input_device(
        self, InputDeviceId: str, TargetCustomerId: str = None, TransferMessage: str = None
    ) -> Dict[str, Any]:
        """
        [Client.transfer_input_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.transfer_input_device)
        """

    def update_channel(
        self,
        ChannelId: str,
        CdiInputSpecification: "CdiInputSpecificationTypeDef" = None,
        Destinations: List["OutputDestinationTypeDef"] = None,
        EncoderSettings: "EncoderSettingsTypeDef" = None,
        InputAttachments: List["InputAttachmentTypeDef"] = None,
        InputSpecification: "InputSpecificationTypeDef" = None,
        LogLevel: Literal["ERROR", "WARNING", "INFO", "DEBUG", "DISABLED"] = None,
        Name: str = None,
        RoleArn: str = None,
    ) -> UpdateChannelResponseTypeDef:
        """
        [Client.update_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.update_channel)
        """

    def update_channel_class(
        self,
        ChannelClass: Literal["STANDARD", "SINGLE_PIPELINE"],
        ChannelId: str,
        Destinations: List["OutputDestinationTypeDef"] = None,
    ) -> UpdateChannelClassResponseTypeDef:
        """
        [Client.update_channel_class documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.update_channel_class)
        """

    def update_input(
        self,
        InputId: str,
        Destinations: List[InputDestinationRequestTypeDef] = None,
        InputDevices: List[InputDeviceRequestTypeDef] = None,
        InputSecurityGroups: List[str] = None,
        MediaConnectFlows: List[MediaConnectFlowRequestTypeDef] = None,
        Name: str = None,
        RoleArn: str = None,
        Sources: List[InputSourceRequestTypeDef] = None,
    ) -> UpdateInputResponseTypeDef:
        """
        [Client.update_input documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.update_input)
        """

    def update_input_device(
        self,
        InputDeviceId: str,
        HdDeviceSettings: InputDeviceConfigurableSettingsTypeDef = None,
        Name: str = None,
    ) -> UpdateInputDeviceResponseTypeDef:
        """
        [Client.update_input_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.update_input_device)
        """

    def update_input_security_group(
        self,
        InputSecurityGroupId: str,
        Tags: Dict[str, str] = None,
        WhitelistRules: List[InputWhitelistRuleCidrTypeDef] = None,
    ) -> UpdateInputSecurityGroupResponseTypeDef:
        """
        [Client.update_input_security_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.update_input_security_group)
        """

    def update_multiplex(
        self,
        MultiplexId: str,
        MultiplexSettings: "MultiplexSettingsTypeDef" = None,
        Name: str = None,
    ) -> UpdateMultiplexResponseTypeDef:
        """
        [Client.update_multiplex documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.update_multiplex)
        """

    def update_multiplex_program(
        self,
        MultiplexId: str,
        ProgramName: str,
        MultiplexProgramSettings: "MultiplexProgramSettingsTypeDef" = None,
    ) -> UpdateMultiplexProgramResponseTypeDef:
        """
        [Client.update_multiplex_program documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.update_multiplex_program)
        """

    def update_reservation(
        self, ReservationId: str, Name: str = None
    ) -> UpdateReservationResponseTypeDef:
        """
        [Client.update_reservation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Client.update_reservation)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_schedule"]
    ) -> DescribeSchedulePaginator:
        """
        [Paginator.DescribeSchedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.DescribeSchedule)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_channels"]) -> ListChannelsPaginator:
        """
        [Paginator.ListChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListChannels)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_input_device_transfers"]
    ) -> ListInputDeviceTransfersPaginator:
        """
        [Paginator.ListInputDeviceTransfers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListInputDeviceTransfers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_input_devices"]
    ) -> ListInputDevicesPaginator:
        """
        [Paginator.ListInputDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListInputDevices)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_input_security_groups"]
    ) -> ListInputSecurityGroupsPaginator:
        """
        [Paginator.ListInputSecurityGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListInputSecurityGroups)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_inputs"]) -> ListInputsPaginator:
        """
        [Paginator.ListInputs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListInputs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_multiplex_programs"]
    ) -> ListMultiplexProgramsPaginator:
        """
        [Paginator.ListMultiplexPrograms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexPrograms)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_multiplexes"]
    ) -> ListMultiplexesPaginator:
        """
        [Paginator.ListMultiplexes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexes)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_offerings"]) -> ListOfferingsPaginator:
        """
        [Paginator.ListOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListOfferings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_reservations"]
    ) -> ListReservationsPaginator:
        """
        [Paginator.ListReservations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Paginator.ListReservations)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["channel_created"]) -> ChannelCreatedWaiter:
        """
        [Waiter.ChannelCreated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.ChannelCreated)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["channel_deleted"]) -> ChannelDeletedWaiter:
        """
        [Waiter.ChannelDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.ChannelDeleted)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["channel_running"]) -> ChannelRunningWaiter:
        """
        [Waiter.ChannelRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.ChannelRunning)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["channel_stopped"]) -> ChannelStoppedWaiter:
        """
        [Waiter.ChannelStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.ChannelStopped)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["input_attached"]) -> InputAttachedWaiter:
        """
        [Waiter.InputAttached documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.InputAttached)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["input_deleted"]) -> InputDeletedWaiter:
        """
        [Waiter.InputDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.InputDeleted)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["input_detached"]) -> InputDetachedWaiter:
        """
        [Waiter.InputDetached documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.InputDetached)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["multiplex_created"]) -> MultiplexCreatedWaiter:
        """
        [Waiter.MultiplexCreated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.MultiplexCreated)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["multiplex_deleted"]) -> MultiplexDeletedWaiter:
        """
        [Waiter.MultiplexDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.MultiplexDeleted)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["multiplex_running"]) -> MultiplexRunningWaiter:
        """
        [Waiter.MultiplexRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.MultiplexRunning)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["multiplex_stopped"]) -> MultiplexStoppedWaiter:
        """
        [Waiter.MultiplexStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/medialive.html#MediaLive.Waiter.MultiplexStopped)
        """
