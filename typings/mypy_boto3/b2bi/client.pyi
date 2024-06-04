"""
Type annotations for b2bi service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_b2bi import B2BIClient

    client: B2BIClient = boto3.client("b2bi")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import FileFormatType, LoggingType, TransformerStatusType
from .paginator import (
    ListCapabilitiesPaginator,
    ListPartnershipsPaginator,
    ListProfilesPaginator,
    ListTransformersPaginator,
)
from .type_defs import (
    CapabilityConfigurationTypeDef,
    CreateCapabilityResponseTypeDef,
    CreatePartnershipResponseTypeDef,
    CreateProfileResponseTypeDef,
    CreateTransformerResponseTypeDef,
    EdiTypeTypeDef,
    GetCapabilityResponseTypeDef,
    GetPartnershipResponseTypeDef,
    GetProfileResponseTypeDef,
    GetTransformerJobResponseTypeDef,
    GetTransformerResponseTypeDef,
    ListCapabilitiesResponseTypeDef,
    ListPartnershipsResponseTypeDef,
    ListProfilesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTransformersResponseTypeDef,
    S3LocationTypeDef,
    StartTransformerJobResponseTypeDef,
    TagTypeDef,
    TestMappingResponseTypeDef,
    TestParsingResponseTypeDef,
    UpdateCapabilityResponseTypeDef,
    UpdatePartnershipResponseTypeDef,
    UpdateProfileResponseTypeDef,
    UpdateTransformerResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("B2BIClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class B2BIClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        B2BIClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#close)
        """

    def create_capability(
        self,
        *,
        name: str,
        type: Literal["edi"],
        configuration: "CapabilityConfigurationTypeDef",
        instructionsDocuments: List["S3LocationTypeDef"] = None,
        clientToken: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateCapabilityResponseTypeDef:
        """
        Instantiates a capability based on the specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.create_capability)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#create_capability)
        """

    def create_partnership(
        self,
        *,
        profileId: str,
        name: str,
        email: str,
        phone: str = None,
        capabilities: List[str] = None,
        clientToken: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreatePartnershipResponseTypeDef:
        """
        Creates a partnership between a customer and a trading partner, based on the
        supplied parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.create_partnership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#create_partnership)
        """

    def create_profile(
        self,
        *,
        name: str,
        phone: str,
        businessName: str,
        logging: LoggingType,
        email: str = None,
        clientToken: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateProfileResponseTypeDef:
        """
        Creates a customer profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.create_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#create_profile)
        """

    def create_transformer(
        self,
        *,
        name: str,
        fileFormat: FileFormatType,
        mappingTemplate: str,
        ediType: "EdiTypeTypeDef",
        sampleDocument: str = None,
        clientToken: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateTransformerResponseTypeDef:
        """
        Creates a transformer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.create_transformer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#create_transformer)
        """

    def delete_capability(self, *, capabilityId: str) -> None:
        """
        Deletes the specified capability.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.delete_capability)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#delete_capability)
        """

    def delete_partnership(self, *, partnershipId: str) -> None:
        """
        Deletes the specified partnership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.delete_partnership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#delete_partnership)
        """

    def delete_profile(self, *, profileId: str) -> None:
        """
        Deletes the specified profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.delete_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#delete_profile)
        """

    def delete_transformer(self, *, transformerId: str) -> None:
        """
        Deletes the specified transformer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.delete_transformer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#delete_transformer)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#generate_presigned_url)
        """

    def get_capability(self, *, capabilityId: str) -> GetCapabilityResponseTypeDef:
        """
        Retrieves the details for the specified capability.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.get_capability)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#get_capability)
        """

    def get_partnership(self, *, partnershipId: str) -> GetPartnershipResponseTypeDef:
        """
        Retrieves the details for a partnership, based on the partner and profile IDs
        specified.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.get_partnership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#get_partnership)
        """

    def get_profile(self, *, profileId: str) -> GetProfileResponseTypeDef:
        """
        Retrieves the details for the profile specified by the profile ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.get_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#get_profile)
        """

    def get_transformer(self, *, transformerId: str) -> GetTransformerResponseTypeDef:
        """
        Retrieves the details for the transformer specified by the transformer ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.get_transformer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#get_transformer)
        """

    def get_transformer_job(
        self, *, transformerJobId: str, transformerId: str
    ) -> GetTransformerJobResponseTypeDef:
        """
        Returns the details of the transformer run, based on the Transformer job ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.get_transformer_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#get_transformer_job)
        """

    def list_capabilities(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListCapabilitiesResponseTypeDef:
        """
        Lists the capabilities associated with your Amazon Web Services account for your
        current or specified region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.list_capabilities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#list_capabilities)
        """

    def list_partnerships(
        self, *, profileId: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListPartnershipsResponseTypeDef:
        """
        Lists the partnerships associated with your Amazon Web Services account for your
        current or specified region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.list_partnerships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#list_partnerships)
        """

    def list_profiles(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListProfilesResponseTypeDef:
        """
        Lists the profiles associated with your Amazon Web Services account for your
        current or specified region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.list_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#list_profiles)
        """

    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all of the tags associated with the Amazon Resource Name (ARN) that you
        specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#list_tags_for_resource)
        """

    def list_transformers(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListTransformersResponseTypeDef:
        """
        Lists the available transformers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.list_transformers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#list_transformers)
        """

    def start_transformer_job(
        self,
        *,
        inputFile: "S3LocationTypeDef",
        outputLocation: "S3LocationTypeDef",
        transformerId: str,
        clientToken: str = None
    ) -> StartTransformerJobResponseTypeDef:
        """
        Runs a job, using a transformer, to parse input EDI (electronic data
        interchange) file into the output structures used by Amazon Web Services B2BI
        Data Interchange.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.start_transformer_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#start_transformer_job)
        """

    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> None:
        """
        Attaches a key-value pair to a resource, as identified by its Amazon Resource
        Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#tag_resource)
        """

    def test_mapping(
        self, *, inputFileContent: str, mappingTemplate: str, fileFormat: FileFormatType
    ) -> TestMappingResponseTypeDef:
        """
        Maps the input file according to the provided template file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.test_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#test_mapping)
        """

    def test_parsing(
        self,
        *,
        inputFile: "S3LocationTypeDef",
        fileFormat: FileFormatType,
        ediType: "EdiTypeTypeDef"
    ) -> TestParsingResponseTypeDef:
        """
        Parses the input EDI (electronic data interchange) file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.test_parsing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#test_parsing)
        """

    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> None:
        """
        Detaches a key-value pair from the specified resource, as identified by its
        Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#untag_resource)
        """

    def update_capability(
        self,
        *,
        capabilityId: str,
        name: str = None,
        configuration: "CapabilityConfigurationTypeDef" = None,
        instructionsDocuments: List["S3LocationTypeDef"] = None
    ) -> UpdateCapabilityResponseTypeDef:
        """
        Updates some of the parameters for a capability, based on the specified
        parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.update_capability)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#update_capability)
        """

    def update_partnership(
        self, *, partnershipId: str, name: str = None, capabilities: List[str] = None
    ) -> UpdatePartnershipResponseTypeDef:
        """
        Updates some of the parameters for a partnership between a customer and trading
        partner.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.update_partnership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#update_partnership)
        """

    def update_profile(
        self,
        *,
        profileId: str,
        name: str = None,
        email: str = None,
        phone: str = None,
        businessName: str = None
    ) -> UpdateProfileResponseTypeDef:
        """
        Updates the specified parameters for a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.update_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#update_profile)
        """

    def update_transformer(
        self,
        *,
        transformerId: str,
        name: str = None,
        fileFormat: FileFormatType = None,
        mappingTemplate: str = None,
        status: TransformerStatusType = None,
        ediType: "EdiTypeTypeDef" = None,
        sampleDocument: str = None
    ) -> UpdateTransformerResponseTypeDef:
        """
        Updates the specified parameters for a transformer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Client.update_transformer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client.html#update_transformer)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_capabilities"]
    ) -> ListCapabilitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Paginator.ListCapabilities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/paginators.html#listcapabilitiespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_partnerships"]
    ) -> ListPartnershipsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Paginator.ListPartnerships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/paginators.html#listpartnershipspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_profiles"]) -> ListProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Paginator.ListProfiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/paginators.html#listprofilespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_transformers"]
    ) -> ListTransformersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/b2bi.html#B2BI.Paginator.ListTransformers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/paginators.html#listtransformerspaginator)
        """
