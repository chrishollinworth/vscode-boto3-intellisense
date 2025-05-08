"""
Type annotations for s3control service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_s3control.client import S3ControlClient

    session = Session()
    client: S3ControlClient = session.client("s3control")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAccessPointsForDirectoryBucketsPaginator,
    ListAccessPointsForObjectLambdaPaginator,
    ListCallerAccessGrantsPaginator,
)
from .type_defs import (
    AssociateAccessGrantsIdentityCenterRequestTypeDef,
    CreateAccessGrantRequestTypeDef,
    CreateAccessGrantResultTypeDef,
    CreateAccessGrantsInstanceRequestTypeDef,
    CreateAccessGrantsInstanceResultTypeDef,
    CreateAccessGrantsLocationRequestTypeDef,
    CreateAccessGrantsLocationResultTypeDef,
    CreateAccessPointForObjectLambdaRequestTypeDef,
    CreateAccessPointForObjectLambdaResultTypeDef,
    CreateAccessPointRequestTypeDef,
    CreateAccessPointResultTypeDef,
    CreateBucketRequestTypeDef,
    CreateBucketResultTypeDef,
    CreateJobRequestTypeDef,
    CreateJobResultTypeDef,
    CreateMultiRegionAccessPointRequestTypeDef,
    CreateMultiRegionAccessPointResultTypeDef,
    CreateStorageLensGroupRequestTypeDef,
    DeleteAccessGrantRequestTypeDef,
    DeleteAccessGrantsInstanceRequestTypeDef,
    DeleteAccessGrantsInstanceResourcePolicyRequestTypeDef,
    DeleteAccessGrantsLocationRequestTypeDef,
    DeleteAccessPointForObjectLambdaRequestTypeDef,
    DeleteAccessPointPolicyForObjectLambdaRequestTypeDef,
    DeleteAccessPointPolicyRequestTypeDef,
    DeleteAccessPointRequestTypeDef,
    DeleteAccessPointScopeRequestTypeDef,
    DeleteBucketLifecycleConfigurationRequestTypeDef,
    DeleteBucketPolicyRequestTypeDef,
    DeleteBucketReplicationRequestTypeDef,
    DeleteBucketRequestTypeDef,
    DeleteBucketTaggingRequestTypeDef,
    DeleteJobTaggingRequestTypeDef,
    DeleteMultiRegionAccessPointRequestTypeDef,
    DeleteMultiRegionAccessPointResultTypeDef,
    DeletePublicAccessBlockRequestTypeDef,
    DeleteStorageLensConfigurationRequestTypeDef,
    DeleteStorageLensConfigurationTaggingRequestTypeDef,
    DeleteStorageLensGroupRequestTypeDef,
    DescribeJobRequestTypeDef,
    DescribeJobResultTypeDef,
    DescribeMultiRegionAccessPointOperationRequestTypeDef,
    DescribeMultiRegionAccessPointOperationResultTypeDef,
    DissociateAccessGrantsIdentityCenterRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAccessGrantRequestTypeDef,
    GetAccessGrantResultTypeDef,
    GetAccessGrantsInstanceForPrefixRequestTypeDef,
    GetAccessGrantsInstanceForPrefixResultTypeDef,
    GetAccessGrantsInstanceRequestTypeDef,
    GetAccessGrantsInstanceResourcePolicyRequestTypeDef,
    GetAccessGrantsInstanceResourcePolicyResultTypeDef,
    GetAccessGrantsInstanceResultTypeDef,
    GetAccessGrantsLocationRequestTypeDef,
    GetAccessGrantsLocationResultTypeDef,
    GetAccessPointConfigurationForObjectLambdaRequestTypeDef,
    GetAccessPointConfigurationForObjectLambdaResultTypeDef,
    GetAccessPointForObjectLambdaRequestTypeDef,
    GetAccessPointForObjectLambdaResultTypeDef,
    GetAccessPointPolicyForObjectLambdaRequestTypeDef,
    GetAccessPointPolicyForObjectLambdaResultTypeDef,
    GetAccessPointPolicyRequestTypeDef,
    GetAccessPointPolicyResultTypeDef,
    GetAccessPointPolicyStatusForObjectLambdaRequestTypeDef,
    GetAccessPointPolicyStatusForObjectLambdaResultTypeDef,
    GetAccessPointPolicyStatusRequestTypeDef,
    GetAccessPointPolicyStatusResultTypeDef,
    GetAccessPointRequestTypeDef,
    GetAccessPointResultTypeDef,
    GetAccessPointScopeRequestTypeDef,
    GetAccessPointScopeResultTypeDef,
    GetBucketLifecycleConfigurationRequestTypeDef,
    GetBucketLifecycleConfigurationResultTypeDef,
    GetBucketPolicyRequestTypeDef,
    GetBucketPolicyResultTypeDef,
    GetBucketReplicationRequestTypeDef,
    GetBucketReplicationResultTypeDef,
    GetBucketRequestTypeDef,
    GetBucketResultTypeDef,
    GetBucketTaggingRequestTypeDef,
    GetBucketTaggingResultTypeDef,
    GetBucketVersioningRequestTypeDef,
    GetBucketVersioningResultTypeDef,
    GetDataAccessRequestTypeDef,
    GetDataAccessResultTypeDef,
    GetJobTaggingRequestTypeDef,
    GetJobTaggingResultTypeDef,
    GetMultiRegionAccessPointPolicyRequestTypeDef,
    GetMultiRegionAccessPointPolicyResultTypeDef,
    GetMultiRegionAccessPointPolicyStatusRequestTypeDef,
    GetMultiRegionAccessPointPolicyStatusResultTypeDef,
    GetMultiRegionAccessPointRequestTypeDef,
    GetMultiRegionAccessPointResultTypeDef,
    GetMultiRegionAccessPointRoutesRequestTypeDef,
    GetMultiRegionAccessPointRoutesResultTypeDef,
    GetPublicAccessBlockOutputTypeDef,
    GetPublicAccessBlockRequestTypeDef,
    GetStorageLensConfigurationRequestTypeDef,
    GetStorageLensConfigurationResultTypeDef,
    GetStorageLensConfigurationTaggingRequestTypeDef,
    GetStorageLensConfigurationTaggingResultTypeDef,
    GetStorageLensGroupRequestTypeDef,
    GetStorageLensGroupResultTypeDef,
    ListAccessGrantsInstancesRequestTypeDef,
    ListAccessGrantsInstancesResultTypeDef,
    ListAccessGrantsLocationsRequestTypeDef,
    ListAccessGrantsLocationsResultTypeDef,
    ListAccessGrantsRequestTypeDef,
    ListAccessGrantsResultTypeDef,
    ListAccessPointsForDirectoryBucketsRequestTypeDef,
    ListAccessPointsForDirectoryBucketsResultTypeDef,
    ListAccessPointsForObjectLambdaRequestTypeDef,
    ListAccessPointsForObjectLambdaResultTypeDef,
    ListAccessPointsRequestTypeDef,
    ListAccessPointsResultTypeDef,
    ListCallerAccessGrantsRequestTypeDef,
    ListCallerAccessGrantsResultTypeDef,
    ListJobsRequestTypeDef,
    ListJobsResultTypeDef,
    ListMultiRegionAccessPointsRequestTypeDef,
    ListMultiRegionAccessPointsResultTypeDef,
    ListRegionalBucketsRequestTypeDef,
    ListRegionalBucketsResultTypeDef,
    ListStorageLensConfigurationsRequestTypeDef,
    ListStorageLensConfigurationsResultTypeDef,
    ListStorageLensGroupsRequestTypeDef,
    ListStorageLensGroupsResultTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResultTypeDef,
    PutAccessGrantsInstanceResourcePolicyRequestTypeDef,
    PutAccessGrantsInstanceResourcePolicyResultTypeDef,
    PutAccessPointConfigurationForObjectLambdaRequestTypeDef,
    PutAccessPointPolicyForObjectLambdaRequestTypeDef,
    PutAccessPointPolicyRequestTypeDef,
    PutAccessPointScopeRequestTypeDef,
    PutBucketLifecycleConfigurationRequestTypeDef,
    PutBucketPolicyRequestTypeDef,
    PutBucketReplicationRequestTypeDef,
    PutBucketTaggingRequestTypeDef,
    PutBucketVersioningRequestTypeDef,
    PutJobTaggingRequestTypeDef,
    PutMultiRegionAccessPointPolicyRequestTypeDef,
    PutMultiRegionAccessPointPolicyResultTypeDef,
    PutPublicAccessBlockRequestTypeDef,
    PutStorageLensConfigurationRequestTypeDef,
    PutStorageLensConfigurationTaggingRequestTypeDef,
    SubmitMultiRegionAccessPointRoutesRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAccessGrantsLocationRequestTypeDef,
    UpdateAccessGrantsLocationResultTypeDef,
    UpdateJobPriorityRequestTypeDef,
    UpdateJobPriorityResultTypeDef,
    UpdateJobStatusRequestTypeDef,
    UpdateJobStatusResultTypeDef,
    UpdateStorageLensGroupRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("S3ControlClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        S3ControlClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#generate_presigned_url)
        """

    def associate_access_grants_identity_center(
        self, **kwargs: Unpack[AssociateAccessGrantsIdentityCenterRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associate your S3 Access Grants instance with an Amazon Web Services IAM
        Identity Center instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/associate_access_grants_identity_center.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#associate_access_grants_identity_center)
        """

    def create_access_grant(
        self, **kwargs: Unpack[CreateAccessGrantRequestTypeDef]
    ) -> CreateAccessGrantResultTypeDef:
        """
        Creates an access grant that gives a grantee access to your S3 data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/create_access_grant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#create_access_grant)
        """

    def create_access_grants_instance(
        self, **kwargs: Unpack[CreateAccessGrantsInstanceRequestTypeDef]
    ) -> CreateAccessGrantsInstanceResultTypeDef:
        """
        Creates an S3 Access Grants instance, which serves as a logical grouping for
        access grants.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/create_access_grants_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#create_access_grants_instance)
        """

    def create_access_grants_location(
        self, **kwargs: Unpack[CreateAccessGrantsLocationRequestTypeDef]
    ) -> CreateAccessGrantsLocationResultTypeDef:
        """
        The S3 data location that you would like to register in your S3 Access Grants
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/create_access_grants_location.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#create_access_grants_location)
        """

    def create_access_point(
        self, **kwargs: Unpack[CreateAccessPointRequestTypeDef]
    ) -> CreateAccessPointResultTypeDef:
        """
        Creates an access point and associates it to a specified bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/create_access_point.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#create_access_point)
        """

    def create_access_point_for_object_lambda(
        self, **kwargs: Unpack[CreateAccessPointForObjectLambdaRequestTypeDef]
    ) -> CreateAccessPointForObjectLambdaResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/create_access_point_for_object_lambda.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#create_access_point_for_object_lambda)
        """

    def create_bucket(
        self, **kwargs: Unpack[CreateBucketRequestTypeDef]
    ) -> CreateBucketResultTypeDef:
        """
        This action creates an Amazon S3 on Outposts bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/create_bucket.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#create_bucket)
        """

    def create_job(self, **kwargs: Unpack[CreateJobRequestTypeDef]) -> CreateJobResultTypeDef:
        """
        This operation creates an S3 Batch Operations job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/create_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#create_job)
        """

    def create_multi_region_access_point(
        self, **kwargs: Unpack[CreateMultiRegionAccessPointRequestTypeDef]
    ) -> CreateMultiRegionAccessPointResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/create_multi_region_access_point.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#create_multi_region_access_point)
        """

    def create_storage_lens_group(
        self, **kwargs: Unpack[CreateStorageLensGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates a new S3 Storage Lens group and associates it with the specified Amazon
        Web Services account ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/create_storage_lens_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#create_storage_lens_group)
        """

    def delete_access_grant(
        self, **kwargs: Unpack[DeleteAccessGrantRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the access grant from the S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_access_grant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#delete_access_grant)
        """

    def delete_access_grants_instance(
        self, **kwargs: Unpack[DeleteAccessGrantsInstanceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes your S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_access_grants_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#delete_access_grants_instance)
        """

    def delete_access_grants_instance_resource_policy(
        self, **kwargs: Unpack[DeleteAccessGrantsInstanceResourcePolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the resource policy of the S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_access_grants_instance_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#delete_access_grants_instance_resource_policy)
        """

    def delete_access_grants_location(
        self, **kwargs: Unpack[DeleteAccessGrantsLocationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deregisters a location from your S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_access_grants_location.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#delete_access_grants_location)
        """

    def delete_access_point(
        self, **kwargs: Unpack[DeleteAccessPointRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified access point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_access_point.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#delete_access_point)
        """

    def delete_access_point_for_object_lambda(
        self, **kwargs: Unpack[DeleteAccessPointForObjectLambdaRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_access_point_for_object_lambda.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#delete_access_point_for_object_lambda)
        """

    def delete_access_point_policy(
        self, **kwargs: Unpack[DeleteAccessPointPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the access point policy for the specified access point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_access_point_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#delete_access_point_policy)
        """

    def delete_access_point_policy_for_object_lambda(
        self, **kwargs: Unpack[DeleteAccessPointPolicyForObjectLambdaRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_access_point_policy_for_object_lambda.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#delete_access_point_policy_for_object_lambda)
        """

    def delete_access_point_scope(
        self, **kwargs: Unpack[DeleteAccessPointScopeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an existing access point scope for a directory bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_access_point_scope.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#delete_access_point_scope)
        """

    def delete_bucket(
        self, **kwargs: Unpack[DeleteBucketRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This action deletes an Amazon S3 on Outposts bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_bucket.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#delete_bucket)
        """

    def delete_bucket_lifecycle_configuration(
        self, **kwargs: Unpack[DeleteBucketLifecycleConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This action deletes an Amazon S3 on Outposts bucket's lifecycle configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_bucket_lifecycle_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#delete_bucket_lifecycle_configuration)
        """

    def delete_bucket_policy(
        self, **kwargs: Unpack[DeleteBucketPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This action deletes an Amazon S3 on Outposts bucket policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_bucket_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#delete_bucket_policy)
        """

    def delete_bucket_replication(
        self, **kwargs: Unpack[DeleteBucketReplicationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation deletes an Amazon S3 on Outposts bucket's replication
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_bucket_replication.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#delete_bucket_replication)
        """

    def delete_bucket_tagging(
        self, **kwargs: Unpack[DeleteBucketTaggingRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This action deletes an Amazon S3 on Outposts bucket's tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_bucket_tagging.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#delete_bucket_tagging)
        """

    def delete_job_tagging(
        self, **kwargs: Unpack[DeleteJobTaggingRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the entire tag set from the specified S3 Batch Operations job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_job_tagging.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#delete_job_tagging)
        """

    def delete_multi_region_access_point(
        self, **kwargs: Unpack[DeleteMultiRegionAccessPointRequestTypeDef]
    ) -> DeleteMultiRegionAccessPointResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_multi_region_access_point.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#delete_multi_region_access_point)
        """

    def delete_public_access_block(
        self, **kwargs: Unpack[DeletePublicAccessBlockRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_public_access_block.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#delete_public_access_block)
        """

    def delete_storage_lens_configuration(
        self, **kwargs: Unpack[DeleteStorageLensConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_storage_lens_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#delete_storage_lens_configuration)
        """

    def delete_storage_lens_configuration_tagging(
        self, **kwargs: Unpack[DeleteStorageLensConfigurationTaggingRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_storage_lens_configuration_tagging.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#delete_storage_lens_configuration_tagging)
        """

    def delete_storage_lens_group(
        self, **kwargs: Unpack[DeleteStorageLensGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an existing S3 Storage Lens group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/delete_storage_lens_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#delete_storage_lens_group)
        """

    def describe_job(self, **kwargs: Unpack[DescribeJobRequestTypeDef]) -> DescribeJobResultTypeDef:
        """
        Retrieves the configuration parameters and status for a Batch Operations job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/describe_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#describe_job)
        """

    def describe_multi_region_access_point_operation(
        self, **kwargs: Unpack[DescribeMultiRegionAccessPointOperationRequestTypeDef]
    ) -> DescribeMultiRegionAccessPointOperationResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/describe_multi_region_access_point_operation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#describe_multi_region_access_point_operation)
        """

    def dissociate_access_grants_identity_center(
        self, **kwargs: Unpack[DissociateAccessGrantsIdentityCenterRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Dissociates the Amazon Web Services IAM Identity Center instance from the S3
        Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/dissociate_access_grants_identity_center.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#dissociate_access_grants_identity_center)
        """

    def get_access_grant(
        self, **kwargs: Unpack[GetAccessGrantRequestTypeDef]
    ) -> GetAccessGrantResultTypeDef:
        """
        Get the details of an access grant from your S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_grant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_access_grant)
        """

    def get_access_grants_instance(
        self, **kwargs: Unpack[GetAccessGrantsInstanceRequestTypeDef]
    ) -> GetAccessGrantsInstanceResultTypeDef:
        """
        Retrieves the S3 Access Grants instance for a Region in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_grants_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_access_grants_instance)
        """

    def get_access_grants_instance_for_prefix(
        self, **kwargs: Unpack[GetAccessGrantsInstanceForPrefixRequestTypeDef]
    ) -> GetAccessGrantsInstanceForPrefixResultTypeDef:
        """
        Retrieve the S3 Access Grants instance that contains a particular prefix.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_grants_instance_for_prefix.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_access_grants_instance_for_prefix)
        """

    def get_access_grants_instance_resource_policy(
        self, **kwargs: Unpack[GetAccessGrantsInstanceResourcePolicyRequestTypeDef]
    ) -> GetAccessGrantsInstanceResourcePolicyResultTypeDef:
        """
        Returns the resource policy of the S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_grants_instance_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_access_grants_instance_resource_policy)
        """

    def get_access_grants_location(
        self, **kwargs: Unpack[GetAccessGrantsLocationRequestTypeDef]
    ) -> GetAccessGrantsLocationResultTypeDef:
        """
        Retrieves the details of a particular location registered in your S3 Access
        Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_grants_location.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_access_grants_location)
        """

    def get_access_point(
        self, **kwargs: Unpack[GetAccessPointRequestTypeDef]
    ) -> GetAccessPointResultTypeDef:
        """
        Returns configuration information about the specified access point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_point.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_access_point)
        """

    def get_access_point_configuration_for_object_lambda(
        self, **kwargs: Unpack[GetAccessPointConfigurationForObjectLambdaRequestTypeDef]
    ) -> GetAccessPointConfigurationForObjectLambdaResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_point_configuration_for_object_lambda.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_access_point_configuration_for_object_lambda)
        """

    def get_access_point_for_object_lambda(
        self, **kwargs: Unpack[GetAccessPointForObjectLambdaRequestTypeDef]
    ) -> GetAccessPointForObjectLambdaResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_point_for_object_lambda.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_access_point_for_object_lambda)
        """

    def get_access_point_policy(
        self, **kwargs: Unpack[GetAccessPointPolicyRequestTypeDef]
    ) -> GetAccessPointPolicyResultTypeDef:
        """
        Returns the access point policy associated with the specified access point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_point_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_access_point_policy)
        """

    def get_access_point_policy_for_object_lambda(
        self, **kwargs: Unpack[GetAccessPointPolicyForObjectLambdaRequestTypeDef]
    ) -> GetAccessPointPolicyForObjectLambdaResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_point_policy_for_object_lambda.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_access_point_policy_for_object_lambda)
        """

    def get_access_point_policy_status(
        self, **kwargs: Unpack[GetAccessPointPolicyStatusRequestTypeDef]
    ) -> GetAccessPointPolicyStatusResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_point_policy_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_access_point_policy_status)
        """

    def get_access_point_policy_status_for_object_lambda(
        self, **kwargs: Unpack[GetAccessPointPolicyStatusForObjectLambdaRequestTypeDef]
    ) -> GetAccessPointPolicyStatusForObjectLambdaResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_point_policy_status_for_object_lambda.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_access_point_policy_status_for_object_lambda)
        """

    def get_access_point_scope(
        self, **kwargs: Unpack[GetAccessPointScopeRequestTypeDef]
    ) -> GetAccessPointScopeResultTypeDef:
        """
        Returns the access point scope for a directory bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_access_point_scope.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_access_point_scope)
        """

    def get_bucket(self, **kwargs: Unpack[GetBucketRequestTypeDef]) -> GetBucketResultTypeDef:
        """
        Gets an Amazon S3 on Outposts bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_bucket.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_bucket)
        """

    def get_bucket_lifecycle_configuration(
        self, **kwargs: Unpack[GetBucketLifecycleConfigurationRequestTypeDef]
    ) -> GetBucketLifecycleConfigurationResultTypeDef:
        """
        This action gets an Amazon S3 on Outposts bucket's lifecycle configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_bucket_lifecycle_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_bucket_lifecycle_configuration)
        """

    def get_bucket_policy(
        self, **kwargs: Unpack[GetBucketPolicyRequestTypeDef]
    ) -> GetBucketPolicyResultTypeDef:
        """
        This action gets a bucket policy for an Amazon S3 on Outposts bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_bucket_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_bucket_policy)
        """

    def get_bucket_replication(
        self, **kwargs: Unpack[GetBucketReplicationRequestTypeDef]
    ) -> GetBucketReplicationResultTypeDef:
        """
        This operation gets an Amazon S3 on Outposts bucket's replication configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_bucket_replication.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_bucket_replication)
        """

    def get_bucket_tagging(
        self, **kwargs: Unpack[GetBucketTaggingRequestTypeDef]
    ) -> GetBucketTaggingResultTypeDef:
        """
        This action gets an Amazon S3 on Outposts bucket's tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_bucket_tagging.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_bucket_tagging)
        """

    def get_bucket_versioning(
        self, **kwargs: Unpack[GetBucketVersioningRequestTypeDef]
    ) -> GetBucketVersioningResultTypeDef:
        """
        This operation returns the versioning state for S3 on Outposts buckets only.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_bucket_versioning.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_bucket_versioning)
        """

    def get_data_access(
        self, **kwargs: Unpack[GetDataAccessRequestTypeDef]
    ) -> GetDataAccessResultTypeDef:
        """
        Returns a temporary access credential from S3 Access Grants to the grantee or
        client application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_data_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_data_access)
        """

    def get_job_tagging(
        self, **kwargs: Unpack[GetJobTaggingRequestTypeDef]
    ) -> GetJobTaggingResultTypeDef:
        """
        Returns the tags on an S3 Batch Operations job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_job_tagging.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_job_tagging)
        """

    def get_multi_region_access_point(
        self, **kwargs: Unpack[GetMultiRegionAccessPointRequestTypeDef]
    ) -> GetMultiRegionAccessPointResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_multi_region_access_point.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_multi_region_access_point)
        """

    def get_multi_region_access_point_policy(
        self, **kwargs: Unpack[GetMultiRegionAccessPointPolicyRequestTypeDef]
    ) -> GetMultiRegionAccessPointPolicyResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_multi_region_access_point_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_multi_region_access_point_policy)
        """

    def get_multi_region_access_point_policy_status(
        self, **kwargs: Unpack[GetMultiRegionAccessPointPolicyStatusRequestTypeDef]
    ) -> GetMultiRegionAccessPointPolicyStatusResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_multi_region_access_point_policy_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_multi_region_access_point_policy_status)
        """

    def get_multi_region_access_point_routes(
        self, **kwargs: Unpack[GetMultiRegionAccessPointRoutesRequestTypeDef]
    ) -> GetMultiRegionAccessPointRoutesResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_multi_region_access_point_routes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_multi_region_access_point_routes)
        """

    def get_public_access_block(
        self, **kwargs: Unpack[GetPublicAccessBlockRequestTypeDef]
    ) -> GetPublicAccessBlockOutputTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_public_access_block.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_public_access_block)
        """

    def get_storage_lens_configuration(
        self, **kwargs: Unpack[GetStorageLensConfigurationRequestTypeDef]
    ) -> GetStorageLensConfigurationResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_storage_lens_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_storage_lens_configuration)
        """

    def get_storage_lens_configuration_tagging(
        self, **kwargs: Unpack[GetStorageLensConfigurationTaggingRequestTypeDef]
    ) -> GetStorageLensConfigurationTaggingResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_storage_lens_configuration_tagging.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_storage_lens_configuration_tagging)
        """

    def get_storage_lens_group(
        self, **kwargs: Unpack[GetStorageLensGroupRequestTypeDef]
    ) -> GetStorageLensGroupResultTypeDef:
        """
        Retrieves the Storage Lens group configuration details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_storage_lens_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_storage_lens_group)
        """

    def list_access_grants(
        self, **kwargs: Unpack[ListAccessGrantsRequestTypeDef]
    ) -> ListAccessGrantsResultTypeDef:
        """
        Returns the list of access grants in your S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_access_grants.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#list_access_grants)
        """

    def list_access_grants_instances(
        self, **kwargs: Unpack[ListAccessGrantsInstancesRequestTypeDef]
    ) -> ListAccessGrantsInstancesResultTypeDef:
        """
        Returns a list of S3 Access Grants instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_access_grants_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#list_access_grants_instances)
        """

    def list_access_grants_locations(
        self, **kwargs: Unpack[ListAccessGrantsLocationsRequestTypeDef]
    ) -> ListAccessGrantsLocationsResultTypeDef:
        """
        Returns a list of the locations registered in your S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_access_grants_locations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#list_access_grants_locations)
        """

    def list_access_points(
        self, **kwargs: Unpack[ListAccessPointsRequestTypeDef]
    ) -> ListAccessPointsResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_access_points.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#list_access_points)
        """

    def list_access_points_for_directory_buckets(
        self, **kwargs: Unpack[ListAccessPointsForDirectoryBucketsRequestTypeDef]
    ) -> ListAccessPointsForDirectoryBucketsResultTypeDef:
        """
        Returns a list of the access points that are owned by the Amazon Web Services
        account and that are associated with the specified directory bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_access_points_for_directory_buckets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#list_access_points_for_directory_buckets)
        """

    def list_access_points_for_object_lambda(
        self, **kwargs: Unpack[ListAccessPointsForObjectLambdaRequestTypeDef]
    ) -> ListAccessPointsForObjectLambdaResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_access_points_for_object_lambda.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#list_access_points_for_object_lambda)
        """

    def list_caller_access_grants(
        self, **kwargs: Unpack[ListCallerAccessGrantsRequestTypeDef]
    ) -> ListCallerAccessGrantsResultTypeDef:
        """
        Use this API to list the access grants that grant the caller access to Amazon
        S3 data through S3 Access Grants.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_caller_access_grants.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#list_caller_access_grants)
        """

    def list_jobs(self, **kwargs: Unpack[ListJobsRequestTypeDef]) -> ListJobsResultTypeDef:
        """
        Lists current S3 Batch Operations jobs as well as the jobs that have ended
        within the last 90 days for the Amazon Web Services account making the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#list_jobs)
        """

    def list_multi_region_access_points(
        self, **kwargs: Unpack[ListMultiRegionAccessPointsRequestTypeDef]
    ) -> ListMultiRegionAccessPointsResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_multi_region_access_points.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#list_multi_region_access_points)
        """

    def list_regional_buckets(
        self, **kwargs: Unpack[ListRegionalBucketsRequestTypeDef]
    ) -> ListRegionalBucketsResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_regional_buckets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#list_regional_buckets)
        """

    def list_storage_lens_configurations(
        self, **kwargs: Unpack[ListStorageLensConfigurationsRequestTypeDef]
    ) -> ListStorageLensConfigurationsResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_storage_lens_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#list_storage_lens_configurations)
        """

    def list_storage_lens_groups(
        self, **kwargs: Unpack[ListStorageLensGroupsRequestTypeDef]
    ) -> ListStorageLensGroupsResultTypeDef:
        """
        Lists all the Storage Lens groups in the specified home Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_storage_lens_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#list_storage_lens_groups)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResultTypeDef:
        """
        This operation allows you to list all the Amazon Web Services resource tags for
        a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#list_tags_for_resource)
        """

    def put_access_grants_instance_resource_policy(
        self, **kwargs: Unpack[PutAccessGrantsInstanceResourcePolicyRequestTypeDef]
    ) -> PutAccessGrantsInstanceResourcePolicyResultTypeDef:
        """
        Updates the resource policy of the S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_access_grants_instance_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#put_access_grants_instance_resource_policy)
        """

    def put_access_point_configuration_for_object_lambda(
        self, **kwargs: Unpack[PutAccessPointConfigurationForObjectLambdaRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_access_point_configuration_for_object_lambda.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#put_access_point_configuration_for_object_lambda)
        """

    def put_access_point_policy(
        self, **kwargs: Unpack[PutAccessPointPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates an access policy with the specified access point.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_access_point_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#put_access_point_policy)
        """

    def put_access_point_policy_for_object_lambda(
        self, **kwargs: Unpack[PutAccessPointPolicyForObjectLambdaRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_access_point_policy_for_object_lambda.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#put_access_point_policy_for_object_lambda)
        """

    def put_access_point_scope(
        self, **kwargs: Unpack[PutAccessPointScopeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates or replaces the access point scope for a directory bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_access_point_scope.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#put_access_point_scope)
        """

    def put_bucket_lifecycle_configuration(
        self, **kwargs: Unpack[PutBucketLifecycleConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This action puts a lifecycle configuration to an Amazon S3 on Outposts bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_bucket_lifecycle_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#put_bucket_lifecycle_configuration)
        """

    def put_bucket_policy(
        self, **kwargs: Unpack[PutBucketPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This action puts a bucket policy to an Amazon S3 on Outposts bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_bucket_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#put_bucket_policy)
        """

    def put_bucket_replication(
        self, **kwargs: Unpack[PutBucketReplicationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This action creates an Amazon S3 on Outposts bucket's replication configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_bucket_replication.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#put_bucket_replication)
        """

    def put_bucket_tagging(
        self, **kwargs: Unpack[PutBucketTaggingRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This action puts tags on an Amazon S3 on Outposts bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_bucket_tagging.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#put_bucket_tagging)
        """

    def put_bucket_versioning(
        self, **kwargs: Unpack[PutBucketVersioningRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation sets the versioning state for S3 on Outposts buckets only.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_bucket_versioning.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#put_bucket_versioning)
        """

    def put_job_tagging(self, **kwargs: Unpack[PutJobTaggingRequestTypeDef]) -> Dict[str, Any]:
        """
        Sets the supplied tag-set on an S3 Batch Operations job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_job_tagging.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#put_job_tagging)
        """

    def put_multi_region_access_point_policy(
        self, **kwargs: Unpack[PutMultiRegionAccessPointPolicyRequestTypeDef]
    ) -> PutMultiRegionAccessPointPolicyResultTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_multi_region_access_point_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#put_multi_region_access_point_policy)
        """

    def put_public_access_block(
        self, **kwargs: Unpack[PutPublicAccessBlockRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_public_access_block.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#put_public_access_block)
        """

    def put_storage_lens_configuration(
        self, **kwargs: Unpack[PutStorageLensConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_storage_lens_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#put_storage_lens_configuration)
        """

    def put_storage_lens_configuration_tagging(
        self, **kwargs: Unpack[PutStorageLensConfigurationTaggingRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/put_storage_lens_configuration_tagging.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#put_storage_lens_configuration_tagging)
        """

    def submit_multi_region_access_point_routes(
        self, **kwargs: Unpack[SubmitMultiRegionAccessPointRoutesRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This operation is not supported by directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/submit_multi_region_access_point_routes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#submit_multi_region_access_point_routes)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates a new Amazon Web Services resource tag or updates an existing resource
        tag.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        This operation removes the specified Amazon Web Services resource tags from an
        S3 resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#untag_resource)
        """

    def update_access_grants_location(
        self, **kwargs: Unpack[UpdateAccessGrantsLocationRequestTypeDef]
    ) -> UpdateAccessGrantsLocationResultTypeDef:
        """
        Updates the IAM role of a registered location in your S3 Access Grants instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/update_access_grants_location.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#update_access_grants_location)
        """

    def update_job_priority(
        self, **kwargs: Unpack[UpdateJobPriorityRequestTypeDef]
    ) -> UpdateJobPriorityResultTypeDef:
        """
        Updates an existing S3 Batch Operations job's priority.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/update_job_priority.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#update_job_priority)
        """

    def update_job_status(
        self, **kwargs: Unpack[UpdateJobStatusRequestTypeDef]
    ) -> UpdateJobStatusResultTypeDef:
        """
        Updates the status for the specified job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/update_job_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#update_job_status)
        """

    def update_storage_lens_group(
        self, **kwargs: Unpack[UpdateStorageLensGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the existing Storage Lens group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/update_storage_lens_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#update_storage_lens_group)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_access_points_for_directory_buckets"]
    ) -> ListAccessPointsForDirectoryBucketsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_access_points_for_object_lambda"]
    ) -> ListAccessPointsForObjectLambdaPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_caller_access_grants"]
    ) -> ListCallerAccessGrantsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/client/#get_paginator)
        """
