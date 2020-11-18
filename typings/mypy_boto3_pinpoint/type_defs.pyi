"""
Main interface for pinpoint service type definitions.

Usage::

    ```python
    from mypy_boto3_pinpoint.type_defs import ADMChannelResponseTypeDef

    data: ADMChannelResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ADMChannelResponseTypeDef",
    "ADMMessageTypeDef",
    "APNSChannelResponseTypeDef",
    "APNSMessageTypeDef",
    "APNSPushNotificationTemplateTypeDef",
    "APNSSandboxChannelResponseTypeDef",
    "APNSVoipChannelResponseTypeDef",
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
    "CreateTemplateMessageBodyTypeDef",
    "CustomDeliveryConfigurationTypeDef",
    "CustomMessageActivityTypeDef",
    "DefaultMessageTypeDef",
    "DefaultPushNotificationMessageTypeDef",
    "DefaultPushNotificationTemplateTypeDef",
    "DirectMessageConfigurationTypeDef",
    "EmailChannelResponseTypeDef",
    "EmailMessageActivityTypeDef",
    "EmailMessageTypeDef",
    "EmailTemplateResponseTypeDef",
    "EndpointBatchItemTypeDef",
    "EndpointDemographicTypeDef",
    "EndpointItemResponseTypeDef",
    "EndpointLocationTypeDef",
    "EndpointMessageResultTypeDef",
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
    "EventsResponseTypeDef",
    "ExportJobResourceTypeDef",
    "ExportJobResponseTypeDef",
    "ExportJobsResponseTypeDef",
    "GCMChannelResponseTypeDef",
    "GCMMessageTypeDef",
    "GPSCoordinatesTypeDef",
    "GPSPointDimensionTypeDef",
    "HoldoutActivityTypeDef",
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
    "JourneysResponseTypeDef",
    "ListRecommenderConfigurationsResponseTypeDef",
    "MessageBodyTypeDef",
    "MessageConfigurationTypeDef",
    "MessageResponseTypeDef",
    "MessageResultTypeDef",
    "MessageTypeDef",
    "MetricDimensionTypeDef",
    "MultiConditionalBranchTypeDef",
    "MultiConditionalSplitActivityTypeDef",
    "NumberValidateResponseTypeDef",
    "PublicEndpointTypeDef",
    "PushMessageActivityTypeDef",
    "PushNotificationTemplateResponseTypeDef",
    "QuietTimeTypeDef",
    "RandomSplitActivityTypeDef",
    "RandomSplitEntryTypeDef",
    "RawEmailTypeDef",
    "RecencyDimensionTypeDef",
    "RecommenderConfigurationResponseTypeDef",
    "ResultRowTypeDef",
    "ResultRowValueTypeDef",
    "SMSChannelResponseTypeDef",
    "SMSMessageActivityTypeDef",
    "SMSMessageTypeDef",
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
    "SendUsersMessageResponseTypeDef",
    "SessionTypeDef",
    "SetDimensionTypeDef",
    "SimpleConditionTypeDef",
    "SimpleEmailPartTypeDef",
    "SimpleEmailTypeDef",
    "StartConditionTypeDef",
    "TagsModelTypeDef",
    "TemplateConfigurationTypeDef",
    "TemplateResponseTypeDef",
    "TemplateTypeDef",
    "TemplateVersionResponseTypeDef",
    "TemplateVersionsResponseTypeDef",
    "TemplatesResponseTypeDef",
    "TreatmentResourceTypeDef",
    "VoiceChannelResponseTypeDef",
    "VoiceMessageTypeDef",
    "VoiceTemplateResponseTypeDef",
    "WaitActivityTypeDef",
    "WaitTimeTypeDef",
    "WriteTreatmentResourceTypeDef",
    "ADMChannelRequestTypeDef",
    "APNSChannelRequestTypeDef",
    "APNSSandboxChannelRequestTypeDef",
    "APNSVoipChannelRequestTypeDef",
    "APNSVoipSandboxChannelRequestTypeDef",
    "BaiduChannelRequestTypeDef",
    "CreateAppResponseTypeDef",
    "CreateApplicationRequestTypeDef",
    "CreateCampaignResponseTypeDef",
    "CreateEmailTemplateResponseTypeDef",
    "CreateExportJobResponseTypeDef",
    "CreateImportJobResponseTypeDef",
    "CreateJourneyResponseTypeDef",
    "CreatePushTemplateResponseTypeDef",
    "CreateRecommenderConfigurationResponseTypeDef",
    "CreateRecommenderConfigurationTypeDef",
    "CreateSegmentResponseTypeDef",
    "CreateSmsTemplateResponseTypeDef",
    "CreateVoiceTemplateResponseTypeDef",
    "DeleteAdmChannelResponseTypeDef",
    "DeleteApnsChannelResponseTypeDef",
    "DeleteApnsSandboxChannelResponseTypeDef",
    "DeleteApnsVoipChannelResponseTypeDef",
    "DeleteApnsVoipSandboxChannelResponseTypeDef",
    "DeleteAppResponseTypeDef",
    "DeleteBaiduChannelResponseTypeDef",
    "DeleteCampaignResponseTypeDef",
    "DeleteEmailChannelResponseTypeDef",
    "DeleteEmailTemplateResponseTypeDef",
    "DeleteEndpointResponseTypeDef",
    "DeleteEventStreamResponseTypeDef",
    "DeleteGcmChannelResponseTypeDef",
    "DeleteJourneyResponseTypeDef",
    "DeletePushTemplateResponseTypeDef",
    "DeleteRecommenderConfigurationResponseTypeDef",
    "DeleteSegmentResponseTypeDef",
    "DeleteSmsChannelResponseTypeDef",
    "DeleteSmsTemplateResponseTypeDef",
    "DeleteUserEndpointsResponseTypeDef",
    "DeleteVoiceChannelResponseTypeDef",
    "DeleteVoiceTemplateResponseTypeDef",
    "EmailChannelRequestTypeDef",
    "EmailTemplateRequestTypeDef",
    "EndpointBatchRequestTypeDef",
    "EndpointRequestTypeDef",
    "EventsRequestTypeDef",
    "ExportJobRequestTypeDef",
    "GCMChannelRequestTypeDef",
    "GetAdmChannelResponseTypeDef",
    "GetApnsChannelResponseTypeDef",
    "GetApnsSandboxChannelResponseTypeDef",
    "GetApnsVoipChannelResponseTypeDef",
    "GetApnsVoipSandboxChannelResponseTypeDef",
    "GetAppResponseTypeDef",
    "GetApplicationDateRangeKpiResponseTypeDef",
    "GetApplicationSettingsResponseTypeDef",
    "GetAppsResponseTypeDef",
    "GetBaiduChannelResponseTypeDef",
    "GetCampaignActivitiesResponseTypeDef",
    "GetCampaignDateRangeKpiResponseTypeDef",
    "GetCampaignResponseTypeDef",
    "GetCampaignVersionResponseTypeDef",
    "GetCampaignVersionsResponseTypeDef",
    "GetCampaignsResponseTypeDef",
    "GetChannelsResponseTypeDef",
    "GetEmailChannelResponseTypeDef",
    "GetEmailTemplateResponseTypeDef",
    "GetEndpointResponseTypeDef",
    "GetEventStreamResponseTypeDef",
    "GetExportJobResponseTypeDef",
    "GetExportJobsResponseTypeDef",
    "GetGcmChannelResponseTypeDef",
    "GetImportJobResponseTypeDef",
    "GetImportJobsResponseTypeDef",
    "GetJourneyDateRangeKpiResponseTypeDef",
    "GetJourneyExecutionActivityMetricsResponseTypeDef",
    "GetJourneyExecutionMetricsResponseTypeDef",
    "GetJourneyResponseTypeDef",
    "GetPushTemplateResponseTypeDef",
    "GetRecommenderConfigurationResponseTypeDef",
    "GetRecommenderConfigurationsResponseTypeDef",
    "GetSegmentExportJobsResponseTypeDef",
    "GetSegmentImportJobsResponseTypeDef",
    "GetSegmentResponseTypeDef",
    "GetSegmentVersionResponseTypeDef",
    "GetSegmentVersionsResponseTypeDef",
    "GetSegmentsResponseTypeDef",
    "GetSmsChannelResponseTypeDef",
    "GetSmsTemplateResponseTypeDef",
    "GetUserEndpointsResponseTypeDef",
    "GetVoiceChannelResponseTypeDef",
    "GetVoiceTemplateResponseTypeDef",
    "ImportJobRequestTypeDef",
    "JourneyStateRequestTypeDef",
    "ListJourneysResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTemplateVersionsResponseTypeDef",
    "ListTemplatesResponseTypeDef",
    "MessageRequestTypeDef",
    "NumberValidateRequestTypeDef",
    "PhoneNumberValidateResponseTypeDef",
    "PushNotificationTemplateRequestTypeDef",
    "PutEventStreamResponseTypeDef",
    "PutEventsResponseTypeDef",
    "RemoveAttributesResponseTypeDef",
    "SMSChannelRequestTypeDef",
    "SMSTemplateRequestTypeDef",
    "SendMessagesResponseTypeDef",
    "SendUsersMessageRequestTypeDef",
    "SendUsersMessagesResponseTypeDef",
    "TemplateActiveVersionRequestTypeDef",
    "UpdateAdmChannelResponseTypeDef",
    "UpdateApnsChannelResponseTypeDef",
    "UpdateApnsSandboxChannelResponseTypeDef",
    "UpdateApnsVoipChannelResponseTypeDef",
    "UpdateApnsVoipSandboxChannelResponseTypeDef",
    "UpdateApplicationSettingsResponseTypeDef",
    "UpdateAttributesRequestTypeDef",
    "UpdateBaiduChannelResponseTypeDef",
    "UpdateCampaignResponseTypeDef",
    "UpdateEmailChannelResponseTypeDef",
    "UpdateEmailTemplateResponseTypeDef",
    "UpdateEndpointResponseTypeDef",
    "UpdateEndpointsBatchResponseTypeDef",
    "UpdateGcmChannelResponseTypeDef",
    "UpdateJourneyResponseTypeDef",
    "UpdateJourneyStateResponseTypeDef",
    "UpdatePushTemplateResponseTypeDef",
    "UpdateRecommenderConfigurationResponseTypeDef",
    "UpdateRecommenderConfigurationTypeDef",
    "UpdateSegmentResponseTypeDef",
    "UpdateSmsChannelResponseTypeDef",
    "UpdateSmsTemplateResponseTypeDef",
    "UpdateTemplateActiveVersionResponseTypeDef",
    "UpdateVoiceChannelResponseTypeDef",
    "UpdateVoiceTemplateResponseTypeDef",
    "VoiceChannelRequestTypeDef",
    "VoiceTemplateRequestTypeDef",
    "WriteApplicationSettingsRequestTypeDef",
    "WriteCampaignRequestTypeDef",
    "WriteEventStreamTypeDef",
    "WriteJourneyRequestTypeDef",
    "WriteSegmentRequestTypeDef",
)

_RequiredADMChannelResponseTypeDef = TypedDict(
    "_RequiredADMChannelResponseTypeDef", {"Platform": str}
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
        "Action": Literal["OPEN_APP", "DEEP_LINK", "URL"],
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

_RequiredAPNSChannelResponseTypeDef = TypedDict(
    "_RequiredAPNSChannelResponseTypeDef", {"Platform": str}
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
        "Action": Literal["OPEN_APP", "DEEP_LINK", "URL"],
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
        "Action": Literal["OPEN_APP", "DEEP_LINK", "URL"],
        "Body": str,
        "MediaUrl": str,
        "RawContent": str,
        "Sound": str,
        "Title": str,
        "Url": str,
    },
    total=False,
)

_RequiredAPNSSandboxChannelResponseTypeDef = TypedDict(
    "_RequiredAPNSSandboxChannelResponseTypeDef", {"Platform": str}
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


_RequiredAPNSVoipChannelResponseTypeDef = TypedDict(
    "_RequiredAPNSVoipChannelResponseTypeDef", {"Platform": str}
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


_RequiredAPNSVoipSandboxChannelResponseTypeDef = TypedDict(
    "_RequiredAPNSVoipSandboxChannelResponseTypeDef", {"Platform": str}
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
    "_RequiredActivitiesResponseTypeDef", {"Item": List["ActivityResponseTypeDef"]}
)
_OptionalActivitiesResponseTypeDef = TypedDict(
    "_OptionalActivitiesResponseTypeDef", {"NextToken": str}, total=False
)


class ActivitiesResponseTypeDef(
    _RequiredActivitiesResponseTypeDef, _OptionalActivitiesResponseTypeDef
):
    pass


_RequiredActivityResponseTypeDef = TypedDict(
    "_RequiredActivityResponseTypeDef", {"ApplicationId": str, "CampaignId": str, "Id": str}
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
        "ChannelType": Literal[
            "PUSH",
            "GCM",
            "APNS",
            "APNS_SANDBOX",
            "APNS_VOIP",
            "APNS_VOIP_SANDBOX",
            "ADM",
            "SMS",
            "VOICE",
            "EMAIL",
            "BAIDU",
            "CUSTOM",
        ],
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
        "Action": Literal["OPEN_APP", "DEEP_LINK", "URL"],
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
    "_OptionalApplicationDateRangeKpiResponseTypeDef", {"NextToken": str}, total=False
)


class ApplicationDateRangeKpiResponseTypeDef(
    _RequiredApplicationDateRangeKpiResponseTypeDef, _OptionalApplicationDateRangeKpiResponseTypeDef
):
    pass


_RequiredApplicationResponseTypeDef = TypedDict(
    "_RequiredApplicationResponseTypeDef", {"Arn": str, "Id": str, "Name": str}
)
_OptionalApplicationResponseTypeDef = TypedDict(
    "_OptionalApplicationResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ApplicationResponseTypeDef(
    _RequiredApplicationResponseTypeDef, _OptionalApplicationResponseTypeDef
):
    pass


_RequiredApplicationSettingsResourceTypeDef = TypedDict(
    "_RequiredApplicationSettingsResourceTypeDef", {"ApplicationId": str}
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
    {"Item": List["ApplicationResponseTypeDef"], "NextToken": str},
    total=False,
)

_RequiredAttributeDimensionTypeDef = TypedDict(
    "_RequiredAttributeDimensionTypeDef", {"Values": List[str]}
)
_OptionalAttributeDimensionTypeDef = TypedDict(
    "_OptionalAttributeDimensionTypeDef",
    {"AttributeType": Literal["INCLUSIVE", "EXCLUSIVE"]},
    total=False,
)


class AttributeDimensionTypeDef(
    _RequiredAttributeDimensionTypeDef, _OptionalAttributeDimensionTypeDef
):
    pass


_RequiredAttributesResourceTypeDef = TypedDict(
    "_RequiredAttributesResourceTypeDef", {"ApplicationId": str, "AttributeType": str}
)
_OptionalAttributesResourceTypeDef = TypedDict(
    "_OptionalAttributesResourceTypeDef", {"Attributes": List[str]}, total=False
)


class AttributesResourceTypeDef(
    _RequiredAttributesResourceTypeDef, _OptionalAttributesResourceTypeDef
):
    pass


_RequiredBaiduChannelResponseTypeDef = TypedDict(
    "_RequiredBaiduChannelResponseTypeDef", {"Credential": str, "Platform": str}
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
        "Action": Literal["OPEN_APP", "DEEP_LINK", "URL"],
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

BaseKpiResultTypeDef = TypedDict("BaseKpiResultTypeDef", {"Rows": List["ResultRowTypeDef"]})

CampaignCustomMessageTypeDef = TypedDict("CampaignCustomMessageTypeDef", {"Data": str}, total=False)

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
    "_OptionalCampaignDateRangeKpiResponseTypeDef", {"NextToken": str}, total=False
)


class CampaignDateRangeKpiResponseTypeDef(
    _RequiredCampaignDateRangeKpiResponseTypeDef, _OptionalCampaignDateRangeKpiResponseTypeDef
):
    pass


CampaignEmailMessageTypeDef = TypedDict(
    "CampaignEmailMessageTypeDef",
    {"Body": str, "FromAddress": str, "HtmlBody": str, "Title": str},
    total=False,
)

CampaignEventFilterTypeDef = TypedDict(
    "CampaignEventFilterTypeDef",
    {"Dimensions": "EventDimensionsTypeDef", "FilterType": Literal["SYSTEM", "ENDPOINT"]},
)

CampaignHookTypeDef = TypedDict(
    "CampaignHookTypeDef",
    {"LambdaFunctionName": str, "Mode": Literal["DELIVERY", "FILTER"], "WebUrl": str},
    total=False,
)

CampaignLimitsTypeDef = TypedDict(
    "CampaignLimitsTypeDef",
    {"Daily": int, "MaximumDuration": int, "MessagesPerSecond": int, "Total": int},
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
    {"Body": str, "MessageType": Literal["TRANSACTIONAL", "PROMOTIONAL"], "SenderId": str},
    total=False,
)

CampaignStateTypeDef = TypedDict(
    "CampaignStateTypeDef",
    {
        "CampaignStatus": Literal[
            "SCHEDULED",
            "EXECUTING",
            "PENDING_NEXT_RUN",
            "COMPLETED",
            "PAUSED",
            "DELETED",
            "INVALID",
        ]
    },
    total=False,
)

_RequiredCampaignsResponseTypeDef = TypedDict(
    "_RequiredCampaignsResponseTypeDef", {"Item": List["CampaignResponseTypeDef"]}
)
_OptionalCampaignsResponseTypeDef = TypedDict(
    "_OptionalCampaignsResponseTypeDef", {"NextToken": str}, total=False
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
    "ChannelsResponseTypeDef", {"Channels": Dict[str, "ChannelResponseTypeDef"]}
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {"Conditions": List["SimpleConditionTypeDef"], "Operator": Literal["ALL", "ANY"]},
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

CreateTemplateMessageBodyTypeDef = TypedDict(
    "CreateTemplateMessageBodyTypeDef", {"Arn": str, "Message": str, "RequestID": str}, total=False
)

_RequiredCustomDeliveryConfigurationTypeDef = TypedDict(
    "_RequiredCustomDeliveryConfigurationTypeDef", {"DeliveryUri": str}
)
_OptionalCustomDeliveryConfigurationTypeDef = TypedDict(
    "_OptionalCustomDeliveryConfigurationTypeDef",
    {
        "EndpointTypes": List[
            Literal[
                "PUSH",
                "GCM",
                "APNS",
                "APNS_SANDBOX",
                "APNS_VOIP",
                "APNS_VOIP_SANDBOX",
                "ADM",
                "SMS",
                "VOICE",
                "EMAIL",
                "BAIDU",
                "CUSTOM",
            ]
        ]
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
        "EndpointTypes": List[
            Literal[
                "PUSH",
                "GCM",
                "APNS",
                "APNS_SANDBOX",
                "APNS_VOIP",
                "APNS_VOIP_SANDBOX",
                "ADM",
                "SMS",
                "VOICE",
                "EMAIL",
                "BAIDU",
                "CUSTOM",
            ]
        ],
        "MessageConfig": "JourneyCustomMessageTypeDef",
        "NextActivity": str,
        "TemplateName": str,
        "TemplateVersion": str,
    },
    total=False,
)

DefaultMessageTypeDef = TypedDict(
    "DefaultMessageTypeDef", {"Body": str, "Substitutions": Dict[str, List[str]]}, total=False
)

DefaultPushNotificationMessageTypeDef = TypedDict(
    "DefaultPushNotificationMessageTypeDef",
    {
        "Action": Literal["OPEN_APP", "DEEP_LINK", "URL"],
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
        "Action": Literal["OPEN_APP", "DEEP_LINK", "URL"],
        "Body": str,
        "Sound": str,
        "Title": str,
        "Url": str,
    },
    total=False,
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

_RequiredEmailChannelResponseTypeDef = TypedDict(
    "_RequiredEmailChannelResponseTypeDef", {"Platform": str}
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

_RequiredEmailTemplateResponseTypeDef = TypedDict(
    "_RequiredEmailTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": Literal["EMAIL", "SMS", "VOICE", "PUSH"],
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
        "ChannelType": Literal[
            "PUSH",
            "GCM",
            "APNS",
            "APNS_SANDBOX",
            "APNS_VOIP",
            "APNS_VOIP_SANDBOX",
            "ADM",
            "SMS",
            "VOICE",
            "EMAIL",
            "BAIDU",
            "CUSTOM",
        ],
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
    "EndpointItemResponseTypeDef", {"Message": str, "StatusCode": int}, total=False
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
        "DeliveryStatus": Literal[
            "SUCCESSFUL",
            "THROTTLED",
            "TEMPORARY_FAILURE",
            "PERMANENT_FAILURE",
            "UNKNOWN_FAILURE",
            "OPT_OUT",
            "DUPLICATE",
        ],
        "StatusCode": int,
    },
)
_OptionalEndpointMessageResultTypeDef = TypedDict(
    "_OptionalEndpointMessageResultTypeDef",
    {"Address": str, "MessageId": str, "StatusMessage": str, "UpdatedToken": str},
    total=False,
)


class EndpointMessageResultTypeDef(
    _RequiredEndpointMessageResultTypeDef, _OptionalEndpointMessageResultTypeDef
):
    pass


EndpointResponseTypeDef = TypedDict(
    "EndpointResponseTypeDef",
    {
        "Address": str,
        "ApplicationId": str,
        "Attributes": Dict[str, List[str]],
        "ChannelType": Literal[
            "PUSH",
            "GCM",
            "APNS",
            "APNS_SANDBOX",
            "APNS_VOIP",
            "APNS_VOIP_SANDBOX",
            "ADM",
            "SMS",
            "VOICE",
            "EMAIL",
            "BAIDU",
            "CUSTOM",
        ],
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
    "EndpointUserTypeDef", {"UserAttributes": Dict[str, List[str]], "UserId": str}, total=False
)

EndpointsResponseTypeDef = TypedDict(
    "EndpointsResponseTypeDef", {"Item": List["EndpointResponseTypeDef"]}
)

EventConditionTypeDef = TypedDict(
    "EventConditionTypeDef",
    {"Dimensions": "EventDimensionsTypeDef", "MessageActivity": str},
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
    {"Dimensions": "EventDimensionsTypeDef", "FilterType": Literal["SYSTEM", "ENDPOINT"]},
)

EventItemResponseTypeDef = TypedDict(
    "EventItemResponseTypeDef", {"Message": str, "StatusCode": int}, total=False
)

EventStartConditionTypeDef = TypedDict(
    "EventStartConditionTypeDef",
    {"EventFilter": "EventFilterTypeDef", "SegmentId": str},
    total=False,
)

_RequiredEventStreamTypeDef = TypedDict(
    "_RequiredEventStreamTypeDef",
    {"ApplicationId": str, "DestinationStreamArn": str, "RoleArn": str},
)
_OptionalEventStreamTypeDef = TypedDict(
    "_OptionalEventStreamTypeDef",
    {"ExternalId": str, "LastModifiedDate": str, "LastUpdatedBy": str},
    total=False,
)


class EventStreamTypeDef(_RequiredEventStreamTypeDef, _OptionalEventStreamTypeDef):
    pass


_RequiredEventTypeDef = TypedDict("_RequiredEventTypeDef", {"EventType": str, "Timestamp": str})
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
    "EventsBatchTypeDef", {"Endpoint": "PublicEndpointTypeDef", "Events": Dict[str, "EventTypeDef"]}
)

EventsResponseTypeDef = TypedDict(
    "EventsResponseTypeDef", {"Results": Dict[str, "ItemResponseTypeDef"]}, total=False
)

_RequiredExportJobResourceTypeDef = TypedDict(
    "_RequiredExportJobResourceTypeDef", {"RoleArn": str, "S3UrlPrefix": str}
)
_OptionalExportJobResourceTypeDef = TypedDict(
    "_OptionalExportJobResourceTypeDef", {"SegmentId": str, "SegmentVersion": int}, total=False
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
        "JobStatus": Literal[
            "CREATED",
            "PREPARING_FOR_INITIALIZATION",
            "INITIALIZING",
            "PROCESSING",
            "PENDING_JOB",
            "COMPLETING",
            "COMPLETED",
            "FAILING",
            "FAILED",
        ],
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
    "_RequiredExportJobsResponseTypeDef", {"Item": List["ExportJobResponseTypeDef"]}
)
_OptionalExportJobsResponseTypeDef = TypedDict(
    "_OptionalExportJobsResponseTypeDef", {"NextToken": str}, total=False
)


class ExportJobsResponseTypeDef(
    _RequiredExportJobsResponseTypeDef, _OptionalExportJobsResponseTypeDef
):
    pass


_RequiredGCMChannelResponseTypeDef = TypedDict(
    "_RequiredGCMChannelResponseTypeDef", {"Credential": str, "Platform": str}
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
        "Action": Literal["OPEN_APP", "DEEP_LINK", "URL"],
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

GPSCoordinatesTypeDef = TypedDict("GPSCoordinatesTypeDef", {"Latitude": float, "Longitude": float})

_RequiredGPSPointDimensionTypeDef = TypedDict(
    "_RequiredGPSPointDimensionTypeDef", {"Coordinates": "GPSCoordinatesTypeDef"}
)
_OptionalGPSPointDimensionTypeDef = TypedDict(
    "_OptionalGPSPointDimensionTypeDef", {"RangeInKilometers": float}, total=False
)


class GPSPointDimensionTypeDef(
    _RequiredGPSPointDimensionTypeDef, _OptionalGPSPointDimensionTypeDef
):
    pass


_RequiredHoldoutActivityTypeDef = TypedDict("_RequiredHoldoutActivityTypeDef", {"Percentage": int})
_OptionalHoldoutActivityTypeDef = TypedDict(
    "_OptionalHoldoutActivityTypeDef", {"NextActivity": str}, total=False
)


class HoldoutActivityTypeDef(_RequiredHoldoutActivityTypeDef, _OptionalHoldoutActivityTypeDef):
    pass


_RequiredImportJobResourceTypeDef = TypedDict(
    "_RequiredImportJobResourceTypeDef",
    {"Format": Literal["CSV", "JSON"], "RoleArn": str, "S3Url": str},
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
        "JobStatus": Literal[
            "CREATED",
            "PREPARING_FOR_INITIALIZATION",
            "INITIALIZING",
            "PROCESSING",
            "PENDING_JOB",
            "COMPLETING",
            "COMPLETED",
            "FAILING",
            "FAILED",
        ],
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
    "_RequiredImportJobsResponseTypeDef", {"Item": List["ImportJobResponseTypeDef"]}
)
_OptionalImportJobsResponseTypeDef = TypedDict(
    "_OptionalImportJobsResponseTypeDef", {"NextToken": str}, total=False
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

JourneyCustomMessageTypeDef = TypedDict("JourneyCustomMessageTypeDef", {"Data": str}, total=False)

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
    "_OptionalJourneyDateRangeKpiResponseTypeDef", {"NextToken": str}, total=False
)


class JourneyDateRangeKpiResponseTypeDef(
    _RequiredJourneyDateRangeKpiResponseTypeDef, _OptionalJourneyDateRangeKpiResponseTypeDef
):
    pass


JourneyEmailMessageTypeDef = TypedDict(
    "JourneyEmailMessageTypeDef", {"FromAddress": str}, total=False
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
    {"ApplicationId": str, "JourneyId": str, "LastEvaluatedTime": str, "Metrics": Dict[str, str]},
)

JourneyLimitsTypeDef = TypedDict(
    "JourneyLimitsTypeDef",
    {"DailyCap": int, "EndpointReentryCap": int, "MessagesPerSecond": int},
    total=False,
)

JourneyPushMessageTypeDef = TypedDict("JourneyPushMessageTypeDef", {"TimeToLive": str}, total=False)

_RequiredJourneyResponseTypeDef = TypedDict(
    "_RequiredJourneyResponseTypeDef", {"ApplicationId": str, "Id": str, "Name": str}
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
        "State": Literal["DRAFT", "ACTIVE", "COMPLETED", "CANCELLED", "CLOSED"],
        "tags": Dict[str, str],
    },
    total=False,
)


class JourneyResponseTypeDef(_RequiredJourneyResponseTypeDef, _OptionalJourneyResponseTypeDef):
    pass


JourneySMSMessageTypeDef = TypedDict(
    "JourneySMSMessageTypeDef",
    {"MessageType": Literal["TRANSACTIONAL", "PROMOTIONAL"], "SenderId": str},
    total=False,
)

JourneyScheduleTypeDef = TypedDict(
    "JourneyScheduleTypeDef",
    {"EndTime": datetime, "StartTime": datetime, "Timezone": str},
    total=False,
)

_RequiredJourneysResponseTypeDef = TypedDict(
    "_RequiredJourneysResponseTypeDef", {"Item": List["JourneyResponseTypeDef"]}
)
_OptionalJourneysResponseTypeDef = TypedDict(
    "_OptionalJourneysResponseTypeDef", {"NextToken": str}, total=False
)


class JourneysResponseTypeDef(_RequiredJourneysResponseTypeDef, _OptionalJourneysResponseTypeDef):
    pass


_RequiredListRecommenderConfigurationsResponseTypeDef = TypedDict(
    "_RequiredListRecommenderConfigurationsResponseTypeDef",
    {"Item": List["RecommenderConfigurationResponseTypeDef"]},
)
_OptionalListRecommenderConfigurationsResponseTypeDef = TypedDict(
    "_OptionalListRecommenderConfigurationsResponseTypeDef", {"NextToken": str}, total=False
)


class ListRecommenderConfigurationsResponseTypeDef(
    _RequiredListRecommenderConfigurationsResponseTypeDef,
    _OptionalListRecommenderConfigurationsResponseTypeDef,
):
    pass


MessageBodyTypeDef = TypedDict(
    "MessageBodyTypeDef", {"Message": str, "RequestID": str}, total=False
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

_RequiredMessageResponseTypeDef = TypedDict(
    "_RequiredMessageResponseTypeDef", {"ApplicationId": str}
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
        "DeliveryStatus": Literal[
            "SUCCESSFUL",
            "THROTTLED",
            "TEMPORARY_FAILURE",
            "PERMANENT_FAILURE",
            "UNKNOWN_FAILURE",
            "OPT_OUT",
            "DUPLICATE",
        ],
        "StatusCode": int,
    },
)
_OptionalMessageResultTypeDef = TypedDict(
    "_OptionalMessageResultTypeDef",
    {"MessageId": str, "StatusMessage": str, "UpdatedToken": str},
    total=False,
)


class MessageResultTypeDef(_RequiredMessageResultTypeDef, _OptionalMessageResultTypeDef):
    pass


MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "Action": Literal["OPEN_APP", "DEEP_LINK", "URL"],
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
    "MetricDimensionTypeDef", {"ComparisonOperator": str, "Value": float}
)

MultiConditionalBranchTypeDef = TypedDict(
    "MultiConditionalBranchTypeDef",
    {"Condition": "SimpleConditionTypeDef", "NextActivity": str},
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

PublicEndpointTypeDef = TypedDict(
    "PublicEndpointTypeDef",
    {
        "Address": str,
        "Attributes": Dict[str, List[str]],
        "ChannelType": Literal[
            "PUSH",
            "GCM",
            "APNS",
            "APNS_SANDBOX",
            "APNS_VOIP",
            "APNS_VOIP_SANDBOX",
            "ADM",
            "SMS",
            "VOICE",
            "EMAIL",
            "BAIDU",
            "CUSTOM",
        ],
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

_RequiredPushNotificationTemplateResponseTypeDef = TypedDict(
    "_RequiredPushNotificationTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": Literal["EMAIL", "SMS", "VOICE", "PUSH"],
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


QuietTimeTypeDef = TypedDict("QuietTimeTypeDef", {"End": str, "Start": str}, total=False)

RandomSplitActivityTypeDef = TypedDict(
    "RandomSplitActivityTypeDef", {"Branches": List["RandomSplitEntryTypeDef"]}, total=False
)

RandomSplitEntryTypeDef = TypedDict(
    "RandomSplitEntryTypeDef", {"NextActivity": str, "Percentage": int}, total=False
)

RawEmailTypeDef = TypedDict("RawEmailTypeDef", {"Data": Union[bytes, IO[bytes]]}, total=False)

RecencyDimensionTypeDef = TypedDict(
    "RecencyDimensionTypeDef",
    {
        "Duration": Literal["HR_24", "DAY_7", "DAY_14", "DAY_30"],
        "RecencyType": Literal["ACTIVE", "INACTIVE"],
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


ResultRowTypeDef = TypedDict(
    "ResultRowTypeDef",
    {"GroupedBys": List["ResultRowValueTypeDef"], "Values": List["ResultRowValueTypeDef"]},
)

ResultRowValueTypeDef = TypedDict("ResultRowValueTypeDef", {"Key": str, "Type": str, "Value": str})

_RequiredSMSChannelResponseTypeDef = TypedDict(
    "_RequiredSMSChannelResponseTypeDef", {"Platform": str}
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
        "MessageType": Literal["TRANSACTIONAL", "PROMOTIONAL"],
        "OriginationNumber": str,
        "SenderId": str,
        "Substitutions": Dict[str, List[str]],
    },
    total=False,
)

_RequiredSMSTemplateResponseTypeDef = TypedDict(
    "_RequiredSMSTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": Literal["EMAIL", "SMS", "VOICE", "PUSH"],
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


_RequiredScheduleTypeDef = TypedDict("_RequiredScheduleTypeDef", {"StartTime": str})
_OptionalScheduleTypeDef = TypedDict(
    "_OptionalScheduleTypeDef",
    {
        "EndTime": str,
        "EventFilter": "CampaignEventFilterTypeDef",
        "Frequency": Literal["ONCE", "HOURLY", "DAILY", "WEEKLY", "MONTHLY", "EVENT"],
        "IsLocalTime": bool,
        "QuietTime": "QuietTimeTypeDef",
        "Timezone": str,
    },
    total=False,
)


class ScheduleTypeDef(_RequiredScheduleTypeDef, _OptionalScheduleTypeDef):
    pass


SegmentBehaviorsTypeDef = TypedDict(
    "SegmentBehaviorsTypeDef", {"Recency": "RecencyDimensionTypeDef"}, total=False
)

SegmentConditionTypeDef = TypedDict("SegmentConditionTypeDef", {"SegmentId": str})

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
    {"Groups": List["SegmentGroupTypeDef"], "Include": Literal["ALL", "ANY", "NONE"]},
    total=False,
)

SegmentGroupTypeDef = TypedDict(
    "SegmentGroupTypeDef",
    {
        "Dimensions": List["SegmentDimensionsTypeDef"],
        "SourceSegments": List["SegmentReferenceTypeDef"],
        "SourceType": Literal["ALL", "ANY", "NONE"],
        "Type": Literal["ALL", "ANY", "NONE"],
    },
    total=False,
)

_RequiredSegmentImportResourceTypeDef = TypedDict(
    "_RequiredSegmentImportResourceTypeDef",
    {
        "ExternalId": str,
        "Format": Literal["CSV", "JSON"],
        "RoleArn": str,
        "S3Url": str,
        "Size": int,
    },
)
_OptionalSegmentImportResourceTypeDef = TypedDict(
    "_OptionalSegmentImportResourceTypeDef", {"ChannelCounts": Dict[str, int]}, total=False
)


class SegmentImportResourceTypeDef(
    _RequiredSegmentImportResourceTypeDef, _OptionalSegmentImportResourceTypeDef
):
    pass


SegmentLocationTypeDef = TypedDict(
    "SegmentLocationTypeDef",
    {"Country": "SetDimensionTypeDef", "GPSPoint": "GPSPointDimensionTypeDef"},
    total=False,
)

_RequiredSegmentReferenceTypeDef = TypedDict("_RequiredSegmentReferenceTypeDef", {"Id": str})
_OptionalSegmentReferenceTypeDef = TypedDict(
    "_OptionalSegmentReferenceTypeDef", {"Version": int}, total=False
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
        "SegmentType": Literal["DIMENSIONAL", "IMPORT"],
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
    "_RequiredSegmentsResponseTypeDef", {"Item": List["SegmentResponseTypeDef"]}
)
_OptionalSegmentsResponseTypeDef = TypedDict(
    "_OptionalSegmentsResponseTypeDef", {"NextToken": str}, total=False
)


class SegmentsResponseTypeDef(_RequiredSegmentsResponseTypeDef, _OptionalSegmentsResponseTypeDef):
    pass


_RequiredSendUsersMessageResponseTypeDef = TypedDict(
    "_RequiredSendUsersMessageResponseTypeDef", {"ApplicationId": str}
)
_OptionalSendUsersMessageResponseTypeDef = TypedDict(
    "_OptionalSendUsersMessageResponseTypeDef",
    {"RequestId": str, "Result": Dict[str, Dict[str, "EndpointMessageResultTypeDef"]]},
    total=False,
)


class SendUsersMessageResponseTypeDef(
    _RequiredSendUsersMessageResponseTypeDef, _OptionalSendUsersMessageResponseTypeDef
):
    pass


_RequiredSessionTypeDef = TypedDict("_RequiredSessionTypeDef", {"Id": str, "StartTimestamp": str})
_OptionalSessionTypeDef = TypedDict(
    "_OptionalSessionTypeDef", {"Duration": int, "StopTimestamp": str}, total=False
)


class SessionTypeDef(_RequiredSessionTypeDef, _OptionalSessionTypeDef):
    pass


_RequiredSetDimensionTypeDef = TypedDict("_RequiredSetDimensionTypeDef", {"Values": List[str]})
_OptionalSetDimensionTypeDef = TypedDict(
    "_OptionalSetDimensionTypeDef",
    {"DimensionType": Literal["INCLUSIVE", "EXCLUSIVE"]},
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
    "SimpleEmailPartTypeDef", {"Charset": str, "Data": str}, total=False
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

TagsModelTypeDef = TypedDict("TagsModelTypeDef", {"tags": Dict[str, str]})

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
        "TemplateType": Literal["EMAIL", "SMS", "VOICE", "PUSH"],
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


TemplateTypeDef = TypedDict("TemplateTypeDef", {"Name": str, "Version": str}, total=False)

_RequiredTemplateVersionResponseTypeDef = TypedDict(
    "_RequiredTemplateVersionResponseTypeDef",
    {"CreationDate": str, "LastModifiedDate": str, "TemplateName": str, "TemplateType": str},
)
_OptionalTemplateVersionResponseTypeDef = TypedDict(
    "_OptionalTemplateVersionResponseTypeDef",
    {"DefaultSubstitutions": str, "TemplateDescription": str, "Version": str},
    total=False,
)


class TemplateVersionResponseTypeDef(
    _RequiredTemplateVersionResponseTypeDef, _OptionalTemplateVersionResponseTypeDef
):
    pass


_RequiredTemplateVersionsResponseTypeDef = TypedDict(
    "_RequiredTemplateVersionsResponseTypeDef", {"Item": List["TemplateVersionResponseTypeDef"]}
)
_OptionalTemplateVersionsResponseTypeDef = TypedDict(
    "_OptionalTemplateVersionsResponseTypeDef",
    {"Message": str, "NextToken": str, "RequestID": str},
    total=False,
)


class TemplateVersionsResponseTypeDef(
    _RequiredTemplateVersionsResponseTypeDef, _OptionalTemplateVersionsResponseTypeDef
):
    pass


_RequiredTemplatesResponseTypeDef = TypedDict(
    "_RequiredTemplatesResponseTypeDef", {"Item": List["TemplateResponseTypeDef"]}
)
_OptionalTemplatesResponseTypeDef = TypedDict(
    "_OptionalTemplatesResponseTypeDef", {"NextToken": str}, total=False
)


class TemplatesResponseTypeDef(
    _RequiredTemplatesResponseTypeDef, _OptionalTemplatesResponseTypeDef
):
    pass


_RequiredTreatmentResourceTypeDef = TypedDict(
    "_RequiredTreatmentResourceTypeDef", {"Id": str, "SizePercent": int}
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


_RequiredVoiceChannelResponseTypeDef = TypedDict(
    "_RequiredVoiceChannelResponseTypeDef", {"Platform": str}
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

_RequiredVoiceTemplateResponseTypeDef = TypedDict(
    "_RequiredVoiceTemplateResponseTypeDef",
    {
        "CreationDate": str,
        "LastModifiedDate": str,
        "TemplateName": str,
        "TemplateType": Literal["EMAIL", "SMS", "VOICE", "PUSH"],
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
    "WaitActivityTypeDef", {"NextActivity": str, "WaitTime": "WaitTimeTypeDef"}, total=False
)

WaitTimeTypeDef = TypedDict("WaitTimeTypeDef", {"WaitFor": str, "WaitUntil": str}, total=False)

_RequiredWriteTreatmentResourceTypeDef = TypedDict(
    "_RequiredWriteTreatmentResourceTypeDef", {"SizePercent": int}
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


_RequiredADMChannelRequestTypeDef = TypedDict(
    "_RequiredADMChannelRequestTypeDef", {"ClientId": str, "ClientSecret": str}
)
_OptionalADMChannelRequestTypeDef = TypedDict(
    "_OptionalADMChannelRequestTypeDef", {"Enabled": bool}, total=False
)


class ADMChannelRequestTypeDef(
    _RequiredADMChannelRequestTypeDef, _OptionalADMChannelRequestTypeDef
):
    pass


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

_RequiredBaiduChannelRequestTypeDef = TypedDict(
    "_RequiredBaiduChannelRequestTypeDef", {"ApiKey": str, "SecretKey": str}
)
_OptionalBaiduChannelRequestTypeDef = TypedDict(
    "_OptionalBaiduChannelRequestTypeDef", {"Enabled": bool}, total=False
)


class BaiduChannelRequestTypeDef(
    _RequiredBaiduChannelRequestTypeDef, _OptionalBaiduChannelRequestTypeDef
):
    pass


CreateAppResponseTypeDef = TypedDict(
    "CreateAppResponseTypeDef", {"ApplicationResponse": "ApplicationResponseTypeDef"}
)

_RequiredCreateApplicationRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestTypeDef", {"Name": str}
)
_OptionalCreateApplicationRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestTypeDef", {"tags": Dict[str, str]}, total=False
)


class CreateApplicationRequestTypeDef(
    _RequiredCreateApplicationRequestTypeDef, _OptionalCreateApplicationRequestTypeDef
):
    pass


CreateCampaignResponseTypeDef = TypedDict(
    "CreateCampaignResponseTypeDef", {"CampaignResponse": "CampaignResponseTypeDef"}
)

CreateEmailTemplateResponseTypeDef = TypedDict(
    "CreateEmailTemplateResponseTypeDef",
    {"CreateTemplateMessageBody": "CreateTemplateMessageBodyTypeDef"},
)

CreateExportJobResponseTypeDef = TypedDict(
    "CreateExportJobResponseTypeDef", {"ExportJobResponse": "ExportJobResponseTypeDef"}
)

CreateImportJobResponseTypeDef = TypedDict(
    "CreateImportJobResponseTypeDef", {"ImportJobResponse": "ImportJobResponseTypeDef"}
)

CreateJourneyResponseTypeDef = TypedDict(
    "CreateJourneyResponseTypeDef", {"JourneyResponse": "JourneyResponseTypeDef"}
)

CreatePushTemplateResponseTypeDef = TypedDict(
    "CreatePushTemplateResponseTypeDef",
    {"CreateTemplateMessageBody": "CreateTemplateMessageBodyTypeDef"},
)

CreateRecommenderConfigurationResponseTypeDef = TypedDict(
    "CreateRecommenderConfigurationResponseTypeDef",
    {"RecommenderConfigurationResponse": "RecommenderConfigurationResponseTypeDef"},
)

_RequiredCreateRecommenderConfigurationTypeDef = TypedDict(
    "_RequiredCreateRecommenderConfigurationTypeDef",
    {"RecommendationProviderRoleArn": str, "RecommendationProviderUri": str},
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


CreateSegmentResponseTypeDef = TypedDict(
    "CreateSegmentResponseTypeDef", {"SegmentResponse": "SegmentResponseTypeDef"}
)

CreateSmsTemplateResponseTypeDef = TypedDict(
    "CreateSmsTemplateResponseTypeDef",
    {"CreateTemplateMessageBody": "CreateTemplateMessageBodyTypeDef"},
)

CreateVoiceTemplateResponseTypeDef = TypedDict(
    "CreateVoiceTemplateResponseTypeDef",
    {"CreateTemplateMessageBody": "CreateTemplateMessageBodyTypeDef"},
)

DeleteAdmChannelResponseTypeDef = TypedDict(
    "DeleteAdmChannelResponseTypeDef", {"ADMChannelResponse": "ADMChannelResponseTypeDef"}
)

DeleteApnsChannelResponseTypeDef = TypedDict(
    "DeleteApnsChannelResponseTypeDef", {"APNSChannelResponse": "APNSChannelResponseTypeDef"}
)

DeleteApnsSandboxChannelResponseTypeDef = TypedDict(
    "DeleteApnsSandboxChannelResponseTypeDef",
    {"APNSSandboxChannelResponse": "APNSSandboxChannelResponseTypeDef"},
)

DeleteApnsVoipChannelResponseTypeDef = TypedDict(
    "DeleteApnsVoipChannelResponseTypeDef",
    {"APNSVoipChannelResponse": "APNSVoipChannelResponseTypeDef"},
)

DeleteApnsVoipSandboxChannelResponseTypeDef = TypedDict(
    "DeleteApnsVoipSandboxChannelResponseTypeDef",
    {"APNSVoipSandboxChannelResponse": "APNSVoipSandboxChannelResponseTypeDef"},
)

DeleteAppResponseTypeDef = TypedDict(
    "DeleteAppResponseTypeDef", {"ApplicationResponse": "ApplicationResponseTypeDef"}
)

DeleteBaiduChannelResponseTypeDef = TypedDict(
    "DeleteBaiduChannelResponseTypeDef", {"BaiduChannelResponse": "BaiduChannelResponseTypeDef"}
)

DeleteCampaignResponseTypeDef = TypedDict(
    "DeleteCampaignResponseTypeDef", {"CampaignResponse": "CampaignResponseTypeDef"}
)

DeleteEmailChannelResponseTypeDef = TypedDict(
    "DeleteEmailChannelResponseTypeDef", {"EmailChannelResponse": "EmailChannelResponseTypeDef"}
)

DeleteEmailTemplateResponseTypeDef = TypedDict(
    "DeleteEmailTemplateResponseTypeDef", {"MessageBody": "MessageBodyTypeDef"}
)

DeleteEndpointResponseTypeDef = TypedDict(
    "DeleteEndpointResponseTypeDef", {"EndpointResponse": "EndpointResponseTypeDef"}
)

DeleteEventStreamResponseTypeDef = TypedDict(
    "DeleteEventStreamResponseTypeDef", {"EventStream": "EventStreamTypeDef"}
)

DeleteGcmChannelResponseTypeDef = TypedDict(
    "DeleteGcmChannelResponseTypeDef", {"GCMChannelResponse": "GCMChannelResponseTypeDef"}
)

DeleteJourneyResponseTypeDef = TypedDict(
    "DeleteJourneyResponseTypeDef", {"JourneyResponse": "JourneyResponseTypeDef"}
)

DeletePushTemplateResponseTypeDef = TypedDict(
    "DeletePushTemplateResponseTypeDef", {"MessageBody": "MessageBodyTypeDef"}
)

DeleteRecommenderConfigurationResponseTypeDef = TypedDict(
    "DeleteRecommenderConfigurationResponseTypeDef",
    {"RecommenderConfigurationResponse": "RecommenderConfigurationResponseTypeDef"},
)

DeleteSegmentResponseTypeDef = TypedDict(
    "DeleteSegmentResponseTypeDef", {"SegmentResponse": "SegmentResponseTypeDef"}
)

DeleteSmsChannelResponseTypeDef = TypedDict(
    "DeleteSmsChannelResponseTypeDef", {"SMSChannelResponse": "SMSChannelResponseTypeDef"}
)

DeleteSmsTemplateResponseTypeDef = TypedDict(
    "DeleteSmsTemplateResponseTypeDef", {"MessageBody": "MessageBodyTypeDef"}
)

DeleteUserEndpointsResponseTypeDef = TypedDict(
    "DeleteUserEndpointsResponseTypeDef", {"EndpointsResponse": "EndpointsResponseTypeDef"}
)

DeleteVoiceChannelResponseTypeDef = TypedDict(
    "DeleteVoiceChannelResponseTypeDef", {"VoiceChannelResponse": "VoiceChannelResponseTypeDef"}
)

DeleteVoiceTemplateResponseTypeDef = TypedDict(
    "DeleteVoiceTemplateResponseTypeDef", {"MessageBody": "MessageBodyTypeDef"}
)

_RequiredEmailChannelRequestTypeDef = TypedDict(
    "_RequiredEmailChannelRequestTypeDef", {"FromAddress": str, "Identity": str}
)
_OptionalEmailChannelRequestTypeDef = TypedDict(
    "_OptionalEmailChannelRequestTypeDef",
    {"ConfigurationSet": str, "Enabled": bool, "RoleArn": str},
    total=False,
)


class EmailChannelRequestTypeDef(
    _RequiredEmailChannelRequestTypeDef, _OptionalEmailChannelRequestTypeDef
):
    pass


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

EndpointBatchRequestTypeDef = TypedDict(
    "EndpointBatchRequestTypeDef", {"Item": List["EndpointBatchItemTypeDef"]}
)

EndpointRequestTypeDef = TypedDict(
    "EndpointRequestTypeDef",
    {
        "Address": str,
        "Attributes": Dict[str, List[str]],
        "ChannelType": Literal[
            "PUSH",
            "GCM",
            "APNS",
            "APNS_SANDBOX",
            "APNS_VOIP",
            "APNS_VOIP_SANDBOX",
            "ADM",
            "SMS",
            "VOICE",
            "EMAIL",
            "BAIDU",
            "CUSTOM",
        ],
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

EventsRequestTypeDef = TypedDict(
    "EventsRequestTypeDef", {"BatchItem": Dict[str, "EventsBatchTypeDef"]}
)

_RequiredExportJobRequestTypeDef = TypedDict(
    "_RequiredExportJobRequestTypeDef", {"RoleArn": str, "S3UrlPrefix": str}
)
_OptionalExportJobRequestTypeDef = TypedDict(
    "_OptionalExportJobRequestTypeDef", {"SegmentId": str, "SegmentVersion": int}, total=False
)


class ExportJobRequestTypeDef(_RequiredExportJobRequestTypeDef, _OptionalExportJobRequestTypeDef):
    pass


_RequiredGCMChannelRequestTypeDef = TypedDict("_RequiredGCMChannelRequestTypeDef", {"ApiKey": str})
_OptionalGCMChannelRequestTypeDef = TypedDict(
    "_OptionalGCMChannelRequestTypeDef", {"Enabled": bool}, total=False
)


class GCMChannelRequestTypeDef(
    _RequiredGCMChannelRequestTypeDef, _OptionalGCMChannelRequestTypeDef
):
    pass


GetAdmChannelResponseTypeDef = TypedDict(
    "GetAdmChannelResponseTypeDef", {"ADMChannelResponse": "ADMChannelResponseTypeDef"}
)

GetApnsChannelResponseTypeDef = TypedDict(
    "GetApnsChannelResponseTypeDef", {"APNSChannelResponse": "APNSChannelResponseTypeDef"}
)

GetApnsSandboxChannelResponseTypeDef = TypedDict(
    "GetApnsSandboxChannelResponseTypeDef",
    {"APNSSandboxChannelResponse": "APNSSandboxChannelResponseTypeDef"},
)

GetApnsVoipChannelResponseTypeDef = TypedDict(
    "GetApnsVoipChannelResponseTypeDef",
    {"APNSVoipChannelResponse": "APNSVoipChannelResponseTypeDef"},
)

GetApnsVoipSandboxChannelResponseTypeDef = TypedDict(
    "GetApnsVoipSandboxChannelResponseTypeDef",
    {"APNSVoipSandboxChannelResponse": "APNSVoipSandboxChannelResponseTypeDef"},
)

GetAppResponseTypeDef = TypedDict(
    "GetAppResponseTypeDef", {"ApplicationResponse": "ApplicationResponseTypeDef"}
)

GetApplicationDateRangeKpiResponseTypeDef = TypedDict(
    "GetApplicationDateRangeKpiResponseTypeDef",
    {"ApplicationDateRangeKpiResponse": "ApplicationDateRangeKpiResponseTypeDef"},
)

GetApplicationSettingsResponseTypeDef = TypedDict(
    "GetApplicationSettingsResponseTypeDef",
    {"ApplicationSettingsResource": "ApplicationSettingsResourceTypeDef"},
)

GetAppsResponseTypeDef = TypedDict(
    "GetAppsResponseTypeDef", {"ApplicationsResponse": "ApplicationsResponseTypeDef"}
)

GetBaiduChannelResponseTypeDef = TypedDict(
    "GetBaiduChannelResponseTypeDef", {"BaiduChannelResponse": "BaiduChannelResponseTypeDef"}
)

GetCampaignActivitiesResponseTypeDef = TypedDict(
    "GetCampaignActivitiesResponseTypeDef", {"ActivitiesResponse": "ActivitiesResponseTypeDef"}
)

GetCampaignDateRangeKpiResponseTypeDef = TypedDict(
    "GetCampaignDateRangeKpiResponseTypeDef",
    {"CampaignDateRangeKpiResponse": "CampaignDateRangeKpiResponseTypeDef"},
)

GetCampaignResponseTypeDef = TypedDict(
    "GetCampaignResponseTypeDef", {"CampaignResponse": "CampaignResponseTypeDef"}
)

GetCampaignVersionResponseTypeDef = TypedDict(
    "GetCampaignVersionResponseTypeDef", {"CampaignResponse": "CampaignResponseTypeDef"}
)

GetCampaignVersionsResponseTypeDef = TypedDict(
    "GetCampaignVersionsResponseTypeDef", {"CampaignsResponse": "CampaignsResponseTypeDef"}
)

GetCampaignsResponseTypeDef = TypedDict(
    "GetCampaignsResponseTypeDef", {"CampaignsResponse": "CampaignsResponseTypeDef"}
)

GetChannelsResponseTypeDef = TypedDict(
    "GetChannelsResponseTypeDef", {"ChannelsResponse": "ChannelsResponseTypeDef"}
)

GetEmailChannelResponseTypeDef = TypedDict(
    "GetEmailChannelResponseTypeDef", {"EmailChannelResponse": "EmailChannelResponseTypeDef"}
)

GetEmailTemplateResponseTypeDef = TypedDict(
    "GetEmailTemplateResponseTypeDef", {"EmailTemplateResponse": "EmailTemplateResponseTypeDef"}
)

GetEndpointResponseTypeDef = TypedDict(
    "GetEndpointResponseTypeDef", {"EndpointResponse": "EndpointResponseTypeDef"}
)

GetEventStreamResponseTypeDef = TypedDict(
    "GetEventStreamResponseTypeDef", {"EventStream": "EventStreamTypeDef"}
)

GetExportJobResponseTypeDef = TypedDict(
    "GetExportJobResponseTypeDef", {"ExportJobResponse": "ExportJobResponseTypeDef"}
)

GetExportJobsResponseTypeDef = TypedDict(
    "GetExportJobsResponseTypeDef", {"ExportJobsResponse": "ExportJobsResponseTypeDef"}
)

GetGcmChannelResponseTypeDef = TypedDict(
    "GetGcmChannelResponseTypeDef", {"GCMChannelResponse": "GCMChannelResponseTypeDef"}
)

GetImportJobResponseTypeDef = TypedDict(
    "GetImportJobResponseTypeDef", {"ImportJobResponse": "ImportJobResponseTypeDef"}
)

GetImportJobsResponseTypeDef = TypedDict(
    "GetImportJobsResponseTypeDef", {"ImportJobsResponse": "ImportJobsResponseTypeDef"}
)

GetJourneyDateRangeKpiResponseTypeDef = TypedDict(
    "GetJourneyDateRangeKpiResponseTypeDef",
    {"JourneyDateRangeKpiResponse": "JourneyDateRangeKpiResponseTypeDef"},
)

GetJourneyExecutionActivityMetricsResponseTypeDef = TypedDict(
    "GetJourneyExecutionActivityMetricsResponseTypeDef",
    {"JourneyExecutionActivityMetricsResponse": "JourneyExecutionActivityMetricsResponseTypeDef"},
)

GetJourneyExecutionMetricsResponseTypeDef = TypedDict(
    "GetJourneyExecutionMetricsResponseTypeDef",
    {"JourneyExecutionMetricsResponse": "JourneyExecutionMetricsResponseTypeDef"},
)

GetJourneyResponseTypeDef = TypedDict(
    "GetJourneyResponseTypeDef", {"JourneyResponse": "JourneyResponseTypeDef"}
)

GetPushTemplateResponseTypeDef = TypedDict(
    "GetPushTemplateResponseTypeDef",
    {"PushNotificationTemplateResponse": "PushNotificationTemplateResponseTypeDef"},
)

GetRecommenderConfigurationResponseTypeDef = TypedDict(
    "GetRecommenderConfigurationResponseTypeDef",
    {"RecommenderConfigurationResponse": "RecommenderConfigurationResponseTypeDef"},
)

GetRecommenderConfigurationsResponseTypeDef = TypedDict(
    "GetRecommenderConfigurationsResponseTypeDef",
    {"ListRecommenderConfigurationsResponse": "ListRecommenderConfigurationsResponseTypeDef"},
)

GetSegmentExportJobsResponseTypeDef = TypedDict(
    "GetSegmentExportJobsResponseTypeDef", {"ExportJobsResponse": "ExportJobsResponseTypeDef"}
)

GetSegmentImportJobsResponseTypeDef = TypedDict(
    "GetSegmentImportJobsResponseTypeDef", {"ImportJobsResponse": "ImportJobsResponseTypeDef"}
)

GetSegmentResponseTypeDef = TypedDict(
    "GetSegmentResponseTypeDef", {"SegmentResponse": "SegmentResponseTypeDef"}
)

GetSegmentVersionResponseTypeDef = TypedDict(
    "GetSegmentVersionResponseTypeDef", {"SegmentResponse": "SegmentResponseTypeDef"}
)

GetSegmentVersionsResponseTypeDef = TypedDict(
    "GetSegmentVersionsResponseTypeDef", {"SegmentsResponse": "SegmentsResponseTypeDef"}
)

GetSegmentsResponseTypeDef = TypedDict(
    "GetSegmentsResponseTypeDef", {"SegmentsResponse": "SegmentsResponseTypeDef"}
)

GetSmsChannelResponseTypeDef = TypedDict(
    "GetSmsChannelResponseTypeDef", {"SMSChannelResponse": "SMSChannelResponseTypeDef"}
)

GetSmsTemplateResponseTypeDef = TypedDict(
    "GetSmsTemplateResponseTypeDef", {"SMSTemplateResponse": "SMSTemplateResponseTypeDef"}
)

GetUserEndpointsResponseTypeDef = TypedDict(
    "GetUserEndpointsResponseTypeDef", {"EndpointsResponse": "EndpointsResponseTypeDef"}
)

GetVoiceChannelResponseTypeDef = TypedDict(
    "GetVoiceChannelResponseTypeDef", {"VoiceChannelResponse": "VoiceChannelResponseTypeDef"}
)

GetVoiceTemplateResponseTypeDef = TypedDict(
    "GetVoiceTemplateResponseTypeDef", {"VoiceTemplateResponse": "VoiceTemplateResponseTypeDef"}
)

_RequiredImportJobRequestTypeDef = TypedDict(
    "_RequiredImportJobRequestTypeDef",
    {"Format": Literal["CSV", "JSON"], "RoleArn": str, "S3Url": str},
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


JourneyStateRequestTypeDef = TypedDict(
    "JourneyStateRequestTypeDef",
    {"State": Literal["DRAFT", "ACTIVE", "COMPLETED", "CANCELLED", "CLOSED"]},
    total=False,
)

ListJourneysResponseTypeDef = TypedDict(
    "ListJourneysResponseTypeDef", {"JourneysResponse": "JourneysResponseTypeDef"}
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"TagsModel": "TagsModelTypeDef"}
)

ListTemplateVersionsResponseTypeDef = TypedDict(
    "ListTemplateVersionsResponseTypeDef",
    {"TemplateVersionsResponse": "TemplateVersionsResponseTypeDef"},
)

ListTemplatesResponseTypeDef = TypedDict(
    "ListTemplatesResponseTypeDef", {"TemplatesResponse": "TemplatesResponseTypeDef"}
)

_RequiredMessageRequestTypeDef = TypedDict(
    "_RequiredMessageRequestTypeDef", {"MessageConfiguration": "DirectMessageConfigurationTypeDef"}
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


NumberValidateRequestTypeDef = TypedDict(
    "NumberValidateRequestTypeDef", {"IsoCountryCode": str, "PhoneNumber": str}, total=False
)

PhoneNumberValidateResponseTypeDef = TypedDict(
    "PhoneNumberValidateResponseTypeDef",
    {"NumberValidateResponse": "NumberValidateResponseTypeDef"},
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

PutEventStreamResponseTypeDef = TypedDict(
    "PutEventStreamResponseTypeDef", {"EventStream": "EventStreamTypeDef"}
)

PutEventsResponseTypeDef = TypedDict(
    "PutEventsResponseTypeDef", {"EventsResponse": "EventsResponseTypeDef"}
)

RemoveAttributesResponseTypeDef = TypedDict(
    "RemoveAttributesResponseTypeDef", {"AttributesResource": "AttributesResourceTypeDef"}
)

SMSChannelRequestTypeDef = TypedDict(
    "SMSChannelRequestTypeDef", {"Enabled": bool, "SenderId": str, "ShortCode": str}, total=False
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

SendMessagesResponseTypeDef = TypedDict(
    "SendMessagesResponseTypeDef", {"MessageResponse": "MessageResponseTypeDef"}
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


SendUsersMessagesResponseTypeDef = TypedDict(
    "SendUsersMessagesResponseTypeDef",
    {"SendUsersMessageResponse": "SendUsersMessageResponseTypeDef"},
)

TemplateActiveVersionRequestTypeDef = TypedDict(
    "TemplateActiveVersionRequestTypeDef", {"Version": str}, total=False
)

UpdateAdmChannelResponseTypeDef = TypedDict(
    "UpdateAdmChannelResponseTypeDef", {"ADMChannelResponse": "ADMChannelResponseTypeDef"}
)

UpdateApnsChannelResponseTypeDef = TypedDict(
    "UpdateApnsChannelResponseTypeDef", {"APNSChannelResponse": "APNSChannelResponseTypeDef"}
)

UpdateApnsSandboxChannelResponseTypeDef = TypedDict(
    "UpdateApnsSandboxChannelResponseTypeDef",
    {"APNSSandboxChannelResponse": "APNSSandboxChannelResponseTypeDef"},
)

UpdateApnsVoipChannelResponseTypeDef = TypedDict(
    "UpdateApnsVoipChannelResponseTypeDef",
    {"APNSVoipChannelResponse": "APNSVoipChannelResponseTypeDef"},
)

UpdateApnsVoipSandboxChannelResponseTypeDef = TypedDict(
    "UpdateApnsVoipSandboxChannelResponseTypeDef",
    {"APNSVoipSandboxChannelResponse": "APNSVoipSandboxChannelResponseTypeDef"},
)

UpdateApplicationSettingsResponseTypeDef = TypedDict(
    "UpdateApplicationSettingsResponseTypeDef",
    {"ApplicationSettingsResource": "ApplicationSettingsResourceTypeDef"},
)

UpdateAttributesRequestTypeDef = TypedDict(
    "UpdateAttributesRequestTypeDef", {"Blacklist": List[str]}, total=False
)

UpdateBaiduChannelResponseTypeDef = TypedDict(
    "UpdateBaiduChannelResponseTypeDef", {"BaiduChannelResponse": "BaiduChannelResponseTypeDef"}
)

UpdateCampaignResponseTypeDef = TypedDict(
    "UpdateCampaignResponseTypeDef", {"CampaignResponse": "CampaignResponseTypeDef"}
)

UpdateEmailChannelResponseTypeDef = TypedDict(
    "UpdateEmailChannelResponseTypeDef", {"EmailChannelResponse": "EmailChannelResponseTypeDef"}
)

UpdateEmailTemplateResponseTypeDef = TypedDict(
    "UpdateEmailTemplateResponseTypeDef", {"MessageBody": "MessageBodyTypeDef"}
)

UpdateEndpointResponseTypeDef = TypedDict(
    "UpdateEndpointResponseTypeDef", {"MessageBody": "MessageBodyTypeDef"}
)

UpdateEndpointsBatchResponseTypeDef = TypedDict(
    "UpdateEndpointsBatchResponseTypeDef", {"MessageBody": "MessageBodyTypeDef"}
)

UpdateGcmChannelResponseTypeDef = TypedDict(
    "UpdateGcmChannelResponseTypeDef", {"GCMChannelResponse": "GCMChannelResponseTypeDef"}
)

UpdateJourneyResponseTypeDef = TypedDict(
    "UpdateJourneyResponseTypeDef", {"JourneyResponse": "JourneyResponseTypeDef"}
)

UpdateJourneyStateResponseTypeDef = TypedDict(
    "UpdateJourneyStateResponseTypeDef", {"JourneyResponse": "JourneyResponseTypeDef"}
)

UpdatePushTemplateResponseTypeDef = TypedDict(
    "UpdatePushTemplateResponseTypeDef", {"MessageBody": "MessageBodyTypeDef"}
)

UpdateRecommenderConfigurationResponseTypeDef = TypedDict(
    "UpdateRecommenderConfigurationResponseTypeDef",
    {"RecommenderConfigurationResponse": "RecommenderConfigurationResponseTypeDef"},
)

_RequiredUpdateRecommenderConfigurationTypeDef = TypedDict(
    "_RequiredUpdateRecommenderConfigurationTypeDef",
    {"RecommendationProviderRoleArn": str, "RecommendationProviderUri": str},
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


UpdateSegmentResponseTypeDef = TypedDict(
    "UpdateSegmentResponseTypeDef", {"SegmentResponse": "SegmentResponseTypeDef"}
)

UpdateSmsChannelResponseTypeDef = TypedDict(
    "UpdateSmsChannelResponseTypeDef", {"SMSChannelResponse": "SMSChannelResponseTypeDef"}
)

UpdateSmsTemplateResponseTypeDef = TypedDict(
    "UpdateSmsTemplateResponseTypeDef", {"MessageBody": "MessageBodyTypeDef"}
)

UpdateTemplateActiveVersionResponseTypeDef = TypedDict(
    "UpdateTemplateActiveVersionResponseTypeDef", {"MessageBody": "MessageBodyTypeDef"}
)

UpdateVoiceChannelResponseTypeDef = TypedDict(
    "UpdateVoiceChannelResponseTypeDef", {"VoiceChannelResponse": "VoiceChannelResponseTypeDef"}
)

UpdateVoiceTemplateResponseTypeDef = TypedDict(
    "UpdateVoiceTemplateResponseTypeDef", {"MessageBody": "MessageBodyTypeDef"}
)

VoiceChannelRequestTypeDef = TypedDict("VoiceChannelRequestTypeDef", {"Enabled": bool}, total=False)

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
    "WriteEventStreamTypeDef", {"DestinationStreamArn": str, "RoleArn": str}
)

_RequiredWriteJourneyRequestTypeDef = TypedDict(
    "_RequiredWriteJourneyRequestTypeDef", {"Name": str}
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
        "State": Literal["DRAFT", "ACTIVE", "COMPLETED", "CANCELLED", "CLOSED"],
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
