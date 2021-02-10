"""
Main interface for iotsitewise service type definitions.

Usage::

    ```python
    from mypy_boto3_iotsitewise.type_defs import AccessPolicySummaryTypeDef

    data: AccessPolicySummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccessPolicySummaryTypeDef",
    "AggregatedValueTypeDef",
    "AggregatesTypeDef",
    "AssetCompositeModelTypeDef",
    "AssetErrorDetailsTypeDef",
    "AssetHierarchyInfoTypeDef",
    "AssetHierarchyTypeDef",
    "AssetModelCompositeModelTypeDef",
    "AssetModelHierarchyTypeDef",
    "AssetModelPropertyDefinitionTypeDef",
    "AssetModelPropertyTypeDef",
    "AssetModelStatusTypeDef",
    "AssetModelSummaryTypeDef",
    "AssetPropertyTypeDef",
    "AssetPropertyValueTypeDef",
    "AssetRelationshipSummaryTypeDef",
    "AssetStatusTypeDef",
    "AssetSummaryTypeDef",
    "AssociatedAssetsSummaryTypeDef",
    "AttributeTypeDef",
    "BatchPutAssetPropertyErrorEntryTypeDef",
    "BatchPutAssetPropertyErrorTypeDef",
    "CompositeModelPropertyTypeDef",
    "ConfigurationErrorDetailsTypeDef",
    "ConfigurationStatusTypeDef",
    "DashboardSummaryTypeDef",
    "ErrorDetailsTypeDef",
    "ExpressionVariableTypeDef",
    "GatewayCapabilitySummaryTypeDef",
    "GatewayPlatformTypeDef",
    "GatewaySummaryTypeDef",
    "GreengrassTypeDef",
    "GroupIdentityTypeDef",
    "IAMRoleIdentityTypeDef",
    "IAMUserIdentityTypeDef",
    "IdentityTypeDef",
    "ImageFileTypeDef",
    "ImageLocationTypeDef",
    "LoggingOptionsTypeDef",
    "MetricTypeDef",
    "MetricWindowTypeDef",
    "MonitorErrorDetailsTypeDef",
    "PortalResourceTypeDef",
    "PortalStatusTypeDef",
    "PortalSummaryTypeDef",
    "ProjectResourceTypeDef",
    "ProjectSummaryTypeDef",
    "PropertyNotificationTypeDef",
    "PropertyTypeDef",
    "PropertyTypeTypeDef",
    "ResourceTypeDef",
    "TimeInNanosTypeDef",
    "TransformTypeDef",
    "TumblingWindowTypeDef",
    "UserIdentityTypeDef",
    "VariableValueTypeDef",
    "VariantTypeDef",
    "AssetModelCompositeModelDefinitionTypeDef",
    "AssetModelHierarchyDefinitionTypeDef",
    "BatchAssociateProjectAssetsResponseTypeDef",
    "BatchDisassociateProjectAssetsResponseTypeDef",
    "BatchPutAssetPropertyValueResponseTypeDef",
    "CreateAccessPolicyResponseTypeDef",
    "CreateAssetModelResponseTypeDef",
    "CreateAssetResponseTypeDef",
    "CreateDashboardResponseTypeDef",
    "CreateGatewayResponseTypeDef",
    "CreatePortalResponseTypeDef",
    "CreateProjectResponseTypeDef",
    "DeleteAssetModelResponseTypeDef",
    "DeleteAssetResponseTypeDef",
    "DeletePortalResponseTypeDef",
    "DescribeAccessPolicyResponseTypeDef",
    "DescribeAssetModelResponseTypeDef",
    "DescribeAssetPropertyResponseTypeDef",
    "DescribeAssetResponseTypeDef",
    "DescribeDashboardResponseTypeDef",
    "DescribeDefaultEncryptionConfigurationResponseTypeDef",
    "DescribeGatewayCapabilityConfigurationResponseTypeDef",
    "DescribeGatewayResponseTypeDef",
    "DescribeLoggingOptionsResponseTypeDef",
    "DescribePortalResponseTypeDef",
    "DescribeProjectResponseTypeDef",
    "GetAssetPropertyAggregatesResponseTypeDef",
    "GetAssetPropertyValueHistoryResponseTypeDef",
    "GetAssetPropertyValueResponseTypeDef",
    "ImageTypeDef",
    "ListAccessPoliciesResponseTypeDef",
    "ListAssetModelsResponseTypeDef",
    "ListAssetRelationshipsResponseTypeDef",
    "ListAssetsResponseTypeDef",
    "ListAssociatedAssetsResponseTypeDef",
    "ListDashboardsResponseTypeDef",
    "ListGatewaysResponseTypeDef",
    "ListPortalsResponseTypeDef",
    "ListProjectAssetsResponseTypeDef",
    "ListProjectsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutAssetPropertyValueEntryTypeDef",
    "PutDefaultEncryptionConfigurationResponseTypeDef",
    "UpdateAssetModelResponseTypeDef",
    "UpdateAssetResponseTypeDef",
    "UpdateGatewayCapabilityConfigurationResponseTypeDef",
    "UpdatePortalResponseTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredAccessPolicySummaryTypeDef = TypedDict(
    "_RequiredAccessPolicySummaryTypeDef",
    {
        "id": str,
        "identity": "IdentityTypeDef",
        "resource": "ResourceTypeDef",
        "permission": Literal["ADMINISTRATOR", "VIEWER"],
    },
)
_OptionalAccessPolicySummaryTypeDef = TypedDict(
    "_OptionalAccessPolicySummaryTypeDef",
    {"creationDate": datetime, "lastUpdateDate": datetime},
    total=False,
)


class AccessPolicySummaryTypeDef(
    _RequiredAccessPolicySummaryTypeDef, _OptionalAccessPolicySummaryTypeDef
):
    pass


_RequiredAggregatedValueTypeDef = TypedDict(
    "_RequiredAggregatedValueTypeDef", {"timestamp": datetime, "value": "AggregatesTypeDef"}
)
_OptionalAggregatedValueTypeDef = TypedDict(
    "_OptionalAggregatedValueTypeDef", {"quality": Literal["GOOD", "BAD", "UNCERTAIN"]}, total=False
)


class AggregatedValueTypeDef(_RequiredAggregatedValueTypeDef, _OptionalAggregatedValueTypeDef):
    pass


AggregatesTypeDef = TypedDict(
    "AggregatesTypeDef",
    {
        "average": float,
        "count": float,
        "maximum": float,
        "minimum": float,
        "sum": float,
        "standardDeviation": float,
    },
    total=False,
)

_RequiredAssetCompositeModelTypeDef = TypedDict(
    "_RequiredAssetCompositeModelTypeDef",
    {"name": str, "type": str, "properties": List["AssetPropertyTypeDef"]},
)
_OptionalAssetCompositeModelTypeDef = TypedDict(
    "_OptionalAssetCompositeModelTypeDef", {"description": str}, total=False
)


class AssetCompositeModelTypeDef(
    _RequiredAssetCompositeModelTypeDef, _OptionalAssetCompositeModelTypeDef
):
    pass


AssetErrorDetailsTypeDef = TypedDict(
    "AssetErrorDetailsTypeDef",
    {"assetId": str, "code": Literal["INTERNAL_FAILURE"], "message": str},
)

AssetHierarchyInfoTypeDef = TypedDict(
    "AssetHierarchyInfoTypeDef", {"parentAssetId": str, "childAssetId": str}, total=False
)

_RequiredAssetHierarchyTypeDef = TypedDict("_RequiredAssetHierarchyTypeDef", {"name": str})
_OptionalAssetHierarchyTypeDef = TypedDict(
    "_OptionalAssetHierarchyTypeDef", {"id": str}, total=False
)


class AssetHierarchyTypeDef(_RequiredAssetHierarchyTypeDef, _OptionalAssetHierarchyTypeDef):
    pass


_RequiredAssetModelCompositeModelTypeDef = TypedDict(
    "_RequiredAssetModelCompositeModelTypeDef", {"name": str, "type": str}
)
_OptionalAssetModelCompositeModelTypeDef = TypedDict(
    "_OptionalAssetModelCompositeModelTypeDef",
    {"description": str, "properties": List["AssetModelPropertyTypeDef"]},
    total=False,
)


class AssetModelCompositeModelTypeDef(
    _RequiredAssetModelCompositeModelTypeDef, _OptionalAssetModelCompositeModelTypeDef
):
    pass


_RequiredAssetModelHierarchyTypeDef = TypedDict(
    "_RequiredAssetModelHierarchyTypeDef", {"name": str, "childAssetModelId": str}
)
_OptionalAssetModelHierarchyTypeDef = TypedDict(
    "_OptionalAssetModelHierarchyTypeDef", {"id": str}, total=False
)


class AssetModelHierarchyTypeDef(
    _RequiredAssetModelHierarchyTypeDef, _OptionalAssetModelHierarchyTypeDef
):
    pass


_RequiredAssetModelPropertyDefinitionTypeDef = TypedDict(
    "_RequiredAssetModelPropertyDefinitionTypeDef",
    {
        "name": str,
        "dataType": Literal["STRING", "INTEGER", "DOUBLE", "BOOLEAN", "STRUCT"],
        "type": "PropertyTypeTypeDef",
    },
)
_OptionalAssetModelPropertyDefinitionTypeDef = TypedDict(
    "_OptionalAssetModelPropertyDefinitionTypeDef", {"dataTypeSpec": str, "unit": str}, total=False
)


class AssetModelPropertyDefinitionTypeDef(
    _RequiredAssetModelPropertyDefinitionTypeDef, _OptionalAssetModelPropertyDefinitionTypeDef
):
    pass


_RequiredAssetModelPropertyTypeDef = TypedDict(
    "_RequiredAssetModelPropertyTypeDef",
    {
        "name": str,
        "dataType": Literal["STRING", "INTEGER", "DOUBLE", "BOOLEAN", "STRUCT"],
        "type": "PropertyTypeTypeDef",
    },
)
_OptionalAssetModelPropertyTypeDef = TypedDict(
    "_OptionalAssetModelPropertyTypeDef", {"id": str, "dataTypeSpec": str, "unit": str}, total=False
)


class AssetModelPropertyTypeDef(
    _RequiredAssetModelPropertyTypeDef, _OptionalAssetModelPropertyTypeDef
):
    pass


_RequiredAssetModelStatusTypeDef = TypedDict(
    "_RequiredAssetModelStatusTypeDef",
    {"state": Literal["CREATING", "ACTIVE", "UPDATING", "PROPAGATING", "DELETING", "FAILED"]},
)
_OptionalAssetModelStatusTypeDef = TypedDict(
    "_OptionalAssetModelStatusTypeDef", {"error": "ErrorDetailsTypeDef"}, total=False
)


class AssetModelStatusTypeDef(_RequiredAssetModelStatusTypeDef, _OptionalAssetModelStatusTypeDef):
    pass


AssetModelSummaryTypeDef = TypedDict(
    "AssetModelSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "status": "AssetModelStatusTypeDef",
    },
)

_RequiredAssetPropertyTypeDef = TypedDict(
    "_RequiredAssetPropertyTypeDef",
    {
        "id": str,
        "name": str,
        "dataType": Literal["STRING", "INTEGER", "DOUBLE", "BOOLEAN", "STRUCT"],
    },
)
_OptionalAssetPropertyTypeDef = TypedDict(
    "_OptionalAssetPropertyTypeDef",
    {"alias": str, "notification": "PropertyNotificationTypeDef", "dataTypeSpec": str, "unit": str},
    total=False,
)


class AssetPropertyTypeDef(_RequiredAssetPropertyTypeDef, _OptionalAssetPropertyTypeDef):
    pass


_RequiredAssetPropertyValueTypeDef = TypedDict(
    "_RequiredAssetPropertyValueTypeDef",
    {"value": "VariantTypeDef", "timestamp": "TimeInNanosTypeDef"},
)
_OptionalAssetPropertyValueTypeDef = TypedDict(
    "_OptionalAssetPropertyValueTypeDef",
    {"quality": Literal["GOOD", "BAD", "UNCERTAIN"]},
    total=False,
)


class AssetPropertyValueTypeDef(
    _RequiredAssetPropertyValueTypeDef, _OptionalAssetPropertyValueTypeDef
):
    pass


_RequiredAssetRelationshipSummaryTypeDef = TypedDict(
    "_RequiredAssetRelationshipSummaryTypeDef", {"relationshipType": Literal["HIERARCHY"]}
)
_OptionalAssetRelationshipSummaryTypeDef = TypedDict(
    "_OptionalAssetRelationshipSummaryTypeDef",
    {"hierarchyInfo": "AssetHierarchyInfoTypeDef"},
    total=False,
)


class AssetRelationshipSummaryTypeDef(
    _RequiredAssetRelationshipSummaryTypeDef, _OptionalAssetRelationshipSummaryTypeDef
):
    pass


_RequiredAssetStatusTypeDef = TypedDict(
    "_RequiredAssetStatusTypeDef",
    {"state": Literal["CREATING", "ACTIVE", "UPDATING", "DELETING", "FAILED"]},
)
_OptionalAssetStatusTypeDef = TypedDict(
    "_OptionalAssetStatusTypeDef", {"error": "ErrorDetailsTypeDef"}, total=False
)


class AssetStatusTypeDef(_RequiredAssetStatusTypeDef, _OptionalAssetStatusTypeDef):
    pass


AssetSummaryTypeDef = TypedDict(
    "AssetSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "assetModelId": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "status": "AssetStatusTypeDef",
        "hierarchies": List["AssetHierarchyTypeDef"],
    },
)

AssociatedAssetsSummaryTypeDef = TypedDict(
    "AssociatedAssetsSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "assetModelId": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "status": "AssetStatusTypeDef",
        "hierarchies": List["AssetHierarchyTypeDef"],
    },
)

AttributeTypeDef = TypedDict("AttributeTypeDef", {"defaultValue": str}, total=False)

BatchPutAssetPropertyErrorEntryTypeDef = TypedDict(
    "BatchPutAssetPropertyErrorEntryTypeDef",
    {"entryId": str, "errors": List["BatchPutAssetPropertyErrorTypeDef"]},
)

BatchPutAssetPropertyErrorTypeDef = TypedDict(
    "BatchPutAssetPropertyErrorTypeDef",
    {
        "errorCode": Literal[
            "ResourceNotFoundException",
            "InvalidRequestException",
            "InternalFailureException",
            "ServiceUnavailableException",
            "ThrottlingException",
            "LimitExceededException",
            "ConflictingOperationException",
            "TimestampOutOfRangeException",
            "AccessDeniedException",
        ],
        "errorMessage": str,
        "timestamps": List["TimeInNanosTypeDef"],
    },
)

CompositeModelPropertyTypeDef = TypedDict(
    "CompositeModelPropertyTypeDef", {"name": str, "type": str, "assetProperty": "PropertyTypeDef"}
)

ConfigurationErrorDetailsTypeDef = TypedDict(
    "ConfigurationErrorDetailsTypeDef",
    {"code": Literal["VALIDATION_ERROR", "INTERNAL_FAILURE"], "message": str},
)

_RequiredConfigurationStatusTypeDef = TypedDict(
    "_RequiredConfigurationStatusTypeDef",
    {"state": Literal["ACTIVE", "UPDATE_IN_PROGRESS", "UPDATE_FAILED"]},
)
_OptionalConfigurationStatusTypeDef = TypedDict(
    "_OptionalConfigurationStatusTypeDef",
    {"error": "ConfigurationErrorDetailsTypeDef"},
    total=False,
)


class ConfigurationStatusTypeDef(
    _RequiredConfigurationStatusTypeDef, _OptionalConfigurationStatusTypeDef
):
    pass


_RequiredDashboardSummaryTypeDef = TypedDict(
    "_RequiredDashboardSummaryTypeDef", {"id": str, "name": str}
)
_OptionalDashboardSummaryTypeDef = TypedDict(
    "_OptionalDashboardSummaryTypeDef",
    {"description": str, "creationDate": datetime, "lastUpdateDate": datetime},
    total=False,
)


class DashboardSummaryTypeDef(_RequiredDashboardSummaryTypeDef, _OptionalDashboardSummaryTypeDef):
    pass


ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef", {"code": Literal["VALIDATION_ERROR", "INTERNAL_FAILURE"], "message": str}
)

ExpressionVariableTypeDef = TypedDict(
    "ExpressionVariableTypeDef", {"name": str, "value": "VariableValueTypeDef"}
)

GatewayCapabilitySummaryTypeDef = TypedDict(
    "GatewayCapabilitySummaryTypeDef",
    {
        "capabilityNamespace": str,
        "capabilitySyncStatus": Literal["IN_SYNC", "OUT_OF_SYNC", "SYNC_FAILED"],
    },
)

GatewayPlatformTypeDef = TypedDict("GatewayPlatformTypeDef", {"greengrass": "GreengrassTypeDef"})

_RequiredGatewaySummaryTypeDef = TypedDict(
    "_RequiredGatewaySummaryTypeDef",
    {"gatewayId": str, "gatewayName": str, "creationDate": datetime, "lastUpdateDate": datetime},
)
_OptionalGatewaySummaryTypeDef = TypedDict(
    "_OptionalGatewaySummaryTypeDef",
    {"gatewayCapabilitySummaries": List["GatewayCapabilitySummaryTypeDef"]},
    total=False,
)


class GatewaySummaryTypeDef(_RequiredGatewaySummaryTypeDef, _OptionalGatewaySummaryTypeDef):
    pass


GreengrassTypeDef = TypedDict("GreengrassTypeDef", {"groupArn": str})

GroupIdentityTypeDef = TypedDict("GroupIdentityTypeDef", {"id": str})

IAMRoleIdentityTypeDef = TypedDict("IAMRoleIdentityTypeDef", {"arn": str})

IAMUserIdentityTypeDef = TypedDict("IAMUserIdentityTypeDef", {"arn": str})

IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "user": "UserIdentityTypeDef",
        "group": "GroupIdentityTypeDef",
        "iamUser": "IAMUserIdentityTypeDef",
        "iamRole": "IAMRoleIdentityTypeDef",
    },
    total=False,
)

ImageFileTypeDef = TypedDict(
    "ImageFileTypeDef", {"data": Union[bytes, IO[bytes]], "type": Literal["PNG"]}
)

ImageLocationTypeDef = TypedDict("ImageLocationTypeDef", {"id": str, "url": str})

LoggingOptionsTypeDef = TypedDict(
    "LoggingOptionsTypeDef", {"level": Literal["ERROR", "INFO", "OFF"]}
)

MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {
        "expression": str,
        "variables": List["ExpressionVariableTypeDef"],
        "window": "MetricWindowTypeDef",
    },
)

MetricWindowTypeDef = TypedDict(
    "MetricWindowTypeDef", {"tumbling": "TumblingWindowTypeDef"}, total=False
)

MonitorErrorDetailsTypeDef = TypedDict(
    "MonitorErrorDetailsTypeDef",
    {"code": Literal["INTERNAL_FAILURE", "VALIDATION_ERROR", "LIMIT_EXCEEDED"], "message": str},
    total=False,
)

PortalResourceTypeDef = TypedDict("PortalResourceTypeDef", {"id": str})

_RequiredPortalStatusTypeDef = TypedDict(
    "_RequiredPortalStatusTypeDef",
    {"state": Literal["CREATING", "UPDATING", "DELETING", "ACTIVE", "FAILED"]},
)
_OptionalPortalStatusTypeDef = TypedDict(
    "_OptionalPortalStatusTypeDef", {"error": "MonitorErrorDetailsTypeDef"}, total=False
)


class PortalStatusTypeDef(_RequiredPortalStatusTypeDef, _OptionalPortalStatusTypeDef):
    pass


_RequiredPortalSummaryTypeDef = TypedDict(
    "_RequiredPortalSummaryTypeDef",
    {"id": str, "name": str, "startUrl": str, "status": "PortalStatusTypeDef"},
)
_OptionalPortalSummaryTypeDef = TypedDict(
    "_OptionalPortalSummaryTypeDef",
    {"description": str, "creationDate": datetime, "lastUpdateDate": datetime, "roleArn": str},
    total=False,
)


class PortalSummaryTypeDef(_RequiredPortalSummaryTypeDef, _OptionalPortalSummaryTypeDef):
    pass


ProjectResourceTypeDef = TypedDict("ProjectResourceTypeDef", {"id": str})

_RequiredProjectSummaryTypeDef = TypedDict(
    "_RequiredProjectSummaryTypeDef", {"id": str, "name": str}
)
_OptionalProjectSummaryTypeDef = TypedDict(
    "_OptionalProjectSummaryTypeDef",
    {"description": str, "creationDate": datetime, "lastUpdateDate": datetime},
    total=False,
)


class ProjectSummaryTypeDef(_RequiredProjectSummaryTypeDef, _OptionalProjectSummaryTypeDef):
    pass


PropertyNotificationTypeDef = TypedDict(
    "PropertyNotificationTypeDef", {"topic": str, "state": Literal["ENABLED", "DISABLED"]}
)

_RequiredPropertyTypeDef = TypedDict(
    "_RequiredPropertyTypeDef",
    {
        "id": str,
        "name": str,
        "dataType": Literal["STRING", "INTEGER", "DOUBLE", "BOOLEAN", "STRUCT"],
    },
)
_OptionalPropertyTypeDef = TypedDict(
    "_OptionalPropertyTypeDef",
    {
        "alias": str,
        "notification": "PropertyNotificationTypeDef",
        "unit": str,
        "type": "PropertyTypeTypeDef",
    },
    total=False,
)


class PropertyTypeDef(_RequiredPropertyTypeDef, _OptionalPropertyTypeDef):
    pass


PropertyTypeTypeDef = TypedDict(
    "PropertyTypeTypeDef",
    {
        "attribute": "AttributeTypeDef",
        "measurement": Dict[str, Any],
        "transform": "TransformTypeDef",
        "metric": "MetricTypeDef",
    },
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {"portal": "PortalResourceTypeDef", "project": "ProjectResourceTypeDef"},
    total=False,
)

_RequiredTimeInNanosTypeDef = TypedDict("_RequiredTimeInNanosTypeDef", {"timeInSeconds": int})
_OptionalTimeInNanosTypeDef = TypedDict(
    "_OptionalTimeInNanosTypeDef", {"offsetInNanos": int}, total=False
)


class TimeInNanosTypeDef(_RequiredTimeInNanosTypeDef, _OptionalTimeInNanosTypeDef):
    pass


TransformTypeDef = TypedDict(
    "TransformTypeDef", {"expression": str, "variables": List["ExpressionVariableTypeDef"]}
)

TumblingWindowTypeDef = TypedDict("TumblingWindowTypeDef", {"interval": str})

UserIdentityTypeDef = TypedDict("UserIdentityTypeDef", {"id": str})

_RequiredVariableValueTypeDef = TypedDict("_RequiredVariableValueTypeDef", {"propertyId": str})
_OptionalVariableValueTypeDef = TypedDict(
    "_OptionalVariableValueTypeDef", {"hierarchyId": str}, total=False
)


class VariableValueTypeDef(_RequiredVariableValueTypeDef, _OptionalVariableValueTypeDef):
    pass


VariantTypeDef = TypedDict(
    "VariantTypeDef",
    {"stringValue": str, "integerValue": int, "doubleValue": float, "booleanValue": bool},
    total=False,
)

_RequiredAssetModelCompositeModelDefinitionTypeDef = TypedDict(
    "_RequiredAssetModelCompositeModelDefinitionTypeDef", {"name": str, "type": str}
)
_OptionalAssetModelCompositeModelDefinitionTypeDef = TypedDict(
    "_OptionalAssetModelCompositeModelDefinitionTypeDef",
    {"description": str, "properties": List["AssetModelPropertyDefinitionTypeDef"]},
    total=False,
)


class AssetModelCompositeModelDefinitionTypeDef(
    _RequiredAssetModelCompositeModelDefinitionTypeDef,
    _OptionalAssetModelCompositeModelDefinitionTypeDef,
):
    pass


AssetModelHierarchyDefinitionTypeDef = TypedDict(
    "AssetModelHierarchyDefinitionTypeDef", {"name": str, "childAssetModelId": str}
)

BatchAssociateProjectAssetsResponseTypeDef = TypedDict(
    "BatchAssociateProjectAssetsResponseTypeDef",
    {"errors": List["AssetErrorDetailsTypeDef"]},
    total=False,
)

BatchDisassociateProjectAssetsResponseTypeDef = TypedDict(
    "BatchDisassociateProjectAssetsResponseTypeDef",
    {"errors": List["AssetErrorDetailsTypeDef"]},
    total=False,
)

BatchPutAssetPropertyValueResponseTypeDef = TypedDict(
    "BatchPutAssetPropertyValueResponseTypeDef",
    {"errorEntries": List["BatchPutAssetPropertyErrorEntryTypeDef"]},
)

CreateAccessPolicyResponseTypeDef = TypedDict(
    "CreateAccessPolicyResponseTypeDef", {"accessPolicyId": str, "accessPolicyArn": str}
)

CreateAssetModelResponseTypeDef = TypedDict(
    "CreateAssetModelResponseTypeDef",
    {"assetModelId": str, "assetModelArn": str, "assetModelStatus": "AssetModelStatusTypeDef"},
)

CreateAssetResponseTypeDef = TypedDict(
    "CreateAssetResponseTypeDef",
    {"assetId": str, "assetArn": str, "assetStatus": "AssetStatusTypeDef"},
)

CreateDashboardResponseTypeDef = TypedDict(
    "CreateDashboardResponseTypeDef", {"dashboardId": str, "dashboardArn": str}
)

CreateGatewayResponseTypeDef = TypedDict(
    "CreateGatewayResponseTypeDef", {"gatewayId": str, "gatewayArn": str}
)

CreatePortalResponseTypeDef = TypedDict(
    "CreatePortalResponseTypeDef",
    {
        "portalId": str,
        "portalArn": str,
        "portalStartUrl": str,
        "portalStatus": "PortalStatusTypeDef",
        "ssoApplicationId": str,
    },
)

CreateProjectResponseTypeDef = TypedDict(
    "CreateProjectResponseTypeDef", {"projectId": str, "projectArn": str}
)

DeleteAssetModelResponseTypeDef = TypedDict(
    "DeleteAssetModelResponseTypeDef", {"assetModelStatus": "AssetModelStatusTypeDef"}
)

DeleteAssetResponseTypeDef = TypedDict(
    "DeleteAssetResponseTypeDef", {"assetStatus": "AssetStatusTypeDef"}
)

DeletePortalResponseTypeDef = TypedDict(
    "DeletePortalResponseTypeDef", {"portalStatus": "PortalStatusTypeDef"}
)

DescribeAccessPolicyResponseTypeDef = TypedDict(
    "DescribeAccessPolicyResponseTypeDef",
    {
        "accessPolicyId": str,
        "accessPolicyArn": str,
        "accessPolicyIdentity": "IdentityTypeDef",
        "accessPolicyResource": "ResourceTypeDef",
        "accessPolicyPermission": Literal["ADMINISTRATOR", "VIEWER"],
        "accessPolicyCreationDate": datetime,
        "accessPolicyLastUpdateDate": datetime,
    },
)

_RequiredDescribeAssetModelResponseTypeDef = TypedDict(
    "_RequiredDescribeAssetModelResponseTypeDef",
    {
        "assetModelId": str,
        "assetModelArn": str,
        "assetModelName": str,
        "assetModelDescription": str,
        "assetModelProperties": List["AssetModelPropertyTypeDef"],
        "assetModelHierarchies": List["AssetModelHierarchyTypeDef"],
        "assetModelCreationDate": datetime,
        "assetModelLastUpdateDate": datetime,
        "assetModelStatus": "AssetModelStatusTypeDef",
    },
)
_OptionalDescribeAssetModelResponseTypeDef = TypedDict(
    "_OptionalDescribeAssetModelResponseTypeDef",
    {"assetModelCompositeModels": List["AssetModelCompositeModelTypeDef"]},
    total=False,
)


class DescribeAssetModelResponseTypeDef(
    _RequiredDescribeAssetModelResponseTypeDef, _OptionalDescribeAssetModelResponseTypeDef
):
    pass


_RequiredDescribeAssetPropertyResponseTypeDef = TypedDict(
    "_RequiredDescribeAssetPropertyResponseTypeDef",
    {"assetId": str, "assetName": str, "assetModelId": str},
)
_OptionalDescribeAssetPropertyResponseTypeDef = TypedDict(
    "_OptionalDescribeAssetPropertyResponseTypeDef",
    {"assetProperty": "PropertyTypeDef", "compositeModel": "CompositeModelPropertyTypeDef"},
    total=False,
)


class DescribeAssetPropertyResponseTypeDef(
    _RequiredDescribeAssetPropertyResponseTypeDef, _OptionalDescribeAssetPropertyResponseTypeDef
):
    pass


_RequiredDescribeAssetResponseTypeDef = TypedDict(
    "_RequiredDescribeAssetResponseTypeDef",
    {
        "assetId": str,
        "assetArn": str,
        "assetName": str,
        "assetModelId": str,
        "assetProperties": List["AssetPropertyTypeDef"],
        "assetHierarchies": List["AssetHierarchyTypeDef"],
        "assetCreationDate": datetime,
        "assetLastUpdateDate": datetime,
        "assetStatus": "AssetStatusTypeDef",
    },
)
_OptionalDescribeAssetResponseTypeDef = TypedDict(
    "_OptionalDescribeAssetResponseTypeDef",
    {"assetCompositeModels": List["AssetCompositeModelTypeDef"]},
    total=False,
)


class DescribeAssetResponseTypeDef(
    _RequiredDescribeAssetResponseTypeDef, _OptionalDescribeAssetResponseTypeDef
):
    pass


_RequiredDescribeDashboardResponseTypeDef = TypedDict(
    "_RequiredDescribeDashboardResponseTypeDef",
    {
        "dashboardId": str,
        "dashboardArn": str,
        "dashboardName": str,
        "projectId": str,
        "dashboardDefinition": str,
        "dashboardCreationDate": datetime,
        "dashboardLastUpdateDate": datetime,
    },
)
_OptionalDescribeDashboardResponseTypeDef = TypedDict(
    "_OptionalDescribeDashboardResponseTypeDef", {"dashboardDescription": str}, total=False
)


class DescribeDashboardResponseTypeDef(
    _RequiredDescribeDashboardResponseTypeDef, _OptionalDescribeDashboardResponseTypeDef
):
    pass


_RequiredDescribeDefaultEncryptionConfigurationResponseTypeDef = TypedDict(
    "_RequiredDescribeDefaultEncryptionConfigurationResponseTypeDef",
    {
        "encryptionType": Literal["SITEWISE_DEFAULT_ENCRYPTION", "KMS_BASED_ENCRYPTION"],
        "configurationStatus": "ConfigurationStatusTypeDef",
    },
)
_OptionalDescribeDefaultEncryptionConfigurationResponseTypeDef = TypedDict(
    "_OptionalDescribeDefaultEncryptionConfigurationResponseTypeDef",
    {"kmsKeyArn": str},
    total=False,
)


class DescribeDefaultEncryptionConfigurationResponseTypeDef(
    _RequiredDescribeDefaultEncryptionConfigurationResponseTypeDef,
    _OptionalDescribeDefaultEncryptionConfigurationResponseTypeDef,
):
    pass


DescribeGatewayCapabilityConfigurationResponseTypeDef = TypedDict(
    "DescribeGatewayCapabilityConfigurationResponseTypeDef",
    {
        "gatewayId": str,
        "capabilityNamespace": str,
        "capabilityConfiguration": str,
        "capabilitySyncStatus": Literal["IN_SYNC", "OUT_OF_SYNC", "SYNC_FAILED"],
    },
)

_RequiredDescribeGatewayResponseTypeDef = TypedDict(
    "_RequiredDescribeGatewayResponseTypeDef",
    {
        "gatewayId": str,
        "gatewayName": str,
        "gatewayArn": str,
        "gatewayCapabilitySummaries": List["GatewayCapabilitySummaryTypeDef"],
        "creationDate": datetime,
        "lastUpdateDate": datetime,
    },
)
_OptionalDescribeGatewayResponseTypeDef = TypedDict(
    "_OptionalDescribeGatewayResponseTypeDef",
    {"gatewayPlatform": "GatewayPlatformTypeDef"},
    total=False,
)


class DescribeGatewayResponseTypeDef(
    _RequiredDescribeGatewayResponseTypeDef, _OptionalDescribeGatewayResponseTypeDef
):
    pass


DescribeLoggingOptionsResponseTypeDef = TypedDict(
    "DescribeLoggingOptionsResponseTypeDef", {"loggingOptions": "LoggingOptionsTypeDef"}
)

_RequiredDescribePortalResponseTypeDef = TypedDict(
    "_RequiredDescribePortalResponseTypeDef",
    {
        "portalId": str,
        "portalArn": str,
        "portalName": str,
        "portalClientId": str,
        "portalStartUrl": str,
        "portalContactEmail": str,
        "portalStatus": "PortalStatusTypeDef",
        "portalCreationDate": datetime,
        "portalLastUpdateDate": datetime,
    },
)
_OptionalDescribePortalResponseTypeDef = TypedDict(
    "_OptionalDescribePortalResponseTypeDef",
    {
        "portalDescription": str,
        "portalLogoImageLocation": "ImageLocationTypeDef",
        "roleArn": str,
        "portalAuthMode": Literal["IAM", "SSO"],
    },
    total=False,
)


class DescribePortalResponseTypeDef(
    _RequiredDescribePortalResponseTypeDef, _OptionalDescribePortalResponseTypeDef
):
    pass


_RequiredDescribeProjectResponseTypeDef = TypedDict(
    "_RequiredDescribeProjectResponseTypeDef",
    {
        "projectId": str,
        "projectArn": str,
        "projectName": str,
        "portalId": str,
        "projectCreationDate": datetime,
        "projectLastUpdateDate": datetime,
    },
)
_OptionalDescribeProjectResponseTypeDef = TypedDict(
    "_OptionalDescribeProjectResponseTypeDef", {"projectDescription": str}, total=False
)


class DescribeProjectResponseTypeDef(
    _RequiredDescribeProjectResponseTypeDef, _OptionalDescribeProjectResponseTypeDef
):
    pass


_RequiredGetAssetPropertyAggregatesResponseTypeDef = TypedDict(
    "_RequiredGetAssetPropertyAggregatesResponseTypeDef",
    {"aggregatedValues": List["AggregatedValueTypeDef"]},
)
_OptionalGetAssetPropertyAggregatesResponseTypeDef = TypedDict(
    "_OptionalGetAssetPropertyAggregatesResponseTypeDef", {"nextToken": str}, total=False
)


class GetAssetPropertyAggregatesResponseTypeDef(
    _RequiredGetAssetPropertyAggregatesResponseTypeDef,
    _OptionalGetAssetPropertyAggregatesResponseTypeDef,
):
    pass


_RequiredGetAssetPropertyValueHistoryResponseTypeDef = TypedDict(
    "_RequiredGetAssetPropertyValueHistoryResponseTypeDef",
    {"assetPropertyValueHistory": List["AssetPropertyValueTypeDef"]},
)
_OptionalGetAssetPropertyValueHistoryResponseTypeDef = TypedDict(
    "_OptionalGetAssetPropertyValueHistoryResponseTypeDef", {"nextToken": str}, total=False
)


class GetAssetPropertyValueHistoryResponseTypeDef(
    _RequiredGetAssetPropertyValueHistoryResponseTypeDef,
    _OptionalGetAssetPropertyValueHistoryResponseTypeDef,
):
    pass


GetAssetPropertyValueResponseTypeDef = TypedDict(
    "GetAssetPropertyValueResponseTypeDef",
    {"propertyValue": "AssetPropertyValueTypeDef"},
    total=False,
)

ImageTypeDef = TypedDict("ImageTypeDef", {"id": str, "file": "ImageFileTypeDef"}, total=False)

_RequiredListAccessPoliciesResponseTypeDef = TypedDict(
    "_RequiredListAccessPoliciesResponseTypeDef",
    {"accessPolicySummaries": List["AccessPolicySummaryTypeDef"]},
)
_OptionalListAccessPoliciesResponseTypeDef = TypedDict(
    "_OptionalListAccessPoliciesResponseTypeDef", {"nextToken": str}, total=False
)


class ListAccessPoliciesResponseTypeDef(
    _RequiredListAccessPoliciesResponseTypeDef, _OptionalListAccessPoliciesResponseTypeDef
):
    pass


_RequiredListAssetModelsResponseTypeDef = TypedDict(
    "_RequiredListAssetModelsResponseTypeDef",
    {"assetModelSummaries": List["AssetModelSummaryTypeDef"]},
)
_OptionalListAssetModelsResponseTypeDef = TypedDict(
    "_OptionalListAssetModelsResponseTypeDef", {"nextToken": str}, total=False
)


class ListAssetModelsResponseTypeDef(
    _RequiredListAssetModelsResponseTypeDef, _OptionalListAssetModelsResponseTypeDef
):
    pass


_RequiredListAssetRelationshipsResponseTypeDef = TypedDict(
    "_RequiredListAssetRelationshipsResponseTypeDef",
    {"assetRelationshipSummaries": List["AssetRelationshipSummaryTypeDef"]},
)
_OptionalListAssetRelationshipsResponseTypeDef = TypedDict(
    "_OptionalListAssetRelationshipsResponseTypeDef", {"nextToken": str}, total=False
)


class ListAssetRelationshipsResponseTypeDef(
    _RequiredListAssetRelationshipsResponseTypeDef, _OptionalListAssetRelationshipsResponseTypeDef
):
    pass


_RequiredListAssetsResponseTypeDef = TypedDict(
    "_RequiredListAssetsResponseTypeDef", {"assetSummaries": List["AssetSummaryTypeDef"]}
)
_OptionalListAssetsResponseTypeDef = TypedDict(
    "_OptionalListAssetsResponseTypeDef", {"nextToken": str}, total=False
)


class ListAssetsResponseTypeDef(
    _RequiredListAssetsResponseTypeDef, _OptionalListAssetsResponseTypeDef
):
    pass


_RequiredListAssociatedAssetsResponseTypeDef = TypedDict(
    "_RequiredListAssociatedAssetsResponseTypeDef",
    {"assetSummaries": List["AssociatedAssetsSummaryTypeDef"]},
)
_OptionalListAssociatedAssetsResponseTypeDef = TypedDict(
    "_OptionalListAssociatedAssetsResponseTypeDef", {"nextToken": str}, total=False
)


class ListAssociatedAssetsResponseTypeDef(
    _RequiredListAssociatedAssetsResponseTypeDef, _OptionalListAssociatedAssetsResponseTypeDef
):
    pass


_RequiredListDashboardsResponseTypeDef = TypedDict(
    "_RequiredListDashboardsResponseTypeDef",
    {"dashboardSummaries": List["DashboardSummaryTypeDef"]},
)
_OptionalListDashboardsResponseTypeDef = TypedDict(
    "_OptionalListDashboardsResponseTypeDef", {"nextToken": str}, total=False
)


class ListDashboardsResponseTypeDef(
    _RequiredListDashboardsResponseTypeDef, _OptionalListDashboardsResponseTypeDef
):
    pass


_RequiredListGatewaysResponseTypeDef = TypedDict(
    "_RequiredListGatewaysResponseTypeDef", {"gatewaySummaries": List["GatewaySummaryTypeDef"]}
)
_OptionalListGatewaysResponseTypeDef = TypedDict(
    "_OptionalListGatewaysResponseTypeDef", {"nextToken": str}, total=False
)


class ListGatewaysResponseTypeDef(
    _RequiredListGatewaysResponseTypeDef, _OptionalListGatewaysResponseTypeDef
):
    pass


ListPortalsResponseTypeDef = TypedDict(
    "ListPortalsResponseTypeDef",
    {"portalSummaries": List["PortalSummaryTypeDef"], "nextToken": str},
    total=False,
)

_RequiredListProjectAssetsResponseTypeDef = TypedDict(
    "_RequiredListProjectAssetsResponseTypeDef", {"assetIds": List[str]}
)
_OptionalListProjectAssetsResponseTypeDef = TypedDict(
    "_OptionalListProjectAssetsResponseTypeDef", {"nextToken": str}, total=False
)


class ListProjectAssetsResponseTypeDef(
    _RequiredListProjectAssetsResponseTypeDef, _OptionalListProjectAssetsResponseTypeDef
):
    pass


_RequiredListProjectsResponseTypeDef = TypedDict(
    "_RequiredListProjectsResponseTypeDef", {"projectSummaries": List["ProjectSummaryTypeDef"]}
)
_OptionalListProjectsResponseTypeDef = TypedDict(
    "_OptionalListProjectsResponseTypeDef", {"nextToken": str}, total=False
)


class ListProjectsResponseTypeDef(
    _RequiredListProjectsResponseTypeDef, _OptionalListProjectsResponseTypeDef
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

_RequiredPutAssetPropertyValueEntryTypeDef = TypedDict(
    "_RequiredPutAssetPropertyValueEntryTypeDef",
    {"entryId": str, "propertyValues": List["AssetPropertyValueTypeDef"]},
)
_OptionalPutAssetPropertyValueEntryTypeDef = TypedDict(
    "_OptionalPutAssetPropertyValueEntryTypeDef",
    {"assetId": str, "propertyId": str, "propertyAlias": str},
    total=False,
)


class PutAssetPropertyValueEntryTypeDef(
    _RequiredPutAssetPropertyValueEntryTypeDef, _OptionalPutAssetPropertyValueEntryTypeDef
):
    pass


_RequiredPutDefaultEncryptionConfigurationResponseTypeDef = TypedDict(
    "_RequiredPutDefaultEncryptionConfigurationResponseTypeDef",
    {
        "encryptionType": Literal["SITEWISE_DEFAULT_ENCRYPTION", "KMS_BASED_ENCRYPTION"],
        "configurationStatus": "ConfigurationStatusTypeDef",
    },
)
_OptionalPutDefaultEncryptionConfigurationResponseTypeDef = TypedDict(
    "_OptionalPutDefaultEncryptionConfigurationResponseTypeDef", {"kmsKeyArn": str}, total=False
)


class PutDefaultEncryptionConfigurationResponseTypeDef(
    _RequiredPutDefaultEncryptionConfigurationResponseTypeDef,
    _OptionalPutDefaultEncryptionConfigurationResponseTypeDef,
):
    pass


UpdateAssetModelResponseTypeDef = TypedDict(
    "UpdateAssetModelResponseTypeDef", {"assetModelStatus": "AssetModelStatusTypeDef"}
)

UpdateAssetResponseTypeDef = TypedDict(
    "UpdateAssetResponseTypeDef", {"assetStatus": "AssetStatusTypeDef"}
)

UpdateGatewayCapabilityConfigurationResponseTypeDef = TypedDict(
    "UpdateGatewayCapabilityConfigurationResponseTypeDef",
    {
        "capabilityNamespace": str,
        "capabilitySyncStatus": Literal["IN_SYNC", "OUT_OF_SYNC", "SYNC_FAILED"],
    },
)

UpdatePortalResponseTypeDef = TypedDict(
    "UpdatePortalResponseTypeDef", {"portalStatus": "PortalStatusTypeDef"}
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
