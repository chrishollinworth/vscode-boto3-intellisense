"""
Type annotations for appintegrations service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appintegrations/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appintegrations.type_defs import CreateEventIntegrationRequestRequestTypeDef

    data: CreateEventIntegrationRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateEventIntegrationRequestRequestTypeDef",
    "CreateEventIntegrationResponseTypeDef",
    "DeleteEventIntegrationRequestRequestTypeDef",
    "EventFilterTypeDef",
    "EventIntegrationAssociationTypeDef",
    "EventIntegrationTypeDef",
    "GetEventIntegrationRequestRequestTypeDef",
    "GetEventIntegrationResponseTypeDef",
    "ListEventIntegrationAssociationsRequestRequestTypeDef",
    "ListEventIntegrationAssociationsResponseTypeDef",
    "ListEventIntegrationsRequestRequestTypeDef",
    "ListEventIntegrationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateEventIntegrationRequestRequestTypeDef",
)

_RequiredCreateEventIntegrationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
        "EventFilter": "EventFilterTypeDef",
        "EventBridgeBus": str,
    },
)
_OptionalCreateEventIntegrationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEventIntegrationRequestRequestTypeDef",
    {
        "Description": str,
        "ClientToken": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateEventIntegrationRequestRequestTypeDef(
    _RequiredCreateEventIntegrationRequestRequestTypeDef,
    _OptionalCreateEventIntegrationRequestRequestTypeDef,
):
    pass

CreateEventIntegrationResponseTypeDef = TypedDict(
    "CreateEventIntegrationResponseTypeDef",
    {
        "EventIntegrationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEventIntegrationRequestRequestTypeDef = TypedDict(
    "DeleteEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

EventFilterTypeDef = TypedDict(
    "EventFilterTypeDef",
    {
        "Source": str,
    },
)

EventIntegrationAssociationTypeDef = TypedDict(
    "EventIntegrationAssociationTypeDef",
    {
        "EventIntegrationAssociationArn": str,
        "EventIntegrationAssociationId": str,
        "EventIntegrationName": str,
        "ClientId": str,
        "EventBridgeRuleName": str,
        "ClientAssociationMetadata": Dict[str, str],
    },
    total=False,
)

EventIntegrationTypeDef = TypedDict(
    "EventIntegrationTypeDef",
    {
        "EventIntegrationArn": str,
        "Name": str,
        "Description": str,
        "EventFilter": "EventFilterTypeDef",
        "EventBridgeBus": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

GetEventIntegrationRequestRequestTypeDef = TypedDict(
    "GetEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetEventIntegrationResponseTypeDef = TypedDict(
    "GetEventIntegrationResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "EventIntegrationArn": str,
        "EventBridgeBus": str,
        "EventFilter": "EventFilterTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEventIntegrationAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredListEventIntegrationAssociationsRequestRequestTypeDef",
    {
        "EventIntegrationName": str,
    },
)
_OptionalListEventIntegrationAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalListEventIntegrationAssociationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListEventIntegrationAssociationsRequestRequestTypeDef(
    _RequiredListEventIntegrationAssociationsRequestRequestTypeDef,
    _OptionalListEventIntegrationAssociationsRequestRequestTypeDef,
):
    pass

ListEventIntegrationAssociationsResponseTypeDef = TypedDict(
    "ListEventIntegrationAssociationsResponseTypeDef",
    {
        "EventIntegrationAssociations": List["EventIntegrationAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventIntegrationsRequestRequestTypeDef = TypedDict(
    "ListEventIntegrationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEventIntegrationsResponseTypeDef = TypedDict(
    "ListEventIntegrationsResponseTypeDef",
    {
        "EventIntegrations": List["EventIntegrationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateEventIntegrationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateEventIntegrationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEventIntegrationRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateEventIntegrationRequestRequestTypeDef(
    _RequiredUpdateEventIntegrationRequestRequestTypeDef,
    _OptionalUpdateEventIntegrationRequestRequestTypeDef,
):
    pass
