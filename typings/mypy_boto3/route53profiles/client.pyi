"""
Type annotations for route53profiles service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_route53profiles import Route53ProfilesClient

    client: Route53ProfilesClient = boto3.client("route53profiles")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListProfileAssociationsPaginator,
    ListProfileResourceAssociationsPaginator,
    ListProfilesPaginator,
)
from .type_defs import (
    AssociateProfileResponseTypeDef,
    AssociateResourceToProfileResponseTypeDef,
    CreateProfileResponseTypeDef,
    DeleteProfileResponseTypeDef,
    DisassociateProfileResponseTypeDef,
    DisassociateResourceFromProfileResponseTypeDef,
    GetProfileAssociationResponseTypeDef,
    GetProfileResourceAssociationResponseTypeDef,
    GetProfileResponseTypeDef,
    ListProfileAssociationsResponseTypeDef,
    ListProfileResourceAssociationsResponseTypeDef,
    ListProfilesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagTypeDef,
    UpdateProfileResourceAssociationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("Route53ProfilesClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/route53profiles.html#Route53Profiles.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        Route53ProfilesClient exceptions.
        """

    def associate_profile(
        self, *, Name: str, ProfileId: str, ResourceId: str, Tags: List["TagTypeDef"] = None
    ) -> AssociateProfileResponseTypeDef:
        """
        Associates a Route 53 Profiles profile with a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/route53profiles.html#Route53Profiles.Client.associate_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client.html#associate_profile)
        """

    def associate_resource_to_profile(
        self, *, Name: str, ProfileId: str, ResourceArn: str, ResourceProperties: str = None
    ) -> AssociateResourceToProfileResponseTypeDef:
        """
        Associates a DNS reource configuration to a Route 53 Profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/route53profiles.html#Route53Profiles.Client.associate_resource_to_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client.html#associate_resource_to_profile)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/route53profiles.html#Route53Profiles.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/route53profiles.html#Route53Profiles.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client.html#close)
        """

    def create_profile(
        self, *, ClientToken: str, Name: str, Tags: List["TagTypeDef"] = None
    ) -> CreateProfileResponseTypeDef:
        """
        Creates an empty Route 53 Profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/route53profiles.html#Route53Profiles.Client.create_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client.html#create_profile)
        """

    def delete_profile(self, *, ProfileId: str) -> DeleteProfileResponseTypeDef:
        """
        Deletes the specified Route 53 Profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/route53profiles.html#Route53Profiles.Client.delete_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client.html#delete_profile)
        """

    def disassociate_profile(
        self, *, ProfileId: str, ResourceId: str
    ) -> DisassociateProfileResponseTypeDef:
        """
        Dissociates a specified Route 53 Profile from the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/route53profiles.html#Route53Profiles.Client.disassociate_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client.html#disassociate_profile)
        """

    def disassociate_resource_from_profile(
        self, *, ProfileId: str, ResourceArn: str
    ) -> DisassociateResourceFromProfileResponseTypeDef:
        """
        Dissoaciated a specified resource, from the Route 53 Profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/route53profiles.html#Route53Profiles.Client.disassociate_resource_from_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client.html#disassociate_resource_from_profile)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/route53profiles.html#Route53Profiles.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client.html#generate_presigned_url)
        """

    def get_profile(self, *, ProfileId: str) -> GetProfileResponseTypeDef:
        """
        Returns information about a specified Route 53 Profile, such as whether whether
        the Profile is shared, and the current status of the Profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/route53profiles.html#Route53Profiles.Client.get_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client.html#get_profile)
        """

    def get_profile_association(
        self, *, ProfileAssociationId: str
    ) -> GetProfileAssociationResponseTypeDef:
        """
        Retrieves a Route 53 Profile association for a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/route53profiles.html#Route53Profiles.Client.get_profile_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client.html#get_profile_association)
        """

    def get_profile_resource_association(
        self, *, ProfileResourceAssociationId: str
    ) -> GetProfileResourceAssociationResponseTypeDef:
        """
        Returns information about a specified Route 53 Profile resource association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/route53profiles.html#Route53Profiles.Client.get_profile_resource_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client.html#get_profile_resource_association)
        """

    def list_profile_associations(
        self,
        *,
        MaxResults: int = None,
        NextToken: str = None,
        ProfileId: str = None,
        ResourceId: str = None
    ) -> ListProfileAssociationsResponseTypeDef:
        """
        Lists all the VPCs that the specified Route 53 Profile is associated with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/route53profiles.html#Route53Profiles.Client.list_profile_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client.html#list_profile_associations)
        """

    def list_profile_resource_associations(
        self,
        *,
        ProfileId: str,
        MaxResults: int = None,
        NextToken: str = None,
        ResourceType: str = None
    ) -> ListProfileResourceAssociationsResponseTypeDef:
        """
        Lists all the resource associations for the specified Route 53 Profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/route53profiles.html#Route53Profiles.Client.list_profile_resource_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client.html#list_profile_resource_associations)
        """

    def list_profiles(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListProfilesResponseTypeDef:
        """
        Lists all the Route 53 Profiles associated with your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/route53profiles.html#Route53Profiles.Client.list_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client.html#list_profiles)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags that you associated with the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/route53profiles.html#Route53Profiles.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client.html#list_tags_for_resource)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds one or more tags to a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/route53profiles.html#Route53Profiles.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/route53profiles.html#Route53Profiles.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client.html#untag_resource)
        """

    def update_profile_resource_association(
        self, *, ProfileResourceAssociationId: str, Name: str = None, ResourceProperties: str = None
    ) -> UpdateProfileResourceAssociationResponseTypeDef:
        """
        Updates the specified Route 53 Profile resourse association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/route53profiles.html#Route53Profiles.Client.update_profile_resource_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/client.html#update_profile_resource_association)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_profile_associations"]
    ) -> ListProfileAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/route53profiles.html#Route53Profiles.Paginator.ListProfileAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/paginators.html#listprofileassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_profile_resource_associations"]
    ) -> ListProfileResourceAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/route53profiles.html#Route53Profiles.Paginator.ListProfileResourceAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/paginators.html#listprofileresourceassociationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_profiles"]) -> ListProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/route53profiles.html#Route53Profiles.Paginator.ListProfiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/paginators.html#listprofilespaginator)
        """
