"""
Type annotations for amplifyuibuilder service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/type_defs.html)

Usage::

    ```python
    from mypy_boto3_amplifyuibuilder.type_defs import ComponentBindingPropertiesValuePropertiesTypeDef

    data: ComponentBindingPropertiesValuePropertiesTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import SortDirectionType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ComponentBindingPropertiesValuePropertiesTypeDef",
    "ComponentBindingPropertiesValueTypeDef",
    "ComponentChildTypeDef",
    "ComponentConditionPropertyTypeDef",
    "ComponentDataConfigurationTypeDef",
    "ComponentPropertyBindingPropertiesTypeDef",
    "ComponentPropertyTypeDef",
    "ComponentSummaryTypeDef",
    "ComponentTypeDef",
    "ComponentVariantTypeDef",
    "CreateComponentDataTypeDef",
    "CreateComponentRequestRequestTypeDef",
    "CreateComponentResponseTypeDef",
    "CreateThemeDataTypeDef",
    "CreateThemeRequestRequestTypeDef",
    "CreateThemeResponseTypeDef",
    "DeleteComponentRequestRequestTypeDef",
    "DeleteThemeRequestRequestTypeDef",
    "ExchangeCodeForTokenRequestBodyTypeDef",
    "ExchangeCodeForTokenRequestRequestTypeDef",
    "ExchangeCodeForTokenResponseTypeDef",
    "ExportComponentsRequestRequestTypeDef",
    "ExportComponentsResponseTypeDef",
    "ExportThemesRequestRequestTypeDef",
    "ExportThemesResponseTypeDef",
    "FormBindingElementTypeDef",
    "GetComponentRequestRequestTypeDef",
    "GetComponentResponseTypeDef",
    "GetThemeRequestRequestTypeDef",
    "GetThemeResponseTypeDef",
    "ListComponentsRequestRequestTypeDef",
    "ListComponentsResponseTypeDef",
    "ListThemesRequestRequestTypeDef",
    "ListThemesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PredicateTypeDef",
    "RefreshTokenRequestBodyTypeDef",
    "RefreshTokenRequestRequestTypeDef",
    "RefreshTokenResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SortPropertyTypeDef",
    "ThemeSummaryTypeDef",
    "ThemeTypeDef",
    "ThemeValueTypeDef",
    "ThemeValuesTypeDef",
    "UpdateComponentDataTypeDef",
    "UpdateComponentRequestRequestTypeDef",
    "UpdateComponentResponseTypeDef",
    "UpdateThemeDataTypeDef",
    "UpdateThemeRequestRequestTypeDef",
    "UpdateThemeResponseTypeDef",
)

ComponentBindingPropertiesValuePropertiesTypeDef = TypedDict(
    "ComponentBindingPropertiesValuePropertiesTypeDef",
    {
        "bucket": str,
        "defaultValue": str,
        "field": str,
        "key": str,
        "model": str,
        "predicates": List["PredicateTypeDef"],
        "userAttribute": str,
    },
    total=False,
)

ComponentBindingPropertiesValueTypeDef = TypedDict(
    "ComponentBindingPropertiesValueTypeDef",
    {
        "bindingProperties": "ComponentBindingPropertiesValuePropertiesTypeDef",
        "defaultValue": str,
        "type": str,
    },
    total=False,
)

_RequiredComponentChildTypeDef = TypedDict(
    "_RequiredComponentChildTypeDef",
    {
        "componentType": str,
        "name": str,
        "properties": Dict[str, "ComponentPropertyTypeDef"],
    },
)
_OptionalComponentChildTypeDef = TypedDict(
    "_OptionalComponentChildTypeDef",
    {
        "children": List[Dict[str, Any]],
    },
    total=False,
)

class ComponentChildTypeDef(_RequiredComponentChildTypeDef, _OptionalComponentChildTypeDef):
    pass

ComponentConditionPropertyTypeDef = TypedDict(
    "ComponentConditionPropertyTypeDef",
    {
        "else": Dict[str, Any],
        "field": str,
        "operand": str,
        "operator": str,
        "property": str,
        "then": Dict[str, Any],
    },
    total=False,
)

_RequiredComponentDataConfigurationTypeDef = TypedDict(
    "_RequiredComponentDataConfigurationTypeDef",
    {
        "model": str,
    },
)
_OptionalComponentDataConfigurationTypeDef = TypedDict(
    "_OptionalComponentDataConfigurationTypeDef",
    {
        "identifiers": List[str],
        "predicate": "PredicateTypeDef",
        "sort": List["SortPropertyTypeDef"],
    },
    total=False,
)

class ComponentDataConfigurationTypeDef(
    _RequiredComponentDataConfigurationTypeDef, _OptionalComponentDataConfigurationTypeDef
):
    pass

_RequiredComponentPropertyBindingPropertiesTypeDef = TypedDict(
    "_RequiredComponentPropertyBindingPropertiesTypeDef",
    {
        "property": str,
    },
)
_OptionalComponentPropertyBindingPropertiesTypeDef = TypedDict(
    "_OptionalComponentPropertyBindingPropertiesTypeDef",
    {
        "field": str,
    },
    total=False,
)

class ComponentPropertyBindingPropertiesTypeDef(
    _RequiredComponentPropertyBindingPropertiesTypeDef,
    _OptionalComponentPropertyBindingPropertiesTypeDef,
):
    pass

ComponentPropertyTypeDef = TypedDict(
    "ComponentPropertyTypeDef",
    {
        "bindingProperties": "ComponentPropertyBindingPropertiesTypeDef",
        "bindings": Dict[str, "FormBindingElementTypeDef"],
        "collectionBindingProperties": "ComponentPropertyBindingPropertiesTypeDef",
        "concat": List[Dict[str, Any]],
        "condition": Dict[str, Any],
        "configured": bool,
        "defaultValue": str,
        "event": str,
        "importedValue": str,
        "model": str,
        "type": str,
        "userAttribute": str,
        "value": str,
    },
    total=False,
)

ComponentSummaryTypeDef = TypedDict(
    "ComponentSummaryTypeDef",
    {
        "appId": str,
        "componentType": str,
        "environmentName": str,
        "id": str,
        "name": str,
    },
)

_RequiredComponentTypeDef = TypedDict(
    "_RequiredComponentTypeDef",
    {
        "appId": str,
        "bindingProperties": Dict[str, "ComponentBindingPropertiesValueTypeDef"],
        "componentType": str,
        "createdAt": datetime,
        "environmentName": str,
        "id": str,
        "name": str,
        "overrides": Dict[str, Dict[str, str]],
        "properties": Dict[str, "ComponentPropertyTypeDef"],
        "variants": List["ComponentVariantTypeDef"],
    },
)
_OptionalComponentTypeDef = TypedDict(
    "_OptionalComponentTypeDef",
    {
        "children": List["ComponentChildTypeDef"],
        "collectionProperties": Dict[str, "ComponentDataConfigurationTypeDef"],
        "modifiedAt": datetime,
        "sourceId": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class ComponentTypeDef(_RequiredComponentTypeDef, _OptionalComponentTypeDef):
    pass

ComponentVariantTypeDef = TypedDict(
    "ComponentVariantTypeDef",
    {
        "overrides": Dict[str, Dict[str, str]],
        "variantValues": Dict[str, str],
    },
    total=False,
)

_RequiredCreateComponentDataTypeDef = TypedDict(
    "_RequiredCreateComponentDataTypeDef",
    {
        "bindingProperties": Dict[str, "ComponentBindingPropertiesValueTypeDef"],
        "componentType": str,
        "name": str,
        "overrides": Dict[str, Dict[str, str]],
        "properties": Dict[str, "ComponentPropertyTypeDef"],
        "variants": List["ComponentVariantTypeDef"],
    },
)
_OptionalCreateComponentDataTypeDef = TypedDict(
    "_OptionalCreateComponentDataTypeDef",
    {
        "children": List["ComponentChildTypeDef"],
        "collectionProperties": Dict[str, "ComponentDataConfigurationTypeDef"],
        "sourceId": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateComponentDataTypeDef(
    _RequiredCreateComponentDataTypeDef, _OptionalCreateComponentDataTypeDef
):
    pass

_RequiredCreateComponentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateComponentRequestRequestTypeDef",
    {
        "appId": str,
        "componentToCreate": "CreateComponentDataTypeDef",
        "environmentName": str,
    },
)
_OptionalCreateComponentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateComponentRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateComponentRequestRequestTypeDef(
    _RequiredCreateComponentRequestRequestTypeDef, _OptionalCreateComponentRequestRequestTypeDef
):
    pass

CreateComponentResponseTypeDef = TypedDict(
    "CreateComponentResponseTypeDef",
    {
        "entity": "ComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateThemeDataTypeDef = TypedDict(
    "_RequiredCreateThemeDataTypeDef",
    {
        "name": str,
        "values": List["ThemeValuesTypeDef"],
    },
)
_OptionalCreateThemeDataTypeDef = TypedDict(
    "_OptionalCreateThemeDataTypeDef",
    {
        "overrides": List["ThemeValuesTypeDef"],
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateThemeDataTypeDef(_RequiredCreateThemeDataTypeDef, _OptionalCreateThemeDataTypeDef):
    pass

_RequiredCreateThemeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "themeToCreate": "CreateThemeDataTypeDef",
    },
)
_OptionalCreateThemeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateThemeRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateThemeRequestRequestTypeDef(
    _RequiredCreateThemeRequestRequestTypeDef, _OptionalCreateThemeRequestRequestTypeDef
):
    pass

CreateThemeResponseTypeDef = TypedDict(
    "CreateThemeResponseTypeDef",
    {
        "entity": "ThemeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteComponentRequestRequestTypeDef = TypedDict(
    "DeleteComponentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)

DeleteThemeRequestRequestTypeDef = TypedDict(
    "DeleteThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)

ExchangeCodeForTokenRequestBodyTypeDef = TypedDict(
    "ExchangeCodeForTokenRequestBodyTypeDef",
    {
        "code": str,
        "redirectUri": str,
    },
)

ExchangeCodeForTokenRequestRequestTypeDef = TypedDict(
    "ExchangeCodeForTokenRequestRequestTypeDef",
    {
        "provider": Literal["figma"],
        "request": "ExchangeCodeForTokenRequestBodyTypeDef",
    },
)

ExchangeCodeForTokenResponseTypeDef = TypedDict(
    "ExchangeCodeForTokenResponseTypeDef",
    {
        "accessToken": str,
        "expiresIn": int,
        "refreshToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportComponentsRequestRequestTypeDef = TypedDict(
    "ExportComponentsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)

ExportComponentsResponseTypeDef = TypedDict(
    "ExportComponentsResponseTypeDef",
    {
        "entities": List["ComponentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportThemesRequestRequestTypeDef = TypedDict(
    "ExportThemesRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)

ExportThemesResponseTypeDef = TypedDict(
    "ExportThemesResponseTypeDef",
    {
        "entities": List["ThemeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FormBindingElementTypeDef = TypedDict(
    "FormBindingElementTypeDef",
    {
        "element": str,
        "property": str,
    },
)

GetComponentRequestRequestTypeDef = TypedDict(
    "GetComponentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)

GetComponentResponseTypeDef = TypedDict(
    "GetComponentResponseTypeDef",
    {
        "component": "ComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetThemeRequestRequestTypeDef = TypedDict(
    "GetThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)

GetThemeResponseTypeDef = TypedDict(
    "GetThemeResponseTypeDef",
    {
        "theme": "ThemeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListComponentsRequestRequestTypeDef = TypedDict(
    "_RequiredListComponentsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalListComponentsRequestRequestTypeDef = TypedDict(
    "_OptionalListComponentsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListComponentsRequestRequestTypeDef(
    _RequiredListComponentsRequestRequestTypeDef, _OptionalListComponentsRequestRequestTypeDef
):
    pass

ListComponentsResponseTypeDef = TypedDict(
    "ListComponentsResponseTypeDef",
    {
        "entities": List["ComponentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThemesRequestRequestTypeDef = TypedDict(
    "_RequiredListThemesRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalListThemesRequestRequestTypeDef = TypedDict(
    "_OptionalListThemesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListThemesRequestRequestTypeDef(
    _RequiredListThemesRequestRequestTypeDef, _OptionalListThemesRequestRequestTypeDef
):
    pass

ListThemesResponseTypeDef = TypedDict(
    "ListThemesResponseTypeDef",
    {
        "entities": List["ThemeSummaryTypeDef"],
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

PredicateTypeDef = TypedDict(
    "PredicateTypeDef",
    {
        "and": List[Dict[str, Any]],
        "field": str,
        "operand": str,
        "operator": str,
        "or": List[Dict[str, Any]],
    },
    total=False,
)

RefreshTokenRequestBodyTypeDef = TypedDict(
    "RefreshTokenRequestBodyTypeDef",
    {
        "token": str,
    },
)

RefreshTokenRequestRequestTypeDef = TypedDict(
    "RefreshTokenRequestRequestTypeDef",
    {
        "provider": Literal["figma"],
        "refreshTokenBody": "RefreshTokenRequestBodyTypeDef",
    },
)

RefreshTokenResponseTypeDef = TypedDict(
    "RefreshTokenResponseTypeDef",
    {
        "accessToken": str,
        "expiresIn": int,
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

SortPropertyTypeDef = TypedDict(
    "SortPropertyTypeDef",
    {
        "direction": SortDirectionType,
        "field": str,
    },
)

ThemeSummaryTypeDef = TypedDict(
    "ThemeSummaryTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
    },
)

_RequiredThemeTypeDef = TypedDict(
    "_RequiredThemeTypeDef",
    {
        "appId": str,
        "createdAt": datetime,
        "environmentName": str,
        "id": str,
        "name": str,
        "values": List["ThemeValuesTypeDef"],
    },
)
_OptionalThemeTypeDef = TypedDict(
    "_OptionalThemeTypeDef",
    {
        "modifiedAt": datetime,
        "overrides": List["ThemeValuesTypeDef"],
        "tags": Dict[str, str],
    },
    total=False,
)

class ThemeTypeDef(_RequiredThemeTypeDef, _OptionalThemeTypeDef):
    pass

ThemeValueTypeDef = TypedDict(
    "ThemeValueTypeDef",
    {
        "children": List[Dict[str, Any]],
        "value": str,
    },
    total=False,
)

ThemeValuesTypeDef = TypedDict(
    "ThemeValuesTypeDef",
    {
        "key": str,
        "value": Dict[str, Any],
    },
    total=False,
)

UpdateComponentDataTypeDef = TypedDict(
    "UpdateComponentDataTypeDef",
    {
        "bindingProperties": Dict[str, "ComponentBindingPropertiesValueTypeDef"],
        "children": List["ComponentChildTypeDef"],
        "collectionProperties": Dict[str, "ComponentDataConfigurationTypeDef"],
        "componentType": str,
        "id": str,
        "name": str,
        "overrides": Dict[str, Dict[str, str]],
        "properties": Dict[str, "ComponentPropertyTypeDef"],
        "sourceId": str,
        "variants": List["ComponentVariantTypeDef"],
    },
    total=False,
)

_RequiredUpdateComponentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateComponentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "updatedComponent": "UpdateComponentDataTypeDef",
    },
)
_OptionalUpdateComponentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateComponentRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateComponentRequestRequestTypeDef(
    _RequiredUpdateComponentRequestRequestTypeDef, _OptionalUpdateComponentRequestRequestTypeDef
):
    pass

UpdateComponentResponseTypeDef = TypedDict(
    "UpdateComponentResponseTypeDef",
    {
        "entity": "ComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateThemeDataTypeDef = TypedDict(
    "_RequiredUpdateThemeDataTypeDef",
    {
        "values": List["ThemeValuesTypeDef"],
    },
)
_OptionalUpdateThemeDataTypeDef = TypedDict(
    "_OptionalUpdateThemeDataTypeDef",
    {
        "id": str,
        "name": str,
        "overrides": List["ThemeValuesTypeDef"],
    },
    total=False,
)

class UpdateThemeDataTypeDef(_RequiredUpdateThemeDataTypeDef, _OptionalUpdateThemeDataTypeDef):
    pass

_RequiredUpdateThemeRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "updatedTheme": "UpdateThemeDataTypeDef",
    },
)
_OptionalUpdateThemeRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateThemeRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateThemeRequestRequestTypeDef(
    _RequiredUpdateThemeRequestRequestTypeDef, _OptionalUpdateThemeRequestRequestTypeDef
):
    pass

UpdateThemeResponseTypeDef = TypedDict(
    "UpdateThemeResponseTypeDef",
    {
        "entity": "ThemeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
