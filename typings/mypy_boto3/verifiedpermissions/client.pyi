"""
Type annotations for verifiedpermissions service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_verifiedpermissions.client import VerifiedPermissionsClient

    session = Session()
    client: VerifiedPermissionsClient = session.client("verifiedpermissions")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListIdentitySourcesPaginator,
    ListPoliciesPaginator,
    ListPolicyStoresPaginator,
    ListPolicyTemplatesPaginator,
)
from .type_defs import (
    BatchGetPolicyInputTypeDef,
    BatchGetPolicyOutputTypeDef,
    BatchIsAuthorizedInputTypeDef,
    BatchIsAuthorizedOutputTypeDef,
    BatchIsAuthorizedWithTokenInputTypeDef,
    BatchIsAuthorizedWithTokenOutputTypeDef,
    CreateIdentitySourceInputTypeDef,
    CreateIdentitySourceOutputTypeDef,
    CreatePolicyInputTypeDef,
    CreatePolicyOutputTypeDef,
    CreatePolicyStoreInputTypeDef,
    CreatePolicyStoreOutputTypeDef,
    CreatePolicyTemplateInputTypeDef,
    CreatePolicyTemplateOutputTypeDef,
    DeleteIdentitySourceInputTypeDef,
    DeletePolicyInputTypeDef,
    DeletePolicyStoreInputTypeDef,
    DeletePolicyTemplateInputTypeDef,
    GetIdentitySourceInputTypeDef,
    GetIdentitySourceOutputTypeDef,
    GetPolicyInputTypeDef,
    GetPolicyOutputTypeDef,
    GetPolicyStoreInputTypeDef,
    GetPolicyStoreOutputTypeDef,
    GetPolicyTemplateInputTypeDef,
    GetPolicyTemplateOutputTypeDef,
    GetSchemaInputTypeDef,
    GetSchemaOutputTypeDef,
    IsAuthorizedInputTypeDef,
    IsAuthorizedOutputTypeDef,
    IsAuthorizedWithTokenInputTypeDef,
    IsAuthorizedWithTokenOutputTypeDef,
    ListIdentitySourcesInputTypeDef,
    ListIdentitySourcesOutputTypeDef,
    ListPoliciesInputTypeDef,
    ListPoliciesOutputTypeDef,
    ListPolicyStoresInputTypeDef,
    ListPolicyStoresOutputTypeDef,
    ListPolicyTemplatesInputTypeDef,
    ListPolicyTemplatesOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    PutSchemaInputTypeDef,
    PutSchemaOutputTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
    UpdateIdentitySourceInputTypeDef,
    UpdateIdentitySourceOutputTypeDef,
    UpdatePolicyInputTypeDef,
    UpdatePolicyOutputTypeDef,
    UpdatePolicyStoreInputTypeDef,
    UpdatePolicyStoreOutputTypeDef,
    UpdatePolicyTemplateInputTypeDef,
    UpdatePolicyTemplateOutputTypeDef,
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

__all__ = ("VerifiedPermissionsClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidStateException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class VerifiedPermissionsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions.html#VerifiedPermissions.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        VerifiedPermissionsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions.html#VerifiedPermissions.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#generate_presigned_url)
        """

    def batch_get_policy(
        self, **kwargs: Unpack[BatchGetPolicyInputTypeDef]
    ) -> BatchGetPolicyOutputTypeDef:
        """
        Retrieves information about a group (batch) of policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/batch_get_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#batch_get_policy)
        """

    def batch_is_authorized(
        self, **kwargs: Unpack[BatchIsAuthorizedInputTypeDef]
    ) -> BatchIsAuthorizedOutputTypeDef:
        """
        Makes a series of decisions about multiple authorization requests for one
        principal or resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/batch_is_authorized.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#batch_is_authorized)
        """

    def batch_is_authorized_with_token(
        self, **kwargs: Unpack[BatchIsAuthorizedWithTokenInputTypeDef]
    ) -> BatchIsAuthorizedWithTokenOutputTypeDef:
        """
        Makes a series of decisions about multiple authorization requests for one token.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/batch_is_authorized_with_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#batch_is_authorized_with_token)
        """

    def create_identity_source(
        self, **kwargs: Unpack[CreateIdentitySourceInputTypeDef]
    ) -> CreateIdentitySourceOutputTypeDef:
        """
        Adds an identity source to a policy store-an Amazon Cognito user pool or OpenID
        Connect (OIDC) identity provider (IdP).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/create_identity_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#create_identity_source)
        """

    def create_policy(
        self, **kwargs: Unpack[CreatePolicyInputTypeDef]
    ) -> CreatePolicyOutputTypeDef:
        """
        Creates a Cedar policy and saves it in the specified policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/create_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#create_policy)
        """

    def create_policy_store(
        self, **kwargs: Unpack[CreatePolicyStoreInputTypeDef]
    ) -> CreatePolicyStoreOutputTypeDef:
        """
        Creates a policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/create_policy_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#create_policy_store)
        """

    def create_policy_template(
        self, **kwargs: Unpack[CreatePolicyTemplateInputTypeDef]
    ) -> CreatePolicyTemplateOutputTypeDef:
        """
        Creates a policy template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/create_policy_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#create_policy_template)
        """

    def delete_identity_source(
        self, **kwargs: Unpack[DeleteIdentitySourceInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an identity source that references an identity provider (IdP) such as
        Amazon Cognito.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/delete_identity_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#delete_identity_source)
        """

    def delete_policy(self, **kwargs: Unpack[DeletePolicyInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified policy from the policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/delete_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#delete_policy)
        """

    def delete_policy_store(
        self, **kwargs: Unpack[DeletePolicyStoreInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/delete_policy_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#delete_policy_store)
        """

    def delete_policy_template(
        self, **kwargs: Unpack[DeletePolicyTemplateInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified policy template from the policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/delete_policy_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#delete_policy_template)
        """

    def get_identity_source(
        self, **kwargs: Unpack[GetIdentitySourceInputTypeDef]
    ) -> GetIdentitySourceOutputTypeDef:
        """
        Retrieves the details about the specified identity source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/get_identity_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#get_identity_source)
        """

    def get_policy(self, **kwargs: Unpack[GetPolicyInputTypeDef]) -> GetPolicyOutputTypeDef:
        """
        Retrieves information about the specified policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/get_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#get_policy)
        """

    def get_policy_store(
        self, **kwargs: Unpack[GetPolicyStoreInputTypeDef]
    ) -> GetPolicyStoreOutputTypeDef:
        """
        Retrieves details about a policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/get_policy_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#get_policy_store)
        """

    def get_policy_template(
        self, **kwargs: Unpack[GetPolicyTemplateInputTypeDef]
    ) -> GetPolicyTemplateOutputTypeDef:
        """
        Retrieve the details for the specified policy template in the specified policy
        store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/get_policy_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#get_policy_template)
        """

    def get_schema(self, **kwargs: Unpack[GetSchemaInputTypeDef]) -> GetSchemaOutputTypeDef:
        """
        Retrieve the details for the specified schema in the specified policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/get_schema.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#get_schema)
        """

    def is_authorized(
        self, **kwargs: Unpack[IsAuthorizedInputTypeDef]
    ) -> IsAuthorizedOutputTypeDef:
        """
        Makes an authorization decision about a service request described in the
        parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/is_authorized.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#is_authorized)
        """

    def is_authorized_with_token(
        self, **kwargs: Unpack[IsAuthorizedWithTokenInputTypeDef]
    ) -> IsAuthorizedWithTokenOutputTypeDef:
        """
        Makes an authorization decision about a service request described in the
        parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/is_authorized_with_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#is_authorized_with_token)
        """

    def list_identity_sources(
        self, **kwargs: Unpack[ListIdentitySourcesInputTypeDef]
    ) -> ListIdentitySourcesOutputTypeDef:
        """
        Returns a paginated list of all of the identity sources defined in the
        specified policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/list_identity_sources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#list_identity_sources)
        """

    def list_policies(
        self, **kwargs: Unpack[ListPoliciesInputTypeDef]
    ) -> ListPoliciesOutputTypeDef:
        """
        Returns a paginated list of all policies stored in the specified policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/list_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#list_policies)
        """

    def list_policy_stores(
        self, **kwargs: Unpack[ListPolicyStoresInputTypeDef]
    ) -> ListPolicyStoresOutputTypeDef:
        """
        Returns a paginated list of all policy stores in the calling Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/list_policy_stores.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#list_policy_stores)
        """

    def list_policy_templates(
        self, **kwargs: Unpack[ListPolicyTemplatesInputTypeDef]
    ) -> ListPolicyTemplatesOutputTypeDef:
        """
        Returns a paginated list of all policy templates in the specified policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/list_policy_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#list_policy_templates)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Returns the tags associated with the specified Amazon Verified Permissions
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#list_tags_for_resource)
        """

    def put_schema(self, **kwargs: Unpack[PutSchemaInputTypeDef]) -> PutSchemaOutputTypeDef:
        """
        Creates or updates the policy schema in the specified policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/put_schema.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#put_schema)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified Amazon Verified
        Permissions resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified Amazon Verified Permissions
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#untag_resource)
        """

    def update_identity_source(
        self, **kwargs: Unpack[UpdateIdentitySourceInputTypeDef]
    ) -> UpdateIdentitySourceOutputTypeDef:
        """
        Updates the specified identity source to use a new identity provider (IdP), or
        to change the mapping of identities from the IdP to a different principal
        entity type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/update_identity_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#update_identity_source)
        """

    def update_policy(
        self, **kwargs: Unpack[UpdatePolicyInputTypeDef]
    ) -> UpdatePolicyOutputTypeDef:
        """
        Modifies a Cedar static policy in the specified policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/update_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#update_policy)
        """

    def update_policy_store(
        self, **kwargs: Unpack[UpdatePolicyStoreInputTypeDef]
    ) -> UpdatePolicyStoreOutputTypeDef:
        """
        Modifies the validation setting for a policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/update_policy_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#update_policy_store)
        """

    def update_policy_template(
        self, **kwargs: Unpack[UpdatePolicyTemplateInputTypeDef]
    ) -> UpdatePolicyTemplateOutputTypeDef:
        """
        Updates the specified policy template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/update_policy_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#update_policy_template)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_identity_sources"]
    ) -> ListIdentitySourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_policies"]
    ) -> ListPoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_policy_stores"]
    ) -> ListPolicyStoresPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_policy_templates"]
    ) -> ListPolicyTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/verifiedpermissions/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client/#get_paginator)
        """
