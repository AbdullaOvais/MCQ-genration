# O-RAN Information Model and Data Models Specification

# This is a re-published version of the attached final specification.

For this re-published version, the prior versions of the IPR Policy will apply, except that the previous requirement for Adopters (as defined in the earlier IPR Policy) to agree to an O-RAN Adopter License Agreement to access and use Final Specifications shall no longer apply or be required for these Final Specifications after 1st July 2022.

The copying or incorporation into any other work of part or all of the material available in this specification in any form without the prior written permission of O-RAN ALLIANCE e.V. is prohibited, save that you may print or download extracts of the material on this site for your personal use, or copy the material on this site for the purpose of sending to individual third parties for their information provided that you acknowledge O-RAN ALLIANCE as the source of the material and that you inform the third party that these conditions apply to them and that they must comply with them.

# O-RAN Information Model and Data Models Specification

# Contents

2   
3 Chapter 1. Introductory Material... ............................................................................................... ....... . 3   
4 1.1 Scope ..... . 3   
5 1.2 References...... ...................................... ... 3   
6 1.2.1 Definitions and Abbreviations.. ... 5   
7 1.2.2 Definitions.. .................. ... 5   
8 1.2.3 Abbreviations and acronyms.. .......................... ..... 5   
9 Chapter 2. Overview and Philosophy........................................................ ............................................................... 7   
10 2.1 “Prosumer” relationship between O-RAN and Standards Development Organizations ............................. ....... 7   
11 2.2 Information and Data Models as a Modeling Continuum......... .................................................. 8   
12 2.3 Information and Data Modeling Co-Evolution....... ............................................................................ 9   
13 2.4 Model and Use Case Development (process) ..... .................................... 10   
14 2.5 O-RAN components reflected within O-RAN Information Model and Data Model(s).. ....................... .... 10   
15 2.6 Open Issues and Future Considerations .... ........................................ 11   
16 Chapter 3. O-RAN Information Model .. ..................................................................... 12   
17 3.1 A general view of an Information Model.... ............................................. .... 12   
18 3.2 Modeling approach, Unified Modeling Language (UML)... 12   
19 3.3 IISOMI (Informal Inter-SDO Open Model Initiative) guidelines.. ................................................ 12   
20 3.4 General Information on the UML Model..... 13   
21 3.5 O-RAN Information Model ....................... 13   
22 3.6 Classes/components and interfaces that comprise the O-RAN Information Model and Data Models... 13   
23 3.7 Installing and using Papyrus ........... ................... 14   
24 Chapter 4. O-RAN Data Models .. . 15   
25 4.1 Repositories; current conventions to distinguish between models under development versus models that   
26 are approved for use......... ....... 15   
27 4.2 Formal relationship (traceability) between O-RAN Data Models and the O-RAN Information Model. ..... . 16   
28 4.3 Usage of 3GPP Data Models ....... . 17   
29 30 4.4 4.5 Usage of non-3GPP data models ..................................................................................................................... 18YANG Conventions......................................................................................................................................... 21   
31 4.5.1 Naming .......... ............................................................................... ..... 21   
32 4.5.2 Revision Statement... ... 21   
33 4.5.3 Indents ............. ............................................................................................... . 22   
34 4.5.4 YANG Language Usage.... ........................... . 22   
35 4.5.5 Cross Working Group Co-ordination ......................................................................................................... 22   
36 Annex A: Link to Information Model source (under development; not approved for use) ..... ....... 23   
37 Annex B: Installing and using Eclipse Papyrus [refer to O-RAN wiki for the most up-to-date guidelines] .................... 24   
38 Annex C: Links to Data Models approved for use... .... 28   
39 Annex ZZZ : O-RAN Adopter License Agreement.. . 29   
40 Section 1: DEFINITIONS .................. ................................................................................................................... 29   
41 Section 2: COPYRIGHT LICENSE . ........................................................................................ .... 29   
42 Section 3: FRAND LICENSE .......... .......................................................................................... ..... 29   
43 Section 4: TERM AND TERMINATION. ................................................... . 30   
44 Section 5: CONFIDENTIALITY . ..................................................................... ... 30   
45 Section 6: INDEMNIFICATION . ................................................................ . 30   
46 Section 7: LIMITATIONS ON LIABILITY; NO WARRANTY ..................................................................... ... 30   
47 Section 8: ASSIGNMENT .......... ........................................................................... ...... 31   
48 Section 9: THIRD-PARTY BENEFICIARY RIGHTS ..... ............................................................................................ 31   
49 Section 10: BINDING ON AFFILIATES ..... ..................................................................................................... 31   
50 Section 11: GENERAL.. ......... .... 31

# Chapter 1.Introductory Material

# 1.1 Scope

This Technical Specification has been produced by the O-RAN.org.

The contents of the present document are subject to continuing work within O-RAN WG1 and may change following formal O-RAN approval. Should the O-RAN.org modify the contents of the present document, it will be re-released by O-RAN Alliance with an identifying change of release date and an increase in version number as follows:

Release x.y.z

where:

x the first digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc. (the initial approved document will have $\scriptstyle \mathbf { X } = 0 1$ ).   
y the second digit is incremented when editorial only changes have been incorporated in the document.   
z the third digit included only in working versions of the document indicating incremental changes during the editing process.

This document is both a Specification and an Informational Report in that it specifies the Information Model (not yet approved for use) and the Data Models (approved for use) that are foundational for O-RAN’s model-driven architecture and for the functions carried out over O-RAN interfaces, e.g., management functions, procedures, operations and corresponding solutions.

In addition, this document includes information about existing standards and industry work that serve as a basis for work items in O-RAN. There is a “prosumer” relationship evolving between O-RAN and 3GPP, as each makes its model available and provides model feedback to the other.

Lastly, this document describes the de facto methods and procedures with respect to a “modeling continuum” that aims to establish and evolve an O-RAN Information Model from which O-RAN Data Models may be generated manually or with a set of tools.

# 1.2 References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

References are either specific (identified by date of publication, edition number, version number, etc.) or non-specific.   
For a specific reference, subsequent revisions do not apply.   
For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document in Release 16

[1] 3GPP TR 21.905: Vocabulary for 3GPP Specifications [2] 3GPP TR 28.890: Management and orchestration; Study on integration of Open Network Automation Platform (ONAP) and 3GPP management for 5G networks

[3] 3GPP TS 28.530: “Management and orchestration; Concepts, use cases and requirements”

[4] 3GPP TS 28.531: Management and orchestration; Provisioning [5] 3GPP TS 28.532: Management and orchestration; Generic management services [6] 3GPP TS 28.533: Management and orchestration: Architecture framework [7] 3GPP TS 28.540: Management and orchestration; 5G Network Resource Model (NRM); Stage 1 [8] 3GPP TS 28.541: Management and orchestration; 5G Network Resource Model (NRM); Stage 2 and stage 3 [9] 3GPP TS 28.545: Management and orchestration; Fault Supervision (FS)

1 [10] 3GPP TS 28.550: Management and orchestration; Performance assurance   
2 [11] 3GPP TS 28.552: Management and orchestration; 5G performance measurements   
3 [12] 3GPP TS 28.554: Management and orchestration; 5G end to end Key Performance Indicators (KPI)   
4 [13] 3GPP TS 28.621: Telecommunication management; Generic Network Resource Model (NRM) Integration   
5 Reference Point (IRP); Requirements   
6 [14] 3GPP TS 28.622: Telecommunication management; Generic Network Resource Model (NRM) Integration   
7 Reference Point (IRP); Information Service (IS)   
8 [15] 3GPP TS 32.341: Telecommunication management; File Transfer (FT) Integration Reference Point (IRP);   
9 Requirements   
10 [16] 3GPP TS 32.342: Telecommunication management; File Transfer (FT) Integration Reference Point (IRP);   
11 Information Service (IS)   
12 [17] 3GPP TS 32.346: Telecommunication management; File Transfer (FT) Integration Reference Point (IRP):   
13 Solution Set (SS) definitions   
14 [18] 3GPP TS 32.421: Telecommunication management; Subscriber and equipment trace; Trace concepts and   
15 requirements   
16 [19] 3GPP TS 32.422: Telecommunication management; Subscriber and equipment trace; Trace control and   
17 configuration management   
18 [20] 3GPP TS 32.423: Telecommunication management; Subscriber and equipment trace; Trace data definition   
19 and management   
20 [21] 3GPP TS 32.508: Telecommunication management; Procedure flows for multi-vendor plug-and-play eNode   
21 B connection to the network   
22 [22] 3GPP TS 32.509: Telecommunication management; Data formats for multi-vendor plug and play eNode B   
23 connection to the network   
24 [23] 3GPP TS 38.401: NG-RAN; Architecture description   
25 [24] O-RAN-WG4.MP.0-v05.00: O-RAN Alliance Working Group 4 Management Plane Specification   
26 [25] O-RAN WG1 OAM Architecture v03.00   
27 [26] RFC 6241, “Network Configuration Protocol (NETCONF)”, IETF, June 2011   
28 [27] RFC 7950, “The YANG 1.1 Data Modeling Language”, IETF, August 2016   
29 [28] 3GPP TS 32.156: Telecommunication management; Fixed Mobile Convergence (FMC) Model repertoire   
30 [29] 3GPP TS 32.160: Management and orchestration; Management service template   
31 [30] ONF TR-514: UML Modeling Guidelines   
32 [31] ONF TR-515: Papyrus Guidelines   
33 [32] ONF TR-531: UML to YANG Mapping Guidelines   
34 [33] O-RAN Information Model (from Eclipse/Papyrus); https://wiki.o-ran-sc.org/x/RYCj   
35 [34] “Modeling, Use Case and Architecture Process,” B.Cheung et al, May 2019, ONAP

# 1.2.1 Definitions and Abbreviations

# 1.2.2 Definitions

For the purposes of the present document, the terms and definitions given in 3GPP TR 21.905 [1] and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in 3GPP TR 21.905 [1].

# 1.2.3 Abbreviations and acronyms

7 For the purposes of the present document, the abbreviations given in 3GPP TR 21.905 [1] and the following apply. An   
8 abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in   
9 3GPP TR 21.905 [1].   
10   
11 3GPP $3 ^ { \mathrm { r d } }$ Generation Partnership Project   
12 API Application Programming Interface   
13 CR Change Requests   
14 EMS Element Management System   
15 FCAPS Fault, Configuration, Accounting, Performance, Security   
16 IOC Information Object Class   
17 LS Liaison Statement   
18 MANO Management and Orchestration   
19 ME Managed Element   
20 MF Managed Function   
21 MnS Management Service   
22 MO Managed Object   
23 MOC Managed Object Class   
24 MOI Managed Object Instance   
25 NAT Network Address Translation   
26 Near-RT RIC O-RAN near real time RAN Intelligent Controller   
27 NMS Network Management System   
28 Non-RT RIC O-RAN non real time RAN Intelligent Controller   
29 NRM Network Resource Model   
30 O-CU-CP O-RAN Central Unit – Control Plane.   
31 O-CU-UP O-RAN Central Unit – User Plane   
32 O-DU O-RAN Distributed Unit   
33 OMG Object Management Group   
34 O-RAN Open Radio Access Network   
35 O-RU O-RAN Radio Unit   
36 ONAP Open Network Automation Platform   
37 PNF Physical Network Function   
1 RAN Radio Access Network   
2 RRH Remote Radio Head   
3 SDO Standards Development Organization   
4 SMO Service Management and Orchestration (layer)   
5 TR Technical Report   
6 TS Technical Specification   
7 UML Unified Modeling Language   
8 SA5 Services & System Aspects Working Group 5 Telecom Management   
9 VNF Virtualized Network Function

# Chapter 2.Overview and Philosophy

# 2.1 “Prosumer” relationship between O-RAN and Standards Development Organizations

The O-RAN Alliance complements the work of other Standards Development Organizations (SDO): 3GPP, IETF, and IANA are among the primary sources for OAM (Management) specifications for O-RAN components.

3GPP published its 5G Network Resource Model (Information Model) as well as “Trial - SA5 Data models,” i.e., yang data models in a publicly available git repository with the license statement “No license. All rights reserved.”

8 In addition, 3GPP published its 4G Network Resource Model (Information Model); however, this is not yet being   
9 referenced and/or used within O-RAN. It should be noted that there is a proposal within O-RAN to model O-eNB that   
10 is likely to necessitate the inclusion of elements from 4G NRM as part of a subsequent release.   
1 To reiterate, the O-RAN Information Model, Data Models, and modeling processes should complement the work of   
12 other SDOs, not conflict or compete.   
13 Accordingly, whenever any O-RAN WG (Working Group) identifies defects and/or omissions in 3GPP models, a   
14 Change Request (CR) is fed back into 3GPP for a mutually agreed upon resolution. It should be noted, however, that   
15 there is still no formalized process for 3GPP to receive CRs from the O-RAN Alliance. This could be addressed via a   
16 statement of intent to be followed by 3GPP member companies that, more often than not, are O-RAN member   
17 companies as well.   
18 Not all identified gaps are within the 3GPP domain. Some may be specific to O-RAN and are not suitable for inclusion   
19 in 3GPP.   
20 As 3GPP CRs are approved, they are incorporated into the O1 Interface Specification. This, in turn, drives the updates   
21 that are to be made to both the Information Model and Data Models within O-RAN. Alignment should proceed as a   
22 clearly defined sequence of events.

# 2.2 Information and Data Models as a Modeling Continuum

Within O-RAN, the de facto methods and procedures with respect to the early stage of an O-RAN “modeling continuum” aim to evolve one common and coherent Information Model for providing O-RAN extensions to the existing 4G/5G IMs such as the 3GPP NRMs, from which O-RAN Data Models may be generated manually or with a set of tools.

![](images/3752997d9a2c5529d716add6483023d23ad103939c2da574afba0a8b36391893.jpg)

> **Image Summary:** (Summary not available)
  
Figure 1 Information and Data Models as a Modeling Continuum (conceptual)

# Definitions:

Information Model: a representation of concepts and the relationships, constraints, rules, and operations to specify data semantics for a chosen domain of discourse. Typically, and Information Model specifies relations between kinds of things, but may also include relations with individual things. It can provide sharable, stable, and organized structure of information requirements or knowledge for the domain context.

14 Data Model: an abstract model that organizes elements of data and standardizes how they relate to one another and to   
15 the properties of real-world entities. The term data model may refer to two distinct but closely related concepts: (1) an   
16 abstract formalization of the objects and relationships found in a particular application domain; (2) the set of concepts   
17 used in defining such formalizations - for example concepts such as entities, attributes, relations, or tables.   
18 Logical Data Model: a data model of a specific problem domain expressed independently of a particular database   
19 management product or storage technology (physical data model) but in terms of data structures such as relational tables   
20 and columns, object-oriented classes, or XML tag

Data Dictionary: a centralized repository of information about data such as meaning, relationships to other data, origin, 2 usage, and format

Component Physical Data Models: a representation of a data design as implemented, or intended to be implemented, in a database management system for each component. In the lifecycle of a project it typically derives from a logical data model and will include the database artifacts required to create relationships between tables or to achieve performance goals, such as indexes, constraint definitions, linking tables, partitioned tables or clusters

# 2.3 Information and Data Modeling Co-Evolution

The “Modeling Continuum” depicted as Figure 1 (above) is purely conceptual and is intended to provide a framework for Information and Data Modeling Co-evolution that can be applied within both O-RAN and 3GPP, laying the groundwork for collaboration.

5 Here is an example of the process to be adapted to, and adopted by, O-RAN:

![](images/97e603ea61b6ea03a391a52d70d283a869d6b3233be5f436535e8e2a45f6047c.jpg)

> **Image Summary:** (Summary not available)
  
Figure 2 Information and Data Modeling Co-Evolution

7   
8   
9   
10   
11   
12   
13   
14   
15   
16   
17   
18   
19   
20

[“Modeling, Use Case and Architecture Process,” B.Cheung et al, May 2019, ONAP]

# 2.4 Model and Use Case Development (process)

In addition, there is another evolvoing process within O-RAN and 3GPP to guide and inform Information Model and Data Model(s) development based on prioritized use cases.

Once again, alignment between O-RAN and 3GPP is paramount, as the former establishes a de facto “software-driven standard,” while the latter is responsible for the formal approval and acceptance of the full set of release-managed standards for 5G/LTE RAN

7 Here is another example of the process to be adapted to, and adopted by, O-RAN.

![](images/c437097d319e988f1383ebe37a7ad7c8f0da0d1688ef00e8171bda498b91590d.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3 Model and Use Case Development (process)

[“Modeling, Use Case and Architecture Process,” B.Cheung et al, May 2019, ONAP]

# 2.5 O-RAN components reflected within O-RAN Information Model and Data Model(s)

The work to evolve the following O-RAN components will both follow and provide feedback on the OAM Information Model and Data Models of 3GPP:

• Near-RT-RIC • O-CU-UP   
• O-CU-CP   
• O-DU   
• O-RU   
• O-eNB

1 The O-RAN entities listed below are also expected to be reflected within the O-RAN Information Model:

Non-RT-RIC: ManagedApplication (rApp), A1-Policies • Near-RT-RIC; ManagedApplication (xApp), A1 interfaces, A1 Policies, A1-Topology • E2 interfaces and E2-Topology • O2 interfaces and O2-Topology [O-Cloud is a future consideration from a modelling perspective] • O1

# 2.6 Open Issues and Future Considerations

There are numerous Open Issues and Future Considerations that are captured within the O-RAN wiki pages; however, regardless of any future considerations, the guiding principle is clear and remains unchanged, that O-RAN seeks to reuse and/or augment, not re-invent, that which already exists and has been adopted, i.e., withstood the test of time, by the telecommunications industry in the areas of Information and Data Models.

12 For the most up-to-date compendium of Open Issues and Future Considerations, please refer to the O-RAN wiki.

# Chapter 3.O-RAN Information Model

# 3.1 A general view of an Information Model

3 In general, an Information Model is an abstract but formal representation of entities including their properties,   
4 relationships and the operations that can be performed on them. In includes a representation of concepts and the   
5 relationships, constraints, rules, and operations to specify data semantics for a chosen domain of discourse:

Things (Modeled as Classes) with Definitions • Class Properties (Attributes); Class Relationships • Association Types (Simple Association, Aggregation, Composition, Inheritance) • Multiplicity and Direction • Operations/Behaviors (optional) • Represented on a Collection of Class Diagrams • Implementation Independent • Interfaces – Operations, Attributes (in, out, return)

# 3.2 Modeling approach, Unified Modeling Language (UML)

Modeling is the designing of software applications before coding. Modeling is an essential part of large software projects, and helpful to medium and even small projects as well. A model plays the analogous role in software development that blueprints and other plans (site maps, elevations, physical models) play in the building of a skyscraper.

Models raise the level of abstraction by hiding or masking details, bringing out the “big picture,” or by focusing on different aspects of a prototype.

The Information Model within O-RAN uses the Unified Modeling Language™ (UML $\textsuperscript { \textregistered }$ ) from the Object Management Group (OMG) with an open source Model-Based Engineering tool, Eclipse Papyrus.

# 3.3 IISOMI (Informal Inter-SDO Open Model Initiative) guidelines

The information model is split into a structural part and a behavioral part; i.e., data model (structural/static) is decoupled from operations model (behavioral/dynamic).

The following guidelines are sourced from a Technical Recommendation developed within IISOMI (Informal InterSDO Open Model Initiative) and originally published by the ONF:

• UML 2.5 (Unified Modeling Language) is used for specifying the model

• The model shall be management/control protocol-neutral, i.e., not reflect any middleware protocol-specific characteristics (like e.g., CORBA, HTTP, JMS)

• The model shall be map-able to various protocol-specific interfaces (it is recommended to automate this mapping supported by tools)

• It shall be possible to separate UML artifact properties which are only required for interface related (purpose specific) models.

• Traceability from each modeling construct back to requirements and use cases shall be provided whenever possible.

# 3.4 General Information on the UML Model

The following general information on the model shall be set/defined, i.e., is captured within the tool (Papyrus) that is currently being used within O-RAN:

Namespace - a unique and persistent namespace for the identifiers in the model. Organization - a human friendly written name of the SDO/Open Source Project defining the model. Contact - detailed information on the project and editor which have developed the model. Description - a brief description of the model content; 1 line (optional). Copyright - the copyright notice for the model. • License - the license statement for the model. • Revision - detailed information on this revision of the model. Each revision of the model should add an additional revision statement.

# 3.5 O-RAN Information Model

Typically, the Information Model specifies relations between kinds of things, but may also include relations with individual things. It can provide sharable, stable, and organized structure of information requirements or knowledge for the domain context.

The complete Information Model in both human- and machine-readable formats as of the date of this document may be found in O-RAN's bitbucket – refer to Appendix A.

Please make sure that you are logged in using your Atlassian user ID & password.

Note that access to the Information Model is purely for informational purposes, as the O-RAN Information Model is still under development and is not yet approved for use.

# 3.6 Classes/components and interfaces that comprise the O-RAN Information Model and Data Models

Following are a list of classes/components as well as interfaces that should be part of the O-RAN Information model, along with the working group developing this entity, any SDO references if appropriate, followed by comments and the status. This is based on the premise that each WG is responsible for modeling the entity within the modeling tool, Eclipse Papyrus, and WG1 is responsible for stewarding the overarching model inclusive of the input from the other groups.

<table><tr><td rowspan=1 colspan=1>Entity</td><td rowspan=1 colspan=1>WG DevelopingModel</td><td rowspan=1 colspan=1>Doc Reference</td><td rowspan=1 colspan=1>Comments</td><td rowspan=1 colspan=1>Status</td></tr><tr><td rowspan=1 colspan=1>Class /Component</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>NonRTRIC</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Out of scope for O-RAN, but will haveinterfaces into O-RAN components.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>NearRTRIC</td><td rowspan=1 colspan=1>WG3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Presently shell only in model.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>O-CU-CP</td><td rowspan=1 colspan=1>WG5</td><td rowspan=1 colspan=1>3GPP TS 28.541</td><td rowspan=1 colspan=1>3GPP start, including attributes</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>O-CU-UP</td><td rowspan=1 colspan=1>WG5</td><td rowspan=1 colspan=1>3GPP TS 28.541</td><td rowspan=1 colspan=1>3GPP start, including attributes</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>O-DU</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3GPP TS 28.541</td><td rowspan=1 colspan=1>3GPP start, including attributes</td><td rowspan=1 colspan=1></td></tr></table>

<table><tr><td rowspan=1 colspan=1>O-RU</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Shell only</td></tr><tr><td rowspan=1 colspan=1>ManagedElement</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3GPP TS 28.622</td><td rowspan=1 colspan=1>Class and attributes</td></tr><tr><td rowspan=1 colspan=1>Xapp</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Not present in model</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td></td></tr><tr><td rowspan=1 colspan=1>Interfaces</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>A1-P</td><td rowspan=1 colspan=1>WG2</td><td rowspan=1 colspan=1>O-RAN.WG2.A1AP-v03.00</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>A1-ML</td><td rowspan=1 colspan=1>WG2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Shell Only - to be pursued in a laterrelease</td></tr><tr><td rowspan=1 colspan=1>A1-EI</td><td rowspan=1 colspan=1>WG2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Shell Only - to be pursued in a laterrelease</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>WG1</td><td rowspan=1 colspan=1>O-RAN-WG1.01Interface -v04</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>E1</td><td rowspan=1 colspan=1>WG5</td><td rowspan=1 colspan=1>3GPP TS 38.460</td><td rowspan=1 colspan=1>3GPP start, including operations list</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>WG3</td><td rowspan=1 colspan=1>ORAN-WG3.E2GAP.0-v0.1</td><td rowspan=1 colspan=1> Interface with 9 operations</td></tr><tr><td rowspan=1 colspan=1>F1-c</td><td rowspan=1 colspan=1>WG5</td><td rowspan=1 colspan=1>3GPP TS 38.470</td><td rowspan=1 colspan=1>3GPP start, including 24 operations</td></tr><tr><td rowspan=1 colspan=1>F1-u</td><td rowspan=1 colspan=1>WG5</td><td rowspan=1 colspan=1>3GPP TS 38.470</td><td rowspan=1 colspan=1>3GPP start, including limited operationlist</td></tr><tr><td rowspan=1 colspan=1>OpenFrontHaul</td><td rowspan=1 colspan=1>WG4</td><td rowspan=1 colspan=1>front-haul mplane / cus</td><td rowspan=1 colspan=1>Shell only</td></tr><tr><td rowspan=1 colspan=1>X2</td><td rowspan=1 colspan=1>WG5</td><td rowspan=1 colspan=1>3GPP TS 36.423</td><td rowspan=1 colspan=1>3GPP based start, including a largenumber of operations</td></tr><tr><td rowspan=1 colspan=1>02</td><td rowspan=1 colspan=1>WG6</td><td rowspan=1 colspan=1>[]</td><td rowspan=1 colspan=1>Not present in model</td></tr></table>

Table 1 Classes/components and interfaces that comprise the O-RAN Information Model and Data Model(s)

# 3.7 Installing and using Papyrus

Eclipse Papyrus is an industrial-grade open source Model-Based Engineering tool. Eclipse Papyrus has notably been used successfuly in industrial projects and is the base platform for several industrial modeling tools.

Information about this tool and how to use it as well as how it is being used within O-RAN may be found in Appendix B.

# Chapter 4.O-RAN Data Models

For O1 interfaces, the O-RAN Information Model development should precede and serve as the basis for the Data Model development within each working group (WG1 through WG9).

# 4.1 Repositories; current conventions to distinguish between models under development versus models that are approved for use

The data models are developed and published in working group specific bitbucket that are expected to be available at the time this document is published:

https://bitbucket.org/bitbucket-o-ran-alliance/workgroup1   
https://bitbucket.org/bitbucket-o-ran-alliance/workgroup2   
https://bitbucket.org/bitbucket-o-ran-alliance/workgroup3   
https://bitbucket.org/bitbucket-o-ran-alliance/workgroup4   
https://bitbucket.org/bitbucket-o-ran-alliance/workgroup5   
https://bitbucket.org/bitbucket-o-ran-alliance/workgroup6   
https://bitbucket.org/bitbucket-o-ran-alliance/workgroup7   
https://bitbucket.org/bitbucket-o-ran-alliance/workgroup8   
https://bitbucket.org/bitbucket-o-ran-alliance/workgroup9

# Note that these are private repositories that include models that are under development, i.e., not yet approved for use.

O-RAN users who require access to bitbucket are instructed to email the WG co-chair(s) with “O-RAN WG_ REPO ACCESS” in the Subject: field, filling in the blank “WG_” with the number of the WG for which repository access is being requested.

The link to the public-facing repository that includes the formally released versions of models may be found within Appendix C.

There is a convention to identify formally published data models and distinguish them from models that are considered “experimental,” i.e., still under development, not yet approved for use:

The revision statement in all YANG models includes a reference statement used to cross-reference the first version of the document where the corresponding description was introduced. For example, the reference in all revision statements for the initial O-RAN models from WG4 include cross-reference to “ORAN-WG4.MP.0-v01.00”.

The revision statement of the YANG models also includes a description that is used to track the versioning of the YANG model. All revision statement descriptions will begin with “version ” ${ } ^ { \prime } < a >$ “.” $^ { \prime \prime } { < } b >$ “.” $^ { \prime \prime } { < } c >$ , where $< a >$ , ${ < b > }$ and $< c >$ are used to reflect the version of the YANG model, where

$< a >$ corresponds to the first digit of the O-RAN specification version where the corresponding description was first introduced, corresponding to $< x >$ in sub-section 1.1;

${ < } b >$ is incremented when errors in the YANG model have been corrected;

$< c >$ is incremented only in working versions of the YANG model indicating incremental changes during the editing process.

# 4.2 Formal relationship (traceability) between O-RAN Data Models and the O-RAN Information Model

At present, there is no formal relationship and/or traceability between the O-RAN Data Models and O-RAN 4 Information Model; however, this is expected to evolve over time.

As indicated within Chapter 2 “Overview and Philosophy,” there is a modeling continuum that aims to establish and evolve one common and coherent Information Model for 5G/LTE RAN from which Data Models may be generated either manually or with a set of tools.

As the modeling practices and processes within O-RAN mature, the Information Model and Data Models are expected to co-evolve to develop the APIs required by specific use cases, as depicted below.

#

![](images/525bc1f986a98359e4195b9c0537ded9d4e02e013cd3efaae125c35609fd3123.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4 Information and Data Modeling Co-Evolution

11   
12   
13   
14   
15   
16   
17   
18   
19   
20   
21

[“Modeling, Use Case and Architecture Process,” B.Cheung et al, May 2019, ONAP]

# 1 4.3 Usage of 3GPP Data Models

The O-RAN Alliance complements the work of other SDOs. 3GPP is the primary source for management plane specifications for O-RAN components. 3GPP has published its “Trial - SA5 Data models” including its yang data models in a public available git repository with the license statement “No license. All rights reserved.”

Please refer to Appendix C for the 3GPP-source Data Models that are approved for use.

The following table (snapshot) shows a subset of the mapping of 3GPP yang data models to O-RAN element functions as defined by OAM Architecture Specifications. For the most current mapping, please refer to the O-RAN wiki.

8

<table><tr><td rowspan=1 colspan=1>3GPP yang datamodel</td><td rowspan=1 colspan=1>3GPP spec forYANG model</td><td rowspan=1 colspan=1>o-ru(in hybrid mode)</td><td rowspan=1 colspan=1>o-du</td><td rowspan=1 colspan=1>o-cu-up</td><td rowspan=1 colspan=1>o-cu-cp</td><td rowspan=1 colspan=1>near-rt-ric</td></tr><tr><td rowspan=1 colspan=1>_3gpp-5g-common-yang-types</td><td rowspan=1 colspan=1>3GPP TS 28.541</td><td rowspan=1 colspan=1>imported by_3gpp-common-managed-element</td><td rowspan=1 colspan=1>imported by_3gpp-common-managed-element</td><td rowspan=1 colspan=1>imported by_3gpp-common-managed-element</td><td rowspan=1 colspan=1>imported by_3gpp-common-managed-element</td><td rowspan=1 colspan=1>imported by_3gpp-common-managed-element</td></tr><tr><td rowspan=1 colspan=1>_3gpp-common-ep-rp</td><td rowspan=1 colspan=1>3GPP TS 28.623</td><td rowspan=1 colspan=1>[open] o-ran-m-int.yang &amp; o-ran-ru-if yang defines theinterface of O-RU,maybe it is notneeded to O-RU</td><td rowspan=1 colspan=1>imported by_3gpp-nr-nrm-epabstract superclassfor all 3GPPendpoints[open] as O-RUremote PORT, toconfigure eCPRIport of O-DU justEP_RP looks notenough</td><td rowspan=1 colspan=1>imported by_3gpp-nr-nrm-epabstractsuperclass foralll3GPP endpoints</td><td rowspan=1 colspan=1>imported by_3gpp-nr-nrm-epabstractsuperclass for all3GPP endpoints</td><td rowspan=1 colspan=1>[open] needdiscussion, fRIC modeled asO-RU whichneed detailedconfiguration tointerfaces, thecommon partprobably fromIETF</td></tr><tr><td rowspan=1 colspan=1>_3gpp-common-当</td><td rowspan=1 colspan=1>3GPP TS 28.623</td><td rowspan=1 colspan=1>imported by_3gpp-common-managed-elementneeded for alarm listhandling</td><td rowspan=1 colspan=1>imported by_3gpp-common-managed-elementneeded for alarm listhandling</td><td rowspan=1 colspan=1>imported by_3gpp-common-managed-elementneeded for alarmlist handling</td><td rowspan=1 colspan=1>imported by_3gpp-common-managed-elementneeded for alarmlist handling</td><td rowspan=1 colspan=1>imported by_3gpp-common-managed-elementneeded foralarm listhandling</td></tr><tr><td rowspan=1 colspan=1>_3gpp-common-managed-element</td><td rowspan=1 colspan=1>3GPP TS 28.623</td><td rowspan=1 colspan=1>root object class</td><td rowspan=1 colspan=1>root object class</td><td rowspan=1 colspan=1>root object class</td><td rowspan=1 colspan=1>root object class</td><td rowspan=1 colspan=1>root objectclass</td></tr><tr><td rowspan=1 colspan=1>_3gpp-common-managed-function</td><td rowspan=1 colspan=1>3GPP TS 28.623</td><td rowspan=1 colspan=1>needed to extendMF for O-RUfunctionality</td><td rowspan=1 colspan=1>imported by_3gpp-nr-nrm-gnbdufunction</td><td rowspan=1 colspan=1>imported by_3gpp-nr-nrm-gnbcuupfunction</td><td rowspan=1 colspan=1>imported by_3gpp-nr-nrm-gnbcuCPfunction</td><td rowspan=1 colspan=1>needed eitherfor a standaloneRIC orcombined RICME</td></tr><tr><td rowspan=1 colspan=1>_3gpp-common-measurements</td><td rowspan=1 colspan=1>3GPP TS 28.623</td><td rowspan=1 colspan=1>imported by_3gpp-common-managed-elementneeded for PM jobcontrol andthreshold monitoring</td><td rowspan=1 colspan=1>imported by_3gpp-common-managed-elementneeded for PM jobcontrol andthreshold monitoring</td><td rowspan=1 colspan=1>imported by_3gpp-common-managed-elementneeded for PM jobcontrol andthresholdmonitoring</td><td rowspan=1 colspan=1>imported by_3gpp-common-managed-elementneeded for PMjob control andthresholdmonitoring</td><td rowspan=1 colspan=1>imported by_3gpp-common-managed-elementneeded for PMjob control andthresholdmonitoring</td></tr><tr><td rowspan=1 colspan=1></td><td></td><td></td><td rowspan=1 colspan=1></td><td></td><td></td><td></td></tr></table>

![](images/ffdada0f3fd7ad6f0a5c76515e0a6caa7b103dbc014ca300910293d4f2d58c24.jpg)

> **Image Summary:** (Summary not available)


# 4.4 Usage of non-3GPP data models

There are domains of data-models being considered by O-RAN WGs (Working Groups) that are not covered by 3GPP but are covered by other SDOs, e.g., IETF, MEF, IEEE, ONF, BBF, and occasionally imported by 3GPP.

Note that this is merely a snapshot as of the date of this document and is expected to be revisited as part of subsequent release(s).

The following table shows data models that are of interest and being considered within O-RAN and/or 3GPP:

<table><tr><td colspan="1" rowspan="1">OrderNo</td><td colspan="1" rowspan="1">yang datamodel</td><td colspan="1" rowspan="1">o-ru (to berevised toseparate 01and M-Plane)</td><td colspan="1" rowspan="1">o-du</td><td colspan="1" rowspan="1">o-cu-up</td><td colspan="1" rowspan="1">o-cu-cp</td><td colspan="1" rowspan="1">near-rt-ric</td><td colspan="1" rowspan="1">Comments</td></tr><tr><td colspan="1" rowspan="1">001</td><td colspan="1" rowspan="1">ietf-yang-types</td><td colspan="1" rowspan="1">import byseveral modelsincluding _3gpp-common-yang-types.yang</td><td colspan="1" rowspan="1">import by_3gpp-common-yang-types.yang</td><td colspan="1" rowspan="1">import by_3gpp-common-yang-types.yang</td><td colspan="1" rowspan="1">import by_3gpp-common-yang-types.yang</td><td colspan="1" rowspan="1">import by_3gpp-common-yang-types.yang</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">002</td><td colspan="1" rowspan="1">ietf-inet-types</td><td colspan="1" rowspan="1">import byseveral modelsincluding _3gpp-common-yang-types.yang</td><td colspan="1" rowspan="1">import by_3gpp-common-yang-types.yang</td><td colspan="1" rowspan="1">import by_3gpp-common-yang-types.yang</td><td colspan="1" rowspan="1">import by_3gpp-common-yang-types.yang</td><td colspan="1" rowspan="1">import by_3gpp-common-yang-types.yang</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">011</td><td colspan="1" rowspan="1">ietf-netconf.yang</td><td colspan="1" rowspan="1">must have</td><td colspan="1" rowspan="1">must have</td><td colspan="1" rowspan="1">must have</td><td colspan="1" rowspan="1">must have</td><td colspan="1" rowspan="1">must have</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">012</td><td colspan="1" rowspan="1">ietf-netconf-acm.yang</td><td colspan="1" rowspan="1">baseline foraccess control</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Network ConfigurationAccess Control Model</td></tr><tr><td colspan="1" rowspan="1">013</td><td colspan="1" rowspan="1">ietf-netconf-monitoring</td><td colspan="1" rowspan="1">used by WG4 M-Plane</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">NETCONF MonitoringModule</td></tr><tr><td colspan="1" rowspan="1">014</td><td colspan="1" rowspan="1">ietf-netconf-nmda</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">NETCONF operations tosupportthe Network ManagementDatastore Architecture</td></tr><tr><td colspan="1" rowspan="1">015</td><td colspan="1" rowspan="1">ietf-netconf-notifications</td><td colspan="1" rowspan="1">not O1 butOpenFronthaulmPlane</td><td colspan="1" rowspan="1">not O1 butOpenFronthaulmPlane</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">This module defines aYANG data model for usewith theNETCONF protocol thatallows the NETCONF clientto receive commonNETCONF base eventnotifications</td></tr><tr><td colspan="1" rowspan="1">016</td><td colspan="1" rowspan="1">ietf-netconf-partial-lock</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">017</td><td colspan="1" rowspan="1">ietf-netconf-time</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">time-triggered configurationand managementoperations</td></tr><tr><td colspan="1" rowspan="1">018</td><td colspan="1" rowspan="1">ietf-netconf-with-defaults</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">NETCONF client to controlhow default values arehandled by the server inparticular NETCONFoperations</td></tr><tr><td colspan="1" rowspan="1">020</td><td colspan="1" rowspan="1">ietf-system</td><td colspan="1" rowspan="1">overlaps with o-ran-operationsbut may berequired tosupport 802.1X</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">configuration andidentification of somecommon systemproperties within a devicecontaining aNETCONFserver●  time-zonemanagement●  radius●  local users● NTP</td></tr><tr><td colspan="1" rowspan="1">030</td><td colspan="1" rowspan="1">ietf-hardware</td><td colspan="1" rowspan="1">not O1 butOpenFronthaulmPlane</td><td colspan="1" rowspan="1">not O1 butOpenFronthaulmPlane</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">031</td><td colspan="1" rowspan="1">iana-hardware</td><td colspan="1" rowspan="1">import by ietf-hardware</td><td colspan="1" rowspan="1">import by ietf-hardware</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">IANA-defined identities forhardware class.</td></tr><tr><td colspan="1" rowspan="1">032</td><td colspan="1" rowspan="1">ietf-hardware-state</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">hardware monitoring</td></tr><tr><td colspan="1" rowspan="1">033</td><td colspan="1" rowspan="1">ietf-interfaces</td><td colspan="1" rowspan="1">foundation forfronthaul</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">034</td><td colspan="1" rowspan="1">iana-if-type</td><td colspan="1" rowspan="1">not O1 butOpenFronthaulmPlane</td><td colspan="1" rowspan="1">not O1 butOpenFronthaulmPlane</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">YANG identities for IANA-registeredinterface types</td></tr><tr><td colspan="1" rowspan="1">040</td><td colspan="1" rowspan="1">ietf-alarms</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">This module defines aninterface for managingalarms.</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">ietf-ip</td><td colspan="1" rowspan="1">foundation forfronthaul M-Plane</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">managing IPimplementations</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">ietf-ptp</td><td colspan="1" rowspan="1">considered - butdecided o defineowno-ran-sync.yang</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">configuration of IEEE Std1588-2008 clocks</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">ietf-yang-library</td><td colspan="1" rowspan="1">foundation forYANG 1.1</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">ietf-yang-metadata</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">This YANG module definesan'extension' statementthat allowsfor defining metadataannotations</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">ietf-yang-patch</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">This module containsconceptual YANGspecifications for theYANG Patch and YANGPatch Status datastructures.</td></tr></table>

Copyright $\circledcirc$ 2021 by the O-RAN Alliance e.V. Your use is subject to the terms of the O-RAN Adopter License Agreement in Annex ZZZ Page 20

Table 3 Non 3GPP yang models   

<table><tr><td rowspan=1 colspan=1>ietf-yang-push</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>ietf-yang-schema-mount</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>This module defines aYANG extension statementthat can be used toincorporate data modelsdefined in other YANGmodules in amodule.</td></tr><tr><td rowspan=1 colspan=1>ietf-yang-smiv2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>This module defines YANGextensions that are used totranslateSMIv2 concepts intoYANG.</td></tr><tr><td rowspan=1 colspan=1>iana-crypto-hash</td><td rowspan=1 colspan=1>used in CTI</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>ietf-crypto-types</td><td rowspan=1 colspan=1>used byfronthaul filemanagement</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>ieee802-dot1x</td><td rowspan=1 colspan=1>beingconsidered bySTG</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

# 4.5 YANG Conventions

This section describes the recommended conventions to be used in the O-RAN Alliance when writing YANG models.

In particular, because the creation and maintenance of YANG models is expected to be distributed across different working groups, this guide is intended to ensure that the way the models are organized and presented will be consistent across the entirety of the O-RAN Alliance.

# 4.5.1 Naming

MODULE FILE NAMING: M-Plane YANG modules should have filenames of the form “o-ran-xxx.yang” (for O1 the file naming is TBD)

MODULE NAMESPACE: YANG modules should have a namespace defined of the form namespace "urn:oran:xxx:version"; where version represents an increasing numerical integer value and where the value used in all newly defined models is "1". The module namespace version will be incremented when any non-backwards compatible changes are introduced into a model.

16 PREFIX NAMING: Each module requires a prefix statement with a prefix that other dependent modules will use (also   
17 used in path references within the same module). Prefixes should be short and clear, with abbreviations as appropriate.   
18 Module prefixes should be of the form: o-ran-xxx, or or-xxx, and must be unique regardless of over which interface the   
19 YANG module is exposed (ex. O1 or Open FrontHaul M-Plane).

# 4.5.2 Revision Statement

The revision statement in all YANG models includes a reference statement used to cross-reference to the version of a particular O-RAN publication where the corresponding functionality was initially introduced. The revision statement of the YANG models also includes a description that is used to track the versioning of the YANG model. All revision

statement descriptions will begin with version a.b.c, where a, b and c are used to reflect the version of the YANG model, where ‘a’ corresponds to the first digit of the O-RAN specification version where the corresponding description was first introduced; ‘b’ is incremented when errors in the YANG model have been corrected; ‘c’ is incremented only in working versions of the YANG model indicating incremental changes during the editing process. Hence, all published versions of O-RAN alliance YANG models should have this value set to zero.

# 4.5.3 Indents

O-RAN Alliance YANG models should use two-space tab indents.

# 4.5.4 YANG Language Usage

YANG VERSION: All models should use YANG data modeling language version 1.1 [1] (RFC 7950) and follow the Guidelines for Authors and Reviewers of YANG Data Model Documents [RFC 6087].

TOP-LEVEL DATA NODE: There should only be one top-level data node defined in each YANG module, if any data nodes are defined at all.

NMDA (Network Management Datastore Architecture): No O-RAN YANG models should prevent the use of NMDA [RFC 8342].

KEY-LESS LISTS OF OPERATIONAL STATE: Although permitted in YANG, the use of a list that consists of operational-state without a defined key should be avoided.

17 VALIDATION: All YANG modules should be validated / compiled with pyang tool using the following flag: pyang --   
18 lint <module>. Note, successful compilation with pyang does not guarantee a working model, as xPATH expressions   
19 aren't evaluated and forbidden operational data dependencies in the configuration may not generate appropriate errors.

NETCONF ACCESS CONTROL: Sensitive data within models should be tagged with an appropriate "nacm:default" statement. O-RAN makes use of NACM (NETCONF Access Control Model RFC 8341) rules to define the privileges associated with user groupings. An O-RAN NETCONF server should hard code these restrictions into the server. The defined NACM rules are therefore unmodifiable, with the rules being used to provide an "external indication" of such restrictions.

CONSTRAINTS: Generally, O-RAN systems should strive to consider a blank configuration to be a valid config.

# 4.5.5 Cross Working Group Co-ordination

Models that are likely to be applicable to more than one O-RAN Alliance working group should provide clear delineation between separate working groups configuration and/or state. The use of feature and if-feature is recommended to ensure that NETCONF servers are not required to implement the entire data model, e.g., when aspects of such relate to the individual working group defined use cases. The feature name should indicate which working group the capabilities have been defined by.

# Annex A: Link to Information Model source (under 2 development; not approved for use)

Papyrus sources for the O-RAN Information Model can be found in O-RAN's bitbucket: https://bitbucket.org/bitbucketo-ran-alliance/workgroup1/src/master/Working/information-model/papyrus/.

6 Please make sure that you are logged in using your Atlassian userID and password.

# Annex B: Installing and using Eclipse Papyrus [refer to ORAN wiki for the most up-to-date guidelines]

Eclipse Papyrus is an industrial-grade open source Model-Based Engineering tool. Eclipse Papyrus has notably been used successfuly in industrial projects and is the base platform for several industrial modeling tools.

5 Eclipse Papyrus provides editors for all the UML diagrams:

• Class Diagram   
• Object Diagram   
• Package Diagram   
• Composite Structure Diagram   
• Component Diagram   
• Deployment Diagram   
• Profile Diagram   
• Use case Diagram   
• Activity Diagram   
• State machine Diagram   
• Communication Diagram   
• Sequence Diagram   
• Timing Diagram   
• Interaction overview Diagram

# Installation

The Open Source UML tool Papyrus is a plug-in for the Open Source integrated development environment (IDE) Eclipse. GenDoc is the associated tool that allows you to output a model in Papyrus into a word document. The artifacts in the output (diagrams, classes, datatypes, etc.) can be copy/pasted directly into a model project's wiki page.

Currently applied tool versions:

Eclipse: version 4.8 "Photon" • Papyrus: version 4.0.0 • GenDoc: version 0.6.0

Note: the full list of IISOMI-recommended modelling tool downloads in all versions is here: https://wiki.opennetworking.org/display/OIMT/Papyrus+Releases

● • Eclipse   
Eclipse "Photon" Modeling Tools package version 4.8 can be downloaded from here: {+}https://www.eclipse.org/downloads/packages/release/photon/r/eclipse-modeling-tools+ Select the download link that is appropriate for the machine on which you will be making the install, i.e. "Windows 64-bit"   
This results in the download of a zip file.   
• Note that Eclipse Photon requires a 1.8 compatible JVM Extract the contents of the zip file to wherever you would like to install Eclipse. On a PC, "Program Files" is always a good option.   
• The content of the extracted files should look something like this: configuration dropins features p2 plugins readme .eclipseproduct about.html artifacts.xml eclipse.exe eclipse.ini   
eclipsec.exe epl-v10.html   
②notice.html To launch eclipse, double-click on the "eclipse.exe" file   
• When Eclipse starts coming up, it will prompt you for a "Workspace", providing a default that you can override.   
• This is where the Eclipse projects, with associated models, will be stored.   
• When Eclipse fully comes up, you can close the Welcome tab To verify you have the correct installation of the product, go to "Help" "About Eclipse"

• You should see something that looks like Eclipse Modeling Tools Version: Photon Release (4.8.0) Build id: 20180619-1200

![](images/1186161bd1ca5ce635e1cdbb94dd2010eae0d55afbfe702c88869349f8cd3ea3.jpg)

> **Image Summary:** (Summary not available)


this:

You have now successfully installed Eclipse

• Papyrus

Papyrus Photon version 4.0.0 can be downloaded from here: {+}https://www.eclipse.org/papyrus/download.html+

• Scroll down on the right side of the page and select: "Papyrus Photon 4.0.0 " and select "Download Page"

This takes you to "Papyrus Update Site for Photon"

Copy the URL of the update site to which it takes you. Should be something like: {+}https://download.eclipse.org/modeling/mdt/papyrus/updates/releases/photon/+ ({+}https://download.eclipse.org/modeling/mdt/papyrus/updates/releases/2019-06/+ for latest version)

Now you go back into Eclipse and select "Help" "Install new software"

![](images/bb7ce15db071a43c4bcea31072ed5808745c6e2db44a07baeb38617e6cbcbac2.jpg)

> **Image Summary:** (Summary not available)


• An "Available Software" screen comes up. Paste your URL into the "Work with:" box and hit enter   
There should be multiple "Papyrus" related packages available to install. Select only the box: "Papyrus" and make sure the others are not selected.   
Click "Next" to install the product. The installation will check for dependencies and requirements   
You will get a screen indicating what will be installed o Papyrus for UML o Papyrus for UML Developer Resources   
• Select Next   
The install will then prompt you to "Accept" the license agreement   
• Once accepted, you can select "Finish" and the installation process continues. Note: The installation might take a while, and perhaps even appear to hang for a while. You can see in the lower right hand corner of Installing Software:(48%） 一 Eclipse the progress on the install. When the installation is finished, restart Eclipse to begin to use Papyrus.   
• Go to "Window" "Perspective" "Open Perspective" "Other" and select Papyrus.   
• You will now be in the Papyrus Perspective where you can begin to use Papyrus.   
• GenDoc

The Gendoc plugin is used in conjunction with a document template. The template contains instructions that enable generation of a Microsoft Word document. The document can include extracts from the model such as diagrams, class definitions, attribute definitions along with their stereotypes etc as well as figures and text directly entered into the template.

• In Eclipse, go to "Help" "Install new software"   
• Enter the GenDoc site: {+}http://download.eclipse.org/gendoc/updates/releases/0.6.0/+ in the "Work with"

![](images/391bbdcc1716e22066409d5b25daa4818c9bf5b221c354dedb2db2c9d0907789.jpg)

> **Image Summary:** (Summary not available)


3 section and hit enter.

• The "gendoc" package should show. Select this package and hit "Next".   
• Follow the instructions to complete the installation. Note: You may get a warning message about installing software that contains unsigned content - select "Install anyway".   
• A Restart will be required to apply the changes.

# Annex C: Links to Data Models approved for use

From O-RAN

The public facing web page that includes the formally released versions of models that are approved for use:

www.o-ran.org/specifications

From 3GPP

3GPP is one of the sources for management plane specifications for O-RAN components. 3GPP publishes its “SA5 Data models” including its yang data models in a public available git repository:

https://forge.3gpp.org/rep/sa5/MnS

# From IETF

IETF is a complementary source for management plane specifications for O-RAN components. IETF publishes its yang data models (inclusive of IANA yang data models) in a public available git repository:

https://github.com/YangModels/yang/tree/master/standard/ietf

# Annex ZZZ : O-RAN Adopter License Agreement

BY DOWNLOADING, USING OR OTHERWISE ACCESSING ANY O-RAN SPECIFICATION, ADOPTER AGREES TO THE TERMS OF THIS AGREEMENT.

This O-RAN Adopter License Agreement (the “Agreement”) is made by and between the O-RAN Alliance and the entity that downloads, uses or otherwise accesses any O-RAN Specification, including its Affiliates (the “Adopter”).

This is a license agreement for entities who wish to adopt any O-RAN Specification.

# 7 Section 1: DEFINITIONS

1.1 “Affiliate” means an entity that directly or indirectly controls, is controlled by, or is under common control with another entity, so long as such control exists. For the purpose of this Section, “Control” means beneficial ownership of fifty $( 5 0 \% )$ percent or more of the voting stock or equity in an entity.

11 1.2 “Compliant Implementation” means any system, device, method or operation (whether implemented in hardware,   
12 software or combinations thereof) that fully conforms to a Final Specification.   
3 1.3 “Adopter(s)” means all entities, who are not Members, Contributors or Academic Contributors, including their   
4 Affiliates, who wish to download, use or otherwise access O-RAN Specifications.

1.4 “Minor Update” means an update or revision to an O-RAN Specification published by O-RAN Alliance that does not add any significant new features or functionality and remains interoperable with the prior version of an O-RAN Specification. The term “O-RAN Specifications” includes Minor Updates.

1.5 “Necessary Claims” means those claims of all present and future patents and patent applications, other than design patents and design registrations, throughout the world, which (i) are owned or otherwise licensable by a Member, Contributor or Academic Contributor during the term of its Member, Contributor or Academic Contributorship; (ii) such Member, Contributor or Academic Contributor has the right to grant a license without the payment of consideration to a third party; and (iii) are necessarily infringed by a Compliant Implementation (without considering any Contributions not included in the Final Specification). A claim is necessarily infringed only when it is not possible on technical (but not commercial) grounds, taking into account normal technical practice and the state of the art generally available at the date any Final Specification was published by the O-RAN Alliance or the date the patent claim first came into existence, whichever last occurred, to make, sell, lease, otherwise dispose of, repair, use or operate a Compliant Implementation without infringing that claim. For the avoidance of doubt in exceptional cases where a Final Specification can only be implemented by technical solutions, all of which infringe patent claims, all such patent claims shall be considered Necessary Claims.

1.6 “Defensive Suspension” means for the purposes of any license grant pursuant to Section 3, Member, Contributor, Academic Contributor, Adopter, or any of their Affiliates, may have the discretion to include in their license a term allowing the licensor to suspend the license against a licensee who brings a patent infringement suit against the licensing Member, Contributor, Academic Contributor, Adopter, or any of their Affiliates.

# Section 2: COPYRIGHT LICENSE

2.1 Subject to the terms and conditions of this Agreement, O-RAN Alliance hereby grants to Adopter a nonexclusive, nontransferable, irrevocable, non-sublicensable, worldwide copyright license to obtain, use and modify O-RAN Specifications, but not to further distribute such O-RAN Specification in any modified or unmodified way, solely in furtherance of implementations of an O-RAN

Specification.

2.2 Adopter shall not use O-RAN Specifications except as expressly set forth in this Agreement or in a separate written agreement with O-RAN Alliance.

# Section 3: FRAND LICENSE

3.1 Members, Contributors and Academic Contributors and their Affiliates are prepared to grant based on a separate Patent License Agreement to each Adopter under Fair Reasonable And Non- Discriminatory (FRAND) terms and conditions with or without compensation (royalties) a nonexclusive, non-transferable, irrevocable (but subject to Defensive Suspension), non-sublicensable, worldwide patent license under their Necessary Claims to make, have made, use, import, offer to sell, lease, sell and otherwise distribute Compliant Implementations; provided, however, that such license shall not extend: (a) to any part or function of a product in which a Compliant Implementation is incorporated that is not itself part of the Compliant Implementation; or (b) to any Adopter if that Adopter is not making a reciprocal

Copyright $\circledcirc$ 2021 by the O-RAN Alliance e.V. Your use is subject to the terms of the O-RAN Adopter License Agreement in Annex ZZZ

1 grant to Members, Contributors and Academic Contributors, as set forth in Section 3.3. For the avoidance of doubt, the   
2 foregoing licensing commitment includes the distribution by the Adopter’s distributors and the use by the Adopter’s   
3 customers of such licensed Compliant Implementations.

3.2 Notwithstanding the above, if any Member, Contributor or Academic Contributor, Adopter or their Affiliates has reserved the right to charge a FRAND royalty or other fee for its license of Necessary Claims to Adopter, then Adopter is entitled to charge a FRAND royalty or other fee to such Member, Contributor or Academic Contributor, Adopter and its Affiliates for its license of Necessary Claims to its licensees.

8 3.3 Adopter, on behalf of itself and its Affiliates, shall be prepared to grant based on a separate Patent License   
9 Agreement to each Members, Contributors, Academic Contributors, Adopters and their Affiliates under Fair   
10 Reasonable And Non-Discriminatory (FRAND) terms and conditions with or without compensation (royalties) a   
11 nonexclusive, non-transferable, irrevocable (but subject to Defensive Suspension), non-sublicensable, worldwide patent   
12 license under their Necessary Claims to make, have made, use, import, offer to sell, lease, sell and otherwise distribute   
13 Compliant Implementations; provided, however, that such license will not extend: (a) to any part or function of a   
14 product in which a Compliant Implementation is incorporated that is not itself part of the Compliant Implementation; or   
15 (b) to any Members, Contributors, Academic Contributors, Adopters and their Affiliates that is not making a reciprocal   
16 grant to Adopter, as set forth in Section 3.1. For the avoidance of doubt, the foregoing licensing commitment includes   
17 the distribution by the Members’, Contributors’, Academic Contributors’, Adopters’ and their Affiliates’ distributors   
18 and the use by the Members’, Contributors’, Academic Contributors’, Adopters’ and their Affiliates’ customers of such   
19 licensed Compliant Implementations.

# Section 4: TERM AND TERMINATION

4.1 This Agreement shall remain in force, unless early terminated according to this Section 4.

4.2 O-RAN Alliance on behalf of its Members, Contributors and Academic Contributors may terminate this Agreement if Adopter materially breaches this Agreement and does not cure or is not capable of curing such breach within thirty (30) days after being given notice specifying the breach.

4.3 Sections 1, 3, 5 - 11 of this Agreement shall survive any termination of this Agreement. Under surviving Section 3, after termination of this Agreement, Adopter will continue to grant licenses (a) to entities who become Adopters after the date of termination; and (b) for future versions of O-RAN Specifications that are backwards compatible with the version that was current as of the date of termination.

# Section 5: CONFIDENTIALITY

Adopter will use the same care and discretion to avoid disclosure, publication, and dissemination of O-RAN Specifications to third parties, as Adopter employs with its own confidential information, but no less than reasonable care. Any disclosure by Adopter to its Affiliates, contractors and consultants should be subject to an obligation of confidentiality at least as restrictive as those contained in this Section. The foregoing obligation shall not apply to any information which is: (1) rightfully known by Adopter without any limitation on use or disclosure prior to disclosure; (2) publicly available through no fault of Adopter; (3) rightfully received without a duty of confidentiality; (4) disclosed by O-RAN Alliance or a Member, Contributor or Academic Contributor to a third party without a duty of confidentiality on such third party; (5) independently developed by Adopter; (6) disclosed pursuant to the order of a court or other authorized governmental body, or as required by law, provided that Adopter provides reasonable prior written notice to O-RAN Alliance, and cooperates with O-RAN Alliance and/or the applicable Member, Contributor or Academic Contributor to have the opportunity to oppose any such order; or (7) disclosed by Adopter with O-RAN Alliance’s prior written approval.

# 42 Section 6: INDEMNIFICATION

43 Adopter shall indemnify, defend, and hold harmless the O-RAN Alliance, its Members, Contributors or Academic   
44 Contributors, and their employees, and agents and their respective successors, heirs and assigns (the “Indemnitees”),   
45 against any liability, damage, loss, or expense (including reasonable attorneys’ fees and expenses) incurred by or   
46 imposed upon any of the Indemnitees in connection with any claims, suits, investigations, actions, demands or   
47 judgments arising out of Adopter’s use of the licensed O-RAN Specifications or Adopter’s commercialization of   
48 products that comply with O-RAN Specifications.

# Section 7: LIMITATIONS ON LIABILITY; NO WARRANTY

50 EXCEPT FOR BREACH OF CONFIDENTIALITY, ADOPTER’S BREACH OF SECTION 3, AND ADOPTER’S   
51 INDEMNIFICATION OBLIGATIONS, IN NO EVENT SHALL ANY PARTY BE LIABLE TO ANY OTHER   
1 PARTY OR THIRD PARTY FOR ANY INDIRECT, SPECIAL, INCIDENTAL, PUNITIVE OR CONSEQUENTIAL   
2 DAMAGES RESULTING FROM ITS PERFORMANCE OR NON-PERFORMANCE UNDER THIS AGREEMENT,   
3 IN EACH CASE WHETHER UNDER CONTRACT, TORT, WARRANTY, OR OTHERWISE, AND WHETHER OR   
4 NOT SUCH PARTY HAD ADVANCE NOTICE OF THE POSSIBILITY OF SUCH DAMAGES. O-RAN   
5 SPECIFICATIONS ARE PROVIDED “AS IS” WITH NO WARRANTIES OR CONDITIONS WHATSOEVER,   
6 WHETHER EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE. THE O-RAN ALLIANCE AND THE   
7 MEMBERS, CONTRIBUTORS OR ACADEMIC CONTRIBUTORS EXPRESSLY DISCLAIM ANY WARRANTY   
8 OR CONDITION OF MERCHANTABILITY, SECURITY, SATISFACTORY QUALITY, NONINFRINGEMENT,   
9 FITNESS FOR ANY PARTICULAR PURPOSE, ERROR-FREE OPERATION, OR ANY WARRANTY OR   
10 CONDITION FOR O-RAN SPECIFICATIONS.

# 11 Section 8: ASSIGNMENT

Adopter may not assign the Agreement or any of its rights or obligations under this Agreement or make any grants or other sublicenses to this Agreement, except as expressly authorized hereunder, without having first received the prior, written consent of the O-RAN Alliance, which consent may be withheld in O-RAN Alliance’s sole discretion. O-RAN Alliance may freely assign this Agreement.

# Section 9: THIRD-PARTY BENEFICIARY RIGHTS

Adopter acknowledges and agrees that Members, Contributors and Academic Contributors (including future Members, Contributors and Academic Contributors) are entitled to rights as a third-party beneficiary under this Agreement, including as licensees under Section 3.

# Section 10: BINDING ON AFFILIATES

Execution of this Agreement by Adopter in its capacity as a legal entity or association constitutes that legal entity’s or association’s agreement that its Affiliates are likewise bound to the obligations that are applicable to Adopter hereunder and are also entitled to the benefits of the rights of Adopter hereunder.

# Section 11: GENERAL

This Agreement is governed by the laws of Germany without regard to its conflict or choice of law provisions.

This Agreement constitutes the entire agreement between the parties as to its express subject matter and expressly supersedes and replaces any prior or contemporaneous agreements between the parties, whether written or oral, relating to the subject matter of this Agreement.

Adopter, on behalf of itself and its Affiliates, agrees to comply at all times with all applicable laws, rules and regulations with respect to its and its Affiliates’ performance under this Agreement, including without limitation, export control and antitrust laws. Without limiting the generality of the foregoing, Adopter acknowledges that this Agreement prohibits any communication that would violate the antitrust laws.

By execution hereof, no form of any partnership, joint venture or other special relationship is created between Adopter, or O-RAN Alliance or its Members, Contributors or Academic Contributors. Except as expressly set forth in this Agreement, no party is authorized to make any commitment on behalf of Adopter, or O-RAN Alliance or its Members, Contributors or Academic Contributors.

In the event that any provision of this Agreement conflicts with governing law or if any provision is held to be null, void or otherwise ineffective or invalid by a court of competent jurisdiction, (i) such provisions will be deemed stricken from the contract, and (ii) the remaining terms, provisions, covenants and restrictions of this Agreement will remain in full force and effect. Any failure by a party or third party beneficiary to insist upon or enforce performance by another party of any of the provisions of this Agreement or to exercise any rights or remedies under this Agreement or otherwise by law shall not be construed as a waiver or relinquishment to any extent of the other parties’ or third party beneficiary’s right to assert or rely upon any such provision, right or remedy in that or any other instance; rather the same shall be and remain in full force and effect.