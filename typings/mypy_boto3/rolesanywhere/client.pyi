"""
Type annotations for rolesanywhere service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_rolesanywhere import IAMRolesAnywhereClient

    client: IAMRolesAnywhereClient = boto3.client("rolesanywhere")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .paginator import (
    ListCrlsPaginator,
    ListProfilesPaginator,
    ListSubjectsPaginator,
    ListTrustAnchorsPaginator,
)
from .type_defs import (
    CrlDetailResponseTypeDef,
    ListCrlsResponseTypeDef,
    ListProfilesResponseTypeDef,
    ListSubjectsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTrustAnchorsResponseTypeDef,
    ProfileDetailResponseTypeDef,
    SourceTypeDef,
    SubjectDetailResponseTypeDef,
    TagTypeDef,
    TrustAnchorDetailResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("IAMRolesAnywhereClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class IAMRolesAnywhereClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IAMRolesAnywhereClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#close)
        """
    def create_profile(
        self,
        *,
        name: str,
        roleArns: List[str],
        durationSeconds: int = None,
        enabled: bool = None,
        managedPolicyArns: List[str] = None,
        requireInstanceProperties: bool = None,
        sessionPolicy: str = None,
        tags: List["TagTypeDef"] = None
    ) -> ProfileDetailResponseTypeDef:
        """
        Creates a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.create_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#create_profile)
        """
    def create_trust_anchor(
        self,
        *,
        name: str,
        source: "SourceTypeDef",
        enabled: bool = None,
        tags: List["TagTypeDef"] = None
    ) -> TrustAnchorDetailResponseTypeDef:
        """
        Creates a trust anchor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.create_trust_anchor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#create_trust_anchor)
        """
    def delete_crl(self, *, crlId: str) -> CrlDetailResponseTypeDef:
        """
        Deletes a certificate revocation list (CRL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.delete_crl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#delete_crl)
        """
    def delete_profile(self, *, profileId: str) -> ProfileDetailResponseTypeDef:
        """
        Deletes a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.delete_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#delete_profile)
        """
    def delete_trust_anchor(self, *, trustAnchorId: str) -> TrustAnchorDetailResponseTypeDef:
        """
        Deletes a trust anchor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.delete_trust_anchor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#delete_trust_anchor)
        """
    def disable_crl(self, *, crlId: str) -> CrlDetailResponseTypeDef:
        """
        Disables a certificate revocation list (CRL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.disable_crl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#disable_crl)
        """
    def disable_profile(self, *, profileId: str) -> ProfileDetailResponseTypeDef:
        """
        Disables a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.disable_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#disable_profile)
        """
    def disable_trust_anchor(self, *, trustAnchorId: str) -> TrustAnchorDetailResponseTypeDef:
        """
        Disables a trust anchor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.disable_trust_anchor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#disable_trust_anchor)
        """
    def enable_crl(self, *, crlId: str) -> CrlDetailResponseTypeDef:
        """
        Enables a certificate revocation list (CRL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.enable_crl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#enable_crl)
        """
    def enable_profile(self, *, profileId: str) -> ProfileDetailResponseTypeDef:
        """
        Enables the roles in a profile to receive session credentials in `CreateSession
        <https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_CreateSession
        .html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.enable_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#enable_profile)
        """
    def enable_trust_anchor(self, *, trustAnchorId: str) -> TrustAnchorDetailResponseTypeDef:
        """
        Enables a trust anchor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.enable_trust_anchor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#enable_trust_anchor)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#generate_presigned_url)
        """
    def get_crl(self, *, crlId: str) -> CrlDetailResponseTypeDef:
        """
        Gets a certificate revocation list (CRL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.get_crl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#get_crl)
        """
    def get_profile(self, *, profileId: str) -> ProfileDetailResponseTypeDef:
        """
        Gets a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.get_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#get_profile)
        """
    def get_subject(self, *, subjectId: str) -> SubjectDetailResponseTypeDef:
        """
        Gets a Subject.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.get_subject)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#get_subject)
        """
    def get_trust_anchor(self, *, trustAnchorId: str) -> TrustAnchorDetailResponseTypeDef:
        """
        Gets a trust anchor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.get_trust_anchor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#get_trust_anchor)
        """
    def import_crl(
        self,
        *,
        crlData: Union[bytes, IO[bytes], StreamingBody],
        name: str,
        trustAnchorArn: str,
        enabled: bool = None,
        tags: List["TagTypeDef"] = None
    ) -> CrlDetailResponseTypeDef:
        """
        Imports the certificate revocation list (CRL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.import_crl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#import_crl)
        """
    def list_crls(self, *, nextToken: str = None, pageSize: int = None) -> ListCrlsResponseTypeDef:
        """
        Lists all Crls in the authenticated account and Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.list_crls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#list_crls)
        """
    def list_profiles(
        self, *, nextToken: str = None, pageSize: int = None
    ) -> ListProfilesResponseTypeDef:
        """
        Lists all profiles in the authenticated account and Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.list_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#list_profiles)
        """
    def list_subjects(
        self, *, nextToken: str = None, pageSize: int = None
    ) -> ListSubjectsResponseTypeDef:
        """
        Lists the subjects in the authenticated account and Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.list_subjects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#list_subjects)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags attached to the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#list_tags_for_resource)
        """
    def list_trust_anchors(
        self, *, nextToken: str = None, pageSize: int = None
    ) -> ListTrustAnchorsResponseTypeDef:
        """
        Lists the trust anchors in the authenticated account and Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.list_trust_anchors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#list_trust_anchors)
        """
    def tag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Attaches tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#untag_resource)
        """
    def update_crl(
        self,
        *,
        crlId: str,
        crlData: Union[bytes, IO[bytes], StreamingBody] = None,
        name: str = None
    ) -> CrlDetailResponseTypeDef:
        """
        Updates the certificate revocation list (CRL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.update_crl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#update_crl)
        """
    def update_profile(
        self,
        *,
        profileId: str,
        durationSeconds: int = None,
        managedPolicyArns: List[str] = None,
        name: str = None,
        roleArns: List[str] = None,
        sessionPolicy: str = None
    ) -> ProfileDetailResponseTypeDef:
        """
        Updates the profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.update_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#update_profile)
        """
    def update_trust_anchor(
        self, *, trustAnchorId: str, name: str = None, source: "SourceTypeDef" = None
    ) -> TrustAnchorDetailResponseTypeDef:
        """
        Updates the trust anchor.You establish trust between IAM Roles Anywhere and your
        certificate authority (CA) by configuring a trust anchor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.update_trust_anchor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/client.html#update_trust_anchor)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_crls"]) -> ListCrlsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Paginator.ListCrls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/paginators.html#listcrlspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_profiles"]) -> ListProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Paginator.ListProfiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/paginators.html#listprofilespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_subjects"]) -> ListSubjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Paginator.ListSubjects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/paginators.html#listsubjectspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_trust_anchors"]
    ) -> ListTrustAnchorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rolesanywhere.html#IAMRolesAnywhere.Paginator.ListTrustAnchors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rolesanywhere/paginators.html#listtrustanchorspaginator)
        """
