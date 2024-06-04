"""
Type annotations for mediatailor service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_mediatailor import MediaTailorClient

    client: MediaTailorClient = boto3.client("mediatailor")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import InsertionModeType, PlaybackModeType, TierType
from .paginator import (
    GetChannelSchedulePaginator,
    ListAlertsPaginator,
    ListChannelsPaginator,
    ListLiveSourcesPaginator,
    ListPlaybackConfigurationsPaginator,
    ListPrefetchSchedulesPaginator,
    ListSourceLocationsPaginator,
    ListVodSourcesPaginator,
)
from .type_defs import (
    AccessConfigurationTypeDef,
    AdBreakTypeDef,
    AudienceMediaTypeDef,
    AvailSuppressionTypeDef,
    BumperTypeDef,
    CdnConfigurationTypeDef,
    ConfigureLogsForChannelResponseTypeDef,
    ConfigureLogsForPlaybackConfigurationResponseTypeDef,
    CreateChannelResponseTypeDef,
    CreateLiveSourceResponseTypeDef,
    CreatePrefetchScheduleResponseTypeDef,
    CreateProgramResponseTypeDef,
    CreateSourceLocationResponseTypeDef,
    CreateVodSourceResponseTypeDef,
    DashConfigurationForPutTypeDef,
    DefaultSegmentDeliveryConfigurationTypeDef,
    DescribeChannelResponseTypeDef,
    DescribeLiveSourceResponseTypeDef,
    DescribeProgramResponseTypeDef,
    DescribeSourceLocationResponseTypeDef,
    DescribeVodSourceResponseTypeDef,
    GetChannelPolicyResponseTypeDef,
    GetChannelScheduleResponseTypeDef,
    GetPlaybackConfigurationResponseTypeDef,
    GetPrefetchScheduleResponseTypeDef,
    HttpConfigurationTypeDef,
    HttpPackageConfigurationTypeDef,
    ListAlertsResponseTypeDef,
    ListChannelsResponseTypeDef,
    ListLiveSourcesResponseTypeDef,
    ListPlaybackConfigurationsResponseTypeDef,
    ListPrefetchSchedulesResponseTypeDef,
    ListSourceLocationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListVodSourcesResponseTypeDef,
    LivePreRollConfigurationTypeDef,
    ManifestProcessingRulesTypeDef,
    PrefetchConsumptionTypeDef,
    PrefetchRetrievalTypeDef,
    PutPlaybackConfigurationResponseTypeDef,
    RequestOutputItemTypeDef,
    ScheduleConfigurationTypeDef,
    SegmentDeliveryConfigurationTypeDef,
    SlateSourceTypeDef,
    TimeShiftConfigurationTypeDef,
    UpdateChannelResponseTypeDef,
    UpdateLiveSourceResponseTypeDef,
    UpdateProgramResponseTypeDef,
    UpdateProgramScheduleConfigurationTypeDef,
    UpdateSourceLocationResponseTypeDef,
    UpdateVodSourceResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("MediaTailorClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]

class MediaTailorClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MediaTailorClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#close)
        """

    def configure_logs_for_channel(
        self, *, ChannelName: str, LogTypes: List[Literal["AS_RUN"]]
    ) -> ConfigureLogsForChannelResponseTypeDef:
        """
        Configures Amazon CloudWatch log settings for a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.configure_logs_for_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#configure_logs_for_channel)
        """

    def configure_logs_for_playback_configuration(
        self, *, PercentEnabled: int, PlaybackConfigurationName: str
    ) -> ConfigureLogsForPlaybackConfigurationResponseTypeDef:
        """
        Amazon CloudWatch log settings for a playback configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.configure_logs_for_playback_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#configure_logs_for_playback_configuration)
        """

    def create_channel(
        self,
        *,
        ChannelName: str,
        Outputs: List["RequestOutputItemTypeDef"],
        PlaybackMode: PlaybackModeType,
        Audiences: List[str] = None,
        FillerSlate: "SlateSourceTypeDef" = None,
        Tags: Dict[str, str] = None,
        Tier: TierType = None,
        TimeShiftConfiguration: "TimeShiftConfigurationTypeDef" = None
    ) -> CreateChannelResponseTypeDef:
        """
        Creates a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.create_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#create_channel)
        """

    def create_live_source(
        self,
        *,
        HttpPackageConfigurations: List["HttpPackageConfigurationTypeDef"],
        LiveSourceName: str,
        SourceLocationName: str,
        Tags: Dict[str, str] = None
    ) -> CreateLiveSourceResponseTypeDef:
        """
        The live source configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.create_live_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#create_live_source)
        """

    def create_prefetch_schedule(
        self,
        *,
        Consumption: "PrefetchConsumptionTypeDef",
        Name: str,
        PlaybackConfigurationName: str,
        Retrieval: "PrefetchRetrievalTypeDef",
        StreamId: str = None
    ) -> CreatePrefetchScheduleResponseTypeDef:
        """
        Creates a prefetch schedule for a playback configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.create_prefetch_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#create_prefetch_schedule)
        """

    def create_program(
        self,
        *,
        ChannelName: str,
        ProgramName: str,
        ScheduleConfiguration: "ScheduleConfigurationTypeDef",
        SourceLocationName: str,
        AdBreaks: List["AdBreakTypeDef"] = None,
        AudienceMedia: List["AudienceMediaTypeDef"] = None,
        LiveSourceName: str = None,
        VodSourceName: str = None
    ) -> CreateProgramResponseTypeDef:
        """
        Creates a program within a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.create_program)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#create_program)
        """

    def create_source_location(
        self,
        *,
        HttpConfiguration: "HttpConfigurationTypeDef",
        SourceLocationName: str,
        AccessConfiguration: "AccessConfigurationTypeDef" = None,
        DefaultSegmentDeliveryConfiguration: "DefaultSegmentDeliveryConfigurationTypeDef" = None,
        SegmentDeliveryConfigurations: List["SegmentDeliveryConfigurationTypeDef"] = None,
        Tags: Dict[str, str] = None
    ) -> CreateSourceLocationResponseTypeDef:
        """
        Creates a source location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.create_source_location)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#create_source_location)
        """

    def create_vod_source(
        self,
        *,
        HttpPackageConfigurations: List["HttpPackageConfigurationTypeDef"],
        SourceLocationName: str,
        VodSourceName: str,
        Tags: Dict[str, str] = None
    ) -> CreateVodSourceResponseTypeDef:
        """
        The VOD source configuration parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.create_vod_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#create_vod_source)
        """

    def delete_channel(self, *, ChannelName: str) -> Dict[str, Any]:
        """
        Deletes a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.delete_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#delete_channel)
        """

    def delete_channel_policy(self, *, ChannelName: str) -> Dict[str, Any]:
        """
        The channel policy to delete.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.delete_channel_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#delete_channel_policy)
        """

    def delete_live_source(self, *, LiveSourceName: str, SourceLocationName: str) -> Dict[str, Any]:
        """
        The live source to delete.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.delete_live_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#delete_live_source)
        """

    def delete_playback_configuration(self, *, Name: str) -> Dict[str, Any]:
        """
        Deletes a playback configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.delete_playback_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#delete_playback_configuration)
        """

    def delete_prefetch_schedule(
        self, *, Name: str, PlaybackConfigurationName: str
    ) -> Dict[str, Any]:
        """
        Deletes a prefetch schedule for a specific playback configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.delete_prefetch_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#delete_prefetch_schedule)
        """

    def delete_program(self, *, ChannelName: str, ProgramName: str) -> Dict[str, Any]:
        """
        Deletes a program within a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.delete_program)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#delete_program)
        """

    def delete_source_location(self, *, SourceLocationName: str) -> Dict[str, Any]:
        """
        Deletes a source location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.delete_source_location)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#delete_source_location)
        """

    def delete_vod_source(self, *, SourceLocationName: str, VodSourceName: str) -> Dict[str, Any]:
        """
        The video on demand (VOD) source to delete.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.delete_vod_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#delete_vod_source)
        """

    def describe_channel(self, *, ChannelName: str) -> DescribeChannelResponseTypeDef:
        """
        Describes a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.describe_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#describe_channel)
        """

    def describe_live_source(
        self, *, LiveSourceName: str, SourceLocationName: str
    ) -> DescribeLiveSourceResponseTypeDef:
        """
        The live source to describe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.describe_live_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#describe_live_source)
        """

    def describe_program(
        self, *, ChannelName: str, ProgramName: str
    ) -> DescribeProgramResponseTypeDef:
        """
        Describes a program within a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.describe_program)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#describe_program)
        """

    def describe_source_location(
        self, *, SourceLocationName: str
    ) -> DescribeSourceLocationResponseTypeDef:
        """
        Describes a source location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.describe_source_location)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#describe_source_location)
        """

    def describe_vod_source(
        self, *, SourceLocationName: str, VodSourceName: str
    ) -> DescribeVodSourceResponseTypeDef:
        """
        Provides details about a specific video on demand (VOD) source in a specific
        source location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.describe_vod_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#describe_vod_source)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#generate_presigned_url)
        """

    def get_channel_policy(self, *, ChannelName: str) -> GetChannelPolicyResponseTypeDef:
        """
        Returns the channel's IAM policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.get_channel_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#get_channel_policy)
        """

    def get_channel_schedule(
        self,
        *,
        ChannelName: str,
        Audience: str = None,
        DurationMinutes: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetChannelScheduleResponseTypeDef:
        """
        Retrieves information about your channel's schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.get_channel_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#get_channel_schedule)
        """

    def get_playback_configuration(self, *, Name: str) -> GetPlaybackConfigurationResponseTypeDef:
        """
        Retrieves a playback configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.get_playback_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#get_playback_configuration)
        """

    def get_prefetch_schedule(
        self, *, Name: str, PlaybackConfigurationName: str
    ) -> GetPrefetchScheduleResponseTypeDef:
        """
        Retrieves a prefetch schedule for a playback configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.get_prefetch_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#get_prefetch_schedule)
        """

    def list_alerts(
        self, *, ResourceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAlertsResponseTypeDef:
        """
        Lists the alerts that are associated with a MediaTailor channel assembly
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.list_alerts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#list_alerts)
        """

    def list_channels(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListChannelsResponseTypeDef:
        """
        Retrieves information about the channels that are associated with the current
        AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.list_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#list_channels)
        """

    def list_live_sources(
        self, *, SourceLocationName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListLiveSourcesResponseTypeDef:
        """
        Lists the live sources contained in a source location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.list_live_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#list_live_sources)
        """

    def list_playback_configurations(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListPlaybackConfigurationsResponseTypeDef:
        """
        Retrieves existing playback configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.list_playback_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#list_playback_configurations)
        """

    def list_prefetch_schedules(
        self,
        *,
        PlaybackConfigurationName: str,
        MaxResults: int = None,
        NextToken: str = None,
        StreamId: str = None
    ) -> ListPrefetchSchedulesResponseTypeDef:
        """
        Lists the prefetch schedules for a playback configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.list_prefetch_schedules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#list_prefetch_schedules)
        """

    def list_source_locations(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListSourceLocationsResponseTypeDef:
        """
        Lists the source locations for a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.list_source_locations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#list_source_locations)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        A list of tags that are associated with this resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#list_tags_for_resource)
        """

    def list_vod_sources(
        self, *, SourceLocationName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListVodSourcesResponseTypeDef:
        """
        Lists the VOD sources contained in a source location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.list_vod_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#list_vod_sources)
        """

    def put_channel_policy(self, *, ChannelName: str, Policy: str) -> Dict[str, Any]:
        """
        Creates an IAM policy for the channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.put_channel_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#put_channel_policy)
        """

    def put_playback_configuration(
        self,
        *,
        Name: str,
        AdDecisionServerUrl: str = None,
        AvailSuppression: "AvailSuppressionTypeDef" = None,
        Bumper: "BumperTypeDef" = None,
        CdnConfiguration: "CdnConfigurationTypeDef" = None,
        ConfigurationAliases: Dict[str, Dict[str, str]] = None,
        DashConfiguration: "DashConfigurationForPutTypeDef" = None,
        InsertionMode: InsertionModeType = None,
        LivePreRollConfiguration: "LivePreRollConfigurationTypeDef" = None,
        ManifestProcessingRules: "ManifestProcessingRulesTypeDef" = None,
        PersonalizationThresholdSeconds: int = None,
        SlateAdUrl: str = None,
        Tags: Dict[str, str] = None,
        TranscodeProfileName: str = None,
        VideoContentSourceUrl: str = None
    ) -> PutPlaybackConfigurationResponseTypeDef:
        """
        Creates a playback configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.put_playback_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#put_playback_configuration)
        """

    def start_channel(self, *, ChannelName: str) -> Dict[str, Any]:
        """
        Starts a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.start_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#start_channel)
        """

    def stop_channel(self, *, ChannelName: str) -> Dict[str, Any]:
        """
        Stops a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.stop_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#stop_channel)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        The resource to tag.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        The resource to untag.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#untag_resource)
        """

    def update_channel(
        self,
        *,
        ChannelName: str,
        Outputs: List["RequestOutputItemTypeDef"],
        Audiences: List[str] = None,
        FillerSlate: "SlateSourceTypeDef" = None,
        TimeShiftConfiguration: "TimeShiftConfigurationTypeDef" = None
    ) -> UpdateChannelResponseTypeDef:
        """
        Updates a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.update_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#update_channel)
        """

    def update_live_source(
        self,
        *,
        HttpPackageConfigurations: List["HttpPackageConfigurationTypeDef"],
        LiveSourceName: str,
        SourceLocationName: str
    ) -> UpdateLiveSourceResponseTypeDef:
        """
        Updates a live source's configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.update_live_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#update_live_source)
        """

    def update_program(
        self,
        *,
        ChannelName: str,
        ProgramName: str,
        ScheduleConfiguration: "UpdateProgramScheduleConfigurationTypeDef",
        AdBreaks: List["AdBreakTypeDef"] = None,
        AudienceMedia: List["AudienceMediaTypeDef"] = None
    ) -> UpdateProgramResponseTypeDef:
        """
        Updates a program within a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.update_program)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#update_program)
        """

    def update_source_location(
        self,
        *,
        HttpConfiguration: "HttpConfigurationTypeDef",
        SourceLocationName: str,
        AccessConfiguration: "AccessConfigurationTypeDef" = None,
        DefaultSegmentDeliveryConfiguration: "DefaultSegmentDeliveryConfigurationTypeDef" = None,
        SegmentDeliveryConfigurations: List["SegmentDeliveryConfigurationTypeDef"] = None
    ) -> UpdateSourceLocationResponseTypeDef:
        """
        Updates a source location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.update_source_location)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#update_source_location)
        """

    def update_vod_source(
        self,
        *,
        HttpPackageConfigurations: List["HttpPackageConfigurationTypeDef"],
        SourceLocationName: str,
        VodSourceName: str
    ) -> UpdateVodSourceResponseTypeDef:
        """
        Updates a VOD source's configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Client.update_vod_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/client.html#update_vod_source)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_channel_schedule"]
    ) -> GetChannelSchedulePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Paginator.GetChannelSchedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators.html#getchannelschedulepaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_alerts"]) -> ListAlertsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Paginator.ListAlerts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators.html#listalertspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_channels"]) -> ListChannelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Paginator.ListChannels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators.html#listchannelspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_live_sources"]
    ) -> ListLiveSourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Paginator.ListLiveSources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators.html#listlivesourcespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_playback_configurations"]
    ) -> ListPlaybackConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Paginator.ListPlaybackConfigurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators.html#listplaybackconfigurationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_prefetch_schedules"]
    ) -> ListPrefetchSchedulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Paginator.ListPrefetchSchedules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators.html#listprefetchschedulespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_source_locations"]
    ) -> ListSourceLocationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Paginator.ListSourceLocations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators.html#listsourcelocationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_vod_sources"]) -> ListVodSourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mediatailor.html#MediaTailor.Paginator.ListVodSources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/paginators.html#listvodsourcespaginator)
        """
