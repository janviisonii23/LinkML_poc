import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Integer, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
REGISTRY = CurieNamespace('registry', 'http://yourdomain.org/schemas/registry/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = REGISTRY


# Types

# Class references



@dataclass(repr=False)
class ResourceSource(YAMLRoot):
    """
    Contains various metadata about a resource
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["ResourceSource"]
    class_class_curie: ClassVar[str] = "registry:ResourceSource"
    class_name: ClassVar[str] = "ResourceSource"
    class_model_uri: ClassVar[URIRef] = REGISTRY.ResourceSource

    item: Union[dict, "Item"] = None
    authority: Optional[Union[dict, "Authority"]] = None
    distributions: Optional[Union[dict, "Distributions"]] = None
    rrid: Optional[Union[dict, "RRID"]] = None
    provenance: Optional[Union[dict, "Provenance"]] = None
    disco: Optional[Union[dict, "Disco"]] = None
    graph: Optional[Union[dict, "Graph"]] = None
    diseases: Optional[Union[dict, "Diseases"]] = None
    supportingAwards: Optional[Union[Union[dict, "SupportingAwards"], List[Union[dict, "SupportingAwards"]]]] = empty_list()
    references: Optional[Union[Union[dict, "References"], List[Union[dict, "References"]]]] = empty_list()
    organisms: Optional[Union[dict, "Organisms"]] = None
    dataItem: Optional[Union[dict, "DataItem"]] = None
    mentions: Optional[Union[Union[dict, "Mentions"], List[Union[dict, "Mentions"]]]] = empty_list()
    organization: Optional[Union[dict, "Organization"]] = None
    recordValid: Optional[Union[bool, Bool]] = None
    legal: Optional[Union[dict, "Legal"]] = None
    issues: Optional[Union[dict, "Issues"]] = None
    validation: Optional[Union[dict, "Validation"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.item):
            self.MissingRequiredField("item")
        if not isinstance(self.item, Item):
            self.item = Item(**as_dict(self.item))

        if self.authority is not None and not isinstance(self.authority, Authority):
            self.authority = Authority(**as_dict(self.authority))

        if self.distributions is not None and not isinstance(self.distributions, Distributions):
            self.distributions = Distributions(**as_dict(self.distributions))

        if self.rrid is not None and not isinstance(self.rrid, RRID):
            self.rrid = RRID(**as_dict(self.rrid))

        if self.provenance is not None and not isinstance(self.provenance, Provenance):
            self.provenance = Provenance(**as_dict(self.provenance))

        if self.disco is not None and not isinstance(self.disco, Disco):
            self.disco = Disco(**as_dict(self.disco))

        if self.graph is not None and not isinstance(self.graph, Graph):
            self.graph = Graph(**as_dict(self.graph))

        if self.diseases is not None and not isinstance(self.diseases, Diseases):
            self.diseases = Diseases(**as_dict(self.diseases))

        if not isinstance(self.supportingAwards, list):
            self.supportingAwards = [self.supportingAwards] if self.supportingAwards is not None else []
        self.supportingAwards = [v if isinstance(v, SupportingAwards) else SupportingAwards(**as_dict(v)) for v in self.supportingAwards]

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, References) else References(**as_dict(v)) for v in self.references]

        if self.organisms is not None and not isinstance(self.organisms, Organisms):
            self.organisms = Organisms(**as_dict(self.organisms))

        if self.dataItem is not None and not isinstance(self.dataItem, DataItem):
            self.dataItem = DataItem(**as_dict(self.dataItem))

        if not isinstance(self.mentions, list):
            self.mentions = [self.mentions] if self.mentions is not None else []
        self.mentions = [v if isinstance(v, Mentions) else Mentions(**as_dict(v)) for v in self.mentions]

        if self.organization is not None and not isinstance(self.organization, Organization):
            self.organization = Organization(**as_dict(self.organization))

        if self.recordValid is not None and not isinstance(self.recordValid, Bool):
            self.recordValid = Bool(self.recordValid)

        if self.legal is not None and not isinstance(self.legal, Legal):
            self.legal = Legal(**as_dict(self.legal))

        if self.issues is not None and not isinstance(self.issues, Issues):
            self.issues = Issues(**as_dict(self.issues))

        if self.validation is not None and not isinstance(self.validation, Validation):
            self.validation = Validation(**as_dict(self.validation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Item(YAMLRoot):
    """
    Represents details about the registry resource.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Item"]
    class_class_curie: ClassVar[str] = "registry:Item"
    class_name: ClassVar[str] = "Item"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Item

    curie: str = None
    supercategory: Optional[Union[Union[dict, "Supercategory"], List[Union[dict, "Supercategory"]]]] = empty_list()
    contentTypes: Optional[Union[Union[dict, "ContentType"], List[Union[dict, "ContentType"]]]] = empty_list()
    synonyms: Optional[Union[Union[dict, "Synonym"], List[Union[dict, "Synonym"]]]] = empty_list()
    types: Optional[Union[Union[dict, "Type"], List[Union[dict, "Type"]]]] = empty_list()
    availability: Optional[Union[Union[dict, "Availability"], List[Union[dict, "Availability"]]]] = empty_list()
    abbreviations: Optional[Union[Union[dict, "Abbreviation"], List[Union[dict, "Abbreviation"]]]] = empty_list()
    alternateIdentifiers: Optional[Union[Union[dict, "AlternateIdentifier"], List[Union[dict, "AlternateIdentifier"]]]] = empty_list()
    keywords: Optional[Union[Union[dict, "Keyword"], List[Union[dict, "Keyword"]]]] = empty_list()
    name: Optional[str] = None
    description: Optional[str] = None
    language: Optional[str] = None
    identifier: Optional[str] = None
    docid: Optional[str] = None
    uuid: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.curie):
            self.MissingRequiredField("curie")
        if not isinstance(self.curie, str):
            self.curie = str(self.curie)

        if not isinstance(self.supercategory, list):
            self.supercategory = [self.supercategory] if self.supercategory is not None else []
        self.supercategory = [v if isinstance(v, Supercategory) else Supercategory(**as_dict(v)) for v in self.supercategory]

        if not isinstance(self.contentTypes, list):
            self.contentTypes = [self.contentTypes] if self.contentTypes is not None else []
        self.contentTypes = [v if isinstance(v, ContentType) else ContentType(**as_dict(v)) for v in self.contentTypes]

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, Synonym) else Synonym(**as_dict(v)) for v in self.synonyms]

        if not isinstance(self.types, list):
            self.types = [self.types] if self.types is not None else []
        self.types = [v if isinstance(v, Type) else Type(**as_dict(v)) for v in self.types]

        if not isinstance(self.availability, list):
            self.availability = [self.availability] if self.availability is not None else []
        self.availability = [v if isinstance(v, Availability) else Availability(**as_dict(v)) for v in self.availability]

        if not isinstance(self.abbreviations, list):
            self.abbreviations = [self.abbreviations] if self.abbreviations is not None else []
        self.abbreviations = [v if isinstance(v, Abbreviation) else Abbreviation(**as_dict(v)) for v in self.abbreviations]

        if not isinstance(self.alternateIdentifiers, list):
            self.alternateIdentifiers = [self.alternateIdentifiers] if self.alternateIdentifiers is not None else []
        self.alternateIdentifiers = [v if isinstance(v, AlternateIdentifier) else AlternateIdentifier(**as_dict(v)) for v in self.alternateIdentifiers]

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, Keyword) else Keyword(**as_dict(v)) for v in self.keywords]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.language is not None and not isinstance(self.language, str):
            self.language = str(self.language)

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.docid is not None and not isinstance(self.docid, str):
            self.docid = str(self.docid)

        if self.uuid is not None and not isinstance(self.uuid, str):
            self.uuid = str(self.uuid)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Keyword(YAMLRoot):
    """
    Keywords related to the resource
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Keyword"]
    class_class_curie: ClassVar[str] = "registry:Keyword"
    class_name: ClassVar[str] = "Keyword"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Keyword

    keyword: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.keyword is not None and not isinstance(self.keyword, str):
            self.keyword = str(self.keyword)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AlternateIdentifier(YAMLRoot):
    """
    Alternate identifier for a resource
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["AlternateIdentifier"]
    class_class_curie: ClassVar[str] = "registry:AlternateIdentifier"
    class_name: ClassVar[str] = "AlternateIdentifier"
    class_model_uri: ClassVar[URIRef] = REGISTRY.AlternateIdentifier

    identifier: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Abbreviation(YAMLRoot):
    """
    Abbreviation of the resource
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Abbreviation"]
    class_class_curie: ClassVar[str] = "registry:Abbreviation"
    class_name: ClassVar[str] = "Abbreviation"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Abbreviation

    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Authority(YAMLRoot):
    """
    Represents the authority managing the resource.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Authority"]
    class_class_curie: ClassVar[str] = "registry:Authority"
    class_name: ClassVar[str] = "Authority"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Authority

    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Distributions(YAMLRoot):
    """
    Contains different distribution URLs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Distributions"]
    class_class_curie: ClassVar[str] = "registry:Distributions"
    class_name: ClassVar[str] = "Distributions"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Distributions

    current: Optional[Union[Union[dict, "URLReference"], List[Union[dict, "URLReference"]]]] = empty_list()
    deprecated: Optional[Union[Union[dict, "URLReference"], List[Union[dict, "URLReference"]]]] = empty_list()
    alternate: Optional[Union[Union[dict, "URLReference"], List[Union[dict, "URLReference"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.current, list):
            self.current = [self.current] if self.current is not None else []
        self.current = [v if isinstance(v, URLReference) else URLReference(**as_dict(v)) for v in self.current]

        if not isinstance(self.deprecated, list):
            self.deprecated = [self.deprecated] if self.deprecated is not None else []
        self.deprecated = [v if isinstance(v, URLReference) else URLReference(**as_dict(v)) for v in self.deprecated]

        if not isinstance(self.alternate, list):
            self.alternate = [self.alternate] if self.alternate is not None else []
        self.alternate = [v if isinstance(v, URLReference) else URLReference(**as_dict(v)) for v in self.alternate]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RRID(YAMLRoot):
    """
    Contains RRID (Research Resource Identifier) metadata.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["RRID"]
    class_class_curie: ClassVar[str] = "registry:RRID"
    class_name: ClassVar[str] = "RRID"
    class_model_uri: ClassVar[URIRef] = REGISTRY.RRID

    is_unique: Optional[str] = None
    curie: Optional[str] = None
    properCitation: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.is_unique is not None and not isinstance(self.is_unique, str):
            self.is_unique = str(self.is_unique)

        if self.curie is not None and not isinstance(self.curie, str):
            self.curie = str(self.curie)

        if self.properCitation is not None and not isinstance(self.properCitation, str):
            self.properCitation = str(self.properCitation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Provenance(YAMLRoot):
    """
    Metadata about how the resource was ingested.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Provenance"]
    class_class_curie: ClassVar[str] = "registry:Provenance"
    class_name: ClassVar[str] = "Provenance"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Provenance

    ingestMethod: Optional[str] = None
    ingestTime: Optional[str] = None
    creationDate: Optional[Union[str, List[str]]] = empty_list()
    lastSeenDate: Optional[str] = None
    docId: Optional[str] = None
    primaryKey: Optional[str] = None
    ingestTarget: Optional[str] = None
    filePattern: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ingestMethod is not None and not isinstance(self.ingestMethod, str):
            self.ingestMethod = str(self.ingestMethod)

        if self.ingestTime is not None and not isinstance(self.ingestTime, str):
            self.ingestTime = str(self.ingestTime)

        if not isinstance(self.creationDate, list):
            self.creationDate = [self.creationDate] if self.creationDate is not None else []
        self.creationDate = [v if isinstance(v, str) else str(v) for v in self.creationDate]

        if self.lastSeenDate is not None and not isinstance(self.lastSeenDate, str):
            self.lastSeenDate = str(self.lastSeenDate)

        if self.docId is not None and not isinstance(self.docId, str):
            self.docId = str(self.docId)

        if self.primaryKey is not None and not isinstance(self.primaryKey, str):
            self.primaryKey = str(self.primaryKey)

        if self.ingestTarget is not None and not isinstance(self.ingestTarget, str):
            self.ingestTarget = str(self.ingestTarget)

        if self.filePattern is not None and not isinstance(self.filePattern, str):
            self.filePattern = str(self.filePattern)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Supercategory(YAMLRoot):
    """
    Represents the supercategory of a resource.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Supercategory"]
    class_class_curie: ClassVar[str] = "registry:Supercategory"
    class_name: ClassVar[str] = "Supercategory"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Supercategory

    name: Optional[str] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContentType(YAMLRoot):
    """
    Represents the type of content.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["ContentType"]
    class_class_curie: ClassVar[str] = "registry:ContentType"
    class_name: ClassVar[str] = "ContentType"
    class_model_uri: ClassVar[URIRef] = REGISTRY.ContentType

    curie: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.curie is not None and not isinstance(self.curie, str):
            self.curie = str(self.curie)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Synonym(YAMLRoot):
    """
    Represents a synonym for a resource.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Synonym"]
    class_class_curie: ClassVar[str] = "registry:Synonym"
    class_name: ClassVar[str] = "Synonym"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Synonym

    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Type(YAMLRoot):
    """
    Represents the type/category of the resource.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Type"]
    class_class_curie: ClassVar[str] = "registry:Type"
    class_name: ClassVar[str] = "Type"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Type

    name: Optional[str] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Availability(YAMLRoot):
    """
    Represents the availability status of the resource.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Availability"]
    class_class_curie: ClassVar[str] = "registry:Availability"
    class_name: ClassVar[str] = "Availability"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Availability

    description: Optional[str] = None
    keyword: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.keyword is not None and not isinstance(self.keyword, str):
            self.keyword = str(self.keyword)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class URLReference(YAMLRoot):
    """
    Represents a reference to a URL.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["URLReference"]
    class_class_curie: ClassVar[str] = "registry:URLReference"
    class_name: ClassVar[str] = "URLReference"
    class_model_uri: ClassVar[URIRef] = REGISTRY.URLReference

    type: Optional[str] = None
    uri: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.uri is not None and not isinstance(self.uri, str):
            self.uri = str(self.uri)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Disco(YAMLRoot):
    """
    Disco metadata
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Disco"]
    class_class_curie: ClassVar[str] = "registry:Disco"
    class_name: ClassVar[str] = "Disco"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Disco

    v_uuid: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.v_uuid is not None and not isinstance(self.v_uuid, str):
            self.v_uuid = str(self.v_uuid)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SupportingAwards(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["SupportingAwards"]
    class_class_curie: ClassVar[str] = "registry:SupportingAwards"
    class_name: ClassVar[str] = "supportingAwards"
    class_model_uri: ClassVar[URIRef] = REGISTRY.SupportingAwards

    agency: Optional[Union[dict, "Agency"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.agency is not None and not isinstance(self.agency, Agency):
            self.agency = Agency(**as_dict(self.agency))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Agency(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Agency"]
    class_class_curie: ClassVar[str] = "registry:Agency"
    class_name: ClassVar[str] = "Agency"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Agency

    identifier: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Graph(YAMLRoot):
    """
    Graph relationships metadata
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Graph"]
    class_class_curie: ClassVar[str] = "registry:Graph"
    class_name: ClassVar[str] = "Graph"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Graph

    relationships: Optional[Union[Union[dict, "Relationship"], List[Union[dict, "Relationship"]]]] = empty_list()
    child: Optional[Union[Union[dict, "ChildRelationship"], List[Union[dict, "ChildRelationship"]]]] = empty_list()
    parent: Optional[Union[Union[dict, "ParentRelationship"], List[Union[dict, "ParentRelationship"]]]] = empty_list()
    related: Optional[Union[Union[dict, "RelatedRelationship"], List[Union[dict, "RelatedRelationship"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.relationships, list):
            self.relationships = [self.relationships] if self.relationships is not None else []
        self.relationships = [v if isinstance(v, Relationship) else Relationship(**as_dict(v)) for v in self.relationships]

        if not isinstance(self.child, list):
            self.child = [self.child] if self.child is not None else []
        self.child = [v if isinstance(v, ChildRelationship) else ChildRelationship(**as_dict(v)) for v in self.child]

        if not isinstance(self.parent, list):
            self.parent = [self.parent] if self.parent is not None else []
        self.parent = [v if isinstance(v, ParentRelationship) else ParentRelationship(**as_dict(v)) for v in self.parent]

        if not isinstance(self.related, list):
            self.related = [self.related] if self.related is not None else []
        self.related = [v if isinstance(v, RelatedRelationship) else RelatedRelationship(**as_dict(v)) for v in self.related]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelatedRelationship(YAMLRoot):
    """
    Non-hierarchical associations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["RelatedRelationship"]
    class_class_curie: ClassVar[str] = "registry:RelatedRelationship"
    class_name: ClassVar[str] = "RelatedRelationship"
    class_model_uri: ClassVar[URIRef] = REGISTRY.RelatedRelationship

    resource: Optional[Union[dict, "RelatedResource"]] = None
    relationship: Optional[Union[dict, "RelationshipType"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.resource is not None and not isinstance(self.resource, RelatedResource):
            self.resource = RelatedResource(**as_dict(self.resource))

        if self.relationship is not None and not isinstance(self.relationship, RelationshipType):
            self.relationship = RelationshipType(**as_dict(self.relationship))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Relationship(YAMLRoot):
    """
    A relationship between resources
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Relationship"]
    class_class_curie: ClassVar[str] = "registry:Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Relationship

    resource: Optional[Union[dict, "RelatedResource"]] = None
    relationship: Optional[Union[dict, "RelationshipType"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.resource is not None and not isinstance(self.resource, RelatedResource):
            self.resource = RelatedResource(**as_dict(self.resource))

        if self.relationship is not None and not isinstance(self.relationship, RelationshipType):
            self.relationship = RelationshipType(**as_dict(self.relationship))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChildRelationship(YAMLRoot):
    """
    A child-type relationship
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["ChildRelationship"]
    class_class_curie: ClassVar[str] = "registry:ChildRelationship"
    class_name: ClassVar[str] = "ChildRelationship"
    class_model_uri: ClassVar[URIRef] = REGISTRY.ChildRelationship

    resource: Optional[Union[dict, "RelatedResource"]] = None
    relationship: Optional[Union[dict, "RelationshipType"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.resource is not None and not isinstance(self.resource, RelatedResource):
            self.resource = RelatedResource(**as_dict(self.resource))

        if self.relationship is not None and not isinstance(self.relationship, RelationshipType):
            self.relationship = RelationshipType(**as_dict(self.relationship))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ParentRelationship(YAMLRoot):
    """
    A parent-type relationship
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["ParentRelationship"]
    class_class_curie: ClassVar[str] = "registry:ParentRelationship"
    class_name: ClassVar[str] = "ParentRelationship"
    class_model_uri: ClassVar[URIRef] = REGISTRY.ParentRelationship

    resource: Optional[Union[dict, "RelatedResource"]] = None
    relationship: Optional[Union[dict, "RelationshipType"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.resource is not None and not isinstance(self.resource, RelatedResource):
            self.resource = RelatedResource(**as_dict(self.resource))

        if self.relationship is not None and not isinstance(self.relationship, RelationshipType):
            self.relationship = RelationshipType(**as_dict(self.relationship))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelatedResource(YAMLRoot):
    """
    Details of a related resource
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["RelatedResource"]
    class_class_curie: ClassVar[str] = "registry:RelatedResource"
    class_name: ClassVar[str] = "RelatedResource"
    class_model_uri: ClassVar[URIRef] = REGISTRY.RelatedResource

    identifier: Optional[str] = None
    name: Optional[str] = None
    is_related_to: Optional[Union[Union[dict, Graph], List[Union[dict, Graph]]]] = empty_list()
    is_related_by: Optional[Union[dict, Relationship]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.is_related_to, list):
            self.is_related_to = [self.is_related_to] if self.is_related_to is not None else []
        self.is_related_to = [v if isinstance(v, Graph) else Graph(**as_dict(v)) for v in self.is_related_to]

        if self.is_related_by is not None and not isinstance(self.is_related_by, Relationship):
            self.is_related_by = Relationship(**as_dict(self.is_related_by))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelationshipType(YAMLRoot):
    """
    Type of relationship between resources
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["RelationshipType"]
    class_class_curie: ClassVar[str] = "registry:RelationshipType"
    class_name: ClassVar[str] = "RelationshipType"
    class_model_uri: ClassVar[URIRef] = REGISTRY.RelationshipType

    identifier: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Diseases(YAMLRoot):
    """
    Disease-related metadata
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Diseases"]
    class_class_curie: ClassVar[str] = "registry:Diseases"
    class_name: ClassVar[str] = "Diseases"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Diseases

    related: Optional[Union[Union[dict, "Disease"], List[Union[dict, "Disease"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.related, list):
            self.related = [self.related] if self.related is not None else []
        self.related = [v if isinstance(v, Disease) else Disease(**as_dict(v)) for v in self.related]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Disease(YAMLRoot):
    """
    Disease metadata
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Disease"]
    class_class_curie: ClassVar[str] = "registry:Disease"
    class_name: ClassVar[str] = "Disease"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Disease

    role: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class References(YAMLRoot):
    """
    References related to the resource
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["References"]
    class_class_curie: ClassVar[str] = "registry:References"
    class_name: ClassVar[str] = "References"
    class_model_uri: ClassVar[URIRef] = REGISTRY.References

    curie: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.curie is not None and not isinstance(self.curie, str):
            self.curie = str(self.curie)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataItem(YAMLRoot):
    """
    Data items associated with the resource
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["DataItem"]
    class_class_curie: ClassVar[str] = "registry:DataItem"
    class_name: ClassVar[str] = "DataItem"
    class_model_uri: ClassVar[URIRef] = REGISTRY.DataItem

    dataTypes: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.dataTypes, list):
            self.dataTypes = [self.dataTypes] if self.dataTypes is not None else []
        self.dataTypes = [v if isinstance(v, str) else str(v) for v in self.dataTypes]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organisms(YAMLRoot):
    """
    Organisms related to the resource
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Organisms"]
    class_class_curie: ClassVar[str] = "registry:Organisms"
    class_name: ClassVar[str] = "Organisms"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Organisms

    related: Optional[Union[Union[dict, "Organism"], List[Union[dict, "Organism"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.related, list):
            self.related = [self.related] if self.related is not None else []
        self.related = [v if isinstance(v, Organism) else Organism(**as_dict(v)) for v in self.related]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organism(YAMLRoot):
    """
    Organism entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Organism"]
    class_class_curie: ClassVar[str] = "registry:Organism"
    class_name: ClassVar[str] = "Organism"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Organism

    role: Optional[str] = None
    species: Optional[Union[dict, "Species"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        if self.species is not None and not isinstance(self.species, Species):
            self.species = Species(**as_dict(self.species))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Species(YAMLRoot):
    """
    Species classification
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Species"]
    class_class_curie: ClassVar[str] = "registry:Species"
    class_name: ClassVar[str] = "Species"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Species

    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Mentions(YAMLRoot):
    """
    Information about mentions of the resource
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Mentions"]
    class_class_curie: ClassVar[str] = "registry:Mentions"
    class_name: ClassVar[str] = "Mentions"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Mentions

    totalResourceMentions: Optional[Union[dict, "TotalResourceMentions"]] = None
    totalRRIDMentions: Optional[Union[dict, "TotalRRIDMentions"]] = None
    totalMentions: Optional[Union[dict, "TotalMentions"]] = None
    timestamp: Optional[str] = None
    availability: Optional[Union[dict, "Availability2"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.totalResourceMentions is not None and not isinstance(self.totalResourceMentions, TotalResourceMentions):
            self.totalResourceMentions = TotalResourceMentions(**as_dict(self.totalResourceMentions))

        if self.totalRRIDMentions is not None and not isinstance(self.totalRRIDMentions, TotalRRIDMentions):
            self.totalRRIDMentions = TotalRRIDMentions(**as_dict(self.totalRRIDMentions))

        if self.totalMentions is not None and not isinstance(self.totalMentions, TotalMentions):
            self.totalMentions = TotalMentions(**as_dict(self.totalMentions))

        if self.timestamp is not None and not isinstance(self.timestamp, str):
            self.timestamp = str(self.timestamp)

        if self.availability is not None and not isinstance(self.availability, Availability2):
            self.availability = Availability2(**as_dict(self.availability))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TotalResourceMentions(YAMLRoot):
    """
    Stores count of resource mentions
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["TotalResourceMentions"]
    class_class_curie: ClassVar[str] = "registry:TotalResourceMentions"
    class_name: ClassVar[str] = "TotalResourceMentions"
    class_model_uri: ClassVar[URIRef] = REGISTRY.TotalResourceMentions

    count: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.count is not None and not isinstance(self.count, int):
            self.count = int(self.count)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TotalRRIDMentions(YAMLRoot):
    """
    Stores count of RRID mentions
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["TotalRRIDMentions"]
    class_class_curie: ClassVar[str] = "registry:TotalRRIDMentions"
    class_name: ClassVar[str] = "TotalRRIDMentions"
    class_model_uri: ClassVar[URIRef] = REGISTRY.TotalRRIDMentions

    count: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.count is not None and not isinstance(self.count, int):
            self.count = int(self.count)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TotalMentions(YAMLRoot):
    """
    Stores count of total mentions
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["TotalMentions"]
    class_class_curie: ClassVar[str] = "registry:TotalMentions"
    class_name: ClassVar[str] = "TotalMentions"
    class_model_uri: ClassVar[URIRef] = REGISTRY.TotalMentions

    count: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.count is not None and not isinstance(self.count, int):
            self.count = int(self.count)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Availability2(YAMLRoot):
    """
    Availability metadata
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Availability2"]
    class_class_curie: ClassVar[str] = "registry:Availability2"
    class_name: ClassVar[str] = "Availability2"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Availability2

    keyword: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.keyword is not None and not isinstance(self.keyword, str):
            self.keyword = str(self.keyword)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organization(YAMLRoot):
    """
    Organization details
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Organization"]
    class_class_curie: ClassVar[str] = "registry:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Organization

    hierarchy: Optional[Union[dict, "Hierarchy"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hierarchy is not None and not isinstance(self.hierarchy, Hierarchy):
            self.hierarchy = Hierarchy(**as_dict(self.hierarchy))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Hierarchy(YAMLRoot):
    """
    Organization hierarchy
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Hierarchy"]
    class_class_curie: ClassVar[str] = "registry:Hierarchy"
    class_name: ClassVar[str] = "Hierarchy"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Hierarchy

    children: Optional[Union[Union[dict, "Children"], List[Union[dict, "Children"]]]] = empty_list()
    descendants: Optional[Union[Union[dict, "Descendants"], List[Union[dict, "Descendants"]]]] = empty_list()
    ancestors: Optional[Union[Union[dict, "Ancestors"], List[Union[dict, "Ancestors"]]]] = empty_list()
    parent: Optional[Union[Union[dict, "Parent"], List[Union[dict, "Parent"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.children, list):
            self.children = [self.children] if self.children is not None else []
        self.children = [v if isinstance(v, Children) else Children(**as_dict(v)) for v in self.children]

        if not isinstance(self.descendants, list):
            self.descendants = [self.descendants] if self.descendants is not None else []
        self.descendants = [v if isinstance(v, Descendants) else Descendants(**as_dict(v)) for v in self.descendants]

        if not isinstance(self.ancestors, list):
            self.ancestors = [self.ancestors] if self.ancestors is not None else []
        self.ancestors = [v if isinstance(v, Ancestors) else Ancestors(**as_dict(v)) for v in self.ancestors]

        if not isinstance(self.parent, list):
            self.parent = [self.parent] if self.parent is not None else []
        self.parent = [v if isinstance(v, Parent) else Parent(**as_dict(v)) for v in self.parent]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Children(YAMLRoot):
    """
    Child organizations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Children"]
    class_class_curie: ClassVar[str] = "registry:Children"
    class_name: ClassVar[str] = "Children"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Children

    curie: Optional[str] = None
    name: Optional[str] = None
    is_child_of: Optional[Union[Union[dict, Hierarchy], List[Union[dict, Hierarchy]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.curie is not None and not isinstance(self.curie, str):
            self.curie = str(self.curie)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.is_child_of, list):
            self.is_child_of = [self.is_child_of] if self.is_child_of is not None else []
        self.is_child_of = [v if isinstance(v, Hierarchy) else Hierarchy(**as_dict(v)) for v in self.is_child_of]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Descendants(YAMLRoot):
    """
    Descendant organizations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Descendants"]
    class_class_curie: ClassVar[str] = "registry:Descendants"
    class_name: ClassVar[str] = "Descendants"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Descendants

    curie: Optional[str] = None
    name: Optional[str] = None
    is_descendant_of: Optional[Union[Union[dict, Hierarchy], List[Union[dict, Hierarchy]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.curie is not None and not isinstance(self.curie, str):
            self.curie = str(self.curie)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.is_descendant_of, list):
            self.is_descendant_of = [self.is_descendant_of] if self.is_descendant_of is not None else []
        self.is_descendant_of = [v if isinstance(v, Hierarchy) else Hierarchy(**as_dict(v)) for v in self.is_descendant_of]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Ancestors(YAMLRoot):
    """
    Ancestor organizations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Ancestors"]
    class_class_curie: ClassVar[str] = "registry:Ancestors"
    class_name: ClassVar[str] = "Ancestors"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Ancestors

    curie: Optional[str] = None
    name: Optional[str] = None
    is_ancestor_of: Optional[Union[Union[dict, Hierarchy], List[Union[dict, Hierarchy]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.curie is not None and not isinstance(self.curie, str):
            self.curie = str(self.curie)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.is_ancestor_of, list):
            self.is_ancestor_of = [self.is_ancestor_of] if self.is_ancestor_of is not None else []
        self.is_ancestor_of = [v if isinstance(v, Hierarchy) else Hierarchy(**as_dict(v)) for v in self.is_ancestor_of]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Parent(YAMLRoot):
    """
    Parent organization
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Parent"]
    class_class_curie: ClassVar[str] = "registry:Parent"
    class_name: ClassVar[str] = "Parent"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Parent

    curie: Optional[str] = None
    name: Optional[str] = None
    is_parent_of: Optional[Union[Union[dict, Hierarchy], List[Union[dict, Hierarchy]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.curie is not None and not isinstance(self.curie, str):
            self.curie = str(self.curie)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.is_parent_of, list):
            self.is_parent_of = [self.is_parent_of] if self.is_parent_of is not None else []
        self.is_parent_of = [v if isinstance(v, Hierarchy) else Hierarchy(**as_dict(v)) for v in self.is_parent_of]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Legal(YAMLRoot):
    """
    Legal information associated with the resource
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Legal"]
    class_class_curie: ClassVar[str] = "registry:Legal"
    class_name: ClassVar[str] = "Legal"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Legal

    license: Optional[Union[dict, "License"]] = None
    terms: Optional[Union[dict, "Terms"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.license is not None and not isinstance(self.license, License):
            self.license = License(**as_dict(self.license))

        if self.terms is not None and not isinstance(self.terms, Terms):
            self.terms = Terms(**as_dict(self.terms))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class License(YAMLRoot):
    """
    License information
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["License"]
    class_class_curie: ClassVar[str] = "registry:License"
    class_name: ClassVar[str] = "License"
    class_model_uri: ClassVar[URIRef] = REGISTRY.License

    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Terms(YAMLRoot):
    """
    Terms of use information
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Terms"]
    class_class_curie: ClassVar[str] = "registry:Terms"
    class_name: ClassVar[str] = "Terms"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Terms

    uris: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.uris, list):
            self.uris = [self.uris] if self.uris is not None else []
        self.uris = [v if isinstance(v, str) else str(v) for v in self.uris]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Issues(YAMLRoot):
    """
    Issues associated with the resource
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Issues"]
    class_class_curie: ClassVar[str] = "registry:Issues"
    class_name: ClassVar[str] = "Issues"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Issues

    totalIssues: Optional[Union[dict, "TotalIssues"]] = None
    status: Optional[Union[str, List[str]]] = empty_list()
    direct: Optional[Union[Union[dict, "Direct"], List[Union[dict, "Direct"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.totalIssues is not None and not isinstance(self.totalIssues, TotalIssues):
            self.totalIssues = TotalIssues(**as_dict(self.totalIssues))

        if not isinstance(self.status, list):
            self.status = [self.status] if self.status is not None else []
        self.status = [v if isinstance(v, str) else str(v) for v in self.status]

        if not isinstance(self.direct, list):
            self.direct = [self.direct] if self.direct is not None else []
        self.direct = [v if isinstance(v, Direct) else Direct(**as_dict(v)) for v in self.direct]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TotalIssues(YAMLRoot):
    """
    Total number of issues
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["TotalIssues"]
    class_class_curie: ClassVar[str] = "registry:TotalIssues"
    class_name: ClassVar[str] = "TotalIssues"
    class_model_uri: ClassVar[URIRef] = REGISTRY.TotalIssues

    count: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.count is not None and not isinstance(self.count, int):
            self.count = int(self.count)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Direct(YAMLRoot):
    """
    Direct issue details
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Direct"]
    class_class_curie: ClassVar[str] = "registry:Direct"
    class_name: ClassVar[str] = "Direct"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Direct

    comments: Optional[str] = None
    issue: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.comments is not None and not isinstance(self.comments, str):
            self.comments = str(self.comments)

        if self.issue is not None and not isinstance(self.issue, str):
            self.issue = str(self.issue)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Validation(YAMLRoot):
    """
    Validation information for the resource
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["Validation"]
    class_class_curie: ClassVar[str] = "registry:Validation"
    class_name: ClassVar[str] = "Validation"
    class_model_uri: ClassVar[URIRef] = REGISTRY.Validation

    isValidated: Optional[Union[bool, Bool]] = None
    totalValidationSites: Optional[Union[dict, "CountValue"]] = None
    validationSitesInformation: Optional[Union[Union[dict, "ValidationSitesInformation"], List[Union[dict, "ValidationSitesInformation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.isValidated is not None and not isinstance(self.isValidated, Bool):
            self.isValidated = Bool(self.isValidated)

        if self.totalValidationSites is not None and not isinstance(self.totalValidationSites, CountValue):
            self.totalValidationSites = CountValue(**as_dict(self.totalValidationSites))

        if not isinstance(self.validationSitesInformation, list):
            self.validationSitesInformation = [self.validationSitesInformation] if self.validationSitesInformation is not None else []
        self.validationSitesInformation = [v if isinstance(v, ValidationSitesInformation) else ValidationSitesInformation(**as_dict(v)) for v in self.validationSitesInformation]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ValidationSitesInformation(YAMLRoot):
    """
    Information about validation sites
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["ValidationSitesInformation"]
    class_class_curie: ClassVar[str] = "registry:ValidationSitesInformation"
    class_name: ClassVar[str] = "ValidationSitesInformation"
    class_model_uri: ClassVar[URIRef] = REGISTRY.ValidationSitesInformation

    comments: Optional[str] = None
    curie: Optional[str] = None
    name: Optional[str] = None
    provider_id: Optional[str] = None
    uri: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.comments is not None and not isinstance(self.comments, str):
            self.comments = str(self.comments)

        if self.curie is not None and not isinstance(self.curie, str):
            self.curie = str(self.curie)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.provider_id is not None and not isinstance(self.provider_id, str):
            self.provider_id = str(self.provider_id)

        if self.uri is not None and not isinstance(self.uri, str):
            self.uri = str(self.uri)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CountValue(YAMLRoot):
    """
    A simple count representation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REGISTRY["CountValue"]
    class_class_curie: ClassVar[str] = "registry:CountValue"
    class_name: ClassVar[str] = "CountValue"
    class_model_uri: ClassVar[URIRef] = REGISTRY.CountValue

    count: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.count is not None and not isinstance(self.count, int):
            self.count = int(self.count)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.has_supercategory = Slot(uri=REGISTRY.supercategory, name="has_supercategory", curie=REGISTRY.curie('supercategory'),
                   model_uri=REGISTRY.has_supercategory, domain=Item, range=Optional[Union[Union[dict, "Supercategory"], List[Union[dict, "Supercategory"]]]])

slots.has_content_type = Slot(uri=REGISTRY.contentTypes, name="has_content_type", curie=REGISTRY.curie('contentTypes'),
                   model_uri=REGISTRY.has_content_type, domain=Item, range=Optional[Union[Union[dict, "ContentType"], List[Union[dict, "ContentType"]]]])

slots.has_synonym = Slot(uri=REGISTRY.synonyms, name="has_synonym", curie=REGISTRY.curie('synonyms'),
                   model_uri=REGISTRY.has_synonym, domain=Item, range=Optional[Union[Union[dict, "Synonym"], List[Union[dict, "Synonym"]]]])

slots.has_type = Slot(uri=REGISTRY.types, name="has_type", curie=REGISTRY.curie('types'),
                   model_uri=REGISTRY.has_type, domain=Item, range=Optional[Union[Union[dict, "Type"], List[Union[dict, "Type"]]]])

slots.has_availability = Slot(uri=REGISTRY.availability, name="has_availability", curie=REGISTRY.curie('availability'),
                   model_uri=REGISTRY.has_availability, domain=Item, range=Optional[Union[Union[dict, "Availability"], List[Union[dict, "Availability"]]]])

slots.has_abbreviation = Slot(uri=REGISTRY.abbreviations, name="has_abbreviation", curie=REGISTRY.curie('abbreviations'),
                   model_uri=REGISTRY.has_abbreviation, domain=Item, range=Optional[Union[Union[dict, "Abbreviation"], List[Union[dict, "Abbreviation"]]]])

slots.has_alternate_identifier = Slot(uri=REGISTRY.alternateIdentifiers, name="has_alternate_identifier", curie=REGISTRY.curie('alternateIdentifiers'),
                   model_uri=REGISTRY.has_alternate_identifier, domain=Item, range=Optional[Union[Union[dict, "AlternateIdentifier"], List[Union[dict, "AlternateIdentifier"]]]])

slots.has_keyword = Slot(uri=REGISTRY.keywords, name="has_keyword", curie=REGISTRY.curie('keywords'),
                   model_uri=REGISTRY.has_keyword, domain=Item, range=Optional[Union[Union[dict, "Keyword"], List[Union[dict, "Keyword"]]]])

slots.has_current_distribution = Slot(uri=REGISTRY.current, name="has_current_distribution", curie=REGISTRY.curie('current'),
                   model_uri=REGISTRY.has_current_distribution, domain=Distributions, range=Optional[Union[Union[dict, "URLReference"], List[Union[dict, "URLReference"]]]])

slots.has_deprecated_distribution = Slot(uri=REGISTRY.deprecated, name="has_deprecated_distribution", curie=REGISTRY.curie('deprecated'),
                   model_uri=REGISTRY.has_deprecated_distribution, domain=Distributions, range=Optional[Union[Union[dict, "URLReference"], List[Union[dict, "URLReference"]]]])

slots.has_alternate_distribution = Slot(uri=REGISTRY.alternate, name="has_alternate_distribution", curie=REGISTRY.curie('alternate'),
                   model_uri=REGISTRY.has_alternate_distribution, domain=Distributions, range=Optional[Union[Union[dict, "URLReference"], List[Union[dict, "URLReference"]]]])

slots.has_uniqueness = Slot(uri=REGISTRY.is_unique, name="has_uniqueness", curie=REGISTRY.curie('is_unique'),
                   model_uri=REGISTRY.has_uniqueness, domain=RRID, range=Optional[str])

slots.has_hierarchy = Slot(uri=REGISTRY.hierarchy, name="has_hierarchy", curie=REGISTRY.curie('hierarchy'),
                   model_uri=REGISTRY.has_hierarchy, domain=Organization, range=Optional[Union[dict, "Hierarchy"]])

slots.has_children = Slot(uri=REGISTRY.children, name="has_children", curie=REGISTRY.curie('children'),
                   model_uri=REGISTRY.has_children, domain=Hierarchy, range=Optional[Union[Union[dict, "Children"], List[Union[dict, "Children"]]]])

slots.has_descendants = Slot(uri=REGISTRY.descendants, name="has_descendants", curie=REGISTRY.curie('descendants'),
                   model_uri=REGISTRY.has_descendants, domain=Hierarchy, range=Optional[Union[Union[dict, "Descendants"], List[Union[dict, "Descendants"]]]])

slots.has_ancestors = Slot(uri=REGISTRY.ancestors, name="has_ancestors", curie=REGISTRY.curie('ancestors'),
                   model_uri=REGISTRY.has_ancestors, domain=Hierarchy, range=Optional[Union[Union[dict, "Ancestors"], List[Union[dict, "Ancestors"]]]])

slots.has_parent_hierachy = Slot(uri=REGISTRY.parent, name="has_parent_hierachy", curie=REGISTRY.curie('parent'),
                   model_uri=REGISTRY.has_parent_hierachy, domain=Hierarchy, range=Optional[Union[Union[dict, "Parent"], List[Union[dict, "Parent"]]]])

slots.has_curie_children = Slot(uri=REGISTRY.curie, name="has_curie_children", curie=REGISTRY.curie('curie'),
                   model_uri=REGISTRY.has_curie_children, domain=Children, range=Optional[str])

slots.has_curie_descendent = Slot(uri=REGISTRY.curie, name="has_curie_descendent", curie=REGISTRY.curie('curie'),
                   model_uri=REGISTRY.has_curie_descendent, domain=Descendants, range=Optional[str])

slots.has_curie_ancestor = Slot(uri=REGISTRY.curie, name="has_curie_ancestor", curie=REGISTRY.curie('curie'),
                   model_uri=REGISTRY.has_curie_ancestor, domain=Ancestors, range=Optional[str])

slots.has_curie_parent = Slot(uri=REGISTRY.curie, name="has_curie_parent", curie=REGISTRY.curie('curie'),
                   model_uri=REGISTRY.has_curie_parent, domain=Parent, range=Optional[str])

slots.has_curie_rrid = Slot(uri=REGISTRY.curie, name="has_curie_rrid", curie=REGISTRY.curie('curie'),
                   model_uri=REGISTRY.has_curie_rrid, domain=RRID, range=Optional[str])

slots.has_curie_validation = Slot(uri=REGISTRY.curie, name="has_curie_validation", curie=REGISTRY.curie('curie'),
                   model_uri=REGISTRY.has_curie_validation, domain=ValidationSitesInformation, range=Optional[str])

slots.has_proper_citation = Slot(uri=REGISTRY.properCitation, name="has_proper_citation", curie=REGISTRY.curie('properCitation'),
                   model_uri=REGISTRY.has_proper_citation, domain=RRID, range=Optional[str])

slots.has_ingest_method = Slot(uri=REGISTRY.ingestMethod, name="has_ingest_method", curie=REGISTRY.curie('ingestMethod'),
                   model_uri=REGISTRY.has_ingest_method, domain=Provenance, range=Optional[str])

slots.has_ingest_time = Slot(uri=REGISTRY.ingestTime, name="has_ingest_time", curie=REGISTRY.curie('ingestTime'),
                   model_uri=REGISTRY.has_ingest_time, domain=Provenance, range=Optional[str])

slots.has_creation_date = Slot(uri=REGISTRY.creationDate, name="has_creation_date", curie=REGISTRY.curie('creationDate'),
                   model_uri=REGISTRY.has_creation_date, domain=Provenance, range=Optional[Union[str, List[str]]])

slots.has_last_seen_date = Slot(uri=REGISTRY.lastSeenDate, name="has_last_seen_date", curie=REGISTRY.curie('lastSeenDate'),
                   model_uri=REGISTRY.has_last_seen_date, domain=Provenance, range=Optional[str])

slots.has_doc_id = Slot(uri=REGISTRY.docId, name="has_doc_id", curie=REGISTRY.curie('docId'),
                   model_uri=REGISTRY.has_doc_id, domain=Provenance, range=Optional[str])

slots.has_primary_key = Slot(uri=REGISTRY.primaryKey, name="has_primary_key", curie=REGISTRY.curie('primaryKey'),
                   model_uri=REGISTRY.has_primary_key, domain=Provenance, range=Optional[str])

slots.has_ingest_target = Slot(uri=REGISTRY.ingestTarget, name="has_ingest_target", curie=REGISTRY.curie('ingestTarget'),
                   model_uri=REGISTRY.has_ingest_target, domain=Provenance, range=Optional[str])

slots.has_file_pattern = Slot(uri=REGISTRY.filePattern, name="has_file_pattern", curie=REGISTRY.curie('filePattern'),
                   model_uri=REGISTRY.has_file_pattern, domain=Provenance, range=Optional[str])

slots.has_relationship = Slot(uri=REGISTRY.relationships, name="has_relationship", curie=REGISTRY.curie('relationships'),
                   model_uri=REGISTRY.has_relationship, domain=Graph, range=Optional[Union[Union[dict, "Relationship"], List[Union[dict, "Relationship"]]]])

slots.has_child = Slot(uri=REGISTRY.child, name="has_child", curie=REGISTRY.curie('child'),
                   model_uri=REGISTRY.has_child, domain=Graph, range=Optional[Union[Union[dict, "ChildRelationship"], List[Union[dict, "ChildRelationship"]]]])

slots.has_parent = Slot(uri=REGISTRY.parent, name="has_parent", curie=REGISTRY.curie('parent'),
                   model_uri=REGISTRY.has_parent, domain=Graph, range=Optional[Union[Union[dict, "ParentRelationship"], List[Union[dict, "ParentRelationship"]]]])

slots.has_related = Slot(uri=REGISTRY.related, name="has_related", curie=REGISTRY.curie('related'),
                   model_uri=REGISTRY.has_related, domain=Graph, range=Optional[Union[Union[dict, "RelatedRelationship"], List[Union[dict, "RelatedRelationship"]]]])

slots.relates_to = Slot(uri=REGISTRY.resource, name="relates_to", curie=REGISTRY.curie('resource'),
                   model_uri=REGISTRY.relates_to, domain=Relationship, range=Optional[Union[dict, "RelatedResource"]])

slots.has_relationship_type = Slot(uri=REGISTRY.relationship, name="has_relationship_type", curie=REGISTRY.curie('relationship'),
                   model_uri=REGISTRY.has_relationship_type, domain=Relationship, range=Optional[Union[dict, "RelationshipType"]])

slots.has_identifier = Slot(uri=REGISTRY.identifier, name="has_identifier", curie=REGISTRY.curie('identifier'),
                   model_uri=REGISTRY.has_identifier, domain=RelatedResource, range=Optional[str])

slots.has_name = Slot(uri=REGISTRY.name, name="has_name", curie=REGISTRY.curie('name'),
                   model_uri=REGISTRY.has_name, domain=RelatedResource, range=Optional[str])

slots.has_name_children = Slot(uri=REGISTRY.name, name="has_name_children", curie=REGISTRY.curie('name'),
                   model_uri=REGISTRY.has_name_children, domain=Children, range=Optional[str])

slots.has_name_descendent = Slot(uri=REGISTRY.name, name="has_name_descendent", curie=REGISTRY.curie('name'),
                   model_uri=REGISTRY.has_name_descendent, domain=Descendants, range=Optional[str])

slots.has_name_ancestors = Slot(uri=REGISTRY.name, name="has_name_ancestors", curie=REGISTRY.curie('name'),
                   model_uri=REGISTRY.has_name_ancestors, domain=Ancestors, range=Optional[str])

slots.has_name_parent = Slot(uri=REGISTRY.name, name="has_name_parent", curie=REGISTRY.curie('name'),
                   model_uri=REGISTRY.has_name_parent, domain=Parent, range=Optional[str])

slots.has_name_license = Slot(uri=REGISTRY.name, name="has_name_license", curie=REGISTRY.curie('name'),
                   model_uri=REGISTRY.has_name_license, domain=License, range=Optional[str])

slots.has_name_validation = Slot(uri=REGISTRY.name, name="has_name_validation", curie=REGISTRY.curie('name'),
                   model_uri=REGISTRY.has_name_validation, domain=ValidationSitesInformation, range=Optional[str])

slots.has_name_species = Slot(uri=REGISTRY.name, name="has_name_species", curie=REGISTRY.curie('name'),
                   model_uri=REGISTRY.has_name_species, domain=Species, range=Optional[str])

slots.has_related_disease = Slot(uri=REGISTRY.related, name="has_related_disease", curie=REGISTRY.curie('related'),
                   model_uri=REGISTRY.has_related_disease, domain=Diseases, range=Optional[Union[Union[dict, "Disease"], List[Union[dict, "Disease"]]]])

slots.has_role_disease = Slot(uri=REGISTRY.role, name="has_role_disease", curie=REGISTRY.curie('role'),
                   model_uri=REGISTRY.has_role_disease, domain=Disease, range=Optional[str])

slots.has_role_organism = Slot(uri=REGISTRY.role, name="has_role_organism", curie=REGISTRY.curie('role'),
                   model_uri=REGISTRY.has_role_organism, domain=Organism, range=Optional[str])

slots.has_total_resource_mentions = Slot(uri=REGISTRY.totalResourceMentions, name="has_total_resource_mentions", curie=REGISTRY.curie('totalResourceMentions'),
                   model_uri=REGISTRY.has_total_resource_mentions, domain=Mentions, range=Optional[Union[dict, "TotalResourceMentions"]])

slots.has_total_rrid_mentions = Slot(uri=REGISTRY.totalRRIDMentions, name="has_total_rrid_mentions", curie=REGISTRY.curie('totalRRIDMentions'),
                   model_uri=REGISTRY.has_total_rrid_mentions, domain=Mentions, range=Optional[Union[dict, "TotalRRIDMentions"]])

slots.has_total_mentions = Slot(uri=REGISTRY.totalMentions, name="has_total_mentions", curie=REGISTRY.curie('totalMentions'),
                   model_uri=REGISTRY.has_total_mentions, domain=Mentions, range=Optional[Union[dict, "TotalMentions"]])

slots.has_mention_timestamp = Slot(uri=REGISTRY.timestamp, name="has_mention_timestamp", curie=REGISTRY.curie('timestamp'),
                   model_uri=REGISTRY.has_mention_timestamp, domain=Mentions, range=Optional[str])

slots.has_availability_2 = Slot(uri=REGISTRY.availability, name="has_availability_2", curie=REGISTRY.curie('availability'),
                   model_uri=REGISTRY.has_availability_2, domain=Mentions, range=Optional[Union[dict, "Availability2"]])

slots.has_count = Slot(uri=REGISTRY.count, name="has_count", curie=REGISTRY.curie('count'),
                   model_uri=REGISTRY.has_count, domain=TotalResourceMentions, range=Optional[int])

slots.has_count_resourcemention = Slot(uri=REGISTRY.count, name="has_count_resourcemention", curie=REGISTRY.curie('count'),
                   model_uri=REGISTRY.has_count_resourcemention, domain=TotalResourceMentions, range=Optional[int])

slots.has_count_rridmention = Slot(uri=REGISTRY.count, name="has_count_rridmention", curie=REGISTRY.curie('count'),
                   model_uri=REGISTRY.has_count_rridmention, domain=TotalRRIDMentions, range=Optional[int])

slots.has_count_mentiona = Slot(uri=REGISTRY.count, name="has_count_mentiona", curie=REGISTRY.curie('count'),
                   model_uri=REGISTRY.has_count_mentiona, domain=TotalMentions, range=Optional[int])

slots.has_count_countvalue = Slot(uri=REGISTRY.count, name="has_count_countvalue", curie=REGISTRY.curie('count'),
                   model_uri=REGISTRY.has_count_countvalue, domain=CountValue, range=Optional[int])

slots.has_count_issue = Slot(uri=REGISTRY.count, name="has_count_issue", curie=REGISTRY.curie('count'),
                   model_uri=REGISTRY.has_count_issue, domain=TotalIssues, range=Optional[int])

slots.has_keyword_2 = Slot(uri=REGISTRY.keyword, name="has_keyword_2", curie=REGISTRY.curie('keyword'),
                   model_uri=REGISTRY.has_keyword_2, domain=Availability2, range=Optional[str])

slots.has_license = Slot(uri=REGISTRY.license, name="has_license", curie=REGISTRY.curie('license'),
                   model_uri=REGISTRY.has_license, domain=Legal, range=Optional[Union[dict, "License"]])

slots.has_terms = Slot(uri=REGISTRY.terms, name="has_terms", curie=REGISTRY.curie('terms'),
                   model_uri=REGISTRY.has_terms, domain=Legal, range=Optional[Union[dict, "Terms"]])

slots.has_uris = Slot(uri=REGISTRY.uris, name="has_uris", curie=REGISTRY.curie('uris'),
                   model_uri=REGISTRY.has_uris, domain=Terms, range=Optional[Union[str, List[str]]])

slots.has_total_issues = Slot(uri=REGISTRY.totalIssues, name="has_total_issues", curie=REGISTRY.curie('totalIssues'),
                   model_uri=REGISTRY.has_total_issues, domain=Issues, range=Optional[Union[dict, "TotalIssues"]])

slots.has_status = Slot(uri=REGISTRY.status, name="has_status", curie=REGISTRY.curie('status'),
                   model_uri=REGISTRY.has_status, domain=Issues, range=Optional[Union[str, List[str]]])

slots.has_direct_issues = Slot(uri=REGISTRY.direct, name="has_direct_issues", curie=REGISTRY.curie('direct'),
                   model_uri=REGISTRY.has_direct_issues, domain=Issues, range=Optional[Union[Union[dict, "Direct"], List[Union[dict, "Direct"]]]])

slots.has_comments = Slot(uri=REGISTRY.comments, name="has_comments", curie=REGISTRY.curie('comments'),
                   model_uri=REGISTRY.has_comments, domain=Direct, range=Optional[str])

slots.has_comments_validation = Slot(uri=REGISTRY.comments, name="has_comments_validation", curie=REGISTRY.curie('comments'),
                   model_uri=REGISTRY.has_comments_validation, domain=ValidationSitesInformation, range=Optional[str])

slots.has_issue = Slot(uri=REGISTRY.issue, name="has_issue", curie=REGISTRY.curie('issue'),
                   model_uri=REGISTRY.has_issue, domain=Direct, range=Optional[str])

slots.has_is_validated = Slot(uri=REGISTRY.isValidated, name="has_is_validated", curie=REGISTRY.curie('isValidated'),
                   model_uri=REGISTRY.has_is_validated, domain=Validation, range=Optional[Union[bool, Bool]])

slots.has_total_validation_sites = Slot(uri=REGISTRY.totalValidationSites, name="has_total_validation_sites", curie=REGISTRY.curie('totalValidationSites'),
                   model_uri=REGISTRY.has_total_validation_sites, domain=Validation, range=Optional[Union[dict, "CountValue"]])

slots.has_validation_sites_info = Slot(uri=REGISTRY.validationSitesInformation, name="has_validation_sites_info", curie=REGISTRY.curie('validationSitesInformation'),
                   model_uri=REGISTRY.has_validation_sites_info, domain=Validation, range=Optional[Union[Union[dict, "ValidationSitesInformation"], List[Union[dict, "ValidationSitesInformation"]]]])

slots.has_provider_id = Slot(uri=REGISTRY.provider_id, name="has_provider_id", curie=REGISTRY.curie('provider_id'),
                   model_uri=REGISTRY.has_provider_id, domain=ValidationSitesInformation, range=Optional[str])

slots.has_uri = Slot(uri=REGISTRY.uri, name="has_uri", curie=REGISTRY.curie('uri'),
                   model_uri=REGISTRY.has_uri, domain=ValidationSitesInformation, range=Optional[str])

slots.has_related_organism = Slot(uri=REGISTRY.related, name="has_related_organism", curie=REGISTRY.curie('related'),
                   model_uri=REGISTRY.has_related_organism, domain=Organisms, range=Optional[Union[Union[dict, "Organism"], List[Union[dict, "Organism"]]]])

slots.has_species = Slot(uri=REGISTRY.species, name="has_species", curie=REGISTRY.curie('species'),
                   model_uri=REGISTRY.has_species, domain=Organism, range=Optional[Union[dict, "Species"]])

slots.is_child_of = Slot(uri=REGISTRY.is_child_of, name="is_child_of", curie=REGISTRY.curie('is_child_of'),
                   model_uri=REGISTRY.is_child_of, domain=Children, range=Optional[Union[Union[dict, Hierarchy], List[Union[dict, Hierarchy]]]])

slots.is_descendant_of = Slot(uri=REGISTRY.is_descendant_of, name="is_descendant_of", curie=REGISTRY.curie('is_descendant_of'),
                   model_uri=REGISTRY.is_descendant_of, domain=Descendants, range=Optional[Union[Union[dict, Hierarchy], List[Union[dict, Hierarchy]]]])

slots.is_ancestor_of = Slot(uri=REGISTRY.is_ancestor_of, name="is_ancestor_of", curie=REGISTRY.curie('is_ancestor_of'),
                   model_uri=REGISTRY.is_ancestor_of, domain=Ancestors, range=Optional[Union[Union[dict, Hierarchy], List[Union[dict, Hierarchy]]]])

slots.is_parent_of = Slot(uri=REGISTRY.is_parent_of, name="is_parent_of", curie=REGISTRY.curie('is_parent_of'),
                   model_uri=REGISTRY.is_parent_of, domain=Parent, range=Optional[Union[Union[dict, Hierarchy], List[Union[dict, Hierarchy]]]])

slots.is_related_to = Slot(uri=REGISTRY.is_related_to, name="is_related_to", curie=REGISTRY.curie('is_related_to'),
                   model_uri=REGISTRY.is_related_to, domain=RelatedResource, range=Optional[Union[Union[dict, Graph], List[Union[dict, Graph]]]])

slots.is_related_by = Slot(uri=REGISTRY.is_related_by, name="is_related_by", curie=REGISTRY.curie('is_related_by'),
                   model_uri=REGISTRY.is_related_by, domain=RelatedResource, range=Optional[Union[dict, Relationship]])

slots.has_item = Slot(uri=REGISTRY.item, name="has_item", curie=REGISTRY.curie('item'),
                   model_uri=REGISTRY.has_item, domain=ResourceSource, range=Union[dict, "Item"])

slots.has_authority = Slot(uri=REGISTRY.authority, name="has_authority", curie=REGISTRY.curie('authority'),
                   model_uri=REGISTRY.has_authority, domain=ResourceSource, range=Optional[Union[dict, "Authority"]])

slots.has_distributions = Slot(uri=REGISTRY.distributions, name="has_distributions", curie=REGISTRY.curie('distributions'),
                   model_uri=REGISTRY.has_distributions, domain=ResourceSource, range=Optional[Union[dict, "Distributions"]])

slots.has_rrid = Slot(uri=REGISTRY.rrid, name="has_rrid", curie=REGISTRY.curie('rrid'),
                   model_uri=REGISTRY.has_rrid, domain=ResourceSource, range=Optional[Union[dict, "RRID"]])

slots.has_provenance = Slot(uri=REGISTRY.provenance, name="has_provenance", curie=REGISTRY.curie('provenance'),
                   model_uri=REGISTRY.has_provenance, domain=ResourceSource, range=Optional[Union[dict, "Provenance"]])

slots.has_disco = Slot(uri=REGISTRY.disco, name="has_disco", curie=REGISTRY.curie('disco'),
                   model_uri=REGISTRY.has_disco, domain=ResourceSource, range=Optional[Union[dict, "Disco"]])

slots.has_graph = Slot(uri=REGISTRY.graph, name="has_graph", curie=REGISTRY.curie('graph'),
                   model_uri=REGISTRY.has_graph, domain=ResourceSource, range=Optional[Union[dict, "Graph"]])

slots.has_diseases = Slot(uri=REGISTRY.diseases, name="has_diseases", curie=REGISTRY.curie('diseases'),
                   model_uri=REGISTRY.has_diseases, domain=ResourceSource, range=Optional[Union[dict, "Diseases"]])

slots.has_supportingAwards = Slot(uri=REGISTRY.supportingAwards, name="has_supportingAwards", curie=REGISTRY.curie('supportingAwards'),
                   model_uri=REGISTRY.has_supportingAwards, domain=ResourceSource, range=Optional[Union[Union[dict, "SupportingAwards"], List[Union[dict, "SupportingAwards"]]]])

slots.has_references = Slot(uri=REGISTRY.references, name="has_references", curie=REGISTRY.curie('references'),
                   model_uri=REGISTRY.has_references, domain=ResourceSource, range=Optional[Union[Union[dict, "References"], List[Union[dict, "References"]]]])

slots.has_organisms = Slot(uri=REGISTRY.organisms, name="has_organisms", curie=REGISTRY.curie('organisms'),
                   model_uri=REGISTRY.has_organisms, domain=ResourceSource, range=Optional[Union[dict, "Organisms"]])

slots.has_dataItem = Slot(uri=REGISTRY.dataItem, name="has_dataItem", curie=REGISTRY.curie('dataItem'),
                   model_uri=REGISTRY.has_dataItem, domain=ResourceSource, range=Optional[Union[dict, "DataItem"]])

slots.has_mentions = Slot(uri=REGISTRY.mentions, name="has_mentions", curie=REGISTRY.curie('mentions'),
                   model_uri=REGISTRY.has_mentions, domain=ResourceSource, range=Optional[Union[Union[dict, "Mentions"], List[Union[dict, "Mentions"]]]])

slots.has_organization = Slot(uri=REGISTRY.organization, name="has_organization", curie=REGISTRY.curie('organization'),
                   model_uri=REGISTRY.has_organization, domain=ResourceSource, range=Optional[Union[dict, "Organization"]])

slots.has_recordValid = Slot(uri=REGISTRY.recordValid, name="has_recordValid", curie=REGISTRY.curie('recordValid'),
                   model_uri=REGISTRY.has_recordValid, domain=ResourceSource, range=Optional[Union[bool, Bool]])

slots.has_legal = Slot(uri=REGISTRY.legal, name="has_legal", curie=REGISTRY.curie('legal'),
                   model_uri=REGISTRY.has_legal, domain=ResourceSource, range=Optional[Union[dict, "Legal"]])

slots.has_issues = Slot(uri=REGISTRY.issues, name="has_issues", curie=REGISTRY.curie('issues'),
                   model_uri=REGISTRY.has_issues, domain=ResourceSource, range=Optional[Union[dict, "Issues"]])

slots.has_validation = Slot(uri=REGISTRY.validation, name="has_validation", curie=REGISTRY.curie('validation'),
                   model_uri=REGISTRY.has_validation, domain=ResourceSource, range=Optional[Union[dict, "Validation"]])

slots.has_agency = Slot(uri=REGISTRY.agency, name="has_agency", curie=REGISTRY.curie('agency'),
                   model_uri=REGISTRY.has_agency, domain=SupportingAwards, range=Optional[Union[dict, "Agency"]])

slots.has_name_agency = Slot(uri=REGISTRY.name, name="has_name_agency", curie=REGISTRY.curie('name'),
                   model_uri=REGISTRY.has_name_agency, domain=Agency, range=Optional[str])

slots.has_identifier_agency = Slot(uri=REGISTRY.identifier, name="has_identifier_agency", curie=REGISTRY.curie('identifier'),
                   model_uri=REGISTRY.has_identifier_agency, domain=Agency, range=Optional[str])

slots.item__name = Slot(uri=REGISTRY.name, name="item__name", curie=REGISTRY.curie('name'),
                   model_uri=REGISTRY.item__name, domain=None, range=Optional[str])

slots.item__description = Slot(uri=REGISTRY.description, name="item__description", curie=REGISTRY.curie('description'),
                   model_uri=REGISTRY.item__description, domain=None, range=Optional[str])

slots.item__language = Slot(uri=REGISTRY.language, name="item__language", curie=REGISTRY.curie('language'),
                   model_uri=REGISTRY.item__language, domain=None, range=Optional[str])

slots.item__identifier = Slot(uri=REGISTRY.identifier, name="item__identifier", curie=REGISTRY.curie('identifier'),
                   model_uri=REGISTRY.item__identifier, domain=None, range=Optional[str])

slots.item__docid = Slot(uri=REGISTRY.docid, name="item__docid", curie=REGISTRY.curie('docid'),
                   model_uri=REGISTRY.item__docid, domain=None, range=Optional[str])

slots.item__uuid = Slot(uri=REGISTRY.uuid, name="item__uuid", curie=REGISTRY.curie('uuid'),
                   model_uri=REGISTRY.item__uuid, domain=None, range=Optional[str])

slots.item__curie = Slot(uri=REGISTRY.curie, name="item__curie", curie=REGISTRY.curie('curie'),
                   model_uri=REGISTRY.item__curie, domain=None, range=str)

slots.keyword__keyword = Slot(uri=REGISTRY.keyword, name="keyword__keyword", curie=REGISTRY.curie('keyword'),
                   model_uri=REGISTRY.keyword__keyword, domain=None, range=Optional[str])

slots.alternateIdentifier__identifier = Slot(uri=REGISTRY.identifier, name="alternateIdentifier__identifier", curie=REGISTRY.curie('identifier'),
                   model_uri=REGISTRY.alternateIdentifier__identifier, domain=None, range=Optional[str])

slots.abbreviation__name = Slot(uri=REGISTRY.name, name="abbreviation__name", curie=REGISTRY.curie('name'),
                   model_uri=REGISTRY.abbreviation__name, domain=None, range=Optional[str])

slots.authority__name = Slot(uri=REGISTRY.name, name="authority__name", curie=REGISTRY.curie('name'),
                   model_uri=REGISTRY.authority__name, domain=None, range=Optional[str])

slots.supercategory__name = Slot(uri=REGISTRY.name, name="supercategory__name", curie=REGISTRY.curie('name'),
                   model_uri=REGISTRY.supercategory__name, domain=None, range=Optional[str])

slots.supercategory__type = Slot(uri=REGISTRY.type, name="supercategory__type", curie=REGISTRY.curie('type'),
                   model_uri=REGISTRY.supercategory__type, domain=None, range=Optional[str])

slots.contentType__curie = Slot(uri=REGISTRY.curie, name="contentType__curie", curie=REGISTRY.curie('curie'),
                   model_uri=REGISTRY.contentType__curie, domain=None, range=Optional[str])

slots.contentType__name = Slot(uri=REGISTRY.name, name="contentType__name", curie=REGISTRY.curie('name'),
                   model_uri=REGISTRY.contentType__name, domain=None, range=Optional[str])

slots.synonym__name = Slot(uri=REGISTRY.name, name="synonym__name", curie=REGISTRY.curie('name'),
                   model_uri=REGISTRY.synonym__name, domain=None, range=Optional[str])

slots.type__name = Slot(uri=REGISTRY.name, name="type__name", curie=REGISTRY.curie('name'),
                   model_uri=REGISTRY.type__name, domain=None, range=Optional[str])

slots.type__type = Slot(uri=REGISTRY.type, name="type__type", curie=REGISTRY.curie('type'),
                   model_uri=REGISTRY.type__type, domain=None, range=Optional[str])

slots.availability__description = Slot(uri=REGISTRY.description, name="availability__description", curie=REGISTRY.curie('description'),
                   model_uri=REGISTRY.availability__description, domain=None, range=Optional[str])

slots.availability__keyword = Slot(uri=REGISTRY.keyword, name="availability__keyword", curie=REGISTRY.curie('keyword'),
                   model_uri=REGISTRY.availability__keyword, domain=None, range=Optional[str])

slots.uRLReference__type = Slot(uri=REGISTRY.type, name="uRLReference__type", curie=REGISTRY.curie('type'),
                   model_uri=REGISTRY.uRLReference__type, domain=None, range=Optional[str])

slots.uRLReference__uri = Slot(uri=REGISTRY.uri, name="uRLReference__uri", curie=REGISTRY.curie('uri'),
                   model_uri=REGISTRY.uRLReference__uri, domain=None, range=Optional[str])

slots.disco__v_uuid = Slot(uri=REGISTRY.v_uuid, name="disco__v_uuid", curie=REGISTRY.curie('v_uuid'),
                   model_uri=REGISTRY.disco__v_uuid, domain=None, range=Optional[str])

slots.disease__name = Slot(uri=REGISTRY.name, name="disease__name", curie=REGISTRY.curie('name'),
                   model_uri=REGISTRY.disease__name, domain=None, range=Optional[str])

slots.references__curie = Slot(uri=REGISTRY.curie, name="references__curie", curie=REGISTRY.curie('curie'),
                   model_uri=REGISTRY.references__curie, domain=None, range=Optional[str])

slots.dataItem__dataTypes = Slot(uri=REGISTRY.dataTypes, name="dataItem__dataTypes", curie=REGISTRY.curie('dataTypes'),
                   model_uri=REGISTRY.dataItem__dataTypes, domain=None, range=Optional[Union[str, List[str]]])
