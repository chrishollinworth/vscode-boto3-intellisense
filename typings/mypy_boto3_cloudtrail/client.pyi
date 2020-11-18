# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for cloudtrail service client

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudtrail import CloudTrailClient

    client: CloudTrailClient = boto3.client("cloudtrail")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_cloudtrail.paginator import (
    ListPublicKeysPaginator,
    ListTagsPaginator,
    ListTrailsPaginator,
    LookupEventsPaginator,
)
from mypy_boto3_cloudtrail.type_defs import (
    CreateTrailResponseTypeDef,
    DescribeTrailsResponseTypeDef,
    EventSelectorTypeDef,
    GetEventSelectorsResponseTypeDef,
    GetInsightSelectorsResponseTypeDef,
    GetTrailResponseTypeDef,
    GetTrailStatusResponseTypeDef,
    InsightSelectorTypeDef,
    ListPublicKeysResponseTypeDef,
    ListTagsResponseTypeDef,
    ListTrailsResponseTypeDef,
    LookupAttributeTypeDef,
    LookupEventsResponseTypeDef,
    PutEventSelectorsResponseTypeDef,
    PutInsightSelectorsResponseTypeDef,
    TagTypeDef,
    UpdateTrailResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CloudTrailClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    CloudTrailARNInvalidException: Type[BotocoreClientError]
    CloudTrailAccessNotEnabledException: Type[BotocoreClientError]
    CloudWatchLogsDeliveryUnavailableException: Type[BotocoreClientError]
    InsightNotEnabledException: Type[BotocoreClientError]
    InsufficientDependencyServiceAccessPermissionException: Type[BotocoreClientError]
    InsufficientEncryptionPolicyException: Type[BotocoreClientError]
    InsufficientS3BucketPolicyException: Type[BotocoreClientError]
    InsufficientSnsTopicPolicyException: Type[BotocoreClientError]
    InvalidCloudWatchLogsLogGroupArnException: Type[BotocoreClientError]
    InvalidCloudWatchLogsRoleArnException: Type[BotocoreClientError]
    InvalidEventCategoryException: Type[BotocoreClientError]
    InvalidEventSelectorsException: Type[BotocoreClientError]
    InvalidHomeRegionException: Type[BotocoreClientError]
    InvalidInsightSelectorsException: Type[BotocoreClientError]
    InvalidKmsKeyIdException: Type[BotocoreClientError]
    InvalidLookupAttributesException: Type[BotocoreClientError]
    InvalidMaxResultsException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidParameterCombinationException: Type[BotocoreClientError]
    InvalidS3BucketNameException: Type[BotocoreClientError]
    InvalidS3PrefixException: Type[BotocoreClientError]
    InvalidSnsTopicNameException: Type[BotocoreClientError]
    InvalidTagParameterException: Type[BotocoreClientError]
    InvalidTimeRangeException: Type[BotocoreClientError]
    InvalidTokenException: Type[BotocoreClientError]
    InvalidTrailNameException: Type[BotocoreClientError]
    KmsException: Type[BotocoreClientError]
    KmsKeyDisabledException: Type[BotocoreClientError]
    KmsKeyNotFoundException: Type[BotocoreClientError]
    MaximumNumberOfTrailsExceededException: Type[BotocoreClientError]
    NotOrganizationMasterAccountException: Type[BotocoreClientError]
    OperationNotPermittedException: Type[BotocoreClientError]
    OrganizationNotInAllFeaturesModeException: Type[BotocoreClientError]
    OrganizationsNotInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceTypeNotSupportedException: Type[BotocoreClientError]
    S3BucketDoesNotExistException: Type[BotocoreClientError]
    TagsLimitExceededException: Type[BotocoreClientError]
    TrailAlreadyExistsException: Type[BotocoreClientError]
    TrailNotFoundException: Type[BotocoreClientError]
    TrailNotProvidedException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]


class CloudTrailClient:
    """
    [CloudTrail.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_tags(self, ResourceId: str, TagsList: List["TagTypeDef"] = None) -> Dict[str, Any]:
        """
        [Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Client.add_tags)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Client.can_paginate)
        """

    def create_trail(
        self,
        Name: str,
        S3BucketName: str,
        S3KeyPrefix: str = None,
        SnsTopicName: str = None,
        IncludeGlobalServiceEvents: bool = None,
        IsMultiRegionTrail: bool = None,
        EnableLogFileValidation: bool = None,
        CloudWatchLogsLogGroupArn: str = None,
        CloudWatchLogsRoleArn: str = None,
        KmsKeyId: str = None,
        IsOrganizationTrail: bool = None,
        TagsList: List["TagTypeDef"] = None,
    ) -> CreateTrailResponseTypeDef:
        """
        [Client.create_trail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Client.create_trail)
        """

    def delete_trail(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_trail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Client.delete_trail)
        """

    def describe_trails(
        self, trailNameList: List[str] = None, includeShadowTrails: bool = None
    ) -> DescribeTrailsResponseTypeDef:
        """
        [Client.describe_trails documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Client.describe_trails)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Client.generate_presigned_url)
        """

    def get_event_selectors(self, TrailName: str) -> GetEventSelectorsResponseTypeDef:
        """
        [Client.get_event_selectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Client.get_event_selectors)
        """

    def get_insight_selectors(self, TrailName: str) -> GetInsightSelectorsResponseTypeDef:
        """
        [Client.get_insight_selectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Client.get_insight_selectors)
        """

    def get_trail(self, Name: str) -> GetTrailResponseTypeDef:
        """
        [Client.get_trail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Client.get_trail)
        """

    def get_trail_status(self, Name: str) -> GetTrailStatusResponseTypeDef:
        """
        [Client.get_trail_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Client.get_trail_status)
        """

    def list_public_keys(
        self, StartTime: datetime = None, EndTime: datetime = None, NextToken: str = None
    ) -> ListPublicKeysResponseTypeDef:
        """
        [Client.list_public_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Client.list_public_keys)
        """

    def list_tags(
        self, ResourceIdList: List[str], NextToken: str = None
    ) -> ListTagsResponseTypeDef:
        """
        [Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Client.list_tags)
        """

    def list_trails(self, NextToken: str = None) -> ListTrailsResponseTypeDef:
        """
        [Client.list_trails documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Client.list_trails)
        """

    def lookup_events(
        self,
        LookupAttributes: List[LookupAttributeTypeDef] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        EventCategory: Literal["insight"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> LookupEventsResponseTypeDef:
        """
        [Client.lookup_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Client.lookup_events)
        """

    def put_event_selectors(
        self, TrailName: str, EventSelectors: List["EventSelectorTypeDef"]
    ) -> PutEventSelectorsResponseTypeDef:
        """
        [Client.put_event_selectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Client.put_event_selectors)
        """

    def put_insight_selectors(
        self, TrailName: str, InsightSelectors: List["InsightSelectorTypeDef"]
    ) -> PutInsightSelectorsResponseTypeDef:
        """
        [Client.put_insight_selectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Client.put_insight_selectors)
        """

    def remove_tags(self, ResourceId: str, TagsList: List["TagTypeDef"] = None) -> Dict[str, Any]:
        """
        [Client.remove_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Client.remove_tags)
        """

    def start_logging(self, Name: str) -> Dict[str, Any]:
        """
        [Client.start_logging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Client.start_logging)
        """

    def stop_logging(self, Name: str) -> Dict[str, Any]:
        """
        [Client.stop_logging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Client.stop_logging)
        """

    def update_trail(
        self,
        Name: str,
        S3BucketName: str = None,
        S3KeyPrefix: str = None,
        SnsTopicName: str = None,
        IncludeGlobalServiceEvents: bool = None,
        IsMultiRegionTrail: bool = None,
        EnableLogFileValidation: bool = None,
        CloudWatchLogsLogGroupArn: str = None,
        CloudWatchLogsRoleArn: str = None,
        KmsKeyId: str = None,
        IsOrganizationTrail: bool = None,
    ) -> UpdateTrailResponseTypeDef:
        """
        [Client.update_trail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Client.update_trail)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_public_keys"]) -> ListPublicKeysPaginator:
        """
        [Paginator.ListPublicKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Paginator.ListPublicKeys)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tags"]) -> ListTagsPaginator:
        """
        [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTags)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_trails"]) -> ListTrailsPaginator:
        """
        [Paginator.ListTrails documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTrails)
        """

    @overload
    def get_paginator(self, operation_name: Literal["lookup_events"]) -> LookupEventsPaginator:
        """
        [Paginator.LookupEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudtrail.html#CloudTrail.Paginator.LookupEvents)
        """
