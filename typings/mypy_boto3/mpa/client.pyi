"""
Type annotations for mpa service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mpa.client import MultipartyApprovalClient

    session = Session()
    client: MultipartyApprovalClient = session.client("mpa")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListApprovalTeamsPaginator,
    ListIdentitySourcesPaginator,
    ListPoliciesPaginator,
    ListPolicyVersionsPaginator,
    ListResourcePoliciesPaginator,
    ListSessionsPaginator,
)
from .type_defs import (
    CancelSessionRequestTypeDef,
    CreateApprovalTeamRequestTypeDef,
    CreateApprovalTeamResponseTypeDef,
    CreateIdentitySourceRequestTypeDef,
    CreateIdentitySourceResponseTypeDef,
    DeleteIdentitySourceRequestTypeDef,
    DeleteInactiveApprovalTeamVersionRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetApprovalTeamRequestTypeDef,
    GetApprovalTeamResponseTypeDef,
    GetIdentitySourceRequestTypeDef,
    GetIdentitySourceResponseTypeDef,
    GetPolicyVersionRequestTypeDef,
    GetPolicyVersionResponseTypeDef,
    GetResourcePolicyRequestTypeDef,
    GetResourcePolicyResponseTypeDef,
    GetSessionRequestTypeDef,
    GetSessionResponseTypeDef,
    ListApprovalTeamsRequestTypeDef,
    ListApprovalTeamsResponseTypeDef,
    ListIdentitySourcesRequestTypeDef,
    ListIdentitySourcesResponseTypeDef,
    ListPoliciesRequestTypeDef,
    ListPoliciesResponseTypeDef,
    ListPolicyVersionsRequestTypeDef,
    ListPolicyVersionsResponseTypeDef,
    ListResourcePoliciesRequestTypeDef,
    ListResourcePoliciesResponseTypeDef,
    ListSessionsRequestTypeDef,
    ListSessionsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    StartActiveApprovalTeamDeletionRequestTypeDef,
    StartActiveApprovalTeamDeletionResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateApprovalTeamRequestTypeDef,
    UpdateApprovalTeamResponseTypeDef,
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

__all__ = ("MultipartyApprovalClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class MultipartyApprovalClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa.html#MultipartyApproval.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MultipartyApprovalClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa.html#MultipartyApproval.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#generate_presigned_url)
        """

    def cancel_session(self, **kwargs: Unpack[CancelSessionRequestTypeDef]) -> Dict[str, Any]:
        """
        Cancels an approval session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/cancel_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#cancel_session)
        """

    def create_approval_team(
        self, **kwargs: Unpack[CreateApprovalTeamRequestTypeDef]
    ) -> CreateApprovalTeamResponseTypeDef:
        """
        Creates a new approval team.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/create_approval_team.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#create_approval_team)
        """

    def create_identity_source(
        self, **kwargs: Unpack[CreateIdentitySourceRequestTypeDef]
    ) -> CreateIdentitySourceResponseTypeDef:
        """
        Creates a new identity source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/create_identity_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#create_identity_source)
        """

    def delete_identity_source(
        self, **kwargs: Unpack[DeleteIdentitySourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an identity source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/delete_identity_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#delete_identity_source)
        """

    def delete_inactive_approval_team_version(
        self, **kwargs: Unpack[DeleteInactiveApprovalTeamVersionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an inactive approval team.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/delete_inactive_approval_team_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#delete_inactive_approval_team_version)
        """

    def get_approval_team(
        self, **kwargs: Unpack[GetApprovalTeamRequestTypeDef]
    ) -> GetApprovalTeamResponseTypeDef:
        """
        Returns details for an approval team.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/get_approval_team.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#get_approval_team)
        """

    def get_identity_source(
        self, **kwargs: Unpack[GetIdentitySourceRequestTypeDef]
    ) -> GetIdentitySourceResponseTypeDef:
        """
        Returns details for an identity source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/get_identity_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#get_identity_source)
        """

    def get_policy_version(
        self, **kwargs: Unpack[GetPolicyVersionRequestTypeDef]
    ) -> GetPolicyVersionResponseTypeDef:
        """
        Returns details for the version of a policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/get_policy_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#get_policy_version)
        """

    def get_resource_policy(
        self, **kwargs: Unpack[GetResourcePolicyRequestTypeDef]
    ) -> GetResourcePolicyResponseTypeDef:
        """
        Returns details about a policy for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/get_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#get_resource_policy)
        """

    def get_session(self, **kwargs: Unpack[GetSessionRequestTypeDef]) -> GetSessionResponseTypeDef:
        """
        Returns details for an approval session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/get_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#get_session)
        """

    def list_approval_teams(
        self, **kwargs: Unpack[ListApprovalTeamsRequestTypeDef]
    ) -> ListApprovalTeamsResponseTypeDef:
        """
        Returns a list of approval teams.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/list_approval_teams.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#list_approval_teams)
        """

    def list_identity_sources(
        self, **kwargs: Unpack[ListIdentitySourcesRequestTypeDef]
    ) -> ListIdentitySourcesResponseTypeDef:
        """
        Returns a list of identity sources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/list_identity_sources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#list_identity_sources)
        """

    def list_policies(
        self, **kwargs: Unpack[ListPoliciesRequestTypeDef]
    ) -> ListPoliciesResponseTypeDef:
        """
        Returns a list of policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/list_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#list_policies)
        """

    def list_policy_versions(
        self, **kwargs: Unpack[ListPolicyVersionsRequestTypeDef]
    ) -> ListPolicyVersionsResponseTypeDef:
        """
        Returns a list of the versions for policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/list_policy_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#list_policy_versions)
        """

    def list_resource_policies(
        self, **kwargs: Unpack[ListResourcePoliciesRequestTypeDef]
    ) -> ListResourcePoliciesResponseTypeDef:
        """
        Returns a list of policies for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/list_resource_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#list_resource_policies)
        """

    def list_sessions(
        self, **kwargs: Unpack[ListSessionsRequestTypeDef]
    ) -> ListSessionsResponseTypeDef:
        """
        Returns a list of approval sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/list_sessions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#list_sessions)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#list_tags_for_resource)
        """

    def start_active_approval_team_deletion(
        self, **kwargs: Unpack[StartActiveApprovalTeamDeletionRequestTypeDef]
    ) -> StartActiveApprovalTeamDeletionResponseTypeDef:
        """
        Starts the deletion process for an active approval team.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/start_active_approval_team_deletion.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#start_active_approval_team_deletion)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates or updates a resource tag.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a resource tag.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#untag_resource)
        """

    def update_approval_team(
        self, **kwargs: Unpack[UpdateApprovalTeamRequestTypeDef]
    ) -> UpdateApprovalTeamResponseTypeDef:
        """
        Updates an approval team.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/update_approval_team.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#update_approval_team)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_approval_teams"]
    ) -> ListApprovalTeamsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_identity_sources"]
    ) -> ListIdentitySourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_policies"]
    ) -> ListPoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_policy_versions"]
    ) -> ListPolicyVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resource_policies"]
    ) -> ListResourcePoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_sessions"]
    ) -> ListSessionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mpa/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mpa/client/#get_paginator)
        """
