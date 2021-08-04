"""
Type annotations for schemas service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/literals.html)

Usage::

    ```python
    from mypy_boto3_schemas.literals import CodeBindingExistsWaiterName

    data: CodeBindingExistsWaiterName = "code_binding_exists"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CodeBindingExistsWaiterName",
    "CodeGenerationStatusType",
    "DiscovererStateType",
    "ListDiscoverersPaginatorName",
    "ListRegistriesPaginatorName",
    "ListSchemaVersionsPaginatorName",
    "ListSchemasPaginatorName",
    "SearchSchemasPaginatorName",
    "TypeType",
)

CodeBindingExistsWaiterName = Literal["code_binding_exists"]
CodeGenerationStatusType = Literal["CREATE_COMPLETE", "CREATE_FAILED", "CREATE_IN_PROGRESS"]
DiscovererStateType = Literal["STARTED", "STOPPED"]
ListDiscoverersPaginatorName = Literal["list_discoverers"]
ListRegistriesPaginatorName = Literal["list_registries"]
ListSchemaVersionsPaginatorName = Literal["list_schema_versions"]
ListSchemasPaginatorName = Literal["list_schemas"]
SearchSchemasPaginatorName = Literal["search_schemas"]
TypeType = Literal["JSONSchemaDraft4", "OpenApi3"]
