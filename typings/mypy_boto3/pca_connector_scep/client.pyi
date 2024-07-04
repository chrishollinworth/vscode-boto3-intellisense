"""
Type annotations for pca-connector-scep service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_pca_connector_scep import PrivateCAConnectorforSCEPClient

    client: PrivateCAConnectorforSCEPClient = boto3.client("pca-connector-scep")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import ListChallengeMetadataPaginator, ListConnectorsPaginator
from .type_defs import (
    CreateChallengeResponseTypeDef,
    CreateConnectorResponseTypeDef,
    GetChallengeMetadataResponseTypeDef,
    GetChallengePasswordResponseTypeDef,
    GetConnectorResponseTypeDef,
    ListChallengeMetadataResponseTypeDef,
    ListConnectorsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MobileDeviceManagementTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("PrivateCAConnectorforSCEPClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class PrivateCAConnectorforSCEPClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PrivateCAConnectorforSCEPClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client.html#close)
        """

    def create_challenge(
        self, *, ConnectorArn: str, ClientToken: str = None, Tags: Dict[str, str] = None
    ) -> CreateChallengeResponseTypeDef:
        """
        For general-purpose connectors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.create_challenge)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client.html#create_challenge)
        """

    def create_connector(
        self,
        *,
        CertificateAuthorityArn: str,
        MobileDeviceManagement: "MobileDeviceManagementTypeDef" = None,
        ClientToken: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateConnectorResponseTypeDef:
        """
        Creates a SCEP connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.create_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client.html#create_connector)
        """

    def delete_challenge(self, *, ChallengeArn: str) -> None:
        """
        Deletes the specified `Challenge <https://docs.aws.amazon.com/C4SCEP_API/pca-
        connector-scep/latest/APIReference/API_Challenge.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.delete_challenge)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client.html#delete_challenge)
        """

    def delete_connector(self, *, ConnectorArn: str) -> None:
        """
        Deletes the specified `Connector <https://docs.aws.amazon.com/C4SCEP_API/pca-
        connector-scep/latest/APIReference/API_Connector.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.delete_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client.html#delete_connector)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client.html#generate_presigned_url)
        """

    def get_challenge_metadata(self, *, ChallengeArn: str) -> GetChallengeMetadataResponseTypeDef:
        """
        Retrieves the metadata for the specified `Challenge
        <https://docs.aws.amazon.com/C4SCEP_API/pca-connector-
        scep/latest/APIReference/API_Challenge.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.get_challenge_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client.html#get_challenge_metadata)
        """

    def get_challenge_password(self, *, ChallengeArn: str) -> GetChallengePasswordResponseTypeDef:
        """
        Retrieves the challenge password for the specified `Challenge
        <https://docs.aws.amazon.com/C4SCEP_API/pca-connector-
        scep/latest/APIReference/API_Challenge.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.get_challenge_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client.html#get_challenge_password)
        """

    def get_connector(self, *, ConnectorArn: str) -> GetConnectorResponseTypeDef:
        """
        Retrieves details about the specified `Connector
        <https://docs.aws.amazon.com/C4SCEP_API/pca-connector-
        scep/latest/APIReference/API_Connector.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.get_connector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client.html#get_connector)
        """

    def list_challenge_metadata(
        self, *, ConnectorArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListChallengeMetadataResponseTypeDef:
        """
        Retrieves the challenge metadata for the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.list_challenge_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client.html#list_challenge_metadata)
        """

    def list_connectors(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListConnectorsResponseTypeDef:
        """
        Lists the connectors belonging to your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.list_connectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client.html#list_connectors)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the tags associated with the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client.html#list_tags_for_resource)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        Adds one or more tags to your resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        Removes one or more tags from your resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/client.html#untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_challenge_metadata"]
    ) -> ListChallengeMetadataPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Paginator.ListChallengeMetadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/paginators.html#listchallengemetadatapaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_connectors"]) -> ListConnectorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/pca-connector-scep.html#PrivateCAConnectorforSCEP.Paginator.ListConnectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/paginators.html#listconnectorspaginator)
        """
