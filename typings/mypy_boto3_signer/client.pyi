# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for signer service client

Usage::

    ```python
    import boto3
    from mypy_boto3_signer import SignerClient

    client: SignerClient = boto3.client("signer")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_signer.paginator import (
    ListSigningJobsPaginator,
    ListSigningPlatformsPaginator,
    ListSigningProfilesPaginator,
)
from mypy_boto3_signer.type_defs import (
    DescribeSigningJobResponseTypeDef,
    DestinationTypeDef,
    GetSigningPlatformResponseTypeDef,
    GetSigningProfileResponseTypeDef,
    ListSigningJobsResponseTypeDef,
    ListSigningPlatformsResponseTypeDef,
    ListSigningProfilesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutSigningProfileResponseTypeDef,
    SigningMaterialTypeDef,
    SigningPlatformOverridesTypeDef,
    SourceTypeDef,
    StartSigningJobResponseTypeDef,
)
from mypy_boto3_signer.waiter import SuccessfulSigningJobWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SignerClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServiceErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class SignerClient:
    """
    [Signer.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Client.can_paginate)
        """

    def cancel_signing_profile(self, profileName: str) -> None:
        """
        [Client.cancel_signing_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Client.cancel_signing_profile)
        """

    def describe_signing_job(self, jobId: str) -> DescribeSigningJobResponseTypeDef:
        """
        [Client.describe_signing_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Client.describe_signing_job)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Client.generate_presigned_url)
        """

    def get_signing_platform(self, platformId: str) -> GetSigningPlatformResponseTypeDef:
        """
        [Client.get_signing_platform documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Client.get_signing_platform)
        """

    def get_signing_profile(self, profileName: str) -> GetSigningProfileResponseTypeDef:
        """
        [Client.get_signing_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Client.get_signing_profile)
        """

    def list_signing_jobs(
        self,
        status: Literal["InProgress", "Failed", "Succeeded"] = None,
        platformId: str = None,
        requestedBy: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListSigningJobsResponseTypeDef:
        """
        [Client.list_signing_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Client.list_signing_jobs)
        """

    def list_signing_platforms(
        self,
        category: str = None,
        partner: str = None,
        target: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListSigningPlatformsResponseTypeDef:
        """
        [Client.list_signing_platforms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Client.list_signing_platforms)
        """

    def list_signing_profiles(
        self, includeCanceled: bool = None, maxResults: int = None, nextToken: str = None
    ) -> ListSigningProfilesResponseTypeDef:
        """
        [Client.list_signing_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Client.list_signing_profiles)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Client.list_tags_for_resource)
        """

    def put_signing_profile(
        self,
        profileName: str,
        signingMaterial: "SigningMaterialTypeDef",
        platformId: str,
        overrides: "SigningPlatformOverridesTypeDef" = None,
        signingParameters: Dict[str, str] = None,
        tags: Dict[str, str] = None,
    ) -> PutSigningProfileResponseTypeDef:
        """
        [Client.put_signing_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Client.put_signing_profile)
        """

    def start_signing_job(
        self,
        source: "SourceTypeDef",
        destination: DestinationTypeDef,
        clientRequestToken: str,
        profileName: str = None,
    ) -> StartSigningJobResponseTypeDef:
        """
        [Client.start_signing_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Client.start_signing_job)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Client.untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_signing_jobs"]
    ) -> ListSigningJobsPaginator:
        """
        [Paginator.ListSigningJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Paginator.ListSigningJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_signing_platforms"]
    ) -> ListSigningPlatformsPaginator:
        """
        [Paginator.ListSigningPlatforms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Paginator.ListSigningPlatforms)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_signing_profiles"]
    ) -> ListSigningProfilesPaginator:
        """
        [Paginator.ListSigningProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Paginator.ListSigningProfiles)
        """

    def get_waiter(
        self, waiter_name: Literal["successful_signing_job"]
    ) -> SuccessfulSigningJobWaiter:
        """
        [Waiter.SuccessfulSigningJob documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/signer.html#Signer.Waiter.SuccessfulSigningJob)
        """
