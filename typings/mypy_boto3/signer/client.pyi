"""
Type annotations for signer service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_signer.client import SignerClient

    session = Session()
    client: SignerClient = session.client("signer")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListSigningJobsPaginator,
    ListSigningPlatformsPaginator,
    ListSigningProfilesPaginator,
)
from .type_defs import (
    AddProfilePermissionRequestTypeDef,
    AddProfilePermissionResponseTypeDef,
    CancelSigningProfileRequestTypeDef,
    DescribeSigningJobRequestTypeDef,
    DescribeSigningJobResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetRevocationStatusRequestTypeDef,
    GetRevocationStatusResponseTypeDef,
    GetSigningPlatformRequestTypeDef,
    GetSigningPlatformResponseTypeDef,
    GetSigningProfileRequestTypeDef,
    GetSigningProfileResponseTypeDef,
    ListProfilePermissionsRequestTypeDef,
    ListProfilePermissionsResponseTypeDef,
    ListSigningJobsRequestTypeDef,
    ListSigningJobsResponseTypeDef,
    ListSigningPlatformsRequestTypeDef,
    ListSigningPlatformsResponseTypeDef,
    ListSigningProfilesRequestTypeDef,
    ListSigningProfilesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutSigningProfileRequestTypeDef,
    PutSigningProfileResponseTypeDef,
    RemoveProfilePermissionRequestTypeDef,
    RemoveProfilePermissionResponseTypeDef,
    RevokeSignatureRequestTypeDef,
    RevokeSigningProfileRequestTypeDef,
    SignPayloadRequestTypeDef,
    SignPayloadResponseTypeDef,
    StartSigningJobRequestTypeDef,
    StartSigningJobResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
)
from .waiter import SuccessfulSigningJobWaiter

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

__all__ = ("SignerClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServiceErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceLimitExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class SignerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SignerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#generate_presigned_url)
        """

    def add_profile_permission(
        self, **kwargs: Unpack[AddProfilePermissionRequestTypeDef]
    ) -> AddProfilePermissionResponseTypeDef:
        """
        Adds cross-account permissions to a signing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/add_profile_permission.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#add_profile_permission)
        """

    def cancel_signing_profile(
        self, **kwargs: Unpack[CancelSigningProfileRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Changes the state of an <code>ACTIVE</code> signing profile to
        <code>CANCELED</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/cancel_signing_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#cancel_signing_profile)
        """

    def describe_signing_job(
        self, **kwargs: Unpack[DescribeSigningJobRequestTypeDef]
    ) -> DescribeSigningJobResponseTypeDef:
        """
        Returns information about a specific code signing job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/describe_signing_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#describe_signing_job)
        """

    def get_revocation_status(
        self, **kwargs: Unpack[GetRevocationStatusRequestTypeDef]
    ) -> GetRevocationStatusResponseTypeDef:
        """
        Retrieves the revocation status of one or more of the signing profile, signing
        job, and signing certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/get_revocation_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#get_revocation_status)
        """

    def get_signing_platform(
        self, **kwargs: Unpack[GetSigningPlatformRequestTypeDef]
    ) -> GetSigningPlatformResponseTypeDef:
        """
        Returns information on a specific signing platform.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/get_signing_platform.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#get_signing_platform)
        """

    def get_signing_profile(
        self, **kwargs: Unpack[GetSigningProfileRequestTypeDef]
    ) -> GetSigningProfileResponseTypeDef:
        """
        Returns information on a specific signing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/get_signing_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#get_signing_profile)
        """

    def list_profile_permissions(
        self, **kwargs: Unpack[ListProfilePermissionsRequestTypeDef]
    ) -> ListProfilePermissionsResponseTypeDef:
        """
        Lists the cross-account permissions associated with a signing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/list_profile_permissions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#list_profile_permissions)
        """

    def list_signing_jobs(
        self, **kwargs: Unpack[ListSigningJobsRequestTypeDef]
    ) -> ListSigningJobsResponseTypeDef:
        """
        Lists all your signing jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/list_signing_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#list_signing_jobs)
        """

    def list_signing_platforms(
        self, **kwargs: Unpack[ListSigningPlatformsRequestTypeDef]
    ) -> ListSigningPlatformsResponseTypeDef:
        """
        Lists all signing platforms available in AWS Signer that match the request
        parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/list_signing_platforms.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#list_signing_platforms)
        """

    def list_signing_profiles(
        self, **kwargs: Unpack[ListSigningProfilesRequestTypeDef]
    ) -> ListSigningProfilesResponseTypeDef:
        """
        Lists all available signing profiles in your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/list_signing_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#list_signing_profiles)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of the tags associated with a signing profile resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#list_tags_for_resource)
        """

    def put_signing_profile(
        self, **kwargs: Unpack[PutSigningProfileRequestTypeDef]
    ) -> PutSigningProfileResponseTypeDef:
        """
        Creates a signing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/put_signing_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#put_signing_profile)
        """

    def remove_profile_permission(
        self, **kwargs: Unpack[RemoveProfilePermissionRequestTypeDef]
    ) -> RemoveProfilePermissionResponseTypeDef:
        """
        Removes cross-account permissions from a signing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/remove_profile_permission.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#remove_profile_permission)
        """

    def revoke_signature(
        self, **kwargs: Unpack[RevokeSignatureRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Changes the state of a signing job to REVOKED.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/revoke_signature.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#revoke_signature)
        """

    def revoke_signing_profile(
        self, **kwargs: Unpack[RevokeSigningProfileRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Changes the state of a signing profile to REVOKED.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/revoke_signing_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#revoke_signing_profile)
        """

    def sign_payload(
        self, **kwargs: Unpack[SignPayloadRequestTypeDef]
    ) -> SignPayloadResponseTypeDef:
        """
        Signs a binary payload and returns a signature envelope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/sign_payload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#sign_payload)
        """

    def start_signing_job(
        self, **kwargs: Unpack[StartSigningJobRequestTypeDef]
    ) -> StartSigningJobResponseTypeDef:
        """
        Initiates a signing job to be performed on the code provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/start_signing_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#start_signing_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds one or more tags to a signing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from a signing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#untag_resource)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_signing_jobs"]
    ) -> ListSigningJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_signing_platforms"]
    ) -> ListSigningPlatformsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_signing_profiles"]
    ) -> ListSigningProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#get_paginator)
        """

    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["successful_signing_job"]
    ) -> SuccessfulSigningJobWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/client/#get_waiter)
        """
