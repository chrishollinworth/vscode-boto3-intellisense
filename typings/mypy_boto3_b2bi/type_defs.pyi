"""
Type annotations for b2bi service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_b2bi/type_defs.html)

Usage::

    ```python
    from mypy_boto3_b2bi.type_defs import CapabilityConfigurationTypeDef

    data: CapabilityConfigurationTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    FileFormatType,
    LoggingType,
    TransformerJobStatusType,
    TransformerStatusType,
    X12TransactionSetType,
    X12VersionType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CapabilityConfigurationTypeDef",
    "CapabilitySummaryTypeDef",
    "CreateCapabilityRequestRequestTypeDef",
    "CreateCapabilityResponseTypeDef",
    "CreatePartnershipRequestRequestTypeDef",
    "CreatePartnershipResponseTypeDef",
    "CreateProfileRequestRequestTypeDef",
    "CreateProfileResponseTypeDef",
    "CreateTransformerRequestRequestTypeDef",
    "CreateTransformerResponseTypeDef",
    "DeleteCapabilityRequestRequestTypeDef",
    "DeletePartnershipRequestRequestTypeDef",
    "DeleteProfileRequestRequestTypeDef",
    "DeleteTransformerRequestRequestTypeDef",
    "EdiConfigurationTypeDef",
    "EdiTypeTypeDef",
    "GetCapabilityRequestRequestTypeDef",
    "GetCapabilityResponseTypeDef",
    "GetPartnershipRequestRequestTypeDef",
    "GetPartnershipResponseTypeDef",
    "GetProfileRequestRequestTypeDef",
    "GetProfileResponseTypeDef",
    "GetTransformerJobRequestRequestTypeDef",
    "GetTransformerJobResponseTypeDef",
    "GetTransformerRequestRequestTypeDef",
    "GetTransformerResponseTypeDef",
    "ListCapabilitiesRequestRequestTypeDef",
    "ListCapabilitiesResponseTypeDef",
    "ListPartnershipsRequestRequestTypeDef",
    "ListPartnershipsResponseTypeDef",
    "ListProfilesRequestRequestTypeDef",
    "ListProfilesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTransformersRequestRequestTypeDef",
    "ListTransformersResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PartnershipSummaryTypeDef",
    "ProfileSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "StartTransformerJobRequestRequestTypeDef",
    "StartTransformerJobResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TestMappingRequestRequestTypeDef",
    "TestMappingResponseTypeDef",
    "TestParsingRequestRequestTypeDef",
    "TestParsingResponseTypeDef",
    "TransformerSummaryTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCapabilityRequestRequestTypeDef",
    "UpdateCapabilityResponseTypeDef",
    "UpdatePartnershipRequestRequestTypeDef",
    "UpdatePartnershipResponseTypeDef",
    "UpdateProfileRequestRequestTypeDef",
    "UpdateProfileResponseTypeDef",
    "UpdateTransformerRequestRequestTypeDef",
    "UpdateTransformerResponseTypeDef",
    "X12DetailsTypeDef",
)

CapabilityConfigurationTypeDef = TypedDict(
    "CapabilityConfigurationTypeDef",
    {
        "edi": "EdiConfigurationTypeDef",
    },
    total=False,
)

_RequiredCapabilitySummaryTypeDef = TypedDict(
    "_RequiredCapabilitySummaryTypeDef",
    {
        "capabilityId": str,
        "name": str,
        "type": Literal["edi"],
        "createdAt": datetime,
    },
)
_OptionalCapabilitySummaryTypeDef = TypedDict(
    "_OptionalCapabilitySummaryTypeDef",
    {
        "modifiedAt": datetime,
    },
    total=False,
)

class CapabilitySummaryTypeDef(
    _RequiredCapabilitySummaryTypeDef, _OptionalCapabilitySummaryTypeDef
):
    pass

_RequiredCreateCapabilityRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCapabilityRequestRequestTypeDef",
    {
        "name": str,
        "type": Literal["edi"],
        "configuration": "CapabilityConfigurationTypeDef",
    },
)
_OptionalCreateCapabilityRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCapabilityRequestRequestTypeDef",
    {
        "instructionsDocuments": List["S3LocationTypeDef"],
        "clientToken": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateCapabilityRequestRequestTypeDef(
    _RequiredCreateCapabilityRequestRequestTypeDef, _OptionalCreateCapabilityRequestRequestTypeDef
):
    pass

CreateCapabilityResponseTypeDef = TypedDict(
    "CreateCapabilityResponseTypeDef",
    {
        "capabilityId": str,
        "capabilityArn": str,
        "name": str,
        "type": Literal["edi"],
        "configuration": "CapabilityConfigurationTypeDef",
        "instructionsDocuments": List["S3LocationTypeDef"],
        "createdAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePartnershipRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePartnershipRequestRequestTypeDef",
    {
        "profileId": str,
        "name": str,
        "email": str,
    },
)
_OptionalCreatePartnershipRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePartnershipRequestRequestTypeDef",
    {
        "phone": str,
        "capabilities": List[str],
        "clientToken": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreatePartnershipRequestRequestTypeDef(
    _RequiredCreatePartnershipRequestRequestTypeDef, _OptionalCreatePartnershipRequestRequestTypeDef
):
    pass

CreatePartnershipResponseTypeDef = TypedDict(
    "CreatePartnershipResponseTypeDef",
    {
        "profileId": str,
        "partnershipId": str,
        "partnershipArn": str,
        "name": str,
        "email": str,
        "phone": str,
        "capabilities": List[str],
        "tradingPartnerId": str,
        "createdAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProfileRequestRequestTypeDef",
    {
        "name": str,
        "phone": str,
        "businessName": str,
        "logging": LoggingType,
    },
)
_OptionalCreateProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProfileRequestRequestTypeDef",
    {
        "email": str,
        "clientToken": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateProfileRequestRequestTypeDef(
    _RequiredCreateProfileRequestRequestTypeDef, _OptionalCreateProfileRequestRequestTypeDef
):
    pass

CreateProfileResponseTypeDef = TypedDict(
    "CreateProfileResponseTypeDef",
    {
        "profileId": str,
        "profileArn": str,
        "name": str,
        "businessName": str,
        "phone": str,
        "email": str,
        "logging": LoggingType,
        "logGroupName": str,
        "createdAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTransformerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTransformerRequestRequestTypeDef",
    {
        "name": str,
        "fileFormat": FileFormatType,
        "mappingTemplate": str,
        "ediType": "EdiTypeTypeDef",
    },
)
_OptionalCreateTransformerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTransformerRequestRequestTypeDef",
    {
        "sampleDocument": str,
        "clientToken": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateTransformerRequestRequestTypeDef(
    _RequiredCreateTransformerRequestRequestTypeDef, _OptionalCreateTransformerRequestRequestTypeDef
):
    pass

CreateTransformerResponseTypeDef = TypedDict(
    "CreateTransformerResponseTypeDef",
    {
        "transformerId": str,
        "transformerArn": str,
        "name": str,
        "fileFormat": FileFormatType,
        "mappingTemplate": str,
        "status": TransformerStatusType,
        "ediType": "EdiTypeTypeDef",
        "sampleDocument": str,
        "createdAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCapabilityRequestRequestTypeDef = TypedDict(
    "DeleteCapabilityRequestRequestTypeDef",
    {
        "capabilityId": str,
    },
)

DeletePartnershipRequestRequestTypeDef = TypedDict(
    "DeletePartnershipRequestRequestTypeDef",
    {
        "partnershipId": str,
    },
)

DeleteProfileRequestRequestTypeDef = TypedDict(
    "DeleteProfileRequestRequestTypeDef",
    {
        "profileId": str,
    },
)

DeleteTransformerRequestRequestTypeDef = TypedDict(
    "DeleteTransformerRequestRequestTypeDef",
    {
        "transformerId": str,
    },
)

EdiConfigurationTypeDef = TypedDict(
    "EdiConfigurationTypeDef",
    {
        "type": "EdiTypeTypeDef",
        "inputLocation": "S3LocationTypeDef",
        "outputLocation": "S3LocationTypeDef",
        "transformerId": str,
    },
)

EdiTypeTypeDef = TypedDict(
    "EdiTypeTypeDef",
    {
        "x12Details": "X12DetailsTypeDef",
    },
    total=False,
)

GetCapabilityRequestRequestTypeDef = TypedDict(
    "GetCapabilityRequestRequestTypeDef",
    {
        "capabilityId": str,
    },
)

GetCapabilityResponseTypeDef = TypedDict(
    "GetCapabilityResponseTypeDef",
    {
        "capabilityId": str,
        "capabilityArn": str,
        "name": str,
        "type": Literal["edi"],
        "configuration": "CapabilityConfigurationTypeDef",
        "instructionsDocuments": List["S3LocationTypeDef"],
        "createdAt": datetime,
        "modifiedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPartnershipRequestRequestTypeDef = TypedDict(
    "GetPartnershipRequestRequestTypeDef",
    {
        "partnershipId": str,
    },
)

GetPartnershipResponseTypeDef = TypedDict(
    "GetPartnershipResponseTypeDef",
    {
        "profileId": str,
        "partnershipId": str,
        "partnershipArn": str,
        "name": str,
        "email": str,
        "phone": str,
        "capabilities": List[str],
        "tradingPartnerId": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProfileRequestRequestTypeDef = TypedDict(
    "GetProfileRequestRequestTypeDef",
    {
        "profileId": str,
    },
)

GetProfileResponseTypeDef = TypedDict(
    "GetProfileResponseTypeDef",
    {
        "profileId": str,
        "profileArn": str,
        "name": str,
        "email": str,
        "phone": str,
        "businessName": str,
        "logging": LoggingType,
        "logGroupName": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTransformerJobRequestRequestTypeDef = TypedDict(
    "GetTransformerJobRequestRequestTypeDef",
    {
        "transformerJobId": str,
        "transformerId": str,
    },
)

GetTransformerJobResponseTypeDef = TypedDict(
    "GetTransformerJobResponseTypeDef",
    {
        "status": TransformerJobStatusType,
        "outputFiles": List["S3LocationTypeDef"],
        "message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTransformerRequestRequestTypeDef = TypedDict(
    "GetTransformerRequestRequestTypeDef",
    {
        "transformerId": str,
    },
)

GetTransformerResponseTypeDef = TypedDict(
    "GetTransformerResponseTypeDef",
    {
        "transformerId": str,
        "transformerArn": str,
        "name": str,
        "fileFormat": FileFormatType,
        "mappingTemplate": str,
        "status": TransformerStatusType,
        "ediType": "EdiTypeTypeDef",
        "sampleDocument": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCapabilitiesRequestRequestTypeDef = TypedDict(
    "ListCapabilitiesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListCapabilitiesResponseTypeDef = TypedDict(
    "ListCapabilitiesResponseTypeDef",
    {
        "capabilities": List["CapabilitySummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPartnershipsRequestRequestTypeDef = TypedDict(
    "ListPartnershipsRequestRequestTypeDef",
    {
        "profileId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListPartnershipsResponseTypeDef = TypedDict(
    "ListPartnershipsResponseTypeDef",
    {
        "partnerships": List["PartnershipSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProfilesRequestRequestTypeDef = TypedDict(
    "ListProfilesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListProfilesResponseTypeDef = TypedDict(
    "ListProfilesResponseTypeDef",
    {
        "profiles": List["ProfileSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTransformersRequestRequestTypeDef = TypedDict(
    "ListTransformersRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListTransformersResponseTypeDef = TypedDict(
    "ListTransformersResponseTypeDef",
    {
        "transformers": List["TransformerSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredPartnershipSummaryTypeDef = TypedDict(
    "_RequiredPartnershipSummaryTypeDef",
    {
        "profileId": str,
        "partnershipId": str,
        "createdAt": datetime,
    },
)
_OptionalPartnershipSummaryTypeDef = TypedDict(
    "_OptionalPartnershipSummaryTypeDef",
    {
        "name": str,
        "capabilities": List[str],
        "tradingPartnerId": str,
        "modifiedAt": datetime,
    },
    total=False,
)

class PartnershipSummaryTypeDef(
    _RequiredPartnershipSummaryTypeDef, _OptionalPartnershipSummaryTypeDef
):
    pass

_RequiredProfileSummaryTypeDef = TypedDict(
    "_RequiredProfileSummaryTypeDef",
    {
        "profileId": str,
        "name": str,
        "businessName": str,
        "createdAt": datetime,
    },
)
_OptionalProfileSummaryTypeDef = TypedDict(
    "_OptionalProfileSummaryTypeDef",
    {
        "logging": LoggingType,
        "logGroupName": str,
        "modifiedAt": datetime,
    },
    total=False,
)

class ProfileSummaryTypeDef(_RequiredProfileSummaryTypeDef, _OptionalProfileSummaryTypeDef):
    pass

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucketName": str,
        "key": str,
    },
    total=False,
)

_RequiredStartTransformerJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartTransformerJobRequestRequestTypeDef",
    {
        "inputFile": "S3LocationTypeDef",
        "outputLocation": "S3LocationTypeDef",
        "transformerId": str,
    },
)
_OptionalStartTransformerJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartTransformerJobRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class StartTransformerJobRequestRequestTypeDef(
    _RequiredStartTransformerJobRequestRequestTypeDef,
    _OptionalStartTransformerJobRequestRequestTypeDef,
):
    pass

StartTransformerJobResponseTypeDef = TypedDict(
    "StartTransformerJobResponseTypeDef",
    {
        "transformerJobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TestMappingRequestRequestTypeDef = TypedDict(
    "TestMappingRequestRequestTypeDef",
    {
        "inputFileContent": str,
        "mappingTemplate": str,
        "fileFormat": FileFormatType,
    },
)

TestMappingResponseTypeDef = TypedDict(
    "TestMappingResponseTypeDef",
    {
        "mappedFileContent": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TestParsingRequestRequestTypeDef = TypedDict(
    "TestParsingRequestRequestTypeDef",
    {
        "inputFile": "S3LocationTypeDef",
        "fileFormat": FileFormatType,
        "ediType": "EdiTypeTypeDef",
    },
)

TestParsingResponseTypeDef = TypedDict(
    "TestParsingResponseTypeDef",
    {
        "parsedFileContent": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredTransformerSummaryTypeDef = TypedDict(
    "_RequiredTransformerSummaryTypeDef",
    {
        "transformerId": str,
        "name": str,
        "fileFormat": FileFormatType,
        "mappingTemplate": str,
        "status": TransformerStatusType,
        "ediType": "EdiTypeTypeDef",
        "createdAt": datetime,
    },
)
_OptionalTransformerSummaryTypeDef = TypedDict(
    "_OptionalTransformerSummaryTypeDef",
    {
        "sampleDocument": str,
        "modifiedAt": datetime,
    },
    total=False,
)

class TransformerSummaryTypeDef(
    _RequiredTransformerSummaryTypeDef, _OptionalTransformerSummaryTypeDef
):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateCapabilityRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCapabilityRequestRequestTypeDef",
    {
        "capabilityId": str,
    },
)
_OptionalUpdateCapabilityRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCapabilityRequestRequestTypeDef",
    {
        "name": str,
        "configuration": "CapabilityConfigurationTypeDef",
        "instructionsDocuments": List["S3LocationTypeDef"],
    },
    total=False,
)

class UpdateCapabilityRequestRequestTypeDef(
    _RequiredUpdateCapabilityRequestRequestTypeDef, _OptionalUpdateCapabilityRequestRequestTypeDef
):
    pass

UpdateCapabilityResponseTypeDef = TypedDict(
    "UpdateCapabilityResponseTypeDef",
    {
        "capabilityId": str,
        "capabilityArn": str,
        "name": str,
        "type": Literal["edi"],
        "configuration": "CapabilityConfigurationTypeDef",
        "instructionsDocuments": List["S3LocationTypeDef"],
        "createdAt": datetime,
        "modifiedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePartnershipRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePartnershipRequestRequestTypeDef",
    {
        "partnershipId": str,
    },
)
_OptionalUpdatePartnershipRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePartnershipRequestRequestTypeDef",
    {
        "name": str,
        "capabilities": List[str],
    },
    total=False,
)

class UpdatePartnershipRequestRequestTypeDef(
    _RequiredUpdatePartnershipRequestRequestTypeDef, _OptionalUpdatePartnershipRequestRequestTypeDef
):
    pass

UpdatePartnershipResponseTypeDef = TypedDict(
    "UpdatePartnershipResponseTypeDef",
    {
        "profileId": str,
        "partnershipId": str,
        "partnershipArn": str,
        "name": str,
        "email": str,
        "phone": str,
        "capabilities": List[str],
        "tradingPartnerId": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProfileRequestRequestTypeDef",
    {
        "profileId": str,
    },
)
_OptionalUpdateProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProfileRequestRequestTypeDef",
    {
        "name": str,
        "email": str,
        "phone": str,
        "businessName": str,
    },
    total=False,
)

class UpdateProfileRequestRequestTypeDef(
    _RequiredUpdateProfileRequestRequestTypeDef, _OptionalUpdateProfileRequestRequestTypeDef
):
    pass

UpdateProfileResponseTypeDef = TypedDict(
    "UpdateProfileResponseTypeDef",
    {
        "profileId": str,
        "profileArn": str,
        "name": str,
        "email": str,
        "phone": str,
        "businessName": str,
        "logging": LoggingType,
        "logGroupName": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTransformerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTransformerRequestRequestTypeDef",
    {
        "transformerId": str,
    },
)
_OptionalUpdateTransformerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTransformerRequestRequestTypeDef",
    {
        "name": str,
        "fileFormat": FileFormatType,
        "mappingTemplate": str,
        "status": TransformerStatusType,
        "ediType": "EdiTypeTypeDef",
        "sampleDocument": str,
    },
    total=False,
)

class UpdateTransformerRequestRequestTypeDef(
    _RequiredUpdateTransformerRequestRequestTypeDef, _OptionalUpdateTransformerRequestRequestTypeDef
):
    pass

UpdateTransformerResponseTypeDef = TypedDict(
    "UpdateTransformerResponseTypeDef",
    {
        "transformerId": str,
        "transformerArn": str,
        "name": str,
        "fileFormat": FileFormatType,
        "mappingTemplate": str,
        "status": TransformerStatusType,
        "ediType": "EdiTypeTypeDef",
        "sampleDocument": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

X12DetailsTypeDef = TypedDict(
    "X12DetailsTypeDef",
    {
        "transactionSet": X12TransactionSetType,
        "version": X12VersionType,
    },
    total=False,
)
