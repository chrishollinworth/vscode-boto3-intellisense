"""
Type annotations for medialive service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_medialive import MediaLiveClient

    client: MediaLiveClient = boto3.client("medialive")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import ChannelClassType, InputTypeType, LogLevelType, RebootInputDeviceForceType
from .paginator import (
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
from .type_defs import (
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
    CreatePartnerInputResponseTypeDef,
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
    MaintenanceCreateSettingsTypeDef,
    MaintenanceUpdateSettingsTypeDef,
    MediaConnectFlowRequestTypeDef,
    MultiplexProgramSettingsTypeDef,
    MultiplexSettingsTypeDef,
    OutputDestinationTypeDef,
    PurchaseOfferingResponseTypeDef,
    RenewalSettingsTypeDef,
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
    VpcOutputSettingsTypeDef,
)
from .waiter import (
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

class MediaLiveClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MediaLiveClient exceptions.
        """
    def accept_input_device_transfer(self, *, InputDeviceId: str) -> Dict[str, Any]:
        """
        Accept an incoming input device transfer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.accept_input_device_transfer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#accept_input_device_transfer)
        """
    def batch_delete(
        self,
        *,
        ChannelIds: List[str] = None,
        InputIds: List[str] = None,
        InputSecurityGroupIds: List[str] = None,
        MultiplexIds: List[str] = None
    ) -> BatchDeleteResponseTypeDef:
        """
        Starts delete of resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.batch_delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#batch_delete)
        """
    def batch_start(
        self, *, ChannelIds: List[str] = None, MultiplexIds: List[str] = None
    ) -> BatchStartResponseTypeDef:
        """
        Starts existing resources See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/BatchStart>`_
        **Request Syntax** response = client.batch_start( ChannelIds=[ 'string', ],
        MultiplexIds=[ 'string', ] ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.batch_start)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#batch_start)
        """
    def batch_stop(
        self, *, ChannelIds: List[str] = None, MultiplexIds: List[str] = None
    ) -> BatchStopResponseTypeDef:
        """
        Stops running resources See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/BatchStop>`_
        **Request Syntax** response = client.batch_stop( ChannelIds=[ 'string', ],
        MultiplexIds=[ 'string', ] ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.batch_stop)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#batch_stop)
        """
    def batch_update_schedule(
        self,
        *,
        ChannelId: str,
        Creates: "BatchScheduleActionCreateRequestTypeDef" = None,
        Deletes: "BatchScheduleActionDeleteRequestTypeDef" = None
    ) -> BatchUpdateScheduleResponseTypeDef:
        """
        Update a channel schedule See also: `AWS API Documentation <https://docs.aws.ama
        zon.com/goto/WebAPI/medialive-2017-10-14/BatchUpdateSchedule>`_ **Request
        Syntax** response = client.batch_update_schedule( ChannelId='string', Creates={
        'ScheduleActions': [ ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.batch_update_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#batch_update_schedule)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#can_paginate)
        """
    def cancel_input_device_transfer(self, *, InputDeviceId: str) -> Dict[str, Any]:
        """
        Cancel an input device transfer that you have requested.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.cancel_input_device_transfer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#cancel_input_device_transfer)
        """
    def claim_device(self, *, Id: str = None) -> Dict[str, Any]:
        """
        Send a request to claim an AWS Elemental device that you have purchased from a
        third-party vendor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.claim_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#claim_device)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#close)
        """
    def create_channel(
        self,
        *,
        CdiInputSpecification: "CdiInputSpecificationTypeDef" = None,
        ChannelClass: ChannelClassType = None,
        Destinations: List["OutputDestinationTypeDef"] = None,
        EncoderSettings: "EncoderSettingsTypeDef" = None,
        InputAttachments: List["InputAttachmentTypeDef"] = None,
        InputSpecification: "InputSpecificationTypeDef" = None,
        LogLevel: LogLevelType = None,
        Maintenance: "MaintenanceCreateSettingsTypeDef" = None,
        Name: str = None,
        RequestId: str = None,
        Reserved: str = None,
        RoleArn: str = None,
        Tags: Dict[str, str] = None,
        Vpc: "VpcOutputSettingsTypeDef" = None
    ) -> CreateChannelResponseTypeDef:
        """
        Creates a new channel See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/CreateChannel>`_
        **Request Syntax** response = client.create_channel( CdiInputSpecification={
        'Resolution': 'SD'|'HD'|'FHD'|'UHD' }, ChannelCl...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.create_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#create_channel)
        """
    def create_input(
        self,
        *,
        Destinations: List["InputDestinationRequestTypeDef"] = None,
        InputDevices: List["InputDeviceSettingsTypeDef"] = None,
        InputSecurityGroups: List[str] = None,
        MediaConnectFlows: List["MediaConnectFlowRequestTypeDef"] = None,
        Name: str = None,
        RequestId: str = None,
        RoleArn: str = None,
        Sources: List["InputSourceRequestTypeDef"] = None,
        Tags: Dict[str, str] = None,
        Type: InputTypeType = None,
        Vpc: "InputVpcRequestTypeDef" = None
    ) -> CreateInputResponseTypeDef:
        """
        Create an input See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/CreateInput>`_
        **Request Syntax** response = client.create_input( Destinations=[ {
        'StreamName': 'string' }, ], InputDevices...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.create_input)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#create_input)
        """
    def create_input_security_group(
        self,
        *,
        Tags: Dict[str, str] = None,
        WhitelistRules: List["InputWhitelistRuleCidrTypeDef"] = None
    ) -> CreateInputSecurityGroupResponseTypeDef:
        """
        Creates a Input Security Group See also: `AWS API Documentation <https://docs.aw
        s.amazon.com/goto/WebAPI/medialive-2017-10-14/CreateInputSecurityGroup>`_
        **Request Syntax** response = client.create_input_security_group( Tags={
        'string': 'string' }, WhitelistR...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.create_input_security_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#create_input_security_group)
        """
    def create_multiplex(
        self,
        *,
        AvailabilityZones: List[str],
        MultiplexSettings: "MultiplexSettingsTypeDef",
        Name: str,
        RequestId: str,
        Tags: Dict[str, str] = None
    ) -> CreateMultiplexResponseTypeDef:
        """
        Create a new multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.create_multiplex)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#create_multiplex)
        """
    def create_multiplex_program(
        self,
        *,
        MultiplexId: str,
        MultiplexProgramSettings: "MultiplexProgramSettingsTypeDef",
        ProgramName: str,
        RequestId: str
    ) -> CreateMultiplexProgramResponseTypeDef:
        """
        Create a new program in the multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.create_multiplex_program)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#create_multiplex_program)
        """
    def create_partner_input(
        self, *, InputId: str, RequestId: str = None, Tags: Dict[str, str] = None
    ) -> CreatePartnerInputResponseTypeDef:
        """
        Create a partner input See also: `AWS API Documentation <https://docs.aws.amazon
        .com/goto/WebAPI/medialive-2017-10-14/CreatePartnerInput>`_ **Request Syntax**
        response = client.create_partner_input( InputId='string', RequestId='string',
        Tags={ 'string': 'stri...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.create_partner_input)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#create_partner_input)
        """
    def create_tags(self, *, ResourceArn: str, Tags: Dict[str, str] = None) -> None:
        """
        Create tags for a resource See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/CreateTags>`_
        **Request Syntax** response = client.create_tags( ResourceArn='string', Tags={
        'string': 'string' } ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#create_tags)
        """
    def delete_channel(self, *, ChannelId: str) -> DeleteChannelResponseTypeDef:
        """
        Starts deletion of channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.delete_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#delete_channel)
        """
    def delete_input(self, *, InputId: str) -> Dict[str, Any]:
        """
        Deletes the input end point See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/DeleteInput>`_
        **Request Syntax** response = client.delete_input( InputId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.delete_input)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#delete_input)
        """
    def delete_input_security_group(self, *, InputSecurityGroupId: str) -> Dict[str, Any]:
        """
        Deletes an Input Security Group See also: `AWS API Documentation <https://docs.a
        ws.amazon.com/goto/WebAPI/medialive-2017-10-14/DeleteInputSecurityGroup>`_
        **Request Syntax** response = client.delete_input_security_group(
        InputSecurityGroupId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.delete_input_security_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#delete_input_security_group)
        """
    def delete_multiplex(self, *, MultiplexId: str) -> DeleteMultiplexResponseTypeDef:
        """
        Delete a multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.delete_multiplex)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#delete_multiplex)
        """
    def delete_multiplex_program(
        self, *, MultiplexId: str, ProgramName: str
    ) -> DeleteMultiplexProgramResponseTypeDef:
        """
        Delete a program from a multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.delete_multiplex_program)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#delete_multiplex_program)
        """
    def delete_reservation(self, *, ReservationId: str) -> DeleteReservationResponseTypeDef:
        """
        Delete an expired reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.delete_reservation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#delete_reservation)
        """
    def delete_schedule(self, *, ChannelId: str) -> Dict[str, Any]:
        """
        Delete all schedule actions on a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.delete_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#delete_schedule)
        """
    def delete_tags(self, *, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        Removes tags for a resource See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/DeleteTags>`_
        **Request Syntax** response = client.delete_tags( ResourceArn='string',
        TagKeys=[ 'string', ] ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.delete_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#delete_tags)
        """
    def describe_channel(self, *, ChannelId: str) -> DescribeChannelResponseTypeDef:
        """
        Gets details about a channel See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/DescribeChannel>`_
        **Request Syntax** response = client.describe_channel( ChannelId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.describe_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#describe_channel)
        """
    def describe_input(self, *, InputId: str) -> DescribeInputResponseTypeDef:
        """
        Produces details about an input See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/DescribeInput>`_
        **Request Syntax** response = client.describe_input( InputId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.describe_input)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#describe_input)
        """
    def describe_input_device(self, *, InputDeviceId: str) -> DescribeInputDeviceResponseTypeDef:
        """
        Gets the details for the input device See also: `AWS API Documentation <https://
        docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/DescribeInputDevice>`_
        **Request Syntax** response = client.describe_input_device(
        InputDeviceId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.describe_input_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#describe_input_device)
        """
    def describe_input_device_thumbnail(
        self, *, InputDeviceId: str, Accept: Literal["image/jpeg"]
    ) -> DescribeInputDeviceThumbnailResponseTypeDef:
        """
        Get the latest thumbnail data for the input device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.describe_input_device_thumbnail)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#describe_input_device_thumbnail)
        """
    def describe_input_security_group(
        self, *, InputSecurityGroupId: str
    ) -> DescribeInputSecurityGroupResponseTypeDef:
        """
        Produces a summary of an Input Security Group See also: `AWS API Documentation <
        https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-
        14/DescribeInputSecurityGroup>`_ **Request Syntax** response =
        client.describe_input_security_group( InputSecurityGroupId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.describe_input_security_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#describe_input_security_group)
        """
    def describe_multiplex(self, *, MultiplexId: str) -> DescribeMultiplexResponseTypeDef:
        """
        Gets details about a multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.describe_multiplex)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#describe_multiplex)
        """
    def describe_multiplex_program(
        self, *, MultiplexId: str, ProgramName: str
    ) -> DescribeMultiplexProgramResponseTypeDef:
        """
        Get the details for a program in a multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.describe_multiplex_program)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#describe_multiplex_program)
        """
    def describe_offering(self, *, OfferingId: str) -> DescribeOfferingResponseTypeDef:
        """
        Get details for an offering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.describe_offering)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#describe_offering)
        """
    def describe_reservation(self, *, ReservationId: str) -> DescribeReservationResponseTypeDef:
        """
        Get details for a reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.describe_reservation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#describe_reservation)
        """
    def describe_schedule(
        self, *, ChannelId: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeScheduleResponseTypeDef:
        """
        Get a channel schedule See also: `AWS API Documentation <https://docs.aws.amazon
        .com/goto/WebAPI/medialive-2017-10-14/DescribeSchedule>`_ **Request Syntax**
        response = client.describe_schedule( ChannelId='string', MaxResults=123,
        NextToken='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.describe_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#describe_schedule)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#generate_presigned_url)
        """
    def list_channels(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListChannelsResponseTypeDef:
        """
        Produces list of channels that have been created See also: `AWS API
        Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/ListChannels>`_
        **Request Syntax** response = client.list_channels( MaxResults=123,
        NextToken='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.list_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#list_channels)
        """
    def list_input_device_transfers(
        self, *, TransferType: str, MaxResults: int = None, NextToken: str = None
    ) -> ListInputDeviceTransfersResponseTypeDef:
        """
        List input devices that are currently being transferred.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.list_input_device_transfers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#list_input_device_transfers)
        """
    def list_input_devices(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListInputDevicesResponseTypeDef:
        """
        List input devices See also: `AWS API Documentation <https://docs.aws.amazon.com
        /goto/WebAPI/medialive-2017-10-14/ListInputDevices>`_ **Request Syntax**
        response = client.list_input_devices( MaxResults=123, NextToken='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.list_input_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#list_input_devices)
        """
    def list_input_security_groups(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListInputSecurityGroupsResponseTypeDef:
        """
        Produces a list of Input Security Groups for an account See also: `AWS API
        Documentation <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-
        14/ListInputSecurityGroups>`_ **Request Syntax** response =
        client.list_input_security_groups( MaxResults=123, NextToken='strin...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.list_input_security_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#list_input_security_groups)
        """
    def list_inputs(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListInputsResponseTypeDef:
        """
        Produces list of inputs that have been created See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/ListInputs>`_
        **Request Syntax** response = client.list_inputs( MaxResults=123,
        NextToken='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.list_inputs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#list_inputs)
        """
    def list_multiplex_programs(
        self, *, MultiplexId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListMultiplexProgramsResponseTypeDef:
        """
        List the programs that currently exist for a specific multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.list_multiplex_programs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#list_multiplex_programs)
        """
    def list_multiplexes(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListMultiplexesResponseTypeDef:
        """
        Retrieve a list of the existing multiplexes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.list_multiplexes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#list_multiplexes)
        """
    def list_offerings(
        self,
        *,
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
        VideoQuality: str = None
    ) -> ListOfferingsResponseTypeDef:
        """
        List offerings available for purchase.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.list_offerings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#list_offerings)
        """
    def list_reservations(
        self,
        *,
        ChannelClass: str = None,
        Codec: str = None,
        MaxResults: int = None,
        MaximumBitrate: str = None,
        MaximumFramerate: str = None,
        NextToken: str = None,
        Resolution: str = None,
        ResourceType: str = None,
        SpecialFeature: str = None,
        VideoQuality: str = None
    ) -> ListReservationsResponseTypeDef:
        """
        List purchased reservations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.list_reservations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#list_reservations)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Produces list of tags that have been created for a resource See also: `AWS API
        Documentation <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-
        14/ListTagsForResource>`_ **Request Syntax** response =
        client.list_tags_for_resource( ResourceArn='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#list_tags_for_resource)
        """
    def purchase_offering(
        self,
        *,
        Count: int,
        OfferingId: str,
        Name: str = None,
        RenewalSettings: "RenewalSettingsTypeDef" = None,
        RequestId: str = None,
        Start: str = None,
        Tags: Dict[str, str] = None
    ) -> PurchaseOfferingResponseTypeDef:
        """
        Purchase an offering and create a reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.purchase_offering)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#purchase_offering)
        """
    def reboot_input_device(
        self, *, InputDeviceId: str, Force: RebootInputDeviceForceType = None
    ) -> Dict[str, Any]:
        """
        Send a reboot command to the specified input device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.reboot_input_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#reboot_input_device)
        """
    def reject_input_device_transfer(self, *, InputDeviceId: str) -> Dict[str, Any]:
        """
        Reject the transfer of the specified input device to your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.reject_input_device_transfer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#reject_input_device_transfer)
        """
    def start_channel(self, *, ChannelId: str) -> StartChannelResponseTypeDef:
        """
        Starts an existing channel See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/StartChannel>`_
        **Request Syntax** response = client.start_channel( ChannelId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.start_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#start_channel)
        """
    def start_input_device_maintenance_window(self, *, InputDeviceId: str) -> Dict[str, Any]:
        """
        Start a maintenance window for the specified input device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.start_input_device_maintenance_window)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#start_input_device_maintenance_window)
        """
    def start_multiplex(self, *, MultiplexId: str) -> StartMultiplexResponseTypeDef:
        """
        Start (run) the multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.start_multiplex)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#start_multiplex)
        """
    def stop_channel(self, *, ChannelId: str) -> StopChannelResponseTypeDef:
        """
        Stops a running channel See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/StopChannel>`_
        **Request Syntax** response = client.stop_channel( ChannelId='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.stop_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#stop_channel)
        """
    def stop_multiplex(self, *, MultiplexId: str) -> StopMultiplexResponseTypeDef:
        """
        Stops a running multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.stop_multiplex)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#stop_multiplex)
        """
    def transfer_input_device(
        self,
        *,
        InputDeviceId: str,
        TargetCustomerId: str = None,
        TargetRegion: str = None,
        TransferMessage: str = None
    ) -> Dict[str, Any]:
        """
        Start an input device transfer to another AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.transfer_input_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#transfer_input_device)
        """
    def update_channel(
        self,
        *,
        ChannelId: str,
        CdiInputSpecification: "CdiInputSpecificationTypeDef" = None,
        Destinations: List["OutputDestinationTypeDef"] = None,
        EncoderSettings: "EncoderSettingsTypeDef" = None,
        InputAttachments: List["InputAttachmentTypeDef"] = None,
        InputSpecification: "InputSpecificationTypeDef" = None,
        LogLevel: LogLevelType = None,
        Maintenance: "MaintenanceUpdateSettingsTypeDef" = None,
        Name: str = None,
        RoleArn: str = None
    ) -> UpdateChannelResponseTypeDef:
        """
        Updates a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.update_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#update_channel)
        """
    def update_channel_class(
        self,
        *,
        ChannelClass: ChannelClassType,
        ChannelId: str,
        Destinations: List["OutputDestinationTypeDef"] = None
    ) -> UpdateChannelClassResponseTypeDef:
        """
        Changes the class of the channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.update_channel_class)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#update_channel_class)
        """
    def update_input(
        self,
        *,
        InputId: str,
        Destinations: List["InputDestinationRequestTypeDef"] = None,
        InputDevices: List["InputDeviceRequestTypeDef"] = None,
        InputSecurityGroups: List[str] = None,
        MediaConnectFlows: List["MediaConnectFlowRequestTypeDef"] = None,
        Name: str = None,
        RoleArn: str = None,
        Sources: List["InputSourceRequestTypeDef"] = None
    ) -> UpdateInputResponseTypeDef:
        """
        Updates an input.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.update_input)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#update_input)
        """
    def update_input_device(
        self,
        *,
        InputDeviceId: str,
        HdDeviceSettings: "InputDeviceConfigurableSettingsTypeDef" = None,
        Name: str = None,
        UhdDeviceSettings: "InputDeviceConfigurableSettingsTypeDef" = None
    ) -> UpdateInputDeviceResponseTypeDef:
        """
        Updates the parameters for the input device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.update_input_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#update_input_device)
        """
    def update_input_security_group(
        self,
        *,
        InputSecurityGroupId: str,
        Tags: Dict[str, str] = None,
        WhitelistRules: List["InputWhitelistRuleCidrTypeDef"] = None
    ) -> UpdateInputSecurityGroupResponseTypeDef:
        """
        Update an Input Security Group's Whilelists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.update_input_security_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#update_input_security_group)
        """
    def update_multiplex(
        self,
        *,
        MultiplexId: str,
        MultiplexSettings: "MultiplexSettingsTypeDef" = None,
        Name: str = None
    ) -> UpdateMultiplexResponseTypeDef:
        """
        Updates a multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.update_multiplex)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#update_multiplex)
        """
    def update_multiplex_program(
        self,
        *,
        MultiplexId: str,
        ProgramName: str,
        MultiplexProgramSettings: "MultiplexProgramSettingsTypeDef" = None
    ) -> UpdateMultiplexProgramResponseTypeDef:
        """
        Update a program in a multiplex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.update_multiplex_program)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#update_multiplex_program)
        """
    def update_reservation(
        self,
        *,
        ReservationId: str,
        Name: str = None,
        RenewalSettings: "RenewalSettingsTypeDef" = None
    ) -> UpdateReservationResponseTypeDef:
        """
        Update reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Client.update_reservation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/client.html#update_reservation)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_schedule"]
    ) -> DescribeSchedulePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Paginator.DescribeSchedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/paginators.html#describeschedulepaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_channels"]) -> ListChannelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Paginator.ListChannels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/paginators.html#listchannelspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_input_device_transfers"]
    ) -> ListInputDeviceTransfersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Paginator.ListInputDeviceTransfers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/paginators.html#listinputdevicetransferspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_input_devices"]
    ) -> ListInputDevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Paginator.ListInputDevices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/paginators.html#listinputdevicespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_input_security_groups"]
    ) -> ListInputSecurityGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Paginator.ListInputSecurityGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/paginators.html#listinputsecuritygroupspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_inputs"]) -> ListInputsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Paginator.ListInputs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/paginators.html#listinputspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_multiplex_programs"]
    ) -> ListMultiplexProgramsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexPrograms)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/paginators.html#listmultiplexprogramspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_multiplexes"]
    ) -> ListMultiplexesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Paginator.ListMultiplexes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/paginators.html#listmultiplexespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_offerings"]) -> ListOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Paginator.ListOfferings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/paginators.html#listofferingspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_reservations"]
    ) -> ListReservationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Paginator.ListReservations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/paginators.html#listreservationspaginator)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["channel_created"]) -> ChannelCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Waiter.ChannelCreated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#channelcreatedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["channel_deleted"]) -> ChannelDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Waiter.ChannelDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#channeldeletedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["channel_running"]) -> ChannelRunningWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Waiter.ChannelRunning)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#channelrunningwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["channel_stopped"]) -> ChannelStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Waiter.ChannelStopped)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#channelstoppedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["input_attached"]) -> InputAttachedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Waiter.InputAttached)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#inputattachedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["input_deleted"]) -> InputDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Waiter.InputDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#inputdeletedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["input_detached"]) -> InputDetachedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Waiter.InputDetached)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#inputdetachedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["multiplex_created"]) -> MultiplexCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Waiter.MultiplexCreated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#multiplexcreatedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["multiplex_deleted"]) -> MultiplexDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Waiter.MultiplexDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#multiplexdeletedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["multiplex_running"]) -> MultiplexRunningWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Waiter.MultiplexRunning)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#multiplexrunningwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["multiplex_stopped"]) -> MultiplexStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/medialive.html#MediaLive.Waiter.MultiplexStopped)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/waiters.html#multiplexstoppedwaiter)
        """
