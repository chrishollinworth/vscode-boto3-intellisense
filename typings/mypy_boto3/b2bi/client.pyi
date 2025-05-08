"""
Type annotations for b2bi service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_b2bi.client import B2BIClient

    session = Session()
    client: B2BIClient = session.client("b2bi")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListCapabilitiesPaginator,
    ListPartnershipsPaginator,
    ListProfilesPaginator,
    ListTransformersPaginator,
)
from .type_defs import (
    CreateCapabilityRequestTypeDef,
    CreateCapabilityResponseTypeDef,
    CreatePartnershipRequestTypeDef,
    CreatePartnershipResponseTypeDef,
    CreateProfileRequestTypeDef,
    CreateProfileResponseTypeDef,
    CreateStarterMappingTemplateRequestTypeDef,
    CreateStarterMappingTemplateResponseTypeDef,
    CreateTransformerRequestTypeDef,
    CreateTransformerResponseTypeDef,
    DeleteCapabilityRequestTypeDef,
    DeletePartnershipRequestTypeDef,
    DeleteProfileRequestTypeDef,
    DeleteTransformerRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GenerateMappingRequestTypeDef,
    GenerateMappingResponseTypeDef,
    GetCapabilityRequestTypeDef,
    GetCapabilityResponseTypeDef,
    GetPartnershipRequestTypeDef,
    GetPartnershipResponseTypeDef,
    GetProfileRequestTypeDef,
    GetProfileResponseTypeDef,
    GetTransformerJobRequestTypeDef,
    GetTransformerJobResponseTypeDef,
    GetTransformerRequestTypeDef,
    GetTransformerResponseTypeDef,
    ListCapabilitiesRequestTypeDef,
    ListCapabilitiesResponseTypeDef,
    ListPartnershipsRequestTypeDef,
    ListPartnershipsResponseTypeDef,
    ListProfilesRequestTypeDef,
    ListProfilesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTransformersRequestTypeDef,
    ListTransformersResponseTypeDef,
    StartTransformerJobRequestTypeDef,
    StartTransformerJobResponseTypeDef,
    TagResourceRequestTypeDef,
    TestConversionRequestTypeDef,
    TestConversionResponseTypeDef,
    TestMappingRequestTypeDef,
    TestMappingResponseTypeDef,
    TestParsingRequestTypeDef,
    TestParsingResponseTypeDef,
    UntagResourceRequestTypeDef,
    UpdateCapabilityRequestTypeDef,
    UpdateCapabilityResponseTypeDef,
    UpdatePartnershipRequestTypeDef,
    UpdatePartnershipResponseTypeDef,
    UpdateProfileRequestTypeDef,
    UpdateProfileResponseTypeDef,
    UpdateTransformerRequestTypeDef,
    UpdateTransformerResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("B2BIClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi.html#B2BI.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        B2BIClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi.html#B2BI.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#generate_presigned_url)
        """

    def create_capability(
        self, **kwargs: Unpack[CreateCapabilityRequestTypeDef]
    ) -> CreateCapabilityResponseTypeDef:
        """
        Instantiates a capability based on the specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/create_capability.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#create_capability)
        """

    def create_partnership(
        self, **kwargs: Unpack[CreatePartnershipRequestTypeDef]
    ) -> CreatePartnershipResponseTypeDef:
        """
        Creates a partnership between a customer and a trading partner, based on the
        supplied parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/create_partnership.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#create_partnership)
        """

    def create_profile(
        self, **kwargs: Unpack[CreateProfileRequestTypeDef]
    ) -> CreateProfileResponseTypeDef:
        """
        Creates a customer profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/create_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#create_profile)
        """

    def create_starter_mapping_template(
        self, **kwargs: Unpack[CreateStarterMappingTemplateRequestTypeDef]
    ) -> CreateStarterMappingTemplateResponseTypeDef:
        """
        Amazon Web Services B2B Data Interchange uses a mapping template in JSONata or
        XSLT format to transform a customer input file into a JSON or XML file that can
        be converted to EDI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/create_starter_mapping_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#create_starter_mapping_template)
        """

    def create_transformer(
        self, **kwargs: Unpack[CreateTransformerRequestTypeDef]
    ) -> CreateTransformerResponseTypeDef:
        """
        Creates a transformer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/create_transformer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#create_transformer)
        """

    def delete_capability(
        self, **kwargs: Unpack[DeleteCapabilityRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified capability.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/delete_capability.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#delete_capability)
        """

    def delete_partnership(
        self, **kwargs: Unpack[DeletePartnershipRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified partnership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/delete_partnership.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#delete_partnership)
        """

    def delete_profile(
        self, **kwargs: Unpack[DeleteProfileRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/delete_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#delete_profile)
        """

    def delete_transformer(
        self, **kwargs: Unpack[DeleteTransformerRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified transformer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/delete_transformer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#delete_transformer)
        """

    def generate_mapping(
        self, **kwargs: Unpack[GenerateMappingRequestTypeDef]
    ) -> GenerateMappingResponseTypeDef:
        """
        Takes sample input and output documents and uses Amazon Bedrock to generate a
        mapping automatically.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/generate_mapping.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#generate_mapping)
        """

    def get_capability(
        self, **kwargs: Unpack[GetCapabilityRequestTypeDef]
    ) -> GetCapabilityResponseTypeDef:
        """
        Retrieves the details for the specified capability.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/get_capability.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#get_capability)
        """

    def get_partnership(
        self, **kwargs: Unpack[GetPartnershipRequestTypeDef]
    ) -> GetPartnershipResponseTypeDef:
        """
        Retrieves the details for a partnership, based on the partner and profile IDs
        specified.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/get_partnership.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#get_partnership)
        """

    def get_profile(self, **kwargs: Unpack[GetProfileRequestTypeDef]) -> GetProfileResponseTypeDef:
        """
        Retrieves the details for the profile specified by the profile ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/get_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#get_profile)
        """

    def get_transformer(
        self, **kwargs: Unpack[GetTransformerRequestTypeDef]
    ) -> GetTransformerResponseTypeDef:
        """
        Retrieves the details for the transformer specified by the transformer ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/get_transformer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#get_transformer)
        """

    def get_transformer_job(
        self, **kwargs: Unpack[GetTransformerJobRequestTypeDef]
    ) -> GetTransformerJobResponseTypeDef:
        """
        Returns the details of the transformer run, based on the Transformer job ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/get_transformer_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#get_transformer_job)
        """

    def list_capabilities(
        self, **kwargs: Unpack[ListCapabilitiesRequestTypeDef]
    ) -> ListCapabilitiesResponseTypeDef:
        """
        Lists the capabilities associated with your Amazon Web Services account for
        your current or specified region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/list_capabilities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#list_capabilities)
        """

    def list_partnerships(
        self, **kwargs: Unpack[ListPartnershipsRequestTypeDef]
    ) -> ListPartnershipsResponseTypeDef:
        """
        Lists the partnerships associated with your Amazon Web Services account for
        your current or specified region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/list_partnerships.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#list_partnerships)
        """

    def list_profiles(
        self, **kwargs: Unpack[ListProfilesRequestTypeDef]
    ) -> ListProfilesResponseTypeDef:
        """
        Lists the profiles associated with your Amazon Web Services account for your
        current or specified region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/list_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#list_profiles)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all of the tags associated with the Amazon Resource Name (ARN) that you
        specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#list_tags_for_resource)
        """

    def list_transformers(
        self, **kwargs: Unpack[ListTransformersRequestTypeDef]
    ) -> ListTransformersResponseTypeDef:
        """
        Lists the available transformers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/list_transformers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#list_transformers)
        """

    def start_transformer_job(
        self, **kwargs: Unpack[StartTransformerJobRequestTypeDef]
    ) -> StartTransformerJobResponseTypeDef:
        """
        Runs a job, using a transformer, to parse input EDI (electronic data
        interchange) file into the output structures used by Amazon Web Services B2B
        Data Interchange.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/start_transformer_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#start_transformer_job)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Attaches a key-value pair to a resource, as identified by its Amazon Resource
        Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#tag_resource)
        """

    def test_conversion(
        self, **kwargs: Unpack[TestConversionRequestTypeDef]
    ) -> TestConversionResponseTypeDef:
        """
        This operation mimics the latter half of a typical Outbound EDI request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/test_conversion.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#test_conversion)
        """

    def test_mapping(
        self, **kwargs: Unpack[TestMappingRequestTypeDef]
    ) -> TestMappingResponseTypeDef:
        """
        Maps the input file according to the provided template file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/test_mapping.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#test_mapping)
        """

    def test_parsing(
        self, **kwargs: Unpack[TestParsingRequestTypeDef]
    ) -> TestParsingResponseTypeDef:
        """
        Parses the input EDI (electronic data interchange) file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/test_parsing.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#test_parsing)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Detaches a key-value pair from the specified resource, as identified by its
        Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#untag_resource)
        """

    def update_capability(
        self, **kwargs: Unpack[UpdateCapabilityRequestTypeDef]
    ) -> UpdateCapabilityResponseTypeDef:
        """
        Updates some of the parameters for a capability, based on the specified
        parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/update_capability.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#update_capability)
        """

    def update_partnership(
        self, **kwargs: Unpack[UpdatePartnershipRequestTypeDef]
    ) -> UpdatePartnershipResponseTypeDef:
        """
        Updates some of the parameters for a partnership between a customer and trading
        partner.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/update_partnership.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#update_partnership)
        """

    def update_profile(
        self, **kwargs: Unpack[UpdateProfileRequestTypeDef]
    ) -> UpdateProfileResponseTypeDef:
        """
        Updates the specified parameters for a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/update_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#update_profile)
        """

    def update_transformer(
        self, **kwargs: Unpack[UpdateTransformerRequestTypeDef]
    ) -> UpdateTransformerResponseTypeDef:
        """
        Updates the specified parameters for a transformer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/update_transformer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#update_transformer)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_capabilities"]
    ) -> ListCapabilitiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_partnerships"]
    ) -> ListPartnershipsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_profiles"]
    ) -> ListProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_transformers"]
    ) -> ListTransformersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/client/#get_paginator)
        """
