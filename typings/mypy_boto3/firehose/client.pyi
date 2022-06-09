"""
Type annotations for firehose service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_firehose import FirehoseClient

    client: FirehoseClient = boto3.client("firehose")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import DeliveryStreamTypeType
from .type_defs import (
    AmazonopensearchserviceDestinationConfigurationTypeDef,
    AmazonopensearchserviceDestinationUpdateTypeDef,
    CreateDeliveryStreamOutputTypeDef,
    DeliveryStreamEncryptionConfigurationInputTypeDef,
    DescribeDeliveryStreamOutputTypeDef,
    ElasticsearchDestinationConfigurationTypeDef,
    ElasticsearchDestinationUpdateTypeDef,
    ExtendedS3DestinationConfigurationTypeDef,
    ExtendedS3DestinationUpdateTypeDef,
    HttpEndpointDestinationConfigurationTypeDef,
    HttpEndpointDestinationUpdateTypeDef,
    KinesisStreamSourceConfigurationTypeDef,
    ListDeliveryStreamsOutputTypeDef,
    ListTagsForDeliveryStreamOutputTypeDef,
    PutRecordBatchOutputTypeDef,
    PutRecordOutputTypeDef,
    RecordTypeDef,
    RedshiftDestinationConfigurationTypeDef,
    RedshiftDestinationUpdateTypeDef,
    S3DestinationConfigurationTypeDef,
    S3DestinationUpdateTypeDef,
    SplunkDestinationConfigurationTypeDef,
    SplunkDestinationUpdateTypeDef,
    TagTypeDef,
)

__all__ = ("FirehoseClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    InvalidArgumentException: Type[BotocoreClientError]
    InvalidKMSResourceException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]

class FirehoseClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/firehose.html#Firehose.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        FirehoseClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/firehose.html#Firehose.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#can_paginate)
        """
    def create_delivery_stream(
        self,
        *,
        DeliveryStreamName: str,
        DeliveryStreamType: DeliveryStreamTypeType = None,
        KinesisStreamSourceConfiguration: "KinesisStreamSourceConfigurationTypeDef" = None,
        DeliveryStreamEncryptionConfigurationInput: "DeliveryStreamEncryptionConfigurationInputTypeDef" = None,
        S3DestinationConfiguration: "S3DestinationConfigurationTypeDef" = None,
        ExtendedS3DestinationConfiguration: "ExtendedS3DestinationConfigurationTypeDef" = None,
        RedshiftDestinationConfiguration: "RedshiftDestinationConfigurationTypeDef" = None,
        ElasticsearchDestinationConfiguration: "ElasticsearchDestinationConfigurationTypeDef" = None,
        AmazonopensearchserviceDestinationConfiguration: "AmazonopensearchserviceDestinationConfigurationTypeDef" = None,
        SplunkDestinationConfiguration: "SplunkDestinationConfigurationTypeDef" = None,
        HttpEndpointDestinationConfiguration: "HttpEndpointDestinationConfigurationTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateDeliveryStreamOutputTypeDef:
        """
        Creates a Kinesis Data Firehose delivery stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/firehose.html#Firehose.Client.create_delivery_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#create_delivery_stream)
        """
    def delete_delivery_stream(
        self, *, DeliveryStreamName: str, AllowForceDelete: bool = None
    ) -> Dict[str, Any]:
        """
        Deletes a delivery stream and its data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/firehose.html#Firehose.Client.delete_delivery_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#delete_delivery_stream)
        """
    def describe_delivery_stream(
        self, *, DeliveryStreamName: str, Limit: int = None, ExclusiveStartDestinationId: str = None
    ) -> DescribeDeliveryStreamOutputTypeDef:
        """
        Describes the specified delivery stream and its status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/firehose.html#Firehose.Client.describe_delivery_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#describe_delivery_stream)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/firehose.html#Firehose.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#generate_presigned_url)
        """
    def list_delivery_streams(
        self,
        *,
        Limit: int = None,
        DeliveryStreamType: DeliveryStreamTypeType = None,
        ExclusiveStartDeliveryStreamName: str = None
    ) -> ListDeliveryStreamsOutputTypeDef:
        """
        Lists your delivery streams in alphabetical order of their names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/firehose.html#Firehose.Client.list_delivery_streams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#list_delivery_streams)
        """
    def list_tags_for_delivery_stream(
        self, *, DeliveryStreamName: str, ExclusiveStartTagKey: str = None, Limit: int = None
    ) -> ListTagsForDeliveryStreamOutputTypeDef:
        """
        Lists the tags for the specified delivery stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/firehose.html#Firehose.Client.list_tags_for_delivery_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#list_tags_for_delivery_stream)
        """
    def put_record(
        self, *, DeliveryStreamName: str, Record: "RecordTypeDef"
    ) -> PutRecordOutputTypeDef:
        """
        Writes a single data record into an Amazon Kinesis Data Firehose delivery
        stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/firehose.html#Firehose.Client.put_record)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#put_record)
        """
    def put_record_batch(
        self, *, DeliveryStreamName: str, Records: List["RecordTypeDef"]
    ) -> PutRecordBatchOutputTypeDef:
        """
        Writes multiple data records into a delivery stream in a single call, which can
        achieve higher throughput per producer than when writing single records.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/firehose.html#Firehose.Client.put_record_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#put_record_batch)
        """
    def start_delivery_stream_encryption(
        self,
        *,
        DeliveryStreamName: str,
        DeliveryStreamEncryptionConfigurationInput: "DeliveryStreamEncryptionConfigurationInputTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Enables server-side encryption (SSE) for the delivery stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/firehose.html#Firehose.Client.start_delivery_stream_encryption)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#start_delivery_stream_encryption)
        """
    def stop_delivery_stream_encryption(self, *, DeliveryStreamName: str) -> Dict[str, Any]:
        """
        Disables server-side encryption (SSE) for the delivery stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/firehose.html#Firehose.Client.stop_delivery_stream_encryption)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#stop_delivery_stream_encryption)
        """
    def tag_delivery_stream(
        self, *, DeliveryStreamName: str, Tags: List["TagTypeDef"]
    ) -> Dict[str, Any]:
        """
        Adds or updates tags for the specified delivery stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/firehose.html#Firehose.Client.tag_delivery_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#tag_delivery_stream)
        """
    def untag_delivery_stream(
        self, *, DeliveryStreamName: str, TagKeys: List[str]
    ) -> Dict[str, Any]:
        """
        Removes tags from the specified delivery stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/firehose.html#Firehose.Client.untag_delivery_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#untag_delivery_stream)
        """
    def update_destination(
        self,
        *,
        DeliveryStreamName: str,
        CurrentDeliveryStreamVersionId: str,
        DestinationId: str,
        S3DestinationUpdate: "S3DestinationUpdateTypeDef" = None,
        ExtendedS3DestinationUpdate: "ExtendedS3DestinationUpdateTypeDef" = None,
        RedshiftDestinationUpdate: "RedshiftDestinationUpdateTypeDef" = None,
        ElasticsearchDestinationUpdate: "ElasticsearchDestinationUpdateTypeDef" = None,
        AmazonopensearchserviceDestinationUpdate: "AmazonopensearchserviceDestinationUpdateTypeDef" = None,
        SplunkDestinationUpdate: "SplunkDestinationUpdateTypeDef" = None,
        HttpEndpointDestinationUpdate: "HttpEndpointDestinationUpdateTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates the specified destination of the specified delivery stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/firehose.html#Firehose.Client.update_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#update_destination)
        """
