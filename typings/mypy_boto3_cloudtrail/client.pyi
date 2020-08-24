# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
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

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

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


class Exceptions:
    ClientError: Type[Boto3ClientError]
    CloudTrailARNInvalidException: Type[Boto3ClientError]
    CloudTrailAccessNotEnabledException: Type[Boto3ClientError]
    CloudWatchLogsDeliveryUnavailableException: Type[Boto3ClientError]
    InsightNotEnabledException: Type[Boto3ClientError]
    InsufficientDependencyServiceAccessPermissionException: Type[Boto3ClientError]
    InsufficientEncryptionPolicyException: Type[Boto3ClientError]
    InsufficientS3BucketPolicyException: Type[Boto3ClientError]
    InsufficientSnsTopicPolicyException: Type[Boto3ClientError]
    InvalidCloudWatchLogsLogGroupArnException: Type[Boto3ClientError]
    InvalidCloudWatchLogsRoleArnException: Type[Boto3ClientError]
    InvalidEventCategoryException: Type[Boto3ClientError]
    InvalidEventSelectorsException: Type[Boto3ClientError]
    InvalidHomeRegionException: Type[Boto3ClientError]
    InvalidInsightSelectorsException: Type[Boto3ClientError]
    InvalidKmsKeyIdException: Type[Boto3ClientError]
    InvalidLookupAttributesException: Type[Boto3ClientError]
    InvalidMaxResultsException: Type[Boto3ClientError]
    InvalidNextTokenException: Type[Boto3ClientError]
    InvalidParameterCombinationException: Type[Boto3ClientError]
    InvalidS3BucketNameException: Type[Boto3ClientError]
    InvalidS3PrefixException: Type[Boto3ClientError]
    InvalidSnsTopicNameException: Type[Boto3ClientError]
    InvalidTagParameterException: Type[Boto3ClientError]
    InvalidTimeRangeException: Type[Boto3ClientError]
    InvalidTokenException: Type[Boto3ClientError]
    InvalidTrailNameException: Type[Boto3ClientError]
    KmsException: Type[Boto3ClientError]
    KmsKeyDisabledException: Type[Boto3ClientError]
    KmsKeyNotFoundException: Type[Boto3ClientError]
    MaximumNumberOfTrailsExceededException: Type[Boto3ClientError]
    NotOrganizationMasterAccountException: Type[Boto3ClientError]
    OperationNotPermittedException: Type[Boto3ClientError]
    OrganizationNotInAllFeaturesModeException: Type[Boto3ClientError]
    OrganizationsNotInUseException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    ResourceTypeNotSupportedException: Type[Boto3ClientError]
    S3BucketDoesNotExistException: Type[Boto3ClientError]
    TagsLimitExceededException: Type[Boto3ClientError]
    TrailAlreadyExistsException: Type[Boto3ClientError]
    TrailNotFoundException: Type[Boto3ClientError]
    TrailNotProvidedException: Type[Boto3ClientError]
    UnsupportedOperationException: Type[Boto3ClientError]


class CloudTrailClient:
    """
    [CloudTrail.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Client)
    """

    exceptions: Exceptions

    def add_tags(self, ResourceId: str, TagsList: List["TagTypeDef"] = None) -> Dict[str, Any]:
        """
        [Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Client.add_tags)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Client.can_paginate)
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
        [Client.create_trail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Client.create_trail)
        """

    def delete_trail(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_trail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Client.delete_trail)
        """

    def describe_trails(
        self, trailNameList: List[str] = None, includeShadowTrails: bool = None
    ) -> DescribeTrailsResponseTypeDef:
        """
        [Client.describe_trails documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Client.describe_trails)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Client.generate_presigned_url)
        """

    def get_event_selectors(self, TrailName: str) -> GetEventSelectorsResponseTypeDef:
        """
        [Client.get_event_selectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Client.get_event_selectors)
        """

    def get_insight_selectors(self, TrailName: str) -> GetInsightSelectorsResponseTypeDef:
        """
        [Client.get_insight_selectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Client.get_insight_selectors)
        """

    def get_trail(self, Name: str) -> GetTrailResponseTypeDef:
        """
        [Client.get_trail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Client.get_trail)
        """

    def get_trail_status(self, Name: str) -> GetTrailStatusResponseTypeDef:
        """
        [Client.get_trail_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Client.get_trail_status)
        """

    def list_public_keys(
        self, StartTime: datetime = None, EndTime: datetime = None, NextToken: str = None
    ) -> ListPublicKeysResponseTypeDef:
        """
        [Client.list_public_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Client.list_public_keys)
        """

    def list_tags(
        self, ResourceIdList: List[str], NextToken: str = None
    ) -> ListTagsResponseTypeDef:
        """
        [Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Client.list_tags)
        """

    def list_trails(self, NextToken: str = None) -> ListTrailsResponseTypeDef:
        """
        [Client.list_trails documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Client.list_trails)
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
        [Client.lookup_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Client.lookup_events)
        """

    def put_event_selectors(
        self, TrailName: str, EventSelectors: List["EventSelectorTypeDef"]
    ) -> PutEventSelectorsResponseTypeDef:
        """
        [Client.put_event_selectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Client.put_event_selectors)
        """

    def put_insight_selectors(
        self, TrailName: str, InsightSelectors: List["InsightSelectorTypeDef"]
    ) -> PutInsightSelectorsResponseTypeDef:
        """
        [Client.put_insight_selectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Client.put_insight_selectors)
        """

    def remove_tags(self, ResourceId: str, TagsList: List["TagTypeDef"] = None) -> Dict[str, Any]:
        """
        [Client.remove_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Client.remove_tags)
        """

    def start_logging(self, Name: str) -> Dict[str, Any]:
        """
        [Client.start_logging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Client.start_logging)
        """

    def stop_logging(self, Name: str) -> Dict[str, Any]:
        """
        [Client.stop_logging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Client.stop_logging)
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
        [Client.update_trail documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Client.update_trail)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_public_keys"]) -> ListPublicKeysPaginator:
        """
        [Paginator.ListPublicKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Paginator.ListPublicKeys)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tags"]) -> ListTagsPaginator:
        """
        [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTags)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_trails"]) -> ListTrailsPaginator:
        """
        [Paginator.ListTrails documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTrails)
        """

    @overload
    def get_paginator(self, operation_name: Literal["lookup_events"]) -> LookupEventsPaginator:
        """
        [Paginator.LookupEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudtrail.html#CloudTrail.Paginator.LookupEvents)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
