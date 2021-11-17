"""
Type annotations for s3control service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_s3control import S3ControlClient

    client: S3ControlClient = boto3.client("s3control")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import BucketCannedACLType, JobStatusType, RequestedJobStatusType
from .paginator import ListAccessPointsForObjectLambdaPaginator
from .type_defs import (
    CreateAccessPointForObjectLambdaResultTypeDef,
    CreateAccessPointResultTypeDef,
    CreateBucketConfigurationTypeDef,
    CreateBucketResultTypeDef,
    CreateJobResultTypeDef,
    CreateMultiRegionAccessPointInputTypeDef,
    CreateMultiRegionAccessPointResultTypeDef,
    DeleteMultiRegionAccessPointInputTypeDef,
    DeleteMultiRegionAccessPointResultTypeDef,
    DescribeJobResultTypeDef,
    DescribeMultiRegionAccessPointOperationResultTypeDef,
    GetAccessPointConfigurationForObjectLambdaResultTypeDef,
    GetAccessPointForObjectLambdaResultTypeDef,
    GetAccessPointPolicyForObjectLambdaResultTypeDef,
    GetAccessPointPolicyResultTypeDef,
    GetAccessPointPolicyStatusForObjectLambdaResultTypeDef,
    GetAccessPointPolicyStatusResultTypeDef,
    GetAccessPointResultTypeDef,
    GetBucketLifecycleConfigurationResultTypeDef,
    GetBucketPolicyResultTypeDef,
    GetBucketResultTypeDef,
    GetBucketTaggingResultTypeDef,
    GetJobTaggingResultTypeDef,
    GetMultiRegionAccessPointPolicyResultTypeDef,
    GetMultiRegionAccessPointPolicyStatusResultTypeDef,
    GetMultiRegionAccessPointResultTypeDef,
    GetPublicAccessBlockOutputTypeDef,
    GetStorageLensConfigurationResultTypeDef,
    GetStorageLensConfigurationTaggingResultTypeDef,
    JobManifestTypeDef,
    JobOperationTypeDef,
    JobReportTypeDef,
    LifecycleConfigurationTypeDef,
    ListAccessPointsForObjectLambdaResultTypeDef,
    ListAccessPointsResultTypeDef,
    ListJobsResultTypeDef,
    ListMultiRegionAccessPointsResultTypeDef,
    ListRegionalBucketsResultTypeDef,
    ListStorageLensConfigurationsResultTypeDef,
    ObjectLambdaConfigurationTypeDef,
    PublicAccessBlockConfigurationTypeDef,
    PutMultiRegionAccessPointPolicyInputTypeDef,
    PutMultiRegionAccessPointPolicyResultTypeDef,
    S3TagTypeDef,
    StorageLensConfigurationTypeDef,
    StorageLensTagTypeDef,
    TaggingTypeDef,
    UpdateJobPriorityResultTypeDef,
    UpdateJobStatusResultTypeDef,
    VpcConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("S3ControlClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    BucketAlreadyExists: Type[BotocoreClientError]
    BucketAlreadyOwnedByYou: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    IdempotencyException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    JobStatusException: Type[BotocoreClientError]
    NoSuchPublicAccessBlockConfiguration: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]

class S3ControlClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        S3ControlClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#can_paginate)
        """
    def create_access_point(
        self,
        *,
        AccountId: str,
        Name: str,
        Bucket: str,
        VpcConfiguration: "VpcConfigurationTypeDef" = None,
        PublicAccessBlockConfiguration: "PublicAccessBlockConfigurationTypeDef" = None
    ) -> CreateAccessPointResultTypeDef:
        """
        Creates an access point and associates it with the specified bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.create_access_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#create_access_point)
        """
    def create_access_point_for_object_lambda(
        self, *, AccountId: str, Name: str, Configuration: "ObjectLambdaConfigurationTypeDef"
    ) -> CreateAccessPointForObjectLambdaResultTypeDef:
        """
        Creates an Object Lambda Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.create_access_point_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#create_access_point_for_object_lambda)
        """
    def create_bucket(
        self,
        *,
        Bucket: str,
        ACL: BucketCannedACLType = None,
        CreateBucketConfiguration: "CreateBucketConfigurationTypeDef" = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWrite: str = None,
        GrantWriteACP: str = None,
        ObjectLockEnabledForBucket: bool = None,
        OutpostId: str = None
    ) -> CreateBucketResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.create_bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#create_bucket)
        """
    def create_job(
        self,
        *,
        AccountId: str,
        Operation: "JobOperationTypeDef",
        Report: "JobReportTypeDef",
        ClientRequestToken: str,
        Manifest: "JobManifestTypeDef",
        Priority: int,
        RoleArn: str,
        ConfirmationRequired: bool = None,
        Description: str = None,
        Tags: List["S3TagTypeDef"] = None
    ) -> CreateJobResultTypeDef:
        """
        You can use S3 Batch Operations to perform large-scale batch actions on Amazon
        S3 objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.create_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#create_job)
        """
    def create_multi_region_access_point(
        self,
        *,
        AccountId: str,
        ClientToken: str,
        Details: "CreateMultiRegionAccessPointInputTypeDef"
    ) -> CreateMultiRegionAccessPointResultTypeDef:
        """
        Creates a Multi-Region Access Point and associates it with the specified
        buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.create_multi_region_access_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#create_multi_region_access_point)
        """
    def delete_access_point(self, *, AccountId: str, Name: str) -> None:
        """
        Deletes the specified access point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.delete_access_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_access_point)
        """
    def delete_access_point_for_object_lambda(self, *, AccountId: str, Name: str) -> None:
        """
        Deletes the specified Object Lambda Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.delete_access_point_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_access_point_for_object_lambda)
        """
    def delete_access_point_policy(self, *, AccountId: str, Name: str) -> None:
        """
        Deletes the access point policy for the specified access point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.delete_access_point_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_access_point_policy)
        """
    def delete_access_point_policy_for_object_lambda(self, *, AccountId: str, Name: str) -> None:
        """
        Removes the resource policy for an Object Lambda Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.delete_access_point_policy_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_access_point_policy_for_object_lambda)
        """
    def delete_bucket(self, *, AccountId: str, Bucket: str) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.delete_bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_bucket)
        """
    def delete_bucket_lifecycle_configuration(self, *, AccountId: str, Bucket: str) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.delete_bucket_lifecycle_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_bucket_lifecycle_configuration)
        """
    def delete_bucket_policy(self, *, AccountId: str, Bucket: str) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.delete_bucket_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_bucket_policy)
        """
    def delete_bucket_tagging(self, *, AccountId: str, Bucket: str) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.delete_bucket_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_bucket_tagging)
        """
    def delete_job_tagging(self, *, AccountId: str, JobId: str) -> Dict[str, Any]:
        """
        Removes the entire tag set from the specified S3 Batch Operations job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.delete_job_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_job_tagging)
        """
    def delete_multi_region_access_point(
        self,
        *,
        AccountId: str,
        ClientToken: str,
        Details: "DeleteMultiRegionAccessPointInputTypeDef"
    ) -> DeleteMultiRegionAccessPointResultTypeDef:
        """
        Deletes a Multi-Region Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.delete_multi_region_access_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_multi_region_access_point)
        """
    def delete_public_access_block(self, *, AccountId: str) -> None:
        """
        Removes the `PublicAccessBlock` configuration for an Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.delete_public_access_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_public_access_block)
        """
    def delete_storage_lens_configuration(self, *, ConfigId: str, AccountId: str) -> None:
        """
        Deletes the Amazon S3 Storage Lens configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.delete_storage_lens_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_storage_lens_configuration)
        """
    def delete_storage_lens_configuration_tagging(
        self, *, ConfigId: str, AccountId: str
    ) -> Dict[str, Any]:
        """
        Deletes the Amazon S3 Storage Lens configuration tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.delete_storage_lens_configuration_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_storage_lens_configuration_tagging)
        """
    def describe_job(self, *, AccountId: str, JobId: str) -> DescribeJobResultTypeDef:
        """
        Retrieves the configuration parameters and status for a Batch Operations job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.describe_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#describe_job)
        """
    def describe_multi_region_access_point_operation(
        self, *, AccountId: str, RequestTokenARN: str
    ) -> DescribeMultiRegionAccessPointOperationResultTypeDef:
        """
        Retrieves the status of an asynchronous request to manage a Multi-Region Access
        Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.describe_multi_region_access_point_operation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#describe_multi_region_access_point_operation)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#generate_presigned_url)
        """
    def get_access_point(self, *, AccountId: str, Name: str) -> GetAccessPointResultTypeDef:
        """
        Returns configuration information about the specified access point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.get_access_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_access_point)
        """
    def get_access_point_configuration_for_object_lambda(
        self, *, AccountId: str, Name: str
    ) -> GetAccessPointConfigurationForObjectLambdaResultTypeDef:
        """
        Returns configuration for an Object Lambda Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.get_access_point_configuration_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_access_point_configuration_for_object_lambda)
        """
    def get_access_point_for_object_lambda(
        self, *, AccountId: str, Name: str
    ) -> GetAccessPointForObjectLambdaResultTypeDef:
        """
        Returns configuration information about the specified Object Lambda Access Point
        The following actions are related to `GetAccessPointForObjectLambda`  *
        `CreateAccessPointForObjectLambda <https://docs.aws.amazon.com/AmazonS3/latest/A
        PI/API_control_CreateAccessPointForObjectLambda.htm...`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.get_access_point_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_access_point_for_object_lambda)
        """
    def get_access_point_policy(
        self, *, AccountId: str, Name: str
    ) -> GetAccessPointPolicyResultTypeDef:
        """
        Returns the access point policy associated with the specified access point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.get_access_point_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_access_point_policy)
        """
    def get_access_point_policy_for_object_lambda(
        self, *, AccountId: str, Name: str
    ) -> GetAccessPointPolicyForObjectLambdaResultTypeDef:
        """
        Returns the resource policy for an Object Lambda Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.get_access_point_policy_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_access_point_policy_for_object_lambda)
        """
    def get_access_point_policy_status(
        self, *, AccountId: str, Name: str
    ) -> GetAccessPointPolicyStatusResultTypeDef:
        """
        Indicates whether the specified access point currently has a policy that allows
        public access.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.get_access_point_policy_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_access_point_policy_status)
        """
    def get_access_point_policy_status_for_object_lambda(
        self, *, AccountId: str, Name: str
    ) -> GetAccessPointPolicyStatusForObjectLambdaResultTypeDef:
        """
        Returns the status of the resource policy associated with an Object Lambda
        Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.get_access_point_policy_status_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_access_point_policy_status_for_object_lambda)
        """
    def get_bucket(self, *, AccountId: str, Bucket: str) -> GetBucketResultTypeDef:
        """
        Gets an Amazon S3 on Outposts bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.get_bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_bucket)
        """
    def get_bucket_lifecycle_configuration(
        self, *, AccountId: str, Bucket: str
    ) -> GetBucketLifecycleConfigurationResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.get_bucket_lifecycle_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_bucket_lifecycle_configuration)
        """
    def get_bucket_policy(self, *, AccountId: str, Bucket: str) -> GetBucketPolicyResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.get_bucket_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_bucket_policy)
        """
    def get_bucket_tagging(self, *, AccountId: str, Bucket: str) -> GetBucketTaggingResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.get_bucket_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_bucket_tagging)
        """
    def get_job_tagging(self, *, AccountId: str, JobId: str) -> GetJobTaggingResultTypeDef:
        """
        Returns the tags on an S3 Batch Operations job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.get_job_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_job_tagging)
        """
    def get_multi_region_access_point(
        self, *, AccountId: str, Name: str
    ) -> GetMultiRegionAccessPointResultTypeDef:
        """
        Returns configuration information about the specified Multi-Region Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.get_multi_region_access_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_multi_region_access_point)
        """
    def get_multi_region_access_point_policy(
        self, *, AccountId: str, Name: str
    ) -> GetMultiRegionAccessPointPolicyResultTypeDef:
        """
        Returns the access control policy of the specified Multi-Region Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.get_multi_region_access_point_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_multi_region_access_point_policy)
        """
    def get_multi_region_access_point_policy_status(
        self, *, AccountId: str, Name: str
    ) -> GetMultiRegionAccessPointPolicyStatusResultTypeDef:
        """
        Indicates whether the specified Multi-Region Access Point has an access control
        policy that allows public access.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.get_multi_region_access_point_policy_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_multi_region_access_point_policy_status)
        """
    def get_public_access_block(self, *, AccountId: str) -> GetPublicAccessBlockOutputTypeDef:
        """
        Retrieves the `PublicAccessBlock` configuration for an Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.get_public_access_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_public_access_block)
        """
    def get_storage_lens_configuration(
        self, *, ConfigId: str, AccountId: str
    ) -> GetStorageLensConfigurationResultTypeDef:
        """
        Gets the Amazon S3 Storage Lens configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.get_storage_lens_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_storage_lens_configuration)
        """
    def get_storage_lens_configuration_tagging(
        self, *, ConfigId: str, AccountId: str
    ) -> GetStorageLensConfigurationTaggingResultTypeDef:
        """
        Gets the tags of Amazon S3 Storage Lens configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.get_storage_lens_configuration_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_storage_lens_configuration_tagging)
        """
    def list_access_points(
        self, *, AccountId: str, Bucket: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListAccessPointsResultTypeDef:
        """
        Returns a list of the access points currently associated with the specified
        bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.list_access_points)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#list_access_points)
        """
    def list_access_points_for_object_lambda(
        self, *, AccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAccessPointsForObjectLambdaResultTypeDef:
        """
        Returns a list of the access points associated with the Object Lambda Access
        Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.list_access_points_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#list_access_points_for_object_lambda)
        """
    def list_jobs(
        self,
        *,
        AccountId: str,
        JobStatuses: List[JobStatusType] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListJobsResultTypeDef:
        """
        Lists current S3 Batch Operations jobs and jobs that have ended within the last
        30 days for the Amazon Web Services account making the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.list_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#list_jobs)
        """
    def list_multi_region_access_points(
        self, *, AccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListMultiRegionAccessPointsResultTypeDef:
        """
        Returns a list of the Multi-Region Access Points currently associated with the
        specified Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.list_multi_region_access_points)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#list_multi_region_access_points)
        """
    def list_regional_buckets(
        self,
        *,
        AccountId: str,
        NextToken: str = None,
        MaxResults: int = None,
        OutpostId: str = None
    ) -> ListRegionalBucketsResultTypeDef:
        """
        Returns a list of all Outposts buckets in an Outpost that are owned by the
        authenticated sender of the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.list_regional_buckets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#list_regional_buckets)
        """
    def list_storage_lens_configurations(
        self, *, AccountId: str, NextToken: str = None
    ) -> ListStorageLensConfigurationsResultTypeDef:
        """
        Gets a list of Amazon S3 Storage Lens configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.list_storage_lens_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#list_storage_lens_configurations)
        """
    def put_access_point_configuration_for_object_lambda(
        self, *, AccountId: str, Name: str, Configuration: "ObjectLambdaConfigurationTypeDef"
    ) -> None:
        """
        Replaces configuration for an Object Lambda Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.put_access_point_configuration_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put_access_point_configuration_for_object_lambda)
        """
    def put_access_point_policy(self, *, AccountId: str, Name: str, Policy: str) -> None:
        """
        Associates an access policy with the specified access point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.put_access_point_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put_access_point_policy)
        """
    def put_access_point_policy_for_object_lambda(
        self, *, AccountId: str, Name: str, Policy: str
    ) -> None:
        """
        Creates or replaces resource policy for an Object Lambda Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.put_access_point_policy_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put_access_point_policy_for_object_lambda)
        """
    def put_bucket_lifecycle_configuration(
        self,
        *,
        AccountId: str,
        Bucket: str,
        LifecycleConfiguration: "LifecycleConfigurationTypeDef" = None
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.put_bucket_lifecycle_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put_bucket_lifecycle_configuration)
        """
    def put_bucket_policy(
        self,
        *,
        AccountId: str,
        Bucket: str,
        Policy: str,
        ConfirmRemoveSelfBucketAccess: bool = None
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.put_bucket_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put_bucket_policy)
        """
    def put_bucket_tagging(self, *, AccountId: str, Bucket: str, Tagging: "TaggingTypeDef") -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.put_bucket_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put_bucket_tagging)
        """
    def put_job_tagging(
        self, *, AccountId: str, JobId: str, Tags: List["S3TagTypeDef"]
    ) -> Dict[str, Any]:
        """
        Sets the supplied tag-set on an S3 Batch Operations job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.put_job_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put_job_tagging)
        """
    def put_multi_region_access_point_policy(
        self,
        *,
        AccountId: str,
        ClientToken: str,
        Details: "PutMultiRegionAccessPointPolicyInputTypeDef"
    ) -> PutMultiRegionAccessPointPolicyResultTypeDef:
        """
        Associates an access control policy with the specified Multi-Region Access
        Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.put_multi_region_access_point_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put_multi_region_access_point_policy)
        """
    def put_public_access_block(
        self,
        *,
        PublicAccessBlockConfiguration: "PublicAccessBlockConfigurationTypeDef",
        AccountId: str
    ) -> None:
        """
        Creates or modifies the `PublicAccessBlock` configuration for an Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.put_public_access_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put_public_access_block)
        """
    def put_storage_lens_configuration(
        self,
        *,
        ConfigId: str,
        AccountId: str,
        StorageLensConfiguration: "StorageLensConfigurationTypeDef",
        Tags: List["StorageLensTagTypeDef"] = None
    ) -> None:
        """
        Puts an Amazon S3 Storage Lens configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.put_storage_lens_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put_storage_lens_configuration)
        """
    def put_storage_lens_configuration_tagging(
        self, *, ConfigId: str, AccountId: str, Tags: List["StorageLensTagTypeDef"]
    ) -> Dict[str, Any]:
        """
        Put or replace tags on an existing Amazon S3 Storage Lens configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.put_storage_lens_configuration_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put_storage_lens_configuration_tagging)
        """
    def update_job_priority(
        self, *, AccountId: str, JobId: str, Priority: int
    ) -> UpdateJobPriorityResultTypeDef:
        """
        Updates an existing S3 Batch Operations job's priority.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.update_job_priority)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#update_job_priority)
        """
    def update_job_status(
        self,
        *,
        AccountId: str,
        JobId: str,
        RequestedJobStatus: RequestedJobStatusType,
        StatusUpdateReason: str = None
    ) -> UpdateJobStatusResultTypeDef:
        """
        Updates the status for the specified job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Client.update_job_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#update_job_status)
        """
    def get_paginator(
        self, operation_name: Literal["list_access_points_for_object_lambda"]
    ) -> ListAccessPointsForObjectLambdaPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/s3control.html#S3Control.Paginator.ListAccessPointsForObjectLambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/paginators.html#listaccesspointsforobjectlambdapaginator)
        """
