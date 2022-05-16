# Auto generated from vrsatile.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-05-16T16:31:06
# Schema: vrsatile
#
# id: https://example.org/vrsatile
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
GA4GHCATEGORICALVARIATIONDEFINITIONS = CurieNamespace('GA4GHCategoricalVariationDefinitions', 'https://example.org/GA4GH-Categorical-Variation-Definitions')
GA4GHVRSDEFINITIONS = CurieNamespace('GA4GHVRSDefinitions', 'https://example.org/GA4GHVRSDefinitions')
GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS = CurieNamespace('GA4GHValueObjectDescriptorDefinitions', 'https://example.org/GA4GHValueObjectDescriptorDefinitions')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
VRSATILE = CurieNamespace('vrsatile', 'https://example.org/vrsatile')
DEFAULT_ = VRSATILE


# Types

# Class references



class CategoricalVariation(YAMLRoot):
    """
    A representation of a categorically-defined [functional
    domain](https://en.wikipedia.org/wiki/Domain_of_a_function) for variation, in which individual variation instances
    may be members.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHCATEGORICALVARIATIONDEFINITIONS.CategoricalVariation
    class_class_curie: ClassVar[str] = "GA4GHCategoricalVariationDefinitions:CategoricalVariation"
    class_name: ClassVar[str] = "CategoricalVariation"
    class_model_uri: ClassVar[URIRef] = VRSATILE.CategoricalVariation


@dataclass
class ComplexVariation(YAMLRoot):
    """
    A categorical variation domain jointly characterized by two or more other categorical  variation domains.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHCATEGORICALVARIATIONDEFINITIONS.ComplexVariation
    class_class_curie: ClassVar[str] = "GA4GHCategoricalVariationDefinitions:ComplexVariation"
    class_name: ClassVar[str] = "ComplexVariation"
    class_model_uri: ClassVar[URIRef] = VRSATILE.ComplexVariation

    catvars_type: str = None
    operands: Union[Union[dict, CategoricalVariation], List[Union[dict, CategoricalVariation]]] = None
    operator: Union[str, "OperatorOptions"] = None
    catvars_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.catvars_type):
            self.MissingRequiredField("catvars_type")
        if not isinstance(self.catvars_type, str):
            self.catvars_type = str(self.catvars_type)

        if self._is_empty(self.operands):
            self.MissingRequiredField("operands")
        if not isinstance(self.operands, list):
            self.operands = [self.operands] if self.operands is not None else []
        self.operands = [v if isinstance(v, CategoricalVariation) else CategoricalVariation(**as_dict(v)) for v in self.operands]

        if self._is_empty(self.operator):
            self.MissingRequiredField("operator")
        if not isinstance(self.operator, OperatorOptions):
            self.operator = OperatorOptions(self.operator)

        if self.catvars_id is not None and not isinstance(self.catvars_id, str):
            self.catvars_id = str(self.catvars_id)

        super().__post_init__(**kwargs)


@dataclass
class CanonicalVariation(YAMLRoot):
    """
    A categorical variation domain characterized by a representative Variation context to which members lift-over,
    project, translate, or otherwise directly align.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHCATEGORICALVARIATIONDEFINITIONS.CanonicalVariation
    class_class_curie: ClassVar[str] = "GA4GHCategoricalVariationDefinitions:CanonicalVariation"
    class_name: ClassVar[str] = "CanonicalVariation"
    class_model_uri: ClassVar[URIRef] = VRSATILE.CanonicalVariation

    catvars_type: str = None
    variation: Union[dict, "Variation"] = None
    catvars_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.catvars_type):
            self.MissingRequiredField("catvars_type")
        if not isinstance(self.catvars_type, str):
            self.catvars_type = str(self.catvars_type)

        if self._is_empty(self.variation):
            self.MissingRequiredField("variation")
        if not isinstance(self.variation, Variation):
            self.variation = Variation()

        if self.catvars_id is not None and not isinstance(self.catvars_id, str):
            self.catvars_id = str(self.catvars_id)

        super().__post_init__(**kwargs)


class Variation(YAMLRoot):
    """
    A representation of the state of one or more biomolecules.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Variation
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:Variation"
    class_name: ClassVar[str] = "Variation"
    class_model_uri: ClassVar[URIRef] = VRSATILE.Variation


class MolecularVariation(YAMLRoot):
    """
    A variation on a contiguous molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.MolecularVariation
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:MolecularVariation"
    class_name: ClassVar[str] = "MolecularVariation"
    class_model_uri: ClassVar[URIRef] = VRSATILE.MolecularVariation


class UtilityVariation(YAMLRoot):
    """
    A collection of Variation subclasses that cannot be constrained to a specific class of biological variation, but
    are necessary for some applications of VRS.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.UtilityVariation
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:UtilityVariation"
    class_name: ClassVar[str] = "UtilityVariation"
    class_model_uri: ClassVar[URIRef] = VRSATILE.UtilityVariation


class SystemicVariation(YAMLRoot):
    """
    A Variation of multiple molecules in the context of a system, e.g. a genome, sample, or homologous chromosomes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.SystemicVariation
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:SystemicVariation"
    class_name: ClassVar[str] = "SystemicVariation"
    class_model_uri: ClassVar[URIRef] = VRSATILE.SystemicVariation


@dataclass
class Allele(YAMLRoot):
    """
    The state of a molecule at a Location.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Allele
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:Allele"
    class_name: ClassVar[str] = "Allele"
    class_model_uri: ClassVar[URIRef] = VRSATILE.Allele

    type: str = None
    location: Union[dict, "SequenceLocation"] = None
    state: str = None
    _id: Optional[Union[dict, "CURIE"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.location):
            self.MissingRequiredField("location")
        if not isinstance(self.location, SequenceLocation):
            self.location = SequenceLocation(**as_dict(self.location))

        if self._is_empty(self.state):
            self.MissingRequiredField("state")
        if not isinstance(self.state, str):
            self.state = str(self.state)

        if self._id is not None and not isinstance(self._id, CURIE):
            self._id = CURIE()

        super().__post_init__(**kwargs)


@dataclass
class Haplotype(YAMLRoot):
    """
    A set of non-overlapping Allele members that co-occur on the same molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Haplotype
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:Haplotype"
    class_name: ClassVar[str] = "Haplotype"
    class_model_uri: ClassVar[URIRef] = VRSATILE.Haplotype

    type: str = None
    members: Union[str, List[str]] = None
    _id: Optional[Union[dict, "CURIE"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.members):
            self.MissingRequiredField("members")
        if not isinstance(self.members, list):
            self.members = [self.members] if self.members is not None else []
        self.members = [v if isinstance(v, str) else str(v) for v in self.members]

        if self._id is not None and not isinstance(self._id, CURIE):
            self._id = CURIE()

        super().__post_init__(**kwargs)


@dataclass
class Text(YAMLRoot):
    """
    A free-text definition of variation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Text
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:Text"
    class_name: ClassVar[str] = "Text"
    class_model_uri: ClassVar[URIRef] = VRSATILE.Text

    type: str = None
    definition: str = None
    _id: Optional[Union[dict, "CURIE"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.definition):
            self.MissingRequiredField("definition")
        if not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self._id is not None and not isinstance(self._id, CURIE):
            self._id = CURIE()

        super().__post_init__(**kwargs)


@dataclass
class VariationSet(YAMLRoot):
    """
    An unconstrained set of Variation members.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.VariationSet
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:VariationSet"
    class_name: ClassVar[str] = "VariationSet"
    class_model_uri: ClassVar[URIRef] = VRSATILE.VariationSet

    type: str = None
    members: Union[str, List[str]] = None
    _id: Optional[Union[dict, "CURIE"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.members):
            self.MissingRequiredField("members")
        if not isinstance(self.members, list):
            self.members = [self.members] if self.members is not None else []
        self.members = [v if isinstance(v, str) else str(v) for v in self.members]

        if self._id is not None and not isinstance(self._id, CURIE):
            self._id = CURIE()

        super().__post_init__(**kwargs)


@dataclass
class CopyNumber(YAMLRoot):
    """
    The absolute count of discrete copies of a MolecularVariation, Feature, SequenceExpression, or a CURIE reference
    within a system (e.g. genome, cell, etc.).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.CopyNumber
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:CopyNumber"
    class_name: ClassVar[str] = "CopyNumber"
    class_model_uri: ClassVar[URIRef] = VRSATILE.CopyNumber

    type: str = None
    subject: str = None
    copies: str = None
    _id: Optional[Union[dict, "CURIE"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self._is_empty(self.copies):
            self.MissingRequiredField("copies")
        if not isinstance(self.copies, str):
            self.copies = str(self.copies)

        if self._id is not None and not isinstance(self._id, CURIE):
            self._id = CURIE()

        super().__post_init__(**kwargs)


class Location(YAMLRoot):
    """
    A contiguous segment of a biological sequence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Location
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = VRSATILE.Location


@dataclass
class ChromosomeLocation(YAMLRoot):
    """
    A Location on a chromosome defined by a species and chromosome name.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.ChromosomeLocation
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:ChromosomeLocation"
    class_name: ClassVar[str] = "ChromosomeLocation"
    class_model_uri: ClassVar[URIRef] = VRSATILE.ChromosomeLocation

    type: str = None
    species_id: Union[dict, "CURIE"] = None
    chr: str = None
    interval: Union[dict, "CytobandInterval"] = None
    _id: Optional[Union[dict, "CURIE"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.species_id):
            self.MissingRequiredField("species_id")
        if not isinstance(self.species_id, CURIE):
            self.species_id = CURIE()

        if self._is_empty(self.chr):
            self.MissingRequiredField("chr")
        if not isinstance(self.chr, str):
            self.chr = str(self.chr)

        if self._is_empty(self.interval):
            self.MissingRequiredField("interval")
        if not isinstance(self.interval, CytobandInterval):
            self.interval = CytobandInterval(**as_dict(self.interval))

        if self._id is not None and not isinstance(self._id, CURIE):
            self._id = CURIE()

        super().__post_init__(**kwargs)


@dataclass
class SequenceLocation(YAMLRoot):
    """
    A Location defined by an interval on a referenced Sequence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.SequenceLocation
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:SequenceLocation"
    class_name: ClassVar[str] = "SequenceLocation"
    class_model_uri: ClassVar[URIRef] = VRSATILE.SequenceLocation

    type: str = None
    sequence_id: Union[dict, "CURIE"] = None
    interval: str = None
    _id: Optional[Union[dict, "CURIE"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.sequence_id):
            self.MissingRequiredField("sequence_id")
        if not isinstance(self.sequence_id, CURIE):
            self.sequence_id = CURIE()

        if self._is_empty(self.interval):
            self.MissingRequiredField("interval")
        if not isinstance(self.interval, str):
            self.interval = str(self.interval)

        if self._id is not None and not isinstance(self._id, CURIE):
            self._id = CURIE()

        super().__post_init__(**kwargs)


@dataclass
class SequenceInterval(YAMLRoot):
    """
    A SequenceInterval represents a span on a Sequence. Positions are always represented by contiguous spans using
    interbase coordinates or coordinate ranges.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.SequenceInterval
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:SequenceInterval"
    class_name: ClassVar[str] = "SequenceInterval"
    class_model_uri: ClassVar[URIRef] = VRSATILE.SequenceInterval

    type: str = None
    start: int = None
    end: int = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.start):
            self.MissingRequiredField("start")
        if not isinstance(self.start, int):
            self.start = int(self.start)

        if self._is_empty(self.end):
            self.MissingRequiredField("end")
        if not isinstance(self.end, int):
            self.end = int(self.end)

        super().__post_init__(**kwargs)


@dataclass
class CytobandInterval(YAMLRoot):
    """
    A contiguous span on a chromosome defined by cytoband features. The span includes the constituent regions
    described by the start and end cytobands, as well as any intervening regions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.CytobandInterval
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:CytobandInterval"
    class_name: ClassVar[str] = "CytobandInterval"
    class_model_uri: ClassVar[URIRef] = VRSATILE.CytobandInterval

    type: str = None
    start: Union[dict, "HumanCytoband"] = None
    end: Union[dict, "HumanCytoband"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.start):
            self.MissingRequiredField("start")
        if not isinstance(self.start, HumanCytoband):
            self.start = HumanCytoband()

        if self._is_empty(self.end):
            self.MissingRequiredField("end")
        if not isinstance(self.end, HumanCytoband):
            self.end = HumanCytoband()

        super().__post_init__(**kwargs)


class SequenceExpression(YAMLRoot):
    """
    An expression describing a Sequence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.SequenceExpression
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:SequenceExpression"
    class_name: ClassVar[str] = "SequenceExpression"
    class_model_uri: ClassVar[URIRef] = VRSATILE.SequenceExpression


@dataclass
class LiteralSequenceExpression(YAMLRoot):
    """
    An explicit expression of a Sequence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.LiteralSequenceExpression
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:LiteralSequenceExpression"
    class_name: ClassVar[str] = "LiteralSequenceExpression"
    class_model_uri: ClassVar[URIRef] = VRSATILE.LiteralSequenceExpression

    type: str = None
    sequence: Union[dict, "Sequence"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.sequence):
            self.MissingRequiredField("sequence")
        if not isinstance(self.sequence, Sequence):
            self.sequence = Sequence()

        super().__post_init__(**kwargs)


@dataclass
class DerivedSequenceExpression(YAMLRoot):
    """
    An approximate expression of a sequence that is derived from a referenced sequence location. Use of this class
    indicates that the derived sequence is *approximately equivalent* to the reference indicated, and is typically
    used for describing large regions in contexts where the use of an approximate sequence is inconsequential.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.DerivedSequenceExpression
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:DerivedSequenceExpression"
    class_name: ClassVar[str] = "DerivedSequenceExpression"
    class_model_uri: ClassVar[URIRef] = VRSATILE.DerivedSequenceExpression

    type: str = None
    location: Union[dict, SequenceLocation] = None
    reverse_complement: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.location):
            self.MissingRequiredField("location")
        if not isinstance(self.location, SequenceLocation):
            self.location = SequenceLocation(**as_dict(self.location))

        if self._is_empty(self.reverse_complement):
            self.MissingRequiredField("reverse_complement")
        if not isinstance(self.reverse_complement, Bool):
            self.reverse_complement = Bool(self.reverse_complement)

        super().__post_init__(**kwargs)


@dataclass
class RepeatedSequenceExpression(YAMLRoot):
    """
    An expression of a sequence comprised of a tandem repeating subsequence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.RepeatedSequenceExpression
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:RepeatedSequenceExpression"
    class_name: ClassVar[str] = "RepeatedSequenceExpression"
    class_model_uri: ClassVar[URIRef] = VRSATILE.RepeatedSequenceExpression

    type: str = None
    seq_expr: str = None
    count: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.seq_expr):
            self.MissingRequiredField("seq_expr")
        if not isinstance(self.seq_expr, str):
            self.seq_expr = str(self.seq_expr)

        if self._is_empty(self.count):
            self.MissingRequiredField("count")
        if not isinstance(self.count, str):
            self.count = str(self.count)

        super().__post_init__(**kwargs)


@dataclass
class ComposedSequenceExpression(YAMLRoot):
    """
    An expression of a sequence composed from multiple other Sequence Expressions objects. MUST have at least one
    component that is not a ref:`LiteralSequenceExpression`. CANNOT be composed from nested composed sequence
    expressions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.ComposedSequenceExpression
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:ComposedSequenceExpression"
    class_name: ClassVar[str] = "ComposedSequenceExpression"
    class_model_uri: ClassVar[URIRef] = VRSATILE.ComposedSequenceExpression

    type: str = None
    components: Union[str, List[str]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.components):
            self.MissingRequiredField("components")
        if not isinstance(self.components, list):
            self.components = [self.components] if self.components is not None else []
        self.components = [v if isinstance(v, str) else str(v) for v in self.components]

        super().__post_init__(**kwargs)


class Feature(YAMLRoot):
    """
    A named entity that can be mapped to a Location. Genes, protein domains, exons, and chromosomes are some examples
    of common biological entities that may be Features.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Feature
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:Feature"
    class_name: ClassVar[str] = "Feature"
    class_model_uri: ClassVar[URIRef] = VRSATILE.Feature


@dataclass
class Gene(YAMLRoot):
    """
    A reference to a Gene as defined by an authority. For human genes, the use of
    [hgnc](https://registry.identifiers.org/registry/hgnc) as the gene authority is RECOMMENDED.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Gene
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:Gene"
    class_name: ClassVar[str] = "Gene"
    class_model_uri: ClassVar[URIRef] = VRSATILE.Gene

    type: str = None
    gene_id: Union[dict, "CURIE"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.gene_id):
            self.MissingRequiredField("gene_id")
        if not isinstance(self.gene_id, CURIE):
            self.gene_id = CURIE()

        super().__post_init__(**kwargs)


@dataclass
class Number(YAMLRoot):
    """
    A simple integer value as a VRS class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Number
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:Number"
    class_name: ClassVar[str] = "Number"
    class_model_uri: ClassVar[URIRef] = VRSATILE.Number

    type: str = None
    value: int = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, int):
            self.value = int(self.value)

        super().__post_init__(**kwargs)


@dataclass
class DefiniteRange(YAMLRoot):
    """
    A bounded, inclusive range of numbers.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.DefiniteRange
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:DefiniteRange"
    class_name: ClassVar[str] = "DefiniteRange"
    class_model_uri: ClassVar[URIRef] = VRSATILE.DefiniteRange

    type: str = None
    min: float = None
    max: float = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.min):
            self.MissingRequiredField("min")
        if not isinstance(self.min, float):
            self.min = float(self.min)

        if self._is_empty(self.max):
            self.MissingRequiredField("max")
        if not isinstance(self.max, float):
            self.max = float(self.max)

        super().__post_init__(**kwargs)


@dataclass
class IndefiniteRange(YAMLRoot):
    """
    A half-bounded range of numbers represented as a number bound and associated comparator. The bound operator is
    interpreted as follows: '>=' are all numbers greater than and including `value`, '<=' are all numbers less than
    and including `value`.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.IndefiniteRange
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:IndefiniteRange"
    class_name: ClassVar[str] = "IndefiniteRange"
    class_model_uri: ClassVar[URIRef] = VRSATILE.IndefiniteRange

    type: str = None
    value: float = None
    comparator: Union[str, "ComparatorOptions"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, float):
            self.value = float(self.value)

        if self._is_empty(self.comparator):
            self.MissingRequiredField("comparator")
        if not isinstance(self.comparator, ComparatorOptions):
            self.comparator = ComparatorOptions(self.comparator)

        super().__post_init__(**kwargs)


class CURIE(YAMLRoot):
    """
    A [W3C Compact URI](https://www.w3.org/TR/curie/) formatted string. A CURIE string has the structure
    ``prefix``:``reference``, as defined by the W3C syntax.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.CURIE
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:CURIE"
    class_name: ClassVar[str] = "CURIE"
    class_model_uri: ClassVar[URIRef] = VRSATILE.CURIE


class HumanCytoband(YAMLRoot):
    """
    A character string representing cytobands derived from the *International System for Human Cytogenomic
    Nomenclature* (ISCN) [guidelines](http://doi.org/10.1159/isbn.978-3-318-06861-0).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.HumanCytoband
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:HumanCytoband"
    class_name: ClassVar[str] = "HumanCytoband"
    class_model_uri: ClassVar[URIRef] = VRSATILE.HumanCytoband


class Residue(YAMLRoot):
    """
    A character representing a specific residue (i.e., molecular species) or groupings of these ("ambiguity codes"),
    using [one-letter IUPAC
    abbreviations](https://en.wikipedia.org/wiki/International_Union_of_Pure_and_Applied_Chemistry#Amino_acid_and_nucleotide_base_codes)
    for nucleic acids and amino acids.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Residue
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:Residue"
    class_name: ClassVar[str] = "Residue"
    class_model_uri: ClassVar[URIRef] = VRSATILE.Residue


class Sequence(YAMLRoot):
    """
    A character string of Residues that represents a biological sequence using the conventional sequence order
    (5’-to-3’ for nucleic acid sequences, and amino-to-carboxyl for amino acid sequences). IUPAC ambiguity codes are
    permitted in Sequences.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.Sequence
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:Sequence"
    class_name: ClassVar[str] = "Sequence"
    class_model_uri: ClassVar[URIRef] = VRSATILE.Sequence


@dataclass
class SequenceState(YAMLRoot):
    """
    DEPRECATED. A Sequence as a State. This is the State class to use for representing "ref-alt" style variation,
    including SNVs, MNVs, del, ins, and delins. This class is deprecated. Use LiteralSequenceExpression instead.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.SequenceState
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:SequenceState"
    class_name: ClassVar[str] = "SequenceState"
    class_model_uri: ClassVar[URIRef] = VRSATILE.SequenceState

    type: str = None
    sequence: Union[dict, Sequence] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.sequence):
            self.MissingRequiredField("sequence")
        if not isinstance(self.sequence, Sequence):
            self.sequence = Sequence()

        super().__post_init__(**kwargs)


@dataclass
class SimpleInterval(YAMLRoot):
    """
    DEPRECATED: A SimpleInterval represents a span of sequence. Positions are always represented by contiguous spans
    using interbase coordinates. This class is deprecated. Use SequenceInterval instead.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVRSDEFINITIONS.SimpleInterval
    class_class_curie: ClassVar[str] = "GA4GHVRSDefinitions:SimpleInterval"
    class_name: ClassVar[str] = "SimpleInterval"
    class_model_uri: ClassVar[URIRef] = VRSATILE.SimpleInterval

    type: str = None
    start: int = None
    end: int = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.start):
            self.MissingRequiredField("start")
        if not isinstance(self.start, int):
            self.start = int(self.start)

        if self._is_empty(self.end):
            self.MissingRequiredField("end")
        if not isinstance(self.end, int):
            self.end = int(self.end)

        super().__post_init__(**kwargs)


class ValueObjectDescriptor(YAMLRoot):
    """
    The abstract *Value Object Descriptor* parent class. All attributes of this parent class are inherited by
    descendent classes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.ValueObjectDescriptor
    class_class_curie: ClassVar[str] = "GA4GHValueObjectDescriptorDefinitions:ValueObjectDescriptor"
    class_name: ClassVar[str] = "ValueObjectDescriptor"
    class_model_uri: ClassVar[URIRef] = VRSATILE.ValueObjectDescriptor


@dataclass
class VariationDescriptor(YAMLRoot):
    """
    This descriptor class is used for describing VRS Variation value objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.VariationDescriptor
    class_class_curie: ClassVar[str] = "GA4GHValueObjectDescriptorDefinitions:VariationDescriptor"
    class_name: ClassVar[str] = "VariationDescriptor"
    class_model_uri: ClassVar[URIRef] = VRSATILE.VariationDescriptor

    id: Union[dict, CURIE] = None
    vrs_type: Union[str, "TypeOptions"] = None
    variation: Union[dict, Variation] = None
    expressions: Union[Union[dict, "Expression"], List[Union[dict, "Expression"]]] = None
    label: Optional[str] = None
    description: Optional[str] = None
    xrefs: Optional[Union[Union[dict, CURIE], List[Union[dict, CURIE]]]] = empty_list()
    alternate_labels: Optional[Union[str, List[str]]] = empty_list()
    extensions: Optional[Union[Union[dict, "Extension"], List[Union[dict, "Extension"]]]] = empty_list()
    variation_id: Optional[Union[dict, CURIE]] = None
    molecule_context: Optional[Union[str, "MoleculeContextOptions"]] = None
    structural_type: Optional[Union[dict, CURIE]] = None
    vcf_record: Optional[Union[dict, "VcfRecord"]] = None
    gene_context: Optional[str] = None
    vrs_ref_allele_seq: Optional[Union[dict, Sequence]] = None
    allelic_state: Optional[Union[dict, CURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CURIE):
            self.id = CURIE()

        if self._is_empty(self.vrs_type):
            self.MissingRequiredField("vrs_type")
        if not isinstance(self.vrs_type, TypeOptions):
            self.vrs_type = TypeOptions(self.vrs_type)

        if self._is_empty(self.variation):
            self.MissingRequiredField("variation")
        if not isinstance(self.variation, Variation):
            self.variation = Variation()

        if self._is_empty(self.expressions):
            self.MissingRequiredField("expressions")
        self._normalize_inlined_as_dict(slot_name="expressions", slot_type=Expression, key_name="vrs_type", keyed=False)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.xrefs, list):
            self.xrefs = [self.xrefs] if self.xrefs is not None else []
        self.xrefs = [v if isinstance(v, CURIE) else CURIE(**as_dict(v)) for v in self.xrefs]

        if not isinstance(self.alternate_labels, list):
            self.alternate_labels = [self.alternate_labels] if self.alternate_labels is not None else []
        self.alternate_labels = [v if isinstance(v, str) else str(v) for v in self.alternate_labels]

        self._normalize_inlined_as_dict(slot_name="extensions", slot_type=Extension, key_name="vrs_type", keyed=False)

        if self.variation_id is not None and not isinstance(self.variation_id, CURIE):
            self.variation_id = CURIE()

        if self.molecule_context is not None and not isinstance(self.molecule_context, MoleculeContextOptions):
            self.molecule_context = MoleculeContextOptions(self.molecule_context)

        if self.structural_type is not None and not isinstance(self.structural_type, CURIE):
            self.structural_type = CURIE()

        if self.vcf_record is not None and not isinstance(self.vcf_record, VcfRecord):
            self.vcf_record = VcfRecord(**as_dict(self.vcf_record))

        if self.gene_context is not None and not isinstance(self.gene_context, str):
            self.gene_context = str(self.gene_context)

        if self.vrs_ref_allele_seq is not None and not isinstance(self.vrs_ref_allele_seq, Sequence):
            self.vrs_ref_allele_seq = Sequence()

        if self.allelic_state is not None and not isinstance(self.allelic_state, CURIE):
            self.allelic_state = CURIE()

        super().__post_init__(**kwargs)


@dataclass
class Extension(YAMLRoot):
    """
    The Extension class provides VODs with a means to extend descriptions with other attributes unique to a content
    provider. These extensions are not expected to be natively understood under VRSATILE, but may be used for
    pre-negotiated exchange of message attributes when needed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.Extension
    class_class_curie: ClassVar[str] = "GA4GHValueObjectDescriptorDefinitions:Extension"
    class_name: ClassVar[str] = "Extension"
    class_model_uri: ClassVar[URIRef] = VRSATILE.Extension

    vrs_type: str = None
    name: str = None
    vrs_value: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.vrs_type):
            self.MissingRequiredField("vrs_type")
        if not isinstance(self.vrs_type, str):
            self.vrs_type = str(self.vrs_type)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.vrs_value):
            self.MissingRequiredField("vrs_value")
        if not isinstance(self.vrs_value, str):
            self.vrs_value = str(self.vrs_value)

        super().__post_init__(**kwargs)


@dataclass
class Expression(YAMLRoot):
    """
    Representation of a variation by a specified nomenclature or syntax for a Variation object. Common examples of
    expressions for the description of molecular variation include the HGVS and ISCN nomenclatures.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.Expression
    class_class_curie: ClassVar[str] = "GA4GHValueObjectDescriptorDefinitions:Expression"
    class_name: ClassVar[str] = "Expression"
    class_model_uri: ClassVar[URIRef] = VRSATILE.Expression

    vrs_type: str = None
    syntax: Union[str, "SyntaxOptions"] = None
    vrs_value: str = None
    syntax_version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.vrs_type):
            self.MissingRequiredField("vrs_type")
        if not isinstance(self.vrs_type, str):
            self.vrs_type = str(self.vrs_type)

        if self._is_empty(self.syntax):
            self.MissingRequiredField("syntax")
        if not isinstance(self.syntax, SyntaxOptions):
            self.syntax = SyntaxOptions(self.syntax)

        if self._is_empty(self.vrs_value):
            self.MissingRequiredField("vrs_value")
        if not isinstance(self.vrs_value, str):
            self.vrs_value = str(self.vrs_value)

        if self.syntax_version is not None and not isinstance(self.syntax_version, str):
            self.syntax_version = str(self.syntax_version)

        super().__post_init__(**kwargs)


@dataclass
class CategoricalVariationDescriptor(YAMLRoot):
    """
    This descriptor class is used for describing Categorical Variation vrs_value objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.CategoricalVariationDescriptor
    class_class_curie: ClassVar[str] = "GA4GHValueObjectDescriptorDefinitions:CategoricalVariationDescriptor"
    class_name: ClassVar[str] = "CategoricalVariationDescriptor"
    class_model_uri: ClassVar[URIRef] = VRSATILE.CategoricalVariationDescriptor

    id: Union[dict, CURIE] = None
    vrs_type: str = None
    label: Optional[str] = None
    description: Optional[str] = None
    xrefs: Optional[Union[Union[dict, CURIE], List[Union[dict, CURIE]]]] = empty_list()
    alternate_labels: Optional[Union[str, List[str]]] = empty_list()
    extensions: Optional[Union[Union[dict, Extension], List[Union[dict, Extension]]]] = empty_list()
    version: Optional[str] = None
    categorical_variation_id: Optional[Union[dict, CURIE]] = None
    categorical_variation: Optional[Union[dict, CategoricalVariation]] = None
    vrs_members: Optional[Union[Union[dict, "VariationMember"], List[Union[dict, "VariationMember"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CURIE):
            self.id = CURIE()

        if self._is_empty(self.vrs_type):
            self.MissingRequiredField("vrs_type")
        if not isinstance(self.vrs_type, str):
            self.vrs_type = str(self.vrs_type)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.xrefs, list):
            self.xrefs = [self.xrefs] if self.xrefs is not None else []
        self.xrefs = [v if isinstance(v, CURIE) else CURIE(**as_dict(v)) for v in self.xrefs]

        if not isinstance(self.alternate_labels, list):
            self.alternate_labels = [self.alternate_labels] if self.alternate_labels is not None else []
        self.alternate_labels = [v if isinstance(v, str) else str(v) for v in self.alternate_labels]

        self._normalize_inlined_as_dict(slot_name="extensions", slot_type=Extension, key_name="vrs_type", keyed=False)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.categorical_variation_id is not None and not isinstance(self.categorical_variation_id, CURIE):
            self.categorical_variation_id = CURIE()

        if self.categorical_variation is not None and not isinstance(self.categorical_variation, CategoricalVariation):
            self.categorical_variation = CategoricalVariation()

        self._normalize_inlined_as_dict(slot_name="vrs_members", slot_type=VariationMember, key_name="expressions", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class VariationMember(YAMLRoot):
    """
    A compact class for representing a variation context that is a member of a Categorical Variation. It supports one
    or more Expressions of a Variation and optionally an associated VRS ID.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.VariationMember
    class_class_curie: ClassVar[str] = "GA4GHValueObjectDescriptorDefinitions:VariationMember"
    class_name: ClassVar[str] = "VariationMember"
    class_model_uri: ClassVar[URIRef] = VRSATILE.VariationMember

    expressions: Union[Union[dict, Expression], List[Union[dict, Expression]]] = None
    vrs_type: Optional[str] = None
    variation_id: Optional[Union[dict, CURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.expressions):
            self.MissingRequiredField("expressions")
        self._normalize_inlined_as_dict(slot_name="expressions", slot_type=Expression, key_name="vrs_type", keyed=False)

        if self.vrs_type is not None and not isinstance(self.vrs_type, str):
            self.vrs_type = str(self.vrs_type)

        if self.variation_id is not None and not isinstance(self.variation_id, CURIE):
            self.variation_id = CURIE()

        super().__post_init__(**kwargs)


@dataclass
class VcfRecord(YAMLRoot):
    """
    This data class is used when it is desirable to pass data as expected from a VCF record. The class is only used as
    an optional attribute within a VariationDescriptor. The Genotype field from a VCF should be captured by the
    `allelic_state` attribute in the Variation Descriptor.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.VcfRecord
    class_class_curie: ClassVar[str] = "GA4GHValueObjectDescriptorDefinitions:VcfRecord"
    class_name: ClassVar[str] = "VcfRecord"
    class_model_uri: ClassVar[URIRef] = VRSATILE.VcfRecord

    genome_assembly: str = None
    chrom: str = None
    pos: str = None
    ref: str = None
    alt: str = None
    id: Optional[str] = None
    qual: Optional[str] = None
    filter: Optional[str] = None
    info: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.genome_assembly):
            self.MissingRequiredField("genome_assembly")
        if not isinstance(self.genome_assembly, str):
            self.genome_assembly = str(self.genome_assembly)

        if self._is_empty(self.chrom):
            self.MissingRequiredField("chrom")
        if not isinstance(self.chrom, str):
            self.chrom = str(self.chrom)

        if self._is_empty(self.pos):
            self.MissingRequiredField("pos")
        if not isinstance(self.pos, str):
            self.pos = str(self.pos)

        if self._is_empty(self.ref):
            self.MissingRequiredField("ref")
        if not isinstance(self.ref, str):
            self.ref = str(self.ref)

        if self._is_empty(self.alt):
            self.MissingRequiredField("alt")
        if not isinstance(self.alt, str):
            self.alt = str(self.alt)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.qual is not None and not isinstance(self.qual, str):
            self.qual = str(self.qual)

        if self.filter is not None and not isinstance(self.filter, str):
            self.filter = str(self.filter)

        if self.info is not None and not isinstance(self.info, str):
            self.info = str(self.info)

        super().__post_init__(**kwargs)


# Enumerations
class OperatorOptions(EnumDefinitionImpl):

    AND = PermissibleValue(text="AND")
    OR = PermissibleValue(text="OR")

    _defn = EnumDefinition(
        name="OperatorOptions",
    )

class ComparatorOptions(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ComparatorOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "<=",
                PermissibleValue(text="<=") )
        setattr(cls, ">=",
                PermissibleValue(text=">=") )

class TypeOptions(EnumDefinitionImpl):

    VariationDescriptor = PermissibleValue(text="VariationDescriptor")

    _defn = EnumDefinition(
        name="TypeOptions",
    )

class MoleculeContextOptions(EnumDefinitionImpl):

    genomic = PermissibleValue(text="genomic")
    transcript = PermissibleValue(text="transcript")
    protein = PermissibleValue(text="protein")

    _defn = EnumDefinition(
        name="MoleculeContextOptions",
    )

class SyntaxOptions(EnumDefinitionImpl):

    iscn = PermissibleValue(text="iscn")
    gnomad = PermissibleValue(text="gnomad")
    spdi = PermissibleValue(text="spdi")

    _defn = EnumDefinition(
        name="SyntaxOptions",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "hgvs.c",
                PermissibleValue(text="hgvs.c") )
        setattr(cls, "hgvs.p",
                PermissibleValue(text="hgvs.p") )
        setattr(cls, "hgvs.g",
                PermissibleValue(text="hgvs.g") )
        setattr(cls, "hgvs.m",
                PermissibleValue(text="hgvs.m") )
        setattr(cls, "hgvs.n",
                PermissibleValue(text="hgvs.n") )
        setattr(cls, "hgvs.r",
                PermissibleValue(text="hgvs.r") )

# Slots
class slots:
    pass

slots.catvars_id = Slot(uri=GA4GHCATEGORICALVARIATIONDEFINITIONS.catvars_id, name="catvars_id", curie=GA4GHCATEGORICALVARIATIONDEFINITIONS.curie('catvars_id'),
                   model_uri=VRSATILE.catvars_id, domain=None, range=Optional[str])

slots.catvars_type = Slot(uri=GA4GHCATEGORICALVARIATIONDEFINITIONS.catvars_type, name="catvars_type", curie=GA4GHCATEGORICALVARIATIONDEFINITIONS.curie('catvars_type'),
                   model_uri=VRSATILE.catvars_type, domain=None, range=str)

slots.operands = Slot(uri=GA4GHCATEGORICALVARIATIONDEFINITIONS.operands, name="operands", curie=GA4GHCATEGORICALVARIATIONDEFINITIONS.curie('operands'),
                   model_uri=VRSATILE.operands, domain=None, range=Union[Union[dict, CategoricalVariation], List[Union[dict, CategoricalVariation]]])

slots.operator = Slot(uri=GA4GHCATEGORICALVARIATIONDEFINITIONS.operator, name="operator", curie=GA4GHCATEGORICALVARIATIONDEFINITIONS.curie('operator'),
                   model_uri=VRSATILE.operator, domain=None, range=Union[str, "OperatorOptions"])

slots.variation = Slot(uri=GA4GHCATEGORICALVARIATIONDEFINITIONS.variation, name="variation", curie=GA4GHCATEGORICALVARIATIONDEFINITIONS.curie('variation'),
                   model_uri=VRSATILE.variation, domain=None, range=Union[dict, Variation])

slots._id = Slot(uri=GA4GHVRSDEFINITIONS._id, name="_id", curie=GA4GHVRSDEFINITIONS.curie('_id'),
                   model_uri=VRSATILE._id, domain=None, range=Optional[Union[dict, CURIE]])

slots.type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=VRSATILE.type, domain=None, range=str)

slots.location = Slot(uri=GA4GHVRSDEFINITIONS.location, name="location", curie=GA4GHVRSDEFINITIONS.curie('location'),
                   model_uri=VRSATILE.location, domain=None, range=Union[dict, SequenceLocation])

slots.state = Slot(uri=GA4GHVRSDEFINITIONS.state, name="state", curie=GA4GHVRSDEFINITIONS.curie('state'),
                   model_uri=VRSATILE.state, domain=None, range=str)

slots.members = Slot(uri=GA4GHVRSDEFINITIONS.members, name="members", curie=GA4GHVRSDEFINITIONS.curie('members'),
                   model_uri=VRSATILE.members, domain=None, range=Union[str, List[str]])

slots.definition = Slot(uri=GA4GHVRSDEFINITIONS.definition, name="definition", curie=GA4GHVRSDEFINITIONS.curie('definition'),
                   model_uri=VRSATILE.definition, domain=None, range=str)

slots.subject = Slot(uri=GA4GHVRSDEFINITIONS.subject, name="subject", curie=GA4GHVRSDEFINITIONS.curie('subject'),
                   model_uri=VRSATILE.subject, domain=None, range=str)

slots.copies = Slot(uri=GA4GHVRSDEFINITIONS.copies, name="copies", curie=GA4GHVRSDEFINITIONS.curie('copies'),
                   model_uri=VRSATILE.copies, domain=None, range=str)

slots.species_id = Slot(uri=GA4GHVRSDEFINITIONS.species_id, name="species_id", curie=GA4GHVRSDEFINITIONS.curie('species_id'),
                   model_uri=VRSATILE.species_id, domain=None, range=Union[dict, CURIE])

slots.chr = Slot(uri=GA4GHVRSDEFINITIONS.chr, name="chr", curie=GA4GHVRSDEFINITIONS.curie('chr'),
                   model_uri=VRSATILE.chr, domain=None, range=str)

slots.interval = Slot(uri=GA4GHVRSDEFINITIONS.interval, name="interval", curie=GA4GHVRSDEFINITIONS.curie('interval'),
                   model_uri=VRSATILE.interval, domain=None, range=str)

slots.sequence_id = Slot(uri=GA4GHVRSDEFINITIONS.sequence_id, name="sequence_id", curie=GA4GHVRSDEFINITIONS.curie('sequence_id'),
                   model_uri=VRSATILE.sequence_id, domain=None, range=Union[dict, CURIE])

slots.start = Slot(uri=GA4GHVRSDEFINITIONS.start, name="start", curie=GA4GHVRSDEFINITIONS.curie('start'),
                   model_uri=VRSATILE.start, domain=None, range=int)

slots.end = Slot(uri=GA4GHVRSDEFINITIONS.end, name="end", curie=GA4GHVRSDEFINITIONS.curie('end'),
                   model_uri=VRSATILE.end, domain=None, range=int)

slots.sequence = Slot(uri=GA4GHVRSDEFINITIONS.sequence, name="sequence", curie=GA4GHVRSDEFINITIONS.curie('sequence'),
                   model_uri=VRSATILE.sequence, domain=None, range=Union[dict, Sequence])

slots.reverse_complement = Slot(uri=GA4GHVRSDEFINITIONS.reverse_complement, name="reverse_complement", curie=GA4GHVRSDEFINITIONS.curie('reverse_complement'),
                   model_uri=VRSATILE.reverse_complement, domain=None, range=Union[bool, Bool])

slots.seq_expr = Slot(uri=GA4GHVRSDEFINITIONS.seq_expr, name="seq_expr", curie=GA4GHVRSDEFINITIONS.curie('seq_expr'),
                   model_uri=VRSATILE.seq_expr, domain=None, range=str)

slots.count = Slot(uri=GA4GHVRSDEFINITIONS.count, name="count", curie=GA4GHVRSDEFINITIONS.curie('count'),
                   model_uri=VRSATILE.count, domain=None, range=str)

slots.components = Slot(uri=GA4GHVRSDEFINITIONS.components, name="components", curie=GA4GHVRSDEFINITIONS.curie('components'),
                   model_uri=VRSATILE.components, domain=None, range=Union[str, List[str]])

slots.gene_id = Slot(uri=GA4GHVRSDEFINITIONS.gene_id, name="gene_id", curie=GA4GHVRSDEFINITIONS.curie('gene_id'),
                   model_uri=VRSATILE.gene_id, domain=None, range=Union[dict, CURIE])

slots.value = Slot(uri=GA4GHVRSDEFINITIONS.value, name="value", curie=GA4GHVRSDEFINITIONS.curie('value'),
                   model_uri=VRSATILE.value, domain=None, range=float)

slots.min = Slot(uri=GA4GHVRSDEFINITIONS.min, name="min", curie=GA4GHVRSDEFINITIONS.curie('min'),
                   model_uri=VRSATILE.min, domain=None, range=float)

slots.max = Slot(uri=GA4GHVRSDEFINITIONS.max, name="max", curie=GA4GHVRSDEFINITIONS.curie('max'),
                   model_uri=VRSATILE.max, domain=None, range=float)

slots.comparator = Slot(uri=GA4GHVRSDEFINITIONS.comparator, name="comparator", curie=GA4GHVRSDEFINITIONS.curie('comparator'),
                   model_uri=VRSATILE.comparator, domain=None, range=Union[str, "ComparatorOptions"])

slots.id = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.id, name="id", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('id'),
                   model_uri=VRSATILE.id, domain=None, range=Optional[str])

slots.vrs_type = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.vrs_type, name="vrs_type", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('vrs_type'),
                   model_uri=VRSATILE.vrs_type, domain=None, range=Optional[str])

slots.label = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.label, name="label", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('label'),
                   model_uri=VRSATILE.label, domain=None, range=Optional[str])

slots.description = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.description, name="description", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('description'),
                   model_uri=VRSATILE.description, domain=None, range=Optional[str])

slots.xrefs = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.xrefs, name="xrefs", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('xrefs'),
                   model_uri=VRSATILE.xrefs, domain=None, range=Optional[Union[Union[dict, CURIE], List[Union[dict, CURIE]]]])

slots.alternate_labels = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.alternate_labels, name="alternate_labels", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('alternate_labels'),
                   model_uri=VRSATILE.alternate_labels, domain=None, range=Optional[Union[str, List[str]]])

slots.extensions = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.extensions, name="extensions", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('extensions'),
                   model_uri=VRSATILE.extensions, domain=None, range=Optional[Union[Union[dict, Extension], List[Union[dict, Extension]]]])

slots.variation_id = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.variation_id, name="variation_id", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('variation_id'),
                   model_uri=VRSATILE.variation_id, domain=None, range=Optional[Union[dict, CURIE]])

slots.molecule_context = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.molecule_context, name="molecule_context", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('molecule_context'),
                   model_uri=VRSATILE.molecule_context, domain=None, range=Optional[Union[str, "MoleculeContextOptions"]])

slots.structural_type = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.structural_type, name="structural_type", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('structural_type'),
                   model_uri=VRSATILE.structural_type, domain=None, range=Optional[Union[dict, CURIE]])

slots.expressions = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.expressions, name="expressions", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('expressions'),
                   model_uri=VRSATILE.expressions, domain=None, range=Union[Union[dict, Expression], List[Union[dict, Expression]]])

slots.vcf_record = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.vcf_record, name="vcf_record", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('vcf_record'),
                   model_uri=VRSATILE.vcf_record, domain=None, range=Optional[Union[dict, VcfRecord]])

slots.gene_context = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.gene_context, name="gene_context", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('gene_context'),
                   model_uri=VRSATILE.gene_context, domain=None, range=Optional[str])

slots.vrs_ref_allele_seq = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.vrs_ref_allele_seq, name="vrs_ref_allele_seq", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('vrs_ref_allele_seq'),
                   model_uri=VRSATILE.vrs_ref_allele_seq, domain=None, range=Optional[Union[dict, Sequence]])

slots.allelic_state = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.allelic_state, name="allelic_state", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('allelic_state'),
                   model_uri=VRSATILE.allelic_state, domain=None, range=Optional[Union[dict, CURIE]])

slots.name = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.name, name="name", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('name'),
                   model_uri=VRSATILE.name, domain=None, range=str)

slots.vrs_value = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.vrs_value, name="vrs_value", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('vrs_value'),
                   model_uri=VRSATILE.vrs_value, domain=None, range=str)

slots.syntax = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.syntax, name="syntax", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('syntax'),
                   model_uri=VRSATILE.syntax, domain=None, range=Union[str, "SyntaxOptions"])

slots.syntax_version = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.syntax_version, name="syntax_version", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('syntax_version'),
                   model_uri=VRSATILE.syntax_version, domain=None, range=Optional[str])

slots.version = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.version, name="version", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('version'),
                   model_uri=VRSATILE.version, domain=None, range=Optional[str])

slots.categorical_variation_id = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.categorical_variation_id, name="categorical_variation_id", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('categorical_variation_id'),
                   model_uri=VRSATILE.categorical_variation_id, domain=None, range=Optional[Union[dict, CURIE]])

slots.categorical_variation = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.categorical_variation, name="categorical_variation", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('categorical_variation'),
                   model_uri=VRSATILE.categorical_variation, domain=None, range=Optional[Union[dict, CategoricalVariation]])

slots.vrs_members = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.vrs_members, name="vrs_members", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('vrs_members'),
                   model_uri=VRSATILE.vrs_members, domain=None, range=Optional[Union[Union[dict, VariationMember], List[Union[dict, VariationMember]]]])

slots.genome_assembly = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.genome_assembly, name="genome_assembly", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('genome_assembly'),
                   model_uri=VRSATILE.genome_assembly, domain=None, range=str)

slots.chrom = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.chrom, name="chrom", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('chrom'),
                   model_uri=VRSATILE.chrom, domain=None, range=str)

slots.pos = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.pos, name="pos", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('pos'),
                   model_uri=VRSATILE.pos, domain=None, range=str)

slots.ref = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.ref, name="ref", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('ref'),
                   model_uri=VRSATILE.ref, domain=None, range=str)

slots.alt = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.alt, name="alt", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('alt'),
                   model_uri=VRSATILE.alt, domain=None, range=str)

slots.qual = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.qual, name="qual", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('qual'),
                   model_uri=VRSATILE.qual, domain=None, range=Optional[str])

slots.filter = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.filter, name="filter", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('filter'),
                   model_uri=VRSATILE.filter, domain=None, range=Optional[str])

slots.info = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.info, name="info", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('info'),
                   model_uri=VRSATILE.info, domain=None, range=Optional[str])

slots.ComplexVariation_catvars_id = Slot(uri=GA4GHCATEGORICALVARIATIONDEFINITIONS.catvars_id, name="ComplexVariation_catvars_id", curie=GA4GHCATEGORICALVARIATIONDEFINITIONS.curie('catvars_id'),
                   model_uri=VRSATILE.ComplexVariation_catvars_id, domain=ComplexVariation, range=Optional[str])

slots.ComplexVariation_catvars_type = Slot(uri=GA4GHCATEGORICALVARIATIONDEFINITIONS.catvars_type, name="ComplexVariation_catvars_type", curie=GA4GHCATEGORICALVARIATIONDEFINITIONS.curie('catvars_type'),
                   model_uri=VRSATILE.ComplexVariation_catvars_type, domain=ComplexVariation, range=str)

slots.ComplexVariation_operands = Slot(uri=GA4GHCATEGORICALVARIATIONDEFINITIONS.operands, name="ComplexVariation_operands", curie=GA4GHCATEGORICALVARIATIONDEFINITIONS.curie('operands'),
                   model_uri=VRSATILE.ComplexVariation_operands, domain=ComplexVariation, range=Union[Union[dict, CategoricalVariation], List[Union[dict, CategoricalVariation]]])

slots.ComplexVariation_operator = Slot(uri=GA4GHCATEGORICALVARIATIONDEFINITIONS.operator, name="ComplexVariation_operator", curie=GA4GHCATEGORICALVARIATIONDEFINITIONS.curie('operator'),
                   model_uri=VRSATILE.ComplexVariation_operator, domain=ComplexVariation, range=Union[str, "OperatorOptions"])

slots.CanonicalVariation_catvars_id = Slot(uri=GA4GHCATEGORICALVARIATIONDEFINITIONS.catvars_id, name="CanonicalVariation_catvars_id", curie=GA4GHCATEGORICALVARIATIONDEFINITIONS.curie('catvars_id'),
                   model_uri=VRSATILE.CanonicalVariation_catvars_id, domain=CanonicalVariation, range=Optional[str])

slots.CanonicalVariation_catvars_type = Slot(uri=GA4GHCATEGORICALVARIATIONDEFINITIONS.catvars_type, name="CanonicalVariation_catvars_type", curie=GA4GHCATEGORICALVARIATIONDEFINITIONS.curie('catvars_type'),
                   model_uri=VRSATILE.CanonicalVariation_catvars_type, domain=CanonicalVariation, range=str)

slots.CanonicalVariation_variation = Slot(uri=GA4GHCATEGORICALVARIATIONDEFINITIONS.variation, name="CanonicalVariation_variation", curie=GA4GHCATEGORICALVARIATIONDEFINITIONS.curie('variation'),
                   model_uri=VRSATILE.CanonicalVariation_variation, domain=CanonicalVariation, range=Union[dict, "Variation"])

slots.Allele__id = Slot(uri=GA4GHVRSDEFINITIONS._id, name="Allele__id", curie=GA4GHVRSDEFINITIONS.curie('_id'),
                   model_uri=VRSATILE.Allele__id, domain=Allele, range=Optional[Union[dict, "CURIE"]])

slots.Allele_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="Allele_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=VRSATILE.Allele_type, domain=Allele, range=str)

slots.Allele_location = Slot(uri=GA4GHVRSDEFINITIONS.location, name="Allele_location", curie=GA4GHVRSDEFINITIONS.curie('location'),
                   model_uri=VRSATILE.Allele_location, domain=Allele, range=Union[dict, "SequenceLocation"])

slots.Allele_state = Slot(uri=GA4GHVRSDEFINITIONS.state, name="Allele_state", curie=GA4GHVRSDEFINITIONS.curie('state'),
                   model_uri=VRSATILE.Allele_state, domain=Allele, range=str)

slots.Haplotype__id = Slot(uri=GA4GHVRSDEFINITIONS._id, name="Haplotype__id", curie=GA4GHVRSDEFINITIONS.curie('_id'),
                   model_uri=VRSATILE.Haplotype__id, domain=Haplotype, range=Optional[Union[dict, "CURIE"]])

slots.Haplotype_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="Haplotype_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=VRSATILE.Haplotype_type, domain=Haplotype, range=str)

slots.Haplotype_members = Slot(uri=GA4GHVRSDEFINITIONS.members, name="Haplotype_members", curie=GA4GHVRSDEFINITIONS.curie('members'),
                   model_uri=VRSATILE.Haplotype_members, domain=Haplotype, range=Union[str, List[str]])

slots.Text__id = Slot(uri=GA4GHVRSDEFINITIONS._id, name="Text__id", curie=GA4GHVRSDEFINITIONS.curie('_id'),
                   model_uri=VRSATILE.Text__id, domain=Text, range=Optional[Union[dict, "CURIE"]])

slots.Text_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="Text_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=VRSATILE.Text_type, domain=Text, range=str)

slots.Text_definition = Slot(uri=GA4GHVRSDEFINITIONS.definition, name="Text_definition", curie=GA4GHVRSDEFINITIONS.curie('definition'),
                   model_uri=VRSATILE.Text_definition, domain=Text, range=str)

slots.VariationSet__id = Slot(uri=GA4GHVRSDEFINITIONS._id, name="VariationSet__id", curie=GA4GHVRSDEFINITIONS.curie('_id'),
                   model_uri=VRSATILE.VariationSet__id, domain=VariationSet, range=Optional[Union[dict, "CURIE"]])

slots.VariationSet_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="VariationSet_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=VRSATILE.VariationSet_type, domain=VariationSet, range=str)

slots.VariationSet_members = Slot(uri=GA4GHVRSDEFINITIONS.members, name="VariationSet_members", curie=GA4GHVRSDEFINITIONS.curie('members'),
                   model_uri=VRSATILE.VariationSet_members, domain=VariationSet, range=Union[str, List[str]])

slots.CopyNumber__id = Slot(uri=GA4GHVRSDEFINITIONS._id, name="CopyNumber__id", curie=GA4GHVRSDEFINITIONS.curie('_id'),
                   model_uri=VRSATILE.CopyNumber__id, domain=CopyNumber, range=Optional[Union[dict, "CURIE"]])

slots.CopyNumber_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="CopyNumber_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=VRSATILE.CopyNumber_type, domain=CopyNumber, range=str)

slots.CopyNumber_subject = Slot(uri=GA4GHVRSDEFINITIONS.subject, name="CopyNumber_subject", curie=GA4GHVRSDEFINITIONS.curie('subject'),
                   model_uri=VRSATILE.CopyNumber_subject, domain=CopyNumber, range=str)

slots.CopyNumber_copies = Slot(uri=GA4GHVRSDEFINITIONS.copies, name="CopyNumber_copies", curie=GA4GHVRSDEFINITIONS.curie('copies'),
                   model_uri=VRSATILE.CopyNumber_copies, domain=CopyNumber, range=str)

slots.ChromosomeLocation__id = Slot(uri=GA4GHVRSDEFINITIONS._id, name="ChromosomeLocation__id", curie=GA4GHVRSDEFINITIONS.curie('_id'),
                   model_uri=VRSATILE.ChromosomeLocation__id, domain=ChromosomeLocation, range=Optional[Union[dict, "CURIE"]])

slots.ChromosomeLocation_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="ChromosomeLocation_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=VRSATILE.ChromosomeLocation_type, domain=ChromosomeLocation, range=str)

slots.ChromosomeLocation_species_id = Slot(uri=GA4GHVRSDEFINITIONS.species_id, name="ChromosomeLocation_species_id", curie=GA4GHVRSDEFINITIONS.curie('species_id'),
                   model_uri=VRSATILE.ChromosomeLocation_species_id, domain=ChromosomeLocation, range=Union[dict, "CURIE"])

slots.ChromosomeLocation_chr = Slot(uri=GA4GHVRSDEFINITIONS.chr, name="ChromosomeLocation_chr", curie=GA4GHVRSDEFINITIONS.curie('chr'),
                   model_uri=VRSATILE.ChromosomeLocation_chr, domain=ChromosomeLocation, range=str)

slots.ChromosomeLocation_interval = Slot(uri=GA4GHVRSDEFINITIONS.interval, name="ChromosomeLocation_interval", curie=GA4GHVRSDEFINITIONS.curie('interval'),
                   model_uri=VRSATILE.ChromosomeLocation_interval, domain=ChromosomeLocation, range=Union[dict, "CytobandInterval"])

slots.SequenceLocation__id = Slot(uri=GA4GHVRSDEFINITIONS._id, name="SequenceLocation__id", curie=GA4GHVRSDEFINITIONS.curie('_id'),
                   model_uri=VRSATILE.SequenceLocation__id, domain=SequenceLocation, range=Optional[Union[dict, "CURIE"]])

slots.SequenceLocation_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="SequenceLocation_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=VRSATILE.SequenceLocation_type, domain=SequenceLocation, range=str)

slots.SequenceLocation_sequence_id = Slot(uri=GA4GHVRSDEFINITIONS.sequence_id, name="SequenceLocation_sequence_id", curie=GA4GHVRSDEFINITIONS.curie('sequence_id'),
                   model_uri=VRSATILE.SequenceLocation_sequence_id, domain=SequenceLocation, range=Union[dict, "CURIE"])

slots.SequenceLocation_interval = Slot(uri=GA4GHVRSDEFINITIONS.interval, name="SequenceLocation_interval", curie=GA4GHVRSDEFINITIONS.curie('interval'),
                   model_uri=VRSATILE.SequenceLocation_interval, domain=SequenceLocation, range=str)

slots.SequenceInterval_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="SequenceInterval_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=VRSATILE.SequenceInterval_type, domain=SequenceInterval, range=str)

slots.SequenceInterval_start = Slot(uri=GA4GHVRSDEFINITIONS.start, name="SequenceInterval_start", curie=GA4GHVRSDEFINITIONS.curie('start'),
                   model_uri=VRSATILE.SequenceInterval_start, domain=SequenceInterval, range=int)

slots.SequenceInterval_end = Slot(uri=GA4GHVRSDEFINITIONS.end, name="SequenceInterval_end", curie=GA4GHVRSDEFINITIONS.curie('end'),
                   model_uri=VRSATILE.SequenceInterval_end, domain=SequenceInterval, range=int)

slots.CytobandInterval_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="CytobandInterval_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=VRSATILE.CytobandInterval_type, domain=CytobandInterval, range=str)

slots.CytobandInterval_start = Slot(uri=GA4GHVRSDEFINITIONS.start, name="CytobandInterval_start", curie=GA4GHVRSDEFINITIONS.curie('start'),
                   model_uri=VRSATILE.CytobandInterval_start, domain=CytobandInterval, range=Union[dict, "HumanCytoband"])

slots.CytobandInterval_end = Slot(uri=GA4GHVRSDEFINITIONS.end, name="CytobandInterval_end", curie=GA4GHVRSDEFINITIONS.curie('end'),
                   model_uri=VRSATILE.CytobandInterval_end, domain=CytobandInterval, range=Union[dict, "HumanCytoband"])

slots.LiteralSequenceExpression_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="LiteralSequenceExpression_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=VRSATILE.LiteralSequenceExpression_type, domain=LiteralSequenceExpression, range=str)

slots.LiteralSequenceExpression_sequence = Slot(uri=GA4GHVRSDEFINITIONS.sequence, name="LiteralSequenceExpression_sequence", curie=GA4GHVRSDEFINITIONS.curie('sequence'),
                   model_uri=VRSATILE.LiteralSequenceExpression_sequence, domain=LiteralSequenceExpression, range=Union[dict, "Sequence"])

slots.DerivedSequenceExpression_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="DerivedSequenceExpression_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=VRSATILE.DerivedSequenceExpression_type, domain=DerivedSequenceExpression, range=str)

slots.DerivedSequenceExpression_location = Slot(uri=GA4GHVRSDEFINITIONS.location, name="DerivedSequenceExpression_location", curie=GA4GHVRSDEFINITIONS.curie('location'),
                   model_uri=VRSATILE.DerivedSequenceExpression_location, domain=DerivedSequenceExpression, range=Union[dict, SequenceLocation])

slots.DerivedSequenceExpression_reverse_complement = Slot(uri=GA4GHVRSDEFINITIONS.reverse_complement, name="DerivedSequenceExpression_reverse_complement", curie=GA4GHVRSDEFINITIONS.curie('reverse_complement'),
                   model_uri=VRSATILE.DerivedSequenceExpression_reverse_complement, domain=DerivedSequenceExpression, range=Union[bool, Bool])

slots.RepeatedSequenceExpression_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="RepeatedSequenceExpression_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=VRSATILE.RepeatedSequenceExpression_type, domain=RepeatedSequenceExpression, range=str)

slots.RepeatedSequenceExpression_seq_expr = Slot(uri=GA4GHVRSDEFINITIONS.seq_expr, name="RepeatedSequenceExpression_seq_expr", curie=GA4GHVRSDEFINITIONS.curie('seq_expr'),
                   model_uri=VRSATILE.RepeatedSequenceExpression_seq_expr, domain=RepeatedSequenceExpression, range=str)

slots.RepeatedSequenceExpression_count = Slot(uri=GA4GHVRSDEFINITIONS.count, name="RepeatedSequenceExpression_count", curie=GA4GHVRSDEFINITIONS.curie('count'),
                   model_uri=VRSATILE.RepeatedSequenceExpression_count, domain=RepeatedSequenceExpression, range=str)

slots.ComposedSequenceExpression_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="ComposedSequenceExpression_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=VRSATILE.ComposedSequenceExpression_type, domain=ComposedSequenceExpression, range=str)

slots.ComposedSequenceExpression_components = Slot(uri=GA4GHVRSDEFINITIONS.components, name="ComposedSequenceExpression_components", curie=GA4GHVRSDEFINITIONS.curie('components'),
                   model_uri=VRSATILE.ComposedSequenceExpression_components, domain=ComposedSequenceExpression, range=Union[str, List[str]])

slots.Gene_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="Gene_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=VRSATILE.Gene_type, domain=Gene, range=str)

slots.Gene_gene_id = Slot(uri=GA4GHVRSDEFINITIONS.gene_id, name="Gene_gene_id", curie=GA4GHVRSDEFINITIONS.curie('gene_id'),
                   model_uri=VRSATILE.Gene_gene_id, domain=Gene, range=Union[dict, "CURIE"])

slots.Number_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="Number_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=VRSATILE.Number_type, domain=Number, range=str)

slots.Number_value = Slot(uri=GA4GHVRSDEFINITIONS.value, name="Number_value", curie=GA4GHVRSDEFINITIONS.curie('value'),
                   model_uri=VRSATILE.Number_value, domain=Number, range=int)

slots.DefiniteRange_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="DefiniteRange_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=VRSATILE.DefiniteRange_type, domain=DefiniteRange, range=str)

slots.DefiniteRange_min = Slot(uri=GA4GHVRSDEFINITIONS.min, name="DefiniteRange_min", curie=GA4GHVRSDEFINITIONS.curie('min'),
                   model_uri=VRSATILE.DefiniteRange_min, domain=DefiniteRange, range=float)

slots.DefiniteRange_max = Slot(uri=GA4GHVRSDEFINITIONS.max, name="DefiniteRange_max", curie=GA4GHVRSDEFINITIONS.curie('max'),
                   model_uri=VRSATILE.DefiniteRange_max, domain=DefiniteRange, range=float)

slots.IndefiniteRange_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="IndefiniteRange_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=VRSATILE.IndefiniteRange_type, domain=IndefiniteRange, range=str)

slots.IndefiniteRange_value = Slot(uri=GA4GHVRSDEFINITIONS.value, name="IndefiniteRange_value", curie=GA4GHVRSDEFINITIONS.curie('value'),
                   model_uri=VRSATILE.IndefiniteRange_value, domain=IndefiniteRange, range=float)

slots.IndefiniteRange_comparator = Slot(uri=GA4GHVRSDEFINITIONS.comparator, name="IndefiniteRange_comparator", curie=GA4GHVRSDEFINITIONS.curie('comparator'),
                   model_uri=VRSATILE.IndefiniteRange_comparator, domain=IndefiniteRange, range=Union[str, "ComparatorOptions"])

slots.SequenceState_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="SequenceState_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=VRSATILE.SequenceState_type, domain=SequenceState, range=str)

slots.SequenceState_sequence = Slot(uri=GA4GHVRSDEFINITIONS.sequence, name="SequenceState_sequence", curie=GA4GHVRSDEFINITIONS.curie('sequence'),
                   model_uri=VRSATILE.SequenceState_sequence, domain=SequenceState, range=Union[dict, Sequence])

slots.SimpleInterval_type = Slot(uri=GA4GHVRSDEFINITIONS.type, name="SimpleInterval_type", curie=GA4GHVRSDEFINITIONS.curie('type'),
                   model_uri=VRSATILE.SimpleInterval_type, domain=SimpleInterval, range=str)

slots.SimpleInterval_start = Slot(uri=GA4GHVRSDEFINITIONS.start, name="SimpleInterval_start", curie=GA4GHVRSDEFINITIONS.curie('start'),
                   model_uri=VRSATILE.SimpleInterval_start, domain=SimpleInterval, range=int)

slots.SimpleInterval_end = Slot(uri=GA4GHVRSDEFINITIONS.end, name="SimpleInterval_end", curie=GA4GHVRSDEFINITIONS.curie('end'),
                   model_uri=VRSATILE.SimpleInterval_end, domain=SimpleInterval, range=int)

slots.VariationDescriptor_id = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.id, name="VariationDescriptor_id", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('id'),
                   model_uri=VRSATILE.VariationDescriptor_id, domain=VariationDescriptor, range=Union[dict, CURIE])

slots.VariationDescriptor_vrs_type = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.vrs_type, name="VariationDescriptor_vrs_type", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('vrs_type'),
                   model_uri=VRSATILE.VariationDescriptor_vrs_type, domain=VariationDescriptor, range=Union[str, "TypeOptions"])

slots.VariationDescriptor_label = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.label, name="VariationDescriptor_label", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('label'),
                   model_uri=VRSATILE.VariationDescriptor_label, domain=VariationDescriptor, range=Optional[str])

slots.VariationDescriptor_description = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.description, name="VariationDescriptor_description", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('description'),
                   model_uri=VRSATILE.VariationDescriptor_description, domain=VariationDescriptor, range=Optional[str])

slots.VariationDescriptor_xrefs = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.xrefs, name="VariationDescriptor_xrefs", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('xrefs'),
                   model_uri=VRSATILE.VariationDescriptor_xrefs, domain=VariationDescriptor, range=Optional[Union[Union[dict, CURIE], List[Union[dict, CURIE]]]])

slots.VariationDescriptor_alternate_labels = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.alternate_labels, name="VariationDescriptor_alternate_labels", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('alternate_labels'),
                   model_uri=VRSATILE.VariationDescriptor_alternate_labels, domain=VariationDescriptor, range=Optional[Union[str, List[str]]])

slots.VariationDescriptor_extensions = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.extensions, name="VariationDescriptor_extensions", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('extensions'),
                   model_uri=VRSATILE.VariationDescriptor_extensions, domain=VariationDescriptor, range=Optional[Union[Union[dict, "Extension"], List[Union[dict, "Extension"]]]])

slots.VariationDescriptor_variation_id = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.variation_id, name="VariationDescriptor_variation_id", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('variation_id'),
                   model_uri=VRSATILE.VariationDescriptor_variation_id, domain=VariationDescriptor, range=Optional[Union[dict, CURIE]])

slots.VariationDescriptor_variation = Slot(uri=GA4GHCATEGORICALVARIATIONDEFINITIONS.variation, name="VariationDescriptor_variation", curie=GA4GHCATEGORICALVARIATIONDEFINITIONS.curie('variation'),
                   model_uri=VRSATILE.VariationDescriptor_variation, domain=VariationDescriptor, range=Union[dict, Variation])

slots.VariationDescriptor_molecule_context = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.molecule_context, name="VariationDescriptor_molecule_context", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('molecule_context'),
                   model_uri=VRSATILE.VariationDescriptor_molecule_context, domain=VariationDescriptor, range=Optional[Union[str, "MoleculeContextOptions"]])

slots.VariationDescriptor_structural_type = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.structural_type, name="VariationDescriptor_structural_type", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('structural_type'),
                   model_uri=VRSATILE.VariationDescriptor_structural_type, domain=VariationDescriptor, range=Optional[Union[dict, CURIE]])

slots.VariationDescriptor_expressions = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.expressions, name="VariationDescriptor_expressions", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('expressions'),
                   model_uri=VRSATILE.VariationDescriptor_expressions, domain=VariationDescriptor, range=Union[Union[dict, "Expression"], List[Union[dict, "Expression"]]])

slots.VariationDescriptor_vcf_record = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.vcf_record, name="VariationDescriptor_vcf_record", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('vcf_record'),
                   model_uri=VRSATILE.VariationDescriptor_vcf_record, domain=VariationDescriptor, range=Optional[Union[dict, "VcfRecord"]])

slots.VariationDescriptor_gene_context = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.gene_context, name="VariationDescriptor_gene_context", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('gene_context'),
                   model_uri=VRSATILE.VariationDescriptor_gene_context, domain=VariationDescriptor, range=Optional[str])

slots.VariationDescriptor_vrs_ref_allele_seq = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.vrs_ref_allele_seq, name="VariationDescriptor_vrs_ref_allele_seq", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('vrs_ref_allele_seq'),
                   model_uri=VRSATILE.VariationDescriptor_vrs_ref_allele_seq, domain=VariationDescriptor, range=Optional[Union[dict, Sequence]])

slots.VariationDescriptor_allelic_state = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.allelic_state, name="VariationDescriptor_allelic_state", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('allelic_state'),
                   model_uri=VRSATILE.VariationDescriptor_allelic_state, domain=VariationDescriptor, range=Optional[Union[dict, CURIE]])

slots.Extension_vrs_type = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.vrs_type, name="Extension_vrs_type", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('vrs_type'),
                   model_uri=VRSATILE.Extension_vrs_type, domain=Extension, range=str)

slots.Extension_name = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.name, name="Extension_name", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('name'),
                   model_uri=VRSATILE.Extension_name, domain=Extension, range=str)

slots.Extension_vrs_value = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.vrs_value, name="Extension_vrs_value", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('vrs_value'),
                   model_uri=VRSATILE.Extension_vrs_value, domain=Extension, range=str)

slots.Expression_vrs_type = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.vrs_type, name="Expression_vrs_type", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('vrs_type'),
                   model_uri=VRSATILE.Expression_vrs_type, domain=Expression, range=str)

slots.Expression_syntax = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.syntax, name="Expression_syntax", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('syntax'),
                   model_uri=VRSATILE.Expression_syntax, domain=Expression, range=Union[str, "SyntaxOptions"])

slots.Expression_vrs_value = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.vrs_value, name="Expression_vrs_value", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('vrs_value'),
                   model_uri=VRSATILE.Expression_vrs_value, domain=Expression, range=str)

slots.Expression_syntax_version = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.syntax_version, name="Expression_syntax_version", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('syntax_version'),
                   model_uri=VRSATILE.Expression_syntax_version, domain=Expression, range=Optional[str])

slots.CategoricalVariationDescriptor_id = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.id, name="CategoricalVariationDescriptor_id", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('id'),
                   model_uri=VRSATILE.CategoricalVariationDescriptor_id, domain=CategoricalVariationDescriptor, range=Union[dict, CURIE])

slots.CategoricalVariationDescriptor_vrs_type = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.vrs_type, name="CategoricalVariationDescriptor_vrs_type", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('vrs_type'),
                   model_uri=VRSATILE.CategoricalVariationDescriptor_vrs_type, domain=CategoricalVariationDescriptor, range=str)

slots.CategoricalVariationDescriptor_label = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.label, name="CategoricalVariationDescriptor_label", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('label'),
                   model_uri=VRSATILE.CategoricalVariationDescriptor_label, domain=CategoricalVariationDescriptor, range=Optional[str])

slots.CategoricalVariationDescriptor_description = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.description, name="CategoricalVariationDescriptor_description", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('description'),
                   model_uri=VRSATILE.CategoricalVariationDescriptor_description, domain=CategoricalVariationDescriptor, range=Optional[str])

slots.CategoricalVariationDescriptor_xrefs = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.xrefs, name="CategoricalVariationDescriptor_xrefs", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('xrefs'),
                   model_uri=VRSATILE.CategoricalVariationDescriptor_xrefs, domain=CategoricalVariationDescriptor, range=Optional[Union[Union[dict, CURIE], List[Union[dict, CURIE]]]])

slots.CategoricalVariationDescriptor_alternate_labels = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.alternate_labels, name="CategoricalVariationDescriptor_alternate_labels", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('alternate_labels'),
                   model_uri=VRSATILE.CategoricalVariationDescriptor_alternate_labels, domain=CategoricalVariationDescriptor, range=Optional[Union[str, List[str]]])

slots.CategoricalVariationDescriptor_extensions = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.extensions, name="CategoricalVariationDescriptor_extensions", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('extensions'),
                   model_uri=VRSATILE.CategoricalVariationDescriptor_extensions, domain=CategoricalVariationDescriptor, range=Optional[Union[Union[dict, Extension], List[Union[dict, Extension]]]])

slots.CategoricalVariationDescriptor_version = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.version, name="CategoricalVariationDescriptor_version", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('version'),
                   model_uri=VRSATILE.CategoricalVariationDescriptor_version, domain=CategoricalVariationDescriptor, range=Optional[str])

slots.CategoricalVariationDescriptor_categorical_variation_id = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.categorical_variation_id, name="CategoricalVariationDescriptor_categorical_variation_id", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('categorical_variation_id'),
                   model_uri=VRSATILE.CategoricalVariationDescriptor_categorical_variation_id, domain=CategoricalVariationDescriptor, range=Optional[Union[dict, CURIE]])

slots.CategoricalVariationDescriptor_categorical_variation = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.categorical_variation, name="CategoricalVariationDescriptor_categorical_variation", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('categorical_variation'),
                   model_uri=VRSATILE.CategoricalVariationDescriptor_categorical_variation, domain=CategoricalVariationDescriptor, range=Optional[Union[dict, CategoricalVariation]])

slots.CategoricalVariationDescriptor_vrs_members = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.vrs_members, name="CategoricalVariationDescriptor_vrs_members", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('vrs_members'),
                   model_uri=VRSATILE.CategoricalVariationDescriptor_vrs_members, domain=CategoricalVariationDescriptor, range=Optional[Union[Union[dict, "VariationMember"], List[Union[dict, "VariationMember"]]]])

slots.VariationMember_vrs_type = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.vrs_type, name="VariationMember_vrs_type", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('vrs_type'),
                   model_uri=VRSATILE.VariationMember_vrs_type, domain=VariationMember, range=Optional[str])

slots.VariationMember_expressions = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.expressions, name="VariationMember_expressions", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('expressions'),
                   model_uri=VRSATILE.VariationMember_expressions, domain=VariationMember, range=Union[Union[dict, Expression], List[Union[dict, Expression]]])

slots.VariationMember_variation_id = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.variation_id, name="VariationMember_variation_id", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('variation_id'),
                   model_uri=VRSATILE.VariationMember_variation_id, domain=VariationMember, range=Optional[Union[dict, CURIE]])

slots.VcfRecord_genome_assembly = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.genome_assembly, name="VcfRecord_genome_assembly", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('genome_assembly'),
                   model_uri=VRSATILE.VcfRecord_genome_assembly, domain=VcfRecord, range=str)

slots.VcfRecord_chrom = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.chrom, name="VcfRecord_chrom", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('chrom'),
                   model_uri=VRSATILE.VcfRecord_chrom, domain=VcfRecord, range=str)

slots.VcfRecord_pos = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.pos, name="VcfRecord_pos", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('pos'),
                   model_uri=VRSATILE.VcfRecord_pos, domain=VcfRecord, range=str)

slots.VcfRecord_id = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.id, name="VcfRecord_id", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('id'),
                   model_uri=VRSATILE.VcfRecord_id, domain=VcfRecord, range=Optional[str])

slots.VcfRecord_ref = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.ref, name="VcfRecord_ref", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('ref'),
                   model_uri=VRSATILE.VcfRecord_ref, domain=VcfRecord, range=str)

slots.VcfRecord_alt = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.alt, name="VcfRecord_alt", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('alt'),
                   model_uri=VRSATILE.VcfRecord_alt, domain=VcfRecord, range=str)

slots.VcfRecord_qual = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.qual, name="VcfRecord_qual", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('qual'),
                   model_uri=VRSATILE.VcfRecord_qual, domain=VcfRecord, range=Optional[str])

slots.VcfRecord_filter = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.filter, name="VcfRecord_filter", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('filter'),
                   model_uri=VRSATILE.VcfRecord_filter, domain=VcfRecord, range=Optional[str])

slots.VcfRecord_info = Slot(uri=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.info, name="VcfRecord_info", curie=GA4GHVALUEOBJECTDESCRIPTORDEFINITIONS.curie('info'),
                   model_uri=VRSATILE.VcfRecord_info, domain=VcfRecord, range=Optional[str])