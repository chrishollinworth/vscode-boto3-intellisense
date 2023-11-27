"""
Type annotations for cloudtrail service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudtrail import CloudTrailClient

    client: CloudTrailClient = boto3.client("cloudtrail")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import BillingModeType, ImportStatusType, QueryStatusType
from .paginator import (
    ListImportFailuresPaginator,
    ListImportsPaginator,
    ListPublicKeysPaginator,
    ListTagsPaginator,
    ListTrailsPaginator,
    LookupEventsPaginator,
)
from .type_defs import (
    AdvancedEventSelectorTypeDef,
    CancelQueryResponseTypeDef,
    CreateChannelResponseTypeDef,
    CreateEventDataStoreResponseTypeDef,
    CreateTrailResponseTypeDef,
    DescribeQueryResponseTypeDef,
    DescribeTrailsResponseTypeDef,
    DestinationTypeDef,
    DisableFederationResponseTypeDef,
    EnableFederationResponseTypeDef,
    EventSelectorTypeDef,
    GetChannelResponseTypeDef,
    GetEventDataStoreResponseTypeDef,
    GetEventSelectorsResponseTypeDef,
    GetImportResponseTypeDef,
    GetInsightSelectorsResponseTypeDef,
    GetQueryResultsResponseTypeDef,
    GetResourcePolicyResponseTypeDef,
    GetTrailResponseTypeDef,
    GetTrailStatusResponseTypeDef,
    ImportSourceTypeDef,
    InsightSelectorTypeDef,
    ListChannelsResponseTypeDef,
    ListEventDataStoresResponseTypeDef,
    ListImportFailuresResponseTypeDef,
    ListImportsResponseTypeDef,
    ListPublicKeysResponseTypeDef,
    ListQueriesResponseTypeDef,
    ListTagsResponseTypeDef,
    ListTrailsResponseTypeDef,
    LookupAttributeTypeDef,
    LookupEventsResponseTypeDef,
    PutEventSelectorsResponseTypeDef,
    PutInsightSelectorsResponseTypeDef,
    PutResourcePolicyResponseTypeDef,
    RestoreEventDataStoreResponseTypeDef,
    StartImportResponseTypeDef,
    StartQueryResponseTypeDef,
    StopImportResponseTypeDef,
    TagTypeDef,
    UpdateChannelResponseTypeDef,
    UpdateEventDataStoreResponseTypeDef,
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
    AccessDeniedException: Type[BotocoreClientError]
    AccountHasOngoingImportException: Type[BotocoreClientError]
    AccountNotFoundException: Type[BotocoreClientError]
    AccountNotRegisteredException: Type[BotocoreClientError]
    AccountRegisteredException: Type[BotocoreClientError]
    CannotDelegateManagementAccountException: Type[BotocoreClientError]
    ChannelARNInvalidException: Type[BotocoreClientError]
    ChannelAlreadyExistsException: Type[BotocoreClientError]
    ChannelExistsForEDSException: Type[BotocoreClientError]
    ChannelMaxLimitExceededException: Type[BotocoreClientError]
    ChannelNotFoundException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    CloudTrailARNInvalidException: Type[BotocoreClientError]
    CloudTrailAccessNotEnabledException: Type[BotocoreClientError]
    CloudTrailInvalidClientTokenIdException: Type[BotocoreClientError]
    CloudWatchLogsDeliveryUnavailableException: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DelegatedAdminAccountLimitExceededException: Type[BotocoreClientError]
    EventDataStoreARNInvalidException: Type[BotocoreClientError]
    EventDataStoreAlreadyExistsException: Type[BotocoreClientError]
    EventDataStoreFederationEnabledException: Type[BotocoreClientError]
    EventDataStoreHasOngoingImportException: Type[BotocoreClientError]
    EventDataStoreMaxLimitExceededException: Type[BotocoreClientError]
    EventDataStoreNotFoundException: Type[BotocoreClientError]
    EventDataStoreTerminationProtectedException: Type[BotocoreClientError]
    ImportNotFoundException: Type[BotocoreClientError]
    InactiveEventDataStoreException: Type[BotocoreClientError]
    InactiveQueryException: Type[BotocoreClientError]
    InsightNotEnabledException: Type[BotocoreClientError]
    InsufficientDependencyServiceAccessPermissionException: Type[BotocoreClientError]
    InsufficientEncryptionPolicyException: Type[BotocoreClientError]
    InsufficientS3BucketPolicyException: Type[BotocoreClientError]
    InsufficientSnsTopicPolicyException: Type[BotocoreClientError]
    InvalidCloudWatchLogsLogGroupArnException: Type[BotocoreClientError]
    InvalidCloudWatchLogsRoleArnException: Type[BotocoreClientError]
    InvalidDateRangeException: Type[BotocoreClientError]
    InvalidEventCategoryException: Type[BotocoreClientError]
    InvalidEventDataStoreCategoryException: Type[BotocoreClientError]
    InvalidEventDataStoreStatusException: Type[BotocoreClientError]
    InvalidEventSelectorsException: Type[BotocoreClientError]
    InvalidHomeRegionException: Type[BotocoreClientError]
    InvalidImportSourceException: Type[BotocoreClientError]
    InvalidInsightSelectorsException: Type[BotocoreClientError]
    InvalidKmsKeyIdException: Type[BotocoreClientError]
    InvalidLookupAttributesException: Type[BotocoreClientError]
    InvalidMaxResultsException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidParameterCombinationException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidQueryStatementException: Type[BotocoreClientError]
    InvalidQueryStatusException: Type[BotocoreClientError]
    InvalidS3BucketNameException: Type[BotocoreClientError]
    InvalidS3PrefixException: Type[BotocoreClientError]
    InvalidSnsTopicNameException: Type[BotocoreClientError]
    InvalidSourceException: Type[BotocoreClientError]
    InvalidTagParameterException: Type[BotocoreClientError]
    InvalidTimeRangeException: Type[BotocoreClientError]
    InvalidTokenException: Type[BotocoreClientError]
    InvalidTrailNameException: Type[BotocoreClientError]
    KmsException: Type[BotocoreClientError]
    KmsKeyDisabledException: Type[BotocoreClientError]
    KmsKeyNotFoundException: Type[BotocoreClientError]
    MaxConcurrentQueriesException: Type[BotocoreClientError]
    MaximumNumberOfTrailsExceededException: Type[BotocoreClientError]
    NoManagementAccountSLRExistsException: Type[BotocoreClientError]
    NotOrganizationManagementAccountException: Type[BotocoreClientError]
    NotOrganizationMasterAccountException: Type[BotocoreClientError]
    OperationNotPermittedException: Type[BotocoreClientError]
    OrganizationNotInAllFeaturesModeException: Type[BotocoreClientError]
    OrganizationsNotInUseException: Type[BotocoreClientError]
    QueryIdNotFoundException: Type[BotocoreClientError]
    ResourceARNNotValidException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourcePolicyNotFoundException: Type[BotocoreClientError]
    ResourcePolicyNotValidException: Type[BotocoreClientError]
    ResourceTypeNotSupportedException: Type[BotocoreClientError]
    S3BucketDoesNotExistException: Type[BotocoreClientError]
    TagsLimitExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TrailAlreadyExistsException: Type[BotocoreClientError]
    TrailNotFoundException: Type[BotocoreClientError]
    TrailNotProvidedException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]

class CloudTrailClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudTrailClient exceptions.
        """
    def add_tags(self, *, ResourceId: str, TagsList: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds one or more tags to a trail, event data store, or channel, up to a limit of
        50.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.add_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#add_tags)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#can_paginate)
        """
    def cancel_query(
        self, *, QueryId: str, EventDataStore: str = None
    ) -> CancelQueryResponseTypeDef:
        """
        Cancels a query if the query is not in a terminated state, such as `CANCELLED`,
        `FAILED`, `TIMED_OUT`, or `FINISHED`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.cancel_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#cancel_query)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#close)
        """
    def create_channel(
        self,
        *,
        Name: str,
        Source: str,
        Destinations: List["DestinationTypeDef"],
        Tags: List["TagTypeDef"] = None
    ) -> CreateChannelResponseTypeDef:
        """
        Creates a channel for CloudTrail to ingest events from a partner or external
        source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.create_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#create_channel)
        """
    def create_event_data_store(
        self,
        *,
        Name: str,
        AdvancedEventSelectors: List["AdvancedEventSelectorTypeDef"] = None,
        MultiRegionEnabled: bool = None,
        OrganizationEnabled: bool = None,
        RetentionPeriod: int = None,
        TerminationProtectionEnabled: bool = None,
        TagsList: List["TagTypeDef"] = None,
        KmsKeyId: str = None,
        StartIngestion: bool = None,
        BillingMode: BillingModeType = None
    ) -> CreateEventDataStoreResponseTypeDef:
        """
        Creates a new event data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.create_event_data_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#create_event_data_store)
        """
    def create_trail(
        self,
        *,
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
        TagsList: List["TagTypeDef"] = None
    ) -> CreateTrailResponseTypeDef:
        """
        Creates a trail that specifies the settings for delivery of log data to an
        Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.create_trail)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#create_trail)
        """
    def delete_channel(self, *, Channel: str) -> Dict[str, Any]:
        """
        Deletes a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.delete_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#delete_channel)
        """
    def delete_event_data_store(self, *, EventDataStore: str) -> Dict[str, Any]:
        """
        Disables the event data store specified by `EventDataStore`, which accepts an
        event data store ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.delete_event_data_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#delete_event_data_store)
        """
    def delete_resource_policy(self, *, ResourceArn: str) -> Dict[str, Any]:
        """
        Deletes the resource-based policy attached to the CloudTrail channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#delete_resource_policy)
        """
    def delete_trail(self, *, Name: str) -> Dict[str, Any]:
        """
        Deletes a trail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.delete_trail)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#delete_trail)
        """
    def deregister_organization_delegated_admin(
        self, *, DelegatedAdminAccountId: str
    ) -> Dict[str, Any]:
        """
        Removes CloudTrail delegated administrator permissions from a member account in
        an organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.deregister_organization_delegated_admin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#deregister_organization_delegated_admin)
        """
    def describe_query(
        self, *, EventDataStore: str = None, QueryId: str = None, QueryAlias: str = None
    ) -> DescribeQueryResponseTypeDef:
        """
        Returns metadata about a query, including query run time in milliseconds, number
        of events scanned and matched, and query status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.describe_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#describe_query)
        """
    def describe_trails(
        self, *, trailNameList: List[str] = None, includeShadowTrails: bool = None
    ) -> DescribeTrailsResponseTypeDef:
        """
        Retrieves settings for one or more trails associated with the current Region for
        your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.describe_trails)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#describe_trails)
        """
    def disable_federation(self, *, EventDataStore: str) -> DisableFederationResponseTypeDef:
        """
        Disables Lake query federation on the specified event data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.disable_federation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#disable_federation)
        """
    def enable_federation(
        self, *, EventDataStore: str, FederationRoleArn: str
    ) -> EnableFederationResponseTypeDef:
        """
        Enables Lake query federation on the specified event data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.enable_federation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#enable_federation)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#generate_presigned_url)
        """
    def get_channel(self, *, Channel: str) -> GetChannelResponseTypeDef:
        """
        Returns information about a specific channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.get_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#get_channel)
        """
    def get_event_data_store(self, *, EventDataStore: str) -> GetEventDataStoreResponseTypeDef:
        """
        Returns information about an event data store specified as either an ARN or the
        ID portion of the ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.get_event_data_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#get_event_data_store)
        """
    def get_event_selectors(self, *, TrailName: str) -> GetEventSelectorsResponseTypeDef:
        """
        Describes the settings for the event selectors that you configured for your
        trail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.get_event_selectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#get_event_selectors)
        """
    def get_import(self, *, ImportId: str) -> GetImportResponseTypeDef:
        """
        Returns information about a specific import.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.get_import)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#get_import)
        """
    def get_insight_selectors(
        self, *, TrailName: str = None, EventDataStore: str = None
    ) -> GetInsightSelectorsResponseTypeDef:
        """
        Describes the settings for the Insights event selectors that you configured for
        your trail or event data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.get_insight_selectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#get_insight_selectors)
        """
    def get_query_results(
        self,
        *,
        QueryId: str,
        EventDataStore: str = None,
        NextToken: str = None,
        MaxQueryResults: int = None
    ) -> GetQueryResultsResponseTypeDef:
        """
        Gets event data results of a query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.get_query_results)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#get_query_results)
        """
    def get_resource_policy(self, *, ResourceArn: str) -> GetResourcePolicyResponseTypeDef:
        """
        Retrieves the JSON text of the resource-based policy document attached to the
        CloudTrail channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.get_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#get_resource_policy)
        """
    def get_trail(self, *, Name: str) -> GetTrailResponseTypeDef:
        """
        Returns settings information for a specified trail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.get_trail)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#get_trail)
        """
    def get_trail_status(self, *, Name: str) -> GetTrailStatusResponseTypeDef:
        """
        Returns a JSON-formatted list of information about the specified trail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.get_trail_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#get_trail_status)
        """
    def list_channels(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListChannelsResponseTypeDef:
        """
        Lists the channels in the current account, and their source names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.list_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#list_channels)
        """
    def list_event_data_stores(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListEventDataStoresResponseTypeDef:
        """
        Returns information about all event data stores in the account, in the current
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.list_event_data_stores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#list_event_data_stores)
        """
    def list_import_failures(
        self, *, ImportId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListImportFailuresResponseTypeDef:
        """
        Returns a list of failures for the specified import.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.list_import_failures)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#list_import_failures)
        """
    def list_imports(
        self,
        *,
        MaxResults: int = None,
        Destination: str = None,
        ImportStatus: ImportStatusType = None,
        NextToken: str = None
    ) -> ListImportsResponseTypeDef:
        """
        Returns information on all imports, or a select set of imports by `ImportStatus`
        or `Destination`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.list_imports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#list_imports)
        """
    def list_public_keys(
        self,
        *,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        NextToken: str = None
    ) -> ListPublicKeysResponseTypeDef:
        """
        Returns all public keys whose private keys were used to sign the digest files
        within the specified time range.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.list_public_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#list_public_keys)
        """
    def list_queries(
        self,
        *,
        EventDataStore: str,
        NextToken: str = None,
        MaxResults: int = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        QueryStatus: QueryStatusType = None
    ) -> ListQueriesResponseTypeDef:
        """
        Returns a list of queries and query statuses for the past seven days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.list_queries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#list_queries)
        """
    def list_tags(
        self, *, ResourceIdList: List[str], NextToken: str = None
    ) -> ListTagsResponseTypeDef:
        """
        Lists the tags for the specified trails, event data stores, or channels in the
        current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.list_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#list_tags)
        """
    def list_trails(self, *, NextToken: str = None) -> ListTrailsResponseTypeDef:
        """
        Lists trails that are in the current account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.list_trails)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#list_trails)
        """
    def lookup_events(
        self,
        *,
        LookupAttributes: List["LookupAttributeTypeDef"] = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        EventCategory: Literal["insight"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> LookupEventsResponseTypeDef:
        """
        Looks up `management events
        <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-
        concepts.html#cloudtrail-concepts-management-events>`__ or `CloudTrail Insights
        events <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-
        concepts.html#cloudtrail-concepts-insigh...`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.lookup_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#lookup_events)
        """
    def put_event_selectors(
        self,
        *,
        TrailName: str,
        EventSelectors: List["EventSelectorTypeDef"] = None,
        AdvancedEventSelectors: List["AdvancedEventSelectorTypeDef"] = None
    ) -> PutEventSelectorsResponseTypeDef:
        """
        Configures an event selector or advanced event selectors for your trail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.put_event_selectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#put_event_selectors)
        """
    def put_insight_selectors(
        self,
        *,
        InsightSelectors: List["InsightSelectorTypeDef"],
        TrailName: str = None,
        EventDataStore: str = None,
        InsightsDestination: str = None
    ) -> PutInsightSelectorsResponseTypeDef:
        """
        Lets you enable Insights event logging by specifying the Insights selectors that
        you want to enable on an existing trail or event data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.put_insight_selectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#put_insight_selectors)
        """
    def put_resource_policy(
        self, *, ResourceArn: str, ResourcePolicy: str
    ) -> PutResourcePolicyResponseTypeDef:
        """
        Attaches a resource-based permission policy to a CloudTrail channel that is used
        for an integration with an event source outside of Amazon Web Services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#put_resource_policy)
        """
    def register_organization_delegated_admin(self, *, MemberAccountId: str) -> Dict[str, Any]:
        """
        Registers an organization’s member account as the CloudTrail `delegated
        administrator
        <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-
        delegated-administrator.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.register_organization_delegated_admin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#register_organization_delegated_admin)
        """
    def remove_tags(self, *, ResourceId: str, TagsList: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Removes the specified tags from a trail, event data store, or channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.remove_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#remove_tags)
        """
    def restore_event_data_store(
        self, *, EventDataStore: str
    ) -> RestoreEventDataStoreResponseTypeDef:
        """
        Restores a deleted event data store specified by `EventDataStore`, which accepts
        an event data store ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.restore_event_data_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#restore_event_data_store)
        """
    def start_event_data_store_ingestion(self, *, EventDataStore: str) -> Dict[str, Any]:
        """
        Starts the ingestion of live events on an event data store specified as either
        an ARN or the ID portion of the ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.start_event_data_store_ingestion)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#start_event_data_store_ingestion)
        """
    def start_import(
        self,
        *,
        Destinations: List[str] = None,
        ImportSource: "ImportSourceTypeDef" = None,
        StartEventTime: Union[datetime, str] = None,
        EndEventTime: Union[datetime, str] = None,
        ImportId: str = None
    ) -> StartImportResponseTypeDef:
        """
        Starts an import of logged trail events from a source S3 bucket to a destination
        event data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.start_import)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#start_import)
        """
    def start_logging(self, *, Name: str) -> Dict[str, Any]:
        """
        Starts the recording of Amazon Web Services API calls and log file delivery for
        a trail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.start_logging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#start_logging)
        """
    def start_query(
        self,
        *,
        QueryStatement: str = None,
        DeliveryS3Uri: str = None,
        QueryAlias: str = None,
        QueryParameters: List[str] = None
    ) -> StartQueryResponseTypeDef:
        """
        Starts a CloudTrail Lake query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.start_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#start_query)
        """
    def stop_event_data_store_ingestion(self, *, EventDataStore: str) -> Dict[str, Any]:
        """
        Stops the ingestion of live events on an event data store specified as either an
        ARN or the ID portion of the ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.stop_event_data_store_ingestion)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#stop_event_data_store_ingestion)
        """
    def stop_import(self, *, ImportId: str) -> StopImportResponseTypeDef:
        """
        Stops a specified import.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.stop_import)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#stop_import)
        """
    def stop_logging(self, *, Name: str) -> Dict[str, Any]:
        """
        Suspends the recording of Amazon Web Services API calls and log file delivery
        for the specified trail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.stop_logging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#stop_logging)
        """
    def update_channel(
        self, *, Channel: str, Destinations: List["DestinationTypeDef"] = None, Name: str = None
    ) -> UpdateChannelResponseTypeDef:
        """
        Updates a channel specified by a required channel ARN or UUID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.update_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#update_channel)
        """
    def update_event_data_store(
        self,
        *,
        EventDataStore: str,
        Name: str = None,
        AdvancedEventSelectors: List["AdvancedEventSelectorTypeDef"] = None,
        MultiRegionEnabled: bool = None,
        OrganizationEnabled: bool = None,
        RetentionPeriod: int = None,
        TerminationProtectionEnabled: bool = None,
        KmsKeyId: str = None,
        BillingMode: BillingModeType = None
    ) -> UpdateEventDataStoreResponseTypeDef:
        """
        Updates an event data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.update_event_data_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#update_event_data_store)
        """
    def update_trail(
        self,
        *,
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
        IsOrganizationTrail: bool = None
    ) -> UpdateTrailResponseTypeDef:
        """
        Updates trail settings that control what events you are logging, and how to
        handle log files.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Client.update_trail)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/client.html#update_trail)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_import_failures"]
    ) -> ListImportFailuresPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Paginator.ListImportFailures)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators.html#listimportfailurespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_imports"]) -> ListImportsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Paginator.ListImports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators.html#listimportspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_public_keys"]) -> ListPublicKeysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Paginator.ListPublicKeys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators.html#listpublickeyspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_tags"]) -> ListTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators.html#listtagspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_trails"]) -> ListTrailsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Paginator.ListTrails)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators.html#listtrailspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["lookup_events"]) -> LookupEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cloudtrail.html#CloudTrail.Paginator.LookupEvents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/paginators.html#lookupeventspaginator)
        """
