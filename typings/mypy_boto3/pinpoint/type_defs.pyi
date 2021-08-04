"""
Type annotations for pinpoint service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/type_defs.html)

Usage::

    ```python
    from mypy_boto3_pinpoint.type_defs import ADMChannelRequestTypeDef

    data: ADMChannelRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ActionType,
    AttributeTypeType,
    CampaignStatusType,
    ChannelTypeType,
    DeliveryStatusType,
    DimensionTypeType,
    DurationType,
    FilterTypeType,
    FormatType,
    FrequencyType,
    IncludeType,
    JobStatusType,
    MessageTypeType,
    ModeType,
    OperatorType,
    RecencyTypeType,
    SegmentTypeType,
    SourceTypeType,
    StateType,
    TemplateTypeType,
    TypeType,
    __EndpointTypesElementType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ADMChannelRequestTypeDef",
    "ADMChannelResponseTypeDef",
    "ADMMessageTypeDef",
    "APNSChannelRequestTypeDef",
    "APNSChannelResponseTypeDef",
    "APNSMessageTypeDef",
    "APNSPushNotificationTemplateTypeDef",
    "APNSSandboxChannelRequestTypeDef",
    "APNSSandboxChannelResponseTypeDef",
    "APNSVoipChannelRequestTypeDef",
    "APNSVoipChannelResponseTypeDef",
    "APNSVoipSandboxChannelRequestTypeDef",
    "APNSVoipSandboxChannelResponseTypeDef",
    "ActivitiesResponseTypeDef",
    "ActivityResponseTypeDef",
    "ActivityTypeDef",
    "AddressConfigurationTypeDef",
    "AndroidPushNotificationTemplateTypeDef",
    "ApplicationDateRangeKpiResponseTypeDef",
    "ApplicationResponseTypeDef",
    "ApplicationSettingsResourceTypeDef",
    "ApplicationsResponseTypeDef",
    "AttributeDimensionTypeDef",
    "AttributesResourceTypeDef",
    "BaiduChannelRequestTypeDef",
    "BaiduChannelResponseTypeDef",
    "BaiduMessageTypeDef",
    "BaseKpiResultTypeDef",
    "CampaignCustomMessageTypeDef",
    "CampaignDateRangeKpiResponseTypeDef",
    "CampaignEmailMessageTypeDef",
    "CampaignEventFilterTypeDef",
    "CampaignHookTypeDef",
    "CampaignLimitsTypeDef",
    "CampaignResponseTypeDef",
    "CampaignSmsMessageTypeDef",
    "CampaignStateTypeDef",
    "CampaignsResponseTypeDef",
    "ChannelResponseTypeDef",
    "ChannelsResponseTypeDef",
    "ConditionTypeDef",
    "ConditionalSplitActivityTypeDef",
    "CreateAppRequestRequestTypeDef",
    "CreateAppResponseTypeDef",
    "CreateApplicationRequestTypeDef",
    "CreateCampaignRequestRequestTypeDef",
    "CreateCampaignResponseTypeDef",
    "CreateEmailTemplateRequestRequestTypeDef",
    "CreateEmailTemplateResponseTypeDef",
    "CreateExportJobRequestRequestTypeDef",
    "CreateExportJobResponseTypeDef",
    "CreateImportJobRequestRequestTypeDef",
    "CreateImportJobResponseTypeDef",
    "CreateJourneyRequestRequestTypeDef",
    "CreateJourneyResponseTypeDef",
    "CreatePushTemplateRequestRequestTypeDef",
    "CreatePushTemplateResponseTypeDef",
    "CreateRecommenderConfigurationRequestRequestTypeDef",
    "CreateRecommenderConfigurationResponseTypeDef",
    "CreateRecommenderConfigurationTypeDef",
    "CreateSegmentRequestRequestTypeDef",
    "CreateSegmentResponseTypeDef",
    "CreateSmsTemplateRequestRequestTypeDef",
    "CreateSmsTemplateResponseTypeDef",
    "CreateTemplateMessageBodyTypeDef",
    "CreateVoiceTemplateRequestRequestTypeDef",
    "CreateVoiceTemplateResponseTypeDef",
    "CustomDeliveryConfigurationTypeDef",
    "CustomMessageActivityTypeDef",
    "DefaultMessageTypeDef",
    "DefaultPushNotificationMessageTypeDef",
    "DefaultPushNotificationTemplateTypeDef",
    "DeleteAdmChannelRequestRequestTypeDef",
    "DeleteAdmChannelResponseTypeDef",
    "DeleteApnsChannelRequestRequestTypeDef",
    "DeleteApnsChannelResponseTypeDef",
    "DeleteApnsSandboxChannelRequestRequestTypeDef",
    "DeleteApnsSandboxChannelResponseTypeDef",
    "DeleteApnsVoipChannelRequestRequestTypeDef",
    "DeleteApnsVoipChannelResponseTypeDef",
    "DeleteApnsVoipSandboxChannelRequestRequestTypeDef",
    "DeleteApnsVoipSandboxChannelResponseTypeDef",
    "DeleteAppRequestRequestTypeDef",
    "DeleteAppResponseTypeDef",
    "DeleteBaiduChannelRequestRequestTypeDef",
    "DeleteBaiduChannelResponseTypeDef",
    "DeleteCampaignRequestRequestTypeDef",
    "DeleteCampaignResponseTypeDef",
    "DeleteEmailChannelRequestRequestTypeDef",
    "DeleteEmailChannelResponseTypeDef",
    "DeleteEmailTemplateRequestRequestTypeDef",
    "DeleteEmailTemplateResponseTypeDef",
    "DeleteEndpointRequestRequestTypeDef",
    "DeleteEndpointResponseTypeDef",
    "DeleteEventStreamRequestRequestTypeDef",
    "DeleteEventStreamResponseTypeDef",
    "DeleteGcmChannelRequestRequestTypeDef",
    "DeleteGcmChannelResponseTypeDef",
    "DeleteJourneyRequestRequestTypeDef",
    "DeleteJourneyResponseTypeDef",
    "DeletePushTemplateRequestRequestTypeDef",
    "DeletePushTemplateResponseTypeDef",
    "DeleteRecommenderConfigurationRequestRequestTypeDef",
    "DeleteRecommenderConfigurationResponseTypeDef",
    "DeleteSegmentRequestRequestTypeDef",
    "DeleteSegmentResponseTypeDef",
    "DeleteSmsChannelRequestRequestTypeDef",
    "DeleteSmsChannelResponseTypeDef",
    "DeleteSmsTemplateRequestRequestTypeDef",
    "DeleteSmsTemplateResponseTypeDef",
    "DeleteUserEndpointsRequestRequestTypeDef",
    "DeleteUserEndpointsResponseTypeDef",
    "DeleteVoiceChannelRequestRequestTypeDef",
    "DeleteVoiceChannelResponseTypeDef",
    "DeleteVoiceTemplateRequestRequestTypeDef",
    "DeleteVoiceTemplateResponseTypeDef",
    "DirectMessageConfigurationTypeDef",
    "EmailChannelRequestTypeDef",
    "EmailChannelResponseTypeDef",
    "EmailMessageActivityTypeDef",
    "EmailMessageTypeDef",
    "EmailTemplateRequestTypeDef",
    "EmailTemplateResponseTypeDef",
    "EndpointBatchItemTypeDef",
    "EndpointBatchRequestTypeDef",
    "EndpointDemographicTypeDef",
    "EndpointItemResponseTypeDef",
    "EndpointLocationTypeDef",
    "EndpointMessageResultTypeDef",
    "EndpointRequestTypeDef",
    "EndpointResponseTypeDef",
    "EndpointSendConfigurationTypeDef",
    "EndpointUserTypeDef",
    "EndpointsResponseTypeDef",
    "EventConditionTypeDef",
    "EventDimensionsTypeDef",
    "EventFilterTypeDef",
    "EventItemResponseTypeDef",
    "EventStartConditionTypeDef",
    "EventStreamTypeDef",
    "EventTypeDef",
    "EventsBatchTypeDef",
    "EventsRequestTypeDef",
    "EventsResponseTypeDef",
    "ExportJobRequestTypeDef",
    "ExportJobResourceTypeDef",
    "ExportJobResponseTypeDef",
    "ExportJobsResponseTypeDef",
    "GCMChannelRequestTypeDef",
    "GCMChannelResponseTypeDef",
    "GCMMessageTypeDef",
    "GPSCoordinatesTypeDef",
    "GPSPointDimensionTypeDef",
    "GetAdmChannelRequestRequestTypeDef",
    "GetAdmChannelResponseTypeDef",
    "GetApnsChannelRequestRequestTypeDef",
    "GetApnsChannelResponseTypeDef",
    "GetApnsSandboxChannelRequestRequestTypeDef",
    "GetApnsSandboxChannelResponseTypeDef",
    "GetApnsVoipChannelRequestRequestTypeDef",
    "GetApnsVoipChannelResponseTypeDef",
    "GetApnsVoipSandboxChannelRequestRequestTypeDef",
    "GetApnsVoipSandboxChannelResponseTypeDef",
    "GetAppRequestRequestTypeDef",
    "GetAppResponseTypeDef",
    "GetApplicationDateRangeKpiRequestRequestTypeDef",
    "GetApplicationDateRangeKpiResponseTypeDef",
    "GetApplicationSettingsRequestRequestTypeDef",
    "GetApplicationSettingsResponseTypeDef",
    "GetAppsRequestRequestTypeDef",
    "GetAppsResponseTypeDef",
    "GetBaiduChannelRequestRequestTypeDef",
    "GetBaiduChannelResponseTypeDef",
    "GetCampaignActivitiesRequestRequestTypeDef",
    "GetCampaignActivitiesResponseTypeDef",
    "GetCampaignDateRangeKpiRequestRequestTypeDef",
    "GetCampaignDateRangeKpiResponseTypeDef",
    "GetCampaignRequestRequestTypeDef",
    "GetCampaignResponseTypeDef",
    "GetCampaignVersionRequestRequestTypeDef",
    "GetCampaignVersionResponseTypeDef",
    "GetCampaignVersionsRequestRequestTypeDef",
    "GetCampaignVersionsResponseTypeDef",
    "GetCampaignsRequestRequestTypeDef",
    "GetCampaignsResponseTypeDef",
    "GetChannelsRequestRequestTypeDef",
    "GetChannelsResponseTypeDef",
    "GetEmailChannelRequestRequestTypeDef",
    "GetEmailChannelResponseTypeDef",
    "GetEmailTemplateRequestRequestTypeDef",
    "GetEmailTemplateResponseTypeDef",
    "GetEndpointRequestRequestTypeDef",
    "GetEndpointResponseTypeDef",
    "GetEventStreamRequestRequestTypeDef",
    "GetEventStreamResponseTypeDef",
    "GetExportJobRequestRequestTypeDef",
    "GetExportJobResponseTypeDef",
    "GetExportJobsRequestRequestTypeDef",
    "GetExportJobsResponseTypeDef",
    "GetGcmChannelRequestRequestTypeDef",
    "GetGcmChannelResponseTypeDef",
    "GetImportJobRequestRequestTypeDef",
    "GetImportJobResponseTypeDef",
    "GetImportJobsRequestRequestTypeDef",
    "GetImportJobsResponseTypeDef",
    "GetJourneyDateRangeKpiRequestRequestTypeDef",
    "GetJourneyDateRangeKpiResponseTypeDef",
    "GetJourneyExecutionActivityMetricsRequestRequestTypeDef",
    "GetJourneyExecutionActivityMetricsResponseTypeDef",
    "GetJourneyExecutionMetricsRequestRequestTypeDef",
    "GetJourneyExecutionMetricsResponseTypeDef",
    "GetJourneyRequestRequestTypeDef",
    "GetJourneyResponseTypeDef",
    "GetPushTemplateRequestRequestTypeDef",
    "GetPushTemplateResponseTypeDef",
    "GetRecommenderConfigurationRequestRequestTypeDef",
    "GetRecommenderConfigurationResponseTypeDef",
    "GetRecommenderConfigurationsRequestRequestTypeDef",
    "GetRecommenderConfigurationsResponseTypeDef",
    "GetSegmentExportJobsRequestRequestTypeDef",
    "GetSegmentExportJobsResponseTypeDef",
    "GetSegmentImportJobsRequestRequestTypeDef",
    "GetSegmentImportJobsResponseTypeDef",
    "GetSegmentRequestRequestTypeDef",
    "GetSegmentResponseTypeDef",
    "GetSegmentVersionRequestRequestTypeDef",
    "GetSegmentVersionResponseTypeDef",
    "GetSegmentVersionsRequestRequestTypeDef",
    "GetSegmentVersionsResponseTypeDef",
    "GetSegmentsRequestRequestTypeDef",
    "GetSegmentsResponseTypeDef",
    "GetSmsChannelRequestRequestTypeDef",
    "GetSmsChannelResponseTypeDef",
    "GetSmsTemplateRequestRequestTypeDef",
    "GetSmsTemplateResponseTypeDef",
    "GetUserEndpointsRequestRequestTypeDef",
    "GetUserEndpointsResponseTypeDef",
    "GetVoiceChannelRequestRequestTypeDef",
    "GetVoiceChannelResponseTypeDef",
    "GetVoiceTemplateRequestRequestTypeDef",
    "GetVoiceTemplateResponseTypeDef",
    "HoldoutActivityTypeDef",
    "ImportJobRequestTypeDef",
    "ImportJobResourceTypeDef",
    "ImportJobResponseTypeDef",
    "ImportJobsResponseTypeDef",
    "ItemResponseTypeDef",
    "JourneyCustomMessageTypeDef",
    "JourneyDateRangeKpiResponseTypeDef",
    "JourneyEmailMessageTypeDef",
    "JourneyExecutionActivityMetricsResponseTypeDef",
    "JourneyExecutionMetricsResponseTypeDef",
    "JourneyLimitsTypeDef",
    "JourneyPushMessageTypeDef",
    "JourneyResponseTypeDef",
    "JourneySMSMessageTypeDef",
    "JourneyScheduleTypeDef",
    "JourneyStateRequestTypeDef",
    "JourneysResponseTypeDef",
    "ListJourneysRequestRequestTypeDef",
    "ListJourneysResponseTypeDef",
    "ListRecommenderConfigurationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTemplateVersionsRequestRequestTypeDef",
    "ListTemplateVersionsResponseTypeDef",
    "ListTemplatesRequestRequestTypeDef",
    "ListTemplatesResponseTypeDef",
    "MessageBodyTypeDef",
    "MessageConfigurationTypeDef",
    "MessageRequestTypeDef",
    "MessageResponseTypeDef",
    "MessageResultTypeDef",
    "MessageTypeDef",
    "MetricDimensionTypeDef",
    "MultiConditionalBranchTypeDef",
    "MultiConditionalSplitActivityTypeDef",
    "NumberValidateRequestTypeDef",
    "NumberValidateResponseTypeDef",
    "PhoneNumberValidateRequestRequestTypeDef",
    "PhoneNumberValidateResponseTypeDef",
    "PublicEndpointTypeDef",
    "PushMessageActivityTypeDef",
    "PushNotificationTemplateRequestTypeDef",
    "PushNotificationTemplateResponseTypeDef",
    "PutEventStreamRequestRequestTypeDef",
    "PutEventStreamResponseTypeDef",
    "PutEventsRequestRequestTypeDef",
    "PutEventsResponseTypeDef",
    "QuietTimeTypeDef",
    "RandomSplitActivityTypeDef",
    "RandomSplitEntryTypeDef",
    "RawEmailTypeDef",
    "RecencyDimensionTypeDef",
    "RecommenderConfigurationResponseTypeDef",
    "RemoveAttributesRequestRequestTypeDef",
    "RemoveAttributesResponseTypeDef",
    "ResponseMetadataTypeDef",
    "ResultRowTypeDef",
    "ResultRowValueTypeDef",
    "SMSChannelRequestTypeDef",
    "SMSChannelResponseTypeDef",
    "SMSMessageActivityTypeDef",
    "SMSMessageTypeDef",
    "SMSTemplateRequestTypeDef",
    "SMSTemplateResponseTypeDef",
    "ScheduleTypeDef",
    "SegmentBehaviorsTypeDef",
    "SegmentConditionTypeDef",
    "SegmentDemographicsTypeDef",
    "SegmentDimensionsTypeDef",
    "SegmentGroupListTypeDef",
    "SegmentGroupTypeDef",
    "SegmentImportResourceTypeDef",
    "SegmentLocationTypeDef",
    "SegmentReferenceTypeDef",
    "SegmentResponseTypeDef",
    "SegmentsResponseTypeDef",
    "SendMessagesRequestRequestTypeDef",
    "SendMessagesResponseTypeDef",
    "SendUsersMessageRequestTypeDef",
    "SendUsersMessageResponseTypeDef",
    "SendUsersMessagesRequestRequestTypeDef",
    "SendUsersMessagesResponseTypeDef",
    "SessionTypeDef",
    "SetDimensionTypeDef",
    "SimpleConditionTypeDef",
    "SimpleEmailPartTypeDef",
    "SimpleEmailTypeDef",
    "StartConditionTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagsModelTypeDef",
    "TemplateActiveVersionRequestTypeDef",
    "TemplateConfigurationTypeDef",
    "TemplateResponseTypeDef",
    "TemplateTypeDef",
    "TemplateVersionResponseTypeDef",
    "TemplateVersionsResponseTypeDef",
    "TemplatesResponseTypeDef",
    "TreatmentResourceTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAdmChannelRequestRequestTypeDef",
    "UpdateAdmChannelResponseTypeDef",
    "UpdateApnsChannelRequestRequestTypeDef",
    "UpdateApnsChannelResponseTypeDef",
    "UpdateApnsSandboxChannelRequestRequestTypeDef",
    "UpdateApnsSandboxChannelResponseTypeDef",
    "UpdateApnsVoipChannelRequestRequestTypeDef",
    "UpdateApnsVoipChannelResponseTypeDef",
    "UpdateApnsVoipSandboxChannelRequestRequestTypeDef",
    "UpdateApnsVoipSandboxChannelResponseTypeDef",
    "UpdateApplicationSettingsRequestRequestTypeDef",
    "UpdateApplicationSettingsResponseTypeDef",
    "UpdateAttributesRequestTypeDef",
    "UpdateBaiduChannelRequestRequestTypeDef",
    "UpdateBaiduChannelResponseTypeDef",
    "UpdateCampaignRequestRequestTypeDef",
    "UpdateCampaignResponseTypeDef",
    "UpdateEmailChannelRequestRequestTypeDef",
    "UpdateEmailChannelResponseTypeDef",
    "UpdateEmailTemplateRequestRequestTypeDef",
    "UpdateEmailTemplateResponseTypeDef",
    "UpdateEndpointRequestRequestTypeDef",
    "UpdateEndpointResponseTypeDef",
    "UpdateEndpointsBatchRequestRequestTypeDef",
    "UpdateEndpointsBatchResponseTypeDef",
    "UpdateGcmChannelRequestRequestTypeDef",
    "UpdateGcmChannelResponseTypeDef",
    "UpdateJourneyRequestRequestTypeDef",
    "UpdateJourneyResponseTypeDef",
    "UpdateJourneyStateRequestRequestTypeDef",
    "UpdateJourneyStateResponseTypeDef",
    "UpdatePushTemplateRequestRequestTypeDef",
    "UpdatePushTemplateResponseTypeDef",
    "UpdateRecommenderConfigurationRequestRequestTypeDef",
    "UpdateRecommenderConfigurationResponseTypeDef",
    "UpdateRecommenderConfigurationTypeDef",
    "UpdateSegmentRequestRequestTypeDef",
    "UpdateSegmentResponseTypeDef",
    "UpdateSmsChannelRequestRequestTypeDef",
    "UpdateSmsChannelResponseTypeDef",
    "UpdateSmsTemplateRequestRequestTypeDef",
    "UpdateSmsTemplateResponseTypeDef",
    "UpdateTemplateActiveVersionRequestRequestTypeDef",
    "UpdateTemplateActiveVersionResponseTypeDef",
    "UpdateVoiceChannelRequestRequestTypeDef",
    "UpdateVoiceChannelResponseTypeDef",
    "UpdateVoiceTemplateRequestRequestTypeDef",
    "UpdateVoiceTemplateResponseTypeDef",
    "VoiceChannelRequestTypeDef",
    "VoiceChannelResponseTypeDef",
    "VoiceMessageTypeDef",
    "VoiceTemplateRequestTypeDef",
    "VoiceTemplateResponseTypeDef",
    "WaitActivityTypeDef",
    "WaitTimeTypeDef",
    "WriteApplicationSettingsRequestTypeDef",
    "WriteCampaignRequestTypeDef",
    "WriteEventStreamTypeDef",
    "WriteJourneyRequestTypeDef",
    "WriteSegmentRequestTypeDef",
    "WriteTreatmentResourceTypeDef",
)

_RequiredADMChannelRequestTypeDef = TypedDict(
    "_RequiredADMChannelRequestTypeDef",
    {
        "ClientId": str,
        "ClientSecret": str,
    },
)
_OptionalADMChannelRequestTypeDef = TypedDict(
    "_OptionalADMChannelRequestTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

class ADMChannelRequestTypeDef(
    _RequiredADMChannelRequestTypeDef, _OptionalADMChannelRequestTypeDef
):
    pass

_RequiredADMChannelResponseTypeDef = TypedDict(
    "_RequiredADMChannelResponseTypeDef",
    {
        "Platform": str,
    },
)
_OptionalADMChannelResponseTypeDef = TypedDict(
    "_OptionalADMChannelResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "Enabled": bool,
        "HasCredential": bool,
        "Id": str,
        "IsArchived": bool,
        "LastModifiedBy": str,
        "LastModifiedDate": str,
        "Version": int,
    },
    total=False,
)

class ADMChannelResponseTypeDef(
    _RequiredADMChannelResponseTypeDef, _OptionalADMChannelResponseTypeDef
):
    pass

ADMMessageTypeDef = TypedDict(
    "ADMMessageTypeDef",
    {
        "Action": ActionType,
        "Body": str,
        "ConsolidationKey": str,
        "Data": Dict[str, str],
        "ExpiresAfter": str,
        "IconReference": str,
        "ImageIconUrl": str,
        "ImageUrl": str,
        "MD5": str,
        "RawContent": str,
        "SilentPush": bool,
        "SmallImageIconUrl": str,
        "Sound": str,
        "Substitutions": Dict[str, List[str]],
        "Title": str,
        "Url": str,
    },
    total=False,
)

APNSChannelRequestTypeDef = TypedDict(
    "APNSChannelRequestTypeDef",
    {
        "BundleId": str,
        "Certificate": str,
        "DefaultAuthenticationMethod": str,
        "Enabled": bool,
        "PrivateKey": str,
        "TeamId": str,
        "TokenKey": str,
        "TokenKeyId": str,
    },
    total=False,
)

_RequiredAPNSChannelResponseTypeDef = TypedDict(
    "_RequiredAPNSChannelResponseTypeDef",
    {
        "Platform": str,
    },
)
_OptionalAPNSChannelResponseTypeDef = TypedDict(
    "_OptionalAPNSChannelResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "DefaultAuthenticationMethod": str,
        "Enabled": bool,
        "HasCredential": bool,
        "HasTokenKey": bool,
        "Id": str,
        "IsArchived": bool,
        "LastModifiedBy": str,
        "LastModifiedDate": str,
        "Version": int,
    },
    total=False,
)

class APNSChannelResponseTypeDef(
    _RequiredAPNSChannelResponseTypeDef, _OptionalAPNSChannelResponseTypeDef
):
    pass

APNSMessageTypeDef = TypedDict(
    "APNSMessageTypeDef",
    {
        "APNSPushType": str,
        "Action": ActionType,
        "Badge": int,
        "Body": str,
        "Category": str,
        "CollapseId": str,
        "Data": Dict[str, str],
        "MediaUrl": str,
        "PreferredAuthenticationMethod": str,
        "Priority": str,
        "RawContent": str,
        "SilentPush": bool,
        "Sound": str,
        "Substitutions": Dict[str, List[str]],
        "ThreadId": str,
        "TimeToLive": int,
        "Title": str,
        "Url": str,
    },
    total=False,
)

APNSPushNotificationTemplateTypeDef = TypedDict(
    "APNSPushNotificationTemplateTypeDef",
    {
        "Action": ActionType,
        "Body": str,
        "MediaUrl": str,
        "RawContent": str,
        "Sound": str,
        "Title": str,
        "Url": str,
    },
    total=False,
)

APNSSandboxChannelRequestTypeDef = TypedDict(
    "APNSSandboxChannelRequestTypeDef",
    {
        "BundleId": str,
        "Certificate": str,
        "DefaultAuthenticationMethod": str,
        "Enabled": bool,
        "PrivateKey": str,
        "TeamId": str,
        "TokenKey": str,
        "TokenKeyId": str,
    },
    total=False,
)

_RequiredAPNSSandboxChannelResponseTypeDef = TypedDict(
    "_RequiredAPNSSandboxChannelResponseTypeDef",
    {
        "Platform": str,
    },
)
_OptionalAPNSSandboxChannelResponseTypeDef = TypedDict(
    "_OptionalAPNSSandboxChannelResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "DefaultAuthenticationMethod": str,
        "Enabled": bool,
        "HasCredential": bool,
        "HasTokenKey": bool,
        "Id": str,
        "IsArchived": bool,
        "LastModifiedBy": str,
        "LastModifiedDate": str,
        "Version": int,
    },
    total=False,
)

class APNSSandboxChannelResponseTypeDef(
    _RequiredAPNSSandboxChannelResponseTypeDef, _OptionalAPNSSandboxChannelResponseTypeDef
):
    pass

APNSVoipChannelRequestTypeDef = TypedDict(
    "APNSVoipChannelRequestTypeDef",
    {
        "BundleId": str,
        "Certificate": str,
        "DefaultAuthenticationMethod": str,
        "Enabled": bool,
        "PrivateKey": str,
        "TeamId": str,
        "TokenKey": str,
        "TokenKeyId": str,
    },
    total=False,
)

_RequiredAPNSVoipChannelResponseTypeDef = TypedDict(
    "_RequiredAPNSVoipChannelResponseTypeDef",
    {
        "Platform": str,
    },
)
_OptionalAPNSVoipChannelResponseTypeDef = TypedDict(
    "_OptionalAPNSVoipChannelResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "DefaultAuthenticationMethod": str,
        "Enabled": bool,
        "HasCredential": bool,
        "HasTokenKey": bool,
        "Id": str,
        "IsArchived": bool,
        "LastModifiedBy": str,
        "LastModifiedDate": str,
        "Version": int,
    },
    total=False,
)

class APNSVoipChannelResponseTypeDef(
    _RequiredAPNSVoipChannelResponseTypeDef, _OptionalAPNSVoipChannelResponseTypeDef
):
    pass

APNSVoipSandboxChannelRequestTypeDef = TypedDict(
    "APNSVoipSandboxChannelRequestTypeDef",
    {
        "BundleId": str,
        "Certificate": str,
        "DefaultAuthenticationMethod": str,
        "Enabled": bool,
        "PrivateKey": str,
        "TeamId": str,
        "TokenKey": str,
        "TokenKeyId": str,
    },
    total=False,
)

_RequiredAPNSVoipSandboxChannelResponseTypeDef = TypedDict(
    "_RequiredAPNSVoipSandboxChannelResponseTypeDef",
    {
        "Platform": str,
    },
)
_OptionalAPNSVoipSandboxChannelResponseTypeDef = TypedDict(
    "_OptionalAPNSVoipSandboxChannelResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "DefaultAuthenticationMethod": str,
        "Enabled": bool,
        "HasCredential": bool,
        "HasTokenKey": bool,
        "Id": str,
        "IsArchived": bool,
        "LastModifiedBy": str,
        "LastModifiedDate": str,
        "Version": int,
    },
    total=False,
)

class APNSVoipSandboxChannelResponseTypeDef(
    _RequiredAPNSVoipSandboxChannelResponseTypeDef, _OptionalAPNSVoipSandboxChannelResponseTypeDef
):
    pass

_RequiredActivitiesResponseTypeDef = TypedDict(
    "_RequiredActivitiesResponseTypeDef",
    {
        "Item": List["ActivityResponseTypeDef"],
    },
)
_OptionalActivitiesResponseTypeDef = TypedDict(
    "_OptionalActivitiesResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ActivitiesResponseTypeDef(
    _RequiredActivitiesResponseTypeDef, _OptionalActivitiesResponseTypeDef
):
    pass

_RequiredActivityResponseTypeDef = TypedDict(
    "_RequiredActivityResponseTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "Id": str,
    },
)
_OptionalActivityResponseTypeDef = TypedDict(
    "_OptionalActivityResponseTypeDef",
    {
        "End": str,
        "Result": str,
        "ScheduledStart": str,
        "Start": str,
        "State": str,
        "SuccessfulEndpointCount": int,
        "TimezonesCompletedCount": int,
        "TimezonesTotalCount": int,
        "TotalEndpointCount": int,
        "TreatmentId": str,
    },
    total=False,
)

class ActivityResponseTypeDef(_RequiredActivityResponseTypeDef, _OptionalActivityResponseTypeDef):
    pass

ActivityTypeDef = TypedDict(
    "ActivityTypeDef",
    {
        "CUSTOM": "CustomMessageActivityTypeDef",
        "ConditionalSplit": "ConditionalSplitActivityTypeDef",
        "Description": str,
        "EMAIL": "EmailMessageActivityTypeDef",
        "Holdout": "HoldoutActivityTypeDef",
        "MultiCondition": "MultiConditionalSplitActivityTypeDef",
        "PUSH": "PushMessageActivityTypeDef",
        "RandomSplit": "RandomSplitActivityTypeDef",
        "SMS": "SMSMessageActivityTypeDef",
        "Wait": "WaitActivityTypeDef",
    },
    total=False,
)

AddressConfigurationTypeDef = TypedDict(
    "AddressConfigurationTypeDef",
    {
        "BodyOverride": str,
        "ChannelType": ChannelTypeType,
        "Context": Dict[str, str],
        "RawContent": str,
        "Substitutions": Dict[str, List[str]],
        "TitleOverride": str,
    },
    total=False,
)

AndroidPushNotificationTemplateTypeDef = TypedDict(
    "AndroidPushNotificationTemplateTypeDef",
    {
        "Action": ActionType,
        "Body": str,
        "ImageIconUrl": str,
        "ImageUrl": str,
        "RawContent": str,
        "SmallImageIconUrl": str,
        "Sound": str,
        "Title": str,
        "Url": str,
    },
    total=False,
)

_RequiredApplicationDateRangeKpiResponseTypeDef = TypedDict(
    "_RequiredApplicationDateRangeKpiResponseTypeDef",
    {
        "ApplicationId": str,
        "EndTime": datetime,
        "KpiName": str,
        "KpiResult": "BaseKpiResultTypeDef",
        "StartTime": datetime,
    },
)
_OptionalApplicationDateRangeKpiResponseTypeDef = TypedDict(
    "_OptionalApplicationDateRangeKpiResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ApplicationDateRangeKpiResponseTypeDef(
    _RequiredApplicationDateRangeKpiResponseTypeDef, _OptionalApplicationDateRangeKpiResponseTypeDef
):
    pass

_RequiredApplicationResponseTypeDef = TypedDict(
    "_RequiredApplicationResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
    },
)
_OptionalApplicationResponseTypeDef = TypedDict(
    "_OptionalApplicationResponseTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class ApplicationResponseTypeDef(
    _RequiredApplicationResponseTypeDef, _OptionalApplicationResponseTypeDef
):
    pass

_RequiredApplicationSettingsResourceTypeDef = TypedDict(
    "_RequiredApplicationSettingsResourceTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalApplicationSettingsResourceTypeDef = TypedDict(
    "_OptionalApplicationSettingsResourceTypeDef",
    {
        "CampaignHook": "CampaignHookTypeDef",
        "LastModifiedDate": str,
        "Limits": "CampaignLimitsTypeDef",
        "QuietTime": "QuietTimeTypeDef",
    },
    total=False,
)

class ApplicationSettingsResourceTypeDef(
    _RequiredApplicationSettingsResourceTypeDef, _OptionalApplicationSettingsResourceTypeDef
):
    pass

ApplicationsResponseTypeDef = TypedDict(
    "ApplicationsResponseTypeDef",
    {
        "Item": List["ApplicationResponseTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredAttributeDimensionTypeDef = TypedDict(
    "_RequiredAttributeDimensionTypeDef",
    {
        "Values": List[str],
    },
)
_OptionalAttributeDimensionTypeDef = TypedDict(
    "_OptionalAttributeDimensionTypeDef",
    {
        "AttributeType": AttributeTypeType,
    },
    total=False,
)

class AttributeDimensionTypeDef(
    _RequiredAttributeDimensionTypeDef, _OptionalAttributeDimensionTypeDef
):
    pass

_RequiredAttributesResourceTypeDef = TypedDict(
    "_RequiredAttributesResourceTypeDef",
    {
        "ApplicationId": str,
        "AttributeType": str,
    },
)
_OptionalAttributesResourceTypeDef = TypedDict(
    "_OptionalAttributesResourceTypeDef",
    {
        "Attributes": List[str],
    },
    total=False,
)

class AttributesResourceTypeDef(
    _RequiredAttributesResourceTypeDef, _OptionalAttributesResourceTypeDef
):
    pass

_RequiredBaiduChannelRequestTypeDef = TypedDict(
    "_RequiredBaiduChannelRequestTypeDef",
    {
        "ApiKey": str,
        "SecretKey": str,
    },
)
_OptionalBaiduChannelRequestTypeDef = TypedDict(
    "_OptionalBaiduChannelRequestTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

class BaiduChannelRequestTypeDef(
    _RequiredBaiduChannelRequestTypeDef, _OptionalBaiduChannelRequestTypeDef
):
    pass

_RequiredBaiduChannelResponseTypeDef = TypedDict(
    "_RequiredBaiduChannelResponseTypeDef",
    {
        "Credential": str,
        "Platform": str,
    },
)
_OptionalBaiduChannelResponseTypeDef = TypedDict(
    "_OptionalBaiduChannelResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "Enabled": bool,
        "HasCredential": bool,
        "Id": str,
        "IsArchived": bool,
        "LastModifiedBy": str,
        "LastModifiedDate": str,
        "Version": int,
    },
    total=False,
)

class BaiduChannelResponseTypeDef(
    _RequiredBaiduChannelResponseTypeDef, _OptionalBaiduChannelResponseTypeDef
):
    pass

BaiduMessageTypeDef = TypedDict(
    "BaiduMessageTypeDef",
    {
        "Action": ActionType,
        "Body": str,
        "Data": Dict[str, str],
        "IconReference": str,
        "ImageIconUrl": str,
        "ImageUrl": str,
        "RawContent": str,
        "SilentPush": bool,
        "SmallImageIconUrl": str,
        "Sound": str,
        "Substitutions": Dict[str, List[str]],
        "TimeToLive": int,
        "Title": str,
        "Url": str,
    },
    total=False,
)

BaseKpiResultTypeDef = TypedDict(
    "BaseKpiResultTypeDef",
    {
        "Rows": List["ResultRowTypeDef"],
    },
)

CampaignCustomMessageTypeDef = TypedDict(
    "CampaignCustomMessageTypeDef",
    {
        "Data": str,
    },
    total=False,
)

_RequiredCampaignDateRangeKpiResponseTypeDef = TypedDict(
    "_RequiredCampaignDateRangeKpiResponseTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "EndTime": datetime,
        "KpiName": str,
        "KpiResult": "BaseKpiResultTypeDef",
        "StartTime": datetime,
    },
)
_OptionalCampaignDateRangeKpiResponseTypeDef = TypedDict(
    "_OptionalCampaignDateRangeKpiResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class CampaignDateRangeKpiResponseTypeDef(
    _RequiredCampaignDateRangeKpiResponseTypeDef, _OptionalCampaignDateRangeKpiResponseTypeDef
):
    pass

CampaignEmailMessageTypeDef = TypedDict(
    "CampaignEmailMessageTypeDef",
    {
        "Body": str,
        "FromAddress": str,
        "HtmlBody": str,
        "Title": str,
    },
    total=False,
)

CampaignEventFilterTypeDef = TypedDict(
    "CampaignEventFilterTypeDef",
    {
        "Dimensions": "EventDimensionsTypeDef",
        "FilterType": FilterTypeType,
    },
)

CampaignHookTypeDef = TypedDict(
    "CampaignHookTypeDef",
    {
        "LambdaFunctionName": str,
        "Mode": ModeType,
        "WebUrl": str,
    },
    total=False,
)

CampaignLimitsTypeDef = TypedDict(
    "CampaignLimitsTypeDef",
    {
        "Daily": int,
        "MaximumDuration": int,
        "MessagesPerSecond": int,
        "Total": int,
    },
    total=False,
)

_RequiredCampaignResponseTypeDef = TypedDict(
    "_RequiredCampaignResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "CreationDate": str,
        "Id": str,
        "LastModifiedDate": str,
        "SegmentId": str,
        "SegmentVersion": int,
    },
)
_OptionalCampaignResponseTypeDef = TypedDict(
    "_OptionalCampaignResponseTypeDef",
    {
        "AdditionalTreatments": List["TreatmentResourceTypeDef"],
        "CustomDeliveryConfiguration": "CustomDeliveryConfigurationTypeDef",
        "DefaultState": "CampaignStateTypeDef",
        "Description": str,
        "HoldoutPercent": int,
        "Hook": "CampaignHookTypeDef",
        "IsPaused": bool,
        "Limits": "CampaignLimitsTypeDef",
        "MessageConfiguration": "MessageConfigurationTypeDef",
        "Name": str,
        "Schedule": "ScheduleTypeDef",
        "State": "CampaignStateTypeDef",
        "tags": Dict[str, str],
        "TemplateConfiguration": "TemplateConfigurationTypeDef",
        "TreatmentDescription": str,
        "TreatmentName": str,
        "Version": int,
    },
    total=False,
)

class CampaignResponseTypeDef(_RequiredCampaignResponseTypeDef, _OptionalCampaignResponseTypeDef):
    pass

CampaignSmsMessageTypeDef = TypedDict(
    "CampaignSmsMessageTypeDef",
    {
        "Body": str,
        "MessageType": MessageTypeType,
        "OriginationNumber": str,
        "SenderId": str,
        "EntityId": str,
        "TemplateId": str,
    },
    total=False,
)

CampaignStateTypeDef = TypedDict(
    "CampaignStateTypeDef",
    {
        "CampaignStatus": CampaignStatusType,
    },
    total=False,
)

_RequiredCampaignsResponseTypeDef = TypedDict(
    "_RequiredCampaignsResponseTypeDef",
    {
        "Item": List["CampaignResponseTypeDef"],
    },
)
_OptionalCampaignsResponseTypeDef = TypedDict(
    "_OptionalCampaignsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class CampaignsResponseTypeDef(
    _RequiredCampaignsResponseTypeDef, _OptionalCampaignsResponseTypeDef
):
    pass

ChannelResponseTypeDef = TypedDict(
    "ChannelResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "Enabled": bool,
        "HasCredential": bool,
        "Id": str,
        "IsArchived": bool,
        "LastModifiedBy": str,
        "LastModifiedDate": str,
        "Version": int,
    },
    total=False,
)

ChannelsResponseTypeDef = TypedDict(
    "ChannelsResponseTypeDef",
    {
        "Channels": Dict[str, "ChannelResponseTypeDef"],
    },
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "Conditions": List["SimpleConditionTypeDef"],
        "Operator": OperatorType,
    },
    total=False,
)

ConditionalSplitActivityTypeDef = TypedDict(
    "ConditionalSplitActivityTypeDef",
    {
        "Condition": "ConditionTypeDef",
        "EvaluationWaitTime": "WaitTimeTypeDef",
        "FalseActivity": str,
        "TrueActivity": str,
    },
    total=False,
)

CreateAppRequestRequestTypeDef = TypedDict(
    "CreateAppRequestRequestTypeDef",
    {
        "CreateApplicationRequest": "CreateApplicationRequestTypeDef",
    },
)

CreateAppResponseTypeDef = TypedDict(
    "CreateAppResponseTypeDef",
    {
        "ApplicationResponse": "ApplicationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateApplicationRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateApplicationRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateApplicationRequestTypeDef(
    _RequiredCreateApplicationRequestTypeDef, _OptionalCreateApplicationRequestTypeDef
):
    pass

CreateCampaignRequestRequestTypeDef = TypedDict(
    "CreateCampaignRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "WriteCampaignRequest": "WriteCampaignRequestTypeDef",
    },
)

CreateCampaignResponseTypeDef = TypedDict(
    "CreateCampaignResponseTypeDef",
    {
        "CampaignResponse": "CampaignResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEmailTemplateRequestRequestTypeDef = TypedDict(
    "CreateEmailTemplateRequestRequestTypeDef",
    {
        "EmailTemplateRequest": "EmailTemplateRequestTypeDef",
        "TemplateName": str,
    },
)

CreateEmailTemplateResponseTypeDef = TypedDict(
    "CreateEmailTemplateResponseTypeDef",
    {
        "CreateTemplateMessageBody": "CreateTemplateMessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateExportJobRequestRequestTypeDef = TypedDict(
    "CreateExportJobRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ExportJobRequest": "ExportJobRequestTypeDef",
    },
)

CreateExportJobResponseTypeDef = TypedDict(
    "CreateExportJobResponseTypeDef",
    {
        "ExportJobResponse": "ExportJobResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateImportJobRequestRequestTypeDef = TypedDict(
    "CreateImportJobRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ImportJobRequest": "ImportJobRequestTypeDef",
    },
)

CreateImportJobResponseTypeDef = TypedDict(
    "CreateImportJobResponseTypeDef",
    {
        "ImportJobResponse": "ImportJobResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateJourneyRequestRequestTypeDef = TypedDict(
    "CreateJourneyRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "WriteJourneyRequest": "WriteJourneyRequestTypeDef",
    },
)

CreateJourneyResponseTypeDef = TypedDict(
    "CreateJourneyResponseTypeDef",
    {
        "JourneyResponse": "JourneyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePushTemplateRequestRequestTypeDef = TypedDict(
    "CreatePushTemplateRequestRequestTypeDef",
    {
        "PushNotificationTemplateRequest": "PushNotificationTemplateRequestTypeDef",
        "TemplateName": str,
    },
)

CreatePushTemplateResponseTypeDef = TypedDict(
    "CreatePushTemplateResponseTypeDef",
    {
        "CreateTemplateMessageBody": "CreateTemplateMessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRecommenderConfigurationRequestRequestTypeDef = TypedDict(
    "CreateRecommenderConfigurationRequestRequestTypeDef",
    {
        "CreateRecommenderConfiguration": "CreateRecommenderConfigurationTypeDef",
    },
)

CreateRecommenderConfigurationResponseTypeDef = TypedDict(
    "CreateRecommenderConfigurationResponseTypeDef",
    {
        "RecommenderConfigurationResponse": "RecommenderConfigurationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRecommenderConfigurationTypeDef = TypedDict(
    "_RequiredCreateRecommenderConfigurationTypeDef",
    {
        "RecommendationProviderRoleArn": str,
        "RecommendationProviderUri": str,
    },
)
_OptionalCreateRecommenderConfigurationTypeDef = TypedDict(
    "_OptionalCreateRecommenderConfigurationTypeDef",
    {
        "Attributes": Dict[str, str],
        "Description": str,
        "Name": str,
        "RecommendationProviderIdType": str,
        "RecommendationTransformerUri": str,
        "RecommendationsDisplayName": str,
        "RecommendationsPerMessage": int,
    },
    total=False,
)

class CreateRecommenderConfigurationTypeDef(
    _RequiredCreateRecommenderConfigurationTypeDef, _OptionalCreateRecommenderConfigurationTypeDef
):
    pass

CreateSegmentRequestRequestTypeDef = TypedDict(
    "CreateSegmentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "WriteSegmentRequest": "WriteSegmentRequestTypeDef",
    },
)

CreateSegmentResponseTypeDef = TypedDict(
    "CreateSegmentResponseTypeDef",
    {
        "SegmentResponse": "SegmentResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSmsTemplateRequestRequestTypeDef = TypedDict(
    "CreateSmsTemplateRequestRequestTypeDef",
    {
        "SMSTemplateRequest": "SMSTemplateRequestTypeDef",
        "TemplateName": str,
    },
)

CreateSmsTemplateResponseTypeDef = TypedDict(
    "CreateSmsTemplateResponseTypeDef",
    {
        "CreateTemplateMessageBody": "CreateTemplateMessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTemplateMessageBodyTypeDef = TypedDict(
    "CreateTemplateMessageBodyTypeDef",
    {
        "Arn": str,
        "Message": str,
        "RequestID": str,
    },
    total=False,
)

CreateVoiceTemplateRequestRequestTypeDef = TypedDict(
    "CreateVoiceTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "VoiceTemplateRequest": "VoiceTemplateRequestTypeDef",
    },
)

CreateVoiceTemplateResponseTypeDef = TypedDict(
    "CreateVoiceTemplateResponseTypeDef",
    {
        "CreateTemplateMessageBody": "CreateTemplateMessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCustomDeliveryConfigurationTypeDef = TypedDict(
    "_RequiredCustomDeliveryConfigurationTypeDef",
    {
        "DeliveryUri": str,
    },
)
_OptionalCustomDeliveryConfigurationTypeDef = TypedDict(
    "_OptionalCustomDeliveryConfigurationTypeDef",
    {
        "EndpointTypes": List[__EndpointTypesElementType],
    },
    total=False,
)

class CustomDeliveryConfigurationTypeDef(
    _RequiredCustomDeliveryConfigurationTypeDef, _OptionalCustomDeliveryConfigurationTypeDef
):
    pass

CustomMessageActivityTypeDef = TypedDict(
    "CustomMessageActivityTypeDef",
    {
        "DeliveryUri": str,
        "EndpointTypes": List[__EndpointTypesElementType],
        "MessageConfig": "JourneyCustomMessageTypeDef",
        "NextActivity": str,
        "TemplateName": str,
        "TemplateVersion": str,
    },
    total=False,
)

DefaultMessageTypeDef = TypedDict(
    "DefaultMessageTypeDef",
    {
        "Body": str,
        "Substitutions": Dict[str, List[str]],
    },
    total=False,
)

DefaultPushNotificationMessageTypeDef = TypedDict(
    "DefaultPushNotificationMessageTypeDef",
    {
        "Action": ActionType,
        "Body": str,
        "Data": Dict[str, str],
        "SilentPush": bool,
        "Substitutions": Dict[str, List[str]],
        "Title": str,
        "Url": str,
    },
    total=False,
)

DefaultPushNotificationTemplateTypeDef = TypedDict(
    "DefaultPushNotificationTemplateTypeDef",
    {
        "Action": ActionType,
        "Body": str,
        "Sound": str,
        "Title": str,
        "Url": str,
    },
    total=False,
)

DeleteAdmChannelRequestRequestTypeDef = TypedDict(
    "DeleteAdmChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteAdmChannelResponseTypeDef = TypedDict(
    "DeleteAdmChannelResponseTypeDef",
    {
        "ADMChannelResponse": "ADMChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApnsChannelRequestRequestTypeDef = TypedDict(
    "DeleteApnsChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteApnsChannelResponseTypeDef = TypedDict(
    "DeleteApnsChannelResponseTypeDef",
    {
        "APNSChannelResponse": "APNSChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApnsSandboxChannelRequestRequestTypeDef = TypedDict(
    "DeleteApnsSandboxChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteApnsSandboxChannelResponseTypeDef = TypedDict(
    "DeleteApnsSandboxChannelResponseTypeDef",
    {
        "APNSSandboxChannelResponse": "APNSSandboxChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApnsVoipChannelRequestRequestTypeDef = TypedDict(
    "DeleteApnsVoipChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteApnsVoipChannelResponseTypeDef = TypedDict(
    "DeleteApnsVoipChannelResponseTypeDef",
    {
        "APNSVoipChannelResponse": "APNSVoipChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApnsVoipSandboxChannelRequestRequestTypeDef = TypedDict(
    "DeleteApnsVoipSandboxChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteApnsVoipSandboxChannelResponseTypeDef = TypedDict(
    "DeleteApnsVoipSandboxChannelResponseTypeDef",
    {
        "APNSVoipSandboxChannelResponse": "APNSVoipSandboxChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAppRequestRequestTypeDef = TypedDict(
    "DeleteAppRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteAppResponseTypeDef = TypedDict(
    "DeleteAppResponseTypeDef",
    {
        "ApplicationResponse": "ApplicationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBaiduChannelRequestRequestTypeDef = TypedDict(
    "DeleteBaiduChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteBaiduChannelResponseTypeDef = TypedDict(
    "DeleteBaiduChannelResponseTypeDef",
    {
        "BaiduChannelResponse": "BaiduChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCampaignRequestRequestTypeDef = TypedDict(
    "DeleteCampaignRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
    },
)

DeleteCampaignResponseTypeDef = TypedDict(
    "DeleteCampaignResponseTypeDef",
    {
        "CampaignResponse": "CampaignResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEmailChannelRequestRequestTypeDef = TypedDict(
    "DeleteEmailChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteEmailChannelResponseTypeDef = TypedDict(
    "DeleteEmailChannelResponseTypeDef",
    {
        "EmailChannelResponse": "EmailChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteEmailTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)
_OptionalDeleteEmailTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteEmailTemplateRequestRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)

class DeleteEmailTemplateRequestRequestTypeDef(
    _RequiredDeleteEmailTemplateRequestRequestTypeDef,
    _OptionalDeleteEmailTemplateRequestRequestTypeDef,
):
    pass

DeleteEmailTemplateResponseTypeDef = TypedDict(
    "DeleteEmailTemplateResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEndpointRequestRequestTypeDef = TypedDict(
    "DeleteEndpointRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EndpointId": str,
    },
)

DeleteEndpointResponseTypeDef = TypedDict(
    "DeleteEndpointResponseTypeDef",
    {
        "EndpointResponse": "EndpointResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEventStreamRequestRequestTypeDef = TypedDict(
    "DeleteEventStreamRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteEventStreamResponseTypeDef = TypedDict(
    "DeleteEventStreamResponseTypeDef",
    {
        "EventStream": "EventStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGcmChannelRequestRequestTypeDef = TypedDict(
    "DeleteGcmChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteGcmChannelResponseTypeDef = TypedDict(
    "DeleteGcmChannelResponseTypeDef",
    {
        "GCMChannelResponse": "GCMChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteJourneyRequestRequestTypeDef = TypedDict(
    "DeleteJourneyRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
    },
)

DeleteJourneyResponseTypeDef = TypedDict(
    "DeleteJourneyResponseTypeDef",
    {
        "JourneyResponse": "JourneyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeletePushTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePushTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)
_OptionalDeletePushTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePushTemplateRequestRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)

class DeletePushTemplateRequestRequestTypeDef(
    _RequiredDeletePushTemplateRequestRequestTypeDef,
    _OptionalDeletePushTemplateRequestRequestTypeDef,
):
    pass

DeletePushTemplateResponseTypeDef = TypedDict(
    "DeletePushTemplateResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRecommenderConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteRecommenderConfigurationRequestRequestTypeDef",
    {
        "RecommenderId": str,
    },
)

DeleteRecommenderConfigurationResponseTypeDef = TypedDict(
    "DeleteRecommenderConfigurationResponseTypeDef",
    {
        "RecommenderConfigurationResponse": "RecommenderConfigurationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSegmentRequestRequestTypeDef = TypedDict(
    "DeleteSegmentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
    },
)

DeleteSegmentResponseTypeDef = TypedDict(
    "DeleteSegmentResponseTypeDef",
    {
        "SegmentResponse": "SegmentResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSmsChannelRequestRequestTypeDef = TypedDict(
    "DeleteSmsChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteSmsChannelResponseTypeDef = TypedDict(
    "DeleteSmsChannelResponseTypeDef",
    {
        "SMSChannelResponse": "SMSChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteSmsTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteSmsTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)
_OptionalDeleteSmsTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteSmsTemplateRequestRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)

class DeleteSmsTemplateRequestRequestTypeDef(
    _RequiredDeleteSmsTemplateRequestRequestTypeDef, _OptionalDeleteSmsTemplateRequestRequestTypeDef
):
    pass

DeleteSmsTemplateResponseTypeDef = TypedDict(
    "DeleteSmsTemplateResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteUserEndpointsRequestRequestTypeDef = TypedDict(
    "DeleteUserEndpointsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "UserId": str,
    },
)

DeleteUserEndpointsResponseTypeDef = TypedDict(
    "DeleteUserEndpointsResponseTypeDef",
    {
        "EndpointsResponse": "EndpointsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVoiceChannelRequestRequestTypeDef = TypedDict(
    "DeleteVoiceChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteVoiceChannelResponseTypeDef = TypedDict(
    "DeleteVoiceChannelResponseTypeDef",
    {
        "VoiceChannelResponse": "VoiceChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVoiceTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteVoiceTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)
_OptionalDeleteVoiceTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteVoiceTemplateRequestRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)

class DeleteVoiceTemplateRequestRequestTypeDef(
    _RequiredDeleteVoiceTemplateRequestRequestTypeDef,
    _OptionalDeleteVoiceTemplateRequestRequestTypeDef,
):
    pass

DeleteVoiceTemplateResponseTypeDef = TypedDict(
    "DeleteVoiceTemplateResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DirectMessageConfigurationTypeDef = TypedDict(
    "DirectMessageConfigurationTypeDef",
    {
        "ADMMessage": "ADMMessageTypeDef",
        "APNSMessage": "APNSMessageTypeDef",
        "BaiduMessage": "BaiduMessageTypeDef",
        "DefaultMessage": "DefaultMessageTypeDef",
        "DefaultPushNotificationMessage": "DefaultPushNotificationMessageTypeDef",
        "EmailMessage": "EmailMessageTypeDef",
        "GCMMessage": "GCMMessageTypeDef",
        "SMSMessage": "SMSMessageTypeDef",
        "VoiceMessage": "VoiceMessageTypeDef",
    },
    total=False,
)

_RequiredEmailChannelRequestTypeDef = TypedDict(
    "_RequiredEmailChannelRequestTypeDef",
    {
        "FromAddress": str,
        "Identity": str,
    },
)
_OptionalEmailChannelRequestTypeDef = TypedDict(
    "_OptionalEmailChannelRequestTypeDef",
    {
        "ConfigurationSet": str,
        "Enabled": bool,
        "RoleArn": str,
    },
    total=False,
)

class EmailChannelRequestTypeDef(
    _RequiredEmailChannelRequestTypeDef, _OptionalEmailChannelRequestTypeDef
):
    pass

_RequiredEmailChannelResponseTypeDef = TypedDict(
    "_RequiredEmailChannelResponseTypeDef",
    {
        "Platform": str,
    },
)
_OptionalEmailChannelResponseTypeDef = TypedDict(
    "_OptionalEmailChannelResponseTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationSet": str,
        "CreationDate": str,
        "Enabled": bool,
        "FromAddress": str,
        "HasCredential": bool,
        "Id": str,
        "Identity": str,
        "IsArchived": bool,
        "LastModifiedBy": str,
        "LastModifiedDate": str,
        "MessagesPerSecond": int,
        "RoleArn": str,
        "Version": int,
    },
    total=False,
)

class EmailChannelResponseTypeDef(
    _RequiredEmailChannelResponseTypeDef, _OptionalEmailChannelResponseTypeDef
):
    pass

EmailMessageActivityTypeDef = TypedDict(
    "EmailMessageActivityTypeDef",
    {
        "MessageConfig": "JourneyEmailMessageTypeDef",
        "NextActivity": str,
        "TemplateName": str,
        "TemplateVersion": str,
    },
    total=False,
)

EmailMessageTypeDef = TypedDict(
    "EmailMessageTypeDef",
    {
        "Body": str,
        "FeedbackForwardingAddress": str,
        "FromAddress": str,
        "RawEmail": "RawEmailTypeDef",
        "ReplyToAddresses": List[str],
        "SimpleEmail": "SimpleEmailTypeDef",
        "Substitutions": Dict[str, List[str]],
    },
    total=False,
)

EmailTemplateRequestTypeDef = TypedDict(
    "EmailTemplateRequestTypeDef",
    {
        "DefaultSubstitutions": str,
        "HtmlPart": str,
        "RecommenderId": str,
        "Subject": str,
        "tags": Dict[str, str],
        "TemplateDescription": str,
        "TextPart": str,
    },
    total=False,
)

_RequiredEmailTemplateResponseTypeDef = TypedDict(
    "_RequiredEmailTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": TemplateTypeType,
    },
)
_OptionalEmailTemplateResponseTypeDef = TypedDict(
    "_OptionalEmailTemplateResponseTypeDef",
    {
        "Arn": str,
        "DefaultSubstitutions": str,
        "HtmlPart": str,
        "RecommenderId": str,
        "Subject": str,
        "tags": Dict[str, str],
        "TemplateDescription": str,
        "TextPart": str,
        "Version": str,
    },
    total=False,
)

class EmailTemplateResponseTypeDef(
    _RequiredEmailTemplateResponseTypeDef, _OptionalEmailTemplateResponseTypeDef
):
    pass

EndpointBatchItemTypeDef = TypedDict(
    "EndpointBatchItemTypeDef",
    {
        "Address": str,
        "Attributes": Dict[str, List[str]],
        "ChannelType": ChannelTypeType,
        "Demographic": "EndpointDemographicTypeDef",
        "EffectiveDate": str,
        "EndpointStatus": str,
        "Id": str,
        "Location": "EndpointLocationTypeDef",
        "Metrics": Dict[str, float],
        "OptOut": str,
        "RequestId": str,
        "User": "EndpointUserTypeDef",
    },
    total=False,
)

EndpointBatchRequestTypeDef = TypedDict(
    "EndpointBatchRequestTypeDef",
    {
        "Item": List["EndpointBatchItemTypeDef"],
    },
)

EndpointDemographicTypeDef = TypedDict(
    "EndpointDemographicTypeDef",
    {
        "AppVersion": str,
        "Locale": str,
        "Make": str,
        "Model": str,
        "ModelVersion": str,
        "Platform": str,
        "PlatformVersion": str,
        "Timezone": str,
    },
    total=False,
)

EndpointItemResponseTypeDef = TypedDict(
    "EndpointItemResponseTypeDef",
    {
        "Message": str,
        "StatusCode": int,
    },
    total=False,
)

EndpointLocationTypeDef = TypedDict(
    "EndpointLocationTypeDef",
    {
        "City": str,
        "Country": str,
        "Latitude": float,
        "Longitude": float,
        "PostalCode": str,
        "Region": str,
    },
    total=False,
)

_RequiredEndpointMessageResultTypeDef = TypedDict(
    "_RequiredEndpointMessageResultTypeDef",
    {
        "DeliveryStatus": DeliveryStatusType,
        "StatusCode": int,
    },
)
_OptionalEndpointMessageResultTypeDef = TypedDict(
    "_OptionalEndpointMessageResultTypeDef",
    {
        "Address": str,
        "MessageId": str,
        "StatusMessage": str,
        "UpdatedToken": str,
    },
    total=False,
)

class EndpointMessageResultTypeDef(
    _RequiredEndpointMessageResultTypeDef, _OptionalEndpointMessageResultTypeDef
):
    pass

EndpointRequestTypeDef = TypedDict(
    "EndpointRequestTypeDef",
    {
        "Address": str,
        "Attributes": Dict[str, List[str]],
        "ChannelType": ChannelTypeType,
        "Demographic": "EndpointDemographicTypeDef",
        "EffectiveDate": str,
        "EndpointStatus": str,
        "Location": "EndpointLocationTypeDef",
        "Metrics": Dict[str, float],
        "OptOut": str,
        "RequestId": str,
        "User": "EndpointUserTypeDef",
    },
    total=False,
)

EndpointResponseTypeDef = TypedDict(
    "EndpointResponseTypeDef",
    {
        "Address": str,
        "ApplicationId": str,
        "Attributes": Dict[str, List[str]],
        "ChannelType": ChannelTypeType,
        "CohortId": str,
        "CreationDate": str,
        "Demographic": "EndpointDemographicTypeDef",
        "EffectiveDate": str,
        "EndpointStatus": str,
        "Id": str,
        "Location": "EndpointLocationTypeDef",
        "Metrics": Dict[str, float],
        "OptOut": str,
        "RequestId": str,
        "User": "EndpointUserTypeDef",
    },
    total=False,
)

EndpointSendConfigurationTypeDef = TypedDict(
    "EndpointSendConfigurationTypeDef",
    {
        "BodyOverride": str,
        "Context": Dict[str, str],
        "RawContent": str,
        "Substitutions": Dict[str, List[str]],
        "TitleOverride": str,
    },
    total=False,
)

EndpointUserTypeDef = TypedDict(
    "EndpointUserTypeDef",
    {
        "UserAttributes": Dict[str, List[str]],
        "UserId": str,
    },
    total=False,
)

EndpointsResponseTypeDef = TypedDict(
    "EndpointsResponseTypeDef",
    {
        "Item": List["EndpointResponseTypeDef"],
    },
)

EventConditionTypeDef = TypedDict(
    "EventConditionTypeDef",
    {
        "Dimensions": "EventDimensionsTypeDef",
        "MessageActivity": str,
    },
    total=False,
)

EventDimensionsTypeDef = TypedDict(
    "EventDimensionsTypeDef",
    {
        "Attributes": Dict[str, "AttributeDimensionTypeDef"],
        "EventType": "SetDimensionTypeDef",
        "Metrics": Dict[str, "MetricDimensionTypeDef"],
    },
    total=False,
)

EventFilterTypeDef = TypedDict(
    "EventFilterTypeDef",
    {
        "Dimensions": "EventDimensionsTypeDef",
        "FilterType": FilterTypeType,
    },
)

EventItemResponseTypeDef = TypedDict(
    "EventItemResponseTypeDef",
    {
        "Message": str,
        "StatusCode": int,
    },
    total=False,
)

EventStartConditionTypeDef = TypedDict(
    "EventStartConditionTypeDef",
    {
        "EventFilter": "EventFilterTypeDef",
        "SegmentId": str,
    },
    total=False,
)

_RequiredEventStreamTypeDef = TypedDict(
    "_RequiredEventStreamTypeDef",
    {
        "ApplicationId": str,
        "DestinationStreamArn": str,
        "RoleArn": str,
    },
)
_OptionalEventStreamTypeDef = TypedDict(
    "_OptionalEventStreamTypeDef",
    {
        "ExternalId": str,
        "LastModifiedDate": str,
        "LastUpdatedBy": str,
    },
    total=False,
)

class EventStreamTypeDef(_RequiredEventStreamTypeDef, _OptionalEventStreamTypeDef):
    pass

_RequiredEventTypeDef = TypedDict(
    "_RequiredEventTypeDef",
    {
        "EventType": str,
        "Timestamp": str,
    },
)
_OptionalEventTypeDef = TypedDict(
    "_OptionalEventTypeDef",
    {
        "AppPackageName": str,
        "AppTitle": str,
        "AppVersionCode": str,
        "Attributes": Dict[str, str],
        "ClientSdkVersion": str,
        "Metrics": Dict[str, float],
        "SdkName": str,
        "Session": "SessionTypeDef",
    },
    total=False,
)

class EventTypeDef(_RequiredEventTypeDef, _OptionalEventTypeDef):
    pass

EventsBatchTypeDef = TypedDict(
    "EventsBatchTypeDef",
    {
        "Endpoint": "PublicEndpointTypeDef",
        "Events": Dict[str, "EventTypeDef"],
    },
)

EventsRequestTypeDef = TypedDict(
    "EventsRequestTypeDef",
    {
        "BatchItem": Dict[str, "EventsBatchTypeDef"],
    },
)

EventsResponseTypeDef = TypedDict(
    "EventsResponseTypeDef",
    {
        "Results": Dict[str, "ItemResponseTypeDef"],
    },
    total=False,
)

_RequiredExportJobRequestTypeDef = TypedDict(
    "_RequiredExportJobRequestTypeDef",
    {
        "RoleArn": str,
        "S3UrlPrefix": str,
    },
)
_OptionalExportJobRequestTypeDef = TypedDict(
    "_OptionalExportJobRequestTypeDef",
    {
        "SegmentId": str,
        "SegmentVersion": int,
    },
    total=False,
)

class ExportJobRequestTypeDef(_RequiredExportJobRequestTypeDef, _OptionalExportJobRequestTypeDef):
    pass

_RequiredExportJobResourceTypeDef = TypedDict(
    "_RequiredExportJobResourceTypeDef",
    {
        "RoleArn": str,
        "S3UrlPrefix": str,
    },
)
_OptionalExportJobResourceTypeDef = TypedDict(
    "_OptionalExportJobResourceTypeDef",
    {
        "SegmentId": str,
        "SegmentVersion": int,
    },
    total=False,
)

class ExportJobResourceTypeDef(
    _RequiredExportJobResourceTypeDef, _OptionalExportJobResourceTypeDef
):
    pass

_RequiredExportJobResponseTypeDef = TypedDict(
    "_RequiredExportJobResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "Definition": "ExportJobResourceTypeDef",
        "Id": str,
        "JobStatus": JobStatusType,
        "Type": str,
    },
)
_OptionalExportJobResponseTypeDef = TypedDict(
    "_OptionalExportJobResponseTypeDef",
    {
        "CompletedPieces": int,
        "CompletionDate": str,
        "FailedPieces": int,
        "Failures": List[str],
        "TotalFailures": int,
        "TotalPieces": int,
        "TotalProcessed": int,
    },
    total=False,
)

class ExportJobResponseTypeDef(
    _RequiredExportJobResponseTypeDef, _OptionalExportJobResponseTypeDef
):
    pass

_RequiredExportJobsResponseTypeDef = TypedDict(
    "_RequiredExportJobsResponseTypeDef",
    {
        "Item": List["ExportJobResponseTypeDef"],
    },
)
_OptionalExportJobsResponseTypeDef = TypedDict(
    "_OptionalExportJobsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ExportJobsResponseTypeDef(
    _RequiredExportJobsResponseTypeDef, _OptionalExportJobsResponseTypeDef
):
    pass

_RequiredGCMChannelRequestTypeDef = TypedDict(
    "_RequiredGCMChannelRequestTypeDef",
    {
        "ApiKey": str,
    },
)
_OptionalGCMChannelRequestTypeDef = TypedDict(
    "_OptionalGCMChannelRequestTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

class GCMChannelRequestTypeDef(
    _RequiredGCMChannelRequestTypeDef, _OptionalGCMChannelRequestTypeDef
):
    pass

_RequiredGCMChannelResponseTypeDef = TypedDict(
    "_RequiredGCMChannelResponseTypeDef",
    {
        "Credential": str,
        "Platform": str,
    },
)
_OptionalGCMChannelResponseTypeDef = TypedDict(
    "_OptionalGCMChannelResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "Enabled": bool,
        "HasCredential": bool,
        "Id": str,
        "IsArchived": bool,
        "LastModifiedBy": str,
        "LastModifiedDate": str,
        "Version": int,
    },
    total=False,
)

class GCMChannelResponseTypeDef(
    _RequiredGCMChannelResponseTypeDef, _OptionalGCMChannelResponseTypeDef
):
    pass

GCMMessageTypeDef = TypedDict(
    "GCMMessageTypeDef",
    {
        "Action": ActionType,
        "Body": str,
        "CollapseKey": str,
        "Data": Dict[str, str],
        "IconReference": str,
        "ImageIconUrl": str,
        "ImageUrl": str,
        "Priority": str,
        "RawContent": str,
        "RestrictedPackageName": str,
        "SilentPush": bool,
        "SmallImageIconUrl": str,
        "Sound": str,
        "Substitutions": Dict[str, List[str]],
        "TimeToLive": int,
        "Title": str,
        "Url": str,
    },
    total=False,
)

GPSCoordinatesTypeDef = TypedDict(
    "GPSCoordinatesTypeDef",
    {
        "Latitude": float,
        "Longitude": float,
    },
)

_RequiredGPSPointDimensionTypeDef = TypedDict(
    "_RequiredGPSPointDimensionTypeDef",
    {
        "Coordinates": "GPSCoordinatesTypeDef",
    },
)
_OptionalGPSPointDimensionTypeDef = TypedDict(
    "_OptionalGPSPointDimensionTypeDef",
    {
        "RangeInKilometers": float,
    },
    total=False,
)

class GPSPointDimensionTypeDef(
    _RequiredGPSPointDimensionTypeDef, _OptionalGPSPointDimensionTypeDef
):
    pass

GetAdmChannelRequestRequestTypeDef = TypedDict(
    "GetAdmChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetAdmChannelResponseTypeDef = TypedDict(
    "GetAdmChannelResponseTypeDef",
    {
        "ADMChannelResponse": "ADMChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApnsChannelRequestRequestTypeDef = TypedDict(
    "GetApnsChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetApnsChannelResponseTypeDef = TypedDict(
    "GetApnsChannelResponseTypeDef",
    {
        "APNSChannelResponse": "APNSChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApnsSandboxChannelRequestRequestTypeDef = TypedDict(
    "GetApnsSandboxChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetApnsSandboxChannelResponseTypeDef = TypedDict(
    "GetApnsSandboxChannelResponseTypeDef",
    {
        "APNSSandboxChannelResponse": "APNSSandboxChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApnsVoipChannelRequestRequestTypeDef = TypedDict(
    "GetApnsVoipChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetApnsVoipChannelResponseTypeDef = TypedDict(
    "GetApnsVoipChannelResponseTypeDef",
    {
        "APNSVoipChannelResponse": "APNSVoipChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApnsVoipSandboxChannelRequestRequestTypeDef = TypedDict(
    "GetApnsVoipSandboxChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetApnsVoipSandboxChannelResponseTypeDef = TypedDict(
    "GetApnsVoipSandboxChannelResponseTypeDef",
    {
        "APNSVoipSandboxChannelResponse": "APNSVoipSandboxChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppRequestRequestTypeDef = TypedDict(
    "GetAppRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetAppResponseTypeDef = TypedDict(
    "GetAppResponseTypeDef",
    {
        "ApplicationResponse": "ApplicationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetApplicationDateRangeKpiRequestRequestTypeDef = TypedDict(
    "_RequiredGetApplicationDateRangeKpiRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "KpiName": str,
    },
)
_OptionalGetApplicationDateRangeKpiRequestRequestTypeDef = TypedDict(
    "_OptionalGetApplicationDateRangeKpiRequestRequestTypeDef",
    {
        "EndTime": Union[datetime, str],
        "NextToken": str,
        "PageSize": str,
        "StartTime": Union[datetime, str],
    },
    total=False,
)

class GetApplicationDateRangeKpiRequestRequestTypeDef(
    _RequiredGetApplicationDateRangeKpiRequestRequestTypeDef,
    _OptionalGetApplicationDateRangeKpiRequestRequestTypeDef,
):
    pass

GetApplicationDateRangeKpiResponseTypeDef = TypedDict(
    "GetApplicationDateRangeKpiResponseTypeDef",
    {
        "ApplicationDateRangeKpiResponse": "ApplicationDateRangeKpiResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApplicationSettingsRequestRequestTypeDef = TypedDict(
    "GetApplicationSettingsRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetApplicationSettingsResponseTypeDef = TypedDict(
    "GetApplicationSettingsResponseTypeDef",
    {
        "ApplicationSettingsResource": "ApplicationSettingsResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppsRequestRequestTypeDef = TypedDict(
    "GetAppsRequestRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)

GetAppsResponseTypeDef = TypedDict(
    "GetAppsResponseTypeDef",
    {
        "ApplicationsResponse": "ApplicationsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBaiduChannelRequestRequestTypeDef = TypedDict(
    "GetBaiduChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetBaiduChannelResponseTypeDef = TypedDict(
    "GetBaiduChannelResponseTypeDef",
    {
        "BaiduChannelResponse": "BaiduChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCampaignActivitiesRequestRequestTypeDef = TypedDict(
    "_RequiredGetCampaignActivitiesRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
    },
)
_OptionalGetCampaignActivitiesRequestRequestTypeDef = TypedDict(
    "_OptionalGetCampaignActivitiesRequestRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)

class GetCampaignActivitiesRequestRequestTypeDef(
    _RequiredGetCampaignActivitiesRequestRequestTypeDef,
    _OptionalGetCampaignActivitiesRequestRequestTypeDef,
):
    pass

GetCampaignActivitiesResponseTypeDef = TypedDict(
    "GetCampaignActivitiesResponseTypeDef",
    {
        "ActivitiesResponse": "ActivitiesResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCampaignDateRangeKpiRequestRequestTypeDef = TypedDict(
    "_RequiredGetCampaignDateRangeKpiRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "KpiName": str,
    },
)
_OptionalGetCampaignDateRangeKpiRequestRequestTypeDef = TypedDict(
    "_OptionalGetCampaignDateRangeKpiRequestRequestTypeDef",
    {
        "EndTime": Union[datetime, str],
        "NextToken": str,
        "PageSize": str,
        "StartTime": Union[datetime, str],
    },
    total=False,
)

class GetCampaignDateRangeKpiRequestRequestTypeDef(
    _RequiredGetCampaignDateRangeKpiRequestRequestTypeDef,
    _OptionalGetCampaignDateRangeKpiRequestRequestTypeDef,
):
    pass

GetCampaignDateRangeKpiResponseTypeDef = TypedDict(
    "GetCampaignDateRangeKpiResponseTypeDef",
    {
        "CampaignDateRangeKpiResponse": "CampaignDateRangeKpiResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCampaignRequestRequestTypeDef = TypedDict(
    "GetCampaignRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
    },
)

GetCampaignResponseTypeDef = TypedDict(
    "GetCampaignResponseTypeDef",
    {
        "CampaignResponse": "CampaignResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCampaignVersionRequestRequestTypeDef = TypedDict(
    "GetCampaignVersionRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "Version": str,
    },
)

GetCampaignVersionResponseTypeDef = TypedDict(
    "GetCampaignVersionResponseTypeDef",
    {
        "CampaignResponse": "CampaignResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCampaignVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredGetCampaignVersionsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
    },
)
_OptionalGetCampaignVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalGetCampaignVersionsRequestRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)

class GetCampaignVersionsRequestRequestTypeDef(
    _RequiredGetCampaignVersionsRequestRequestTypeDef,
    _OptionalGetCampaignVersionsRequestRequestTypeDef,
):
    pass

GetCampaignVersionsResponseTypeDef = TypedDict(
    "GetCampaignVersionsResponseTypeDef",
    {
        "CampaignsResponse": "CampaignsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCampaignsRequestRequestTypeDef = TypedDict(
    "_RequiredGetCampaignsRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalGetCampaignsRequestRequestTypeDef = TypedDict(
    "_OptionalGetCampaignsRequestRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)

class GetCampaignsRequestRequestTypeDef(
    _RequiredGetCampaignsRequestRequestTypeDef, _OptionalGetCampaignsRequestRequestTypeDef
):
    pass

GetCampaignsResponseTypeDef = TypedDict(
    "GetCampaignsResponseTypeDef",
    {
        "CampaignsResponse": "CampaignsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChannelsRequestRequestTypeDef = TypedDict(
    "GetChannelsRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetChannelsResponseTypeDef = TypedDict(
    "GetChannelsResponseTypeDef",
    {
        "ChannelsResponse": "ChannelsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEmailChannelRequestRequestTypeDef = TypedDict(
    "GetEmailChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetEmailChannelResponseTypeDef = TypedDict(
    "GetEmailChannelResponseTypeDef",
    {
        "EmailChannelResponse": "EmailChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetEmailTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredGetEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)
_OptionalGetEmailTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalGetEmailTemplateRequestRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)

class GetEmailTemplateRequestRequestTypeDef(
    _RequiredGetEmailTemplateRequestRequestTypeDef, _OptionalGetEmailTemplateRequestRequestTypeDef
):
    pass

GetEmailTemplateResponseTypeDef = TypedDict(
    "GetEmailTemplateResponseTypeDef",
    {
        "EmailTemplateResponse": "EmailTemplateResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEndpointRequestRequestTypeDef = TypedDict(
    "GetEndpointRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EndpointId": str,
    },
)

GetEndpointResponseTypeDef = TypedDict(
    "GetEndpointResponseTypeDef",
    {
        "EndpointResponse": "EndpointResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventStreamRequestRequestTypeDef = TypedDict(
    "GetEventStreamRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetEventStreamResponseTypeDef = TypedDict(
    "GetEventStreamResponseTypeDef",
    {
        "EventStream": "EventStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExportJobRequestRequestTypeDef = TypedDict(
    "GetExportJobRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JobId": str,
    },
)

GetExportJobResponseTypeDef = TypedDict(
    "GetExportJobResponseTypeDef",
    {
        "ExportJobResponse": "ExportJobResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetExportJobsRequestRequestTypeDef = TypedDict(
    "_RequiredGetExportJobsRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalGetExportJobsRequestRequestTypeDef = TypedDict(
    "_OptionalGetExportJobsRequestRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)

class GetExportJobsRequestRequestTypeDef(
    _RequiredGetExportJobsRequestRequestTypeDef, _OptionalGetExportJobsRequestRequestTypeDef
):
    pass

GetExportJobsResponseTypeDef = TypedDict(
    "GetExportJobsResponseTypeDef",
    {
        "ExportJobsResponse": "ExportJobsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGcmChannelRequestRequestTypeDef = TypedDict(
    "GetGcmChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetGcmChannelResponseTypeDef = TypedDict(
    "GetGcmChannelResponseTypeDef",
    {
        "GCMChannelResponse": "GCMChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImportJobRequestRequestTypeDef = TypedDict(
    "GetImportJobRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JobId": str,
    },
)

GetImportJobResponseTypeDef = TypedDict(
    "GetImportJobResponseTypeDef",
    {
        "ImportJobResponse": "ImportJobResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetImportJobsRequestRequestTypeDef = TypedDict(
    "_RequiredGetImportJobsRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalGetImportJobsRequestRequestTypeDef = TypedDict(
    "_OptionalGetImportJobsRequestRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)

class GetImportJobsRequestRequestTypeDef(
    _RequiredGetImportJobsRequestRequestTypeDef, _OptionalGetImportJobsRequestRequestTypeDef
):
    pass

GetImportJobsResponseTypeDef = TypedDict(
    "GetImportJobsResponseTypeDef",
    {
        "ImportJobsResponse": "ImportJobsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetJourneyDateRangeKpiRequestRequestTypeDef = TypedDict(
    "_RequiredGetJourneyDateRangeKpiRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
        "KpiName": str,
    },
)
_OptionalGetJourneyDateRangeKpiRequestRequestTypeDef = TypedDict(
    "_OptionalGetJourneyDateRangeKpiRequestRequestTypeDef",
    {
        "EndTime": Union[datetime, str],
        "NextToken": str,
        "PageSize": str,
        "StartTime": Union[datetime, str],
    },
    total=False,
)

class GetJourneyDateRangeKpiRequestRequestTypeDef(
    _RequiredGetJourneyDateRangeKpiRequestRequestTypeDef,
    _OptionalGetJourneyDateRangeKpiRequestRequestTypeDef,
):
    pass

GetJourneyDateRangeKpiResponseTypeDef = TypedDict(
    "GetJourneyDateRangeKpiResponseTypeDef",
    {
        "JourneyDateRangeKpiResponse": "JourneyDateRangeKpiResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetJourneyExecutionActivityMetricsRequestRequestTypeDef = TypedDict(
    "_RequiredGetJourneyExecutionActivityMetricsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyActivityId": str,
        "JourneyId": str,
    },
)
_OptionalGetJourneyExecutionActivityMetricsRequestRequestTypeDef = TypedDict(
    "_OptionalGetJourneyExecutionActivityMetricsRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": str,
    },
    total=False,
)

class GetJourneyExecutionActivityMetricsRequestRequestTypeDef(
    _RequiredGetJourneyExecutionActivityMetricsRequestRequestTypeDef,
    _OptionalGetJourneyExecutionActivityMetricsRequestRequestTypeDef,
):
    pass

GetJourneyExecutionActivityMetricsResponseTypeDef = TypedDict(
    "GetJourneyExecutionActivityMetricsResponseTypeDef",
    {
        "JourneyExecutionActivityMetricsResponse": "JourneyExecutionActivityMetricsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetJourneyExecutionMetricsRequestRequestTypeDef = TypedDict(
    "_RequiredGetJourneyExecutionMetricsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
    },
)
_OptionalGetJourneyExecutionMetricsRequestRequestTypeDef = TypedDict(
    "_OptionalGetJourneyExecutionMetricsRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": str,
    },
    total=False,
)

class GetJourneyExecutionMetricsRequestRequestTypeDef(
    _RequiredGetJourneyExecutionMetricsRequestRequestTypeDef,
    _OptionalGetJourneyExecutionMetricsRequestRequestTypeDef,
):
    pass

GetJourneyExecutionMetricsResponseTypeDef = TypedDict(
    "GetJourneyExecutionMetricsResponseTypeDef",
    {
        "JourneyExecutionMetricsResponse": "JourneyExecutionMetricsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJourneyRequestRequestTypeDef = TypedDict(
    "GetJourneyRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
    },
)

GetJourneyResponseTypeDef = TypedDict(
    "GetJourneyResponseTypeDef",
    {
        "JourneyResponse": "JourneyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPushTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredGetPushTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)
_OptionalGetPushTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalGetPushTemplateRequestRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)

class GetPushTemplateRequestRequestTypeDef(
    _RequiredGetPushTemplateRequestRequestTypeDef, _OptionalGetPushTemplateRequestRequestTypeDef
):
    pass

GetPushTemplateResponseTypeDef = TypedDict(
    "GetPushTemplateResponseTypeDef",
    {
        "PushNotificationTemplateResponse": "PushNotificationTemplateResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecommenderConfigurationRequestRequestTypeDef = TypedDict(
    "GetRecommenderConfigurationRequestRequestTypeDef",
    {
        "RecommenderId": str,
    },
)

GetRecommenderConfigurationResponseTypeDef = TypedDict(
    "GetRecommenderConfigurationResponseTypeDef",
    {
        "RecommenderConfigurationResponse": "RecommenderConfigurationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecommenderConfigurationsRequestRequestTypeDef = TypedDict(
    "GetRecommenderConfigurationsRequestRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)

GetRecommenderConfigurationsResponseTypeDef = TypedDict(
    "GetRecommenderConfigurationsResponseTypeDef",
    {
        "ListRecommenderConfigurationsResponse": "ListRecommenderConfigurationsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSegmentExportJobsRequestRequestTypeDef = TypedDict(
    "_RequiredGetSegmentExportJobsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
    },
)
_OptionalGetSegmentExportJobsRequestRequestTypeDef = TypedDict(
    "_OptionalGetSegmentExportJobsRequestRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)

class GetSegmentExportJobsRequestRequestTypeDef(
    _RequiredGetSegmentExportJobsRequestRequestTypeDef,
    _OptionalGetSegmentExportJobsRequestRequestTypeDef,
):
    pass

GetSegmentExportJobsResponseTypeDef = TypedDict(
    "GetSegmentExportJobsResponseTypeDef",
    {
        "ExportJobsResponse": "ExportJobsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSegmentImportJobsRequestRequestTypeDef = TypedDict(
    "_RequiredGetSegmentImportJobsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
    },
)
_OptionalGetSegmentImportJobsRequestRequestTypeDef = TypedDict(
    "_OptionalGetSegmentImportJobsRequestRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)

class GetSegmentImportJobsRequestRequestTypeDef(
    _RequiredGetSegmentImportJobsRequestRequestTypeDef,
    _OptionalGetSegmentImportJobsRequestRequestTypeDef,
):
    pass

GetSegmentImportJobsResponseTypeDef = TypedDict(
    "GetSegmentImportJobsResponseTypeDef",
    {
        "ImportJobsResponse": "ImportJobsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSegmentRequestRequestTypeDef = TypedDict(
    "GetSegmentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
    },
)

GetSegmentResponseTypeDef = TypedDict(
    "GetSegmentResponseTypeDef",
    {
        "SegmentResponse": "SegmentResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSegmentVersionRequestRequestTypeDef = TypedDict(
    "GetSegmentVersionRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
        "Version": str,
    },
)

GetSegmentVersionResponseTypeDef = TypedDict(
    "GetSegmentVersionResponseTypeDef",
    {
        "SegmentResponse": "SegmentResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSegmentVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredGetSegmentVersionsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
    },
)
_OptionalGetSegmentVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalGetSegmentVersionsRequestRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)

class GetSegmentVersionsRequestRequestTypeDef(
    _RequiredGetSegmentVersionsRequestRequestTypeDef,
    _OptionalGetSegmentVersionsRequestRequestTypeDef,
):
    pass

GetSegmentVersionsResponseTypeDef = TypedDict(
    "GetSegmentVersionsResponseTypeDef",
    {
        "SegmentsResponse": "SegmentsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSegmentsRequestRequestTypeDef = TypedDict(
    "_RequiredGetSegmentsRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalGetSegmentsRequestRequestTypeDef = TypedDict(
    "_OptionalGetSegmentsRequestRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)

class GetSegmentsRequestRequestTypeDef(
    _RequiredGetSegmentsRequestRequestTypeDef, _OptionalGetSegmentsRequestRequestTypeDef
):
    pass

GetSegmentsResponseTypeDef = TypedDict(
    "GetSegmentsResponseTypeDef",
    {
        "SegmentsResponse": "SegmentsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSmsChannelRequestRequestTypeDef = TypedDict(
    "GetSmsChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetSmsChannelResponseTypeDef = TypedDict(
    "GetSmsChannelResponseTypeDef",
    {
        "SMSChannelResponse": "SMSChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSmsTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredGetSmsTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)
_OptionalGetSmsTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalGetSmsTemplateRequestRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)

class GetSmsTemplateRequestRequestTypeDef(
    _RequiredGetSmsTemplateRequestRequestTypeDef, _OptionalGetSmsTemplateRequestRequestTypeDef
):
    pass

GetSmsTemplateResponseTypeDef = TypedDict(
    "GetSmsTemplateResponseTypeDef",
    {
        "SMSTemplateResponse": "SMSTemplateResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserEndpointsRequestRequestTypeDef = TypedDict(
    "GetUserEndpointsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "UserId": str,
    },
)

GetUserEndpointsResponseTypeDef = TypedDict(
    "GetUserEndpointsResponseTypeDef",
    {
        "EndpointsResponse": "EndpointsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceChannelRequestRequestTypeDef = TypedDict(
    "GetVoiceChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetVoiceChannelResponseTypeDef = TypedDict(
    "GetVoiceChannelResponseTypeDef",
    {
        "VoiceChannelResponse": "VoiceChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetVoiceTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredGetVoiceTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)
_OptionalGetVoiceTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalGetVoiceTemplateRequestRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)

class GetVoiceTemplateRequestRequestTypeDef(
    _RequiredGetVoiceTemplateRequestRequestTypeDef, _OptionalGetVoiceTemplateRequestRequestTypeDef
):
    pass

GetVoiceTemplateResponseTypeDef = TypedDict(
    "GetVoiceTemplateResponseTypeDef",
    {
        "VoiceTemplateResponse": "VoiceTemplateResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredHoldoutActivityTypeDef = TypedDict(
    "_RequiredHoldoutActivityTypeDef",
    {
        "Percentage": int,
    },
)
_OptionalHoldoutActivityTypeDef = TypedDict(
    "_OptionalHoldoutActivityTypeDef",
    {
        "NextActivity": str,
    },
    total=False,
)

class HoldoutActivityTypeDef(_RequiredHoldoutActivityTypeDef, _OptionalHoldoutActivityTypeDef):
    pass

_RequiredImportJobRequestTypeDef = TypedDict(
    "_RequiredImportJobRequestTypeDef",
    {
        "Format": FormatType,
        "RoleArn": str,
        "S3Url": str,
    },
)
_OptionalImportJobRequestTypeDef = TypedDict(
    "_OptionalImportJobRequestTypeDef",
    {
        "DefineSegment": bool,
        "ExternalId": str,
        "RegisterEndpoints": bool,
        "SegmentId": str,
        "SegmentName": str,
    },
    total=False,
)

class ImportJobRequestTypeDef(_RequiredImportJobRequestTypeDef, _OptionalImportJobRequestTypeDef):
    pass

_RequiredImportJobResourceTypeDef = TypedDict(
    "_RequiredImportJobResourceTypeDef",
    {
        "Format": FormatType,
        "RoleArn": str,
        "S3Url": str,
    },
)
_OptionalImportJobResourceTypeDef = TypedDict(
    "_OptionalImportJobResourceTypeDef",
    {
        "DefineSegment": bool,
        "ExternalId": str,
        "RegisterEndpoints": bool,
        "SegmentId": str,
        "SegmentName": str,
    },
    total=False,
)

class ImportJobResourceTypeDef(
    _RequiredImportJobResourceTypeDef, _OptionalImportJobResourceTypeDef
):
    pass

_RequiredImportJobResponseTypeDef = TypedDict(
    "_RequiredImportJobResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "Definition": "ImportJobResourceTypeDef",
        "Id": str,
        "JobStatus": JobStatusType,
        "Type": str,
    },
)
_OptionalImportJobResponseTypeDef = TypedDict(
    "_OptionalImportJobResponseTypeDef",
    {
        "CompletedPieces": int,
        "CompletionDate": str,
        "FailedPieces": int,
        "Failures": List[str],
        "TotalFailures": int,
        "TotalPieces": int,
        "TotalProcessed": int,
    },
    total=False,
)

class ImportJobResponseTypeDef(
    _RequiredImportJobResponseTypeDef, _OptionalImportJobResponseTypeDef
):
    pass

_RequiredImportJobsResponseTypeDef = TypedDict(
    "_RequiredImportJobsResponseTypeDef",
    {
        "Item": List["ImportJobResponseTypeDef"],
    },
)
_OptionalImportJobsResponseTypeDef = TypedDict(
    "_OptionalImportJobsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ImportJobsResponseTypeDef(
    _RequiredImportJobsResponseTypeDef, _OptionalImportJobsResponseTypeDef
):
    pass

ItemResponseTypeDef = TypedDict(
    "ItemResponseTypeDef",
    {
        "EndpointItemResponse": "EndpointItemResponseTypeDef",
        "EventsItemResponse": Dict[str, "EventItemResponseTypeDef"],
    },
    total=False,
)

JourneyCustomMessageTypeDef = TypedDict(
    "JourneyCustomMessageTypeDef",
    {
        "Data": str,
    },
    total=False,
)

_RequiredJourneyDateRangeKpiResponseTypeDef = TypedDict(
    "_RequiredJourneyDateRangeKpiResponseTypeDef",
    {
        "ApplicationId": str,
        "EndTime": datetime,
        "JourneyId": str,
        "KpiName": str,
        "KpiResult": "BaseKpiResultTypeDef",
        "StartTime": datetime,
    },
)
_OptionalJourneyDateRangeKpiResponseTypeDef = TypedDict(
    "_OptionalJourneyDateRangeKpiResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class JourneyDateRangeKpiResponseTypeDef(
    _RequiredJourneyDateRangeKpiResponseTypeDef, _OptionalJourneyDateRangeKpiResponseTypeDef
):
    pass

JourneyEmailMessageTypeDef = TypedDict(
    "JourneyEmailMessageTypeDef",
    {
        "FromAddress": str,
    },
    total=False,
)

JourneyExecutionActivityMetricsResponseTypeDef = TypedDict(
    "JourneyExecutionActivityMetricsResponseTypeDef",
    {
        "ActivityType": str,
        "ApplicationId": str,
        "JourneyActivityId": str,
        "JourneyId": str,
        "LastEvaluatedTime": str,
        "Metrics": Dict[str, str],
    },
)

JourneyExecutionMetricsResponseTypeDef = TypedDict(
    "JourneyExecutionMetricsResponseTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
        "LastEvaluatedTime": str,
        "Metrics": Dict[str, str],
    },
)

JourneyLimitsTypeDef = TypedDict(
    "JourneyLimitsTypeDef",
    {
        "DailyCap": int,
        "EndpointReentryCap": int,
        "MessagesPerSecond": int,
        "EndpointReentryInterval": str,
    },
    total=False,
)

JourneyPushMessageTypeDef = TypedDict(
    "JourneyPushMessageTypeDef",
    {
        "TimeToLive": str,
    },
    total=False,
)

_RequiredJourneyResponseTypeDef = TypedDict(
    "_RequiredJourneyResponseTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
    },
)
_OptionalJourneyResponseTypeDef = TypedDict(
    "_OptionalJourneyResponseTypeDef",
    {
        "Activities": Dict[str, "ActivityTypeDef"],
        "CreationDate": str,
        "LastModifiedDate": str,
        "Limits": "JourneyLimitsTypeDef",
        "LocalTime": bool,
        "QuietTime": "QuietTimeTypeDef",
        "RefreshFrequency": str,
        "Schedule": "JourneyScheduleTypeDef",
        "StartActivity": str,
        "StartCondition": "StartConditionTypeDef",
        "State": StateType,
        "tags": Dict[str, str],
        "WaitForQuietTime": bool,
        "RefreshOnSegmentUpdate": bool,
    },
    total=False,
)

class JourneyResponseTypeDef(_RequiredJourneyResponseTypeDef, _OptionalJourneyResponseTypeDef):
    pass

JourneySMSMessageTypeDef = TypedDict(
    "JourneySMSMessageTypeDef",
    {
        "MessageType": MessageTypeType,
        "OriginationNumber": str,
        "SenderId": str,
        "EntityId": str,
        "TemplateId": str,
    },
    total=False,
)

JourneyScheduleTypeDef = TypedDict(
    "JourneyScheduleTypeDef",
    {
        "EndTime": Union[datetime, str],
        "StartTime": Union[datetime, str],
        "Timezone": str,
    },
    total=False,
)

JourneyStateRequestTypeDef = TypedDict(
    "JourneyStateRequestTypeDef",
    {
        "State": StateType,
    },
    total=False,
)

_RequiredJourneysResponseTypeDef = TypedDict(
    "_RequiredJourneysResponseTypeDef",
    {
        "Item": List["JourneyResponseTypeDef"],
    },
)
_OptionalJourneysResponseTypeDef = TypedDict(
    "_OptionalJourneysResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class JourneysResponseTypeDef(_RequiredJourneysResponseTypeDef, _OptionalJourneysResponseTypeDef):
    pass

_RequiredListJourneysRequestRequestTypeDef = TypedDict(
    "_RequiredListJourneysRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalListJourneysRequestRequestTypeDef = TypedDict(
    "_OptionalListJourneysRequestRequestTypeDef",
    {
        "PageSize": str,
        "Token": str,
    },
    total=False,
)

class ListJourneysRequestRequestTypeDef(
    _RequiredListJourneysRequestRequestTypeDef, _OptionalListJourneysRequestRequestTypeDef
):
    pass

ListJourneysResponseTypeDef = TypedDict(
    "ListJourneysResponseTypeDef",
    {
        "JourneysResponse": "JourneysResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRecommenderConfigurationsResponseTypeDef = TypedDict(
    "_RequiredListRecommenderConfigurationsResponseTypeDef",
    {
        "Item": List["RecommenderConfigurationResponseTypeDef"],
    },
)
_OptionalListRecommenderConfigurationsResponseTypeDef = TypedDict(
    "_OptionalListRecommenderConfigurationsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListRecommenderConfigurationsResponseTypeDef(
    _RequiredListRecommenderConfigurationsResponseTypeDef,
    _OptionalListRecommenderConfigurationsResponseTypeDef,
):
    pass

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "TagsModel": "TagsModelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTemplateVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListTemplateVersionsRequestRequestTypeDef",
    {
        "TemplateName": str,
        "TemplateType": str,
    },
)
_OptionalListTemplateVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListTemplateVersionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": str,
    },
    total=False,
)

class ListTemplateVersionsRequestRequestTypeDef(
    _RequiredListTemplateVersionsRequestRequestTypeDef,
    _OptionalListTemplateVersionsRequestRequestTypeDef,
):
    pass

ListTemplateVersionsResponseTypeDef = TypedDict(
    "ListTemplateVersionsResponseTypeDef",
    {
        "TemplateVersionsResponse": "TemplateVersionsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTemplatesRequestRequestTypeDef = TypedDict(
    "ListTemplatesRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": str,
        "Prefix": str,
        "TemplateType": str,
    },
    total=False,
)

ListTemplatesResponseTypeDef = TypedDict(
    "ListTemplatesResponseTypeDef",
    {
        "TemplatesResponse": "TemplatesResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MessageBodyTypeDef = TypedDict(
    "MessageBodyTypeDef",
    {
        "Message": str,
        "RequestID": str,
    },
    total=False,
)

MessageConfigurationTypeDef = TypedDict(
    "MessageConfigurationTypeDef",
    {
        "ADMMessage": "MessageTypeDef",
        "APNSMessage": "MessageTypeDef",
        "BaiduMessage": "MessageTypeDef",
        "CustomMessage": "CampaignCustomMessageTypeDef",
        "DefaultMessage": "MessageTypeDef",
        "EmailMessage": "CampaignEmailMessageTypeDef",
        "GCMMessage": "MessageTypeDef",
        "SMSMessage": "CampaignSmsMessageTypeDef",
    },
    total=False,
)

_RequiredMessageRequestTypeDef = TypedDict(
    "_RequiredMessageRequestTypeDef",
    {
        "MessageConfiguration": "DirectMessageConfigurationTypeDef",
    },
)
_OptionalMessageRequestTypeDef = TypedDict(
    "_OptionalMessageRequestTypeDef",
    {
        "Addresses": Dict[str, "AddressConfigurationTypeDef"],
        "Context": Dict[str, str],
        "Endpoints": Dict[str, "EndpointSendConfigurationTypeDef"],
        "TemplateConfiguration": "TemplateConfigurationTypeDef",
        "TraceId": str,
    },
    total=False,
)

class MessageRequestTypeDef(_RequiredMessageRequestTypeDef, _OptionalMessageRequestTypeDef):
    pass

_RequiredMessageResponseTypeDef = TypedDict(
    "_RequiredMessageResponseTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalMessageResponseTypeDef = TypedDict(
    "_OptionalMessageResponseTypeDef",
    {
        "EndpointResult": Dict[str, "EndpointMessageResultTypeDef"],
        "RequestId": str,
        "Result": Dict[str, "MessageResultTypeDef"],
    },
    total=False,
)

class MessageResponseTypeDef(_RequiredMessageResponseTypeDef, _OptionalMessageResponseTypeDef):
    pass

_RequiredMessageResultTypeDef = TypedDict(
    "_RequiredMessageResultTypeDef",
    {
        "DeliveryStatus": DeliveryStatusType,
        "StatusCode": int,
    },
)
_OptionalMessageResultTypeDef = TypedDict(
    "_OptionalMessageResultTypeDef",
    {
        "MessageId": str,
        "StatusMessage": str,
        "UpdatedToken": str,
    },
    total=False,
)

class MessageResultTypeDef(_RequiredMessageResultTypeDef, _OptionalMessageResultTypeDef):
    pass

MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "Action": ActionType,
        "Body": str,
        "ImageIconUrl": str,
        "ImageSmallIconUrl": str,
        "ImageUrl": str,
        "JsonBody": str,
        "MediaUrl": str,
        "RawContent": str,
        "SilentPush": bool,
        "TimeToLive": int,
        "Title": str,
        "Url": str,
    },
    total=False,
)

MetricDimensionTypeDef = TypedDict(
    "MetricDimensionTypeDef",
    {
        "ComparisonOperator": str,
        "Value": float,
    },
)

MultiConditionalBranchTypeDef = TypedDict(
    "MultiConditionalBranchTypeDef",
    {
        "Condition": "SimpleConditionTypeDef",
        "NextActivity": str,
    },
    total=False,
)

MultiConditionalSplitActivityTypeDef = TypedDict(
    "MultiConditionalSplitActivityTypeDef",
    {
        "Branches": List["MultiConditionalBranchTypeDef"],
        "DefaultActivity": str,
        "EvaluationWaitTime": "WaitTimeTypeDef",
    },
    total=False,
)

NumberValidateRequestTypeDef = TypedDict(
    "NumberValidateRequestTypeDef",
    {
        "IsoCountryCode": str,
        "PhoneNumber": str,
    },
    total=False,
)

NumberValidateResponseTypeDef = TypedDict(
    "NumberValidateResponseTypeDef",
    {
        "Carrier": str,
        "City": str,
        "CleansedPhoneNumberE164": str,
        "CleansedPhoneNumberNational": str,
        "Country": str,
        "CountryCodeIso2": str,
        "CountryCodeNumeric": str,
        "County": str,
        "OriginalCountryCodeIso2": str,
        "OriginalPhoneNumber": str,
        "PhoneType": str,
        "PhoneTypeCode": int,
        "Timezone": str,
        "ZipCode": str,
    },
    total=False,
)

PhoneNumberValidateRequestRequestTypeDef = TypedDict(
    "PhoneNumberValidateRequestRequestTypeDef",
    {
        "NumberValidateRequest": "NumberValidateRequestTypeDef",
    },
)

PhoneNumberValidateResponseTypeDef = TypedDict(
    "PhoneNumberValidateResponseTypeDef",
    {
        "NumberValidateResponse": "NumberValidateResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PublicEndpointTypeDef = TypedDict(
    "PublicEndpointTypeDef",
    {
        "Address": str,
        "Attributes": Dict[str, List[str]],
        "ChannelType": ChannelTypeType,
        "Demographic": "EndpointDemographicTypeDef",
        "EffectiveDate": str,
        "EndpointStatus": str,
        "Location": "EndpointLocationTypeDef",
        "Metrics": Dict[str, float],
        "OptOut": str,
        "RequestId": str,
        "User": "EndpointUserTypeDef",
    },
    total=False,
)

PushMessageActivityTypeDef = TypedDict(
    "PushMessageActivityTypeDef",
    {
        "MessageConfig": "JourneyPushMessageTypeDef",
        "NextActivity": str,
        "TemplateName": str,
        "TemplateVersion": str,
    },
    total=False,
)

PushNotificationTemplateRequestTypeDef = TypedDict(
    "PushNotificationTemplateRequestTypeDef",
    {
        "ADM": "AndroidPushNotificationTemplateTypeDef",
        "APNS": "APNSPushNotificationTemplateTypeDef",
        "Baidu": "AndroidPushNotificationTemplateTypeDef",
        "Default": "DefaultPushNotificationTemplateTypeDef",
        "DefaultSubstitutions": str,
        "GCM": "AndroidPushNotificationTemplateTypeDef",
        "RecommenderId": str,
        "tags": Dict[str, str],
        "TemplateDescription": str,
    },
    total=False,
)

_RequiredPushNotificationTemplateResponseTypeDef = TypedDict(
    "_RequiredPushNotificationTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": TemplateTypeType,
    },
)
_OptionalPushNotificationTemplateResponseTypeDef = TypedDict(
    "_OptionalPushNotificationTemplateResponseTypeDef",
    {
        "ADM": "AndroidPushNotificationTemplateTypeDef",
        "APNS": "APNSPushNotificationTemplateTypeDef",
        "Arn": str,
        "Baidu": "AndroidPushNotificationTemplateTypeDef",
        "Default": "DefaultPushNotificationTemplateTypeDef",
        "DefaultSubstitutions": str,
        "GCM": "AndroidPushNotificationTemplateTypeDef",
        "RecommenderId": str,
        "tags": Dict[str, str],
        "TemplateDescription": str,
        "Version": str,
    },
    total=False,
)

class PushNotificationTemplateResponseTypeDef(
    _RequiredPushNotificationTemplateResponseTypeDef,
    _OptionalPushNotificationTemplateResponseTypeDef,
):
    pass

PutEventStreamRequestRequestTypeDef = TypedDict(
    "PutEventStreamRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "WriteEventStream": "WriteEventStreamTypeDef",
    },
)

PutEventStreamResponseTypeDef = TypedDict(
    "PutEventStreamResponseTypeDef",
    {
        "EventStream": "EventStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutEventsRequestRequestTypeDef = TypedDict(
    "PutEventsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EventsRequest": "EventsRequestTypeDef",
    },
)

PutEventsResponseTypeDef = TypedDict(
    "PutEventsResponseTypeDef",
    {
        "EventsResponse": "EventsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QuietTimeTypeDef = TypedDict(
    "QuietTimeTypeDef",
    {
        "End": str,
        "Start": str,
    },
    total=False,
)

RandomSplitActivityTypeDef = TypedDict(
    "RandomSplitActivityTypeDef",
    {
        "Branches": List["RandomSplitEntryTypeDef"],
    },
    total=False,
)

RandomSplitEntryTypeDef = TypedDict(
    "RandomSplitEntryTypeDef",
    {
        "NextActivity": str,
        "Percentage": int,
    },
    total=False,
)

RawEmailTypeDef = TypedDict(
    "RawEmailTypeDef",
    {
        "Data": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

RecencyDimensionTypeDef = TypedDict(
    "RecencyDimensionTypeDef",
    {
        "Duration": DurationType,
        "RecencyType": RecencyTypeType,
    },
)

_RequiredRecommenderConfigurationResponseTypeDef = TypedDict(
    "_RequiredRecommenderConfigurationResponseTypeDef",
    {
        "CreationDate": str,
        "Id": str,
        "LastModifiedDate": str,
        "RecommendationProviderRoleArn": str,
        "RecommendationProviderUri": str,
    },
)
_OptionalRecommenderConfigurationResponseTypeDef = TypedDict(
    "_OptionalRecommenderConfigurationResponseTypeDef",
    {
        "Attributes": Dict[str, str],
        "Description": str,
        "Name": str,
        "RecommendationProviderIdType": str,
        "RecommendationTransformerUri": str,
        "RecommendationsDisplayName": str,
        "RecommendationsPerMessage": int,
    },
    total=False,
)

class RecommenderConfigurationResponseTypeDef(
    _RequiredRecommenderConfigurationResponseTypeDef,
    _OptionalRecommenderConfigurationResponseTypeDef,
):
    pass

RemoveAttributesRequestRequestTypeDef = TypedDict(
    "RemoveAttributesRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "AttributeType": str,
        "UpdateAttributesRequest": "UpdateAttributesRequestTypeDef",
    },
)

RemoveAttributesResponseTypeDef = TypedDict(
    "RemoveAttributesResponseTypeDef",
    {
        "AttributesResource": "AttributesResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

ResultRowTypeDef = TypedDict(
    "ResultRowTypeDef",
    {
        "GroupedBys": List["ResultRowValueTypeDef"],
        "Values": List["ResultRowValueTypeDef"],
    },
)

ResultRowValueTypeDef = TypedDict(
    "ResultRowValueTypeDef",
    {
        "Key": str,
        "Type": str,
        "Value": str,
    },
)

SMSChannelRequestTypeDef = TypedDict(
    "SMSChannelRequestTypeDef",
    {
        "Enabled": bool,
        "SenderId": str,
        "ShortCode": str,
    },
    total=False,
)

_RequiredSMSChannelResponseTypeDef = TypedDict(
    "_RequiredSMSChannelResponseTypeDef",
    {
        "Platform": str,
    },
)
_OptionalSMSChannelResponseTypeDef = TypedDict(
    "_OptionalSMSChannelResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "Enabled": bool,
        "HasCredential": bool,
        "Id": str,
        "IsArchived": bool,
        "LastModifiedBy": str,
        "LastModifiedDate": str,
        "PromotionalMessagesPerSecond": int,
        "SenderId": str,
        "ShortCode": str,
        "TransactionalMessagesPerSecond": int,
        "Version": int,
    },
    total=False,
)

class SMSChannelResponseTypeDef(
    _RequiredSMSChannelResponseTypeDef, _OptionalSMSChannelResponseTypeDef
):
    pass

SMSMessageActivityTypeDef = TypedDict(
    "SMSMessageActivityTypeDef",
    {
        "MessageConfig": "JourneySMSMessageTypeDef",
        "NextActivity": str,
        "TemplateName": str,
        "TemplateVersion": str,
    },
    total=False,
)

SMSMessageTypeDef = TypedDict(
    "SMSMessageTypeDef",
    {
        "Body": str,
        "Keyword": str,
        "MediaUrl": str,
        "MessageType": MessageTypeType,
        "OriginationNumber": str,
        "SenderId": str,
        "Substitutions": Dict[str, List[str]],
        "EntityId": str,
        "TemplateId": str,
    },
    total=False,
)

SMSTemplateRequestTypeDef = TypedDict(
    "SMSTemplateRequestTypeDef",
    {
        "Body": str,
        "DefaultSubstitutions": str,
        "RecommenderId": str,
        "tags": Dict[str, str],
        "TemplateDescription": str,
    },
    total=False,
)

_RequiredSMSTemplateResponseTypeDef = TypedDict(
    "_RequiredSMSTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": TemplateTypeType,
    },
)
_OptionalSMSTemplateResponseTypeDef = TypedDict(
    "_OptionalSMSTemplateResponseTypeDef",
    {
        "Arn": str,
        "Body": str,
        "DefaultSubstitutions": str,
        "RecommenderId": str,
        "tags": Dict[str, str],
        "TemplateDescription": str,
        "Version": str,
    },
    total=False,
)

class SMSTemplateResponseTypeDef(
    _RequiredSMSTemplateResponseTypeDef, _OptionalSMSTemplateResponseTypeDef
):
    pass

_RequiredScheduleTypeDef = TypedDict(
    "_RequiredScheduleTypeDef",
    {
        "StartTime": str,
    },
)
_OptionalScheduleTypeDef = TypedDict(
    "_OptionalScheduleTypeDef",
    {
        "EndTime": str,
        "EventFilter": "CampaignEventFilterTypeDef",
        "Frequency": FrequencyType,
        "IsLocalTime": bool,
        "QuietTime": "QuietTimeTypeDef",
        "Timezone": str,
    },
    total=False,
)

class ScheduleTypeDef(_RequiredScheduleTypeDef, _OptionalScheduleTypeDef):
    pass

SegmentBehaviorsTypeDef = TypedDict(
    "SegmentBehaviorsTypeDef",
    {
        "Recency": "RecencyDimensionTypeDef",
    },
    total=False,
)

SegmentConditionTypeDef = TypedDict(
    "SegmentConditionTypeDef",
    {
        "SegmentId": str,
    },
)

SegmentDemographicsTypeDef = TypedDict(
    "SegmentDemographicsTypeDef",
    {
        "AppVersion": "SetDimensionTypeDef",
        "Channel": "SetDimensionTypeDef",
        "DeviceType": "SetDimensionTypeDef",
        "Make": "SetDimensionTypeDef",
        "Model": "SetDimensionTypeDef",
        "Platform": "SetDimensionTypeDef",
    },
    total=False,
)

SegmentDimensionsTypeDef = TypedDict(
    "SegmentDimensionsTypeDef",
    {
        "Attributes": Dict[str, "AttributeDimensionTypeDef"],
        "Behavior": "SegmentBehaviorsTypeDef",
        "Demographic": "SegmentDemographicsTypeDef",
        "Location": "SegmentLocationTypeDef",
        "Metrics": Dict[str, "MetricDimensionTypeDef"],
        "UserAttributes": Dict[str, "AttributeDimensionTypeDef"],
    },
    total=False,
)

SegmentGroupListTypeDef = TypedDict(
    "SegmentGroupListTypeDef",
    {
        "Groups": List["SegmentGroupTypeDef"],
        "Include": IncludeType,
    },
    total=False,
)

SegmentGroupTypeDef = TypedDict(
    "SegmentGroupTypeDef",
    {
        "Dimensions": List["SegmentDimensionsTypeDef"],
        "SourceSegments": List["SegmentReferenceTypeDef"],
        "SourceType": SourceTypeType,
        "Type": TypeType,
    },
    total=False,
)

_RequiredSegmentImportResourceTypeDef = TypedDict(
    "_RequiredSegmentImportResourceTypeDef",
    {
        "ExternalId": str,
        "Format": FormatType,
        "RoleArn": str,
        "S3Url": str,
        "Size": int,
    },
)
_OptionalSegmentImportResourceTypeDef = TypedDict(
    "_OptionalSegmentImportResourceTypeDef",
    {
        "ChannelCounts": Dict[str, int],
    },
    total=False,
)

class SegmentImportResourceTypeDef(
    _RequiredSegmentImportResourceTypeDef, _OptionalSegmentImportResourceTypeDef
):
    pass

SegmentLocationTypeDef = TypedDict(
    "SegmentLocationTypeDef",
    {
        "Country": "SetDimensionTypeDef",
        "GPSPoint": "GPSPointDimensionTypeDef",
    },
    total=False,
)

_RequiredSegmentReferenceTypeDef = TypedDict(
    "_RequiredSegmentReferenceTypeDef",
    {
        "Id": str,
    },
)
_OptionalSegmentReferenceTypeDef = TypedDict(
    "_OptionalSegmentReferenceTypeDef",
    {
        "Version": int,
    },
    total=False,
)

class SegmentReferenceTypeDef(_RequiredSegmentReferenceTypeDef, _OptionalSegmentReferenceTypeDef):
    pass

_RequiredSegmentResponseTypeDef = TypedDict(
    "_RequiredSegmentResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "CreationDate": str,
        "Id": str,
        "SegmentType": SegmentTypeType,
    },
)
_OptionalSegmentResponseTypeDef = TypedDict(
    "_OptionalSegmentResponseTypeDef",
    {
        "Dimensions": "SegmentDimensionsTypeDef",
        "ImportDefinition": "SegmentImportResourceTypeDef",
        "LastModifiedDate": str,
        "Name": str,
        "SegmentGroups": "SegmentGroupListTypeDef",
        "tags": Dict[str, str],
        "Version": int,
    },
    total=False,
)

class SegmentResponseTypeDef(_RequiredSegmentResponseTypeDef, _OptionalSegmentResponseTypeDef):
    pass

_RequiredSegmentsResponseTypeDef = TypedDict(
    "_RequiredSegmentsResponseTypeDef",
    {
        "Item": List["SegmentResponseTypeDef"],
    },
)
_OptionalSegmentsResponseTypeDef = TypedDict(
    "_OptionalSegmentsResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class SegmentsResponseTypeDef(_RequiredSegmentsResponseTypeDef, _OptionalSegmentsResponseTypeDef):
    pass

SendMessagesRequestRequestTypeDef = TypedDict(
    "SendMessagesRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "MessageRequest": "MessageRequestTypeDef",
    },
)

SendMessagesResponseTypeDef = TypedDict(
    "SendMessagesResponseTypeDef",
    {
        "MessageResponse": "MessageResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendUsersMessageRequestTypeDef = TypedDict(
    "_RequiredSendUsersMessageRequestTypeDef",
    {
        "MessageConfiguration": "DirectMessageConfigurationTypeDef",
        "Users": Dict[str, "EndpointSendConfigurationTypeDef"],
    },
)
_OptionalSendUsersMessageRequestTypeDef = TypedDict(
    "_OptionalSendUsersMessageRequestTypeDef",
    {
        "Context": Dict[str, str],
        "TemplateConfiguration": "TemplateConfigurationTypeDef",
        "TraceId": str,
    },
    total=False,
)

class SendUsersMessageRequestTypeDef(
    _RequiredSendUsersMessageRequestTypeDef, _OptionalSendUsersMessageRequestTypeDef
):
    pass

_RequiredSendUsersMessageResponseTypeDef = TypedDict(
    "_RequiredSendUsersMessageResponseTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalSendUsersMessageResponseTypeDef = TypedDict(
    "_OptionalSendUsersMessageResponseTypeDef",
    {
        "RequestId": str,
        "Result": Dict[str, Dict[str, "EndpointMessageResultTypeDef"]],
    },
    total=False,
)

class SendUsersMessageResponseTypeDef(
    _RequiredSendUsersMessageResponseTypeDef, _OptionalSendUsersMessageResponseTypeDef
):
    pass

SendUsersMessagesRequestRequestTypeDef = TypedDict(
    "SendUsersMessagesRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SendUsersMessageRequest": "SendUsersMessageRequestTypeDef",
    },
)

SendUsersMessagesResponseTypeDef = TypedDict(
    "SendUsersMessagesResponseTypeDef",
    {
        "SendUsersMessageResponse": "SendUsersMessageResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSessionTypeDef = TypedDict(
    "_RequiredSessionTypeDef",
    {
        "Id": str,
        "StartTimestamp": str,
    },
)
_OptionalSessionTypeDef = TypedDict(
    "_OptionalSessionTypeDef",
    {
        "Duration": int,
        "StopTimestamp": str,
    },
    total=False,
)

class SessionTypeDef(_RequiredSessionTypeDef, _OptionalSessionTypeDef):
    pass

_RequiredSetDimensionTypeDef = TypedDict(
    "_RequiredSetDimensionTypeDef",
    {
        "Values": List[str],
    },
)
_OptionalSetDimensionTypeDef = TypedDict(
    "_OptionalSetDimensionTypeDef",
    {
        "DimensionType": DimensionTypeType,
    },
    total=False,
)

class SetDimensionTypeDef(_RequiredSetDimensionTypeDef, _OptionalSetDimensionTypeDef):
    pass

SimpleConditionTypeDef = TypedDict(
    "SimpleConditionTypeDef",
    {
        "EventCondition": "EventConditionTypeDef",
        "SegmentCondition": "SegmentConditionTypeDef",
        "SegmentDimensions": "SegmentDimensionsTypeDef",
    },
    total=False,
)

SimpleEmailPartTypeDef = TypedDict(
    "SimpleEmailPartTypeDef",
    {
        "Charset": str,
        "Data": str,
    },
    total=False,
)

SimpleEmailTypeDef = TypedDict(
    "SimpleEmailTypeDef",
    {
        "HtmlPart": "SimpleEmailPartTypeDef",
        "Subject": "SimpleEmailPartTypeDef",
        "TextPart": "SimpleEmailPartTypeDef",
    },
    total=False,
)

StartConditionTypeDef = TypedDict(
    "StartConditionTypeDef",
    {
        "Description": str,
        "EventStartCondition": "EventStartConditionTypeDef",
        "SegmentStartCondition": "SegmentConditionTypeDef",
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagsModel": "TagsModelTypeDef",
    },
)

TagsModelTypeDef = TypedDict(
    "TagsModelTypeDef",
    {
        "tags": Dict[str, str],
    },
)

TemplateActiveVersionRequestTypeDef = TypedDict(
    "TemplateActiveVersionRequestTypeDef",
    {
        "Version": str,
    },
    total=False,
)

TemplateConfigurationTypeDef = TypedDict(
    "TemplateConfigurationTypeDef",
    {
        "EmailTemplate": "TemplateTypeDef",
        "PushTemplate": "TemplateTypeDef",
        "SMSTemplate": "TemplateTypeDef",
        "VoiceTemplate": "TemplateTypeDef",
    },
    total=False,
)

_RequiredTemplateResponseTypeDef = TypedDict(
    "_RequiredTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": TemplateTypeType,
    },
)
_OptionalTemplateResponseTypeDef = TypedDict(
    "_OptionalTemplateResponseTypeDef",
    {
        "Arn": str,
        "DefaultSubstitutions": str,
        "tags": Dict[str, str],
        "TemplateDescription": str,
        "Version": str,
    },
    total=False,
)

class TemplateResponseTypeDef(_RequiredTemplateResponseTypeDef, _OptionalTemplateResponseTypeDef):
    pass

TemplateTypeDef = TypedDict(
    "TemplateTypeDef",
    {
        "Name": str,
        "Version": str,
    },
    total=False,
)

_RequiredTemplateVersionResponseTypeDef = TypedDict(
    "_RequiredTemplateVersionResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": str,
    },
)
_OptionalTemplateVersionResponseTypeDef = TypedDict(
    "_OptionalTemplateVersionResponseTypeDef",
    {
        "DefaultSubstitutions": str,
        "TemplateDescription": str,
        "Version": str,
    },
    total=False,
)

class TemplateVersionResponseTypeDef(
    _RequiredTemplateVersionResponseTypeDef, _OptionalTemplateVersionResponseTypeDef
):
    pass

_RequiredTemplateVersionsResponseTypeDef = TypedDict(
    "_RequiredTemplateVersionsResponseTypeDef",
    {
        "Item": List["TemplateVersionResponseTypeDef"],
    },
)
_OptionalTemplateVersionsResponseTypeDef = TypedDict(
    "_OptionalTemplateVersionsResponseTypeDef",
    {
        "Message": str,
        "NextToken": str,
        "RequestID": str,
    },
    total=False,
)

class TemplateVersionsResponseTypeDef(
    _RequiredTemplateVersionsResponseTypeDef, _OptionalTemplateVersionsResponseTypeDef
):
    pass

_RequiredTemplatesResponseTypeDef = TypedDict(
    "_RequiredTemplatesResponseTypeDef",
    {
        "Item": List["TemplateResponseTypeDef"],
    },
)
_OptionalTemplatesResponseTypeDef = TypedDict(
    "_OptionalTemplatesResponseTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class TemplatesResponseTypeDef(
    _RequiredTemplatesResponseTypeDef, _OptionalTemplatesResponseTypeDef
):
    pass

_RequiredTreatmentResourceTypeDef = TypedDict(
    "_RequiredTreatmentResourceTypeDef",
    {
        "Id": str,
        "SizePercent": int,
    },
)
_OptionalTreatmentResourceTypeDef = TypedDict(
    "_OptionalTreatmentResourceTypeDef",
    {
        "CustomDeliveryConfiguration": "CustomDeliveryConfigurationTypeDef",
        "MessageConfiguration": "MessageConfigurationTypeDef",
        "Schedule": "ScheduleTypeDef",
        "State": "CampaignStateTypeDef",
        "TemplateConfiguration": "TemplateConfigurationTypeDef",
        "TreatmentDescription": str,
        "TreatmentName": str,
    },
    total=False,
)

class TreatmentResourceTypeDef(
    _RequiredTreatmentResourceTypeDef, _OptionalTreatmentResourceTypeDef
):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateAdmChannelRequestRequestTypeDef = TypedDict(
    "UpdateAdmChannelRequestRequestTypeDef",
    {
        "ADMChannelRequest": "ADMChannelRequestTypeDef",
        "ApplicationId": str,
    },
)

UpdateAdmChannelResponseTypeDef = TypedDict(
    "UpdateAdmChannelResponseTypeDef",
    {
        "ADMChannelResponse": "ADMChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApnsChannelRequestRequestTypeDef = TypedDict(
    "UpdateApnsChannelRequestRequestTypeDef",
    {
        "APNSChannelRequest": "APNSChannelRequestTypeDef",
        "ApplicationId": str,
    },
)

UpdateApnsChannelResponseTypeDef = TypedDict(
    "UpdateApnsChannelResponseTypeDef",
    {
        "APNSChannelResponse": "APNSChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApnsSandboxChannelRequestRequestTypeDef = TypedDict(
    "UpdateApnsSandboxChannelRequestRequestTypeDef",
    {
        "APNSSandboxChannelRequest": "APNSSandboxChannelRequestTypeDef",
        "ApplicationId": str,
    },
)

UpdateApnsSandboxChannelResponseTypeDef = TypedDict(
    "UpdateApnsSandboxChannelResponseTypeDef",
    {
        "APNSSandboxChannelResponse": "APNSSandboxChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApnsVoipChannelRequestRequestTypeDef = TypedDict(
    "UpdateApnsVoipChannelRequestRequestTypeDef",
    {
        "APNSVoipChannelRequest": "APNSVoipChannelRequestTypeDef",
        "ApplicationId": str,
    },
)

UpdateApnsVoipChannelResponseTypeDef = TypedDict(
    "UpdateApnsVoipChannelResponseTypeDef",
    {
        "APNSVoipChannelResponse": "APNSVoipChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApnsVoipSandboxChannelRequestRequestTypeDef = TypedDict(
    "UpdateApnsVoipSandboxChannelRequestRequestTypeDef",
    {
        "APNSVoipSandboxChannelRequest": "APNSVoipSandboxChannelRequestTypeDef",
        "ApplicationId": str,
    },
)

UpdateApnsVoipSandboxChannelResponseTypeDef = TypedDict(
    "UpdateApnsVoipSandboxChannelResponseTypeDef",
    {
        "APNSVoipSandboxChannelResponse": "APNSVoipSandboxChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApplicationSettingsRequestRequestTypeDef = TypedDict(
    "UpdateApplicationSettingsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "WriteApplicationSettingsRequest": "WriteApplicationSettingsRequestTypeDef",
    },
)

UpdateApplicationSettingsResponseTypeDef = TypedDict(
    "UpdateApplicationSettingsResponseTypeDef",
    {
        "ApplicationSettingsResource": "ApplicationSettingsResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAttributesRequestTypeDef = TypedDict(
    "UpdateAttributesRequestTypeDef",
    {
        "Blacklist": List[str],
    },
    total=False,
)

UpdateBaiduChannelRequestRequestTypeDef = TypedDict(
    "UpdateBaiduChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "BaiduChannelRequest": "BaiduChannelRequestTypeDef",
    },
)

UpdateBaiduChannelResponseTypeDef = TypedDict(
    "UpdateBaiduChannelResponseTypeDef",
    {
        "BaiduChannelResponse": "BaiduChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCampaignRequestRequestTypeDef = TypedDict(
    "UpdateCampaignRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "CampaignId": str,
        "WriteCampaignRequest": "WriteCampaignRequestTypeDef",
    },
)

UpdateCampaignResponseTypeDef = TypedDict(
    "UpdateCampaignResponseTypeDef",
    {
        "CampaignResponse": "CampaignResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEmailChannelRequestRequestTypeDef = TypedDict(
    "UpdateEmailChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EmailChannelRequest": "EmailChannelRequestTypeDef",
    },
)

UpdateEmailChannelResponseTypeDef = TypedDict(
    "UpdateEmailChannelResponseTypeDef",
    {
        "EmailChannelResponse": "EmailChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEmailTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEmailTemplateRequestRequestTypeDef",
    {
        "EmailTemplateRequest": "EmailTemplateRequestTypeDef",
        "TemplateName": str,
    },
)
_OptionalUpdateEmailTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEmailTemplateRequestRequestTypeDef",
    {
        "CreateNewVersion": bool,
        "Version": str,
    },
    total=False,
)

class UpdateEmailTemplateRequestRequestTypeDef(
    _RequiredUpdateEmailTemplateRequestRequestTypeDef,
    _OptionalUpdateEmailTemplateRequestRequestTypeDef,
):
    pass

UpdateEmailTemplateResponseTypeDef = TypedDict(
    "UpdateEmailTemplateResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEndpointRequestRequestTypeDef = TypedDict(
    "UpdateEndpointRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EndpointId": str,
        "EndpointRequest": "EndpointRequestTypeDef",
    },
)

UpdateEndpointResponseTypeDef = TypedDict(
    "UpdateEndpointResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEndpointsBatchRequestRequestTypeDef = TypedDict(
    "UpdateEndpointsBatchRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EndpointBatchRequest": "EndpointBatchRequestTypeDef",
    },
)

UpdateEndpointsBatchResponseTypeDef = TypedDict(
    "UpdateEndpointsBatchResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGcmChannelRequestRequestTypeDef = TypedDict(
    "UpdateGcmChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "GCMChannelRequest": "GCMChannelRequestTypeDef",
    },
)

UpdateGcmChannelResponseTypeDef = TypedDict(
    "UpdateGcmChannelResponseTypeDef",
    {
        "GCMChannelResponse": "GCMChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateJourneyRequestRequestTypeDef = TypedDict(
    "UpdateJourneyRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
        "WriteJourneyRequest": "WriteJourneyRequestTypeDef",
    },
)

UpdateJourneyResponseTypeDef = TypedDict(
    "UpdateJourneyResponseTypeDef",
    {
        "JourneyResponse": "JourneyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateJourneyStateRequestRequestTypeDef = TypedDict(
    "UpdateJourneyStateRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "JourneyId": str,
        "JourneyStateRequest": "JourneyStateRequestTypeDef",
    },
)

UpdateJourneyStateResponseTypeDef = TypedDict(
    "UpdateJourneyStateResponseTypeDef",
    {
        "JourneyResponse": "JourneyResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePushTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePushTemplateRequestRequestTypeDef",
    {
        "PushNotificationTemplateRequest": "PushNotificationTemplateRequestTypeDef",
        "TemplateName": str,
    },
)
_OptionalUpdatePushTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePushTemplateRequestRequestTypeDef",
    {
        "CreateNewVersion": bool,
        "Version": str,
    },
    total=False,
)

class UpdatePushTemplateRequestRequestTypeDef(
    _RequiredUpdatePushTemplateRequestRequestTypeDef,
    _OptionalUpdatePushTemplateRequestRequestTypeDef,
):
    pass

UpdatePushTemplateResponseTypeDef = TypedDict(
    "UpdatePushTemplateResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRecommenderConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateRecommenderConfigurationRequestRequestTypeDef",
    {
        "RecommenderId": str,
        "UpdateRecommenderConfiguration": "UpdateRecommenderConfigurationTypeDef",
    },
)

UpdateRecommenderConfigurationResponseTypeDef = TypedDict(
    "UpdateRecommenderConfigurationResponseTypeDef",
    {
        "RecommenderConfigurationResponse": "RecommenderConfigurationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRecommenderConfigurationTypeDef = TypedDict(
    "_RequiredUpdateRecommenderConfigurationTypeDef",
    {
        "RecommendationProviderRoleArn": str,
        "RecommendationProviderUri": str,
    },
)
_OptionalUpdateRecommenderConfigurationTypeDef = TypedDict(
    "_OptionalUpdateRecommenderConfigurationTypeDef",
    {
        "Attributes": Dict[str, str],
        "Description": str,
        "Name": str,
        "RecommendationProviderIdType": str,
        "RecommendationTransformerUri": str,
        "RecommendationsDisplayName": str,
        "RecommendationsPerMessage": int,
    },
    total=False,
)

class UpdateRecommenderConfigurationTypeDef(
    _RequiredUpdateRecommenderConfigurationTypeDef, _OptionalUpdateRecommenderConfigurationTypeDef
):
    pass

UpdateSegmentRequestRequestTypeDef = TypedDict(
    "UpdateSegmentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SegmentId": str,
        "WriteSegmentRequest": "WriteSegmentRequestTypeDef",
    },
)

UpdateSegmentResponseTypeDef = TypedDict(
    "UpdateSegmentResponseTypeDef",
    {
        "SegmentResponse": "SegmentResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSmsChannelRequestRequestTypeDef = TypedDict(
    "UpdateSmsChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SMSChannelRequest": "SMSChannelRequestTypeDef",
    },
)

UpdateSmsChannelResponseTypeDef = TypedDict(
    "UpdateSmsChannelResponseTypeDef",
    {
        "SMSChannelResponse": "SMSChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSmsTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSmsTemplateRequestRequestTypeDef",
    {
        "SMSTemplateRequest": "SMSTemplateRequestTypeDef",
        "TemplateName": str,
    },
)
_OptionalUpdateSmsTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSmsTemplateRequestRequestTypeDef",
    {
        "CreateNewVersion": bool,
        "Version": str,
    },
    total=False,
)

class UpdateSmsTemplateRequestRequestTypeDef(
    _RequiredUpdateSmsTemplateRequestRequestTypeDef, _OptionalUpdateSmsTemplateRequestRequestTypeDef
):
    pass

UpdateSmsTemplateResponseTypeDef = TypedDict(
    "UpdateSmsTemplateResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTemplateActiveVersionRequestRequestTypeDef = TypedDict(
    "UpdateTemplateActiveVersionRequestRequestTypeDef",
    {
        "TemplateActiveVersionRequest": "TemplateActiveVersionRequestTypeDef",
        "TemplateName": str,
        "TemplateType": str,
    },
)

UpdateTemplateActiveVersionResponseTypeDef = TypedDict(
    "UpdateTemplateActiveVersionResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVoiceChannelRequestRequestTypeDef = TypedDict(
    "UpdateVoiceChannelRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "VoiceChannelRequest": "VoiceChannelRequestTypeDef",
    },
)

UpdateVoiceChannelResponseTypeDef = TypedDict(
    "UpdateVoiceChannelResponseTypeDef",
    {
        "VoiceChannelResponse": "VoiceChannelResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateVoiceTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateVoiceTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "VoiceTemplateRequest": "VoiceTemplateRequestTypeDef",
    },
)
_OptionalUpdateVoiceTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateVoiceTemplateRequestRequestTypeDef",
    {
        "CreateNewVersion": bool,
        "Version": str,
    },
    total=False,
)

class UpdateVoiceTemplateRequestRequestTypeDef(
    _RequiredUpdateVoiceTemplateRequestRequestTypeDef,
    _OptionalUpdateVoiceTemplateRequestRequestTypeDef,
):
    pass

UpdateVoiceTemplateResponseTypeDef = TypedDict(
    "UpdateVoiceTemplateResponseTypeDef",
    {
        "MessageBody": "MessageBodyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VoiceChannelRequestTypeDef = TypedDict(
    "VoiceChannelRequestTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

_RequiredVoiceChannelResponseTypeDef = TypedDict(
    "_RequiredVoiceChannelResponseTypeDef",
    {
        "Platform": str,
    },
)
_OptionalVoiceChannelResponseTypeDef = TypedDict(
    "_OptionalVoiceChannelResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "Enabled": bool,
        "HasCredential": bool,
        "Id": str,
        "IsArchived": bool,
        "LastModifiedBy": str,
        "LastModifiedDate": str,
        "Version": int,
    },
    total=False,
)

class VoiceChannelResponseTypeDef(
    _RequiredVoiceChannelResponseTypeDef, _OptionalVoiceChannelResponseTypeDef
):
    pass

VoiceMessageTypeDef = TypedDict(
    "VoiceMessageTypeDef",
    {
        "Body": str,
        "LanguageCode": str,
        "OriginationNumber": str,
        "Substitutions": Dict[str, List[str]],
        "VoiceId": str,
    },
    total=False,
)

VoiceTemplateRequestTypeDef = TypedDict(
    "VoiceTemplateRequestTypeDef",
    {
        "Body": str,
        "DefaultSubstitutions": str,
        "LanguageCode": str,
        "tags": Dict[str, str],
        "TemplateDescription": str,
        "VoiceId": str,
    },
    total=False,
)

_RequiredVoiceTemplateResponseTypeDef = TypedDict(
    "_RequiredVoiceTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": TemplateTypeType,
    },
)
_OptionalVoiceTemplateResponseTypeDef = TypedDict(
    "_OptionalVoiceTemplateResponseTypeDef",
    {
        "Arn": str,
        "Body": str,
        "DefaultSubstitutions": str,
        "LanguageCode": str,
        "tags": Dict[str, str],
        "TemplateDescription": str,
        "Version": str,
        "VoiceId": str,
    },
    total=False,
)

class VoiceTemplateResponseTypeDef(
    _RequiredVoiceTemplateResponseTypeDef, _OptionalVoiceTemplateResponseTypeDef
):
    pass

WaitActivityTypeDef = TypedDict(
    "WaitActivityTypeDef",
    {
        "NextActivity": str,
        "WaitTime": "WaitTimeTypeDef",
    },
    total=False,
)

WaitTimeTypeDef = TypedDict(
    "WaitTimeTypeDef",
    {
        "WaitFor": str,
        "WaitUntil": str,
    },
    total=False,
)

WriteApplicationSettingsRequestTypeDef = TypedDict(
    "WriteApplicationSettingsRequestTypeDef",
    {
        "CampaignHook": "CampaignHookTypeDef",
        "CloudWatchMetricsEnabled": bool,
        "EventTaggingEnabled": bool,
        "Limits": "CampaignLimitsTypeDef",
        "QuietTime": "QuietTimeTypeDef",
    },
    total=False,
)

WriteCampaignRequestTypeDef = TypedDict(
    "WriteCampaignRequestTypeDef",
    {
        "AdditionalTreatments": List["WriteTreatmentResourceTypeDef"],
        "CustomDeliveryConfiguration": "CustomDeliveryConfigurationTypeDef",
        "Description": str,
        "HoldoutPercent": int,
        "Hook": "CampaignHookTypeDef",
        "IsPaused": bool,
        "Limits": "CampaignLimitsTypeDef",
        "MessageConfiguration": "MessageConfigurationTypeDef",
        "Name": str,
        "Schedule": "ScheduleTypeDef",
        "SegmentId": str,
        "SegmentVersion": int,
        "tags": Dict[str, str],
        "TemplateConfiguration": "TemplateConfigurationTypeDef",
        "TreatmentDescription": str,
        "TreatmentName": str,
    },
    total=False,
)

WriteEventStreamTypeDef = TypedDict(
    "WriteEventStreamTypeDef",
    {
        "DestinationStreamArn": str,
        "RoleArn": str,
    },
)

_RequiredWriteJourneyRequestTypeDef = TypedDict(
    "_RequiredWriteJourneyRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalWriteJourneyRequestTypeDef = TypedDict(
    "_OptionalWriteJourneyRequestTypeDef",
    {
        "Activities": Dict[str, "ActivityTypeDef"],
        "CreationDate": str,
        "LastModifiedDate": str,
        "Limits": "JourneyLimitsTypeDef",
        "LocalTime": bool,
        "QuietTime": "QuietTimeTypeDef",
        "RefreshFrequency": str,
        "Schedule": "JourneyScheduleTypeDef",
        "StartActivity": str,
        "StartCondition": "StartConditionTypeDef",
        "State": StateType,
        "WaitForQuietTime": bool,
        "RefreshOnSegmentUpdate": bool,
    },
    total=False,
)

class WriteJourneyRequestTypeDef(
    _RequiredWriteJourneyRequestTypeDef, _OptionalWriteJourneyRequestTypeDef
):
    pass

WriteSegmentRequestTypeDef = TypedDict(
    "WriteSegmentRequestTypeDef",
    {
        "Dimensions": "SegmentDimensionsTypeDef",
        "Name": str,
        "SegmentGroups": "SegmentGroupListTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredWriteTreatmentResourceTypeDef = TypedDict(
    "_RequiredWriteTreatmentResourceTypeDef",
    {
        "SizePercent": int,
    },
)
_OptionalWriteTreatmentResourceTypeDef = TypedDict(
    "_OptionalWriteTreatmentResourceTypeDef",
    {
        "CustomDeliveryConfiguration": "CustomDeliveryConfigurationTypeDef",
        "MessageConfiguration": "MessageConfigurationTypeDef",
        "Schedule": "ScheduleTypeDef",
        "TemplateConfiguration": "TemplateConfigurationTypeDef",
        "TreatmentDescription": str,
        "TreatmentName": str,
    },
    total=False,
)

class WriteTreatmentResourceTypeDef(
    _RequiredWriteTreatmentResourceTypeDef, _OptionalWriteTreatmentResourceTypeDef
):
    pass
