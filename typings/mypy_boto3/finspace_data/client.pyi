"""
Type annotations for finspace-data service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_finspace_data import FinSpaceDataClient

    client: FinSpaceDataClient = boto3.client("finspace-data")
    ```
"""
import sys
from typing import Any, Dict, Type

from botocore.client import BaseClient, ClientMeta

from .literals import ChangeTypeType, FormatTypeType, locationTypeType
from .type_defs import (
    CreateChangesetResponseTypeDef,
    GetProgrammaticAccessCredentialsResponseTypeDef,
    GetWorkingLocationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("FinSpaceDataClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class FinSpaceDataClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/finspace-data.html#FinSpaceData.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        FinSpaceDataClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/finspace-data.html#FinSpaceData.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#can_paginate)
        """
    def create_changeset(
        self,
        *,
        datasetId: str,
        changeType: ChangeTypeType,
        sourceType: Literal["S3"],
        sourceParams: Dict[str, str],
        formatType: FormatTypeType = None,
        formatParams: Dict[str, str] = None,
        tags: Dict[str, str] = None
    ) -> CreateChangesetResponseTypeDef:
        """
        Creates a new changeset in a FinSpace dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/finspace-data.html#FinSpaceData.Client.create_changeset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#create_changeset)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/finspace-data.html#FinSpaceData.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#generate_presigned_url)
        """
    def get_programmatic_access_credentials(
        self, *, environmentId: str, durationInMinutes: int = None
    ) -> GetProgrammaticAccessCredentialsResponseTypeDef:
        """
        Request programmatic credentials to use with Habanero SDK.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/finspace-data.html#FinSpaceData.Client.get_programmatic_access_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#get_programmatic_access_credentials)
        """
    def get_working_location(
        self, *, locationType: locationTypeType = None
    ) -> GetWorkingLocationResponseTypeDef:
        """
        A temporary Amazon S3 location to copy your files from a source location to
        stage or use as a scratch space in Habanero notebook.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/finspace-data.html#FinSpaceData.Client.get_working_location)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/client.html#get_working_location)
        """
