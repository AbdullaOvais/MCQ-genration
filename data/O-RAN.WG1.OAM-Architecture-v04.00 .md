# O-RAN Operations and Maintenance Architecture

# This is a re-published version of the attached final specification.

For this re-published version, the prior versions of the IPR Policy will apply, except that the previous requirement for Adopters (as defined in the earlier IPR Policy) to agree to an O-RAN Adopter License Agreement to access and use Final Specifications shall no longer apply or be required for these Final Specifications after 1st July 2022.

The copying or incorporation into any other work of part or all of the material available in this specification in any form without the prior written permission of O-RAN ALLIANCE e.V. is prohibited, save that you may print or download extracts of the material on this site for your personal use, or copy the material on this site for the purpose of sending to individual third parties for their information provided that you acknowledge O-RAN ALLIANCE as the source of the material and that you inform the third party that these conditions apply to them and that they must comply with them.

# O-RAN Operations and Maintenance Architecture

Copyright $^ ©$ 2021 by the O-RAN ALLIANCE e.V.

By using, accessing or downloading any part of this O-RAN specification document, including by copying, saving, distributing, displaying or preparing derivatives of, you agree to be and are bound to the terms of the O-RAN Adopter License Agreement contained in Annex ZZZ of this specification. All other rights reserved.

# Contents

3 Chapter 1. Introductory Material .. .............................................................................................. .....3   
4 1.1 Scope ......   
5 6 1.2 1.3 References.....................................................................................................................................................Definitions and Abbreviations ...................................................................................................................... ... 3   
7 8 1.3.1 1.3.2 Definitions.........Abbreviations .... ........................... ............................................................... .............................. 4   
....................................................................................................................................... 5   
9 Chapter 2. O-RAN Overview .. ................................................................................................ ....6   
10 2.1 Scope and Objectives....... ........................... ................................................................................................ 6   
11 2.2 End to End OAM Use Cases.............................................................................................................................. 6   
12 2.2.1 O-RAN Service Provisioning ......................... .............................................................................................. 6   
13 2.2.2 O-RAN Measurement Data Collection ...................................................................................................... 11   
14 Chapter 3. OAM Architecture .... ...........................................................................................................19   
15 16 3.1 3.2 Architectural Principles ................................................................................................................................... 19Architecture Requirements .............................................................................................................................. 19   
17 3.2.1 Functional Requirements............................................................................................................................ 19   
18 3.2.2 Non-Functional Requirements ............................................................................................................... .... 20   
19 3.2.3 Security Requirements .... ........................................................................................................ ..... 20   
20 3.3 Reference Architecture . ................................................................................... ... 20   
21 22 3.3.1 3.3.2 Architectural Building Blocks..Basic OAM Architecture.......... .......... ............................................................................................ 23 .................................................................................. ... 20   
23 3.3.3 OAM Models and Deployment Options..................................................................................................... 23   
24 3.3.4 Managed Elements Deployed behind a NAT .. ......................................................................................... 28   
25 Chapter 4. Application Lifecycle Management (LCM) . ..................................................................... ....30   
26 4.1 Scope ........ .................................................... ..... 30   
27 4.1.1 Information Model .. ..................................................................................... ... 31   
28 4.1.2 Diagramming Legend. ................................................................................................................................ 33   
29 4.1.3 App Development Lifecycles ..................................................................................................................... 33   
30 4.1.4 App Onboarding Lifecycles ....... ........................................................................................................ 35   
31 4.1.5 App Operation Lifecycles .... ....................... .............. ... 37   
32 4.2 Common Application Lifecycle Conclusions .. ......................................................................................... ..... 37   
33 Appendix A: Cardinality . ...38   
34 Appendix B: Sequence Diagram Template ................ ...................................................... ....39   
35 Annex A: SMO and Non-RT RIC mapping with 3GPP management system .................................................................. 49   
36 37 Annex ZZZ : O-RAN Adopter License Agreement ...Section 1: DEFINITIONS .................................................. .............................................................................................. 51 ................................................... ...51   
38 Section 2: COPYRIGHT LICENSE . ........................................................................................................... . 51   
39 Section 3: FRAND LICENSE ......... ....................................................................................... ..... 51   
40 Section 4: TERM AND TERMINATION... ................................................................................... ... 52   
41 Section 5: CONFIDENTIALITY . .............................................................................................. 52   
42 Section 6: INDEMNIFICATION ... .......................................................................................... 52   
43 Section 7: LIMITATIONS ON LIABILITY; NO WARRANTY .............................................................................. ..... 53   
44 Section 8: ASSIGNMENT . .................................................... ... 53   
45 Section 9: THIRD-PARTY BENEFICIARY RIGHTS .. ..................................................................................... . 53   
46 Section 10: BINDING ON AFFILIATES ............ ............................................................................................ 53   
47 Section 11: GENERAL. .......................................................................................... . 53

# Chapter 1.Introductory Material

# 1.1 Scope

This Technical Specification has been produced by the O-RAN.org.

The contents of the present document are subject to continuing work within O-RAN WG1 and may change following formal o-RAN approval. Should the o-RAN.org modify the contents of the present document, it will be re-released by o-RAN Alliance with an identifying change of release date and an increase in version number as follows:

Release x.y.z where:

x the first digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc. (the initial approved document will have $\scriptstyle \mathbf { X } = 0 1$ ).   
y the second digit is incremented when editorial only changes have been incorporated in the document.   
z the third digit included only in working versions of the document indicating incremental changes during the editing process.

4 The present document studies O-RAN OAM architecture and interface functions. The OAM architecture supports a   
5 variety of management network deployment models, including the model of management entities (NMS/EMS/MANO)   
6 connecting directly to NEs, and the indirect connection (e.g., M-Plane involved) model. A separate OAM interface   
7 document provides details of the functions and protocols conveyed over the interface, that include management   
8 functions, procedures, operations and corresponding solutions.

# 1.2 References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

References are either specific (identified by date of publication, edition number, version number, etc.) or non-specific.

- For a specific reference, subsequent revisions do not apply.

For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document in Release 15.

[1] 3GPP TR 21.905: “Vocabulary for 3GPP Specifications”

[2] 3GPP TS 38.401: "NG-RAN; Architecture description".

[3] 3GPP TS 28.622: "Telecommunication management; Generic Network Resource Model (NRM) Integration Reference Point (IRP); Information Service (IS)".

[4] 3GPP TS 32.101: “Telecommunication management; Principles and high level requirements”.

[5] 3GPP TS 28.532: Management and orchestration; Generic management services [6] 3GPP TS 28.533: Management and orchestration; Architecture framework [7] 3GPP TS 28.550: Management and orchestration; Performance assurance [8] 3GPP TS 28.552: Management and orchestration; 5G performance measurements [9] ETSI GS NFV-IFA 005 V3.3.1 (2019-08), Network Functions Virtualisation (NFV) Release 3;Management and Orchestration;Or-Vi reference point - Interface and Information Model Specification

[10] ETSI GS NFV-IFA 027 V2.4.1 (2018-05), Network Functions Virtualisation (NFV) Release 2;Management and Orchestration; Performance Measurements Specification

[11] O-RAN White Paper: “O-RAN: Towards an Open and Smart RAN”, October 2018

[12] O-RAN-WG4.MP.0-v05.00: O-RAN Alliance Working Group 4 Management Plane Specification [13] O-RAN.WG1.O1-Interface-v04.00: “O-RAN Operations and Maintenance Interface Specification”. [14] ORAN.WG2.Use Case Requirements v01.00: “O-RAN Working Group 2 (Non-RT RIC & A1 interface)”. [15] O-RAN.WG6.CAD-v02.00, “Cloud Architecture and Deployment Scenarios for O-RAN Virtualized RAN”   
5 [16] O-RAN.WG6.ORC-v02.00, “Orchestration Use Cases for O-RAN Virtualized RAN”   
6 [17] O-RAN.WG1-O-RAN Architecture Description - v03.00: “O-RAN Architecture Description”. [18] ORAN.WG3.E2GAP.0-v0.1: “O-RAN Working Group 3; Near-Real-time RAN Intelligent Controller   
8 Architecture & E2 General Aspects and Principles”.   
9 [19] O-RAN.WG3.RICARCH-v01.00: “O-RAN Working Group 3;Near-Real-time RAN Intelligent Controller;   
0 Near-RT RIC Architecture” [20] 3GPP TR 28.809 v0.2.0, Study on enhancement of management data analytics [21] O-RAN-WG6.O2-GA&P-v01.00: “O2 General Aspects and Principles v.01.00”   
[22] https://yaml.org/spec/1.2/spec.html, "YAML Ain’t Markup Language (YAML™) Version 1.2", October 2009 [23] O-RAN.WG1.Information Model and Data Models-v01.00: “O-RAN Information Model and Data Models Specification”

# 1.3 Definitions and Abbreviations

# 1.3.1 Definitions

For the purposes of the present document, the terms and definitions given in 3GPP TR 21.905 [1] and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in 3GPP TR 21.905 [1].

Also, any terms and definitions that are also given in the O-RAN Architecture [17] are intended to be aligned. Text in the O-RAN Architecture [17] takes precedence in case of any difference.

infrastructure resources: Infrastructure resources as used here refer to a set of resources provided to a VNF [9] by its supporting O-Cloud.

Service Planning: The activity of a Service Operator around certifying a solution configuration for deployment into their network.

Service Provider: A network provider who is planning to deploy applications into their network.

Solution Provider: An application developer who delivers applications to Service Providers.

"SP" Exchange: Not a formal interface in terms of between systems. However, the structure and content of the exchange is defined such that a Solution Provider can deliver applications to a Service Provider for deployment.

Definitions for the following terms used in the document can be found in the O-RAN Architecture [17]:

near-RT RIC   
non-RT RIC   
NMS   
O-Cloud   
O-CU   
O-CU-CP   
O-CU-UP   
O-DU   
O-RU   
O1

O2 SMO rApp xApp

# 1.3.2 Abbreviations

6 For the purposes of the present document, the abbreviations given in 3GPP TR 21.905 [1] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in 3GPP TR 21.905 [1].

FCAPS Fault, Configuration, Accounting, Performance, Securit FOCOM Federated O-Cloud Orchestration and Management MA Managed Application   
ME Managed Element   
MF Managed Function   
MMP Meet-Me-Point   
NAT Network Address Translation   
Near-RT RIC O-RAN near real time RAN Intelligent Controller NFO Network Function Orchestration   
NFV Network Function Virtualization   
NFVI Network Function Virtualization Infrastructure   
NM Network Manager   
Non-RT RIC O-RAN non-real time RAN Intelligent Controller O-CU-CP O-RAN Central Unit – Control Plane.   
O-CU-UP O-RAN Central Unit – User Plane   
O-DU O-RAN Distributed Unit   
O-RU O-RAN Radio Unit   
PCP Port Control Protocol   
PK Primary Key   
PNF Physical Network Function   
RAN Radio Access Network   
SDLC Software Development LifeCycle   
SMO Service Management and Orchestration   
VNF Virtualized Network Function   
VPN Virtual Private Network   
UPNP Universal Plug-N-Play

# Chapter 2. O-RAN Overview

# 2.1 Scope and Objectives

O-RAN activities are guided by the following objectives [11]:

• Leading the industry towards open, interoperable interfaces, RAN virtualization, and big data and AI enabled RAN intelligence.

• Maximizing the use of common-off-the-shelf hardware and merchant silicon and minimizing proprietary hardware • Specifying APIs and interfaces, driving standards to adopt them as appropriate, and exploring open source where appropriate

The O-RAN OAM Architecture identifies management services, managed functions and managed elements supported in O-RAN, including the interworking between service management and orchestration and other O-RAN components such as infrastructure management. Requirements are derived from end-to-end OAM use cases, initially using the initial provisioning of O-RAN service across VNFs and PNFs as the primary use case. The architecture identifies the interfaces between O-RAN Service Management and Orchestration and Managed Elements for different models and example deployment options. It provides a description of the LifeCycle Management for applications delivered from a Solution Provider to a Service Provider/Network Operator.

Future versions of the architecture will address additional areas of O-RAN OAM functionality.

# 2.2 End to End OAM Use Cases

This section contains end to end OAM use cases that O-RAN is expected to support. Requirements will be derived from the use cases.

The initial use cases defined include O-RAN Service Provisioning and Data Collection. Additional Use Cases will be added as prioritized by the O-RAN community in future versions of this document

# 2.2.1 O-RAN Service Provisioning

# 2.2.1.1 Basic Objective

In the O-RAN architecture, the radio side includes Near-RT RIC, O-CU-CP, O-CU-UP, O-DU, and O-RU Managed Functions, and the management side is comprised of the Service Management and Orchestration Framework (including the Non-RT RIC). In the NFV environment, O-RAN network elements can also be implemented in a virtualized form, and thus include an Infrastructure layer (e.g. COTS/White Box/Peripheral hardware and virtualization layer) based on an O-Cloud.

The current use case focuses on network/element deployment rather than physical construction. According to the radio coverage requirement, operators could deploy the O-RAN network/element on dedicated physical resources and/or virtualized resources in a specific area.

This use case assumes that the network elements are deployed based on an example Network Design using VNFs for centralized functions and PNFs for functions closer to the customer, so that the sequence calls for deployment of VNFs for the Near-RT RIC, O-CU-CP and O-CU-UP first followed by PNFs for the O-DU and O-RU. Note: RF functions must always be realized as PNFs but the O-DU can be realized as a PNF or VNF; this document uses PNF as an example to illustrate the associated OAM flows.

It is also assumed that secure network connectivity is already available between RAN components.

# 2.2.1.2 Entities/Resources involved

To support the O-RAN network provisioning, the Service Management and Orchestration Framework needs to support the following capabilities:

O-RAN network element deployed in selected area   
a) For non-virtualized parts, the Service Management and Orchestration Framework supports the deployment of physical network elements on the target dedicated physical resources which satisfy the coverage requirements, with management through the O1 interface.   
b) For virtualized network elements, the Service Management and Orchestration Framework has the capability to interact with the O-Cloud to perform network element life cycle management, e.g. instantiate the virtualized network element on the target infrastructure through the O2 interface (e.g., indicate the selected geo-location for each VNF to be instantiated, where close to the PNFs).   
c) The Service Management and Orchestration Framework has the capability to consume the provisioning management service through the O1 interface to manage the configuration of the network element, details are defined in O-RAN.WG1.OAM Interface Specification [13].   
O-RAN network provisioning   
a) Based on the deployed network elements, the Service Management and Orchestration Framework configures the IP addressing, etc. in the PNFs and VNFs to support connectivity between them (this operation could also be performed during the instantiation steps).   
b) Operators can operate and maintain the network dynamically through the O1 and/or O2 interface by means of: i. Reconfiguration of the network elements ii. System update (usually refers to software management, without adding network elements) and system upgrade (the network elements could be added/removed/modified)

According to above, the Service Management and Orchestration Framework together with the O-Cloud implements the O-RAN network element deployment and provisioning, creating an O-RAN network to provide service to consumers.

# 2.2.1.3 Solutions

Table 2.2.1-1 shows the O-RAN service provisioning procedures.

Table 2.2.1-1: O-RAN service provisioning

<table><tr><td colspan="3" rowspan="1">O-RAN                                                                       O-RAN.WG1.OAM-Architecture-v04.00N</td></tr><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">O-RAN service provisioning</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">[1].Service Management and Orchestration Framework: NFO, OAM同Functions, Non-RT RICO-Cloud: DMSPNF</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">[1].The Service Management and Orchestration Framework and O-Cloud are connected and interact normally[2].O-Cloud supports platform and resource management normallyThe PNF was constructed/installed but not activatedThe VNF Software Package has been uploaded to the O-Cloud[5].Secure network connectivity is already available between RANcomponents- Note: security related procedure is FFS</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">The network operator/manager decides to deploy an O-RAN network inspecific geo-location</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">The service designer deploys Service Model and Artifacts to SMO</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step2 (M)</td><td colspan="1" rowspan="1">SMO on boarding the VNF Descriptors for the service to the O-Cloud</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">The radio planner orders RAN Service Deployment</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">The SMO initiates the O-RAN Service instantiation</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">The SMO interacts with O-Cloud to instantiate Near-RT RIC based onNear-RT RIC VNFD</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">The O-Cloud creates VNF of Near-RT RIC</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7 (M)</td><td colspan="1" rowspan="1">The O-Cloud notifies the SMO the Near-RT RIC has been instantiatedand SMO updates its inventory</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8 (M)</td><td colspan="1" rowspan="1">The SMO configures the Near-RT RIC</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9 (M)</td><td colspan="1" rowspan="1">the O-Cloud creates VNF of O-CU-CP</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10 (M)</td><td colspan="1" rowspan="1">The O-Cloud notifies the SMO the O-CU-CP has been instantiated andSMO updates its inventory</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 11 (M)</td><td colspan="1" rowspan="1">The SMO prepares configuration, e.g. Near-RT RIC related</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 12 (M)</td><td colspan="1" rowspan="1">The SMO configures the O-CU-CP</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 13 (M)</td><td colspan="1" rowspan="1">The SMO interacts with O-Cloud to instantiate O-CU-UP, for multiple O-CU-UP VNF, the step 13 to 17 is circulated</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 14 (M)</td><td colspan="1" rowspan="1"> the O-Cloud creates VNF of O-CU-UP</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 15 (M)</td><td colspan="1" rowspan="1">The O-Cloud notifies the SMO the O-CU-UP has been instantiated andSMO updates its inventory</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 16 (M)</td><td colspan="1" rowspan="1">The SMO prepares configuration, e.g. Near-RT RIC, O-CU-CP related</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 17 (M)</td><td colspan="1" rowspan="1">The SMO configures the O-CU-UP</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 18 (0)</td><td colspan="1" rowspan="1">The SMO deploys xApp to Near-RT RIC</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 19 (0)</td><td colspan="1" rowspan="1">After the above steps the Near-RT RIC could interact with O-CU-CP viaE2 interface</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 20 (0)</td><td colspan="1" rowspan="1">After the above steps the Near-RT RIC could interact with O-CU-UP viaE2 interface</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 21 (M)</td><td colspan="1" rowspan="1">SMO adds O-DU into inventory, e.g. with an O-DU.ID for each O-DU.For multiple O-DU this step is circulated</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 22 (M)</td><td colspan="1" rowspan="1">SMO add O-RU into inventory in the O-DU record, e.g. with an O-RU.IDfor each O-RU. For multiple O-DU this step is circulated</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 23 (M)</td><td colspan="1" rowspan="1">The field technician powers on the O-DU</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 24 (M)</td><td colspan="1" rowspan="1">The O-DU sends Registration to the SMONote: controller address determined as per O-RAN-WG1.O1 InterfaceSpecification</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 25 (M)</td><td colspan="1" rowspan="1">The SMO registers the O-DU as on-line</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 26 (M)</td><td colspan="1" rowspan="1">The SMO prepares O-DU configuration, e.g. related information fromNear-RT RIC and O-CU-CP, O-CU-UP</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Step 27 (M)</td><td colspan="1" rowspan="1">The SMO configures the O-DUNote: includes NETCONF configuration as per O-RAN WG4.MP.0-v01.00 [12]</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 28 (0)</td><td colspan="1" rowspan="1">The SMO could deploy xApp to O-DU</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 29 (0)</td><td colspan="1" rowspan="1">After the above steps the Near-RT RIC could interact with O-DU via E2interface</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 30 (M)</td><td colspan="1" rowspan="1">The field technician powers on the O-RU</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 31 (M)</td><td colspan="1" rowspan="1">The O-RU registers to the O-DUNote: detailed procedures as per O-RAN WG4.MP.0-v01.00 – additionalactions for hybrid case not shown</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 32 (M)</td><td colspan="1" rowspan="1">The O-DU sends Config Change Notification to the SMO indicating O-RU on-line</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 33 (M)</td><td colspan="1" rowspan="1">The SMO registers the O-RU as on-line</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 34 (M)</td><td colspan="1" rowspan="1">The SMO configures the O-RU via O-DU</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 35 (M)</td><td colspan="1" rowspan="1">The O-DU gets O-RU configuration information from the SMO</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 36 (M)</td><td colspan="1" rowspan="1">The O-DU configures the O-RU</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 37 (M)</td><td colspan="1" rowspan="1">O-RU sends Registration to the SMONote: procedure not currently supported in WG4.MP.0-v01.00 but detailsassumed as per O-RAN-WG1.O1 Interface Specification</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 38 (M)</td><td colspan="1" rowspan="1">The SMO registers the O-RU as on-line</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 39 (M)</td><td colspan="1" rowspan="1">The SMO prepares O-RU configuration, e.g. include co-related O-DU,etc.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 40 (M)</td><td colspan="1" rowspan="1">The SMO configures the O-RU</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">All O-RAN network functions needed for service have been registeredand configured; SMO holds current inventory of all O-RAN networkfunctions</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">Not applicable</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">The O-RAN network has been established and can provide service tocustomers</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Traceability</td><td colspan="1" rowspan="1">REQ-M&amp;O-FUN1, REQ-M&amp;O-FUN2, REQ-M&amp;O-FUN3, REQ-M&amp;O-FUN4, REQ-M&amp;O-FUN5, REQ-M&amp;O-FUN6, REQ-M&amp;O-FUN9, REQ-M&amp;O-FUN10</td><td colspan="1" rowspan="1"></td></tr></table>

![](images/06dea7225184dcd1de5a10e27838e49da8a787524f232caec4aab4f2443058c5.jpg)

> **Image Summary:** (Summary not available)


![](images/ccac94fcc13735d09359eeb60a37410cbe713603bcc0db68213eb1a939cd0848.jpg)

> **Image Summary:** (Summary not available)
  
Figure 2.2.1-1: O-RAN Service Provisioning

# 2.2.2 O-RAN Measurement Data Collection

# 2.2.2.1 Basic Objective

In this use case, the Non-RT RIC as the intelligent management center located in Service Management and Orchestration Framework determines that measurement data is needed and interacts with the SMO OAM Functions to collect measurement data from network for AI/ML training/inference/analyzing, and then generate optimization operations in order to improve the end-to-end user service experience and the network performance.

10 According to the Service Management and Orchestration Framework, to fulfill the Non-RT RIC requested data   
11 collection, the following capability should be supported by the SMO (framework):   
1 i The SMO should support the MnS component Type A (defined in [6])generation and the corresponding   
2 operation performing (defined in [5] and [7]), according to the measurement data collection request from the   
3 Non-RT RIC

ii The SMO (framework) should support the MnS component type C (defined in [6]) consumption such as the measurement data requested by the Non-RT RIC

The current use case focuses on the Non-RT RIC requested measurement data collection and consumption, the SMO should generate the PM Job and perform the PM Job control operations accordingly, and the SMO (framework) should support the measurement data consumption by the Non-RT RIC.

#

Notes:   
i In the O-RAN SMO framework, in order to avoid the PM Job confliction, it is suggested that the SMO take the responsibility for generating the PM Job and performing the PM Job control related operations. The resolution of conflict resolving by the SMO is FFS.   
ii In this use case, the network elements decide if the PM Job is acceptable or not, in other words, it is ultimately the network element (MnS producer) who decides whether the measurement data collection task can be established or not.   
iii Specifications for collecting infrastructure measurements do not yet exist. The Measurement Data Collection procedures will be updated to comply with [15] once WG6 has published the specification.   
iv The measurement data producer in the use case so far doesn’t refer to Network Slicing, but this will be added in the use case once the O-RAN network slice has been defined.

# 2.2.2.2 Entities/Resources involved

Roles in the PM Job Control related operations:

a). The Non-RT RIC: PM Job initiator b). The SMO (framework): measurement service component type A consumer

To fulfill the Non-RT RIC requested measurement data collection by the SMO on the O1/O2 interface, the information related to the collection task should comply with section2.3 defined in [13].

27 The measurement data collection information provided by the Non-RT RIC should be converted into a PM Job, and any   
28 management operations to the data collection task requested by the Non-RT RIC should be converted into the O1/O2   
29 interface supported PM Job control related management service operations by the SMO.

Roles in the NotifyFileReady subscribing:

a). SMO: management service component type A consumer (the referenceConsumer, defined in [5]) b). O-RAN MOs: Notification producer

Roles in the measurement data consumption:

a). SMO: management service component type C consumer b). O-RAN MOs: streaming data producer c). File Server: storage the measurement data file

# 2.2.2.3 Solutions

# 2.2.2.3.1 Measurement Data Collection Creation

Table 2.2.2-1 shows the procedure of the Non-RT RIC requested measurement data collection task fulfilled by the SMO on the O1/O2 interface.

<table><tr><td rowspan=1 colspan=1>Use Case Stage</td><td rowspan=1 colspan=1>Evolution / Specification</td><td rowspan=1 colspan=1>&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td rowspan=1 colspan=1>Goal</td><td rowspan=1 colspan=1>O-RAN Measurement Data Collection</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Actors and Roles</td><td rowspan=1 colspan=1>[1]. Service Management and Orchestration Framework[2].Non-RT RIC[3].O-Cloud[4].O-RAN components/logical nodes, e.g. O-CU, O-DU, O-RU,Near-RT RIC.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Assumptions</td><td rowspan=1 colspan=1>None</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Pre-conditions</td><td rowspan=1 colspan=1>[1].The SMO and the Non-RT RIC are connected and interactnormally[2].O-RAN &#x27;components are in normal running status[3].Secure network connectivity is already available between RANcomponents- Note: security related procedure is FFS</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Begins when</td><td rowspan=1 colspan=1>The Non-RT RIC determines that it needs measurement data from the O-RAN MOs and corresponding infrastructure resources, e.g., O-CU-CP instance and corresponding infrastructure resources</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 1 (M)</td><td rowspan=1 colspan=1>The Non-RT RIC provides the information of the measurement datato the SMO</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 2 (M)</td><td rowspan=1 colspan=1>The SMO generates a PM Job as the Non-RT RIC required</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 3.1 (M)</td><td rowspan=1 colspan=1>The SMO performs PM Job control management to the O-CU-CP viathe O1 interface, e.g. Operation createMeasurementJob defined in [7]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 3.2 (M)</td><td rowspan=1 colspan=1>The SMO performs PM Job control management to the O-Cloud overthe O2 interface for the O-CU-CP infrastructure resource instance,e.g. Create PM Job operation defined in clause 7.7.2, [9]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 4.1 (M)</td><td rowspan=1 colspan=1>The measured O-CU-CP responds to the SMO with the PM Jobcreation result. The PM Job iD should be contained.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 4.2 (M)</td><td rowspan=1 colspan=1>The O-Cloud responds to the SMO with the PM Job creation resultwith the PM Job ID.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 5.1 (M)</td><td rowspan=1 colspan=1>The SMO subscribes to PM Notifications to the O-CU-CP instance viathe O1 interface. The ConsumerReference defined in 7.1.1.3 [5]could be the SMO address</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 5.2 (M)</td><td rowspan=1 colspan=1>The SMO subscribes to O-CU-CP related infrastructure resourceinstance PM data to the O-Cloud over the O2 interface</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 6.1 (M)</td><td rowspan=1 colspan=1>The O-CU-CP instance provides the result of this operation to theSMO</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 6.2 (M)</td><td rowspan=1 colspan=1>The O-Cloud provides the SMO with the result of the subscription tothe O-CU-CP infrastructure resource instance</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 7 (M)</td><td rowspan=1 colspan=1>The SMO provides the result of the measurement data collectionestablishment to the Non-RT RIC</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Ends when</td><td rowspan=1 colspan=1>Non-RT RIC has measurement data</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Exceptions</td><td rowspan=1 colspan=1>FFS</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Post Conditions</td><td rowspan=1 colspan=1>The Non-RT RIC initiated measurement data collection has beenfulfiled by the SMO; the measured O-RAN MOs generate measureddata as the PM Job required. The subscription to the File Readynotification has been created successfully</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Traceability</td><td rowspan=1 colspan=1>REQ-M&amp;O-FUN7</td><td rowspan=1 colspan=1></td></tr></table>

![](images/49508ef22453436b8518d7b26096ece540432cc1a321b2c41266649ab2d17866.jpg)

> **Image Summary:** (Summary not available)
  
Figure 2.2.2-1: Measurement Data Collection Creation

# 2.2.2.3.2 Measurement Data File Consumption

5 With the performance data file reporting method:

The measurement data file could be stored in a file server, and the path should be contained in the   
NotifyFileReady   
Once the measurement data file has been prepared, the O-CU-CP instance shall report the notification   
NotifyFileReady to the SMO

1 Table 2.2.2-2 shows the measurement data file consumption

Table 2.2.2-2: Measurement Data File Ready Report   

<table><tr><td rowspan=1 colspan=1>Use Case Stage</td><td rowspan=1 colspan=1>Evolution / Specification</td><td rowspan=1 colspan=1>&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td rowspan=1 colspan=1>Goal</td><td rowspan=1 colspan=1>O-RAN Measurement Data Collection</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Actors and Roles</td><td rowspan=1 colspan=1>[1]. Service Management and Orchestration Framework[2]. Non-RT RIC[3]. O-Cloud[4].O-RAN components/ogical nodes, e.g. O-CU, O-DU, O-RU,Near-RT RIC.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Assumptions</td><td rowspan=1 colspan=1>None</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Pre-conditions</td><td rowspan=1 colspan=1>[1].The SMO and the Non-RT RIC are connected and interactnormally[2]O-RAN &#x27;components are in normal running status[3].Secure network connectivity is already available between RANcomponents- Note: security related procedure is FFS</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Begins when</td><td rowspan=1 colspan=1>The SMO shall perform the Operation Subscribe to provide theconsumer information to the measurement data producer. Theproducer shall report the NotifyFileReady once the measurementdata file has been prepared</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 1.1 (M)</td><td rowspan=1 colspan=1>The O-CU-CP sends the notification NotifyFileReady to the SMO, andit is consumed by the SMO</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 1.2 (M)</td><td rowspan=1 colspan=1>The O-Cloud reports the infrastructure resource measured data file tothe SMO</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 2 (M)</td><td rowspan=1 colspan=1>The SMO retrieves the data file from the FileServer, and the collecteddata is eventually consumed by the Non-RT RIC</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Ends when</td><td rowspan=1 colspan=1>SMO has collected data</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Exceptions</td><td rowspan=1 colspan=1>FFS</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Post Conditions</td><td rowspan=1 colspan=1>The SMO received the notification of NotifyFileReady successfully,the data file eventually consumed by the Non-RT RIC</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Traceability</td><td rowspan=1 colspan=1>REQ-M&amp;O-FUN7</td><td rowspan=1 colspan=1></td></tr></table>

![](images/8d3f7eb9efc8cac0187cb5eef42aeb7e9afbceb48b2c419b8746e15a838037f7.jpg)

> **Image Summary:** (Summary not available)
  
Figure 2.2.2-2: Measurement Data File Consumption

# 2.2.2.3.3 Measurement Streaming Data Consumption

With the streaming reporting method:

The consumer related information was taken to the producer in the operation of performance data collection creation. The performance data streaming service producer shall establish streaming connection(s) to the consumer, in this use case, the O-CU-CP instance act as the performance data streaming service producer and the SMO as the consumer. • The O-CU-CP instance shall send measured data on the established connection(s). The table 2.2.2-3 shows the streaming connection(s) establishment and streaming data consumption.

<table><tr><td rowspan=1 colspan=1>Use Case Stage</td><td rowspan=1 colspan=1>Evolution / Specification</td><td rowspan=1 colspan=1>&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td rowspan=1 colspan=1>Goal</td><td rowspan=1 colspan=1>O-RAN Measurement Data Collection</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Actors and Roles</td><td rowspan=1 colspan=1>[1]Service Management and Orchestration Framework[2]. Non-RT RIC[3]. O-Cloud[4].O-RAN components/logical nodes, e.g. O-CU, O-DU, O-RU,Near-RT RIC.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Assumptions</td><td rowspan=1 colspan=1>None</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Pre-conditions</td><td rowspan=1 colspan=1>[1].The SMO and the Non-RT RIC are connected and interactnormally[2].O-RAN&#x27;components are in normal running status[3].Secure network connectivity is already available between RANcomponents- Note: security related procedure is FS</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Begins when</td><td rowspan=1 colspan=1>The O-CU-CP instance starts streaming connection(s) establishmentto the SMO, and reports the measured data as the PM Job required</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 1 (M)</td><td rowspan=1 colspan=1>The O-CU-CP instance interworks with the SMO to establishstreaming connection(s). the connection(s) should not be releaseduntil the PM Job is stopped</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 2.1 (M)</td><td rowspan=1 colspan=1>The O-CU-CP instance reports the measured data to the SMO as thePM Job required via the streaming connection(s)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 2.2 (0)</td><td rowspan=1 colspan=1>The O-Cloud reports the infrastructure resource measured data to theSMO</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Ends when</td><td rowspan=1 colspan=1>SMO receives measured data</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Exceptions</td><td rowspan=1 colspan=1>FFS</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Post Conditions</td><td rowspan=1 colspan=1>The streaming connection(s) has been established between the O-CU-CP instance and the SMO successfully.The SMO consumed the measured data successfully</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Traceability</td><td rowspan=1 colspan=1>REQ-M&amp;O-FUN7</td><td rowspan=1 colspan=1></td></tr></table>

![](images/9000322d1b3f98f99a055336d6583db00e8992dba72af5b78938309a2b5a7143.jpg)

> **Image Summary:** (Summary not available)


Figure 2.2.2-3: Measurement Streaming Data Consumption

# Chapter 3.OAM Architecture

# 3.1 Architectural Principles

The following section provides architecture principals guiding the support of OAM in the O-RAN architecture. Common OAM functions should be supported through a common set of OAM interface protocols across the different components of the O-RAN architecture

Management Services should, to the degree possible, align with existing standards specifications:

 3GPP 5G Specifications for management interfaces   
 ETSI NFV Specifications for life cycle management   
 O-RAN WG4.MP.0-v01.00 (Future enhancements to align to 3GPP can be considered.)

O-RAN OAM specifications should refer to the 3GPP and ETSI specs and not replicate them here. O-RAN OAM specifications must identify needed extensions to support O-RAN and exceptions which cannot be supported. It is the goal of O-RAN to drive any needed extensions into standards to maintain alignment between O-RAN and existing standards.

# 3.2 Architecture Requirements

Defines the Architecture requirements applicable to the O-RAN reference architecture. Architecture requirements are derived from Use Cases to be supported and define the functional needs the architecture aims to satisfy.

The initial set of requirements in this document are derived from the O-RAN Service Provisioning Use Case. More requirements may be added in future versions of the OAM Architecture.

# 20 3.2.1 Functional Requirements

<table><tr><td colspan="1" rowspan="1">REQ</td><td colspan="1" rowspan="1">Description</td><td colspan="1" rowspan="1">Note</td></tr><tr><td colspan="1" rowspan="1">[REQ-M&amp;O-FUN1]</td><td colspan="1" rowspan="1">O-RAN OAM Architecture must support the interaction between the ServiceManagement and Orchestration Framework and the O-Cloud through O2interface to perform virtualized resource orchestration.</td><td colspan="1" rowspan="1">Use Case</td></tr><tr><td colspan="1" rowspan="1">[REQ-M&amp;O-FUN2]</td><td colspan="1" rowspan="1">O-RAN OAM Architecture must support the capability for the ServiceManagement and Orchestration Framework to consume the provisioningmanagement service exposed by each O-RAN managed element, whetherimplemented as PNF or VNF, through the O1 interface.</td><td colspan="1" rowspan="1">O-RAN-WG1.OAMInterfaceSpecification[13]</td></tr><tr><td colspan="1" rowspan="1">[REQ-M&amp;O-FUN3]</td><td colspan="1" rowspan="1">O-RAN OAM Architecture must support creation, modification andtermination of VNFs in an O-RAN network by the Service Management andOrchestration Framework</td><td colspan="1" rowspan="1">Use Case</td></tr><tr><td colspan="1" rowspan="1">[REQ-M&amp;O-FUN4]</td><td colspan="1" rowspan="1">O-RAN OAM Architecture must support registration and inventory of newlyactivated VNFs and PNFs by the Service Management and OrchestrationFramework</td><td colspan="1" rowspan="1">Use Case</td></tr><tr><td colspan="1" rowspan="1">[REQ-M&amp;O-FUN5]</td><td colspan="1" rowspan="1">O-RAN OAM Architecture must support collection of status change andother indications from VNFs and PNFs by the Service Management andOrchestration Framework</td><td colspan="1" rowspan="1">Use Case</td></tr><tr><td colspan="1" rowspan="1">[REQ-M&amp;O-FUN6]</td><td colspan="1" rowspan="1">O-RAN OAM Architecture must support configuration of VNFs and PNFsby the Service Management and Orchestration Framework, including, forexample, addressing information needed to allow them to connect to each</td><td colspan="1" rowspan="1">Use Case</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">other</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">[REQ-M&amp;O-FUN7]</td><td colspan="1" rowspan="1">O-RAN OAM Architecture must support management of PM jobs, PM datacollection/storage/query/statistical reports from O-RAN Components</td><td colspan="1" rowspan="1">Use Case</td></tr><tr><td colspan="1" rowspan="1">[REQ-M&amp;O-FUN8]</td><td colspan="1" rowspan="1">O-RAN OAM Architecture must support operation logging and operationauthority of Managed Elements</td><td colspan="1" rowspan="1">Use Case tobe added</td></tr><tr><td colspan="1" rowspan="1">[REQ-M&amp;O-FUN9]</td><td colspan="1" rowspan="1">O-RAN OAM Architecture must support management of ManagedFunctions contained within a Managed Element</td><td colspan="1" rowspan="1">ETSI 3GPPTS 28.622</td></tr><tr><td colspan="1" rowspan="1">[REQ-M&amp;O-FUN10]</td><td colspan="1" rowspan="1">O-RAN OAM Architecture must support hierarchical and hybridmanagement of O-RAN O-DU and O-RU components as defined in O-RAN-WG4.MP.0-v01.00</td><td colspan="1" rowspan="1">Use Case &amp;O-RAN MPSpec [12]</td></tr><tr><td colspan="1" rowspan="1">[REQ-M&amp;O-FUN11]</td><td colspan="1" rowspan="1">O-RAN OAM Architecture and interfaces must support network slicing,where an instance of O-RAN managed function may be associated with oneor more slices.</td><td colspan="1" rowspan="1">Use Case tobe added</td></tr><tr><td colspan="1" rowspan="1">[REQ-M&amp;O-FUN12]</td><td colspan="1" rowspan="1">O-RAN OAM Architecture must support O1 interface for all ManagedElements (with the exception of the RU) even if the Managed Element isdeployed behind a NAT</td><td colspan="1" rowspan="1">O-RAN-WG1.OAMInterfaceSpecification[13]</td></tr></table>

# 1 3.2.2 Non-Functional Requirements

<table><tr><td rowspan=1 colspan=1>[REQ-M&amp;O-NFUN1]</td><td rowspan=1 colspan=1>O-RAN OAM Architecture must support the introduction of new and morecost-effective technologies into the RAN through open, standard interfaces</td><td rowspan=1 colspan=1>O-RANwhite paper[11]</td></tr><tr><td rowspan=1 colspan=1>[REQ-M&amp;O-NFUN2]</td><td rowspan=1 colspan=1>O-RAN OAM Architecture must support virtualization of RAN components,allowing operators use of common, off-the-shelf hardware implementations</td><td rowspan=1 colspan=1>O-RANwhite paper[11]</td></tr><tr><td rowspan=1 colspan=1>[REQ-M&amp;O-NFUN3]</td><td rowspan=1 colspan=1>O-RAN OAM Architecture must support use of Analytics and ArtificialIntelligence/Machine Learning to improve network efficiency andperformance and reduce operations costs</td><td rowspan=1 colspan=1>O-RANwhite paper[11]</td></tr></table>

# 3 3.2.3 Security Requirements

<table><tr><td>[REQ-M&amp;O-NFUN4]</td><td>O-RAN OAM Architecture must support security of interactions between the components of an O-RAN network</td><td>See note</td></tr></table>

Note: more detailed requirements for security will be addressed in future versions of the OAM Architecture.

# 3.3 Reference Architecture

The reference architecture defines a set of basic architectural building blocks – management services, managed functions and managed elements – for the O-RAN management domain.

# 3.3.1 Architectural Building Blocks

# 3.3.1.1 Management Services

O-RAN Management Services offer capabilities to manage and orchestrate managed elements. Managed elements expose their management services to managers. Managers consume the management services.

1 Examples of Management Services supported by O-RAN include:

 Provisioning   
 Fault Supervision   
 Performance Assurance   
 Trace Management   
 File Management   
 Software Management   
 Communication Surveillance   
 Startup and Registration of a Physical Network Function (PNF)   
 Instantiation and Termination of a Virtualized Network Function (VNF)   
 Scaling Management Services for VNF

'The definition of supported management services and their APIs will be covered in the OAM O1 Interface specification [13].

# 3.3.1.2 Managed Elements

The definition of a Managed Element (ME) is given in 3GPP TS 28.622 [3] section 4.3.3. The ME is an IOC that supports communication over management interface(s) to the manager for purposes of control and monitoring.

17 Examples of O-RAN Managed Elements include:

 O-RAN Managed Functions deployed individually as MEs (e.g., Near-RT RIC ME, CU-CP ME, CU-UP ME, O-DU ME, O-RU ME).   
 Central Unit (CU) composed of CU-CP and CU-UP   
ME composed of Near-RT RIC, CU-CP, CU-UP, DU and RU

A variety of deployment examples and their OAM interfaces are given in a later section. Choice of deployment options will be based on operator requirements.

A key motivation for the Managed Element concept is that an ME is a tightly integrated and tested group of MFs that are deployed together. This has implications on how software updates are managed, because all software updates need to retain the property that all MFs in the ME have been tested together. Depending on the deployment scenario and other considerations, the MFs may be grouped in different ways. An interface is required to each ME, which can manage the communications to each MF that is contained within it. Following sections present many examples of how the O1 interface can connect to either an ME that contains an individual MF, or to an integrated ME that contains multiple MFs.

# 3.3.1.3 Managed Functions

The definition of a Managed Function (MF) is given in 3GPP TS 28.622 [3] section 4.3.4. An MF instance is managed using the management interface(s) exposed by its containing ME instance.

4 O-RAN managed functions include:

 Near-Real-Time Radio Intelligent Controller (Near-RT RIC)  O-RAN Central Unit – Control Plane (O-CU-CP)  O-RAN Central Unit – User Plane (O-CU-UP)  O-RAN Distributed Unit (O-DU)

# 3.3.1.4 Managed Applications

ManagedApplication: This Information Object Class (IOC) represents a software application that may be independently tested and separately deployed from its containing ManagedFunction instance. The containing ManagedFunction instance mediates the management service for the Managed Application. A ManagedFunction instance may have zero or more Managed Application instances.

The xApp is defined in [19]. Management of the xApp shall comply with the following principles:

The O1 interface terminates on the Near-RT RIC platform ME, the Near-RT RIC platform delegates the management of xApps   
xApp could be provided by the third party, it is decoupled from the O-RAN nodes, O-RAN node supports one or more xApp running on it   
In order to model a variety of different types of xApps, it is necessary to extend common features of a parent Class, and the specific xApp IOC could inherit from its parent Class.

According to above principles, the modeling to the xApp could be described as the following:

• xApp IOC represents the management aspects of the xApp xApp IOC inherits from ManagedApplication and could extend specific attributes.

The details of the MA will be defined in the O-RAN Information Model document [23].

# 3.3.1.5 Service Management and Orchestration Framework

Service Management and Orchestration Framework is responsible for the management and orchestration of the managed elements under its span of control. The framework can for example be a third-party Network Management System (NMS) or orchestration platform.

Service Management and Orchestration Framework must provide an integration fabric and data services for the managed functions. The integration fabric enables interoperation and communication between managed functions within the O-RAN domain. Data services provide efficient data collection, storage and movement capabilities for the managed functions. In order to implement multiple OAM architecture options together with RAN service modeling, the modeling of different OAM deployment options and OAM services (integration fabric etc.) must be supported by SMO

# 3.3.1.6 Non-Real Time Radio Intelligent Controller

The non-RT RIC is a part of the Service Management & Orchestration Framework and communicates to the near-RT RIC using the A1 interface. [11]

31 Non-RT control functionality $( > 1 \mathrm { s } )$ and near-Real Time (near-RT) control functions $( < 1 \mathrm { s } )$ are decoupled in the RIC.   
32 Non-RT functions include service and policy management, RAN analytics and model-training for some of the near-RT   
33 RIC functionality, and non-RT RIC optimization.

# 3.3.1.7 Control Loop Support

O-RAN defines 3 control loops with different latency bands [11]. It is not expected that these loops are hierarchical but instead run in parallel. This does not mean that an ME with an inner loop will not generate its own event as result of an inner loop failure, but it will not simply propagate the lower level event received by the inner loop. The three loops are roughly defined as:

Loop 1: In the DU for per TTI/msec resource scheduling $_ { < 1 0 }$ millisecond)   
Loop 2: In the Near-RT RIC and CU for resource optimization (10 milliseconds to 1 second)   
Loop 3: In the Service Management and Orchestration Framework for ML Training, Trending, Orchestration $>$   
1 second)

# 3.3.2 Basic OAM Architecture

![](images/8de60845925bbdf9f2be145536c1f9a5b563a1470a5559cc7472d194e0b0d586.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.3.2-1 O-RAN OAM Logical Architecture

Figure 3.3.2-1 shows the overall O-RAN OAM Logical Architecture. In the original white paper [11], the interface between the Manager and the O-RAN components for control purposes was identified as A1. The O-RAN OAM Architecture adds another interface for OAM functions, labeled O1 (OAM). O1 is the interface between the O-RAN Managed Element and the management entity. Note: the figure uses 5G terminology, however the same principles will apply for LTE/4G. Mapping to LTE/4G may be added in future. O-RAN OAM also adds the O2 interface for management of the O-Cloud, which has different requirements from the O1 interface and as defined in [21].

11 The O1 OAM Interface includes implementation of Fault, Configuration, Accounting, Performance, Security (FCAPS)   
12 functions, File management and Software management functions to ME (s) virtualized and physical alike. For details of   
13 the management services supported by O1, see [13].   
14 The O2 OAM Interface enables the management of O-Cloud infrastructures and the deployment life cycle management   
15 of O-RAN cloudified NFs that run on an O-Cloud. For details of the functions supported by O2, see [21].   
16 As shown in the figure, there is a logical OAM interface to individual O-RAN Managed Functions, however in practice   
17 the grouping of Managed Functions into Managed Elements will determine where actual O1 interfaces are terminated.   
18 More detail is explained in subsequent sections. The O1 interface could be the terminated directly on the Service   
19 Management & Orchestration Framework or in a hierarchical model could be terminated on a Managed Element which   
20 manages other O-RAN Managed Functions.   
1 The sections below identify possible management topologies, for example, the basic “flat” model of OAM relationships   
22 as well as the hierarchical model of O-DU to O-RU relationship and the hybrid model of O-DU to O-RU relationship   
23 defined in the O-RAN Front Haul M-Plane specification, as well as example deployment options.

# 3.3.3 OAM Models and Deployment Options

5 This section provides examples of possible models and deployments of Managed Functions into Managed Elements.   
6 Adoption of a single model is not required in the O-RAN OAM Architecture, rather multiple model deployments may   
7 be supported in a network.

# 1 3.3.3.1 Flat Management Architecture Model

![](images/1ec98dec7f752b7e6e6af46f057722441984fb1c775bf81510bc15a39c9478ae.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.3.3-1: Flat Model

4 In the Flat management model, all the MFs comprising the O-RAN architecture are also MEs and expose an O1   
5 interface to the SMO. Note: The Open Fronthaul M-Plane does not support a flat management model for the O-RU.

NM/orchestration platforms provide a distributed deployment model of NM functions which allows for greater scaling and lower latency functions that traditional centralized monolithic NM implementations. In this specification, no specific platform is required, however the NM is assumed to have orchestration capabilities. Therefore, deployment of SMOs, analytics, configuration and control functions can be potentially collocated with some of the NEs. This allows for localized processing and localized scaling to handle the expected large number of NEs to be managed. The NM functions can be distributed across the network edge and therefore handle a logically flat architecture.

# 3.3.3.2 Hierarchical Management Architecture Model

Where the distributed NM architecture is not available it may be desirable to deploy a hierarchical management architecture where a higher level ME is used to manage a subnetwork of MEs as shown in Figure 3.3.3-2, where the ODU manages the O-RU using the Open Front Haul M-Plane interface.

![](images/a6dee910052653b8a40ba4223e57580a4ed8ed4d139faee426b90c687600c6a0.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.3.3-2: Hierarchical Model Example

18 In the example of the figure 3-3, the O-RU is managed by the Open Fronthaul M-Plane interface to the O-DU rather   
19 than the Service Management & Orchestration Framework, so there is a hierarchical relationship between Service   
1 Management & Orchestration and the O-DU. The O-DU must provide a consistent and standardized view of the   
2 subtending O-RUs as specified above.

# 3.3.3.3 Hybrid Management Architecture Model

In the Hybrid management architecture, the O-RU is managed partially by the O-DU and partially by the SMO.

5 The management by O-DU is via the Open Fronthaul M-Plane, and the SMO manages the O-RU through a direct   
6 interface. Note: The O-RU currently supports hybrid mode using an Open Fronthaul M-Plane logical direct interface   
7 defined in the Open Fronthaul M-Plane specification [12] between the O-RU and SMO. This direct interface may be   
8 augmented with an O1 Interface at some time in the future, as in [17].   
14 Management responsibility is divided in this case between the O-DU and the Service Management & Orchestration   
15 Framework. Open Fronthaul M-Plane interface in the figure is defined in [12]. The O-RU supports connection to   
16 multiple clients as well as access control that can be used to control the privileges available to a particular client in   
17 Open Fronthaul M-Plane [12]. The alignment between the Open Fronthaul M-Plane and O1 interfaces is for further   
18 study.

![](images/d64dbff8c676b6a75fbc4ded20a2d93d8fd2a21d1912d378963d610402fd9d1d.jpg)

> **Image Summary:** (Summary not available)
  
Figure 2.3.3-3: Hybrid Model

# 3.3.3.4 Example Managed Deployment Options

In aggregated equipment, the Managed Element contains multiple internal Managed Functions. This section provides a number of examples showing how the OAM architecture is applied to different groupings of Managed Functions into Managed Elements. Use cases associated with different deployment options are defined in [15].

Figure 3.3.3-4 shows a single Managed Element that contains CU-CP, CU-UP, O-DU and O-RU Managed Functions.

![](images/1274c750e91dca8c78ac2e61a25c16a32f3795d40c0d22b0509cb156708b5555.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.3.3-4: Example with Single Integrated ME

As shown in the figure 3.3.3-4, there is a single O1 interface to the Managed Element. However, the O1 interface still provides a consistent and standardized view of the Managed Functions that are contained within the Managed Element.

Figure 3.3.3-5 shows another example where the Near-RT RIC has been split off as a standalone ME.

![](images/e4aeb301365775af6d6ef1411e01060ba5c66f5e00ba2df5cd2c634b6e4febe6.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.3.3-5: Example with Single Integrated $\mathbf { M E } +$ Standalone Near-RT RIC

8 In the example of Figure 3.3.3-5, there are separate O1 interfaces supported by each ME. The ME containing the Near  
9 RT RIC Managed Function supports management of only this function through its O1 interface, while the ME   
10 containing the other Managed Functions provides a view of all contained functions.

![](images/c5b315728188e730bd865f20865243e16b1b371225bba5ce3d148c66c9695fe5.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.3.3-6: Example ME aggregating Near-RT RIC, O-CU-CP and O-CU-UP

Figure 3.3.3-6 shows an alternative example with two Managed Elements containing the Near-RT RIC/O-CU-CP/OCU-UP, and the O-DU and O-RU Managed Functions, respectively. Again, the O1 interfaces from the MEs provide a consistent and standardized view of the contained Managed Functions.

![](images/acd3a51791bef45cdde533f9fdc179d0dfde4102522088e283084aeaa0fa4b61.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.3.3-7: Example with Three MEs

Figure 3.3.3-7 shows an alternative example with three Managed Elements containing the Near-RT RIC/CU-CP, the CU-UP, and the O-DU and O-RU Managed Functions, respectively. Again, the O1 interfaces from the MEs provide a consistent and standardized view of the contained Managed Functions.

Finally, Figure 3.3.3-8 shows a similar grouping of Managed Functions, but with the Near-RT RIC separated as its own Managed Element. The same architectural concepts apply.

![](images/4b6d8a8cba4aabeb8b984b6e2409210b324d149790cf23d88b6241c4ce1b5a5b.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.3.3-8: Example with Three MEs including Standalone Near-RT RIC

# 3.3.4 Managed Elements Deployed behind a NAT

Service Providers prefer to not deploy Managed Elements (ME) behind a NAT, but there are cases where this cannot be avoided, for example:

 exhaustion of public IPv4 addresses managed elements deployed in large complexes not owned by the Service Provider (Apartments, Sports Venues etc.) managed elements connected via third-party networks using a NAT

When a Service Provider deploys managed elements behind a NAT it is critical that they are able to retain full management control of these elements.

![](images/9f38dd09e87a60c352d8ad9a20d90c6b4536b368075070bdcb039d48247c7910.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.3.4.1 O-RAN MEs behind a NAT

Four methods of providing the O-RAN Manager with the ability to address a ME behind a NAT and identify data received from a ME behind a NAT are recommended in priority order:

1. ME uses IPv6 as Backhaul transport where possible eliminating the need for a NAT - exhaustion of public IPv4 addresses   
2. ME establishes persistent VPN tunnel (e.g. IPSec) toward a VPN concentrator (gateway) located outside of network with the NAT. The ME is then accessible through the established tunnel.   
3. ME uses a standard protocol (UPNP or PCP) to establish a port-forwarding rule at the firewall and automatically assign itself a port.

4. Service Provider manually configures the firewall to assign a port to each ME that resides within the protected network.

# Chapter 4.Application Lifecycle Management (LCM)

This chapter describes Lifecycle Management of applications that are developed by a Solution Provider and delivered to a Service Provider or Network Operator for deployment in O-RAN. The chapter’s current focus is on LCM of rApps and xApps, as defined in [17].

6 Lifecycle Management follows the basic models of a Software Development   
7 Lifecycle by defining the transitional information from one state to another. There   
8 are several Software Development Life Cycle (SDLC) definitions. For the purposes   
9 of discussion this document generally follows a 7-state model as shown in Figure 4-   
10 3. Some states might also include activities that align with other states. However,   
11 this level of detail is not depicted here in order to introduce those details later in the   
12 document.   
13 A Service Provider or Network Operator has needs which are fulfilled by a Solution   
14 Provider. Once the Solution Provider delivers the application it is validated in a test   
15 environment prior to giving to operations to deploy. Usage of the deployed application may result in changes to   
16 configuration by the Service Provider or may be feedback to Solution Providers to evolve the capabilities of the   
17 network and/or its management.

![](images/4370316838dfee4a36b0840e23f4ebc375a180f8f852a7c16fabbec1d303ae03.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4-3: Generalized Lifecycle

Although applications may come in many forms the delivery from the Solution Provider to the Service Provider needs to be done in a standardized manner. The seven steps defined in the SDLC are high level. Each may break down into a set of finer grain steps.

# 4.1 Scope

The end-to-end lifecycle involves two entities, the Solution Provider and the Service Provider. The Solution Provider provides applications for the Service Provider to use in their network. The working flow could be summarized as three phases: Development, Onboarding and Operations, as shown in Figure 4.1-4.

![](images/420f74450147acc63c04eaacf924321e199ba39308340c1357f07ad2b89002db.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4.1-4 Application Lifecycle Phases

These applications need to be onboarded in a common manner, regardless of how they are deployed. This document focuses on the data that must be included in the App Package as it is exchanged between the Solution Provider and the Service Provider. This exchange is referred to as the "SP" exchange. This is not a formal interface between systems and therefore is not denoted as other O-RAN interfaces are. Care is given as not to put implementation or tooling mandates on either the Solution Provider in their development of the application, or the Service Provider in the aspect of training or deploying the application. Aspects of the lifecycle across both parties are introduced. However, not all aspects are discussed. Instead the focus is on those activities that affect the data contained in the SP Exchange. Later in this document the term "Service Planning" is used to represent activities internal to the Service Provider. This is not the

same as the "SP Exchange" used to describe the data passed from the Solution Provider to the Service Provider. The method of the SP Exchange is not defined in this document. It is sometimes referred to as the "Marketplace". The marketplace can be implemented by either the solution provider, the service provider, and an external entity to both. The Marketplace simply represents an exchange between entities which could be done by electronic means or physical media.

The App Development will provide application solutions w/wo AI/ML models, while “App Onboard” and “App Operate” will be responsible for application onboarding and operations. Considering the data privacy and security requirements, the application development could be completed in the environment provided by the Service Provider.

Applications utilize AI/ML models or not. Therefore, although the Model Information may be optional in the package, we will focus on the data exchange requirements for applications with AI/ML models as the superset.

# 4.1.1 Information Model

12 An Entity Relationship Diagram (ERD) is a way to pictorially show relationships and cardinality between "Entities".   
13 Entities can be anything, physical, logical, or conceptual. They usually have some attributes to differentiate one instance   
14 from another. The entities relationship is identified with a connector which uses symbols at both ends to show the   
15 cardinality between the entities. The symbol represents the cardinality of the far end to the entity near the symbol. These   
16 basic concepts are shown in Figure 4.1-5 Entity Relationship Diagram Basic ComponentsFigure 4.1-5. Some other   
17 notations are fields marked as a Primary Key (PK), a Foreign Key (FK), or an Alternate Key (AK). Numbers may be   
18 appended to show when multiple fields are combined to create a unique key value.   
21 The following ERD diagram illustrates the composition of the Application Package. An Application Package is the   
22 basic unit exchanged between the Solution Provider and Service Provider. The attributes of the entities in the diagram   
23 are representative. The actual contents are FFS and will be refined in a later release of this document.

![](images/269b946566c8a857810132b74abbe410d352dd77592eeafc625f5c67d2cd3f5c.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4.1-5 Entity Relationship Diagram Basic Components

![](images/9ee22d61e6217eda8f324c90a3a3ff4d10442823bcae4b1662601f7c70e73882.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4.1-6 Application Package Entity Relationship Diagram

The following modifiers can be pre-pended to Information Model Elements to indicate context:

"Solution" The version of the element as defined by the Solution Provider   
"Onboarded" The initial version of the catalogued elements created during onboarding.   
"Catalogue" Subsequent versions of the catalogued package or its elements which may have been adjusted by the Service Provider.

10 The "Application Package" contains a Metadata repository with metadata files in YAML [21] format. It also contains   
11 a security metadata file in YAML format which describes the procedures used for ensuring the integrity of the software   
12 contained in the package.   
13 The Application Package also contains repositories for Deployment Configurations, Application Types, and   
14 Deployable Components. An optional repository for ML Models is supplied for Application Packages with one or   
15 more application types employing ML technology.   
16 ML Models may be pre-trained by the Solution Provider and therefore provide initial Training History. The Service   
17 Provider may also train the model or retrain the model with a more specialized data set, this is called specialization.   
18 The Training History provides the mechanism to record all training and subsequent specializations applied to that   
19 training through the Training History.   
0 An example of specialization is a ML Model created to predict the flow of traffic volumes. This algorithm can be   
1 generally trained to follow road patterns for devices with a velocity greater than 20 miles per hour. This training could   
2 be done by the Solution Provider on a generalized or open data set and recording in the Solution Training History.   
23 After onboarding the Service Provider may provide specialized training for dense urban traffic patterns which don't   
4 always follow the roads due to periodic traffic congestion This would be an additional Training History record added   
5 by the Service Provider and referenced as specialization in the Catalogue Training History. Further refinement could   
6 also be applied for specific cities such as New York, Los Angeles, or San Francisco which would now add 3   
27 specializations Catalogue Training History records relating to the dense urban Catalogue Training History which is   
8 a specialization if the Onboarded Training History.   
1 Once a Catalogue Deployment Configuration is validated as safe for use in operations it is published to a runtime   
2 environment as a Published Deployment Configuration. Runtime instance data can be applied to the Published   
3 Deployment Configuration. Application Types deployed as part of this activity are call an App Instance. An APP   
4 Instance running in the Non-RT RIC Runtime can be referred to as an rAPP instance. An App Instance running in the   
5 near-RT RIC Runtime can be referred to as an xApp instance. An App Instance running in a training environment is   
6 referred to as a Training App instance.

# 4.1.2 Diagramming Legend

The legend depicted in Figure 4.1-7 is used across all lifecycle diagrams in this section and is shown once so it is not required on every diagram. Bolded text on a diagram is an item identified as requiring further discussion later in the document. Text in Italics are items identified for completeness but not requiring further discussion. Meet-Me-Points (MMPs) are places where a major aspect of the lifecycle interchanges. Data may be exchanged through these MMPs but the exact mechanism of the exchange is outside the scope of this document. Destination or Decision points are color coded according to their user community. Destination or Decision points are not a contributing factor to the data demands of the "SP" Exchange and are therefore not named. Instead the actions or conditions that are used as a transition between points are named as the items of interest.

![](images/2e3c519b4db20b9b45f78ae397e29aa6a52d40cc762b5fba4720771eb7ac5759.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4.1-7: Life Cycle Diagram Legend

# 4.1.3 App Development Lifecycles

In the App Development Lifecycle only two types are defined, the Solution App Package and the Solution App Type.

# 4.1.3.1 Solution App Type Lifecycle

The Development Lifecycle steps related the Solution App Type are shown below in Figure 4.1-8 错误！未找到引用 源。.

![](images/81933fec4f6766222fcad4724bbb78fd857c7bbbda74d74c887ce683417833d6.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4.1-8: Solution App Type App Development Lifecycle

Customer feedback can consist of use case requirements, feature requests, defect notifications, or a variety of other comments. These feed the development cycle to develop new application or enhance existing ones. Requirements are usually identified and sent to developers to implement. The outcome of the build process is the container images built using SDKs for their intended deployments. If the application is AI/ML enabled, then the training action is done. The training might happen with synthetic data or with data provided by Service Providers. Information on the training performed will be included in the Solution Training History. The completed Solution App Type is stored in a development repository.

# 4.1.3.2 Solution App Package Lifecycle

The Development Lifecycle steps related the Solution App Package are shown below in Figure 4.1-9.

![](images/6071b4084973359e634656aa9b2d17c4158105b07ab2d6000812492e0b48b033.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4.1-9: Solution App Package App Development Lifecycle

14 The Solution App Package is used to convey the Solution App Type through the onboarding process to the Service   
15 Provider. It begins by pulling the Application App Type out of its repository and placing it in the package as mandated   
16 by the exchange requirements. Next security is applied such that the Service Provider can ensure that an Onboarded   
17 Application Package did in fact come from the expected Solution Provider. The secure package, Solution App Package,   
18 is then delivered to the Service Provider for onboarding.

# 4.1.4 App Onboarding Lifecycles

The App Onboarding phase deals with establishing configuration, policies, measurements, and required analytics. The App Onboarding Phase is involved with both App Packages and App Types, each with its own steps and associated actions. These will be treated separately.

# 4.1.4.1 Onboarded App Package Lifecycles

The Service Design steps associated with an Onboarded App Package are shown below:

![](images/bae140145a354d7d4c9cf82bd2c71473f272f83f7be49a4100cae9f6dd5ced96.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4.1-10: Onboarded App Package Service Provider Configuration Lifecycle

An App Package is onboarded from the exchange, and its content verified. If valid, its contents (App Types) are unpacked and the Onboarded App Package and associated Onboarded App Types catalogued. If invalid, the Service Provider can provide App Package-level feedback to the Solution Provider via the Marketplace.

# 4.1.4.2 Onboarded App Type Lifecycles

The App Onboarding Phase for Onboarded App Types is split between normal processing for all applications, named "Configuration", and the lifecycle for "Training" App Types with included AI/ML Models. Workflow can interchange between these cycles iteratively. We will treat each of these separately below.

# 4.1.4.2.1 Onboarded App Type Configuration Lifecycle

The Service Operator Configuration steps associated with an Onboarded App Type are shown below:

![](images/9222e3499c881ba934789f0d802ea35f31c940bdd032e1f0e45d5461c5d51cc1.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4.1-11 Onboarded App Type Service Provider Configuration Lifecycle

Onboarded App Types are made visible in the SMO environment when published into the catalogue. Each recommended configuration of the App Type is certified prior to publication to a runtime library. If Certification fails, then Service Planning will determine the next course of action.

Service Planning aggregates “fix” requests from Configuration which can be passed back to the Solution Provider (at the App Package level) as feedback across the SP interface of the Marketplace Exchange. This exchange also aggregates “change” requests from Configuration or Operations and determines if the request is for additional development (a “feature” request) or additional training (a “training” request). The former would be aggregated and

passed back to the Solution Provider via the SP interface as described above for “fix” requests. For the latter, the 2 Service Design: Training lifecycle would ensue.

3 If the Onboarded App Type requires AI/ML training, then a request through Service Planning is used to train the model.   
4 When the "Specialized App Type" is returned, like non-ML Onboarded App Types it is catalogued and scheduled for   
5 certification. Once certified the App Type is distributed as a Published App Type to a Run Time Library. From there   
6 operations can deploy as either a management (rApp) or network application instance (xApp).

# 4.1.4.2.2 App Type Training Lifecycle

8 The Service Operator Training Lifecycle associated with a Training App Type is shown below:

![](images/ce6d75689671e2aa8debace50ad5eae8654f582be7560481608832bc60a150b3.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4.1-12: Training App Type Service Provider Training Lifecycle

11 When a training request is received then resources within the training environment are scheduled for the application.   
12 Data is collected and groomed for training after which a training iteration is executed. At the end of the training cycle a   
13 test set is applied to the model and accuracy is calculated. If the test fails or other metadata indicates more training   
14 iterations are required, then the cycle repeats. Once the model is adequately trained it is promoted and sent back to   
15 service planning for continuation in another lifecycle.   
16 Inside the "Training Lifecycle" the process MAY require multiple iterations of training before being returned to the   
17 Service Planning MMP.

18 The iteration count SHALL be included in the specialization metadata info.

# 4.1.5 App Operation Lifecycles

There can be many runtime environments in the service providers’ network. Some can be production while others might be for non-production execution, such as offline training and lab certification. For this document we will focus on the runtime aspects of rApps, which execute within the Non-RT RIC as part of the SMO, and the xApps which execute in the near-RT RIC as part of the RAN. Although they have the same lifecycle steps the data demands due to their operational environment are different and therefore need to be independently addressed.

# 7 4.1.5.1 App Instance Lifecycles

![](images/2af10c53ccfc78fa4d501c9ad56307665adff67719558a17d17700f652f6bdac.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4.1-13: Service Provider Runtime Lifecycles

10 After the App Instance is created through a deploy operation it is monitored. As monitoring reports the health and   
11 workload of the application it is scaled up and down based on demand. Based on monitoring result, a series of operation   
12 and management functions are triggered, such as alert management, event management, incident management and   
13 further analysis. The analysis results can be guidance for further actions such as termination, healing and scaling.   
14 Finally, when its job is completed the instance is terminated. While in operation the service provider may discover   
15 defects, performance issues, or identify new features that would be beneficial. Such issue or change request will   
16 be communicated to the Service planning where the Application could be retrained or updated. The information can   
17 also be sent via the Service Planning to the Solution Provider as feedback.   
18 Operations determine when an application is deployed, or undeployed. Since applications are atomic, the update process   
19 is an orchestrated process of deploy and terminate. It is possible for two versions to be active at the same time, but care   
20 must be given not to provide overlapping scopes to the application instances, otherwise they may give differing   
21 directives to the network in a random order. This could cause a destabilization of the network.

# 4.2 Common Application Lifecycle Conclusions

The initial conclusion of Common Application Lifecycle procedures is that there is a formalized exchange between the Solution Provider and the Service Provider, the "SP Exchange". The SP Exchange consists of data describing the package and its security. The package also contains information regarding Deployment Configurations, Application Types, Deployable Components, and potentially ML Models. Further details regarding the composition of these areas will be defined through analysis of the Actions identified in section 4.1 as an action requiring further analysis (Bolded).

# Appendix A: Cardinality

This informative Appendix provides background information regarding the cardinality of different O-RAN architecture elements. It is not intended as a requirement on cardinality.

4 The RAN network has an expected hierarchical fan out. Therefore, the O-RAN sizing would be:

Non-RT RIC (1..j) Near-RT RIC (1..k) CU-CP (1..m) CU-UP (1..n) O-DU (1..p) O-RU (1..q)

11 Where: $\scriptstyle 1 < = \mathbf { j }$ ; $\mathrm { { \dot { J } } } < = \mathsf { k }$ ; $k < = \mathsf { m }$ ; $m < = \mathsf { n }$ ; $\mathsf { m } < = \mathsf { p }$ ; $\mathsf { p } < = \mathsf { q }$

2 Due to resiliency and scaling aspects of cloud implementations an O-DU will logically be connected to one CU-CP. The   
3 CU-CP may in fact be a pool of CU-CP instances to handle loads.   
14 CU-UP MEs will be pooled and aligned with the services they are configured to serve. The CU-CP will assign the CU  
15 UP that an O-DU needs to connect to for a given UE session.

16 An O-DU may serve many O-RU MEs depending on its designed capacity to manage the loop 1 processing.

One Near-RT RIC will be connected to multiple CU-CP, CU-UP, and O-DU MEs. For resiliency the MEs may be connected to more than one Near-RT RIC, however, it shall not require duplication of data to be sent to each RIC instance.

0 A Near-RT RIC will be connected to one non-RT RIC.

# Appendix B: Sequence Diagram Template

This section provides a common template for the description of end-to-end use cases.

B.1 Installing the PlantUML plugin for windows

Follow the installation instructions found at: https://github.com/plantuml/word-template

The plantuml.jar file can be downloaded from: http://sourceforge.net/projects/plantuml/files/plantuml.jar/download

The word “\*.dotm” file to use would be in the “Template_Word_16” (https://github.com/plantuml/wordtemplate/tree/master/Template_Word_2016) link.

Once you have the plugin installed you can select “Show PlantUML” which will unhide the text used to generate the diagrams.

# B.2 Plant UML Colors

1 The following Palette are the named colors recognized by PlantUML. Colors can also be defined by RGB Hexcode   
2 (RRGGBB).

@startuml colors @enduml

<table><tr><td rowspan=1 colspan=1>APPLICATION</td><td rowspan=1 colspan=1>Crimson</td><td rowspan=1 colspan=1>DeepPink</td><td rowspan=1 colspan=1>Indigo</td><td rowspan=1 colspan=1>LightYellow</td><td rowspan=1 colspan=1>Navy</td><td rowspan=1 colspan=1>RoyalBlue</td><td rowspan=1 colspan=2>Turquoise</td></tr><tr><td rowspan=1 colspan=1>AliceBlue</td><td rowspan=1 colspan=1>Cyan</td><td rowspan=1 colspan=1>DeepskyBlue</td><td rowspan=1 colspan=1>Ivory</td><td rowspan=1 colspan=1>Lime</td><td rowspan=1 colspan=1>OldLace</td><td rowspan=1 colspan=1>STRATEGY</td><td rowspan=1 colspan=2>violet</td></tr><tr><td rowspan=1 colspan=1>Antiquewhite</td><td rowspan=1 colspan=1>DarkBlue</td><td rowspan=1 colspan=1>DimGray</td><td rowspan=1 colspan=1>Khaki</td><td rowspan=1 colspan=1>LimeGreen</td><td rowspan=1 colspan=1>olive</td><td rowspan=1 colspan=1>SadleBrown</td><td rowspan=1 colspan=2>Wheat</td></tr><tr><td rowspan=1 colspan=1>Aqua</td><td rowspan=1 colspan=1>Darkcyan</td><td rowspan=1 colspan=1>DimGrey</td><td rowspan=1 colspan=1>Lavender</td><td rowspan=1 colspan=1>Linen</td><td rowspan=1 colspan=1>OliveDrab</td><td rowspan=1 colspan=1>Salmon</td><td rowspan=1 colspan=2>white</td></tr><tr><td rowspan=1 colspan=1>Aquamarine</td><td rowspan=1 colspan=1>DarkGoldenRod</td><td rowspan=1 colspan=1>DodgerBlue</td><td rowspan=1 colspan=1>LavenderBlush</td><td rowspan=1 colspan=1>MOTIVATION</td><td rowspan=1 colspan=1>Orange</td><td rowspan=1 colspan=1>SandyBrown</td><td rowspan=1 colspan=2>Whitesmoke</td></tr><tr><td rowspan=1 colspan=1>Azure</td><td rowspan=1 colspan=1>DarkGray</td><td rowspan=1 colspan=1>FireBrick</td><td rowspan=1 colspan=1>LawnGreen</td><td rowspan=1 colspan=1>Magenta</td><td rowspan=1 colspan=1>OrangeRed</td><td rowspan=1 colspan=1>SeaGreen</td><td rowspan=1 colspan=2>Yellow</td></tr><tr><td rowspan=1 colspan=1>BUSINESS</td><td rowspan=1 colspan=1>DarkGreen</td><td rowspan=1 colspan=1>FloralWhite</td><td rowspan=1 colspan=1>Lemonchiffon</td><td rowspan=1 colspan=1>Maroon</td><td rowspan=1 colspan=1>orchid</td><td rowspan=1 colspan=1>Seashell</td><td rowspan=1 colspan=2>YellowGreen</td></tr><tr><td rowspan=1 colspan=1>Beige</td><td rowspan=1 colspan=1>DarkGrey</td><td rowspan=1 colspan=1>ForestGreen</td><td rowspan=1 colspan=1>LightBlue</td><td rowspan=1 colspan=1>MediumAquaMarine</td><td rowspan=1 colspan=1>PHYSICAL</td><td rowspan=1 colspan=1>sienna</td><td rowspan=1 colspan=2></td></tr><tr><td rowspan=1 colspan=1>Bisque</td><td rowspan=1 colspan=1>DarkKhaki</td><td rowspan=1 colspan=1>Fuchsia</td><td rowspan=1 colspan=1>Lightcoral</td><td rowspan=1 colspan=1>MediumBlue</td><td rowspan=1 colspan=1>PaleGoldenRod</td><td rowspan=1 colspan=1>silver</td><td rowspan=1 colspan=2></td></tr><tr><td rowspan=1 colspan=1>Black</td><td rowspan=1 colspan=1>DarkMagenta</td><td rowspan=1 colspan=1>Gainsboro</td><td rowspan=1 colspan=1>Lightcyan</td><td rowspan=1 colspan=1>Mediumorchid</td><td rowspan=1 colspan=1>PaleGreen</td><td rowspan=1 colspan=1>SkyBlue</td><td rowspan=2 colspan=2></td></tr><tr><td rowspan=1 colspan=1>BlanchedAImond</td><td rowspan=1 colspan=1>DarkOliveGreen</td><td rowspan=1 colspan=1>GhostWhite</td><td rowspan=1 colspan=1>LightGoldenRodYellow</td><td rowspan=1 colspan=1>MediumPurple</td><td rowspan=1 colspan=1>PaleTurquoise</td><td rowspan=1 colspan=1>SlateBlue</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Blue</td><td rowspan=1 colspan=1>Darkorchid</td><td rowspan=1 colspan=1>Gold</td><td rowspan=1 colspan=1>LightGray</td><td rowspan=1 colspan=1>MediumSeaGreen</td><td rowspan=1 colspan=1>PaleVioletRed</td><td rowspan=1 colspan=1>SlateGray</td><td rowspan=1 colspan=1></td><td rowspan=2 colspan=1></td></tr><tr><td rowspan=1 colspan=1>BlueViolet</td><td rowspan=1 colspan=1>DarkRed</td><td rowspan=1 colspan=1>GoldenRod</td><td rowspan=1 colspan=1>LightGreen</td><td rowspan=1 colspan=1>MediumSlateBlue</td><td rowspan=1 colspan=1>PapayaWhip</td><td rowspan=1 colspan=1>SlateGrey</td><td></td></tr><tr><td rowspan=1 colspan=1>Brown</td><td rowspan=1 colspan=1>Darksalmon</td><td rowspan=1 colspan=1>Gray</td><td rowspan=1 colspan=1>LightGrey</td><td rowspan=1 colspan=1>MediumspringGreen</td><td rowspan=1 colspan=1>PeachPuff</td><td rowspan=1 colspan=1>Snow</td><td rowspan=9 colspan=2></td></tr><tr><td rowspan=1 colspan=1>BurlyWood</td><td rowspan=1 colspan=1>DarkSeaGreen</td><td rowspan=1 colspan=1>Green</td><td rowspan=1 colspan=1>LightPink</td><td rowspan=1 colspan=1>MediumTurquoise</td><td rowspan=1 colspan=1>Peru</td><td rowspan=1 colspan=1>SpringGreen</td></tr><tr><td rowspan=1 colspan=1>CadetBlue</td><td rowspan=1 colspan=1>DarkSlateBlue</td><td rowspan=1 colspan=1>GreenYellow</td><td rowspan=1 colspan=1>Lightsalmon</td><td rowspan=1 colspan=1>MediumVioletRed</td><td rowspan=1 colspan=1>Pink</td><td rowspan=1 colspan=1>SteelBlue</td></tr><tr><td rowspan=1 colspan=1>Chartreuse</td><td rowspan=1 colspan=1>DarkSlateGray</td><td rowspan=1 colspan=1>Grey</td><td rowspan=1 colspan=1>LightseaGreen</td><td rowspan=1 colspan=1>MidnightBlue</td><td rowspan=1 colspan=1>Plum</td><td rowspan=1 colspan=1>TECHNOLOGY</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Chocolate</td><td rowspan=1 colspan=1>DarkSlateGrey</td><td rowspan=1 colspan=1>HoneyDew</td><td rowspan=1 colspan=1>LightskyBlue</td><td rowspan=1 colspan=1>Mintcream</td><td rowspan=1 colspan=1>PowderBlue</td><td rowspan=1 colspan=1>Tan</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Coral</td><td rowspan=1 colspan=1>DarkTurquoise</td><td rowspan=1 colspan=1>HotPink</td><td rowspan=1 colspan=1>LightslateGray</td><td rowspan=1 colspan=1>MistyRose</td><td rowspan=1 colspan=1>Purple</td><td rowspan=1 colspan=1>Teal</td></tr><tr><td rowspan=2 colspan=1>CornflowerBlue</td><td rowspan=2 colspan=1>DarkViolet</td><td rowspan=2 colspan=1>IMPLEMENTATION</td><td rowspan=2 colspan=1>LightslateGrey</td><td rowspan=2 colspan=1>Moccasin</td><td rowspan=2 colspan=1>Red</td><td rowspan=2 colspan=1>Thistle</td></tr><tr></tr><tr><td rowspan=1 colspan=1>Cornsilk</td><td rowspan=1 colspan=1>Darkorange</td><td rowspan=1 colspan=1>IndianRed</td><td rowspan=1 colspan=1>LightsteelBlue</td><td rowspan=1 colspan=1>NavajoWhite</td><td rowspan=1 colspan=1>RosyBrown</td><td rowspan=1 colspan=1>Tomato</td></tr></table>

# B.3 Depicting human actors as participants

The participant type Actor should be used. For Clarity these should be the first group and therefore always on the left side of the diagram. The color “#lightblue” has been identified as the background for this group of use case participants.

@startuml   
Box “Personnel” #lightblue Actor FT as “Field Technician” Actor RP as “Radio Planner”   
End box   
@enduml

![](images/f58641e0d1b8a9a4939f6c361b44b22a07b76fce3c9aa069696e0736e0b8ca0e.jpg)

> **Image Summary:** (Summary not available)


1

2 At times it may be desirable to identify external data sources. These would be presented using the same color as   
3 personnel but be titled as Non-RAN Data. The Source of the data would be identified as an “Entity”. The list of these   
4 could be immense but small within the context of a use case. Therefore, a few examples are shown below, and is not   
5 intended to be an exhaustive list.

@startuml   
Box “Non-RAN Data” #lightblue Entity weather as “Weather Data” Entity fire as “Fire Data” Entity earth as “Earthquake Data” Entity subs as “Subscriber Data”   
End box   
@enduml

![](images/9f54ada7cade084deb55d9c025be8c3e0ff60aad351df560f3be2ca14290b94f.jpg)

> **Image Summary:** (Summary not available)


# B.4 Depicting Service Management and Orchestration Participants

Service Management and Orchestration participants can vary by type. The following UML shows the standard types for defined participants. Participants can be deleted when not pertinent to the use case but additional participants should be avoided unless they are defined in the O-RAN Architecture Description [17] or other O-RAN specifications. For consistency SMO should be the second group unless the personnel group is not required which would make this the first group. The color “#gold” has been identified as the background for this group of use case participants.

22 23 24 The O-RAN Architecture [17] identifies three types of functions in SMO: FCAPS for O-RAN Network Functions(named here as “OAM Functions”), Non-RT RIC, and O-Cloud Management, Orchestration and Workflow Management. The O2 General Aspects and Principles [21] further distinguishes between management of the 25 distribution of O-Cloud software and orchestration for O-Cloud life cycle processes, called “Federated O-Cloud 26 Operations and Management”, or “FOCOM”, and coordination between SMO and the O-Cloud for managing 27 deployment life cycle events and operational processes, called “Network Function Orchestration”, or “NFO”. These are 28 shown as participants in the UML as below.

@startuml   
Box “Service Orchestration and Management Framework” #gold participant NFO participant SMO as “OAM Functions” Collections RPGF as “non-RT RIC” Participant FOCOM

end box @enduml

![](images/f8af2fe16c4aa7e8fc44f7bdb19ad130fc1261c90f86a3c3e8800727ab0cf915.jpg)

> **Image Summary:** (Summary not available)


# B.5 Depicting Cloud Platform Participants

7 As described in the O-Ran Architecture Description [17] the Cloud platform has two roles. These are depicted by the   
8 end points in the O-Cloud Management and Control Planes. The Infrastructure Management Services (IMS) provides   
9 management of the O-Cloud as a platform. The Deployment Management Services (DMS) provides management of   
10 Deployments using the O-Cloud resources. Like in the SMO the internal software modules and components to the O  
11 Cloud can vary from implementation to implementation. Therefore it is not advised to add additional entities unless it is   
12 unavoidable for the use case. The color “#lightseagreen” has been identified as the background for this group of use   
13 case participants.

@startuml   
Box “O-Cloud Platform” #lightseagreen participant IMS participant DMS   
End box   
@enduml

![](images/d52a69fc616f959d2fdc49cd18ee4d64748eb58d4b9cf4ced979736f06672680.jpg)

> **Image Summary:** (Summary not available)


# B.6 O-RAN Managed Elements as participants

The O-RAN architecture defines 5 Managed Functions (MF) which can be deployed independently or aggregated in different ways into a Managed Element (ME). The O-CU is a predefined aggregation of the O-CU-CP and O-CU-UP.

@startuml   
Box “O-RAN” #lightpink Participant RIC as “near-RT RIC” Participant OCUCP as “O-CU-CP” Participant OCUUP as “O-CU-UP” Participant OCU as “O-CU” Participant ODU as “O-DU” Participant ORU as “O-RU”   
end box   
@enduml

![](images/499cf0a878fbef61860d51b1829510a3116534e6f4a8902770f35c56ccba2f3a.jpg)

> **Image Summary:** (Summary not available)


# 1 B.7 3GPP RAN elements as participants

2 On occasion some use cases may need to show interaction between O-RAN and 3GPP elements. 3GPP defines both   
3 LTE and 5G elements. The gNodeB is also defined with a split defining the Centralized Unit (CU) and the Distributed   
4 Unit (DU). These participants are in the 3GPPP RAN box with a background of “#Tan”.

@startuml   
Box “3GPP RAN” #Tan Participant eNB Participant gNB Participant CU Participant DU   
Endbox   
@enduml

![](images/faaf2dcc765c06dbd3080e76f3804236ec33b8e0cc59f38a613ed6acaeb29110.jpg)

> **Image Summary:** (Summary not available)


13

# B.8 Messaging

Autonumber should be used so that individual messages in a diagram can be easily referenced in conversation.

Synchronous calls have an implicit return or the return can be implicitly depicted, often after a long block so as to provide clarity of where processing continues. Some use cases can be used with a start message and end with either a message or response. This is helpful when a common block can be used multiple times.

@startuml   
Autonumber   
Participant One   
Participant Two   
[-> One : Use Case incoming message   
One $- >$ Two: Synchronous Call   
Two ->> One : Asynchronous message   
One -> One : Call to Self   
Two $- >$ ] : Use Case outgoing message   
Two --> One : Explicit Synchronous Return [<-- One : Use Case Return Message   
@enduml

![](images/b7c6d3e92c1a5ebfbb71e52e3791e2911f37256173fe07637d6d53cdf22ea25d.jpg)

> **Image Summary:** (Summary not available)


# 1 B.9 Adding Comments

Comments can be added to the diagram. This is sometimes better than trying to describe the comment in text or for the picture to be able to standalone.

@startuml   
Autonumber   
Participant One   
Participant Two   
Note over One   
Notes can be used and placed over a lifeline   
To describe something happening along that line   
End note   
[-> One : Use Case incoming message   
Rnote over One, Two   
Notes can be a simple rectangle instead of the standard   
Note above and can be spanning multiple life lines to   
Describe the interaction about to occur   
endrnote   
One -> Two: Synchronous Call   
Hnote right One   
The can be hexagonal and to the Right   
Endhnote   
Hnote over One   
Over   
endhnote   
Hnote left One   
Or Left of a lifeline   
endhnote   
Two -> Two :   
Note Right : Messages on notes can\nbe used to describe\ninternal processing\nwithout adding to\nparticpant spacing.   
Two ->> One : Asynchronous message   
Note Left: Message Notes can be\nright or left of the\nmessage but must be\nimmediately after the\nmessage they are noting.   
Note over One #fuchsia   
Note backgrounds can be \*\*changed\*\* as //well// as the __text__   
End note   
One -> One : Call to Self   
Two $- >$ ] : Use Case outgoing message   
Two --> One : Explicit Synchronous Return   
[<-- One : Use Case Return Message   
@enduml

![](images/0904b5dc31374ceaa435887e9ccb08ffbda365f91d26ec6b9327ab124cb76a0f.jpg)

> **Image Summary:** (Summary not available)


# B.10 Participant Creation/Deletion

Sometimes clarity is depicted by showing when a participant is created or first comes into being and likewise when it is destroyed. This is very helpful in understanding timing and existence of a participant. This happens with modifiers to the message.

@startuml   
Autonumber   
Participant One   
Participant Two   
[-> One : Use Case incoming message

One $- >$ Two \*\*: Synchronous Call Two $- > >$ One : Asynchronous message Two $- >$ ] : Use Case outgoing message Two $- >$ Two !! : Terminate One $- >$ One : Call to Self [<-- One : Use Case Return Message @enduml

![](images/60ffde1ef2ec96634da5b9b09d74a03a11b70ea268708dbcdce08f61dcce7b29.jpg)

> **Image Summary:** (Summary not available)


# B.11 Dividers

In some cases, it is helpful to provide divisions of separate activities of the use case. This can be to define pre-requisite activity such as configuration or subscriptions to an event. It can also be used to depict stages of a lifecycle.

@startuml   
Autonumber   
Box “Personnel” #lightblue Actor FT as “Field Technician” Actor RP as “Radio Planner” Actor SD as “Service Designer”   
End box   
Box “Orchestration and Management Platform” #gold participant SMO as “OAM Functions”   
end box   
Box “O-Cloud Platform” #lightseagreen participant OCM as “IMS”   
End box   
Box “O-RAN” #NavajoWhite Participant OCU as “O-CU”   
end box   
Box “3GPP RAN” #Tan Participant DU   
Endbox   
$= =$ Service Design $= =$   
SD -> SMO : Onboard Service Descriptor   
SMO -> OCM : Onboard VNF Descriptor

![](images/57e203ca2121ab160b27863abbe6f29c505f490b7e44dff18bb7b6b255e32eb5.jpg)

> **Image Summary:** (Summary not available)


# B.12 Grouping and References

Grouping can be used for many different aspects. In UML there are many types of groups. PlantUML support the basic three. Any of the group types can be nested. “Alt” for conditional processing which can show different path processing rather than just a sunny day scenario. It can also be used to show any logical, as the condition is stated in the swim lane, processing. Sometimes the message and the grouping boundary are close and need some separation. Use the “|||” to create that space.

The “loop” group is used to show iterations or conditional loops. The loop condition is stated on the lines and contain the statements within the loop.

The last kind of group is the fragment. This is a logic group of a sequence of events that go together. The tag line at the top describes the group.

Although references look like groups they cannot be nested. Use the single line version for references to use cases in the current document. The Multi-Line version should be used for reference to use cases in an external document.

@startuml   
Box “Orchestration and Management Platform” #gold participant SMO as “Orchestration”   
end box   
Box “O-RAN” #NavajoWhite Participant ODU as “O-DU” Participant ORU as “O-RU”   
end box   
Group Configure O-RU associated with O-DU   
Alt if flat management model then Loop for each O-RU managed by the current O-DU SMO -> ORU : Config (Full_Config) ref over ORU : Edit-Config <color red>(Internal Document Reference)</color> Hnote over ORU Ready Endhnote End |||   
Else else if hierarchical model then SMO $- >$ ODU : Config_RU (Global_Config) Loop for each O-RU managed by this O-DU instance ODU $- >$ ODU : Full_Config $=$ Config_Merge (Global_Config, Local_Config) ODU $- >$ ORU : Config (Full_Config) ref over ORU Edit-Config <color red>(External Document Reference)</color> WG4 M-Plane Specification [12] End ref Hnote over ORU Ready endhnote end ||   
Else else must be hybrid model then Rnote over SMO, ORU Order of Global and Local Configuration can vary Endrnote Loop for each O-RU managed by the current O-DU SMO -> ORU : Config (Global_Config) end Loop for each O-RU managed by this O-DU instance ODU -> ORU : Config (Local_Config) end Alt If both Local_Config and Local_Config Received then ref over ORU Edit-Config WG4 M-Plane Specification [12] End ref Hnote over ORU Ready endhnote End   
End   
end   
@enduml

![](images/b3a6ba217bf03f4f03a51eabfd6c39b9644aaa292633ac83587108eeacbd2938.jpg)

> **Image Summary:** (Summary not available)


# 1 Annex A: SMO and Non-RT RIC mapping with 3GPP management 2 system

This section shows the SMO, Non-RT RIC and the related management interface/service mapping with 3GPP management system.

In [9], 3GPP defines the network management and orchestration architecture for 3GPP networks including network slicing. The management data analytic function (MDAF) is identified as the key function to enable the intelligent management of the network, which provides management data analytics service (MDAS) to both the management functions and the network element. Meanwhile, intent driven management service (IDMS) is under discussion in 3GPP SA5, where the management system could generate intent as the target of the network optimization and automation. The management system should have the capability to consume the service (IDMS) provided by the network. Currently, the two studies are mainly to enable the network management automaton and intelligence. In this sense, it is quite aligned with the motivation of introducing Non-RT RIC in O-RAN.

To better understand the O-RAN OAM architecture, the management services defined in O-RAN, and the relationship with 3GPP and the potential gaps between 3GPP and O-RAN. Fig. A-1 below tries to do some mapping between the SMO, Non-RT RIC and 3GPP management system and interfaces with the following preliminary analysis.

1. A1 interface is closely related to the current SA5 3GPP IDMS and MDAS study.

(1) A1-P, as declarative policy is closely related to Intent-NOP discussed in IDMS. Performance target is expected to be provided by management system via the IDMS. But only system level targets are being discussed in the IDMS study. A1-P is finer granularity to enable the UE level, group UE level and even application level automation and optimization.

(2) A1-EI/ML is closely related to the 3GPP MDAS study. MDAS provider is expected to provide data analytics reports and recommendations to the consumers, e.g., CN or RAN leveraging the data analytics and machine learning technologies. AI-EI/ML studied in O-RAN is to enable the enrichment information communication and ML model management towards the RAN. The enrichment information may come from the data analytics based on the historical RAN data collected over O1 interface or from RAN external data sources. In this sense, A1-EI/ML has a larger scope than the MDAS in 3GPP.

2. O1 interface reflects the 3GPP traditional FCAPS management services.

3. O2 interface perform the O-Cloud management, the mapping with 3GPP is FFS.

4. Non-RT RIC could be seen as a MDAF instance, which provides management data analytic service to both internal functions reside in the SMO and external consumers such as near-RT RIC.

The management service, Non-RT RIC and A1 work in O-RAN will continue evolve and the MDAS/IDMS related SI/WI are under study and still in early stage in 3GPP. The gap analysis and mapping relationship will be continuously updated based on the latest progress.

![](images/5efd4de0d4ac24ac31f37f0b4b0fddec646d78cc5b0b03d33ea86a24be9e6d02.jpg)

> **Image Summary:** (Summary not available)
  
Figure A- 1: SMO and Non-RT RIC mapping with the 3GPP management system

1 Note :

2 3 i. The figure shows the entire services provided by the SMO Framework, the O-Cloud management and Integration   
fabric and data service defined by O-RAN so far there is no corresponding services defined in 3GPP.   
4 ii. The Security management service and Accounting management defined in 3GPP so far they are not used in OAM   
5 Functions.   
6 iii. The A1 Policy management, A1 EI management, A1 ML management are being studied in O-RAN and being   
7 implemented in O-RAN software community.   
8 iv. The A1 Policy management maps to 3GPP IDMS.   
9 v. A1 EI management and A1 ML management is correlated to the MDAS, when the EI is retrieved from the Data   
10 Analytic and AI/ML Model Training, the concrete mapping relationship with 3GPP is FFS.   
11 vi. The Data Analytics and AI/ML Model Training studied in O-RAN maps to 3GPP RAN domain MDAS producer.

# Annex ZZZ : O-RAN Adopter License Agreement

BY DOWNLOADING, USING OR OTHERWISE ACCESSING ANY O-RAN SPECIFICATION, ADOPTER AGREES TO THE TERMS OF THIS AGREEMENT.

This O-RAN Adopter License Agreement (the “Agreement”) is made by and between the O-RAN Alliance and the entity that downloads, uses or otherwise accesses any O-RAN Specification, including its Affiliates (the “Adopter”).

This is a license agreement for entities who wish to adopt any O-RAN Specification.

# 7 Section 1: DEFINITIONS

1.1 “Affiliate” means an entity that directly or indirectly controls, is controlled by, or is under common control with another entity, so long as such control exists. For the purpose of this Section, “Control” means beneficial ownership of fifty $( 5 0 \% )$ percent or more of the voting stock or equity in an entity.

1 1.2 “Compliant Implementation” means any system, device, method or operation (whether implemented in hardware,   
2 software or combinations thereof) that fully conforms to a Final Specification.   
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

3.1 Members, Contributors and Academic Contributors and their Affiliates are prepared to grant based on a separate Patent License Agreement to each Adopter under Fair Reasonable And Non- Discriminatory (FRAND) terms and conditions with or without compensation (royalties) a nonexclusive, non-transferable, irrevocable (but subject to Defensive Suspension), non-sublicensable, worldwide patent license under their Necessary Claims to make, have made, use, import, offer to sell, lease, sell and otherwise distribute Compliant Implementations; provided, however, that such license shall not extend: (a) to any part or function of a product in which a Compliant Implementation is incorporated that is not itself part of the Compliant Implementation; or (b) to any Adopter if that Adopter is not making a reciprocal grant to Members, Contributors and Academic Contributors, as set forth in Section 3.3. For the avoidance of doubt, the foregoing licensing commitment includes the distribution by the Adopter’s distributors and the use by the Adopter’s customers of such licensed Compliant Implementations.

3.2 Notwithstanding the above, if any Member, Contributor or Academic Contributor, Adopter or their Affiliates has reserved the right to charge a FRAND royalty or other fee for its license of Necessary Claims to Adopter, then Adopter is entitled to charge a FRAND royalty or other fee to such Member, Contributor or Academic Contributor, Adopter and its Affiliates for its license of Necessary Claims to its licensees.

9 3.3 Adopter, on behalf of itself and its Affiliates, shall be prepared to grant based on a separate Patent License   
10 Agreement to each Members, Contributors, Academic Contributors, Adopters and their Affiliates under Fair   
11 Reasonable And Non-Discriminatory (FRAND) terms and conditions with or without compensation (royalties) a   
12 nonexclusive, non-transferable, irrevocable (but subject to Defensive Suspension), non-sublicensable, worldwide patent   
13 license under their Necessary Claims to make, have made, use, import, offer to sell, lease, sell and otherwise distribute   
14 Compliant Implementations; provided, however, that such license will not extend: (a) to any part or function of a   
15 product in which a Compliant Implementation is incorporated that is not itself part of the Compliant Implementation; or   
16 (b) to any Members, Contributors, Academic Contributors, Adopters and their Affiliates that is not making a reciprocal   
17 grant to Adopter, as set forth in Section 3.1. For the avoidance of doubt, the foregoing licensing commitment includes   
18 the distribution by the Members’, Contributors’, Academic Contributors’, Adopters’ and their Affiliates’ distributors   
19 and the use by the Members’, Contributors’, Academic Contributors’, Adopters’ and their Affiliates’ customers of such   
20 licensed Compliant Implementations.

# Section 4: TERM AND TERMINATION

4.1 This Agreement shall remain in force, unless early terminated according to this Section 4.

4.2 O-RAN Alliance on behalf of its Members, Contributors and Academic Contributors may terminate this Agreement if Adopter materially breaches this Agreement and does not cure or is not capable of curing such breach within thirty (30) days after being given notice specifying the breach.

4.3 Sections 1, 3, 5 - 11 of this Agreement shall survive any termination of this Agreement. Under surviving Section 3, after termination of this Agreement, Adopter will continue to grant licenses (a) to entities who become Adopters after the date of termination; and (b) for future versions of O-RAN Specifications that are backwards compatible with the version that was current as of the date of termination.

# Section 5: CONFIDENTIALITY

Adopter will use the same care and discretion to avoid disclosure, publication, and dissemination of O-RAN Specifications to third parties, as Adopter employs with its own confidential information, but no less than reasonable care. Any disclosure by Adopter to its Affiliates, contractors and consultants should be subject to an obligation of confidentiality at least as restrictive as those contained in this Section. The foregoing obligation shall not apply to any information which is: (1) rightfully known by Adopter without any limitation on use or disclosure prior to disclosure; (2) publicly available through no fault of Adopter; (3) rightfully received without a duty of confidentiality; (4) disclosed by O-RAN Alliance or a Member, Contributor or Academic Contributor to a third party without a duty of confidentiality on such third party; (5) independently developed by Adopter; (6) disclosed pursuant to the order of a court or other authorized governmental body, or as required by law, provided that Adopter provides reasonable prior written notice to O-RAN Alliance, and cooperates with O-RAN Alliance and/or the applicable Member, Contributor or Academic Contributor to have the opportunity to oppose any such order; or (7) disclosed by Adopter with O-RAN Alliance’s prior written approval.

# Section 6: INDEMNIFICATION

Adopter shall indemnify, defend, and hold harmless the O-RAN Alliance, its Members, Contributors or Academic Contributors, and their employees, and agents and their respective successors, heirs and assigns (the “Indemnitees”), against any liability, damage, loss, or expense (including reasonable attorneys’ fees and expenses) incurred by or imposed upon any of the Indemnitees in connection with any claims, suits, investigations, actions, demands or judgments arising out of Adopter’s use of the licensed O-RAN Specifications or Adopter’s commercialization of products that comply with O-RAN Specifications.

# Section 7: LIMITATIONS ON LIABILITY; NO WARRANTY

2 EXCEPT FOR BREACH OF CONFIDENTIALITY, ADOPTER’S BREACH OF SECTION 3, AND ADOPTER’S   
3 INDEMNIFICATION OBLIGATIONS, IN NO EVENT SHALL ANY PARTY BE LIABLE TO ANY OTHER   
4 PARTY OR THIRD PARTY FOR ANY INDIRECT, SPECIAL, INCIDENTAL, PUNITIVE OR CONSEQUENTIAL   
5 DAMAGES RESULTING FROM ITS PERFORMANCE OR NON-PERFORMANCE UNDER THIS AGREEMENT,   
6 IN EACH CASE WHETHER UNDER CONTRACT, TORT, WARRANTY, OR OTHERWISE, AND WHETHER OR   
7 NOT SUCH PARTY HAD ADVANCE NOTICE OF THE POSSIBILITY OF SUCH DAMAGES. O-RAN   
8 SPECIFICATIONS ARE PROVIDED “AS IS” WITH NO WARRANTIES OR CONDITIONS WHATSOEVER,   
9 WHETHER EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE. THE O-RAN ALLIANCE AND THE   
10 MEMBERS, CONTRIBUTORS OR ACADEMIC CONTRIBUTORS EXPRESSLY DISCLAIM ANY WARRANTY   
11 OR CONDITION OF MERCHANTABILITY, SECURITY, SATISFACTORY QUALITY, NONINFRINGEMENT,   
12 FITNESS FOR ANY PARTICULAR PURPOSE, ERROR-FREE OPERATION, OR ANY WARRANTY OR   
13 CONDITION FOR O-RAN SPECIFICATIONS.

# Section 8: ASSIGNMENT

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

In the event that any provision of this Agreement conflicts with governing law or if any provision is held to be null, void or otherwise ineffective or invalid by a court of competent jurisdiction, (i) such provisions will be deemed stricken from the contract, and (ii) the remaining terms, provisions, covenants and restrictions of this Agreement will remain in full force and effect.

Any failure by a party or third party beneficiary to insist upon or enforce performance by another party of any of the provisions of this Agreement or to exercise any rights or remedies under this Agreement or otherwise by law shall not be construed as a waiver or relinquishment to any extent of the other parties’ or third party beneficiary’s right to assert or rely upon any such provision, right or remedy in that or any other instance; rather the same shall be and remain in full force and effect.

# Chapter 5.