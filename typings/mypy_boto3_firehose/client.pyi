# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for firehose service client

Usage::

    ```python
    import boto3
    from mypy_boto3_firehose import FirehoseClient

    client: FirehoseClient = boto3.client("firehose")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_firehose.type_defs import (
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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("FirehoseClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    ConcurrentModificationException: Type[Boto3ClientError]
    InvalidArgumentException: Type[Boto3ClientError]
    InvalidKMSResourceException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    ResourceInUseException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    ServiceUnavailableException: Type[Boto3ClientError]


class FirehoseClient:
    """
    [Firehose.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/firehose.html#Firehose.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/firehose.html#Firehose.Client.can_paginate)
        """

    def create_delivery_stream(
        self,
        DeliveryStreamName: str,
        DeliveryStreamType: Literal["DirectPut", "KinesisStreamAsSource"] = None,
        KinesisStreamSourceConfiguration: KinesisStreamSourceConfigurationTypeDef = None,
        DeliveryStreamEncryptionConfigurationInput: DeliveryStreamEncryptionConfigurationInputTypeDef = None,
        S3DestinationConfiguration: "S3DestinationConfigurationTypeDef" = None,
        ExtendedS3DestinationConfiguration: ExtendedS3DestinationConfigurationTypeDef = None,
        RedshiftDestinationConfiguration: RedshiftDestinationConfigurationTypeDef = None,
        ElasticsearchDestinationConfiguration: ElasticsearchDestinationConfigurationTypeDef = None,
        SplunkDestinationConfiguration: SplunkDestinationConfigurationTypeDef = None,
        HttpEndpointDestinationConfiguration: HttpEndpointDestinationConfigurationTypeDef = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDeliveryStreamOutputTypeDef:
        """
        [Client.create_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/firehose.html#Firehose.Client.create_delivery_stream)
        """

    def delete_delivery_stream(
        self, DeliveryStreamName: str, AllowForceDelete: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/firehose.html#Firehose.Client.delete_delivery_stream)
        """

    def describe_delivery_stream(
        self, DeliveryStreamName: str, Limit: int = None, ExclusiveStartDestinationId: str = None
    ) -> DescribeDeliveryStreamOutputTypeDef:
        """
        [Client.describe_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/firehose.html#Firehose.Client.describe_delivery_stream)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/firehose.html#Firehose.Client.generate_presigned_url)
        """

    def list_delivery_streams(
        self,
        Limit: int = None,
        DeliveryStreamType: Literal["DirectPut", "KinesisStreamAsSource"] = None,
        ExclusiveStartDeliveryStreamName: str = None,
    ) -> ListDeliveryStreamsOutputTypeDef:
        """
        [Client.list_delivery_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/firehose.html#Firehose.Client.list_delivery_streams)
        """

    def list_tags_for_delivery_stream(
        self, DeliveryStreamName: str, ExclusiveStartTagKey: str = None, Limit: int = None
    ) -> ListTagsForDeliveryStreamOutputTypeDef:
        """
        [Client.list_tags_for_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/firehose.html#Firehose.Client.list_tags_for_delivery_stream)
        """

    def put_record(self, DeliveryStreamName: str, Record: RecordTypeDef) -> PutRecordOutputTypeDef:
        """
        [Client.put_record documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/firehose.html#Firehose.Client.put_record)
        """

    def put_record_batch(
        self, DeliveryStreamName: str, Records: List[RecordTypeDef]
    ) -> PutRecordBatchOutputTypeDef:
        """
        [Client.put_record_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/firehose.html#Firehose.Client.put_record_batch)
        """

    def start_delivery_stream_encryption(
        self,
        DeliveryStreamName: str,
        DeliveryStreamEncryptionConfigurationInput: DeliveryStreamEncryptionConfigurationInputTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.start_delivery_stream_encryption documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/firehose.html#Firehose.Client.start_delivery_stream_encryption)
        """

    def stop_delivery_stream_encryption(self, DeliveryStreamName: str) -> Dict[str, Any]:
        """
        [Client.stop_delivery_stream_encryption documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/firehose.html#Firehose.Client.stop_delivery_stream_encryption)
        """

    def tag_delivery_stream(
        self, DeliveryStreamName: str, Tags: List["TagTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Client.tag_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/firehose.html#Firehose.Client.tag_delivery_stream)
        """

    def untag_delivery_stream(self, DeliveryStreamName: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_delivery_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/firehose.html#Firehose.Client.untag_delivery_stream)
        """

    def update_destination(
        self,
        DeliveryStreamName: str,
        CurrentDeliveryStreamVersionId: str,
        DestinationId: str,
        S3DestinationUpdate: "S3DestinationUpdateTypeDef" = None,
        ExtendedS3DestinationUpdate: ExtendedS3DestinationUpdateTypeDef = None,
        RedshiftDestinationUpdate: RedshiftDestinationUpdateTypeDef = None,
        ElasticsearchDestinationUpdate: ElasticsearchDestinationUpdateTypeDef = None,
        SplunkDestinationUpdate: SplunkDestinationUpdateTypeDef = None,
        HttpEndpointDestinationUpdate: HttpEndpointDestinationUpdateTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/firehose.html#Firehose.Client.update_destination)
        """
