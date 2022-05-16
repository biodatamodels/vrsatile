

CREATE TABLE "Allele" (
	_id TEXT, 
	type TEXT NOT NULL, 
	location TEXT NOT NULL, 
	state TEXT NOT NULL, 
	PRIMARY KEY (_id, type, location, state)
);

CREATE TABLE "CanonicalVariation" (
	catvars_id TEXT, 
	catvars_type TEXT NOT NULL, 
	variation TEXT NOT NULL, 
	PRIMARY KEY (catvars_id, catvars_type, variation)
);

CREATE TABLE "CategoricalVariationDescriptor" (
	id TEXT NOT NULL, 
	vrs_type TEXT NOT NULL, 
	label TEXT, 
	description TEXT, 
	xrefs TEXT, 
	alternate_labels TEXT, 
	extensions TEXT, 
	version TEXT, 
	categorical_variation_id TEXT, 
	categorical_variation TEXT, 
	vrs_members TEXT, 
	PRIMARY KEY (id, vrs_type, label, description, xrefs, alternate_labels, extensions, version, categorical_variation_id, categorical_variation, vrs_members)
);

CREATE TABLE "ChromosomeLocation" (
	_id TEXT, 
	type TEXT NOT NULL, 
	species_id TEXT NOT NULL, 
	chr TEXT NOT NULL, 
	interval TEXT NOT NULL, 
	PRIMARY KEY (_id, type, species_id, chr, interval)
);

CREATE TABLE "ComplexVariation" (
	catvars_id TEXT, 
	catvars_type TEXT NOT NULL, 
	operands TEXT NOT NULL, 
	operator VARCHAR(3) NOT NULL, 
	PRIMARY KEY (catvars_id, catvars_type, operands, operator)
);

CREATE TABLE "ComposedSequenceExpression" (
	type TEXT NOT NULL, 
	components TEXT NOT NULL, 
	PRIMARY KEY (type, components)
);

CREATE TABLE "CopyNumber" (
	_id TEXT, 
	type TEXT NOT NULL, 
	subject TEXT NOT NULL, 
	copies TEXT NOT NULL, 
	PRIMARY KEY (_id, type, subject, copies)
);

CREATE TABLE "CytobandInterval" (
	type TEXT NOT NULL, 
	start TEXT NOT NULL, 
	"end" TEXT NOT NULL, 
	PRIMARY KEY (type, start, "end")
);

CREATE TABLE "DefiniteRange" (
	type TEXT NOT NULL, 
	min FLOAT NOT NULL, 
	max FLOAT NOT NULL, 
	PRIMARY KEY (type, min, max)
);

CREATE TABLE "DerivedSequenceExpression" (
	type TEXT NOT NULL, 
	location TEXT NOT NULL, 
	reverse_complement BOOLEAN NOT NULL, 
	PRIMARY KEY (type, location, reverse_complement)
);

CREATE TABLE "Expression" (
	vrs_type TEXT NOT NULL, 
	syntax VARCHAR(6) NOT NULL, 
	vrs_value TEXT NOT NULL, 
	syntax_version TEXT, 
	PRIMARY KEY (vrs_type, syntax, vrs_value, syntax_version)
);

CREATE TABLE "Extension" (
	vrs_type TEXT NOT NULL, 
	name TEXT NOT NULL, 
	vrs_value TEXT NOT NULL, 
	PRIMARY KEY (vrs_type, name, vrs_value)
);

CREATE TABLE "Gene" (
	type TEXT NOT NULL, 
	gene_id TEXT NOT NULL, 
	PRIMARY KEY (type, gene_id)
);

CREATE TABLE "Haplotype" (
	_id TEXT, 
	type TEXT NOT NULL, 
	members TEXT NOT NULL, 
	PRIMARY KEY (_id, type, members)
);

CREATE TABLE "IndefiniteRange" (
	type TEXT NOT NULL, 
	value FLOAT NOT NULL, 
	comparator VARCHAR(2) NOT NULL, 
	PRIMARY KEY (type, value, comparator)
);

CREATE TABLE "LiteralSequenceExpression" (
	type TEXT NOT NULL, 
	sequence TEXT NOT NULL, 
	PRIMARY KEY (type, sequence)
);

CREATE TABLE "Number" (
	type TEXT NOT NULL, 
	value INTEGER NOT NULL, 
	PRIMARY KEY (type, value)
);

CREATE TABLE "RepeatedSequenceExpression" (
	type TEXT NOT NULL, 
	seq_expr TEXT NOT NULL, 
	count TEXT NOT NULL, 
	PRIMARY KEY (type, seq_expr, count)
);

CREATE TABLE "SequenceInterval" (
	type TEXT NOT NULL, 
	start INTEGER NOT NULL, 
	"end" INTEGER NOT NULL, 
	PRIMARY KEY (type, start, "end")
);

CREATE TABLE "SequenceLocation" (
	_id TEXT, 
	type TEXT NOT NULL, 
	sequence_id TEXT NOT NULL, 
	interval TEXT NOT NULL, 
	PRIMARY KEY (_id, type, sequence_id, interval)
);

CREATE TABLE "SequenceState" (
	type TEXT NOT NULL, 
	sequence TEXT NOT NULL, 
	PRIMARY KEY (type, sequence)
);

CREATE TABLE "SimpleInterval" (
	type TEXT NOT NULL, 
	start INTEGER NOT NULL, 
	"end" INTEGER NOT NULL, 
	PRIMARY KEY (type, start, "end")
);

CREATE TABLE "Text" (
	_id TEXT, 
	type TEXT NOT NULL, 
	definition TEXT NOT NULL, 
	PRIMARY KEY (_id, type, definition)
);

CREATE TABLE "VariationDescriptor" (
	id TEXT NOT NULL, 
	vrs_type VARCHAR(19) NOT NULL, 
	label TEXT, 
	description TEXT, 
	xrefs TEXT, 
	alternate_labels TEXT, 
	extensions TEXT, 
	variation_id TEXT, 
	variation TEXT NOT NULL, 
	molecule_context VARCHAR(10), 
	structural_type TEXT, 
	expressions TEXT NOT NULL, 
	vcf_record TEXT, 
	gene_context TEXT, 
	vrs_ref_allele_seq TEXT, 
	allelic_state TEXT, 
	PRIMARY KEY (id, vrs_type, label, description, xrefs, alternate_labels, extensions, variation_id, variation, molecule_context, structural_type, expressions, vcf_record, gene_context, vrs_ref_allele_seq, allelic_state)
);

CREATE TABLE "VariationMember" (
	vrs_type TEXT, 
	expressions TEXT NOT NULL, 
	variation_id TEXT, 
	PRIMARY KEY (vrs_type, expressions, variation_id)
);

CREATE TABLE "VariationSet" (
	_id TEXT, 
	type TEXT NOT NULL, 
	members TEXT NOT NULL, 
	PRIMARY KEY (_id, type, members)
);

CREATE TABLE "VcfRecord" (
	genome_assembly TEXT NOT NULL, 
	chrom TEXT NOT NULL, 
	pos TEXT NOT NULL, 
	id TEXT, 
	ref TEXT NOT NULL, 
	alt TEXT NOT NULL, 
	qual TEXT, 
	filter TEXT, 
	info TEXT, 
	PRIMARY KEY (genome_assembly, chrom, pos, id, ref, alt, qual, filter, info)
);
