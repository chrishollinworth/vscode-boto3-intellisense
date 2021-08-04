"""
Type annotations for macie service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/type_defs.html)

Usage::

    ```python
    from mypy_boto3_macie.type_defs import AssociateMemberAccountRequestRequestTypeDef

    data: AssociateMemberAccountRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import S3OneTimeClassificationTypeType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AssociateMemberAccountRequestRequestTypeDef",
    "AssociateS3ResourcesRequestRequestTypeDef",
    "AssociateS3ResourcesResultTypeDef",
    "ClassificationTypeTypeDef",
    "ClassificationTypeUpdateTypeDef",
    "DisassociateMemberAccountRequestRequestTypeDef",
    "DisassociateS3ResourcesRequestRequestTypeDef",
    "DisassociateS3ResourcesResultTypeDef",
    "FailedS3ResourceTypeDef",
    "ListMemberAccountsRequestRequestTypeDef",
    "ListMemberAccountsResultTypeDef",
    "ListS3ResourcesRequestRequestTypeDef",
    "ListS3ResourcesResultTypeDef",
    "MemberAccountTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "S3ResourceClassificationTypeDef",
    "S3ResourceClassificationUpdateTypeDef",
    "S3ResourceTypeDef",
    "UpdateS3ResourcesRequestRequestTypeDef",
    "UpdateS3ResourcesResultTypeDef",
)

AssociateMemberAccountRequestRequestTypeDef = TypedDict(
    "AssociateMemberAccountRequestRequestTypeDef",
    {
        "memberAccountId": str,
    },
)

_RequiredAssociateS3ResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateS3ResourcesRequestRequestTypeDef",
    {
        "s3Resources": List["S3ResourceClassificationTypeDef"],
    },
)
_OptionalAssociateS3ResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateS3ResourcesRequestRequestTypeDef",
    {
        "memberAccountId": str,
    },
    total=False,
)

class AssociateS3ResourcesRequestRequestTypeDef(
    _RequiredAssociateS3ResourcesRequestRequestTypeDef,
    _OptionalAssociateS3ResourcesRequestRequestTypeDef,
):
    pass

AssociateS3ResourcesResultTypeDef = TypedDict(
    "AssociateS3ResourcesResultTypeDef",
    {
        "failedS3Resources": List["FailedS3ResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClassificationTypeTypeDef = TypedDict(
    "ClassificationTypeTypeDef",
    {
        "oneTime": S3OneTimeClassificationTypeType,
        "continuous": Literal["FULL"],
    },
)

ClassificationTypeUpdateTypeDef = TypedDict(
    "ClassificationTypeUpdateTypeDef",
    {
        "oneTime": S3OneTimeClassificationTypeType,
        "continuous": Literal["FULL"],
    },
    total=False,
)

DisassociateMemberAccountRequestRequestTypeDef = TypedDict(
    "DisassociateMemberAccountRequestRequestTypeDef",
    {
        "memberAccountId": str,
    },
)

_RequiredDisassociateS3ResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateS3ResourcesRequestRequestTypeDef",
    {
        "associatedS3Resources": List["S3ResourceTypeDef"],
    },
)
_OptionalDisassociateS3ResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateS3ResourcesRequestRequestTypeDef",
    {
        "memberAccountId": str,
    },
    total=False,
)

class DisassociateS3ResourcesRequestRequestTypeDef(
    _RequiredDisassociateS3ResourcesRequestRequestTypeDef,
    _OptionalDisassociateS3ResourcesRequestRequestTypeDef,
):
    pass

DisassociateS3ResourcesResultTypeDef = TypedDict(
    "DisassociateS3ResourcesResultTypeDef",
    {
        "failedS3Resources": List["FailedS3ResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailedS3ResourceTypeDef = TypedDict(
    "FailedS3ResourceTypeDef",
    {
        "failedItem": "S3ResourceTypeDef",
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

ListMemberAccountsRequestRequestTypeDef = TypedDict(
    "ListMemberAccountsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListMemberAccountsResultTypeDef = TypedDict(
    "ListMemberAccountsResultTypeDef",
    {
        "memberAccounts": List["MemberAccountTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListS3ResourcesRequestRequestTypeDef = TypedDict(
    "ListS3ResourcesRequestRequestTypeDef",
    {
        "memberAccountId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListS3ResourcesResultTypeDef = TypedDict(
    "ListS3ResourcesResultTypeDef",
    {
        "s3Resources": List["S3ResourceClassificationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MemberAccountTypeDef = TypedDict(
    "MemberAccountTypeDef",
    {
        "accountId": str,
    },
    total=False,
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

_RequiredS3ResourceClassificationTypeDef = TypedDict(
    "_RequiredS3ResourceClassificationTypeDef",
    {
        "bucketName": str,
        "classificationType": "ClassificationTypeTypeDef",
    },
)
_OptionalS3ResourceClassificationTypeDef = TypedDict(
    "_OptionalS3ResourceClassificationTypeDef",
    {
        "prefix": str,
    },
    total=False,
)

class S3ResourceClassificationTypeDef(
    _RequiredS3ResourceClassificationTypeDef, _OptionalS3ResourceClassificationTypeDef
):
    pass

_RequiredS3ResourceClassificationUpdateTypeDef = TypedDict(
    "_RequiredS3ResourceClassificationUpdateTypeDef",
    {
        "bucketName": str,
        "classificationTypeUpdate": "ClassificationTypeUpdateTypeDef",
    },
)
_OptionalS3ResourceClassificationUpdateTypeDef = TypedDict(
    "_OptionalS3ResourceClassificationUpdateTypeDef",
    {
        "prefix": str,
    },
    total=False,
)

class S3ResourceClassificationUpdateTypeDef(
    _RequiredS3ResourceClassificationUpdateTypeDef, _OptionalS3ResourceClassificationUpdateTypeDef
):
    pass

_RequiredS3ResourceTypeDef = TypedDict(
    "_RequiredS3ResourceTypeDef",
    {
        "bucketName": str,
    },
)
_OptionalS3ResourceTypeDef = TypedDict(
    "_OptionalS3ResourceTypeDef",
    {
        "prefix": str,
    },
    total=False,
)

class S3ResourceTypeDef(_RequiredS3ResourceTypeDef, _OptionalS3ResourceTypeDef):
    pass

_RequiredUpdateS3ResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateS3ResourcesRequestRequestTypeDef",
    {
        "s3ResourcesUpdate": List["S3ResourceClassificationUpdateTypeDef"],
    },
)
_OptionalUpdateS3ResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateS3ResourcesRequestRequestTypeDef",
    {
        "memberAccountId": str,
    },
    total=False,
)

class UpdateS3ResourcesRequestRequestTypeDef(
    _RequiredUpdateS3ResourcesRequestRequestTypeDef, _OptionalUpdateS3ResourcesRequestRequestTypeDef
):
    pass

UpdateS3ResourcesResultTypeDef = TypedDict(
    "UpdateS3ResourcesResultTypeDef",
    {
        "failedS3Resources": List["FailedS3ResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
