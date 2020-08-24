# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for s3control service client

Usage::

    ```python
    import boto3
    from mypy_boto3_s3control import S3ControlClient

    client: S3ControlClient = boto3.client("s3control")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_s3control.type_defs import (
    CreateJobResultTypeDef,
    DescribeJobResultTypeDef,
    GetAccessPointPolicyResultTypeDef,
    GetAccessPointPolicyStatusResultTypeDef,
    GetAccessPointResultTypeDef,
    GetJobTaggingResultTypeDef,
    GetPublicAccessBlockOutputTypeDef,
    JobManifestTypeDef,
    JobOperationTypeDef,
    JobReportTypeDef,
    ListAccessPointsResultTypeDef,
    ListJobsResultTypeDef,
    PublicAccessBlockConfigurationTypeDef,
    S3TagTypeDef,
    UpdateJobPriorityResultTypeDef,
    UpdateJobStatusResultTypeDef,
    VpcConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("S3ControlClient",)


class Exceptions:
    BadRequestException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    IdempotencyException: Type[Boto3ClientError]
    InternalServiceException: Type[Boto3ClientError]
    InvalidNextTokenException: Type[Boto3ClientError]
    InvalidRequestException: Type[Boto3ClientError]
    JobStatusException: Type[Boto3ClientError]
    NoSuchPublicAccessBlockConfiguration: Type[Boto3ClientError]
    NotFoundException: Type[Boto3ClientError]
    TooManyRequestsException: Type[Boto3ClientError]
    TooManyTagsException: Type[Boto3ClientError]


class S3ControlClient:
    """
    [S3Control.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/s3control.html#S3Control.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/s3control.html#S3Control.Client.can_paginate)
        """

    def create_access_point(
        self,
        AccountId: str,
        Name: str,
        Bucket: str,
        VpcConfiguration: "VpcConfigurationTypeDef" = None,
        PublicAccessBlockConfiguration: "PublicAccessBlockConfigurationTypeDef" = None,
    ) -> None:
        """
        [Client.create_access_point documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/s3control.html#S3Control.Client.create_access_point)
        """

    def create_job(
        self,
        AccountId: str,
        Operation: "JobOperationTypeDef",
        Report: "JobReportTypeDef",
        ClientRequestToken: str,
        Manifest: "JobManifestTypeDef",
        Priority: int,
        RoleArn: str,
        ConfirmationRequired: bool = None,
        Description: str = None,
        Tags: List["S3TagTypeDef"] = None,
    ) -> CreateJobResultTypeDef:
        """
        [Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/s3control.html#S3Control.Client.create_job)
        """

    def delete_access_point(self, AccountId: str, Name: str) -> None:
        """
        [Client.delete_access_point documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/s3control.html#S3Control.Client.delete_access_point)
        """

    def delete_access_point_policy(self, AccountId: str, Name: str) -> None:
        """
        [Client.delete_access_point_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/s3control.html#S3Control.Client.delete_access_point_policy)
        """

    def delete_job_tagging(self, AccountId: str, JobId: str) -> Dict[str, Any]:
        """
        [Client.delete_job_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/s3control.html#S3Control.Client.delete_job_tagging)
        """

    def delete_public_access_block(self, AccountId: str) -> None:
        """
        [Client.delete_public_access_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/s3control.html#S3Control.Client.delete_public_access_block)
        """

    def describe_job(self, AccountId: str, JobId: str) -> DescribeJobResultTypeDef:
        """
        [Client.describe_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/s3control.html#S3Control.Client.describe_job)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/s3control.html#S3Control.Client.generate_presigned_url)
        """

    def get_access_point(self, AccountId: str, Name: str) -> GetAccessPointResultTypeDef:
        """
        [Client.get_access_point documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/s3control.html#S3Control.Client.get_access_point)
        """

    def get_access_point_policy(
        self, AccountId: str, Name: str
    ) -> GetAccessPointPolicyResultTypeDef:
        """
        [Client.get_access_point_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/s3control.html#S3Control.Client.get_access_point_policy)
        """

    def get_access_point_policy_status(
        self, AccountId: str, Name: str
    ) -> GetAccessPointPolicyStatusResultTypeDef:
        """
        [Client.get_access_point_policy_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/s3control.html#S3Control.Client.get_access_point_policy_status)
        """

    def get_job_tagging(self, AccountId: str, JobId: str) -> GetJobTaggingResultTypeDef:
        """
        [Client.get_job_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/s3control.html#S3Control.Client.get_job_tagging)
        """

    def get_public_access_block(self, AccountId: str) -> GetPublicAccessBlockOutputTypeDef:
        """
        [Client.get_public_access_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/s3control.html#S3Control.Client.get_public_access_block)
        """

    def list_access_points(
        self, AccountId: str, Bucket: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListAccessPointsResultTypeDef:
        """
        [Client.list_access_points documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/s3control.html#S3Control.Client.list_access_points)
        """

    def list_jobs(
        self,
        AccountId: str,
        JobStatuses: List[
            Literal[
                "Active",
                "Cancelled",
                "Cancelling",
                "Complete",
                "Completing",
                "Failed",
                "Failing",
                "New",
                "Paused",
                "Pausing",
                "Preparing",
                "Ready",
                "Suspended",
            ]
        ] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListJobsResultTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/s3control.html#S3Control.Client.list_jobs)
        """

    def put_access_point_policy(self, AccountId: str, Name: str, Policy: str) -> None:
        """
        [Client.put_access_point_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/s3control.html#S3Control.Client.put_access_point_policy)
        """

    def put_job_tagging(
        self, AccountId: str, JobId: str, Tags: List["S3TagTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Client.put_job_tagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/s3control.html#S3Control.Client.put_job_tagging)
        """

    def put_public_access_block(
        self,
        PublicAccessBlockConfiguration: "PublicAccessBlockConfigurationTypeDef",
        AccountId: str,
    ) -> None:
        """
        [Client.put_public_access_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/s3control.html#S3Control.Client.put_public_access_block)
        """

    def update_job_priority(
        self, AccountId: str, JobId: str, Priority: int
    ) -> UpdateJobPriorityResultTypeDef:
        """
        [Client.update_job_priority documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/s3control.html#S3Control.Client.update_job_priority)
        """

    def update_job_status(
        self,
        AccountId: str,
        JobId: str,
        RequestedJobStatus: Literal["Cancelled", "Ready"],
        StatusUpdateReason: str = None,
    ) -> UpdateJobStatusResultTypeDef:
        """
        [Client.update_job_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/s3control.html#S3Control.Client.update_job_status)
        """
