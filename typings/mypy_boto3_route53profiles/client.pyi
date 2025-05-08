"""
Type annotations for route53profiles service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_route53profiles.client import Route53ProfilesClient

    session = Session()
    client: Route53ProfilesClient = session.client("route53profiles")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListProfileAssociationsPaginator,
    ListProfileResourceAssociationsPaginator,
    ListProfilesPaginator,
)
from .type_defs import (
    AssociateProfileRequestTypeDef,
    AssociateProfileResponseTypeDef,
    AssociateResourceToProfileRequestTypeDef,
    AssociateResourceToProfileResponseTypeDef,
    CreateProfileRequestTypeDef,
    CreateProfileResponseTypeDef,
    DeleteProfileRequestTypeDef,
    DeleteProfileResponseTypeDef,
    DisassociateProfileRequestTypeDef,
    DisassociateProfileResponseTypeDef,
    DisassociateResourceFromProfileRequestTypeDef,
    DisassociateResourceFromProfileResponseTypeDef,
    GetProfileAssociationRequestTypeDef,
    GetProfileAssociationResponseTypeDef,
    GetProfileRequestTypeDef,
    GetProfileResourceAssociationRequestTypeDef,
    GetProfileResourceAssociationResponseTypeDef,
    GetProfileResponseTypeDef,
    ListProfileAssociationsRequestTypeDef,
    ListProfileAssociationsResponseTypeDef,
    ListProfileResourceAssociationsRequestTypeDef,
    ListProfileResourceAssociationsResponseTypeDef,
    ListProfilesRequestTypeDef,
    ListProfilesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateProfileResourceAssociationRequestTypeDef,
    UpdateProfileResourceAssociationResponseTypeDef,
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

__all__ = ("Route53ProfilesClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServiceErrorException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class Route53ProfilesClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles.html#Route53Profiles.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        Route53ProfilesClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles.html#Route53Profiles.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/#generate_presigned_url)
        """

    def associate_profile(
        self, **kwargs: Unpack[AssociateProfileRequestTypeDef]
    ) -> AssociateProfileResponseTypeDef:
        """
        Associates a Route 53 Profiles profile with a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/client/associate_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/#associate_profile)
        """

    def associate_resource_to_profile(
        self, **kwargs: Unpack[AssociateResourceToProfileRequestTypeDef]
    ) -> AssociateResourceToProfileResponseTypeDef:
        """
        Associates a DNS reource configuration to a Route 53 Profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/client/associate_resource_to_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/#associate_resource_to_profile)
        """

    def create_profile(
        self, **kwargs: Unpack[CreateProfileRequestTypeDef]
    ) -> CreateProfileResponseTypeDef:
        """
        Creates an empty Route 53 Profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/client/create_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/#create_profile)
        """

    def delete_profile(
        self, **kwargs: Unpack[DeleteProfileRequestTypeDef]
    ) -> DeleteProfileResponseTypeDef:
        """
        Deletes the specified Route 53 Profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/client/delete_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/#delete_profile)
        """

    def disassociate_profile(
        self, **kwargs: Unpack[DisassociateProfileRequestTypeDef]
    ) -> DisassociateProfileResponseTypeDef:
        """
        Dissociates a specified Route 53 Profile from the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/client/disassociate_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/#disassociate_profile)
        """

    def disassociate_resource_from_profile(
        self, **kwargs: Unpack[DisassociateResourceFromProfileRequestTypeDef]
    ) -> DisassociateResourceFromProfileResponseTypeDef:
        """
        Dissoaciated a specified resource, from the Route 53 Profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/client/disassociate_resource_from_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/#disassociate_resource_from_profile)
        """

    def get_profile(self, **kwargs: Unpack[GetProfileRequestTypeDef]) -> GetProfileResponseTypeDef:
        """
        Returns information about a specified Route 53 Profile, such as whether whether
        the Profile is shared, and the current status of the Profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/client/get_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/#get_profile)
        """

    def get_profile_association(
        self, **kwargs: Unpack[GetProfileAssociationRequestTypeDef]
    ) -> GetProfileAssociationResponseTypeDef:
        """
        Retrieves a Route 53 Profile association for a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/client/get_profile_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/#get_profile_association)
        """

    def get_profile_resource_association(
        self, **kwargs: Unpack[GetProfileResourceAssociationRequestTypeDef]
    ) -> GetProfileResourceAssociationResponseTypeDef:
        """
        Returns information about a specified Route 53 Profile resource association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/client/get_profile_resource_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/#get_profile_resource_association)
        """

    def list_profile_associations(
        self, **kwargs: Unpack[ListProfileAssociationsRequestTypeDef]
    ) -> ListProfileAssociationsResponseTypeDef:
        """
        Lists all the VPCs that the specified Route 53 Profile is associated with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/client/list_profile_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/#list_profile_associations)
        """

    def list_profile_resource_associations(
        self, **kwargs: Unpack[ListProfileResourceAssociationsRequestTypeDef]
    ) -> ListProfileResourceAssociationsResponseTypeDef:
        """
        Lists all the resource associations for the specified Route 53 Profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/client/list_profile_resource_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/#list_profile_resource_associations)
        """

    def list_profiles(
        self, **kwargs: Unpack[ListProfilesRequestTypeDef]
    ) -> ListProfilesResponseTypeDef:
        """
        Lists all the Route 53 Profiles associated with your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/client/list_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/#list_profiles)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags that you associated with the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/#list_tags_for_resource)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds one or more tags to a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/#untag_resource)
        """

    def update_profile_resource_association(
        self, **kwargs: Unpack[UpdateProfileResourceAssociationRequestTypeDef]
    ) -> UpdateProfileResourceAssociationResponseTypeDef:
        """
        Updates the specified Route 53 Profile resourse association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/client/update_profile_resource_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/#update_profile_resource_association)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_profile_associations"]
    ) -> ListProfileAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_profile_resource_associations"]
    ) -> ListProfileResourceAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_profiles"]
    ) -> ListProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client/#get_paginator)
        """
