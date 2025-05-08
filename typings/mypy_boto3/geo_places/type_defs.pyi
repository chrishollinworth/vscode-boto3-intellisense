"""
Type annotations for geo-places service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_geo_places/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_geo_places.type_defs import AccessPointTypeDef

    data: AccessPointTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

from .literals import (
    AutocompleteFilterPlaceTypeType,
    GeocodeAdditionalFeatureType,
    GeocodeFilterPlaceTypeType,
    GeocodeIntendedUseType,
    GetPlaceAdditionalFeatureType,
    GetPlaceIntendedUseType,
    PlaceTypeType,
    PostalCodeModeType,
    PostalCodeTypeType,
    QueryTypeType,
    RecordTypeCodeType,
    ReverseGeocodeAdditionalFeatureType,
    ReverseGeocodeFilterPlaceTypeType,
    ReverseGeocodeIntendedUseType,
    SearchNearbyAdditionalFeatureType,
    SearchNearbyIntendedUseType,
    SearchTextAdditionalFeatureType,
    SearchTextIntendedUseType,
    SuggestAdditionalFeatureType,
    SuggestResultItemTypeType,
    TypePlacementType,
    ZipClassificationCodeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccessPointTypeDef",
    "AccessRestrictionTypeDef",
    "AddressComponentMatchScoresTypeDef",
    "AddressComponentPhonemesTypeDef",
    "AddressTypeDef",
    "AutocompleteAddressHighlightsTypeDef",
    "AutocompleteFilterTypeDef",
    "AutocompleteHighlightsTypeDef",
    "AutocompleteRequestTypeDef",
    "AutocompleteResponseTypeDef",
    "AutocompleteResultItemTypeDef",
    "BusinessChainTypeDef",
    "CategoryTypeDef",
    "ComponentMatchScoresTypeDef",
    "ContactDetailsTypeDef",
    "ContactsTypeDef",
    "CountryHighlightsTypeDef",
    "CountryTypeDef",
    "FilterCircleTypeDef",
    "FoodTypeTypeDef",
    "GeocodeFilterTypeDef",
    "GeocodeQueryComponentsTypeDef",
    "GeocodeRequestTypeDef",
    "GeocodeResponseTypeDef",
    "GeocodeResultItemTypeDef",
    "GetPlaceRequestTypeDef",
    "GetPlaceResponseTypeDef",
    "HighlightTypeDef",
    "MatchScoreDetailsTypeDef",
    "OpeningHoursComponentsTypeDef",
    "OpeningHoursTypeDef",
    "PhonemeDetailsTypeDef",
    "PhonemeTranscriptionTypeDef",
    "PostalCodeDetailsTypeDef",
    "QueryRefinementTypeDef",
    "RegionHighlightsTypeDef",
    "RegionTypeDef",
    "ResponseMetadataTypeDef",
    "ReverseGeocodeFilterTypeDef",
    "ReverseGeocodeRequestTypeDef",
    "ReverseGeocodeResponseTypeDef",
    "ReverseGeocodeResultItemTypeDef",
    "SearchNearbyFilterTypeDef",
    "SearchNearbyRequestTypeDef",
    "SearchNearbyResponseTypeDef",
    "SearchNearbyResultItemTypeDef",
    "SearchTextFilterTypeDef",
    "SearchTextRequestTypeDef",
    "SearchTextResponseTypeDef",
    "SearchTextResultItemTypeDef",
    "StreetComponentsTypeDef",
    "SubRegionHighlightsTypeDef",
    "SubRegionTypeDef",
    "SuggestAddressHighlightsTypeDef",
    "SuggestFilterTypeDef",
    "SuggestHighlightsTypeDef",
    "SuggestPlaceResultTypeDef",
    "SuggestQueryResultTypeDef",
    "SuggestRequestTypeDef",
    "SuggestResponseTypeDef",
    "SuggestResultItemTypeDef",
    "TimeZoneTypeDef",
    "UspsZipPlus4TypeDef",
    "UspsZipTypeDef",
)

class AccessPointTypeDef(TypedDict):
    Position: NotRequired[List[float]]

class CategoryTypeDef(TypedDict):
    Id: str
    Name: str
    LocalizedName: NotRequired[str]
    Primary: NotRequired[bool]

class AddressComponentMatchScoresTypeDef(TypedDict):
    Country: NotRequired[float]
    Region: NotRequired[float]
    SubRegion: NotRequired[float]
    Locality: NotRequired[float]
    District: NotRequired[float]
    SubDistrict: NotRequired[float]
    PostalCode: NotRequired[float]
    Block: NotRequired[float]
    SubBlock: NotRequired[float]
    Intersection: NotRequired[List[float]]
    AddressNumber: NotRequired[float]
    Building: NotRequired[float]

class PhonemeTranscriptionTypeDef(TypedDict):
    Value: NotRequired[str]
    Language: NotRequired[str]
    Preferred: NotRequired[bool]

class CountryTypeDef(TypedDict):
    Code2: NotRequired[str]
    Code3: NotRequired[str]
    Name: NotRequired[str]

class RegionTypeDef(TypedDict):
    Code: NotRequired[str]
    Name: NotRequired[str]

StreetComponentsTypeDef = TypedDict(
    "StreetComponentsTypeDef",
    {
        "BaseName": NotRequired[str],
        "Type": NotRequired[str],
        "TypePlacement": NotRequired[TypePlacementType],
        "TypeSeparator": NotRequired[str],
        "Prefix": NotRequired[str],
        "Suffix": NotRequired[str],
        "Direction": NotRequired[str],
        "Language": NotRequired[str],
    },
)

class SubRegionTypeDef(TypedDict):
    Code: NotRequired[str]
    Name: NotRequired[str]

class HighlightTypeDef(TypedDict):
    StartIndex: NotRequired[int]
    EndIndex: NotRequired[int]
    Value: NotRequired[str]

class FilterCircleTypeDef(TypedDict):
    Center: Sequence[float]
    Radius: int

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class BusinessChainTypeDef(TypedDict):
    Name: NotRequired[str]
    Id: NotRequired[str]

class FoodTypeTypeDef(TypedDict):
    LocalizedName: str
    Id: NotRequired[str]
    Primary: NotRequired[bool]

class GeocodeFilterTypeDef(TypedDict):
    IncludeCountries: NotRequired[Sequence[str]]
    IncludePlaceTypes: NotRequired[Sequence[GeocodeFilterPlaceTypeType]]

class GeocodeQueryComponentsTypeDef(TypedDict):
    Country: NotRequired[str]
    Region: NotRequired[str]
    SubRegion: NotRequired[str]
    Locality: NotRequired[str]
    District: NotRequired[str]
    Street: NotRequired[str]
    AddressNumber: NotRequired[str]
    PostalCode: NotRequired[str]

class TimeZoneTypeDef(TypedDict):
    Name: str
    Offset: NotRequired[str]
    OffsetSeconds: NotRequired[int]

class GetPlaceRequestTypeDef(TypedDict):
    PlaceId: str
    AdditionalFeatures: NotRequired[Sequence[GetPlaceAdditionalFeatureType]]
    Language: NotRequired[str]
    PoliticalView: NotRequired[str]
    IntendedUse: NotRequired[GetPlaceIntendedUseType]
    Key: NotRequired[str]

class OpeningHoursComponentsTypeDef(TypedDict):
    OpenTime: NotRequired[str]
    OpenDuration: NotRequired[str]
    Recurrence: NotRequired[str]

class UspsZipPlus4TypeDef(TypedDict):
    RecordTypeCode: NotRequired[RecordTypeCodeType]

class UspsZipTypeDef(TypedDict):
    ZipClassificationCode: NotRequired[ZipClassificationCodeType]

class QueryRefinementTypeDef(TypedDict):
    RefinedTerm: str
    OriginalTerm: str
    StartIndex: int
    EndIndex: int

class ReverseGeocodeFilterTypeDef(TypedDict):
    IncludePlaceTypes: NotRequired[Sequence[ReverseGeocodeFilterPlaceTypeType]]

class SearchNearbyFilterTypeDef(TypedDict):
    BoundingBox: NotRequired[Sequence[float]]
    IncludeCountries: NotRequired[Sequence[str]]
    IncludeCategories: NotRequired[Sequence[str]]
    ExcludeCategories: NotRequired[Sequence[str]]
    IncludeBusinessChains: NotRequired[Sequence[str]]
    ExcludeBusinessChains: NotRequired[Sequence[str]]
    IncludeFoodTypes: NotRequired[Sequence[str]]
    ExcludeFoodTypes: NotRequired[Sequence[str]]

class SuggestQueryResultTypeDef(TypedDict):
    QueryId: NotRequired[str]
    QueryType: NotRequired[QueryTypeType]

class AccessRestrictionTypeDef(TypedDict):
    Restricted: NotRequired[bool]
    Categories: NotRequired[List[CategoryTypeDef]]

class ContactDetailsTypeDef(TypedDict):
    Label: NotRequired[str]
    Value: NotRequired[str]
    Categories: NotRequired[List[CategoryTypeDef]]

class ComponentMatchScoresTypeDef(TypedDict):
    Title: NotRequired[float]
    Address: NotRequired[AddressComponentMatchScoresTypeDef]

class AddressComponentPhonemesTypeDef(TypedDict):
    Country: NotRequired[List[PhonemeTranscriptionTypeDef]]
    Region: NotRequired[List[PhonemeTranscriptionTypeDef]]
    SubRegion: NotRequired[List[PhonemeTranscriptionTypeDef]]
    Locality: NotRequired[List[PhonemeTranscriptionTypeDef]]
    District: NotRequired[List[PhonemeTranscriptionTypeDef]]
    SubDistrict: NotRequired[List[PhonemeTranscriptionTypeDef]]
    Block: NotRequired[List[PhonemeTranscriptionTypeDef]]
    SubBlock: NotRequired[List[PhonemeTranscriptionTypeDef]]
    Street: NotRequired[List[PhonemeTranscriptionTypeDef]]

class AddressTypeDef(TypedDict):
    Label: NotRequired[str]
    Country: NotRequired[CountryTypeDef]
    Region: NotRequired[RegionTypeDef]
    SubRegion: NotRequired[SubRegionTypeDef]
    Locality: NotRequired[str]
    District: NotRequired[str]
    SubDistrict: NotRequired[str]
    PostalCode: NotRequired[str]
    Block: NotRequired[str]
    SubBlock: NotRequired[str]
    Intersection: NotRequired[List[str]]
    Street: NotRequired[str]
    StreetComponents: NotRequired[List[StreetComponentsTypeDef]]
    AddressNumber: NotRequired[str]
    Building: NotRequired[str]

class CountryHighlightsTypeDef(TypedDict):
    Code: NotRequired[List[HighlightTypeDef]]
    Name: NotRequired[List[HighlightTypeDef]]

class RegionHighlightsTypeDef(TypedDict):
    Code: NotRequired[List[HighlightTypeDef]]
    Name: NotRequired[List[HighlightTypeDef]]

class SubRegionHighlightsTypeDef(TypedDict):
    Code: NotRequired[List[HighlightTypeDef]]
    Name: NotRequired[List[HighlightTypeDef]]

class SuggestAddressHighlightsTypeDef(TypedDict):
    Label: NotRequired[List[HighlightTypeDef]]

class AutocompleteFilterTypeDef(TypedDict):
    BoundingBox: NotRequired[Sequence[float]]
    Circle: NotRequired[FilterCircleTypeDef]
    IncludeCountries: NotRequired[Sequence[str]]
    IncludePlaceTypes: NotRequired[Sequence[AutocompleteFilterPlaceTypeType]]

class SearchTextFilterTypeDef(TypedDict):
    BoundingBox: NotRequired[Sequence[float]]
    Circle: NotRequired[FilterCircleTypeDef]
    IncludeCountries: NotRequired[Sequence[str]]

class SuggestFilterTypeDef(TypedDict):
    BoundingBox: NotRequired[Sequence[float]]
    Circle: NotRequired[FilterCircleTypeDef]
    IncludeCountries: NotRequired[Sequence[str]]

class GeocodeRequestTypeDef(TypedDict):
    QueryText: NotRequired[str]
    QueryComponents: NotRequired[GeocodeQueryComponentsTypeDef]
    MaxResults: NotRequired[int]
    BiasPosition: NotRequired[Sequence[float]]
    Filter: NotRequired[GeocodeFilterTypeDef]
    AdditionalFeatures: NotRequired[Sequence[GeocodeAdditionalFeatureType]]
    Language: NotRequired[str]
    PoliticalView: NotRequired[str]
    IntendedUse: NotRequired[GeocodeIntendedUseType]
    Key: NotRequired[str]

class OpeningHoursTypeDef(TypedDict):
    Display: NotRequired[List[str]]
    OpenNow: NotRequired[bool]
    Components: NotRequired[List[OpeningHoursComponentsTypeDef]]
    Categories: NotRequired[List[CategoryTypeDef]]

class PostalCodeDetailsTypeDef(TypedDict):
    PostalCode: NotRequired[str]
    PostalAuthority: NotRequired[Literal["Usps"]]
    PostalCodeType: NotRequired[PostalCodeTypeType]
    UspsZip: NotRequired[UspsZipTypeDef]
    UspsZipPlus4: NotRequired[UspsZipPlus4TypeDef]

class ReverseGeocodeRequestTypeDef(TypedDict):
    QueryPosition: Sequence[float]
    QueryRadius: NotRequired[int]
    MaxResults: NotRequired[int]
    Filter: NotRequired[ReverseGeocodeFilterTypeDef]
    AdditionalFeatures: NotRequired[Sequence[ReverseGeocodeAdditionalFeatureType]]
    Language: NotRequired[str]
    PoliticalView: NotRequired[str]
    IntendedUse: NotRequired[ReverseGeocodeIntendedUseType]
    Key: NotRequired[str]

class SearchNearbyRequestTypeDef(TypedDict):
    QueryPosition: Sequence[float]
    QueryRadius: NotRequired[int]
    MaxResults: NotRequired[int]
    Filter: NotRequired[SearchNearbyFilterTypeDef]
    AdditionalFeatures: NotRequired[Sequence[SearchNearbyAdditionalFeatureType]]
    Language: NotRequired[str]
    PoliticalView: NotRequired[str]
    IntendedUse: NotRequired[SearchNearbyIntendedUseType]
    NextToken: NotRequired[str]
    Key: NotRequired[str]

class ContactsTypeDef(TypedDict):
    Phones: NotRequired[List[ContactDetailsTypeDef]]
    Faxes: NotRequired[List[ContactDetailsTypeDef]]
    Websites: NotRequired[List[ContactDetailsTypeDef]]
    Emails: NotRequired[List[ContactDetailsTypeDef]]

class MatchScoreDetailsTypeDef(TypedDict):
    Overall: NotRequired[float]
    Components: NotRequired[ComponentMatchScoresTypeDef]

class PhonemeDetailsTypeDef(TypedDict):
    Title: NotRequired[List[PhonemeTranscriptionTypeDef]]
    Address: NotRequired[AddressComponentPhonemesTypeDef]

class AutocompleteAddressHighlightsTypeDef(TypedDict):
    Label: NotRequired[List[HighlightTypeDef]]
    Country: NotRequired[CountryHighlightsTypeDef]
    Region: NotRequired[RegionHighlightsTypeDef]
    SubRegion: NotRequired[SubRegionHighlightsTypeDef]
    Locality: NotRequired[List[HighlightTypeDef]]
    District: NotRequired[List[HighlightTypeDef]]
    SubDistrict: NotRequired[List[HighlightTypeDef]]
    Street: NotRequired[List[HighlightTypeDef]]
    Block: NotRequired[List[HighlightTypeDef]]
    SubBlock: NotRequired[List[HighlightTypeDef]]
    Intersection: NotRequired[List[List[HighlightTypeDef]]]
    PostalCode: NotRequired[List[HighlightTypeDef]]
    AddressNumber: NotRequired[List[HighlightTypeDef]]
    Building: NotRequired[List[HighlightTypeDef]]

class SuggestHighlightsTypeDef(TypedDict):
    Title: NotRequired[List[HighlightTypeDef]]
    Address: NotRequired[SuggestAddressHighlightsTypeDef]

class AutocompleteRequestTypeDef(TypedDict):
    QueryText: str
    MaxResults: NotRequired[int]
    BiasPosition: NotRequired[Sequence[float]]
    Filter: NotRequired[AutocompleteFilterTypeDef]
    PostalCodeMode: NotRequired[PostalCodeModeType]
    AdditionalFeatures: NotRequired[Sequence[Literal["Core"]]]
    Language: NotRequired[str]
    PoliticalView: NotRequired[str]
    IntendedUse: NotRequired[Literal["SingleUse"]]
    Key: NotRequired[str]

class SearchTextRequestTypeDef(TypedDict):
    QueryText: NotRequired[str]
    QueryId: NotRequired[str]
    MaxResults: NotRequired[int]
    BiasPosition: NotRequired[Sequence[float]]
    Filter: NotRequired[SearchTextFilterTypeDef]
    AdditionalFeatures: NotRequired[Sequence[SearchTextAdditionalFeatureType]]
    Language: NotRequired[str]
    PoliticalView: NotRequired[str]
    IntendedUse: NotRequired[SearchTextIntendedUseType]
    NextToken: NotRequired[str]
    Key: NotRequired[str]

class SuggestRequestTypeDef(TypedDict):
    QueryText: str
    MaxResults: NotRequired[int]
    MaxQueryRefinements: NotRequired[int]
    BiasPosition: NotRequired[Sequence[float]]
    Filter: NotRequired[SuggestFilterTypeDef]
    AdditionalFeatures: NotRequired[Sequence[SuggestAdditionalFeatureType]]
    Language: NotRequired[str]
    PoliticalView: NotRequired[str]
    IntendedUse: NotRequired[Literal["SingleUse"]]
    Key: NotRequired[str]

class ReverseGeocodeResultItemTypeDef(TypedDict):
    PlaceId: str
    PlaceType: PlaceTypeType
    Title: str
    Address: NotRequired[AddressTypeDef]
    AddressNumberCorrected: NotRequired[bool]
    PostalCodeDetails: NotRequired[List[PostalCodeDetailsTypeDef]]
    Position: NotRequired[List[float]]
    Distance: NotRequired[int]
    MapView: NotRequired[List[float]]
    Categories: NotRequired[List[CategoryTypeDef]]
    FoodTypes: NotRequired[List[FoodTypeTypeDef]]
    AccessPoints: NotRequired[List[AccessPointTypeDef]]
    TimeZone: NotRequired[TimeZoneTypeDef]
    PoliticalView: NotRequired[str]

class GeocodeResultItemTypeDef(TypedDict):
    PlaceId: str
    PlaceType: PlaceTypeType
    Title: str
    Address: NotRequired[AddressTypeDef]
    AddressNumberCorrected: NotRequired[bool]
    PostalCodeDetails: NotRequired[List[PostalCodeDetailsTypeDef]]
    Position: NotRequired[List[float]]
    Distance: NotRequired[int]
    MapView: NotRequired[List[float]]
    Categories: NotRequired[List[CategoryTypeDef]]
    FoodTypes: NotRequired[List[FoodTypeTypeDef]]
    AccessPoints: NotRequired[List[AccessPointTypeDef]]
    TimeZone: NotRequired[TimeZoneTypeDef]
    PoliticalView: NotRequired[str]
    MatchScores: NotRequired[MatchScoreDetailsTypeDef]

class GetPlaceResponseTypeDef(TypedDict):
    PlaceId: str
    PlaceType: PlaceTypeType
    Title: str
    PricingBucket: str
    Address: AddressTypeDef
    AddressNumberCorrected: bool
    PostalCodeDetails: List[PostalCodeDetailsTypeDef]
    Position: List[float]
    MapView: List[float]
    Categories: List[CategoryTypeDef]
    FoodTypes: List[FoodTypeTypeDef]
    BusinessChains: List[BusinessChainTypeDef]
    Contacts: ContactsTypeDef
    OpeningHours: List[OpeningHoursTypeDef]
    AccessPoints: List[AccessPointTypeDef]
    AccessRestrictions: List[AccessRestrictionTypeDef]
    TimeZone: TimeZoneTypeDef
    PoliticalView: str
    Phonemes: PhonemeDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchNearbyResultItemTypeDef(TypedDict):
    PlaceId: str
    PlaceType: PlaceTypeType
    Title: str
    Address: NotRequired[AddressTypeDef]
    AddressNumberCorrected: NotRequired[bool]
    Position: NotRequired[List[float]]
    Distance: NotRequired[int]
    MapView: NotRequired[List[float]]
    Categories: NotRequired[List[CategoryTypeDef]]
    FoodTypes: NotRequired[List[FoodTypeTypeDef]]
    BusinessChains: NotRequired[List[BusinessChainTypeDef]]
    Contacts: NotRequired[ContactsTypeDef]
    OpeningHours: NotRequired[List[OpeningHoursTypeDef]]
    AccessPoints: NotRequired[List[AccessPointTypeDef]]
    AccessRestrictions: NotRequired[List[AccessRestrictionTypeDef]]
    TimeZone: NotRequired[TimeZoneTypeDef]
    PoliticalView: NotRequired[str]
    Phonemes: NotRequired[PhonemeDetailsTypeDef]

class SearchTextResultItemTypeDef(TypedDict):
    PlaceId: str
    PlaceType: PlaceTypeType
    Title: str
    Address: NotRequired[AddressTypeDef]
    AddressNumberCorrected: NotRequired[bool]
    Position: NotRequired[List[float]]
    Distance: NotRequired[int]
    MapView: NotRequired[List[float]]
    Categories: NotRequired[List[CategoryTypeDef]]
    FoodTypes: NotRequired[List[FoodTypeTypeDef]]
    BusinessChains: NotRequired[List[BusinessChainTypeDef]]
    Contacts: NotRequired[ContactsTypeDef]
    OpeningHours: NotRequired[List[OpeningHoursTypeDef]]
    AccessPoints: NotRequired[List[AccessPointTypeDef]]
    AccessRestrictions: NotRequired[List[AccessRestrictionTypeDef]]
    TimeZone: NotRequired[TimeZoneTypeDef]
    PoliticalView: NotRequired[str]
    Phonemes: NotRequired[PhonemeDetailsTypeDef]

class SuggestPlaceResultTypeDef(TypedDict):
    PlaceId: NotRequired[str]
    PlaceType: NotRequired[PlaceTypeType]
    Address: NotRequired[AddressTypeDef]
    Position: NotRequired[List[float]]
    Distance: NotRequired[int]
    MapView: NotRequired[List[float]]
    Categories: NotRequired[List[CategoryTypeDef]]
    FoodTypes: NotRequired[List[FoodTypeTypeDef]]
    BusinessChains: NotRequired[List[BusinessChainTypeDef]]
    AccessPoints: NotRequired[List[AccessPointTypeDef]]
    AccessRestrictions: NotRequired[List[AccessRestrictionTypeDef]]
    TimeZone: NotRequired[TimeZoneTypeDef]
    PoliticalView: NotRequired[str]
    Phonemes: NotRequired[PhonemeDetailsTypeDef]

class AutocompleteHighlightsTypeDef(TypedDict):
    Title: NotRequired[List[HighlightTypeDef]]
    Address: NotRequired[AutocompleteAddressHighlightsTypeDef]

class ReverseGeocodeResponseTypeDef(TypedDict):
    PricingBucket: str
    ResultItems: List[ReverseGeocodeResultItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GeocodeResponseTypeDef(TypedDict):
    PricingBucket: str
    ResultItems: List[GeocodeResultItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchNearbyResponseTypeDef(TypedDict):
    PricingBucket: str
    ResultItems: List[SearchNearbyResultItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SearchTextResponseTypeDef(TypedDict):
    PricingBucket: str
    ResultItems: List[SearchTextResultItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SuggestResultItemTypeDef(TypedDict):
    Title: str
    SuggestResultItemType: SuggestResultItemTypeType
    Place: NotRequired[SuggestPlaceResultTypeDef]
    Query: NotRequired[SuggestQueryResultTypeDef]
    Highlights: NotRequired[SuggestHighlightsTypeDef]

class AutocompleteResultItemTypeDef(TypedDict):
    PlaceId: str
    PlaceType: PlaceTypeType
    Title: str
    Address: NotRequired[AddressTypeDef]
    Distance: NotRequired[int]
    Language: NotRequired[str]
    PoliticalView: NotRequired[str]
    Highlights: NotRequired[AutocompleteHighlightsTypeDef]

class SuggestResponseTypeDef(TypedDict):
    PricingBucket: str
    ResultItems: List[SuggestResultItemTypeDef]
    QueryRefinements: List[QueryRefinementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AutocompleteResponseTypeDef(TypedDict):
    PricingBucket: str
    ResultItems: List[AutocompleteResultItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
