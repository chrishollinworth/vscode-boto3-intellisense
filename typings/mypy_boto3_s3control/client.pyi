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

from .literals import (
    BucketCannedACLType,
    GranteeTypeType,
    JobStatusType,
    PermissionType,
    PrivilegeType,
    RequestedJobStatusType,
)
from .paginator import ListAccessPointsForObjectLambdaPaginator
from .type_defs import (
    AccessGrantsLocationConfigurationTypeDef,
    CreateAccessGrantResultTypeDef,
    CreateAccessGrantsInstanceResultTypeDef,
    CreateAccessGrantsLocationResultTypeDef,
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
    GetAccessGrantResultTypeDef,
    GetAccessGrantsInstanceForPrefixResultTypeDef,
    GetAccessGrantsInstanceResourcePolicyResultTypeDef,
    GetAccessGrantsInstanceResultTypeDef,
    GetAccessGrantsLocationResultTypeDef,
    GetAccessPointConfigurationForObjectLambdaResultTypeDef,
    GetAccessPointForObjectLambdaResultTypeDef,
    GetAccessPointPolicyForObjectLambdaResultTypeDef,
    GetAccessPointPolicyResultTypeDef,
    GetAccessPointPolicyStatusForObjectLambdaResultTypeDef,
    GetAccessPointPolicyStatusResultTypeDef,
    GetAccessPointResultTypeDef,
    GetBucketLifecycleConfigurationResultTypeDef,
    GetBucketPolicyResultTypeDef,
    GetBucketReplicationResultTypeDef,
    GetBucketResultTypeDef,
    GetBucketTaggingResultTypeDef,
    GetBucketVersioningResultTypeDef,
    GetDataAccessResultTypeDef,
    GetJobTaggingResultTypeDef,
    GetMultiRegionAccessPointPolicyResultTypeDef,
    GetMultiRegionAccessPointPolicyStatusResultTypeDef,
    GetMultiRegionAccessPointResultTypeDef,
    GetMultiRegionAccessPointRoutesResultTypeDef,
    GetPublicAccessBlockOutputTypeDef,
    GetStorageLensConfigurationResultTypeDef,
    GetStorageLensConfigurationTaggingResultTypeDef,
    GetStorageLensGroupResultTypeDef,
    GranteeTypeDef,
    JobManifestGeneratorTypeDef,
    JobManifestTypeDef,
    JobOperationTypeDef,
    JobReportTypeDef,
    LifecycleConfigurationTypeDef,
    ListAccessGrantsInstancesResultTypeDef,
    ListAccessGrantsLocationsResultTypeDef,
    ListAccessGrantsResultTypeDef,
    ListAccessPointsForObjectLambdaResultTypeDef,
    ListAccessPointsResultTypeDef,
    ListJobsResultTypeDef,
    ListMultiRegionAccessPointsResultTypeDef,
    ListRegionalBucketsResultTypeDef,
    ListStorageLensConfigurationsResultTypeDef,
    ListStorageLensGroupsResultTypeDef,
    ListTagsForResourceResultTypeDef,
    MultiRegionAccessPointRouteTypeDef,
    ObjectLambdaConfigurationTypeDef,
    PublicAccessBlockConfigurationTypeDef,
    PutAccessGrantsInstanceResourcePolicyResultTypeDef,
    PutMultiRegionAccessPointPolicyInputTypeDef,
    PutMultiRegionAccessPointPolicyResultTypeDef,
    ReplicationConfigurationTypeDef,
    S3TagTypeDef,
    StorageLensConfigurationTypeDef,
    StorageLensGroupTypeDef,
    StorageLensTagTypeDef,
    TaggingTypeDef,
    TagTypeDef,
    UpdateAccessGrantsLocationResultTypeDef,
    UpdateJobPriorityResultTypeDef,
    UpdateJobStatusResultTypeDef,
    VersioningConfigurationTypeDef,
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        S3ControlClient exceptions.
        """
    def associate_access_grants_identity_center(
        self, *, AccountId: str, IdentityCenterArn: str
    ) -> None:
        """
        Associate your S3 Access Grants instance with an Amazon Web Services IAM
        Identity Center instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.associate_access_grants_identity_center)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#associate_access_grants_identity_center)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#close)
        """
    def create_access_grant(
        self,
        *,
        AccountId: str,
        AccessGrantsLocationId: str,
        Grantee: "GranteeTypeDef",
        Permission: PermissionType,
        AccessGrantsLocationConfiguration: "AccessGrantsLocationConfigurationTypeDef" = None,
        ApplicationArn: str = None,
        S3PrefixType: Literal["Object"] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateAccessGrantResultTypeDef:
        """
        Creates an access grant that gives a grantee access to your S3 data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.create_access_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#create_access_grant)
        """
    def create_access_grants_instance(
        self, *, AccountId: str, IdentityCenterArn: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateAccessGrantsInstanceResultTypeDef:
        """
        Creates an S3 Access Grants instance, which serves as a logical grouping for
        access grants.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.create_access_grants_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#create_access_grants_instance)
        """
    def create_access_grants_location(
        self,
        *,
        AccountId: str,
        LocationScope: str,
        IAMRoleArn: str,
        Tags: List["TagTypeDef"] = None
    ) -> CreateAccessGrantsLocationResultTypeDef:
        """
        The S3 data location that you would like to register in your S3 Access Grants
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.create_access_grants_location)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#create_access_grants_location)
        """
    def create_access_point(
        self,
        *,
        AccountId: str,
        Name: str,
        Bucket: str,
        VpcConfiguration: "VpcConfigurationTypeDef" = None,
        PublicAccessBlockConfiguration: "PublicAccessBlockConfigurationTypeDef" = None,
        BucketAccountId: str = None
    ) -> CreateAccessPointResultTypeDef:
        """
        Creates an access point and associates it with the specified bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.create_access_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#create_access_point)
        """
    def create_access_point_for_object_lambda(
        self, *, AccountId: str, Name: str, Configuration: "ObjectLambdaConfigurationTypeDef"
    ) -> CreateAccessPointForObjectLambdaResultTypeDef:
        """
        Creates an Object Lambda Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.create_access_point_for_object_lambda)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.create_bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#create_bucket)
        """
    def create_job(
        self,
        *,
        AccountId: str,
        Operation: "JobOperationTypeDef",
        Report: "JobReportTypeDef",
        ClientRequestToken: str,
        Priority: int,
        RoleArn: str,
        ConfirmationRequired: bool = None,
        Manifest: "JobManifestTypeDef" = None,
        Description: str = None,
        Tags: List["S3TagTypeDef"] = None,
        ManifestGenerator: "JobManifestGeneratorTypeDef" = None
    ) -> CreateJobResultTypeDef:
        """
        You can use S3 Batch Operations to perform large-scale batch actions on Amazon
        S3 objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.create_job)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.create_multi_region_access_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#create_multi_region_access_point)
        """
    def create_storage_lens_group(
        self,
        *,
        AccountId: str,
        StorageLensGroup: "StorageLensGroupTypeDef",
        Tags: List["TagTypeDef"] = None
    ) -> None:
        """
        Creates a new S3 Storage Lens group and associates it with the specified Amazon
        Web Services account ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.create_storage_lens_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#create_storage_lens_group)
        """
    def delete_access_grant(self, *, AccountId: str, AccessGrantId: str) -> None:
        """
        Deletes the access grant from the S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.delete_access_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_access_grant)
        """
    def delete_access_grants_instance(self, *, AccountId: str) -> None:
        """
        Deletes your S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.delete_access_grants_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_access_grants_instance)
        """
    def delete_access_grants_instance_resource_policy(self, *, AccountId: str) -> None:
        """
        Deletes the resource policy of the S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.delete_access_grants_instance_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_access_grants_instance_resource_policy)
        """
    def delete_access_grants_location(self, *, AccountId: str, AccessGrantsLocationId: str) -> None:
        """
        Deregisters a location from your S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.delete_access_grants_location)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_access_grants_location)
        """
    def delete_access_point(self, *, AccountId: str, Name: str) -> None:
        """
        Deletes the specified access point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.delete_access_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_access_point)
        """
    def delete_access_point_for_object_lambda(self, *, AccountId: str, Name: str) -> None:
        """
        Deletes the specified Object Lambda Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.delete_access_point_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_access_point_for_object_lambda)
        """
    def delete_access_point_policy(self, *, AccountId: str, Name: str) -> None:
        """
        Deletes the access point policy for the specified access point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.delete_access_point_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_access_point_policy)
        """
    def delete_access_point_policy_for_object_lambda(self, *, AccountId: str, Name: str) -> None:
        """
        Removes the resource policy for an Object Lambda Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.delete_access_point_policy_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_access_point_policy_for_object_lambda)
        """
    def delete_bucket(self, *, AccountId: str, Bucket: str) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.delete_bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_bucket)
        """
    def delete_bucket_lifecycle_configuration(self, *, AccountId: str, Bucket: str) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.delete_bucket_lifecycle_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_bucket_lifecycle_configuration)
        """
    def delete_bucket_policy(self, *, AccountId: str, Bucket: str) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.delete_bucket_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_bucket_policy)
        """
    def delete_bucket_replication(self, *, AccountId: str, Bucket: str) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.delete_bucket_replication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_bucket_replication)
        """
    def delete_bucket_tagging(self, *, AccountId: str, Bucket: str) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.delete_bucket_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_bucket_tagging)
        """
    def delete_job_tagging(self, *, AccountId: str, JobId: str) -> Dict[str, Any]:
        """
        Removes the entire tag set from the specified S3 Batch Operations job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.delete_job_tagging)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.delete_multi_region_access_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_multi_region_access_point)
        """
    def delete_public_access_block(self, *, AccountId: str) -> None:
        """
        Removes the `PublicAccessBlock` configuration for an Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.delete_public_access_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_public_access_block)
        """
    def delete_storage_lens_configuration(self, *, ConfigId: str, AccountId: str) -> None:
        """
        Deletes the Amazon S3 Storage Lens configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.delete_storage_lens_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_storage_lens_configuration)
        """
    def delete_storage_lens_configuration_tagging(
        self, *, ConfigId: str, AccountId: str
    ) -> Dict[str, Any]:
        """
        Deletes the Amazon S3 Storage Lens configuration tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.delete_storage_lens_configuration_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_storage_lens_configuration_tagging)
        """
    def delete_storage_lens_group(self, *, Name: str, AccountId: str) -> None:
        """
        Deletes an existing S3 Storage Lens group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.delete_storage_lens_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#delete_storage_lens_group)
        """
    def describe_job(self, *, AccountId: str, JobId: str) -> DescribeJobResultTypeDef:
        """
        Retrieves the configuration parameters and status for a Batch Operations job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.describe_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#describe_job)
        """
    def describe_multi_region_access_point_operation(
        self, *, AccountId: str, RequestTokenARN: str
    ) -> DescribeMultiRegionAccessPointOperationResultTypeDef:
        """
        Retrieves the status of an asynchronous request to manage a Multi-Region Access
        Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.describe_multi_region_access_point_operation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#describe_multi_region_access_point_operation)
        """
    def dissociate_access_grants_identity_center(self, *, AccountId: str) -> None:
        """
        Dissociates the Amazon Web Services IAM Identity Center instance from the S3
        Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.dissociate_access_grants_identity_center)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#dissociate_access_grants_identity_center)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#generate_presigned_url)
        """
    def get_access_grant(
        self, *, AccountId: str, AccessGrantId: str
    ) -> GetAccessGrantResultTypeDef:
        """
        Get the details of an access grant from your S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_access_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_access_grant)
        """
    def get_access_grants_instance(self, *, AccountId: str) -> GetAccessGrantsInstanceResultTypeDef:
        """
        Retrieves the S3 Access Grants instance for a Region in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_access_grants_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_access_grants_instance)
        """
    def get_access_grants_instance_for_prefix(
        self, *, AccountId: str, S3Prefix: str
    ) -> GetAccessGrantsInstanceForPrefixResultTypeDef:
        """
        Retrieve the S3 Access Grants instance that contains a particular prefix.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_access_grants_instance_for_prefix)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_access_grants_instance_for_prefix)
        """
    def get_access_grants_instance_resource_policy(
        self, *, AccountId: str
    ) -> GetAccessGrantsInstanceResourcePolicyResultTypeDef:
        """
        Returns the resource policy of the S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_access_grants_instance_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_access_grants_instance_resource_policy)
        """
    def get_access_grants_location(
        self, *, AccountId: str, AccessGrantsLocationId: str
    ) -> GetAccessGrantsLocationResultTypeDef:
        """
        Retrieves the details of a particular location registered in your S3 Access
        Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_access_grants_location)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_access_grants_location)
        """
    def get_access_point(self, *, AccountId: str, Name: str) -> GetAccessPointResultTypeDef:
        """
        Returns configuration information about the specified access point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_access_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_access_point)
        """
    def get_access_point_configuration_for_object_lambda(
        self, *, AccountId: str, Name: str
    ) -> GetAccessPointConfigurationForObjectLambdaResultTypeDef:
        """
        Returns configuration for an Object Lambda Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_access_point_configuration_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_access_point_configuration_for_object_lambda)
        """
    def get_access_point_for_object_lambda(
        self, *, AccountId: str, Name: str
    ) -> GetAccessPointForObjectLambdaResultTypeDef:
        """
        Returns configuration information about the specified Object Lambda Access Point
        The following actions are related to `GetAccessPointForObjectLambda` *
        `CreateAccessPointForObjectLambda <https://docs.aws.amazon.com/AmazonS3/latest/A
        PI/API_control_CreateAccessPointForObjectLambda.html>...`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_access_point_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_access_point_for_object_lambda)
        """
    def get_access_point_policy(
        self, *, AccountId: str, Name: str
    ) -> GetAccessPointPolicyResultTypeDef:
        """
        Returns the access point policy associated with the specified access point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_access_point_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_access_point_policy)
        """
    def get_access_point_policy_for_object_lambda(
        self, *, AccountId: str, Name: str
    ) -> GetAccessPointPolicyForObjectLambdaResultTypeDef:
        """
        Returns the resource policy for an Object Lambda Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_access_point_policy_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_access_point_policy_for_object_lambda)
        """
    def get_access_point_policy_status(
        self, *, AccountId: str, Name: str
    ) -> GetAccessPointPolicyStatusResultTypeDef:
        """
        Indicates whether the specified access point currently has a policy that allows
        public access.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_access_point_policy_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_access_point_policy_status)
        """
    def get_access_point_policy_status_for_object_lambda(
        self, *, AccountId: str, Name: str
    ) -> GetAccessPointPolicyStatusForObjectLambdaResultTypeDef:
        """
        Returns the status of the resource policy associated with an Object Lambda
        Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_access_point_policy_status_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_access_point_policy_status_for_object_lambda)
        """
    def get_bucket(self, *, AccountId: str, Bucket: str) -> GetBucketResultTypeDef:
        """
        Gets an Amazon S3 on Outposts bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_bucket)
        """
    def get_bucket_lifecycle_configuration(
        self, *, AccountId: str, Bucket: str
    ) -> GetBucketLifecycleConfigurationResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_bucket_lifecycle_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_bucket_lifecycle_configuration)
        """
    def get_bucket_policy(self, *, AccountId: str, Bucket: str) -> GetBucketPolicyResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_bucket_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_bucket_policy)
        """
    def get_bucket_replication(
        self, *, AccountId: str, Bucket: str
    ) -> GetBucketReplicationResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_bucket_replication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_bucket_replication)
        """
    def get_bucket_tagging(self, *, AccountId: str, Bucket: str) -> GetBucketTaggingResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_bucket_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_bucket_tagging)
        """
    def get_bucket_versioning(
        self, *, AccountId: str, Bucket: str
    ) -> GetBucketVersioningResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_bucket_versioning)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_bucket_versioning)
        """
    def get_data_access(
        self,
        *,
        AccountId: str,
        Target: str,
        Permission: PermissionType,
        DurationSeconds: int = None,
        Privilege: PrivilegeType = None,
        TargetType: Literal["Object"] = None
    ) -> GetDataAccessResultTypeDef:
        """
        Returns a temporary access credential from S3 Access Grants to the grantee or
        client application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_data_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_data_access)
        """
    def get_job_tagging(self, *, AccountId: str, JobId: str) -> GetJobTaggingResultTypeDef:
        """
        Returns the tags on an S3 Batch Operations job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_job_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_job_tagging)
        """
    def get_multi_region_access_point(
        self, *, AccountId: str, Name: str
    ) -> GetMultiRegionAccessPointResultTypeDef:
        """
        Returns configuration information about the specified Multi-Region Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_multi_region_access_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_multi_region_access_point)
        """
    def get_multi_region_access_point_policy(
        self, *, AccountId: str, Name: str
    ) -> GetMultiRegionAccessPointPolicyResultTypeDef:
        """
        Returns the access control policy of the specified Multi-Region Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_multi_region_access_point_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_multi_region_access_point_policy)
        """
    def get_multi_region_access_point_policy_status(
        self, *, AccountId: str, Name: str
    ) -> GetMultiRegionAccessPointPolicyStatusResultTypeDef:
        """
        Indicates whether the specified Multi-Region Access Point has an access control
        policy that allows public access.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_multi_region_access_point_policy_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_multi_region_access_point_policy_status)
        """
    def get_multi_region_access_point_routes(
        self, *, AccountId: str, Mrap: str
    ) -> GetMultiRegionAccessPointRoutesResultTypeDef:
        """
        Returns the routing configuration for a Multi-Region Access Point, indicating
        which Regions are active or passive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_multi_region_access_point_routes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_multi_region_access_point_routes)
        """
    def get_public_access_block(self, *, AccountId: str) -> GetPublicAccessBlockOutputTypeDef:
        """
        Retrieves the `PublicAccessBlock` configuration for an Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_public_access_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_public_access_block)
        """
    def get_storage_lens_configuration(
        self, *, ConfigId: str, AccountId: str
    ) -> GetStorageLensConfigurationResultTypeDef:
        """
        Gets the Amazon S3 Storage Lens configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_storage_lens_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_storage_lens_configuration)
        """
    def get_storage_lens_configuration_tagging(
        self, *, ConfigId: str, AccountId: str
    ) -> GetStorageLensConfigurationTaggingResultTypeDef:
        """
        Gets the tags of Amazon S3 Storage Lens configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_storage_lens_configuration_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_storage_lens_configuration_tagging)
        """
    def get_storage_lens_group(
        self, *, Name: str, AccountId: str
    ) -> GetStorageLensGroupResultTypeDef:
        """
        Retrieves the Storage Lens group configuration details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.get_storage_lens_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#get_storage_lens_group)
        """
    def list_access_grants(
        self,
        *,
        AccountId: str,
        NextToken: str = None,
        MaxResults: int = None,
        GranteeType: GranteeTypeType = None,
        GranteeIdentifier: str = None,
        Permission: PermissionType = None,
        GrantScope: str = None,
        ApplicationArn: str = None
    ) -> ListAccessGrantsResultTypeDef:
        """
        Returns the list of access grants in your S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.list_access_grants)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#list_access_grants)
        """
    def list_access_grants_instances(
        self, *, AccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAccessGrantsInstancesResultTypeDef:
        """
        Returns a list of S3 Access Grants instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.list_access_grants_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#list_access_grants_instances)
        """
    def list_access_grants_locations(
        self,
        *,
        AccountId: str,
        NextToken: str = None,
        MaxResults: int = None,
        LocationScope: str = None
    ) -> ListAccessGrantsLocationsResultTypeDef:
        """
        Returns a list of the locations registered in your S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.list_access_grants_locations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#list_access_grants_locations)
        """
    def list_access_points(
        self, *, AccountId: str, Bucket: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListAccessPointsResultTypeDef:
        """
        Returns a list of the access points that are owned by the current account that's
        associated with the specified bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.list_access_points)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#list_access_points)
        """
    def list_access_points_for_object_lambda(
        self, *, AccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAccessPointsForObjectLambdaResultTypeDef:
        """
        Returns some or all (up to 1,000) access points associated with the Object
        Lambda Access Point per call.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.list_access_points_for_object_lambda)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.list_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#list_jobs)
        """
    def list_multi_region_access_points(
        self, *, AccountId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListMultiRegionAccessPointsResultTypeDef:
        """
        Returns a list of the Multi-Region Access Points currently associated with the
        specified Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.list_multi_region_access_points)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.list_regional_buckets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#list_regional_buckets)
        """
    def list_storage_lens_configurations(
        self, *, AccountId: str, NextToken: str = None
    ) -> ListStorageLensConfigurationsResultTypeDef:
        """
        Gets a list of Amazon S3 Storage Lens configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.list_storage_lens_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#list_storage_lens_configurations)
        """
    def list_storage_lens_groups(
        self, *, AccountId: str, NextToken: str = None
    ) -> ListStorageLensGroupsResultTypeDef:
        """
        Lists all the Storage Lens groups in the specified home Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.list_storage_lens_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#list_storage_lens_groups)
        """
    def list_tags_for_resource(
        self, *, AccountId: str, ResourceArn: str
    ) -> ListTagsForResourceResultTypeDef:
        """
        This operation allows you to list all the Amazon Web Services resource tags for
        a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#list_tags_for_resource)
        """
    def put_access_grants_instance_resource_policy(
        self, *, AccountId: str, Policy: str, Organization: str = None
    ) -> PutAccessGrantsInstanceResourcePolicyResultTypeDef:
        """
        Updates the resource policy of the S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.put_access_grants_instance_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put_access_grants_instance_resource_policy)
        """
    def put_access_point_configuration_for_object_lambda(
        self, *, AccountId: str, Name: str, Configuration: "ObjectLambdaConfigurationTypeDef"
    ) -> None:
        """
        Replaces configuration for an Object Lambda Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.put_access_point_configuration_for_object_lambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put_access_point_configuration_for_object_lambda)
        """
    def put_access_point_policy(self, *, AccountId: str, Name: str, Policy: str) -> None:
        """
        Associates an access policy with the specified access point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.put_access_point_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put_access_point_policy)
        """
    def put_access_point_policy_for_object_lambda(
        self, *, AccountId: str, Name: str, Policy: str
    ) -> None:
        """
        Creates or replaces resource policy for an Object Lambda Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.put_access_point_policy_for_object_lambda)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.put_bucket_lifecycle_configuration)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.put_bucket_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put_bucket_policy)
        """
    def put_bucket_replication(
        self,
        *,
        AccountId: str,
        Bucket: str,
        ReplicationConfiguration: "ReplicationConfigurationTypeDef"
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.put_bucket_replication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put_bucket_replication)
        """
    def put_bucket_tagging(self, *, AccountId: str, Bucket: str, Tagging: "TaggingTypeDef") -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.put_bucket_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put_bucket_tagging)
        """
    def put_bucket_versioning(
        self,
        *,
        AccountId: str,
        Bucket: str,
        VersioningConfiguration: "VersioningConfigurationTypeDef",
        MFA: str = None
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.put_bucket_versioning)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put_bucket_versioning)
        """
    def put_job_tagging(
        self, *, AccountId: str, JobId: str, Tags: List["S3TagTypeDef"]
    ) -> Dict[str, Any]:
        """
        Sets the supplied tag-set on an S3 Batch Operations job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.put_job_tagging)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.put_multi_region_access_point_policy)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.put_public_access_block)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.put_storage_lens_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put_storage_lens_configuration)
        """
    def put_storage_lens_configuration_tagging(
        self, *, ConfigId: str, AccountId: str, Tags: List["StorageLensTagTypeDef"]
    ) -> Dict[str, Any]:
        """
        Put or replace tags on an existing Amazon S3 Storage Lens configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.put_storage_lens_configuration_tagging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#put_storage_lens_configuration_tagging)
        """
    def submit_multi_region_access_point_routes(
        self, *, AccountId: str, Mrap: str, RouteUpdates: List["MultiRegionAccessPointRouteTypeDef"]
    ) -> Dict[str, Any]:
        """
        Submits an updated route configuration for a Multi-Region Access Point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.submit_multi_region_access_point_routes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#submit_multi_region_access_point_routes)
        """
    def tag_resource(
        self, *, AccountId: str, ResourceArn: str, Tags: List["TagTypeDef"]
    ) -> Dict[str, Any]:
        """
        Creates a new Amazon Web Services resource tag or updates an existing resource
        tag.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#tag_resource)
        """
    def untag_resource(
        self, *, AccountId: str, ResourceArn: str, TagKeys: List[str]
    ) -> Dict[str, Any]:
        """
        This operation removes the specified Amazon Web Services resource tags from an
        S3 resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#untag_resource)
        """
    def update_access_grants_location(
        self, *, AccountId: str, AccessGrantsLocationId: str, IAMRoleArn: str
    ) -> UpdateAccessGrantsLocationResultTypeDef:
        """
        Updates the IAM role of a registered location in your S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.update_access_grants_location)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#update_access_grants_location)
        """
    def update_job_priority(
        self, *, AccountId: str, JobId: str, Priority: int
    ) -> UpdateJobPriorityResultTypeDef:
        """
        Updates an existing S3 Batch Operations job's priority.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.update_job_priority)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.update_job_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#update_job_status)
        """
    def update_storage_lens_group(
        self, *, Name: str, AccountId: str, StorageLensGroup: "StorageLensGroupTypeDef"
    ) -> None:
        """
        Updates the existing Storage Lens group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Client.update_storage_lens_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/client.html#update_storage_lens_group)
        """
    def get_paginator(
        self, operation_name: Literal["list_access_points_for_object_lambda"]
    ) -> ListAccessPointsForObjectLambdaPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/s3control.html#S3Control.Paginator.ListAccessPointsForObjectLambda)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/paginators.html#listaccesspointsforobjectlambdapaginator)
        """
