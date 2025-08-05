from pathlib import Path
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, RDFS, FOAF, XSD, SKOS, OWL, DCTERMS

# Load your ontology
# import patient_ontology

# Resolve the path relative to the current script
ontology_path = Path(__file__).resolve().parent.parent / "ontology" / "owlapi.xrdf"

g = Graph()
#g.parse(ontology_path, format="xml")  # If this fails, try format="application/rdf+xml"

# Define custom namespaces
# FHIR RDF core namespace
FHIR = Namespace("http://hl7.org/fhir/")
EX = Namespace("http://example.org/")
SNOMED = Namespace("http://snomed.info/id/")
MONDO = Namespace("http://purl.obolibrary.org/obo/MONDO_")
NCIT = Namespace("http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#")
LAYER = Namespace("http://example.org/layer#")

# Bind prefixes for readability
# Bind for readability
g.bind("fhir", FHIR)
g.bind("ex", EX)
g.bind("foaf", FOAF)
g.bind("rdfs", RDFS)
g.bind("xsd", XSD)
g.bind("mondo", MONDO)
g.bind("snomed", SNOMED)
g.bind("layer", LAYER)

### -----------------------
layer0 = EX.Layer0
layer1 = EX.Layer1

#g.add((layer0, RDF.type, OWL.Class))
#g.add((layer1, RDF.type, OWL.Class))
### -----------------------

### ——————— Layer 0 ———————
# Define the disease class (ontology concept)
# Define the disease (PAH - pulmonary arterial hypertension )
pah_class = MONDO["0015924"]
g.add((pah_class, RDF.type, FHIR.Condition))
#g.add((pah_class, RDF.type, OWL.Class))
g.add((pah_class, RDFS.label, Literal("Pulmonary Arterial Hypertension")))
g.add((pah_class, LAYER.hasLayer, layer0))
### ——————— Layer 1 ———————
# Define the patient instance
# Define the first patient

patient = EX.Patient1
g.add((patient, RDF.type, FHIR.Patient))
g.add((patient, FOAF.name, Literal("Amelia Hart")))
g.add((patient, FHIR.gender, Literal("female")))
g.add((patient, FHIR.birthDate, Literal("1970-04-25", datatype=XSD.date)))
g.add((patient, FHIR.id, Literal("123456")))

g.add((patient, LAYER.hasLayer, layer1))

# Type declaration
# pah_instance = EX.PAH
# g.add((pah_instance, RDF.type, FHIR.Condition))
# # Preferred label
# g.add((pah_instance, RDFS.label, Literal("PAH diagnosis in Patient 1")))
# g.add((pah_instance, RDF.type, pah_class))  # link to MONDO class
#g.add((pah, SKOS.prefLabel, Literal("Pulmonary Arterial Hypertension")))
# Synonyms (if needed)
#g.add((pah, SKOS.altLabel, Literal("PAH")))

# Definition
#g.add((pah, DCTERMS.description, Literal("Pulmonary arterial hypertension is a progressive disorder characterized by high blood pressure in the arteries of the lungs.")))

# Equivalence mapping (optional)
#g.add((pah, OWL.sameAs, URIRef("http://snomed.info/id/70995007")))  # SNOMED-CT
#g.add((pah, OWL.sameAs, URIRef("http://purl.bioontology.org/ontology/NCIT/C84468")))  # NCIT

g.add((patient, FHIR.condition, pah_class))

"""
# Add observation (e.g., BNP level)
obs = EX.Observation1
g.add((obs, RDF.type, FHIR.Observation))
g.add((obs, FHIR.subject, patient))
g.add((obs, FHIR.code, SNOMED["390917008"]))   # BNP (NT pro-BNP) (once)
g.add((obs, FHIR.valueQuantity, Literal("180", datatype=XSD.integer)))
g.add((obs, FHIR.unit, Literal("pg/mL")))
g.add((obs, FHIR.effectiveDateTime, Literal("2025-07-22T08:00:00Z", datatype=XSD.dateTime)))

# Add medication
med = EX.Medication1
g.add((med, RDF.type, FHIR.MedicationStatement))
g.add((med, FHIR.medicationCodeableConcept, SNOMED["34783311000001104"]))
g.add((med, FHIR.subject, patient))
g.add((med, FHIR.dateAsserted, Literal("2024-01-15", datatype=XSD.date)))


# --------------------------------------------------------------------------------------

# Define the first patient
patient2 = EX.Patient2
g.add((patient2, RDF.type, FHIR.Patient))
g.add((patient2, FOAF.name, Literal("Oliver Bennett")))
g.add((patient2, FHIR.gender, Literal("male")))
g.add((patient2, FHIR.birthDate, Literal("1977-06-20", datatype=XSD.date)))
g.add((patient2, FHIR.id, Literal("654321")))

# Define the disease (PAH - pulmonary arterial hypertension )
g.add((patient2, FHIR.condition, pah))


# Add observation (e.g., BNP level)
obs2 = EX.Observation2
g.add((obs2, RDF.type, FHIR.Observation))
g.add((obs2, FHIR.subject, patient2))
g.add((obs2, FHIR.code, SNOMED["390917008"]))   # BNP (NT pro-BNP) (once)
g.add((obs2, FHIR.valueQuantity, Literal("121", datatype=XSD.integer)))
g.add((obs2, FHIR.unit, Literal("pg/mL")))
g.add((obs2, FHIR.effectiveDateTime, Literal("2024-06-20T09:00:00Z", datatype=XSD.dateTime)))

# Add medication
med2 = EX.Medication2
g.add((med2, RDF.type, FHIR.MedicationStatement))
g.add((med2, FHIR.medicationCodeableConcept, SNOMED["34783311000001104"]))
g.add((med2, FHIR.subject, patient2))
g.add((med2, FHIR.dateAsserted, Literal("2024-07-15", datatype=XSD.date)))

"""
# --------------------------------------------------------------------------------------
# Patient ontology


# --------------------------------------------------------------------------------------

# Resolve the path relative to the current script
output_path = Path(__file__).resolve().parent.parent / "data" / "cvd_knowledge_graph.ttl"
output_path.parent.mkdir(parents=True, exist_ok=True)
# Save the Turtle file
g.serialize(destination=str(output_path), format="turtle")


