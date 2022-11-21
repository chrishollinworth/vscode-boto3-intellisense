"""
Type annotations for servicecatalog-appregistry service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/type_defs.html)

Usage::

    ```python
    from mypy_boto3_servicecatalog_appregistry.type_defs import AppRegistryConfigurationTypeDef

    data: AppRegistryConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import ResourceGroupStateType, ResourceTypeType, SyncActionType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AppRegistryConfigurationTypeDef",
    "ApplicationSummaryTypeDef",
    "ApplicationTypeDef",
    "AssociateAttributeGroupRequestRequestTypeDef",
    "AssociateAttributeGroupResponseTypeDef",
    "AssociateResourceRequestRequestTypeDef",
    "AssociateResourceResponseTypeDef",
    "AttributeGroupDetailsTypeDef",
    "AttributeGroupSummaryTypeDef",
    "AttributeGroupTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateAttributeGroupRequestRequestTypeDef",
    "CreateAttributeGroupResponseTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteApplicationResponseTypeDef",
    "DeleteAttributeGroupRequestRequestTypeDef",
    "DeleteAttributeGroupResponseTypeDef",
    "DisassociateAttributeGroupRequestRequestTypeDef",
    "DisassociateAttributeGroupResponseTypeDef",
    "DisassociateResourceRequestRequestTypeDef",
    "DisassociateResourceResponseTypeDef",
    "GetApplicationRequestRequestTypeDef",
    "GetApplicationResponseTypeDef",
    "GetAssociatedResourceRequestRequestTypeDef",
    "GetAssociatedResourceResponseTypeDef",
    "GetAttributeGroupRequestRequestTypeDef",
    "GetAttributeGroupResponseTypeDef",
    "GetConfigurationResponseTypeDef",
    "IntegrationsTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListAssociatedAttributeGroupsRequestRequestTypeDef",
    "ListAssociatedAttributeGroupsResponseTypeDef",
    "ListAssociatedResourcesRequestRequestTypeDef",
    "ListAssociatedResourcesResponseTypeDef",
    "ListAttributeGroupsForApplicationRequestRequestTypeDef",
    "ListAttributeGroupsForApplicationResponseTypeDef",
    "ListAttributeGroupsRequestRequestTypeDef",
    "ListAttributeGroupsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutConfigurationRequestRequestTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceGroupTypeDef",
    "ResourceInfoTypeDef",
    "ResourceIntegrationsTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "SyncResourceRequestRequestTypeDef",
    "SyncResourceResponseTypeDef",
    "TagQueryConfigurationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "UpdateApplicationResponseTypeDef",
    "UpdateAttributeGroupRequestRequestTypeDef",
    "UpdateAttributeGroupResponseTypeDef",
)

AppRegistryConfigurationTypeDef = TypedDict(
    "AppRegistryConfigurationTypeDef",
    {
        "tagQueryConfiguration": "TagQueryConfigurationTypeDef",
    },
    total=False,
)

ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

AssociateAttributeGroupRequestRequestTypeDef = TypedDict(
    "AssociateAttributeGroupRequestRequestTypeDef",
    {
        "application": str,
        "attributeGroup": str,
    },
)

AssociateAttributeGroupResponseTypeDef = TypedDict(
    "AssociateAttributeGroupResponseTypeDef",
    {
        "applicationArn": str,
        "attributeGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateResourceRequestRequestTypeDef = TypedDict(
    "AssociateResourceRequestRequestTypeDef",
    {
        "application": str,
        "resourceType": ResourceTypeType,
        "resource": str,
    },
)

AssociateResourceResponseTypeDef = TypedDict(
    "AssociateResourceResponseTypeDef",
    {
        "applicationArn": str,
        "resourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttributeGroupDetailsTypeDef = TypedDict(
    "AttributeGroupDetailsTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
    },
    total=False,
)

AttributeGroupSummaryTypeDef = TypedDict(
    "AttributeGroupSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

AttributeGroupTypeDef = TypedDict(
    "AttributeGroupTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredCreateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestRequestTypeDef",
    {
        "name": str,
        "clientToken": str,
    },
)
_OptionalCreateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateApplicationRequestRequestTypeDef(
    _RequiredCreateApplicationRequestRequestTypeDef, _OptionalCreateApplicationRequestRequestTypeDef
):
    pass

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "application": "ApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAttributeGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAttributeGroupRequestRequestTypeDef",
    {
        "name": str,
        "attributes": str,
        "clientToken": str,
    },
)
_OptionalCreateAttributeGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAttributeGroupRequestRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateAttributeGroupRequestRequestTypeDef(
    _RequiredCreateAttributeGroupRequestRequestTypeDef,
    _OptionalCreateAttributeGroupRequestRequestTypeDef,
):
    pass

CreateAttributeGroupResponseTypeDef = TypedDict(
    "CreateAttributeGroupResponseTypeDef",
    {
        "attributeGroup": "AttributeGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "application": str,
    },
)

DeleteApplicationResponseTypeDef = TypedDict(
    "DeleteApplicationResponseTypeDef",
    {
        "application": "ApplicationSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAttributeGroupRequestRequestTypeDef = TypedDict(
    "DeleteAttributeGroupRequestRequestTypeDef",
    {
        "attributeGroup": str,
    },
)

DeleteAttributeGroupResponseTypeDef = TypedDict(
    "DeleteAttributeGroupResponseTypeDef",
    {
        "attributeGroup": "AttributeGroupSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateAttributeGroupRequestRequestTypeDef = TypedDict(
    "DisassociateAttributeGroupRequestRequestTypeDef",
    {
        "application": str,
        "attributeGroup": str,
    },
)

DisassociateAttributeGroupResponseTypeDef = TypedDict(
    "DisassociateAttributeGroupResponseTypeDef",
    {
        "applicationArn": str,
        "attributeGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateResourceRequestRequestTypeDef = TypedDict(
    "DisassociateResourceRequestRequestTypeDef",
    {
        "application": str,
        "resourceType": ResourceTypeType,
        "resource": str,
    },
)

DisassociateResourceResponseTypeDef = TypedDict(
    "DisassociateResourceResponseTypeDef",
    {
        "applicationArn": str,
        "resourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApplicationRequestRequestTypeDef = TypedDict(
    "GetApplicationRequestRequestTypeDef",
    {
        "application": str,
    },
)

GetApplicationResponseTypeDef = TypedDict(
    "GetApplicationResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "associatedResourceCount": int,
        "tags": Dict[str, str],
        "integrations": "IntegrationsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssociatedResourceRequestRequestTypeDef = TypedDict(
    "GetAssociatedResourceRequestRequestTypeDef",
    {
        "application": str,
        "resourceType": ResourceTypeType,
        "resource": str,
    },
)

GetAssociatedResourceResponseTypeDef = TypedDict(
    "GetAssociatedResourceResponseTypeDef",
    {
        "resource": "ResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAttributeGroupRequestRequestTypeDef = TypedDict(
    "GetAttributeGroupRequestRequestTypeDef",
    {
        "attributeGroup": str,
    },
)

GetAttributeGroupResponseTypeDef = TypedDict(
    "GetAttributeGroupResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "attributes": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConfigurationResponseTypeDef = TypedDict(
    "GetConfigurationResponseTypeDef",
    {
        "configuration": "AppRegistryConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IntegrationsTypeDef = TypedDict(
    "IntegrationsTypeDef",
    {
        "resourceGroup": "ResourceGroupTypeDef",
    },
    total=False,
)

ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "applications": List["ApplicationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAssociatedAttributeGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListAssociatedAttributeGroupsRequestRequestTypeDef",
    {
        "application": str,
    },
)
_OptionalListAssociatedAttributeGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListAssociatedAttributeGroupsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListAssociatedAttributeGroupsRequestRequestTypeDef(
    _RequiredListAssociatedAttributeGroupsRequestRequestTypeDef,
    _OptionalListAssociatedAttributeGroupsRequestRequestTypeDef,
):
    pass

ListAssociatedAttributeGroupsResponseTypeDef = TypedDict(
    "ListAssociatedAttributeGroupsResponseTypeDef",
    {
        "attributeGroups": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAssociatedResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListAssociatedResourcesRequestRequestTypeDef",
    {
        "application": str,
    },
)
_OptionalListAssociatedResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListAssociatedResourcesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListAssociatedResourcesRequestRequestTypeDef(
    _RequiredListAssociatedResourcesRequestRequestTypeDef,
    _OptionalListAssociatedResourcesRequestRequestTypeDef,
):
    pass

ListAssociatedResourcesResponseTypeDef = TypedDict(
    "ListAssociatedResourcesResponseTypeDef",
    {
        "resources": List["ResourceInfoTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAttributeGroupsForApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredListAttributeGroupsForApplicationRequestRequestTypeDef",
    {
        "application": str,
    },
)
_OptionalListAttributeGroupsForApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalListAttributeGroupsForApplicationRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListAttributeGroupsForApplicationRequestRequestTypeDef(
    _RequiredListAttributeGroupsForApplicationRequestRequestTypeDef,
    _OptionalListAttributeGroupsForApplicationRequestRequestTypeDef,
):
    pass

ListAttributeGroupsForApplicationResponseTypeDef = TypedDict(
    "ListAttributeGroupsForApplicationResponseTypeDef",
    {
        "attributeGroupsDetails": List["AttributeGroupDetailsTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAttributeGroupsRequestRequestTypeDef = TypedDict(
    "ListAttributeGroupsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListAttributeGroupsResponseTypeDef = TypedDict(
    "ListAttributeGroupsResponseTypeDef",
    {
        "attributeGroups": List["AttributeGroupSummaryTypeDef"],
        "nextToken": str,
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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PutConfigurationRequestRequestTypeDef = TypedDict(
    "PutConfigurationRequestRequestTypeDef",
    {
        "configuration": "AppRegistryConfigurationTypeDef",
    },
)

ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "tagValue": str,
    },
    total=False,
)

ResourceGroupTypeDef = TypedDict(
    "ResourceGroupTypeDef",
    {
        "state": ResourceGroupStateType,
        "arn": str,
        "errorMessage": str,
    },
    total=False,
)

ResourceInfoTypeDef = TypedDict(
    "ResourceInfoTypeDef",
    {
        "name": str,
        "arn": str,
        "resourceType": ResourceTypeType,
        "resourceDetails": "ResourceDetailsTypeDef",
    },
    total=False,
)

ResourceIntegrationsTypeDef = TypedDict(
    "ResourceIntegrationsTypeDef",
    {
        "resourceGroup": "ResourceGroupTypeDef",
    },
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "name": str,
        "arn": str,
        "associationTime": datetime,
        "integrations": "ResourceIntegrationsTypeDef",
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

SyncResourceRequestRequestTypeDef = TypedDict(
    "SyncResourceRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resource": str,
    },
)

SyncResourceResponseTypeDef = TypedDict(
    "SyncResourceResponseTypeDef",
    {
        "applicationArn": str,
        "resourceArn": str,
        "actionTaken": SyncActionType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagQueryConfigurationTypeDef = TypedDict(
    "TagQueryConfigurationTypeDef",
    {
        "tagKey": str,
    },
    total=False,
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

_RequiredUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationRequestRequestTypeDef",
    {
        "application": str,
    },
)
_OptionalUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationRequestRequestTypeDef",
    {
        "name": str,
        "description": str,
    },
    total=False,
)

class UpdateApplicationRequestRequestTypeDef(
    _RequiredUpdateApplicationRequestRequestTypeDef, _OptionalUpdateApplicationRequestRequestTypeDef
):
    pass

UpdateApplicationResponseTypeDef = TypedDict(
    "UpdateApplicationResponseTypeDef",
    {
        "application": "ApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAttributeGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAttributeGroupRequestRequestTypeDef",
    {
        "attributeGroup": str,
    },
)
_OptionalUpdateAttributeGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAttributeGroupRequestRequestTypeDef",
    {
        "name": str,
        "description": str,
        "attributes": str,
    },
    total=False,
)

class UpdateAttributeGroupRequestRequestTypeDef(
    _RequiredUpdateAttributeGroupRequestRequestTypeDef,
    _OptionalUpdateAttributeGroupRequestRequestTypeDef,
):
    pass

UpdateAttributeGroupResponseTypeDef = TypedDict(
    "UpdateAttributeGroupResponseTypeDef",
    {
        "attributeGroup": "AttributeGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
