"""
Type annotations for rolesanywhere service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_rolesanywhere.client import IAMRolesAnywhereClient

    session = Session()
    client: IAMRolesAnywhereClient = session.client("rolesanywhere")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListCrlsPaginator,
    ListProfilesPaginator,
    ListSubjectsPaginator,
    ListTrustAnchorsPaginator,
)
from .type_defs import (
    CreateProfileRequestTypeDef,
    CreateTrustAnchorRequestTypeDef,
    CrlDetailResponseTypeDef,
    DeleteAttributeMappingRequestTypeDef,
    DeleteAttributeMappingResponseTypeDef,
    ImportCrlRequestTypeDef,
    ListCrlsResponseTypeDef,
    ListProfilesResponseTypeDef,
    ListRequestRequestExtraExtraTypeDef,
    ListRequestRequestExtraTypeDef,
    ListRequestRequestTypeDef,
    ListRequestTypeDef,
    ListSubjectsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTrustAnchorsResponseTypeDef,
    ProfileDetailResponseTypeDef,
    PutAttributeMappingRequestTypeDef,
    PutAttributeMappingResponseTypeDef,
    PutNotificationSettingsRequestTypeDef,
    PutNotificationSettingsResponseTypeDef,
    ResetNotificationSettingsRequestTypeDef,
    ResetNotificationSettingsResponseTypeDef,
    ScalarCrlRequestRequestExtraExtraTypeDef,
    ScalarCrlRequestRequestExtraTypeDef,
    ScalarCrlRequestRequestTypeDef,
    ScalarCrlRequestTypeDef,
    ScalarProfileRequestRequestExtraExtraTypeDef,
    ScalarProfileRequestRequestExtraTypeDef,
    ScalarProfileRequestRequestTypeDef,
    ScalarProfileRequestTypeDef,
    ScalarSubjectRequestTypeDef,
    ScalarTrustAnchorRequestRequestExtraExtraTypeDef,
    ScalarTrustAnchorRequestRequestExtraTypeDef,
    ScalarTrustAnchorRequestRequestTypeDef,
    ScalarTrustAnchorRequestTypeDef,
    SubjectDetailResponseTypeDef,
    TagResourceRequestTypeDef,
    TrustAnchorDetailResponseTypeDef,
    UntagResourceRequestTypeDef,
    UpdateCrlRequestTypeDef,
    UpdateProfileRequestTypeDef,
    UpdateTrustAnchorRequestTypeDef,
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

__all__ = ("IAMRolesAnywhereClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class IAMRolesAnywhereClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IAMRolesAnywhereClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#generate_presigned_url)
        """

    def create_profile(
        self, **kwargs: Unpack[CreateProfileRequestTypeDef]
    ) -> ProfileDetailResponseTypeDef:
        """
        Creates a <i>profile</i>, a list of the roles that Roles Anywhere service is
        trusted to assume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/create_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#create_profile)
        """

    def create_trust_anchor(
        self, **kwargs: Unpack[CreateTrustAnchorRequestTypeDef]
    ) -> TrustAnchorDetailResponseTypeDef:
        """
        Creates a trust anchor to establish trust between IAM Roles Anywhere and your
        certificate authority (CA).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/create_trust_anchor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#create_trust_anchor)
        """

    def delete_attribute_mapping(
        self, **kwargs: Unpack[DeleteAttributeMappingRequestTypeDef]
    ) -> DeleteAttributeMappingResponseTypeDef:
        """
        Delete an entry from the attribute mapping rules enforced by a given profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/delete_attribute_mapping.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#delete_attribute_mapping)
        """

    def delete_crl(self, **kwargs: Unpack[ScalarCrlRequestTypeDef]) -> CrlDetailResponseTypeDef:
        """
        Deletes a certificate revocation list (CRL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/delete_crl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#delete_crl)
        """

    def delete_profile(
        self, **kwargs: Unpack[ScalarProfileRequestTypeDef]
    ) -> ProfileDetailResponseTypeDef:
        """
        Deletes a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/delete_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#delete_profile)
        """

    def delete_trust_anchor(
        self, **kwargs: Unpack[ScalarTrustAnchorRequestTypeDef]
    ) -> TrustAnchorDetailResponseTypeDef:
        """
        Deletes a trust anchor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/delete_trust_anchor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#delete_trust_anchor)
        """

    def disable_crl(
        self, **kwargs: Unpack[ScalarCrlRequestRequestTypeDef]
    ) -> CrlDetailResponseTypeDef:
        """
        Disables a certificate revocation list (CRL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/disable_crl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#disable_crl)
        """

    def disable_profile(
        self, **kwargs: Unpack[ScalarProfileRequestRequestTypeDef]
    ) -> ProfileDetailResponseTypeDef:
        """
        Disables a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/disable_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#disable_profile)
        """

    def disable_trust_anchor(
        self, **kwargs: Unpack[ScalarTrustAnchorRequestRequestTypeDef]
    ) -> TrustAnchorDetailResponseTypeDef:
        """
        Disables a trust anchor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/disable_trust_anchor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#disable_trust_anchor)
        """

    def enable_crl(
        self, **kwargs: Unpack[ScalarCrlRequestRequestExtraTypeDef]
    ) -> CrlDetailResponseTypeDef:
        """
        Enables a certificate revocation list (CRL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/enable_crl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#enable_crl)
        """

    def enable_profile(
        self, **kwargs: Unpack[ScalarProfileRequestRequestExtraTypeDef]
    ) -> ProfileDetailResponseTypeDef:
        """
        Enables temporary credential requests for a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/enable_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#enable_profile)
        """

    def enable_trust_anchor(
        self, **kwargs: Unpack[ScalarTrustAnchorRequestRequestExtraTypeDef]
    ) -> TrustAnchorDetailResponseTypeDef:
        """
        Enables a trust anchor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/enable_trust_anchor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#enable_trust_anchor)
        """

    def get_crl(
        self, **kwargs: Unpack[ScalarCrlRequestRequestExtraExtraTypeDef]
    ) -> CrlDetailResponseTypeDef:
        """
        Gets a certificate revocation list (CRL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/get_crl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#get_crl)
        """

    def get_profile(
        self, **kwargs: Unpack[ScalarProfileRequestRequestExtraExtraTypeDef]
    ) -> ProfileDetailResponseTypeDef:
        """
        Gets a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/get_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#get_profile)
        """

    def get_subject(
        self, **kwargs: Unpack[ScalarSubjectRequestTypeDef]
    ) -> SubjectDetailResponseTypeDef:
        """
        Gets a <i>subject</i>, which associates a certificate identity with
        authentication attempts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/get_subject.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#get_subject)
        """

    def get_trust_anchor(
        self, **kwargs: Unpack[ScalarTrustAnchorRequestRequestExtraExtraTypeDef]
    ) -> TrustAnchorDetailResponseTypeDef:
        """
        Gets a trust anchor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/get_trust_anchor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#get_trust_anchor)
        """

    def import_crl(self, **kwargs: Unpack[ImportCrlRequestTypeDef]) -> CrlDetailResponseTypeDef:
        """
        Imports the certificate revocation list (CRL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/import_crl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#import_crl)
        """

    def list_crls(self, **kwargs: Unpack[ListRequestTypeDef]) -> ListCrlsResponseTypeDef:
        """
        Lists all certificate revocation lists (CRL) in the authenticated account and
        Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/list_crls.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#list_crls)
        """

    def list_profiles(
        self, **kwargs: Unpack[ListRequestRequestTypeDef]
    ) -> ListProfilesResponseTypeDef:
        """
        Lists all profiles in the authenticated account and Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/list_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#list_profiles)
        """

    def list_subjects(
        self, **kwargs: Unpack[ListRequestRequestExtraTypeDef]
    ) -> ListSubjectsResponseTypeDef:
        """
        Lists the subjects in the authenticated account and Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/list_subjects.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#list_subjects)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags attached to the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#list_tags_for_resource)
        """

    def list_trust_anchors(
        self, **kwargs: Unpack[ListRequestRequestExtraExtraTypeDef]
    ) -> ListTrustAnchorsResponseTypeDef:
        """
        Lists the trust anchors in the authenticated account and Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/list_trust_anchors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#list_trust_anchors)
        """

    def put_attribute_mapping(
        self, **kwargs: Unpack[PutAttributeMappingRequestTypeDef]
    ) -> PutAttributeMappingResponseTypeDef:
        """
        Put an entry in the attribute mapping rules that will be enforced by a given
        profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/put_attribute_mapping.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#put_attribute_mapping)
        """

    def put_notification_settings(
        self, **kwargs: Unpack[PutNotificationSettingsRequestTypeDef]
    ) -> PutNotificationSettingsResponseTypeDef:
        """
        Attaches a list of <i>notification settings</i> to a trust anchor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/put_notification_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#put_notification_settings)
        """

    def reset_notification_settings(
        self, **kwargs: Unpack[ResetNotificationSettingsRequestTypeDef]
    ) -> ResetNotificationSettingsResponseTypeDef:
        """
        Resets the <i>custom notification setting</i> to IAM Roles Anywhere default
        setting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/reset_notification_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#reset_notification_settings)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Attaches tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#untag_resource)
        """

    def update_crl(self, **kwargs: Unpack[UpdateCrlRequestTypeDef]) -> CrlDetailResponseTypeDef:
        """
        Updates the certificate revocation list (CRL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/update_crl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#update_crl)
        """

    def update_profile(
        self, **kwargs: Unpack[UpdateProfileRequestTypeDef]
    ) -> ProfileDetailResponseTypeDef:
        """
        Updates a <i>profile</i>, a list of the roles that IAM Roles Anywhere service
        is trusted to assume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/update_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#update_profile)
        """

    def update_trust_anchor(
        self, **kwargs: Unpack[UpdateTrustAnchorRequestTypeDef]
    ) -> TrustAnchorDetailResponseTypeDef:
        """
        Updates a trust anchor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/update_trust_anchor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#update_trust_anchor)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_crls"]
    ) -> ListCrlsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_profiles"]
    ) -> ListProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_subjects"]
    ) -> ListSubjectsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_trust_anchors"]
    ) -> ListTrustAnchorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client/#get_paginator)
        """
