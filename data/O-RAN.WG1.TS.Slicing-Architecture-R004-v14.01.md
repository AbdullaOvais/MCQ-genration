# O-RAN Work Group 1 (Use Cases and Overall Architecture) Slicing Architecture

Copyright $©$ 2025 by the O-RAN ALLIANCE e.V.

# Contents

Foreword... ..4   
Modal verbs terminology ..... ............................................................................................. ......4   
1 Scope .......... ..........................................................................................................................................5   
2   
2.1 Normative references ......................................................................................................................................... 5   
2.2 Informative references ....................................................................................................................................... 6   
3 Definition of terms, symbols and abbreviations................................................................................. .....7   
3.1 3.2 Terms ........ Symbols .......... ............................................................................................................................. .................................................................................................. ..... 7 ..... 8   
3.3 Abbreviations.... ........................................................................................................................................ 8   
4 Slicing overview.... .................................................................................... .....9   
5 High-level O-RAN slicing use cases......................................................................................................10   
5.1 O-RAN slicing use cases .......... ...................................................................................................... 10   
5.2 O-RAN slice subnet management and provisioning use cases ........................................................................ 10   
5.2.1 O-RAN slice subnet instance creation....... ...................................................................................... 10   
5.2.2 O-RAN slice subnet instance activation ..................................................................................................... 12   
5.2.3 O-RAN slice subnet instance modification ................................................................................................ 14   
5.2.4 O-RAN slice subnet instance deactivation ................................................................................................. 16   
5.2.5 O-RAN slice subnet instance termination .................................................................................................. 18   
5.2.6 O-RAN slice subnet instance configuration ............................................................................................... 19   
5.2.7 O-RAN slice subnet feasibility check ........................................................................................................ 20   
5.3 O-RAN slicing use cases ............. ............................................................................................................. 21   
5.3.1 Use case 1: RAN slice SLA assurance ....................................................................................................... 21   
5.3.2 Use case 2: Multi-vendor slices.............. ................................................................................................... 23   
5.3.3 Use case 3: O-NSSI resource allocation optimization................................................................................ 24   
6 O-RAN slicing principles and requirements . ........................................................................................27   
6.1 General principles ...... ........................................................................................................... 27   
6.2 Slicing requirements .. .................................................................................................................................. 27   
6.2.1 Functional requirements ............................................................................................................................. 27   
6.2.2 Non-functional requirements...................................................................................................................... 30   
7 O-RAN reference slicing architecture..... ................................................................................. ....31   
7.1 O-RAN reference slicing architecture... ................................................................................ .... 31   
7.2 Non-RT RIC . ................................................................................. ....... 31   
7.3 Near-RT RIC ....... .......................................................................... ....... 32   
7.4 O-RAN Central Unit (O-CU-CP, O-CU-UP) . .............................................................................. ....... 32   
7.5 O-RAN Distributed Unit (O-DU) . .............................................................................. ....... 32   
7.6 A1 interface .... .............................................................................. ...... 33   
7.7 E2 interface..... ...... 33   
7.8 7.9 O1 interface .....O2 interface ..... ....................................................... ...... 33...... 33   
7.10 Transport network slicing .. ..... 34   
8 O-RAN slice subnet provisioning procedures......... ....... ..................................................... ...36   
8.1 O-RAN Slice Subnet Instance (O-NSSI) allocation procedure . ................................................. .... 36   
8.2 O-RAN Slice Subnet Instance (O-NSSI) modification procedure.. .................................. . 39   
8.3 O-RAN Slice Subnet Instance (O-NSSI) deallocation procedure........ ............... ... 40   
8.4 O-RAN Slice Subnet Instance (O-NSSI) feasibility check and reservation procedure.................... ... 43   
8.4.1 Introduction .... .... 43   
8.4.2 Procedure ..... .............................. ... 43   
Annex A (informative): Implementation options . ...46   
. 46

A.1 Implementation options .

A.1.1 3GPP and ETSI NFV-MANO based O-RAN slicing architecture implementation option . ... 46   
A.1.2 ONAP based O-RAN slicing architecture implementation option . .... 47   
Annex B (informative): Transport network slicing . ..................................... ....48   
B.1 Transport network slicing use cases .... .................................................................... 48   
Annex C (informative): Slicing terminology...... .............................................................. ...56   
C.1 Slicing and 3GPP slice modeling terminology awareness . ............................................................. .. 56   
C.1.1 NSI and NSSI context in 3GPP SA2 and SA5 .. ............................................................... ... 56   
C.1.2 Name containment limitation . ................................................................. .... 56   
C.1.3 Network slice subnet is a purposeful generic collection ...................................................................... ..... 57   
C.1.4 Slicing instance example ........ .............................................................................. 58   
C.1.5 NSSI slice profile and PLMNInfo.. . 59   
C.1.6 Managed functions have a list of PLMNInfo . ......................................... ..... 60   
C.1.7 Single Network Slice Selection Assistance Information (S-NSSAI) . ..... 60   
Annex D (informative): Multi-operator slice RAN management services exposure . ...61   
D.1 RAN management services exposure for multi-operator slice.... .... 61   
D.1.1 Management services exposure for multi-operator slice - Relevant standards.. .......................... ..... 62   
D.1.2 Concepts of management services exposure for multi-operator slice ..... ... 63   
D.1.3 Management aspects of external exposure of MnS related to RAN slicing . ..... 64   
D.1.4 Multi-operator slice: High-level use cases and potential requirements for exposure fo MnS related to   
O-RAN slicing ..... ..... 65   
Annex (informative): Change history/Change request (history) .. ...75

# Foreword

This Technical Specification (TS) has been produced by WG1 of the O-RAN Alliance.

The content of the present document is subject to continuing work within O-RAN and may change following formal ORAN approval. Should the O-RAN Alliance modify the contents of the present document, it will be re-released by ORAN with an identifying change of version date and an increase in version number as follows:

version xx.yy.zz

where:

xx: the first digit-group is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc. (the initial approved document will have $\scriptstyle \mathbf { X } \mathbf { X } = 0 1$ ). Always 2 digits with leading zero if needed.   
yy: the second digit-group is incremented when editorial only changes have been incorporated in the document. Always 2 digits with leading zero if needed.   
zz: the third digit-group included only in working versions of the document indicating incremental changes during the editing process. External versions never include the third digit-group. Always 2 digits with leading zero if needed.

# Modal verbs terminology

In the present document "shall", "shall not", "should", "should not", "may", "need not", "will", "will not", "can" and "cannot" are to be interpreted as described in clause 3.2 of the O-RAN Drafting Rules (Verbal forms for the expression of provisions).

"must" and "must not" are NOT allowed in O-RAN deliverables except when used in direct citation.

# 1 Scope

The present document specifies the high level O-RAN slicing related use cases, requirements and architecture. While some of the requirements are derived from use cases, some of the relevant SDO requirements are captured as they have impact on O-RAN functions. Along with requirements and reference slicing architecture, slicing related impact to O-RAN functions and interfaces are captured as well.

# 2 References

# 2.1 Normative references

References are either specific (identified by date of publication and/or edition number or version number) or non-specific. For specific references, only the cited version applies. For non-specific references, the latest version of the referenced document (including any amendments) applies. In the case of a reference to a 3GPP document, a non-specific reference implicitly refers to the latest version of that document in Release 18, or the latest 3GPP release prior to Release 18 that includes that document.

NOTE: While any hyperlinks included in this clause were valid at the time of publication, O-RAN cannot guarantee their long term validity.

The following referenced documents are necessary for the application of the present document.

<table><tr><td>[1]</td><td>3GPP TS 22.261: Technical Specification Group Services and System Aspects; Service requirements for the 5G system; Stage 1</td></tr><tr><td>[2]</td><td>3GPP TS 23.501: Technical Specification Group Services and System Aspects; System Architecture for the 5G System; Stage 2</td></tr><tr><td>[3]</td><td>3GPP TS 28.526: Technical Specification Group Services and System Aspects; Telecommunication management; Life Cycle Management (LCM) for mobile networks that include virtualized network</td></tr><tr><td>[4]</td><td>functions; Procedures 3GPP TS 28.531: Management and orchestration; Provisioning, Release 16, March 2020.</td></tr><tr><td>[5]</td><td>3GPP TS 28.532: Management and orchestration; Generic Management Services</td></tr><tr><td>[6]</td><td>Void</td></tr><tr><td>[7]</td><td>3GPP TS 28.541: Management and orchestration; 5G Network Resource Model (NRM); Stage 2 and stage 3</td></tr><tr><td>[8]</td><td>3GPP TS 28.552: Technical Specification Group Services and System Aspects; Management and orchestration; 5G performance measurements</td></tr><tr><td>[9]</td><td>3GPP TS 32.300: Technical Specification Group Services and System Aspects; Telecommunication management; Configuration Management (CM); Name convention for managed objects</td></tr><tr><td>[10]</td><td>3GPP TS 38.300: NR and NG-RAN Overall Description</td></tr><tr><td>[11]</td><td>ETSI GS NFV 003: Network Functions Virtualisation (NFV); Terminology for Main Concepts in NFV</td></tr><tr><td>[12]</td><td>Void</td></tr><tr><td>[13]</td><td>O-RAN.WG1.O1-Interface.0-v04.00: O-RAN Operations and Maintenance Interface Specification</td></tr><tr><td>[14]</td><td>Void</td></tr></table>

[15] Void   
[16] Void   
[17] Void   
[18] O-RAN.WG6.ORCH-USE-CASES-v04.00: Orchestration Use Cases and Requirements for O-RAN Virtualized RAN   
[19] Void   
[20] Void   
[21] Void   
[22] Void   
[23] 3GPP TS 28.530: Management and orchestration; Concepts, use cases and requirements   
[24] O-RAN.WG11.Security-Protocols-Specification: “O-RAN Working Group 11 (Security Working Group) Security Protocols Specifications”

# 2.2 Informative references

References are either specific (identified by date of publication and/or edition number or version number) or non-specific. For specific references, only the cited version applies. For non-specific references, the latest version of the referenced document (including any amendments) applies. In the case of a reference to a 3GPP document, a non-specific reference implicitly refers to the latest version of that document in Release 18, or the latest 3GPP release prior to Release 18 that includes that document.

NOTE: While any hyperlinks included in this clause were valid at the time of publication, O-RAN cannot guarantee their long term validity.

The following referenced documents are not necessary for the application of the present document but they assist the user with regard to a particular subject area.

<table><tr><td>[i.1]</td><td>3GPP TR 21.905: &quot;Vocabulary for 3GPP Specifications&quot;.</td></tr><tr><td>[i.2]</td><td>3GPP TS 23.003: “Technical Specification Group Core Network and Terminals; Numbering, addressing and identification&#x27;&quot;.</td></tr><tr><td>[i.3]</td><td>3GPP TR 28.801: &quot;Study on management and orchestration of network slicing for next generation network&quot;.</td></tr><tr><td>[i.4]</td><td>O-RAN_Study_ORAN_Slicing_Technical_Report.v02.00: &quot;Study on O-RAN Slicing&quot;, Technical Report.</td></tr><tr><td>[i.5]</td><td>3GPP TS 23.222: &quot;Functional architecture and information flows to support Common API Framework for 3GPP Northbound APIs; Stage 2&quot;, Release 17, June 2021.</td></tr><tr><td>[i.6]</td><td>3GPP TS 29.222: &quot;Common API Framework for 3GPP Northbound APIs&quot;, Release 17, December 2021.</td></tr><tr><td>[i.7]</td><td>3GPP TR 28.824: &quot;Study on network slice management capability exposure&#x27;&quot;, Release 17, July 2022.</td></tr><tr><td>[i.8]</td><td>3GPP TR 28.811: &quot;Management and orchestration; Study on Network Slice Management Enhancement&quot;&#x27;, Release 17, December 2021.</td></tr><tr><td>[i.9]</td><td>3GPP TR 23.700-99: Study on Network Slice Capability Exposure for Application Layer Enablement&quot;, Release 18, September 2022.</td></tr></table>

[i.10] Slicenet, https://5g-ppp.eu/slicenet/.   
[i.11] NGMN Alliance: “5G P1 Requirements & Architecture “Description of Network Slicing Concept”, Version 1.0.8, September 2016.   
[i.12] O-RAN.WG1.OAM-Architecture- $\mathbf { \partial } \cdot \mathbf { v } 0 4 . 0 0$ : “O-RAN WG1 Operations and Maintenance Architecture”.   
[i.13] O-RAN.WG2.A1.GA&P-v01.00: “O-RAN Working Group 2; (A1 interface: General Aspects and Principles)”.   
[i.14] O-RAN.WG3.E2GAP-v01.00: “O-RAN Working Group 3; Near-Real-time RAN Intelligent Controller Architecture & E2 General Aspects and Principles”.   
[i.15] O-RAN.WG6.CAD-V02.01: “Cloud Architecture and Deployment Scenarios for O-RAN Virtualized RAN”.   
[i.16] O-RAN.WG9.XPSAAS-v01.00: “O-RAN Open Transport Working Group 9 Xhaul Packet Switched Architectures and Solutions”.   
[i.17] O-RAN.WG9.XTRP-REQ-v01.00: “O-RAN Open Xhaul Transport Working Group 9 Xhaul Transport Network Requirements”.   
[i.18] 3GPP TS 28.533: “Management and orchestration; Architecture framework”, Release 17, March 2022.   
[i.19] O-RAN.WG9.XTRP-MGT.0-v04.00: “O-RAN Open X-haul Transport Working Group Management interfaces for Transport Network Elements”

# 3 Definition of terms, symbols and abbreviations

# 3.1 Terms

For the purposes of the present document, the terms and definitions [given in [i.1] and the following] apply. A term defined in the present document takes precedence over the definition of the same term, if any, in [i.1].

A1: Interface between Non-RT RIC and Near-RT RIC to enable policy-driven guidance of Near-RT RIC applications/functions, and support AI/ML workflow.

A1 policy: Type of declarative policies expressed using formal statements that enable the Non-RT RIC function in the SMO to guide the Near-RT RIC function, and hence the RAN, towards better fulfilment of the RAN intent.

A1 enrichment information: Information utilized by Near-RT RIC that is collected or derived at SMO/Non-RT RIC either from non-network data sources or from network functions themselves.

E2: Interface connecting the Near-RT RIC and one or more O-CU-CPs, one or more O-CU-UPs, and one or more ODUs.

E2 Node: A logical node terminating E2 interface. In the present document, O-RAN nodes terminating E2 interface are:

- for NR access: O-CU-CP, O-CU-UP, O-DU or any combination.   
- for E-UTRA access: O-eNB.

FCAPS: Fault, Configuration, Accounting, Performance, Security.

Near-RT RIC: O-RAN Near-Real-Time RAN Intelligent Controller: A logical function that enables near-real-time control and optimization of RAN elements and resources via fine-grained data collection and actions over E2 interface.

Non-RT RIC: O-RAN Non-Real-Time RAN Intelligent Controller: A logical function that enables non-real-time control and optimization of RAN elements and resources, AI/ML workflow including model training and updates, and policybased guidance of applications/features in Near-RT RIC.

NMS: A Network Management System.

Network Service: Composition of network function(s) and/or network service(s), as specified in ETSI GS NFV 003 [11].

Network Slice: A network slice is a set of run-time network functions, and resources to run these network functions, forming a complete instantiated logical network to meet certain network characteristics required by the service instance(s). See reference NGMN 5G P1 Description of a Network Slice [i.11].

Network Slice Instance (NSI): A Managed Object Instance (MOI) of NetworkSlice IOC as specified in 3GPP TS 28.530 [23].

NetworkSliceSubnet Instance (NSSI): A Managed Object Instance (MOI) of NetworkSliceSubnet IOC as specified in 3GPP TS 28.530 [23].

O-CU-CP: O-RAN Central Unit – Control Plane: A logical node hosting the RRC and the control plane part of the PDCP protocol.

O-CU-UP: O-RAN Central Unit – User Plane: A logical node hosting the user plane part of the PDCP protocol and the SDAP protocol.

O-DU: O-RAN Distributed Unit: A logical node hosting RLC/MAC/High-PHY layers based on a lower layer functional split.

O-RU: O-RAN Radio Unit: A logical node hosting Low-PHY layer and RF processing based on a lower layer functional split.

O1: Interface between the Service Management and Orchestration framework and O-RAN managed elements

O2: Interface between the Service Management and Orchestration framework and the O-Cloud

RAN: Generally referred as Radio Access Network. In terms of this document, any component below Near-RT RIC per O-RAN architecture, including O-CU-CP/O-CU-UP/O-DU/O-RU.

Resource isolation: Regime of resource management when a resource used by one network slice instance cannot be shared with another network slice instance. See 3GPP TR 28.801 [i.3].

Single Network Slice Selection Assistance Information (S-NSSAI): An S-NSSAI is comprised of an SST (Slice/Service type) and an optional SD (Slice Differentiator) field (3GPP TS 28.541 [7], clause 4.3.37).

# 3.2 Symbols

Void

# 3.3 Abbreviations

For the purposes of the present document, the abbreviations [given in [i.1] and the following] apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in [i.1].

Distinguished Name

eNB eNodeB (applies to LTE)   
gNB gNodeB (applies to NR)   
KPI Key Performance Indicator   
KQI Key Quality Indicator   
Near-RT RIC O-RAN Near-Real-Time RIC   
NFMF Network Function Management Function   
Non-RT RIC O-RAN Non-Real-Time RIC   
NS Network Service   
NSMF Network Slice Management Function   
NSSMF Network Slice Subnet Management Function   
O-DU O-RAN Distributed Unit   
O-RU O-RAN Radio Unit   
PNF Physical Network Function   
PRB Physical Resource Block   
RIC O-RAN RAN Intelligent Controller   
RRM Radio Resource Management   
SD Slice Differentiator   
SDO Standards Developing Organizations (For ex: 3GPP, ETSI, ONAP, O-RAN)   
SMO Service and Management Orchestration   
SST Slice/Service Type   
VNF Virtual Network Function

# 4 Slicing overview

Network slicing is expected to play a critical role in 5G networks because of various use cases and services 5G will support. It allows a network operator to provide services tailored to customers’ requirements. Network slice is defined as a logical network with a bundle of specified network services over a common network infrastructure. A single physical network is sliced into multiple virtual networks that may support different service types over a single RAN. 3GPP has standardized 6 different service types: eMBB, URLLC, MioT, V2X, HMTC, and HDLCC as specified in 3GPP TS 23.501 [2].

3GPP defined 5G architecture and procedures containing network slicing and related concepts in Release 15. Furthermore, management and orchestration of 5G networks featuring slicing was defined in the 3GPP specifications. Other standard groups e.g. GSMA, ETSI NFV-MANO, ETSI ZSM and ONAP focus on the different aspects of network slicing. Further information regarding network slicing and other SDO’s contributions was discussed in the Study on O-RAN Slicing Technical Report [i.4].

An example RAN slicing deployment of O-RAN network functions based on the select initial deployment option, option B as described in [i.15], is shown in figure 4-1, with some of the network functions shared between O-RAN slice subnets (such as O-CU-CP, O-DU, O-RU) and some network functions dedicated to a particular O-RAN slice subnet (such as OCU-UP).

![](images/bf6e7eb6360930391552f77fee1db7acd90212b87795bd23bc342bd4e6e0281d.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4-1: Example O-RAN slicing deployment

# 5 High-level O-RAN slicing use cases

# 5.1 O-RAN slicing use cases

This clause contains high-level O-RAN slicing use cases that O-RAN is expected to support. Slicing requirements are derived from the specified use cases.

# 5.2 O-RAN slice subnet management and provisioning use cases

Network slicing is conceived to be an end-to-end feature that includes the core network, transport network, and the RAN. Although 3GPP has started defining network slicing support with Release 15, slicing in O-RAN needs to be further addressed in line with 3GPP to achieve deployable network slicing in an open RAN environment.

Management aspects of network slicing such as Network Slice Instances (NSI) and Network Slice Subnet Instances (NSSI) are specified in 3GPP TS 28.531 [4]. While NSI refers to an end-to-end network slice, NSSI refers to a part of an end-to-end network slice as a RAN slice subnet. The provisioning of network slicing includes the four phases which are preparation, commissioning, operation, and decommissioning. The NSI/NSSI provisioning operations shall include:

Create an NSI/NSSI;   
- Activate an NSI/NSSI;   
- De-active an NSI/NSSI;   
- Modify an NSI/NSSI;   
- Terminate an NSI/NSSI.

Please refer to 3GPP TS 28.531 [4], clause 4.1 for further details of NSI and NSSI lifecycle management and provisioning.

The following clauses define the use cases and procedures necessary for O-RAN slice subnet management that is in-line with 3GPP slice management framework. For this purpose, use cases such as slice subnet creation, activation, modification, deactivation, termination, configuration, and feasibility check are utilized by O-RAN architecture.

# 5.2.1 O-RAN slice subnet instance creation

The context of the O-RAN slice subnet instance creation use case is captured in table 5.2.1-1.

Table 5.2.1-1: O-RAN slice subnet instance creation use case   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Creation of a new O-RAN network slice subnet instance (O-NSSI) or use anexisting O-NSSI to satisfy the O-RAN slice subnet related requirements (3GPPTS 28.531 [4], clause 5.1.2).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">NSSMS_C, such as NSMF, who acts as the network slice subnet managementservice consumer. NSSMS_P, such as NSsMF, who acts as the network slice subnet managementservice provider.NFMS_P, such as SMO OAM functions or NFMF, who acts as the networkfunction management service provider.O-Cloud M&amp;O, who acts as the O-Cloud management and orchestrationprovider within SMO.Non-RT RICO-RAN Network Functions: NFs such as Near-RT RIC, O-CU-CP, O-CU-UP, O-DU and O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">NSSMS_P has the knowledge of O-Cloud M&amp;O to manage the lifecycle of VNFsand interconnection between the VNFs and PNFs.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">VNF packages for virtualized O-RAN network functions to be included in the O-RAN slice subnet instance have been already on-boarded.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">NSSMS_P receives request for a network slice subnet instance. The requestcontains network slice subnet related requirements.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">NSSMS_P checks the feasibility of the request, based on the received networkslice subnet related requirements.</td><td colspan="1" rowspan="1">O-RAN slicesubnet feasibilitycheck</td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">NSSMS_P decides to create a new O-NSSI or use an existing O-NSSI.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">If an existing O-NSSI is decided to be used, NSSMS_P should triggermodification of the existing O-NSsI to satisfy the network slice subnet relatedrequirements.Go to “Step 11".Otherwise, NSSMS_P triggers creation of a new O-NSSl, continue with Step 4</td><td colspan="1" rowspan="1">O-RAN slicesubnet instancemodification usecase</td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">NSSMS_P derives the requirements for the constituent O-NSSI(s).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (O)</td><td colspan="1" rowspan="1"> If the required O-NSSI contains constituent O-NSSI(s) managed by otherNSSMs_P(s), NSSMS_P may trigger creation of respective constituent O- NSSI(s) through other NssMS_P(s) which manages the constituent O-NSSI(s). In that case, NSSMS_P receives the constituent O-NSSl information from theother NSsMS_P(s) and associates the constituent O-NSSI(s) with the requiredO-NSSI.</td><td colspan="1" rowspan="1">(O-RAN) slicesubnet instancecreation use case(to createconstituent(O-)NSSI(s)managed by otherNSSMS_P(s))</td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">NSSMS_P determines the service-related requirements and triggers a servicerequest to O-Cloud M&amp;O for instantiation of virtual O-RAN network functionsand virtual links within the determined O-Cloud(s).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Based on the service request, O-Cloud M&amp;O performs corresponding NFinstantiation procedures and virtual link establishment.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7 (M)</td><td colspan="1" rowspan="1">NSSMS_P associates the service response received from O-Cloud M&amp;O withthe corresponding O-NSSI.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8 (M)</td><td colspan="1" rowspan="1">NSSMS_P uses (O-RAN) NF provisioning service exposed by NFMS_P toconfigure (O-)NSSI constituents.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 9 (M)</td><td colspan="1" rowspan="1">NSSMS_P configures the O-NSSI MOI with each constituent (O-)NSSI MOIidentifier.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 10 (M)</td><td colspan="1" rowspan="1">NSSMS_P triggers O-RAN TN manager coordination procedure to establishnecessary links such as for A1, E2, and midhaul and fronthaul connectivity.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 11 (M)</td><td colspan="1" rowspan="1">NSSMS_P notifies Non-RT RIC with network slice subnet requirements andrespective O-NSSl information.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 12 (M)</td><td colspan="1" rowspan="1">NSSMS_P notifies NSSMS_C with the resulting status of this process andrelevant O-NSSI information.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">O-RAN O-NSSI and relevant O-RAN NFs are created, and Non-RT RIC isconfigured with slice requirements and O-NSsl information.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">One of the steps identified above fails.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">O-NSsl is ready to satisfy the network slice subnet related requirements.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Traceability</td><td colspan="1" rowspan="1">REQ-SL-FUN14, REQ-SL-FUN20 - REQ-SL-FUN27</td><td colspan="1" rowspan="1"></td></tr></table>

# 5.2.2 O-RAN slice subnet instance activation

The context of the O-RAN slice subnet instance activation use case is captured in table 5.2.2-1.

Table 5.2.2-1: O-RAN slice subnet instance activation use case   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Activation of an O-RAN network slice subnet instance (O-NSSI) (3GPP TS28.531 [4], clause 5.1.10).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">NSSMS_C, such as NSMF, who acts as the network slice subnet managementservice consumer. NSSMS_P, such as NSSMF, who acts as the network slice subnet managementservice provider.NFMS_P, such as SMO OAM functions or NFMF, who acts as the networkfunction management service provider.O-RAN network functions: NFs such as Near-RT RIC, O-CU-CP, O-CU-UP, O-DU and O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">NSSMS_P is providing services to authorized consumers.</td><td colspan="1" rowspan="1"></td></tr><tr><td></td><td>An O-NSSI has already been created and it is inactive. As an example, the O-NSSI may contain inactive O-RAN NFs:- Near-RT RIC is installed and active</td><td></td></tr><tr><td>Pre-conditions</td><td>- O-CU-CP installed (i.e. operationalstate = enabled), but not yet activated (i.e. administrativestate = locked). - O-CU-UP installed (i.e. operationalstate = enabled), but not yet</td><td></td></tr><tr><td></td><td>activated (i.e. administrativestate = locked). - O-DU installed (i.e. operational state = enabled), but not yet activated (i.e. administrativeState = locked) (3GPP TS 28.541 [7], figure</td><td></td></tr><tr><td>B.2.1).</td><td>- O-RU physically installed (i.e. operational state = enabled), but not</td><td></td></tr><tr><td></td><td>yet activated (i.e. administrativestate = locked). See NOTE 1.</td><td></td></tr><tr><td>Begins when Step 1 (M)</td><td>NSSMS_P decides to activate the O-NSSI based on the received network slice subnet related request from its authorized consumer NSSMS_C.</td><td></td></tr><tr><td></td><td>NSSMS_P receives a request from NSSMS_C to activate the O-NSSI (via O- NSSI provisioning service with operation modifyMOIAttributes (3GPP TS 28.531 [4], table 6.2-1) to change administrativestate of the O-NSsI to unlocked.)</td><td></td></tr><tr><td rowspan="5">Step 2 (M)</td><td>NSSMS_P identifies the inactive constituents within the O-NSSI and decides to activate those constituents which can be NFs or O-NSSI. As an example， NSSMS_P activates the following inactive O-RAN NF</td><td></td></tr><tr><td>constituents:</td><td colspan="1"></td></tr><tr><td>- the O-CU-CP NF constituent, and invokes NF provisioning service with operation modifyMOIAttributes (3GPP TS 28.531 [4]， table 6.3-1） to request NFMS_P to activate the O-CU-CP by changing the administrativeState of the O-CU-CP to unlocked.</td><td colspan="1"></td></tr><tr><td>See NOTE 2.</td><td colspan="1"></td></tr><tr><td>- the O-CU-UP NF constituent, and invokes NF provisioning service with operation modifyMOIAttributes (3GPP TS 28.531 [4], table 6.3-1) to request NFMS_P to activate the O-CU-UP by changing the administrativeState of the O-CU-UP to unlocked. See NOTE 3, NOTE 4.</td><td colspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">- the O-RU NF constituent, and invokes NF provisioning service withoperation modifyMOIAttributes (3GPP TS 28.531 [4], table 6.3-1) torequest NFMS_P to activate the O-RU by changing theadministrativeState of the O-RU to unlocked.See NOTE 7.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">NSSMS_P receives notifications indicating that all inactive O-NSSI constituentsare activated. (NSSMS_P is notified by respective NFMS_P(s) through NFprovisioning      data      report      service      with      notificationnotifyMOlAttribute ValueChanges (3GPP TS 28.531 [4], table 6.3-1) that the O-CU-CP, O-CU-UP, O-DU and O-RU have been activated.)</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (M)</td><td colspan="1" rowspan="1">NSSMS_P changes admini strativeState of the O-NSSI to unlocked, andinvokes O-NSSI provisioningg data report service with notificationnotifyMOIAttributeValueChanges (3GPP TS 28.531 [4], table 6.2-1) to notifyNSSMS_C that the O-NSSI has been activated.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">O-RAN O-NSSI is activated.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">One of the steps identified above fails.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">O-NSSl is in operation.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Traceability</td><td colspan="1" rowspan="1">REQ-SL-FUN25, REQ-SL-FUN28</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="3" rowspan="1">NOTE 1: The O-CU-CP, O-CU-UP, O-DU and O-RU are not shared by other O-NSSl, since they are not yet activated.Near-RT RIC has already been activated for other services.NOTE 2: O-CU-CP triggers establishment of the E2 interface connection with Near-RT RIC.NOTE 3: O-CU-UP triggers establishment of the E2 interface connection with Near-RT RIC.NOTE 4: E1 interface connection will be established between O-CU-CP and O-CU-UP.NOTE 5: O-DU triggers establishment of the F1 interface connection with O-CU-CP and O-CU-UP, (3GPP TS 28.541[7], Annex A.1). NOTE 6: O-DU triggers establishment of the E2 interface connection with Near-RT RIC.NOTE 7: O-RU triggers establishment of the M plane interface connection with O-DU (O-RAN.WG1.O1-Interface.0-v04.00 [13]).</td></tr></table>

# 5.2.3 O-RAN slice subnet instance modification

The context of the O-RAN slice subnet instance modification use case is captured in table 5.2.3-1.

Table 5.2.3-1: O-RAN slice subnet instance modification use case   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Modification of an existing O-NSSI to satisfy O-RAN slice subnet relatedrequirements (3GPP TS 28.531 [4], clause 5.1.9).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">NSSMS_C, such as NSMF, who acts as the network slice subnet managementservice consumer. NSSMS_P, such as NSSMF, who acts as the network slice subnet managementservice provider.NFMS_P, such as SMO OAM functions or NFMF, who acts as the networkfunction management service provider.O-Cloud M&amp;O, who acts as the O-Cloud management and orchestrationprovider within SMO.Non-RT RICO-RAN network functions: NFs such as Near-RT RIC, O-CU-CP, O-CU-UP, O-DU and O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">NSSMS_P has the knowledge of O-Cloud M&amp;O to manage the lifecycle of VNFsand interconnection between the VNFs and PNFs.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">VNF packages for virtualized O-RAN network functions to be included in the O-RAN slice subnet instance have been already on-boarded.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">NSSMS_P receives request for a modification of an existing O-NSSI. Therequest contains new network slice subnet related requirements.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">NSSMS_P checks the feasibiity of the request, based on the received networkslice subnet related modification requirements. If the modification requirementscan be satisfied, go to step 2, else go to step 8.</td><td colspan="1" rowspan="1">O-RAN slicesubnetfeasibility check</td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">NSSMS_P decomposes the O-NSSI modification request into modificationrequests for each (O-)NSSI constituent.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (0)</td><td colspan="1" rowspan="1">If the required O-NSSI contains constituent (O-)NSSI(s) managed by otherNSSMs_P(s), NSsMS_P may trigger modification of respective constituent(O-)NSSI(s) through other NssMS_P(s) which manages the constituent(O-)NSSI(s).In that case, NSSMS_P receives the constituent (O-)NSSl information from theother NSSMS_P(s) and associates the constituent (O-)NSSI(s) with therequired O-NsSI.</td><td colspan="1" rowspan="1">(O-RAN) slicesubnet instancemodification usecase (to modifyconstituent(O-)NSSI(s)managed  byotherNSSMS_P(s))</td></tr><tr><td colspan="1" rowspan="1">Step 4 (0)</td><td colspan="1" rowspan="1">If the O-NSSI contains virtualized part(s), NSSMS_P triggers a servicemodification request to O-Cloud M&amp;O for scaling, updating, instantiation etc. ofvirtual O-RAN network functions and virtual links within the determined O-Cloud(s).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (0)</td><td colspan="1" rowspan="1">If the O-NSSI consists of NF instances, NSSMS_P uses NF provisioning serviceexposed by NFMS_P to (re-)configure (O-)NSSI constituents.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (0)</td><td colspan="1" rowspan="1">If the O-NSSI contains TN part, NSSMS_P triggers O-RAN TN managercoordination procedure to establish/modify necessary links such as for A1, E2,midhaul and fronthaul connectivity.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 7 (M)</td><td colspan="1" rowspan="1">NSSMS_P notifies Non-RT RIC with the updated network slice subnetrequirements and respective O-NSSl information.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 8 (M)</td><td colspan="1" rowspan="1">NSSMS_P notifies NSSMS_C with the resulting status of this process andrelevant O-NSSI information.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">O-RAN O-NSSI and relevant O-RAN NFs are modified, and Non-RT RIC isconfigured with modified slice requirements and O-NSSl information.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">One of the steps identified above fails.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">O-NSSI is ready to satisfy the updated network slice subnet relatedrequirements.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Traceability</td><td colspan="1" rowspan="1">REQ-SL-FUN24 - REQ-SL-FUN27, REQ-SL-FUN29, REQ-SL-FUN30</td><td colspan="1" rowspan="1"></td></tr></table>

# 5.2.4 O-RAN slice subnet instance deactivation

The context of the O-RAN slice subnet instance deactivation use case is captured in table 5.2.4-1.

Table 5.2.4-1: O-RAN slice subnet instance deactivation use case   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Deactivation of an O-RAN network slice subnet instance (O-NSSI) (3GPP TS28.531 [4], clause 5.1.11).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">NSSMS_C, such as NSMF, who acts as the network slice subnet managementservice consumer. NSSMS_P, such as NSSMF, who acts as the network slice subnet managementservice provider.NFMS_P, such as SMO OAM functions or NFMF, who acts as the networkfunction management service provider.O-RAN network functions: NFs such as Near-RT RIC, O-CU-CP, O-CU-UP, O-DU and O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">NSSMS_P is providing services to authorized consumers.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">An O-NSSI has already and it is in active state.As an example, the existing O-NSSlincludes active O-CU-CP, O-CU-UP, O-DUand O-RU O-RAN NFs, where the administrativeState is unlocked (3GPPTS 28.541 [7], figure B.2.1). See NOTE 1.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">NSSMS_C decides to deactivate the O-NSSI based on the received networkslice subnet related request from its authorized consumer NSSMS_C.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">NSSMS_P receives a request from NSSMS_C to deactivate the O-NSSI (via O-NSSI provisioning service with operation modifyMOlAttributes (3GPP TS28.531 [4], table 6.2-1) to request NSSMS_P to deactivate the O-NSSI that isto change administrativeState of the O-NSSI to locked).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">NSSMS_P identifies active constituents (e.g. O-NSSI, NF) of the O-NSSI anddecides to deactivate those constituents.</td><td colspan="1" rowspan="1"></td></tr><tr><td>RAN NFs:</td><td>As an example, NSSMS_P finds that the O-NSSI contains active non-shared O- - the O-CU-CP NF constituent, and invokes NF provisioning service with operation modifyMOIAttributes (3GPP TS 28.531 [4], table 6.3-1) to</td><td rowspan="3"></td></tr><tr><td>See NOTE 2, NOTE 3.</td><td colspan="1">request NFMS_P to deactivate the O-CU-CP by changing the administrativeState of the O-CU-CP to locked.</td></tr><tr><td>See NOTE 4.</td><td colspan="1">- the O-CU-UP NF constituent, and invokes NF provisioning service with operation modifyMOIAttributes (3GPP TS 28.531 [4], table 6.3-1) to request NFMS_P to deactivate the O-CU-UP by changing the administrativestate of the O-CU-UP to locked.</td></tr><tr><td>See NOTE 5, NOTE 6.</td><td colspan="1">- the O-DU NF constituent, and invokes NF provisioning service with operation modifyMOIAttributes (3GPP TS 28.531 [4],， table 6.3-1) to request NFMS_P to deactivate the O-DU by changing the administrativestate of the O-DU to locked.</td></tr><tr><td></td><td colspan="1">- the O-RU constituent, and invokes NF provisioning service with operation modifyMOIAttributes (3GPP TS 28.531 [4], table 6.3-1) to request NFMS_P to deactivate the O-RU by changing the administrativeState of the O-RU to locked.</td></tr><tr><td>See NOTE 7. constituents are deactivated.</td><td colspan="1">NSSMS_P receives notifications indicating that all active non-shared O-NSSI</td></tr><tr><td>Step 3 (M) have been deactivated.)</td><td colspan="1">(NSSMS_P is notified by respective NFMS_P(s) which invoke NF provisioning data report service with notification notifyMOlAttribute ValueChanges (3GPP TS 28.531 [4], table 6.3-1) to notify that the O-CU-CP, O-CU-UP, O-DU and O-RU</td></tr><tr><td>Step 4 (M)</td><td colspan="1">NSSMs_P changes administrativestate of the O-NSSI to locked, and invokes O-NSSI provisioning data report service with notification</td></tr><tr><td></td><td colspan="1">notifyMOIAttribute ValueChanges (3GPP TS 28.531 [4], table 6.2-1) to notify NSSMs_C that the O-NSSI has been deactivated.</td></tr><tr><td>Ends when O-RAN O-NSSI is deactivated.</td><td colspan="1"></td></tr><tr><td></td><td colspan="1"></td></tr><tr><td></td><td colspan="1"></td></tr><tr><td></td><td colspan="1"></td></tr><tr><td></td><td colspan="1"></td></tr><tr><td></td><td colspan="1"></td></tr><tr><td></td><td colspan="1"></td></tr><tr><td>Exceptions</td><td colspan="1"></td></tr><tr><td>One of the steps identified above fails. Post Conditions O-NSSl is inactive.</td><td colspan="1"></td></tr><tr><td></td><td colspan="1"></td></tr><tr><td></td><td colspan="1"></td></tr><tr><td></td><td colspan="1"></td></tr><tr><td></td><td colspan="1"></td></tr><tr><td></td><td colspan="1"></td></tr><tr><td></td><td colspan="1"></td></tr><tr><td>Traceability REQ-SL-FUN25, REQ-SL-FUN31</td><td colspan="1"></td></tr><tr><td colspan="3">NOTE 2: O-CU-CP triggers termination of the E2 interface connection with Near-RT RIC. NOTE 3: E1 interface connection wil be released between O-CU-CP and O-CU-UP.</td></tr><tr><td colspan="3">NOTE 4: O-CU-UP triggers termination of the E2 interface connection with Near-RT RIC.</td></tr><tr><td colspan="3">NOTE 5: O-DU triggers termination of the F1 interface connection with O-CU-CP and O-CU-UP (3GPP TS 28.541 [7] Annex A.1).</td></tr><tr><td colspan="3">NOTE 6: O-DU triggers termination of the E2 interface connection with Near-RT RIC. NOTE 7: O-RU triggers termination of the M plane interface connection with O-DU (O-RAN.WG1.O1-Interface.0-</td></tr></table>

# 5.2.5 O-RAN slice subnet instance termination

The context of the O-RAN slice subnet instance termination use case is captured in table 5.2.5-1.

Table 5.2.5-1: O-RAN slice subnet instance termination use case   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Termination or disassociation of an existing O-RAN network slice subnetinstance (O-NSSI) (3GPP TS 28.531 [4], clause 5.1.4).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">NSSMS_C, such as NSMF, who acts as the network slice subnet managementservice consumer. NSSMS_P, such as NSSMF, who acts as the network slice subnet managementservice provider.O-Cloud M&amp;O, who acts as the O-Cloud management and orchestrationprovider within SMO.Non-RT RICO-RAN network functions: NFs such as Near-RT RIC, O-CU-CP, O-CU-UP, O-DU and O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">NSSMS_P has the knowledge of O-Cloud M&amp;O to manage the lifecycle of VNFsand interconnection between the VNFs and PNFs.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">O-NSSI exists, and it is in inactive state.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">NSSMS_P receives a request for an O-RAN network slice subnet instance indicating that the O-NSSl is no longer needed. The request contains networkslice subnet identifier.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">NSSMS_P checks whether the O-NSSI is a shared network slice subnetinstance.If the O-NSSI is shared, O-NSSI shall be disassociated via O-NSSI sice subnetinstance modification use case. Go to step 5.</td><td colspan="1" rowspan="1">O-RAN slicesubnet instancemodification usecase</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"> If the O-NSSI is not shared, O-NSSI shall be terminated. Go to step 2.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">If the O-NSsI consists of consttuent O-NSSIs that are not managed directly bythe NSSMS_P, it sends a request to other NSSMS_P(s) indicating that theconstituent O-NSSIs are no longer needed for the O-NSSI.</td><td colspan="1" rowspan="1">O-RAN slicesubnet instancetermination usecase</td></tr><tr><td colspan="1" rowspan="1">Step 3 (0)</td><td colspan="1" rowspan="1">NSSMS_P may trigger a service termination request to O-Cloud M&amp;O forremoval of non-shared virtual O-RAN network functions.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (0)</td><td colspan="1" rowspan="1">If the O-NSSI includes constituent transport links, NSSMS_P may trigger O-RAN TN manager coordination procedure.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 5 (M)</td><td colspan="1" rowspan="1">NSSMS_P notifies Non-RT RIC that the O-NSSI has been terminated.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">NSSMS_P noties NSSMS_C with the resulting status of this process andrelevant O-NSSI information.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">All the steps identified above are successfully completed.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">One of the steps identified above fails.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">O-NSSI has been terminated or disassociated and Non-RT RIC is notified.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Traceability</td><td colspan="1" rowspan="1">REQ-SL-FUN21, REQ-SL-FUN23, REQ-SL-FUN27, REQ-SL-FUN32 - REQ-SL-FUN34</td><td colspan="1" rowspan="1"></td></tr></table>

# 5.2.6 O-RAN slice subnet instance configuration

The context of the O-RAN slice subnet instance configuration use case is captured in table 5.2.6-1.

Table 5.2.6-1: O-RAN slice subnet instance configuration use case   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">Configuration of an O-NSSI (3GPP TS 28.531 [4], clause 5.1.13).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">NSSMS_C, such as NSMF, who acts as the network slice subnet managementservice consumer.NSSMS_P, such as NSSMF, who acts as the network slice subnet managementservice provider.NFMS_P, such as SMO OAM functions or NFMF, who acts as the networkfunction management service provider.O-RAN network functions: NFs such as Near-RT RIC, O-CU-CP, O-CU-UP, O-DU and O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">NSSMS_P is providing services to authorized consumers. NSSMS_P has the knowledge of the respective NSSMS_P(s) and NFMS_P(s)which manages the constituent O-NSSI(s) and NF(s).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">The O-NSSI exists.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">NSSMS_C triggers the (re-)configuration of an O-NSSI and its constituents.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">NSSMS_P receives a request from NSSMS_C with slice subnet(re-)configuration information for (re-)configuration of an O-NSSI.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (M)</td><td colspan="1" rowspan="1">NSSMS_P decomposes the received slice subnet configuration information andprepares CM requests for each constituent if necessary and applicable.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (0)</td><td colspan="1" rowspan="1">NSSMS_P configures the constituent O-NSSI(s) if it is managed directly by theNSSMS_P.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (0)</td><td colspan="1" rowspan="1"> If the O-NSSI contains constituent O-NSSI(s) managed by other NSSMS_P(s),NSSMS_P triggers configuration of respective constituent O-NSSI(s) through NSSMS_P(s) which manages the constituent O-NSSI(s).</td><td colspan="1" rowspan="1">(O-RAN) slicesubnetconfigurationuse case</td></tr><tr><td colspan="1" rowspan="1">Step 5 (0)</td><td colspan="1" rowspan="1">If the required O-NSSI contains constituent O-RAN NF(s) managed by NFMS_P(s), NSSMS_P may trigger configuration requests with correspondingslice subnet configuration information through NFMS_P(s) which manages theconstituent O-RAN NF(s).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 6 (M)</td><td colspan="1" rowspan="1">NSSMS_P sends the configuration result to the NSSMS_C which may be basedon results received from other CM service providers.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">All the steps identified above are successfully completed.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">One of the steps identified above fails.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">The required (re-)configuration is accomplished at the correspondingconstituent(s).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Traceability</td><td colspan="1" rowspan="1">REQ-SL-FUN24, REQ-SL-FUN25</td><td colspan="1" rowspan="1"></td></tr></table>

# 5.2.7 O-RAN slice subnet feasibility check

The context of the O-RAN slice subnet feasibility check is captured in table 5.2.7-1.

Table 5.2.7-1: O-RAN slice subnet feasibility check   

<table><tr><td colspan="1" rowspan="1">Use Case Stage</td><td colspan="1" rowspan="1">Evolution / Specification</td><td colspan="1" rowspan="1">&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td colspan="1" rowspan="1">Goal</td><td colspan="1" rowspan="1">To check the feasibility of provisioning an O-RAN network slice subnet instance(O-NSSI) to determine whether the O-NSSI requirements can be satisfied (e.g.,in terms of resources) (3GPP TS 28.531 [4], clause 5.1.21).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Actors and Roles</td><td colspan="1" rowspan="1">NSSMS_C, such as NSMF, who acts as the network slice subnet managementservice consumer.NSSMS_P, such as NSSMF, who acts as the network slice subnet managementservice provider.NFMS_P, such as SMO OAM functions or NFMF, who acts as the networkfunction management service provider.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">O-Cloud M&amp;O, who acts as the O-Cloud management and orchestrationprovider within SMO.Non-RT RICO-RAN network functions: NFs such as Near-RT RIC, O-CU-CP, O-CU-UP, O-DU and O-RU.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Assumptions</td><td colspan="1" rowspan="1">NSSMS_C has decided to check the feasibility of provisioning an O-NSSI basedon, for example, internal decision or an external service request.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Pre-conditions</td><td colspan="1" rowspan="1">Network slice subnet requirements have been derived or received by networkslice subnet management service consumer NssMS_C.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Begins when</td><td colspan="1" rowspan="1">NSSMS_P receives the request to evaluate the feasibility of an O-NSSIaccording to the network slice subnet requirements.</td><td colspan="1" rowspan="1">O-RAN slicesubnet instancecreation, O-RAN slicesubnet instancemodification</td></tr><tr><td colspan="1" rowspan="1">Step 1 (M)</td><td colspan="1" rowspan="1">NSSMS_P identifies the network slice subnet constituents according to therequirements, e.g., network services to be requested from O-Cloud M&amp;O.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 2 (0)</td><td colspan="1" rowspan="1">For the purpose of checking the feasibility of provisioning an O-NSSl,NSSMS_P may obtain information from the SMO and Non-RT RIC (e.g., loadlevel information, resource usage information from management data analyticsservices).</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 3 (M)</td><td colspan="1" rowspan="1">NSSMS_P sends enquiries with reservation requests to O-Cloud M&amp;O todetermine availability of network consttuents, e.g., network services, networkfunctions.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Step 4 (0)</td><td colspan="1" rowspan="1">For the purpose of checking the feasibility of transport network links, NSSMS_Pmay obtain information from TN manager.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Ends when</td><td colspan="1" rowspan="1">NSSMS_P provides feasibility check results to NSSMS_C. If provisioning of O-NSSI is feasible, the information about reserved resources may also beprovided.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Exceptions</td><td colspan="1" rowspan="1">One of the mandatory steps fails.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Post Conditions</td><td colspan="1" rowspan="1">NA</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Traceability</td><td colspan="1" rowspan="1">REQ-SL-FUN35 - REQ-SL-FUN37</td><td colspan="1" rowspan="1"></td></tr></table>

# 5.3 O-RAN slicing use cases

# 5.3.1 Use case 1: RAN slice SLA assurance

In the 5G era, network slicing is a prominent feature which provides end-to-end connectivity and data processing tailored to specific business requirements. These requirements include customizable network capabilities such as the support of very high data rates, traffic densities, service availability and very low latency. According to 5G standardization efforts, the 5G system can support the needs of the business through the specification of several service needs such as data rate, traffic capacity, user density, latency, reliability, and availability. These capabilities are always provided based on a Service

Level Agreement (SLA) between the mobile operator and the business customer, which brought up interest for mechanisms to ensure slice SLAs and prevent its possible violations. O-RAN’s open interfaces and AI/ML based architecture will enable such challenging mechanisms to be implemented and help pave the way for operators to realize the opportunities of network slicing in an efficient manner.

RAN slice SLA assurance scenario involves Non-RT RIC, Near-RT RIC, E2 Nodes and SMO interaction. The scenario starts with the retrieval of RAN specific slice SLA/requirements (possibly within SMO or from NSSMF depending on operator deployment options). Based on slice specific performance measurements from E2 Nodes, Non-RT RIC and NearRT RIC can fine-tune RAN behavior aligned with O-RAN architectural roles to assure RAN slice SLAs. Non-RT RIC monitors long-term trends and patterns for O-RAN slice subnets’ performance and employs AI/ML methods to perform corrective actions through SMO (e.g. reconfiguration via O1) or via creation of A1 policies. Non-RT RIC can also construct/train relevant AI/ML models that will be deployed at Near-RT RIC. A1 policies possibly include scope identifiers (e.g. S-NSSAI) and statements such as KPI targets. On the other hand, Near-RT RIC enables optimized RAN actions through execution of deployed AI/ML models in near-real-time by considering both O1 configuration (e.g. static RRM policies) and received A1 policies, as well as received slice specific E2 measurements.

An overview of RAN slice SLA assurance use case is given in figure 5.3.1-1.

![](images/2ebb234641f0ee6616534685d20311d260894077fccf0d16588f8bbddfb6520d.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.3.1-1: RAN slice SLA assurance use case overview

The more detailed functions provided by the entities for RAN slice SLA assurance are listed as below:

1) SMO:

a) Provides information about slice topology and SLA associated with the slice to the Non-RT RIC

2) Non-RT RIC:

a) Retrieve RAN slice SLA target from respective entities such as SMO, NSSMF   
b) Long term monitoring of O-RAN slice subnet performance measurements   
c) Training of potential ML models that will be deployed in Near-RT RIC for optimized slice assurance   
d) Support deployment and update of AI/ML models into Near-RT RIC   
e) Send A1 policies and enrichment information to Near-RT RIC to drive slice assurance   
f) Send O1 reconfiguration requests to SMO for slow-loop slice assurance

3) Near-RT RIC:

a) Near-real-time monitoring of slice specific RAN performance measurements   
b) Support deployment and execution of the AI/ML models from Non-RT RIC   
c) Support interpretation and execution of policies from Non-RT RIC   
d) Perform optimized RAN (E2) actions to achieve O-RAN slice subnet requirements based on O1 configuration, A1 policy, and E2 reports

4) E2 Nodes (O-CU-CP, O-CU-UP, O-DU):

a) Support slice assurance actions such as slice-aware resource allocation, prioritization, etc. b) Support slice specific performance measurements through O1   
c) Support slice specific performance reports through E2

# 5.3.2 Use case 2: Multi-vendor slices

This use case enables multiple slices with functions provided by multi-vendors, such as slice #1, composed of DU(s) and CU(s), provided by vendor B and slice #2, composed of DU(s) and CU(s), provided by vendor C (see figure 5.3.2-1).

![](images/597e2f3f469c2d3d74c3c7bd80cac18f25b6d7644b3af3912db6854926a8aad2.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.3.2-1: Multi-vendor slices

When providing multiple slices, it is assumed that suitable virtualized O-DU (vO-DU)/scheduler and virtualized O-CUCP and virtualized O-CU-UP treat each slice respectively. A vendor who provides vO-DU and vO-CU-UP function may include a customized scheduler for a certain service, with advantages for optimized functionality. With accomplishment of multi-vendor circumstances, following benefits may be expected:

1) More flexible and time to market deployment

Operators can maximize options to choose suitable vO-DU/scheduler and vO-CU-CP and vO-CU-UP to offer various slices. For example, some vendors may have an optimized scheduler for eMBB services and the other may have an optimized scheduler for URLLC services. Or, vendor A can provide vO-DU/scheduler and vO-CU-CP and vO-CU-UP suitable for URLLC earlier than vendor B, therefore operators can choose vO-DU and vO-CU-CP and vO-CU-UP functions from vendor A to meet their service requirements.

Also, when an operator wants to add a new service/slice, new functions from a new vendor can be introduced with less consideration for existing vendors if multi-vendor circumstance was realized. This can help expand vendor’s business opportunities rapidly.

2) Flexible deployment when sharing RAN equipment among operators

When operators want to share RAN equipment and resources, RAN vendors and their placement of each RAN functions can be different. If multi-vendor circumstance was introduced, then it can relax restrictions among operators to share RAN equipment and resources. This can help expanded opportunities for reaching agreements of RAN sharing among operators. With expansion of RAN sharing, operators CAPEX and OPEX can be optimized, helping with additional investment opportunities.

3) Reducing supply chain risk

If an existing vendor providing a certain pair of vO-DU and vO-CU-CP and vO-CU-UP functions withdraws of the market due to business reasons, operators can deploy new vO-DU and vO-CU-CP and vO-CU-UP functions alternatively from other vendors under this multi-vendor circumstance. This can reduce the risk for operators’ business continuity.

To realise multi-vendor slices, some coordination between vO-DU/vO-CU-CP/v-O-CU-UPs is required since radio resources shall be assigned properly and without any conflicts. Depending on different service goals and the potential impact on O-RAN architecture, a required coordination scheme needs to be determined. The possible cases are:

1) Loose coordination through O1/E2/A1 interface (case 1 shown in figure 5.3.2-2)   
2) Moderate coordination through X2/F1 interface (case 2 shown in figure 5.3.2-2)   
3) Tight coordination through a new interface between vO-DUs (case 3 shown in figure 5.3.2-2)

![](images/4ee3da64187deb64a142d0c95fd41ab8d796dd7564882652a4ffa3753270e902.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.3.2-2: Multi-vendor slices coordination scheme options

In case 1, a resource allocation between slices or vO-DU/vO-CU-CP/vO-CU-UPs shall be provisioned through O1/A1/E2 interface, and each pair of vO-DU and vO-CU will allocate radio resources to each customer within radio resources allocated by Near-RT RIC and/or Non-RT RIC.

In case 2, a resource allocation may be negotiated between slices or vO-DU/vO-CU-CP/vO-CU-UPs through X2 and F1 after provisioned through O1/E2/A1 interface. Negotiation period will be several seconds due to periodicity of X2 and F1 message exchange between vO-CU-CP(s).

If a more adaptive radio resource allocation is needed (case 3), more frequent negotiation would be required. This may potentially be achieved via an interface or API extension between vO-DU(s).

# 5.3.3 Use case 3: O-NSSI resource allocation optimization

5G networks are becoming increasingly complex with the densification of millimeter wave small cells, and various new services, such as eMBB (enhanced Mobile Broadband), URLLC (Ultra Reliable Low Latency Communications), and mMTC (massive Machine Type Communications) that are characterized by high speed high data volume, low speed ultralow latency, and infrequent transmitting low data volume from huge number of emerging smart devices, respectively. It is a challenging task for 5G networks to allocate resources dynamically and efficiently among multiple network nodes to support various services. However, eMBB, URLLC, and mMTC services in 5G are typically realized as NSI(s) (Network Slice instance(s)). Therefore, the resources allocated to O-NSSI (O-RAN Network Slice Subnet Instance) to support the O-RAN nodes can be optimized according to the service requirements.

As the new 5G services have different characteristics, the network traffic tends to be sporadic, where there can be different usage pattern in terms of time, location, UE distribution, and types of applications. For example, most IoT sensor applications may run during off-peak hours or weekends. Special events, such as sport games, concerts, can cause traffic demand to shoot up at certain times and locations. Therefore, O-NSSI resource allocation optimization function trains the AI/ML model, based on the huge volume of performance data collected over days, weeks, months from O-RAN nodes. It then uses the AI/ML model to predict the traffic demand patterns of 5G networks in different times and locations for each network slice subnet, and automatically re-allocates the network resources ahead of the network issues surfaced.

The resource quota policies associated with RAN NFs (E2 Nodes) included in the respective O-NSSIs enable 5G network providers to optimize or prioritize the utilization of the RAN resources across slices and supports the flexibility to share resources optimally across critical service slices during resource surplus or scarcity. For example, an O-NSSI allocated for premium service can receive a major share of the resources compared to a slice allocated for a standard/best-effort service. Another such example is the scenario of additional resource allocation for emergency services. An important consideration here is that the O-NSSI resource quota policies focuses on maximization of resource utilization across the O-NSSIs. The resource quota policies can be used as a constraint for resource allocation that defines the range of resources that can be allocated per slice. One use case for applying such a constraint is the analysis and decision based on history of resource allocation failure that may be reflected in the RAN node measurements. Here resource quota policy can be provisioned to control the minimum, maximum and dedicated resources that need to be allocated based on the historical pattern. The O-NSSI resource allocation optimization on the Non-RT RIC is shown in figure 5.3.3-1 shows, and may consist of the following steps:

1. Monitoring: monitor the radio network(s) by collecting data via the O1 interface, including the following performance measurements that are measured per S-NSSAI (3GPP TS 28.552 [8] shall apply):

DL PRB used for data traffic (3GPP TS 28.552 [8], clause 5.1.1.2.5 shall apply) UL PRB used for data traffic (3GPP TS 28.552 [8], clause 5.1.1.2.7 shall apply) Average DL UE throughput in gNB (3GPP TS 28.552 [8], clause 5.1.1.3.1 shall apply) Average UL UE throughput in gNB (3GPP TS 28.552 [8], clause 5.1.1.3.3 shall apply) Number of PDU sessions requested to setup (3GPP TS 28.552 [8], clause 5.1.1.5.1 shall apply) Number of PDU sessions successfully setup (3GPP TS 28.552 [8], clause 5.1.1.5.2 shall apply) Distribution of DL UE throughput in gNB (3GPP TS 28.552 [8], clause 5.1.1.3.2 shall apply) Distribution of UL UE throughput in gNB (3GPP TS 28.552 [8], clause 5.1.1.3.4 shall apply) Number of DRBs successfully setup (3GPP TS 28.552 [8], clause 5.1.1.10.2 shall apply)

2. Analysis & Decision: consisting of the following steps:

o Utilize AI/ML models to analyze the measurements and predict the future traffic demand, including the RRMPolicyRatio IOC limits, for each O-NSSI for a given time and location.   
o Determine the actions needed to add or reduce the resources (e.g. capacity, VNF resources, slice subnet attributes (3GPP TS 28.541 [7] shall apply), etc.) for the RAN NFs (E2 Nodes) included in the respective O-NSSI at the given time, and location.

3. Execution: execute the following actions to reallocate the O-NSSI resources:

3a. Re-configure the O-NSSI attributes, including RRMPolicyRatio IOCs (3GPP TS 28.541 [7] shall apply) via the OAM functions in SMO which uses O1 interface to configure the E2 Nodes.

3b. Update the cloud resources via the O2 interface

![](images/7b559a22e1ec3235caf1d06ec6030cb58fad20b5b32e634628c13cc009411ece.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.3.3-1: The realization of O-NSSI resource allocation optimization over Non-Real Time RIC

The more detailed functions provided by the entities for O-NSSI resource optimization are listed as follows:

1) SMO:

a) Pre-provision the default O-NSSI resource quota policy as constraint for O-NSSI resource allocation optimization. This information is optionally used by the Non-RT RIC in case the resource quota that needs to be allocated per slice is not specified during the slice creation and for conflict resolution at the time of resource scarcity.

2) Non-RT RIC:

a) Collect the performance measurements related to O-NSSI resource usage from the O-RAN nodes via the O1 interface.   
b) Train the AI/ML model based on the analysis of historical performance measurements, to predict of the traffic demand patterns of O-NSSI at different times and locations.   
c) Determine the time/date and locations (i.e. which O-RAN nodes) to add or reduce the resources (e.g. capacity, VNF resources, slice subnet attributes (3GPP TS 28.541 [7]), RRMPolicyRatio IOC, etc.) for a given O-NSSI based on inference.   
d) Perform the following action(s) to optimize the O-NSSI resource allocation, at the time determined by the model i. Re-configure the O-NSSI attributes via the O1 interface. ii. Update the cloud resources via the O2 interface.

3) E2 Nodes (O-CU-CP, O-CU-UP, O-DU, and O-RU):

a) Support the performance measurement collection with required granularity over O1 interface.   
b) Support the configuration related to the O-NSSI resource allocation update over O1 interface.

# 6

# O-RAN slicing principles and requirements

# 6.1 General principles

This clause contains general O-RAN slicing architecture principles as described below:

• O-RAN slicing architecture and interface specifications shall be consistent with 3GPP architecture and interface specifications to the extent possible   
• O-RAN slicing architecture shall provide standardized management service interfaces for O-RAN slice management services   
• O-RAN slicing architecture shall enable multi-vendor interoperability   
• O-RAN slicing architecture shall support multiple different network operator deployment options   
• O-RAN slicing architecture shall support management of O-RAN slice subnets in multi-operator scenarios

# 6.2 Slicing requirements

# 6.2.1 Functional requirements

Initial set of O-RAN slicing functional requirements based on the use cases defined in the present document is captured in table 6.2.1-1.

Table 6.2.1-1: O-RAN slicing functional requirements   

<table><tr><td colspan="1" rowspan="1">REQ</td><td colspan="1" rowspan="1">Description</td><td colspan="1" rowspan="1">Note</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN1]</td><td colspan="1" rowspan="1">O-RAN slicing architecture and interfaces shall support networkslicing， where an instance of O-RAN network function may beassociated with one or more slices.</td><td colspan="1" rowspan="1">ORAN OAM Specificationv02.00</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN2]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall support diferentiated handing oftraffic for different O-RAN slice subnets.</td><td colspan="1" rowspan="1">3GPP TS 38.300</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN3]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall support resource isolation betweenslices.</td><td colspan="1" rowspan="1">3GPP TS 38.300</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN4]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall enable trafic and services in oneO-RAN slice subnet having no impact on traffic and services in otherO-RAN slice subnets in the same network.</td><td colspan="1" rowspan="1">3GPP TS 22.261</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN5]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall enable mechanisms to avoidshortage of shared resources in one slice breaking the service levelagreement for another slice.</td><td colspan="1" rowspan="1">3GPP TS 38.300</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN6]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall enable defining a priority orderbetween diferent O-RAN slice subnets in case multiple slicescompete for resources on the same RAN.</td><td colspan="1" rowspan="1">3GPP TS 22.261</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN7]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall apply policies at S-NSSAI levelaccording to the SLA required by the network slice.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN8]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall support means by which theoperator can differentiate policy control， functionality andperformance provided in different O-RAN slice subnets.</td><td colspan="1" rowspan="1">3GPP TS 22.261</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN9]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall support QoS differentiation within aslice.</td><td colspan="1" rowspan="1">3GPP TS 38.300</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN10]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall enable slice aware radio resourcemanagement strategies (such as admission control,， congestioncontrol, handover preparation).</td><td colspan="1" rowspan="1">3GPP TS 38.300</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN11]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall allow creation, modification, anddeletion of an O-RAN slice subnet.</td><td colspan="1" rowspan="1">3GPP TS 28.531</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN12]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall support interaction between theSMO frameWork and Non-RT RiC to consume provisioningmanagement services exposed by each O-RAN managed elementto configure O-RAN slice subnets through the O1 interface.</td><td colspan="1" rowspan="1">RAN slice SLA assuranceuse case, O-Nssl resourceallocation optimization usecase</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN13]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall support the interaction between theSMO framework and Non-RT RIC to consume management of slicespecific PM jobs， PM data collection/storage/query/statisticalreports from O-RAN network functions through the O1 interface.</td><td colspan="1" rowspan="1">RAN slice SLA assuranceuse case, O-NSSl resourceallocation optimization usecase</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN14]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall support interaction between theSMO framework and Non-RT RIC to retrieve/notify O-RAN slicesubnet requirements (SLA) along with O-NSSI information.</td><td colspan="1" rowspan="1">RAN slice SLA assuranceuse case, O-RAN slicesubnet instance creationuse case</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN15]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall support provisioning, generation,and monitoring of slice specific RAN performance metrics through01 interface.</td><td colspan="1" rowspan="1">RAN slice SLA assuranceuse case, O-NSSl resourceallocation optimization usecase</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN16]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall support training, deployment, andexecution of Al/ML models for slice SLA assurance and O-NSSIresource allocation optimization.</td><td colspan="1" rowspan="1">RAN slice SLA assuranceuse case, O-NssI resourceallocation optimization usecase</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN17]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall support slice specific policyguidance, enrichment information and policy feedback.</td><td colspan="1" rowspan="1">RAN slice SLA assuranceuse case</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN18]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall support provisioning, generation,and monitoring of slice specific RAN performance data through E2interface.</td><td colspan="1" rowspan="1">RAN slice SLA assuranceuse case</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN19]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall support reconfiguration of slice specific RAN parameters and resources for slice SLA assurance.</td><td colspan="1" rowspan="1">RAN slice SLA assuranceuse case</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN20]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall enable creation of O-RAN networkslice subnet instances as O-RAN network service (NS) instance(s)within O-Cloud(s).</td><td colspan="1" rowspan="1">O-RAN  slice   subnetinstance creation use case</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN21]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall enable association anddisassociation of O-Cloud NS instances with corresponding O-NSSIs.</td><td colspan="1" rowspan="1">O-RAN   slice   subnetinstance creation use case,O-RAN  slice   subnetinstancetermination usecase</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN22]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall enable creation of O-RAN networkslice subnet instances as O-RAN network function (NF) instance(s)within O-Cloud(s).</td><td colspan="1" rowspan="1">O-RAN  slice  subnet instance creation use case</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN23]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall enable association anddisassociation of O-Cloud NF instances with corresponding O-NSSIs.</td><td colspan="1" rowspan="1">O-RAN  slice  subnet instance creation use case,O-RAN   slice  subnet</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">instancetermination usecase</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN24]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall support (re-)configuration of an O-NSSI's constituent network functions through the O1 interface.</td><td colspan="1" rowspan="1">O-RAN   slice   subnetinstance creation use case,O-RAN  slice   subnetmodification use case, O-RAN    slice    subnetconfiguration use case</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN25]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall support (re-)configuration of an O-RAN network slice subnet instance (O-NSSI) attributes.</td><td colspan="1" rowspan="1">O-RAN   slice   subnetinstance    creationactivation / modification /deactivation / configurationuse case</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN26]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall have the capability for theestablishment of required transport network connectivity betweenO-RAN NFs during provisioning of O-RAN network slice subnetinstances.</td><td colspan="1" rowspan="1">O-RAN  slice   subnetinstance creation use case,O-RAN   slice   subnetinstance modification usecase</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN27]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall enable Non-RT RIC to be notifiedwhen an O-NSSI has been created, activated, modified, deactivatedand terminated.</td><td colspan="1" rowspan="1">O-RAN   slice  subnetinstance creation use case,O-RAN   slice   subnetinstance modification usecase, O-RAN slice subnetinstance termination usecase</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN28]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall support the capability to activatethe constituent physical network functions such as O-DU and O-RUwithin an O-NSSI.</td><td colspan="1" rowspan="1">O-RAN   slice   subnetinstance activationusecase</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN29]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall enable modification of O-RANnetwork slice subnet instances through modification (such asscaling, updating, instantiation, etc.) of O-RAN network service (NS) instance(s) within O-Cloud(s).</td><td colspan="1" rowspan="1">O-RAN   slice   subnetinstance modification usecase</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN30]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall enable modification of O-RANnetwork slice subnet instances through modification (such asscaling, updating, instantiation, etc.) of O-RAN network function(NF) instance(s) within O-Cloud(s).</td><td colspan="1" rowspan="1">O-RAN   slice   subnetinstance modification usecase</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN31]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall support the capability to deactivatethe constituent physical network functions such as O-DU and O-RUwithin an O-NSSI.</td><td colspan="1" rowspan="1">O-RAN   slice   subnetinstance deactivation usecase</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN32]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall enable removal of constituent O-RAN network service (NS) instance(s) that were functioning withinO-Cloud(s) and were associated to O-RAN network slice subnetinstance(s).</td><td colspan="1" rowspan="1">O-RAN   slice   subnetinstancetermination usecase</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN33]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall enable removal of constituent O-RAN network function (NF) instance(s) that were functioning withinO-Cloud(s) and were associated to Ó-RAN network slice subnetinstance(s).</td><td colspan="1" rowspan="1">O-RAN  slice   subnetinstancetermination usecase</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN34]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall have the capability for the removalof non-shared transport network connectivity between O-RAN NFsduring termination of O-RAN network slice subnet instances.</td><td colspan="1" rowspan="1">O-RAN   slice   subnetinstancetermination usecase</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN35]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall enable reservation of O-RANnetwork service (NS) instance(s) within O-Cloud(s).</td><td colspan="1" rowspan="1">O-RAN   slice   subnetfeasibility check</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN36]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall enable reservation of O-RANnetwork service (NF) instance(s) within O-Cloud(s).</td><td colspan="1" rowspan="1">O-RAN   slice   subnetfeasibility check</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN37]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall enable retrieval of networkutilization information from the SMO and Non-RT RIC (e.g., loadlevel information, resource usage information from managementdata analytics services).</td><td colspan="1" rowspan="1">O-RAN  slice  subnetfeasibility check</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN38]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall support interaction between theSMO framework and Non-RT RIC to consume O-Cloudmanagement and orchestration services through the O2 interface.</td><td colspan="1" rowspan="1">RAN slice SLA assuranceuse case, O-NSSl resourceallocation optimization usecase</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN39]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall enable provisioning andmanagement of multiple slices on O-RU.</td><td colspan="1" rowspan="1">Multi-vendor slices usecase</td></tr><tr><td colspan="1" rowspan="1">[REQ-SL-FUN40]</td><td colspan="1" rowspan="1">O-RAN slicing architecture shall enable O-RU to route per slice userplane traffic to one or more O-Dus.</td><td colspan="1" rowspan="1">Multi-vendor slices usecase</td></tr></table>

# 6.2.2 Non-functional requirements

Initial set of O-RAN slicing non-functional requirements based on the use cases defined in the present document is captured in table 6.2.2-1.

Table 6.2.2-1: O-RAN slicing non-functional requirements   

<table><tr><td rowspan=1 colspan=1>REQ</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Note</td></tr><tr><td rowspan=1 colspan=1>[REQ-SL-NFUN1]</td><td rowspan=1 colspan=1>O-RAN slicing architecture shall support use of Al/ML to support O-RANslicing use cases.</td><td rowspan=1 colspan=1></td></tr></table>

# O-RAN reference slicing architecture

# 7.1 O-RAN reference slicing architecture

This clause provides O-RAN reference slicing architecture (see figure 7.1-1) along with the high-level roles and responsibilities of O-RAN network functions.

![](images/4c43a9161ac4a7dc5d46c43661c7dcd4bfaf1fad1a9306c48bcbe68f9d94d5d4.jpg)

> **Image Summary:** (Summary not available)
  
Figure 7.1-1: O-RAN reference slicing architecture

O-RAN reference slicing architecture includes slice management functions along with O-RAN architectural components. As O-RAN’s general principle is to be as compliant as possible with 3GPP architecture, these slice management functions are 3GPP-defined NSMF and NSSMF with extensions defined for O-RAN network functions. Various deployment options for the location of NSMF(s) and NSSMF(s) are included in [i.4]. Detailed architectural implementation options for SMOs including NFV-MANO and ONAP are being presented in Appendix A of this document.

# 7.2 Non-RT RIC

The fundamental role of the Non-RT RIC in O-RAN slicing architecture is to gather long term slice related data through interaction with the SMO framework and apply AI/ML based approaches interworking with the Near-RT RIC to provide innovative RAN slicing use cases. For this purpose, Non-RT RIC shall have the knowledge of O-RAN slice subnets and their respective SLA(s) through SMO. In addition, Non-RT RIC may retrieve enrichment information from $3 ^ { \mathrm { r d } }$ party applications and use that information for RAN slice SLA assurance purposes.

In order to construct AI/ML models to be deployed in the Near-RT RIC, Non-RT RIC shall retrieve slice specific performance metrics, configuration parameters and required attributes of the O-RAN slice subnets from the SMO framework. The output of these algorithms may lead non-real-time optimization of the slice specific parameters of NearRT RIC, O-CU-CP, O-CU-UP and O-DU over O1 interface through SMO interaction. Moreover, these performance, configuration and other slice related data are used to generate policy guidance and assist Near-RT RIC over A1 to provide closed loop slice optimization. Applying such slice optimizations in the Near-RT RIC may be used for SLA assurance and prevent SLA violations between the slices as well.

# 7.3 Near-RT RIC

Near-RT RIC enables near-real-time O-RAN slice subnet optimization through execution of slicing-related xApps and communicating necessary parameters to O-CU-CP, O-CU-UP and O-DU through E2 interface. Deployed xApps may utilize either AI/ML based models or non-AI/ML algorithms which may further be guided by A1 policies that are generated by Non-RT RIC.

In order to drive sliced RAN resources properly, Near-RT RIC shall have the knowledge of existing O-RAN slice subnets as well as their SLA requirements. This information will be received through O1 interface during provisioning of O-RAN slice subnets. Therefore, similar to Non-RT RIC, Near-RT RIC will be aware of O-RAN slice subnets through O-RAN specific information models and provisioning procedures.

In O-RAN slicing architecture, configuration of slice resources on E2 nodes can be achieved through slow loop with O1 configuration and through fast loop with E2 configuration. This architecture enables advanced slicing use cases such as RAN slice SLA assurance and further enhances 3GPP slicing capability without misalignment. In the context of the RAN, the SLA assurance parameters sent over the A1 interface assist the Near-RT RIC guide the behavior of the E2 Nodes (OCU-UP, O-CU-CP, O-DU). While Near-RT RIC is capable for fast-loop configuration, slicing related O1 configuration, such as RRM policy information sent to O-CU-CP, O-CU-UP and O-DU configured by the SMO framework will be taken into account. Moreover, slice-specific near-real-time performance data shall be monitored through E2 interface which needs proper PM mechanisms between E2 nodes and Near-RT RIC as well.

# 7.4 O-RAN Central Unit (O-CU-CP, O-CU-UP)

O-CU-CP and O-CU-UP need to support slicing features as defined by 3GPP. Depending on slice requirements, O-CUUP may be shared across slices or a specific instance of O-CU-UP may be instantiated per slice. On top of 3GPP slicing features, O-RAN further enhances slicing through the utilization of E2 interface and the assistance of Near-RT RIC dynamic slice optimizations along with the enhanced O1 interface to support additional slice configuration parameters.

O-CU-CP and O-CU-UP stacks, which are the upper layer protocols of the RAN stack, shall be slice aware and execute slice specific resource allocation and isolation strategies. These stacks are initially configured through O1 interface based on the slice specific requirements and then dynamically updated through E2 interface via Near-RT RIC for various slicing use cases.

Based on the PM requests from SMO and Near-RT RIC, O-CU-CP and O-CU-UP shall generate and send specific PMs through O1 and E2 interfaces respectively, where the PMs may be used for slice performance monitoring and slice SLA assurance purposes.

# 7.5 O-RAN Distributed Unit (O-DU)

O-DU, which runs the lower layer protocols of RAN stack, shall support slice specific resource allocation strategies as well. Based on the initial O1 configuration of PRB allocation levels along with O-CU-CP and O-CU-UP directives over F1 interface and the dynamic guidance received from Near-RT RIC over E2 interface, MAC layer needs to allocate and isolate relevant PRBs to specific slices.

Based on the PM requests from SMO and Near-RT RIC, O-DU shall generate and send specific PMs through O1 and E2 interfaces respectively, where the PMs may be used for slice performance monitoring and slice SLA assurance purposes.

# 7.6 A1 interface

A1, which is the interface between the Non-RT RIC and the Near-RT RIC, supports policy management, ML model management and enrichment information services [i.13]. These three services will be utilized for various slicing use cases, such as slice SLA assurance. Policy management will be used by Non-RT RIC to send slice specific (e.g. S-NSSAI based) policies to guide Near-RT RIC with slice resource allocations and slice specific control activities, as well as to receive slice specific policy feedback for the policies deployed on the Near-RT RIC.

For the use cases that make use of external enrichment data or where Non-RT RIC produces enrichment information, A1 enrichment interface will be used to send slice specific enrichment data to Near-RT RIC.

It should be noted that slice specific A1 policies are not persistent (do not survive the restart of Near-RT RIC) and while they may take precedence over O1 slice specific configurations, they should be aligned and not deviate significantly from O1 configurations.

# 7.7 E2 interface

E2, which is the interface between the Near-RT RIC and the E2 nodes, supports E2 primitives (report, insert, control and policy) to control the services exposed by E2 nodes [i.14]. These primitives will be used by slice specific applications (xApps) to drive E2 nodes’ slice configurations and slice specific behaviour, such as slice based radio resource management, radio resource allocations, MAC scheduling policies and other configuration parameters used by various RAN protocol stacks.

E2 will be used to configure and receive slice specific reports and performance data from E2 nodes. These reports may include 3GPP defined slice specific PMs (such as PRB utilization, average delay, etc. 3GPP TS 28.552 [8]) and new PMs that may be defined by O-RAN to support various slicing use cases.

# 7.8 O1 interface

O1, which is the interface between O-RAN managed elements and the management entity shall be used as specified in O-RAN.WG1.O1-Interface.0-v04.00 [13], to configure slice specific parameters of O-RAN nodes based on the service requirements of the slice. Some of the slice specific information models have been specified in 3GPP TS 28.541 [7], including the RRM policy attributes to provide the ratio of PRBs and the split of these PRBs among slices. To support ORAN slicing use cases and their requirements, 3GPP information models may be extended and additional information models may be defined to capture slice profiles and slice specific configuration parameters, which will be carried over O1 interface as well.

O1 will also be used to configure and gather slice specific performance metrics and slice specific faults from O-RAN nodes.

# 7.9 O2 interface

O2, which is the interface between the SMO and O-Cloud as introduced in [i.15], shall be used for life cycle management of virtual O-RAN network functions. As part of O-RAN NSSI creation and provisioning, RAN NSSMF, in interaction with SMO, triggers the instantiation of necessary O-RAN functions (such as Near-RT RIC, O-CU-CP, O-CU-UP and ODU) based on slice requirements. After the creation of O-RAN NSSI, NSSMF in interaction with SMO may execute ONSSI modification and O-NSSI deletion procedures.

Since Non-RT RIC is part of SMO and would be instantiated along with other SMO functions, O2 is not expected to be used for lifecycle management of Non-RT RIC.

# 7.10 Transport network slicing

As O-RAN slice subnet is composed of not only the O-RAN NFs but also the transport network components; Fronthaul interface (FH) between O-RU and O-DU and the Midhaul interface (MH) between the O-DU and O-CU, transport slicing aspects needs to be considered and incorporated into the overall O-RAN slicing architecture.

There are different emerging approaches for defining transport network slicing that can meet 5G requirements, which mobile interfaces (fronthaul and midhaul in O-RAN slice subnet, backhaul between O-RAN slice subnet and core slice subnet, and between core slice subnet and the PDN) may and need to be sliced, what form they will take and the number of slices required at the transport layer [i.16].

This clause aims to capture the transport network slicing aspects for fronthaul and midhaul links and provide references to relevant O-RAN specifications (related to fronthaul, intra-DC virtual links, inter-DC links). Given the current state and progress in these WGs, this version of the O-RAN Slicing Architecture Specification will focus only on transport network aspects, with the scope of the network segments covered by O-RAN as shown in figure 7.10-1. The area inside the dotted green line characterizes the transport networks composed of a number of Transport Network Elements (TNE) deployed among different components defined in other O-RAN WGs. O-RAN does not define the interfaces along the dotted green line.

![](images/471de3cf9b919ab7e2b4e2b5ee1d270777933c41962efc19eede67eed80fddee.jpg)

> **Image Summary:** (Summary not available)
  
Figure 7.10-1: Xhaul transport network overview (ref: Figure 3-1 [i.16])

# Packet switched transport network slicing:

O-RAN has defined the architecture and the best practices for an open Xhaul transport network based on an end-to-end packet switching architecture in “Xhaul Packet Switched Architectures and Solutions specification” [i.16] that may support the requirements outlined in O-RAN.WG9.XTRP-REQ-v01.00 [i.17]. While the “Xhaul Packet Switched Architectures and Solutions specification” [i.16] describes the best practices for O-RAN transport based on end-to-end packet switching technology, it is recognized that other solutions, not based on packet switching, could be utilized, or mixed with a packet switching solution as well.

As indicated in clause 17 [i.16] the terms hard and soft slicing has emerged for transport networks, referring to the level of isolation between different slices:

Hard slicing: Transport resources are dedicated to a specific “Network Slice Instance” (NSI) and cannot be shared with other slices.   
Soft slicing: Transport resources are shared and may be re-used by other slices.

A packet switched infrastructure, as described in [i.16], has an extensive toolset, consisting of underlay forwarding solutions, Quality of Service (QoS) and VPNs that allows an operator to scalable partition the transport network to cater for both hard and soft slices. Transport slice requirements and associated toolset are shown in figure 7.10-2.

![](images/a2fdf2082aec5d17a85152ee00433a40dc85e76822bbf83de06ab7a17293c84d.jpg)

> **Image Summary:** (Summary not available)
  
Figure 7.10-2: Packet switched toolset for transport level slicing (ref: Figure 17-2 [i.16])

Further details of transport network slicing based on packet switching technology is captured in clause 17 and clause 18.10 of [i.16], including packet-switched underlay networks, transport network quality of service, 5G service and slices and a transport slicing scenario on a packet switched Xhaul network.

# O-RAN slice subnet provisioning procedures

# 8.1 O-RAN Slice Subnet Instance (O-NSSI) allocation procedure

The procedure for allocation of an O-RAN slice subnet instance to satisfy the O-NSSI requirements is given in figure 8.1- 1.

![](images/5a3c0485c6af05d43d74e5345e594d1e9fdd8aeb0a415536967f327a6e83799f.jpg)

> **Image Summary:** (Summary not available)
  
Figure 8.1-1: O-NSSI allocation procedure

1) Allocation request - Slice subnet management function receives an allocate O-NSSI request (AllocateNssi operation specified in 3GPP TS 28.531 [4], clause 6.5.2 shall apply) with network slice subnet related requirements (network slice subnet related requirements specified in SliceProfile in 3GPP TS 28.541 [7], clause 6.3.4 shall be used).   
2) Feasibility check - Slice subnet management function checks the feasibility of O-RAN slice subnet related requirements utilizing O-NSSI feasibility check procedure (see clause 8.4). If the network slice subnet related requirements can be satisfied, the following steps are needed, else go to step 15.   
3) O-NSSI decision - Based on the O-RAN slice subnet related requirements slice subnet management function decides whether to use an existing O-NSSI or create a new O-NSSI.   
4) Modification procedure - If using an existing O-NSSI and the existing O-NSSI needs to be modified, slice subnet management function invokes the O-NSSI modification procedure.   
5) Derive requirements - If creating a new O-NSSI, slice subnet management function creates the MOI for the O-NSSI to be created and then derives the corresponding O-RAN slice subnet constituent (i.e. O-RAN NF, constituent ONSSI) related requirements and transport network related requirements from the received network slice subnet related requirements.

For each required O-NSSI constituent, steps 6-11 are needed:

6) Allocation procedure - If the required O-NSSI constituent is constituent O-NSSI, slice subnet management function invokes O-NSSI allocation procedure (clause 8.1).

If the required O-NSSI constituent is a virtual O-RAN NF instance, steps 7-8 are needed:

7) Derive requirements - Slice subnet management function derives O-Cloud requirements for O-RAN NF.

8) Instantiate/Scale NF - If the O-RAN NF is a virtual NF, slice subnet management function establishes virtual intraCloud links, allocates slice tags (i.e., VLAN ID) and optionally instantiates NF on O-Cloud by executing network slice creation as specified in O-RAN.WG6.ORCH-USE-CASES- $\cdot \mathbf { v } 4 . 0 0$ [18], clause 3.10.1. If an existing O-RAN virtual NF instance needs to be modified, slice subnet management function may execute Scale Out of NF as specified in O-RAN.WG6.ORCH-USE-CASES-v4.00 [18], clause 3.2.2, Scale In of NF as specified in ORAN.WG6.ORCH-USE-CASES-v4.00 [18], clause 3.2.3.

9) CM requirements - Slice subnet management function derives CM requirements for O-RAN NF.

10) NF provisioning - Slice subnet management function executes provisioning management services as specified in ORAN.WG1.O1-Interface.0-v4.00 [13], clause 2.1.

11) Configure O-NSSI - Slice subnet management function configures the O-NSSI MOI.

For each transport network requirement, step 12 is needed:

12) Transport link request - If the transport link is a physical link that needs to be established across clouds, slice subnet management function request transport link establishment from TN management functions.   
13) Notification - If Non-RT RIC has subscribed for O-NSSI allocation event notifications, slice subnet management function notifies Non-RT RIC with O-NSSI information.   
14) Allocation response - Slice subnet management function returns appropriate O-NSSI allocation result (AllocateNssi operation specified in 3GPP TS 28.531 [4], clause 6.5.2 shall apply). If the O-NSSI is created successfully, the result includes the relevant constituent network slice subnet instance information (NetworkSliceSubnet IOC specified in 3GPP TS 28.541 [7], clause 6.3.2 shall apply).

# 8.2 O-RAN Slice Subnet Instance (O-NSSI) modification procedure

The procedure for modification of an O-RAN slice subnet instance to satisfy the O-NSSI requirements is given in figure 8.2-1.

![](images/7ea46839a88b53d42fcdd6a970af4d515f91b2ee96bc81b77ca90abefcd83eb1.jpg)

> **Image Summary:** (Summary not available)
  
Figure 8.2-1: O-NSSI modification procedure

1) Modify request - Slice subnet management function receives a modify O-NSSI request (modifyMOIAttributes operation specified in 3GPP TS 28.532 [5], clause 11.1.1.3 shall apply).   
2) Derive requirements - Based on the modification request, slice subnet management function derives modification requirements for the O-NSSI that may involve its constituents and transport network.   
3) Feasibility check - If required, slice subnet management function checks the feasibility of modification requirements utilizing O-NSSI feasibility check procedure. If the network slice subnet modification requirements can be satisfied, the following steps are needed, else go to step 11. For each O-NSSI constituent that needs modification, steps 4-9 are needed:   
4) Modification procedure - If the constituent is an O-NSSI constituent that needs to be modified, slice subnet management function invokes O-NSSI modification procedure (clause 8.2). If the constituent is an O-RAN network function, steps 5 and 6 are needed:   
5) NF orchestration - If the constituent network function is an O-RAN virtual network function that needs to be instantiated / modified / deleted, slice subnet management function realizes the following use cases as specified in O-RAN.WG6.ORCH-USE-CASES-v4.00 [18] depending on the modification requirements: a. O-RAN.WG6.ORCH-USE-CASES-v4.00 [18], clause 3.2.1 Instantiate NF On O-Cloud b. O-RAN.WG6.ORCH-USE-CASES-v4.00 [18], clause 3.2.2 Scale Out of NF c. O-RAN.WG6.ORCH-USE-CASES-v4.00 [18], clause 3.2.3 Scale In of NF d. O-RAN.WG6.ORCH-USE-CASES-v4.00 [18], clause 3.2.5 Terminate NF on O-Cloud   
6) NF provisioning - If the constituent network function needs configuration changes, slice subnet management function executes provisioning management services as specified in O-RAN.WG1.O1-Interface.0-v4.00 [13], clause 2.1. If O-NSSI constituent has TN part that needs to be modified, for each transport network requirement, steps 7-8 are needed:   
7) Transport link request - If the transport link is within a cloud, slice subnet management function requests virtual link modification within respective O-Cloud from NFO. Details of this request are not defined in the present document.   
8) Transport link modification - If the transport link is a physical link that is established across clouds, slice subnet management function requests transport link modification from TN management functions. Details of this request are not defined in the present document.   
9) Reconfigure O-NSSI - If O-NSSI MOI needs to be modified, slice subnet management function reconfigures the O-NSSI MOI.   
10) Notification - If Non-RT RIC has subscribed for O-NSSI modification event notifications, slice subnet management function notifies Non-RT RIC with modified O-NSSI information. Details of event notification between slice subnet management function and Non-RT RIC are not defined in the present document.   
11) Modification response - Slice subnet management function returns O-NSSI modification result (modifyMOIAttributes operation specified in 3GPP TS 28.532 [5], clause 11.1.1.3 shall apply).

# 8.3 O-RAN Slice Subnet Instance (O-NSSI) deallocation procedure

The procedure for deallocation of an O-RAN slice subnet instance to satisfy the O-NSSI requirements is given in figure 8.3-1.

![](images/9a2274d307761452953801d586a012ae6de242a7b58892d14189a9f3c285c015.jpg)

> **Image Summary:** (Summary not available)
  
Figure 8.3-1: O-NSSI deallocation procedure

1) Deallocation request - Slice subnet management function receives a deallocate O-NSSI request (DeallocateNssi operation specified in 3GPP TS 28.531 [4], clause 6.5.4 shall apply).

Slice subnet management function decides whether the O-RAN slice subnet instance needs to be modified or terminated. If the O-NSSI needs to be modified, go to step 2 and then step 13, else steps 3-13 are needed.

2) Modification procedure - Slice subnet management function invokes the O-NSSI modification procedure.

For each O-NSSI constituent, steps 3-9 are needed:

3) Deallocation procedure - If the constituent is an O-NSSI constituent, slice subnet management function invokes ONSSI deallocation procedure (clause 8.3). Then go to step 13.

If the constituent is an O-RAN NF, steps 4-9 are needed:

If O-RAN NF needs to be terminated and is a virtual NF, steps 4-5 are needed, else if O-RAN NF needs to be modified go to step 6.

4) Derive requirements - Slice subnet management function derives the O-Cloud requirements for O-RAN NF termination to terminate the NF within the respective O-Cloud.

5) Terminate NF - Slice subnet management function removes virtual intra-Cloud links, optionally deallocates slice tags (i.e., VLAN ID) and terminates NF on O-Cloud utilizing steps as specified in network slice deletion use case in O-RAN.WG6.ORCH-USE-CASES-v4.00 [18], clause 3.10.2.

If O-RAN NF is a virtual NF that needs to be modified, steps 6-7 are needed, else go to step 8:

6) Derive requirements - Slice subnet management function derives the requirements for O-RAN NF modification request to modify the NF within the respective O-Cloud.

7) Scale NF - Slice subnet management function invokes Scale In of NF use case as specified in O-RAN.WG6.ORCHUSE-CASES-v4.00 [18], clause 3.2.3.

If O-RAN NF needs to be reconfigured, steps 8-9 are needed, else go to step 10:

8) CM requirements - Slice subnet management function derives the CM requirements for the O-RAN NF.

9) NF provisioning - Slice subnet management function invokes provisioning management services as specified in ORAN.WG1.O1-Interface.0-v4.00 [13], clause 2.1.

For each transport network requirement, step 10 is needed:

10) Transport link request - If the transport link is a physical link that needs to be modified/terminated across clouds, slice subnet management function request transport link modification/termination from TN management functions.

11) Notification - If Non-RT RIC has subscribed for O-NSSI deallocation event notifications, slice subnet management function notifies Non-RT RIC with O-NSSI deallocation.

12) Deallocation response - Slice subnet management function returns appropriate O-NSSI deallocation result (DeallocateNssi operation specified in 3GPP TS 28.531 [4], clause 6.5.4 shall apply).

# 8.4 O-RAN Slice Subnet Instance (O-NSSI) feasibility check and reservation procedure

# 8.4.1 Introduction

The feasibility check and reservation procedure enables a service consumer to perform feasibility check and request reservation for O-NSSIs. The reservation request is optional. The procedure determines if adequate resources are available to support the O-RAN network slice subnet related requirements provided in the request. The procedure also allows a service consumer to request the reservation of those resources for specified time window.

# 8.4.2 Procedure

The procedure for feasibility check and reservation of an O-RAN slice subnet instance is given in figure 8.4.2-1.

![](images/5b1b177d358e8919fdf8e43d937d341fcbd4a73d2e5fb627faf786fc24a4c0fb.jpg)

> **Image Summary:** (Summary not available)
  
Figure 8.4.2-1: O-NSSI feasibility check and reservation procedure

1) Feasibility check and reservation job creation request – Slice management function receives a O-NSSI feasibility check and reservation job creation request from the SMO service consumer.

2) Instance creation The slice management function creates and configures the FeasibilityCheckAndReservationJob instance and applies the attributes received from the request. See 3GPP TS 28.541 [7], clause 6.3.37 for more details on the IOC. Then, the slice management function starts executing the feasibility check process.

3) Feasibility check and reservation job creation response – The slice management function sends the O-NSSI feasibility check and reservation job creation response for the received Distinguished Name (DN) of the

FeasibilityCheckAndReservationJob instance back to the SMO service consumer. See Create Managed Object Instance operation described in O-RAN WG1 O1-Interface [13], clause 2.1.

4) Feasibility check – For each O-NSSI constituent that has an active job, the slice management function performs a feasibility check within the SMO internally, such as communicating with FOCOM, OAM functions and TN management functions, as to whether the resources are available. This would be a use case from the Cloudification & Orchestration (WG6) in the O-RAN WG6.ORCH-USE-CASES [18] specification using the NFO and FOCOM SMOS services.

5) Reservation procedure – Slice management function performs resource reservation process when resourceReservation is true and feasibility result is feasible. The reservation procedure for the constituent network slice subnet is a use case from the Cloudification & Orchestration (WG6) use cases with the NFO and FOCOM SMOS services.

6) Progress notification – The SMO service consumer may subscribe for the attribute value change notifications for this specific job or for any of the job(s) created by it to receive any asynchronous job progress notifications for those job(s). The slice management function sends an asynchronous job progress notification for the feasibility check and reservation process with processMonitor attributes to the SMO service consumer.

7) Reservation conclusion – The slice management function sends the final notification with the feasibility check and reservation status. This includes the feasibilityResult, inFeasibleReason, resourceReservation status, reservationFailure reason, reservation expiration and recommended requirements of the feasibility check and reservation job.

A progress check is performed in steps 8-10:

8) The SMO service consumer can send a feasibility check and reservation progress query request to slice management function any time, to query about the feasibility check and reservation job status and receive the feasibility check and reservation job status.

9) The slice management function reads the corresponding information of the feasibility check and reservation job instance.

10) The slice management function returns the feasibility check and reservation progress query response.

SMO service consumer deletes the feasibility and reservation job in steps 11-14:

11) Delete operation – SMO service consumer can request to delete the feasibility check and reservation job any time. This is done by sending to the slice management function a feasibility check and reservation job deletion request.

12) For each reserved O-NSSI constituent, the cancel the reservation process is executed.

13) The slice management function deletes the job.

14) The slice management function returns a feasibility check and reservation job deletion response back to the slice management function.

# Annex A (informative): Implementation options

A.1 Implementation options

This clause presents example deployment options for various SMO options.

# A.1.1 3GPP and ETSI NFV-MANO based O-RAN slicing architecture implementation option

![](images/1feac9bc53619613857e0ae0c8cf13d700b2dff1aff9fff5659cbb180d2f3235.jpg)

> **Image Summary:** (Summary not available)
  
Figure A.1.1-1: O-RAN slicing reference architecture (ETSI NFV-MANO based example)

A 3GPP – ETSI NFV-MANO based example of O-RAN slicing reference architecture and interfaces is shown in figure A.1.1-1 to describe the relationship between 3GPP defined slice management functions (NSMF, NSSMF), 3GPP defined management functions (3GPP TS 28.531 [4], Network Function Management Function (NFMF) and O-RAN network functions in terms of slice lifecycle management and slice configuration procedures. Life Cycle Management (LCM) procedures for mobile networks that include Virtualized Network Functions (VNFs) as well as addition of Physical Network Functions (PNFs) to Network Service (NS) instances are specified in 3GPP TS 28.526 [3].

![](images/cc38d025016c6f361f819963c9a673c6e2a8df206317965acc0904cec42c82fc.jpg)

> **Image Summary:** (Summary not available)
  
A.1.2 ONAP based O-RAN slicing architecture implementation option   
Figure A.1.2-1: Example architecture depiction for ONAP based O-RAN slicing support

Current version of ONAP - O-RAN slicing reference architecture is shown in figure A.1.2-1 (based on ONAP G-release). In this architecture, one option is RAN NSSMF being located within SMO and is responsible for the entire RAN subnet, including the O-RAN NFs and the related O-RAN transport network components; Fronthaul interface (FH) between ORU and O-DU and Midhaul interface (MH) between O-DU and O-CU. RAN NSSMF determines slice specific configuration of O-RAN NFs based on SliceProfile received from NSMF and determines the necessary slice specific requirements for FH and MH interface triggering Transport Network Management Domain (TN MD) to execute the actual configuration of FH and MH interface. ETSI ZSM based management domain approach is adopted for TN management.

# Annex B (informative): Transport network slicing

# B.1 Transport network slicing use cases

This clause describes the ORAN transport network slicing related use cases and per-slice configuration of O-RAN transport network instances, phases of transport network slicing definition process and the corresponding scope of work for the relevant O-RAN WGs, considering the projected progress.

Transport network slicing use cases are built based on the definitions of slicing in O-RAN WG1 Slicing Architecture Specification, WG6.CAD Scenario C.1 and C.2, WG4 O-RU Slicing with support of RAN-Sharing (WG4 Use Case 7 and Use Case 10).

Transport network slicing use cases are grouped into phases to incrementally extend the scope of work in relevant ORAN WGs.

Brief definition of phases:

Phase 1: Slicing as specified in 3GPP TS 22.261 [1], [i.2] and 3GPP TS 23.501 [2]. Slicing appears on the N3 (NG) interface. Number of slices are limited. UPF is centrally located.

Phase 2: Phase 1 is augmented with per-slice QoS characteristics. Slices are multiple with multiple exit-points and local break-outs.

Phase 3 and beyond are not defined in the present document.

For the current version of transport network slicing use cases the following scope and constrains are assumed, based on mutual discussions and agreements between WG1, WG6, WG9:

Delineation of slices in O-RAN CUPS user plane interfaces for current phases 1-5 is based on physical or VLAN+IP separation. For this delineation, procedures for coordination between TN<>O-RAN and $\mathrm { T N } { \lesssim } { > } 5 \mathrm { G C }$ provisioning VLAN, IP and corresponding TN service instances are expected. Fronthaul – connectivity driven domain, providing traffic differentiation and prioritization according to open fronthaul interface definition, given in O-RAN.WG4.CUS.0-v06.00. No need to support slicing in phases 1 to 4. The support for multi-vendor slicing in the fronthaul is expected to be introduced in phase 5.   
• Midhaul – connectivity driven domain, providing traffic differentiation and prioritization according to 5QI model of F1 interface, defined in TS38.474. No need to support slicing in phases 1 to 3. DDoS prevention and traffic control are expected to protect O-DUs from O-CU-UPs, which in future phases may belong and be controlled by $3 ^ { \mathrm { r d } }$ parties. From phase 3 and beyond, midhaul is slicing aware domain, serving communication of O-CUUP $< >$ O-DU with slicing. For that O-CU-UP and O-DU are expected to perform marking of F1AP with DSCP and attach VLAN .1q tag and assign IP for slice delineation. Backhaul – slicing aware domain, serving communication of UPF $< >$ O-CU-UP with slicing. O-CU-UP and UPF are expected to perform marking of N3 interface according to 5QI $< >$ DSCP marking and push .1q tag and assign IP for slice delineation.   
• Based on shared O-RU feature progress (WG4 Use Case 7 and Use Case 10), single O-RU are expected to serve multiple slices and multiple O-DUs, so the expectation is to have capability to maintain mapping of PLMN ID information to corresponding VLAN $^ +$ optional IP pair on C/U Plane of open fronthaul interface.   
• O-DU is expected to support multiple slices. Single O-DU, serving multiple slices, supposed to have capability to maintain mapping of O-NSSI information to corresponding VLAN+IP pair on F1 interface and 5QI to DSCP mapping. This assumes progress of WG5 effort on definition upstream DU $>$ CU_UP F1_U 5QI $< >$ DSCP mapping capabilities.

O-CU-UP is expected to support multiple slices. Single O-CU-UP, serving multiple slices, supposed to have capability to maintain mapping of O-NSSI information to corresponding VLAN+IP pair on F1 interface, however in current phases 1-5 it is assumed that cluster of O-CU-UPs will serve single O-NSSI, as it is shown in figure B.1-1.

![](images/e5be32bfbf64d7b1c4c898c286d0d15cd35821acfe74b88b959c447fec4aa126.jpg)

> **Image Summary:** (Summary not available)
  
Figure B.1-1: Assumption of mapping functions of O-DU and O-CU-UP to slices

From O-RAN perspective, a single network slice may start from O-DU and may have multiple distributed O-CU-UPs and UPFs, connecting a certain slice in data network with multiple N6 interfaces and multiple local breakouts.

In TN domain TNEs with attachment circuits to O-RU, O-DU and O-CU-CP and O-CU-UP maintain corresponding QoS schemes and transport network slice profiles as shown in figure B.1-2 and in figure B.1-3.

![](images/ed9e60beaac8f2dcc8bc0a852621e9198b9000d0d67a887c9f8cb12fda7be380.jpg)

> **Image Summary:** (Summary not available)
  
Figure B.1-2: Types of slicing in various O-RAN scenarios

![](images/5074d440800a1fb84199046cd19f6da60e94345471e31153fd0e24b92f00fca7.jpg)

> **Image Summary:** (Summary not available)
  
Figure B.1.-3: Types of attachment circuits in TNE

The assumptions of slicing capabilities on the core and O-RAN for the option 1 which are mapped to the phase 1 are given in figure B.1-4.

The option 2 depicts the expectation of the target capabilities of the systems, including capabilities on the option 1.

![](images/f53df76dbeba4ffd4172cbe501209ac2cfd52a12607a2299bd7e62f182972398.jpg)

> **Image Summary:** (Summary not available)


# Figure B.1-4: Options for slicing, demapping orthogonal plane of 5QI per slice in option 1 and multiple planes of 5QI as attribute per planes of slices

For phase 1 following constrains are assumed (see figure B.1.5):

1) Single operator with one O-NSSI MBB, one O-NSSI mMTC, one O-NSSI NB-IoT slice.

2) Fix mapping of slices inter to intra – DC.

3) Flat mapping of standards based 5QI (3GPP TS 23.501 [2], table 5 $. 7 . 4 \mathrm { - } 1 ) \hookrightarrow \mathrm { D S C P } \diamondsuit \mathrm { Q o } \ddagger$ S in TN domain.

![](images/c0b3320cae47774e2e558a284238c9390e1ff30fbce489e4e1ac0387e0e4ff23.jpg)

> **Image Summary:** (Summary not available)


# Figure B.1-5: Diagram of network location of O-RAN instances with relevant domains for use cases

As an outcome of the following mapping, it is expected capability of TN domain to accommodate all domains with relevant QoS profiles and slices in each TNE, as shown in figure B.1.6 below:

![](images/5ffb6cd6c9ca8b207b16cbb67789cba5fa01924fcf3cbef9c74305e4baaf8943.jpg)

> **Image Summary:** (Summary not available)
  
Figure B.1-6: Diagram of O-RAN flows to be accomodated in each TNE

Table B.1-1 captures assumptions of TN slicing capabilities in each interface for the phase 1.

Table B.1-1: Scope of the capabilities of O-RAN elements in phase 1   

<table><tr><td colspan="1" rowspan="1">ORANinterface</td><td colspan="1" rowspan="1">Streamdirection</td><td colspan="1" rowspan="1">Queue</td><td colspan="1" rowspan="1">SlicingVLAN</td><td colspan="1" rowspan="1">Differentiated QoSbehavior per slice</td></tr><tr><td colspan="1" rowspan="1">Fronthaul C/U</td><td colspan="1" rowspan="1">Any</td><td colspan="1" rowspan="1">EF (HP)</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">No</td></tr><tr><td colspan="1" rowspan="1">Fronthaul M-pane,</td><td colspan="1" rowspan="1">Any</td><td colspan="1" rowspan="1">AF</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">No</td></tr><tr><td colspan="1" rowspan="1">E1, E2, F1_c, O2, A1,Xn_C, N2, N4</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">F1_U</td><td colspan="1" rowspan="1">DU &gt;CU-UP</td><td colspan="1" rowspan="1">AF*or 5QI&lt;&gt;DSCPmapped**</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">No</td></tr><tr><td colspan="1" rowspan="1">F1_U</td><td colspan="1" rowspan="1">CU-UP&gt;DU</td><td colspan="1" rowspan="1">5QI&lt;&gt;DSCPmapped**</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">No</td></tr><tr><td colspan="1" rowspan="1">N3 (NG)</td><td colspan="1" rowspan="1">CU-UP&gt;UPF</td><td colspan="1" rowspan="1">5Ql&lt;&gt;DSCPmapped**</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">No</td></tr><tr><td colspan="1" rowspan="1">N3</td><td colspan="1" rowspan="1">UPF&gt;CU-UP</td><td colspan="1" rowspan="1">5Ql&lt;&gt;DSCPmapped**</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">No</td></tr><tr><td colspan="1" rowspan="1">xn_U</td><td colspan="1" rowspan="1">Any</td><td colspan="1" rowspan="1">5Ql&lt;&gt;DSCP mapped(as per TS 38.424)</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">No</td></tr></table>

\* Based on current 3GPP TS38.474, clause 5.4 definition of 5QI $< >$ DSCP capability of F1_U for the link DU $>$ CU-UP may be limited. If this is the case, for the phase 1 the mapping of F1_U is recommended to a bandwidth queue.

\*\* 5QI QoS identifiers, the priority level (if explicitly signaled), and other NG-RAN traffic parameters (e.g., ARP) in ORAN and core domains mapped to DSCP and ToS or CoS parameters, aligned with TN domain with accordance to NRM as specified in 3GPP TS 28.541 [7], with the flow shown in figure B.1-7 below:

![](images/9806983c4ffc2219b1c6cbc1b7edac01b370048d2cd2f81134d5990eb1ed9996.jpg)

> **Image Summary:** (Summary not available)
  
Figure B.1-7: Diagram of profiles information model parameters mapped to the domains to form a slice

According to these parameters, the relation of RANSliceSubnetProfile and RANSliceSubnetProfile with VLAN and IP mapping could be established with corresponding EP_Transport VLAN and IP mapping, allowing TN domain to perform separation allocation of resources per slice.

Definition of 3GPP IM/DM in 3GPP TS 28.541 [7] TN domain is out of scope, and network slice parameters of the RAN and CN are existing in the corresponding fields of the IM/DM. More details in of 3GPP IM/DM in regard for network slicing can be found in O-RAN.WG9.XTRP-MGT.0-v04.00 [i.19], clause 9.1.

# Phase 2 assumes the following constrains (see figure B.1-8):

1) Single operator with enterprise slices use case.   
2) Number of slices: many.   
3) Multiple exit points and multiple UPFs.   
4) Per-slice (tenant) 5QI<>DSCP $< >$ QoS model in TN domain.

![](images/23ea6ab4ce449ff13bab76b1b7487289e2844a4dc98494bf69f191fe3e544fe2.jpg)

> **Image Summary:** (Summary not available)
  
Figure B.1-8: Scope of the capabilities of O-RAN elements in phase 2

\* 5QI QoS identifiers, the priority level (if explicitly signaled), and other NG-RAN traffic parameters (e.g., ARP) in ORAN and core domains mapped to DSCP and ToS or CoS parameters, aligned with TN domain with accordance to NRM as specified in 3GPP TS 28.541 [7], with the flow shown in figure B.1-9 below:

![](images/36fef6883a027b0f153a366608ca4a0f3980133486abc770079fabc07a9d3de3.jpg)

> **Image Summary:** (Summary not available)
  
Phase 2 and 3:   
Figure B.1-9 Diagram of use cases for phase 2 and 3

Table B.1-2 captures assumptions of TN slicing capabilities in each interface for the phase 2 and later.

Table B.1-2: Scope of the capabilities of O-RAN elements in phase 2 and later \*\*Based on assumption on WG5 and WG6 effort on definition F1_U slicing capabilities (inter-DC risk of missing the March train).

<table><tr><td rowspan=1 colspan=1>ORANinterface</td><td rowspan=1 colspan=1>Streamdirection</td><td rowspan=1 colspan=1>Queue in 4Queue model</td><td rowspan=1 colspan=1>SlicingVLAN</td><td rowspan=1 colspan=1>DifferentiatedQoS behaviorper slice</td></tr><tr><td rowspan=1 colspan=1>Fronthaul C/U</td><td rowspan=1 colspan=1>any</td><td rowspan=1 colspan=1>EF (HP)</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr><tr><td rowspan=1 colspan=1>Fronthaul M-pane,E1, E2, F1_C, O2, A1,Xn_C, N2, N4</td><td rowspan=1 colspan=1>any</td><td rowspan=1 colspan=1>AF</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr><tr><td rowspan=1 colspan=1>F1_U</td><td rowspan=1 colspan=1>DU &gt; CU-UP</td><td rowspan=1 colspan=1>5Ql&lt;&gt;DSCP mapped*</td><td rowspan=1 colspan=1>yes**</td><td rowspan=1 colspan=1>no</td></tr><tr><td rowspan=1 colspan=1>F1_U</td><td rowspan=1 colspan=1>CU-UP &gt;DU</td><td rowspan=1 colspan=1>5Ql&lt;&gt;DSCP mapped</td><td rowspan=1 colspan=1>yes**</td><td rowspan=1 colspan=1>no</td></tr><tr><td rowspan=1 colspan=1>N3 (NG)</td><td rowspan=1 colspan=1>CU-UP&gt;UPF</td><td rowspan=1 colspan=1>5Ql&lt;&gt;DSCP mapped***</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td></tr><tr><td rowspan=1 colspan=1>N3</td><td rowspan=1 colspan=1>UPF&gt; CU-UP</td><td rowspan=1 colspan=1>5Ql&lt;&gt;DSCP mapped***</td><td rowspan=1 colspan=1>yes</td><td rowspan=1 colspan=1>no</td></tr><tr><td rowspan=1 colspan=1>Xn_U</td><td rowspan=1 colspan=1>any</td><td rowspan=1 colspan=1>AF</td><td rowspan=1 colspan=1>no</td><td rowspan=1 colspan=1>no</td></tr></table>

\*Based on assumption on WG5 and WG6 effort on definition upstream DU $>$ CU_UP F1_U 5QI $< >$ DSCP mapping capabilities.

\*\*\*More on Mapping recommendation in WG9 “RBBN-TFCA-QoS mapping” contribution.

After this analysis and discussions within ORAN WG9 the conclusion is that NRM as specified in 3GPP TS 28.541 [7] does not provide enough data to create valid transport network slice.

However, since some of the parameters required to create transport network slice may be extracted from NRM as specified in 3GPP TS 28.541 [7] and some may be translated from SMO expectations, the following scope of work for WG9 and WG10 is proposed:

Collect missing parameters in 3GPP TS 28.541 [7] for TN slice creation. Propose enhancements of 3GPP TS 28.541 [7] to include OpenModelClass TNSliceSubnet to link EP_Transport to TN and add options for linking 3GPP subsystems to TN subsystems. File ORAN liaison to SA5 in order to augment 3GPP TS 28.541 [7] with missing information and proposed items. Align with IETF TN network slice abstraction. Define information flows. Align ORAN WG1, WG9 and WG10.

# Annex C (informative): Slicing terminology

# C.1 Slicing and 3GPP slice modeling terminology awareness

This clause intends to provide further information and clarified awareness for some of the fundamental network slicing concepts and 3GPP modeling aspects.

# C.1.1 NSI and NSSI context in 3GPP SA2 and SA5

(System Architecture) Network Slice (3GPP SA2): Even though this is a system architecture group, the RAN architecture is out of the scope of SA2. RAN3 owns the RAN architecture. SA2 service-based architecture (SBA) is a functional architecture with mostly service-based interfaces.

(Management Aspect) Network Slice (3GPP SA5): SA5 describes all the management aspects of a network, which is modular, and model driven. It is a service-based management architecture (SBMA), using service-based API allowing implementations to pick and choose appropriate API and compliance per API. See 3GPP TS 28.533 [i.18].

A Network Slice Instance (NSI), a SA2 term, is a set of functions. SA2 also introduced the concept of an instance because there would be more than one slice of the same type for the purpose of scaling. What is managed by an operator is a group of functions (an NSI).

A NetworkSlice Managed Object Instance (MOI), a SA5 usage, is an object exposing to an external consumer. Once an operator builds a something to satisfy expectations, it needs to build something that is exposed to an external consumer which is a NetworkSlice MOI. Scale in/Scale out is an operation within life cycle management which is under the purview of SA5. In the context of SA5, a NSI is just an attribute carrying signaling “NSI” value semantic. From a management perspective, the abbreviation NSI is sometimes used as a replacement of the proper term NetworkSlice MOI. However, this is just an improper use of terminology.

A NetworkSliceSubnet MOI is sometimes called an NSSI. However, in SA5, any occurrences of the term NSSI should be perceived as a NetworkSliceSubnet MOI.

# C.1.2 Name containment limitation

NSSI stands for NetworkSliceSubnet Instance a.k.a. Managed Object Instance (MOI) of the NetworkSliceSubnet Information Object Class (IOC).

NetworkSliceSubnet IOC has been introduced to group instances (of any IOC) in a way that is not restricted by the Name Containment (DN) rules. Those name containment rules are specified in 3GPP TS 32.300 [9]. Name containment defines a managing hierarchy. The flexibility of supporting network sharing management in network slice scenario (especially for shared network functions) is fulfilled by introducing the NetworkSliceSubnet concept in 3GPP TS 28.541 [7] which allows for multiple views or “overlays” to augment the management hierarchies. This grouping is independent of how the network is managed and structured via distinguished names. Note that the NetworkSliceSubnet inherits from the top IOC (3GPP TS 28.541 [7], clause 6.2.2).

This is illustrated in the following diagram given in figure C.1.2-1:

![](images/82cc4eadc0c728d0ee528121343c81939ad134480390ebdd52269d360c32b2e8.jpg)

> **Image Summary:** (Summary not available)
  
Figure C.1.2-1: Multi-parent inheritance supported from network slice subnet instance

# C.1.3 Network slice subnet is a purposeful generic collection

The definitions and diagrams that follow are driven from 3GPP 5G NRM specifications in 3GPP TS 28.541 [7]. The 3GPP 5G NRM serves as a foundation for ORAN specification development, and modeling work from which ORAN development aligns to. For further details, please refer to O-RAN WG5 and WG10 specifications. The diagrams in this document utilize elements from the 3GPP 5G NRM but should be fully applicable to the ORAN IM.

The NetworkSliceSubnet is a purposeful generic collection of objects. The NetworkSliceSubnet can be comprised of a number of managedfunctions, networkservices and EP_Transport endpoints as shown in the diagram below inspired from the 3GPP TS 28.541 [7], clause 6.

Three key points that the diagram illustrates is that:

1. Generic Collection: The NetworkSliceSubnet is a purposeful generic collection of objects shown in the diagram.

2. Recursive:The NetworkSliceSubnet is a recursive structure which may self-reference NetworkSliceSubnets

3. Purposeful: The “purpose” of that generic collection of objects is defined in the SliceProfile.

NOTE 1: The cardinality between NetworkSliceSubnet and SliceProfile which is written as 1…\* could be an empty list: 1…0 which would imply there is no SliceProfile. You could group a set of objects without a profile. Profiles are derived from the SLS.

NOTE 2: It is stated that it is under consideration in 3GPP that the SliceProfile can become an IOC.

These points are highlighted in the following diagram given in figure C.1.3-1:

![](images/419afd996f50d2bd3af6e8630b563752691ae2f1f661c00cd8988b0bfa4e869f.jpg)

> **Image Summary:** (Summary not available)
  
Figure C.1.3-1: NetworkSliceSubnet is a purposeful generic collection

# C.1.4 Slicing instance example

The following diagram given in figure C.1.4-1 shows an example instance of a NetworkSliceSubnet.

![](images/749e7c5820b1e33465167ecfca5845766b38a4b47372e449305c996e330124af.jpg)

> **Image Summary:** (Summary not available)
  
Figure C.1.4-1: Slicing instance example

As a concrete example given in figure C.1.4-1, the above diagram shows instances of managed functions and network slice subnets. Depicted are two network slices (NS1, NS2), with their associated NetworkSliceSubnets, core and RAN managed function components. The picture illustrates that NetworkSliceSubnets are generic groupings of objects. These relationships are indicated by the $< <$ groups>> tag. This diagram shows two eMBB network slices that are providing two different services with different throughput SLA requirements within the network of the same service provider (PLMNA).

Notice that the NetworkSliceSubnets have SliceProfiles associated with them in this example. The illustration also highlights how some name containment relationships (3GPP TS 32.300 [9]). These are indicated by the <<names>> tag. Notice that NSS2 (NetworkSliceSubnet #2) is a collection of 5G core components (UPF1, AMF1, SMF1); and that NSS1 is a collection of 5G RAN components (DU1, CUCP1, CUUP1, NRCellDU1, NRCellCU1). NSS3 and NSS4 are the NetworkSliceSubnets that expose the “stitched” groupings. The NSS3/NSS4 will have a slice profile that reflects the entire SLA/SLS represented by the service profile. While NSS1/NSS2 will have portions of the entire SLS pertaining to the corresponding (e.g. transport, RAN, core) parts of the slice. This illustrates that the “stitching” occurs at the OSS / network management layer not at the BSS layer where slice orchestration happens. Slice instances at the BSS, the subnets are handled as the management layers.

# C.1.5 NSSI slice profile and PLMNInfo

The “purpose” of the NetworkSliceSubnet MOI is given in the SliceProfile which is associated with it. It may be associated with a particular network slice or a group of network slices. The association is accomplished through the pLMNInfoList attribute of the SliceProfile. The Slice Profile is a data type that represents the requirements or purpose of the generic collection instance that may support one or more NetworkSliceSubnet instances. For an end-to-end Network Slice to exist, it is expected that it would have an associated slice profile containing a pLMNInfoList.

NOTE: A NetworkSliceSubnet may be just a generic collection of objects not associated with an End-to-End Network Slice. In this case, there may not be a slice profile associated with NetworkSliceSubnet.

Both 3GPP Release 16 and 3GPP Release 17 5G NRM have the SliceProfile, therefore 3GPP TS 28.541 [7] shall be used for further details. This is illustrated in the following diagram given in figure C.1.5-1:

# TS28.541 3GPP Release 16

# TS28.541 3GPP Release 17

3GPP TS28.541 (Release 16) Clause 6.3.2 / 6.3.4.2

3GPP TS28.541 (Release 17) Clause 6.3.2 /6.3.4.2

# Slice Profile

# Slice Profile

<table><tr><td rowspan=1 colspan=1>ATTRIBUTE NAME</td></tr><tr><td rowspan=1 colspan=1>sliceProfileld</td></tr><tr><td rowspan=1 colspan=1>pLMNInfoList</td></tr><tr><td rowspan=1 colspan=1>perfReq</td></tr><tr><td rowspan=1 colspan=1>maxNumberofUEs</td></tr><tr><td rowspan=1 colspan=1>coverageAreaTAList</td></tr><tr><td rowspan=1 colspan=1>latency</td></tr><tr><td rowspan=1 colspan=1>uEMobityLlevel</td></tr><tr><td rowspan=1 colspan=1>resourceSharingLevel</td></tr></table>

<table><tr><td rowspan=1 colspan=1>ATTRIBUTE NAME</td></tr><tr><td rowspan=1 colspan=1>sliceProfileld</td></tr><tr><td rowspan=1 colspan=1>pLMNInfoList</td></tr><tr><td rowspan=1 colspan=1>CNSliceSubnetProfile</td></tr><tr><td rowspan=1 colspan=1>RANSliceSubnetProfile</td></tr><tr><td rowspan=1 colspan=1>TopSliceSubnetProfile</td></tr></table>

# SLICE PROFILEpLMNInfoList

The "purpose" of a NetworksliceSubnet MOl may be associated with a particular slice / group of slices. The association is done via pLMNInfoLi st attribute of sliceProfi le (slice profile represents the purpose of the collection instance, the purpose may be to support one or more slices).

Figure C.1.5-1: Slice Profile contains a List of PLMNInfo

# C.1.6 Managed functions have a list of PLMNInfo

The concrete managed functions, notably the gNBCUUPFunction, NRCellCU and NRCellDU each can have a list of PLMNInfo attributes. Concrete managed functions are configured with the slice information via the pLMNInfoList attribute. It is mainly used for signaling. Additionally, the concrete managed function becomes associated with a network slice.

Configuration caveats for network slice management:

First, a managed function can be configured with a particular entry in the pLMNInfoList but it is not member of any network slice subnets associated with profiles containing the same entry in their pLMNInfoList (signaling configured, management association missing).

Second, a managed function cannot be configured with a particular entry in the pLMNInfoList but is a member of a network slice subnet associated with profiles containing this particular entry (management association present, signaling configuration missing).

This is illustrated in the following diagram given in figure C.1.6-1:

# (Concrete managed functions)pLMNInfoList

![](images/8748d70b8ccc8d01cc09878f472182711e704aa6e473dd99abab372c74e4ca60.jpg)

> **Image Summary:** (Summary not available)
  
Figure C.1.6-1: Managed functions have a list of PLMNInfo

Concrete managed functions are configured with the slice information via the pLMNInfoLi st attribute. It is mainly used for signaling. Additionally, the concrete managed function becomes associated with a Network Slice.

# C.1.7 Single Network Slice Selection Assistance Information (S-NSSAI)

A Single Network Slice Selection Assistance Information (S-NSSAI) is used to define a slice. It is a 32-bit number defined by 3GPP TS 23.003 [i.2], clause 28.4.1. S-NSSAI is comprised of Slice / Service Type (SST) and Slice Differentiator (SD). SST have values 0 to 127 standards reserved and 128 values are operator defined. These are specified in 3GPP TS 23.501 [2]. The standardized SST values are specified in 3GPP TS 23.501 [2], clause 5.15.2.2.

# Annex D (informative): Multi-operator slice RAN management services exposure

# D.1 RAN management services exposure for multi-operator slice

Sharing of RAN resources is one of the key requirements for Mobile Network Operators (MNO) to reduce the RAN infrastructure cost and increase profitability, while enhancing the coverage. Currently O-RAN drives the RAN sharing models and associated considerations through WG1 Use Cases Detailed Specification Use Case 7: RAN Sharing which focus on the MORAN (Multi Operator RAN) scenario and sharing computing resources (for more details 3GPP TS 22.261 [1] shall be used). The goal of the existing RAN Sharing use case is to enable multiple operators to share the same ORAN infrastructure wherein each operator utilizes a separate carrier, while allowing them to remotely configure and control the shared resources via a remote O1, O2 and E2 interface.

While the RAN Sharing use case set the premise for sharing the infrastructure and extending the management interfaces, the use case does not clearly depict the network slicing scenarios especially offering and usage of RAN objects related to network slicing in context of relation between multiple operators. The need for such a slice usage consumption /offering scenario is depicted in 3GPP specification 3GPP TR 28.824 [i.7], 3GPP TR 28.801 [i.3], 3GPP TS 28.530 [23] and other industry initiatives like 5GPPP Slicenet [i.10] project. Specifically, 3GPP TR 28.824 [i.7] depicts the management capability exposure across multiple operators, especially Network Operator (NOP) role played by multiple operator organizations – one offering RAN objects related to network slicing and other using the RAN objects related to network slicing to establish an end-to-end slice. Few examples of business use cases are depicted below:

Cross MNO Model of offering and usage of RAN objects related to network slicing

Two MNOs get into agreement in a scenario where one of the MNOs do not have spectrum or coverage in a particular region (such as foreign country, remote areas, out of service area) to share RAN resources. The arrived solution to share RAN is to utilize RAN objects related to network slicing to fix coverage gaps. E.g., network slice consisting of core objects belonging to MNO1, and RAN objects belonging to MNO2.

Many MNOs form a consortium and share RAN resource through bulk provisioning of RAN objects related to network slicing that can be offered on demand for subscription to address the needs of consortium participating MNOs (for example to address the emergency, disaster response).

• MVNO relying on multiple MNOs. Each MNO offers its RAN resources as RAN objects related to network slicing.

MNO and Hyperscale Public Cloud Provider slice consumption offering model

There is a market trend of collaboration between Hyperscale Public Cloud companies and MNOs in which Hyperscalers count on access network infrastructure owned by MNO, while utilizing the edge and core network services using their own or partner services. In this model the RAN objects related to network slicing is offered to the Hyperscalers and integrated to offer a unified service.

Considering that standards, related marketing trends and described cases with multiple parties involved, there is a great value to streamline parties’ interaction with respective O-RAN specification activities.

From an O-RAN standardization perspective following three aspects need to be considered in context of these use case models:

Exposure of management services providing lifecycle management, CM, FM, PM, performance analytics and other management capabilities of RAN logical instances (as a collected group of RAN objects related to network slicing) for usage of RAN objects related to network slicing in context of relation between multiple operators

Exchange and mapping of resource identifiers corresponding to a collected group of RAN objects related to network slicing for it to be composed into an end-to-end slice. Governance of the exposed O-RAN slice subnet management services for them to be made available externally in a secured and manageable manner.

NOTE 1: Logical instances as collected group of RAN objects related to network slicing implies representation of a group of logical components within each RAN node that collectively provide required characteristics of network slice at RAN part which is commonly called in the O-RAN Slicing Architecture Specification as O-RAN slice subnet.

NOTE 2: Direct SMO exposure to external slice management systems across MNOs assumes prior business agreement (contract) between parties.

NOTE 3: Correct interpretation of FM and PM data may require prior interface agreements with exchange of related data (e.g., specifications of PM, FM problem types, MIB files).

NOTE 4: “Multi-Operator slice” is a term used to represent a concept of end-to-end network slice that uses O-RAN slice subnet instances (collected group of RAN objects related to network slicing) provided by MNO in shared RAN resources. As needed, the partner operator would define its PLMN specific network slice (as per 3GPP TS 23.501 [2], slice is identified by S-NSSAI within a specific PLMN ID but not multiple PLMN IDs) in that end-to-end slice.

# D.1.1 Management services exposure for multi-operator slice - Relevant standards

3GPP TS 28.530 [23], clause 4.1.6 Network Slice as a Service (NSaaS): Explains the concept of NSaaS offered by CSP to CSC and the ability of the CSC to manage the network slice as manager via management interface exposed by the CSP. Further, the CSC is also allowed to offer their own services (e.g., communication services) on top of the network slice obtained from the CSP.

3GPP TS 28.533 [i.18], clause A.3 Utilization of management services by Exposure Governance Management Function (EGMF): Explains the management capability of EGMF, especially exposure governance and also depicts an example of exposing the Management Function (MnF) capability through the EGMF to MnF from another operator or to $3 ^ { \mathrm { r d } }$ Party. The standardization of EGMF in 3GPP is not mature and require further elaboration.

• 3GPP TS 28.824 [i.7]: Focused study on network slice management capability exposure. Highlights the general concept of exposure of management service (e.g., via BSS, without going through BSS), the roles related to network management capability exposure, types of interfaces for exposure of network slice. Further, the study item also highlights a use cases and scenario of exposure of network slice as a service, wherein RAN slice is offered as a product to CSP. This informative clause reuses the concepts defined in 3GPP 28.824 [i.7] and investigate the O-RAN specific impacts.

3GPP TR 28.811 [i.8]: Study on the network slice management enhancements. This study item covers potential enhancements to slice management such as multi-operator relationships in network slice management, concepts like roaming, network slice isolation, edge computing, network slice specific authentication, management data isolation for different Network Slice Consumers (NSCs). One relevant scenario considered in the study item is network slice using multiple networks scenario which highlights two potential options – a) Solution based on Network Slice as a Service (NSaaS) – enhancements to NetworkSlice IOC or new ExternalNetworkSlice IOC and b) Solution based on Network Slice Subnet as a Service (NSSaaS) - enhancements to NetworkSliceSubnet IOC or new ExternalNetworkSliceSubnet IOC.

3GPP TR 28.801 [i.3]: Study on management and orchestration of network slicing for next generation network. Clause 5.1.8.2 describes the scenario of creating an end-to-end network slice instance across multiple operators. Similarly, clause 5.1.9 describes a scenario of limited level of management exposure for multiple network slice instances.

3GPP TR 23.700-99 [i.9]: Study on Network Slice Capability Exposure for Application Layer Enablement (NSCALE). This study identifies key issues, solutions, and potential requirements to enable exposure of network slice management capabilities applied to vertical industries (exposure to application function). This study item highlights some key requirements that may be relevant for the external management of O-RAN slice subnet – such as the ones described in clause 4.1.1 [i.9] - The application enablement layer should support interaction with 3GPP network management system to consume network slice management service.

# D.1.2 Concepts of management services exposure for multi-operator slice

This clause summarizes the key concepts related to management services exposure for multi-operator slice. These concepts build on those already defined in 3GPP TR 28.824 [i.7].

exposed Management Service (eMnS): The SMO has a certain set of capabilities. Some of the capabilities of the SMO need to be exposed northbound.   
• eMnS producer: The logical function of SMO that provides management service that can be consumed by an eMnS consumer.   
eMnS consumer: The logical entity outside the administrative and trust boundaries of SMO that consumes exposed management service.   
• MnS producer: The logical function of SMO that provides management service(s) that can be discovered and consumed within a MNO's administrative and trust boundaries.   
• eMnS exposure: Set of procedures that make available management service in SMO for external consumer. This can include registration of service producers in external exposure functions, publishing of a management service for external exposure, authentication, and authorization of eMnS consumer, discovery of required eMnS based on selection criteria defined by eMnS consumer.   
• eMnS discovery: Discovery of the eMnS producer management services by an eMnS consumer based on its selection criteria.   
• SMO external exposure functions: Abstract notion to be used in use cases and scenarios description consolidating SMO services providing capabilities to support eMnS exposure and potentially other similar services. SMO external exposure function is used as an example to logically represent this set of capabilities.

NOTE 1: The discovery service can be realized using either an existing service discovery functions in SMO or to be defined new SMO external exposure functions or a gateway function as defined in 3GPP 28.533 [i.18] like EGMF. The exposure of eMnS capabilities may also adopt the approach in 3GPP TR 23.700-99 [i.9] leveraging the Network Slice Capability Enablement Server (NSCE-S) in combination with EGMF.

NOTE 2: Since SMO external exposure function is not limited to eMnSs related to RAN network slicing, it is assumed to be addressed within the scope of WG1 Architecture work and is not supposed to be formally defined in this specification. An extensive functional description is beyond the scope of this specification. Some potential references for realizing the functionality of SMO external exposure functions are – CAPIF (3GPP TS 23.222 [i.5], 29.222 [i.6]), EGMF (3GPP 28.533 [i.18]) etc.

Operator business roles:

o Managed Network Operator (MNO): provides or consumes management services related to RAN slicing.   
o E_NSSMS_C (External consumer of MnS related to RAN slicing): Operator who discovers and consumes eMnSs related to RAN slicing.   
o E_NSSMS_P (Provider of external MnS related to RAN slicing): Operator who is exposes and provides eMnSs related to RAN slicing.

# D.1.3 Management aspects of external exposure of MnS related to RAN slicing

# D.1.3.1 General

External exposure of MnS related to RAN slicing may be treated as a particular case of the generic service exposure existing in the industry and covered in standard specifications like 3GPP Common API Framework [i.5], [i.6]. Therefore, many aspects related to generic exposure architecture may be applicable to the the external exposure of MnS related to RAN slicing case as well.

According to 3GPP CAPIF framework, clear separation of registry specific aspects and service specific aspects is recommended in functional model, architecture, and procedures. In CAPIF architecture the CAPIF core function consolidates all registry specific aspects and enable service APIs from both the MNO trust domain and the 3rd party trust domain having business relationship with MNO, while service specific aspects are covered by API provider functions (API Exposing Function (AEF), API Publishing Function (APF) and API Management Function (AMF)).

Similarly, management of external exposure of MnS related to RAN slicing would include two categories of aspects:

related to service specific aspects (i.e., actual processing of service requests to exposed management services (eMnSs) from E_NSSMS_C e.g., service endpoint termination, throttling, translation between external and internal information, re-exposure of service operations and events, topology hiding, routing, etc.) related to registry and catalog specific aspects (i.e., capabilities to manage various data records and profiles to support registration, discovery, publishing, identity management, authentication, authorization, access policies, data translation rules, topology hiding policies etc.)

While the CAPIF framework helps to reuse registry specific capabilities for various API exposure scenarios, it presumes decomposed architecture with additional interactions between CAPIF Core Function (CCF) and API provider functions (AEF, APF, AMF) which adds more complexity and need not to be always preferred.

With regards to possible impact on capabilities of SMO management services, at least two alternative options can be considered for management of external exposure of MnS related to RAN slicing:

Option 1: Consolidation of exposure capabilities (see figure D.1.3.1-1). Internal SMO management services are offloaded from capabilities of external exposure as much as possible, i.e., service-related aspects are as well managed by dedicated category of SMO external exposure services.

![](images/fb66725c8a75d03c552a39f14f859f369d9ae8b1ab3cb447d643cc3c6f2760f6.jpg)

> **Image Summary:** (Summary not available)
  
Figure D.1.3.1-1: Option 1: Consolidation of exposure capabilities

Option 2: Decomposition of exposure capabilities (see figure D.1.3.1-2). Internal SMO management services are aware of exposure and enriched with at least service specific aspects to proceed requests from external consumer of MnS related to RAN slicing following identity and policy information managed in SMO external exposure services responsible for registry specific aspects.

![](images/e332057a108e8675091551f2fe0c826e1a6620eed17e486606ddbc9a6740b32d.jpg)

> **Image Summary:** (Summary not available)
  
Figure D.1.3.1-2: Option 2: Decomposition of exposure capabilities

NOTE: CAPIF is originated out of 3GPP SA6 WG (application enablement and critical communication applications group for vertical markets) and 3GPP CT WG3 (design and specification of the Northbound APIs between the vertical application servers and the core network) which are not dedicated to management specifications design. Management specifications design is in responsibility of 3GPP SA5 WG (Management, Orchestration and Charging for 3GPP systems)

SA5 WG gives high level definition [i.18] of Exposure Governance Management Function (EGMF) as a management function with the role of management service exposure governance (i.e., abstraction, simplification, filtering, etc.). Functional model and requirements are not yet defined for EGMF. 3GPP conducts the study ([i.7] not yet finalized) suggesting possible roles of EGMF and possible solutions for combined CAPIF/EGMF architecture applied to management domain. One of the considered architectures is where EGMF consolidates the registry specific functions (CAPIF core function) and API provider domain functions.

# D.1.4 Multi-operator slice: High-level use cases and potential requirements for exposure fo MnS related to O-RAN slicing

As noted above, the term “multi-operator slice” is used here to represent a concept of end-to-end network slice that uses O-RAN slice subnet instances (collected group of RAN objects related to network slicing) provided by MNO in shared RAN resources. As needed, the partner operator would define its PLMN specific network slice (as per 3GPP TS 23.501 [2], slice is identified by S-NSSAI within specific PLMN ID but not multiple PLMN IDs) in that end-to-end slice.

This clause provides the high-level use cases and potential requirements for controlled external exposure of of MnS related to RAN slicing.

# D.1.4.1 Registration of producers of MnSs related to RAN slicing for external exposure

# D.1.4.1.1 Background and goal of the use case

In order to expose MnS related to RAN slicing externally SMO functions responsible for external exposure (SMO external exposure functions) need to be aware of producer of these services in SMO. This can be achieved by registering producers of respective MnSs in SMO external exposure functions.

# D.1.4.1.2 Description

# Pre-condition

There are existing trust relations between SMO external exposure functions and SMOF that is a producer of MnS related to RAN slicing.

SMOF can reach SMO external exposure services (as one of the possibilities, SMOF gets informed of SMO external exposure services capabilities and service end-points through preliminary registration of SMO external exposure functions as a producer of SMO external exposure services in SMOF responsible for service registration and management).

NOTE: SMOF responsible for service registration and management is not yet formally defined in SMO architecture.

SMOF playing a role of a producer of MnS related to RAN slicing determines its MnSs are required to be exposed externally.   
SMO function responsible for external exposure does not have information about the producer of MnSs related to RAN slicing.

# High level procedure (see figure D.1.4.1.2-1)

1. SMOF playing a role of a producer of MnS related to RAN slicing requests SMO external exposure services to register its MnSs.   
2. SMO external exposure services producer creates registry record for the producer of MnSs related to RAN slicing containing data about available MnSs and additional data (e.g., id, end-point URIs, MnS producer profile with supported MnSs, load level, heartbeat etc).   
3. SMO external exposure services producer acknowledges the successful registration or failure. SMO external exposure function may subscribe to SMOF status or SMOF sets pushing status heartbeat.

![](images/8ce68b74a7397fc7fe765093b5a050c73413ae5c56d05c0605d076c386ce445e.jpg)

> **Image Summary:** (Summary not available)
  
Figure D.1.4.1.2-1. Flow of registration of MnS related to RAN slicing for external exposure

SMO external exposure services producer has created the registry record for a producer of MnS related to RAN slicing.

# D.1.4.1.3 Potential requirements

REQ-SL-EXP-FUNxx SMO should support a capability to register MnSs that are required to be exposed externally.

REQ-SL-EXP-FUNxx SMO should support a capability to discover the MnS of the function that provides registration for MnSs that are required to be exposed externally.

REQ-SL-EXP-FUNxx SMO should support a capability to store, query, update, and deliver information about producer of MnSs that can be exposed externally.

Editor’s note: The above requirements are intentionally not yet numbered and will be numbered if/when they become normative requirements.

# D.1.4.2 Discovery of producers of MnS related to RAN slicing for external exposure

# D.1.4.2.1 Background and goal of the use case

In order to expose capabilities of MnS related to RAN slicing externally SMO external exposure functions need to be aware of producer of these services in SMO. This can be achieved by discovering producers of respective MnSs by querying SMOF responsible for service registration and management and providing common registration service to MnSs).

NOTE: SMOF responsible for service registration and management is not yet formally defined in SMO architecture.

# D.1.4.2.2 Description

# Pre-condition

There are existing trust relations between SMO external exposure function and SMOF responsible for service registration and management.   
• SMO external exposure function can reach SMOF responsible for service registration and management.   
• SMOF playing the role of a producer of MnS related to RAN slicing registered its MnSs in SMOF responsible for service registration and management. SMO external exposure function determines MnSs that are required to be exposed externally.   
• SMO external exposure function does not have information of the producer of MnSs that are required to be exposed externally.

# High level procedure (see figure D.1.4.2.2-1)

1. SMO external exposure function requests SMOF responsible for service registration and management to discover a producer of specific MnSs by providing filter criteria.   
2. SMOF responsible for service registration and management applies filter criteria to the existing registry records for MnS producers.   
3. SMOF responsible for service registration and management provides response with details on producers of matching MnSs.

![](images/914d832add723620e7281062cc942dd880cbf02f1a1798c669700c0108b250eb.jpg)

> **Image Summary:** (Summary not available)
  
Figure D.1.4.2.2-1: Flow of discovery of MnS related to RAN slicing for external exposure

# Post-condition

SMO external exposure function has obtained the registry records for a producer of the MnSs that are required to be exposed externally as per requested filter criteria.

# D.1.4.2.3 Potential requirements

REQ-SL-EXP-FUNxx SMO should support a capability for an authorized SMOF to discover MnSs that are required to be exposed externally.

REQ-SL-EXP-FUNxx SMO should support a capability for an authorized SMOF to obtain information about MnSs that are required to be exposed externally based on criteria specified by that SMOF.

Editor’s note: The above requirements are intentionally not yet numbered and will be numbered if/when they become normative requirements.

# D.1.4.3 Registration of eMnS consumer

# D.1.4.3.1 Background and goal of the use case

A consumer outside the trust and administrative boundary of the SMO needs to be authenticated and authorized using the identity data of the consumer in order to allow acess to exposed management services. Consumer identity data needs to be registered at SMO. Traditionally, in the industry, registration is performed manually at producer side. It may also be performed automatically. Automatic registration presumes mechanisms for secured communication, for instance, certificate check and ecryption based on server (SMO) certificate. Registration capabilities also presume management of records containing consumer account data including but not limited to consumer credentials, consumer roles and rights it is authorized to.

NOTE: In case of manual registration, consumer details corresponding to the registration are created through SMO operational procedures initiated by a human operator. By completion of registration procedures exposed management services consumer is provided with credentials and is aware of authentication method and access rights.

# D.1.4.3.2 Description

# Pre-condition

eMnS consumer can reach SMO external exposure.   
SMO function responsible for external exposure does not have consumer account data record for eMnS consumer.   
1. eMnS consumer requests SMO external exposure services to register itself and provides information about intended scope of management services to consume.   
2. SMO external exposure services producer performs eligibility check based on provided by eMnS consumer information and makes a descision on request approval.   
3. In case of positive result, SMO external exposure services producer creates registry record for the eMnS consumer containing data about intended and authorized management services to consume, credentials and authentication method.   
4. SMO external exposure services producer acknowledges the successful registration and provide credentials data to eMnS. eMnS consumer may subscribe to status of SMO external exposure function or SMO external exposure function sets pushing status heartbeat.

![](images/d99626827c37f6fa6400804c9589874ca76bdfad6193083d85b3e0adf3fc6275.jpg)

> **Image Summary:** (Summary not available)
  
Figure D.1.4.3.2-1: Flow of registration of consumer of eMnS related to RAN slicing

# Post-condition

SMO external exposure function has created the consumer account data record for the eMnS consumer and eMnS consumer has received registration confirmation with required data.

# D.1.4.3.3 Potential requirements

REQ-SL-EXP-FUNxx SMO should support a capability to register a consumer of exposed management services.

REQ-SL-EXP-FUNxx SMO should support a capability to manage lifecycle of account data record (creation, modification, deletion) of a consumer of exposed management services.

REQ-SL-EXP-FUNxx SMO should support a capability to manage credentials, related roles, and authorized access rights of a consumer of exposed management services.

REQ-SL-EXP-FUNxx SMO should support a capability for an authorized SMOF to store, query, update, and deliver information about consumer of exposed management services.

Editor’s note: The above requirements are intentionally not yet numbered and will be numbered if/when they become normative requirements.

# D.1.4.4 Authentication and authorization of eMnS consumer

# D.1.4.4.1 Background and goal of the use case

In order consumer of exposed management services be authenticated and authorized to consume intended scope of MnSs, SMO external exposure functions need to support authentication and authorization processes capabilities relying on identity and authorized rights for the eMnS consumer created during its registration.

NOTE: Authentication procedures shall comply with all the security requirements as specified in O-RAN.WG11.SecurityProtocols-Specification [24].

# D.1.4.4.2 Description

# Pre-condition

There are existing trust relations between SMO external exposure functions and eMnS consumer.   
eMnS consumer can reach SMO external exposure.   
SMO function responsible for external exposure has consumer account data record for eMnS consumer including credentials, roles, and authorized access rights.

# High level procedure (see figure D.1.4.4.2-1)

1. eMnS consumer initiates authentication by providing its credentials and information on security capabilities to SMO external exposure function.   
2. SMO external exposure function selects security method and performs mutual authentication with eMnS consumer.   
3. After receiving successful authentication response eMnS consumer may request for permission to access certain exposed management services (otherwise decision on access permission is made based on previously stored data)   
4. SMO external exposure function checks access rights in registry record for eMnS consumer and sends authorization response containg access token and scope defining allowed for eMnS consumer exposed management services.

![](images/fbfc476f8243c21e7dbb7bfe6eec49f4956d829211d7dbaf67e7249dc5bf9a11.jpg)

> **Image Summary:** (Summary not available)
  
Figure D.1.4.4.2-1: Flow of authentication and authorization of eMnS consumer

SMO external exposure function has authenticated and authorized eMnS consumer to access allowed scope of exposed management services.

# D.1.4.4.3 Potential requirements

REQ-SL-EXP-FUNxx SMO should support a capability for mutual authentication between SMO and consumer of exposed management services.

REQ-SL-EXP-FUNxx SMO should support a capability for authorization of consumer of exposed management services.

REQ-SL-EXP-FUNxx SMO should support internal to SMO capability to create, read, update, and delete authorization policies related to exposed management services.

Editor’s note: The above requirements are intentionally not yet numbered and will be numbered if/when they become normative requirements.

# D.1.4.5 Publishing of eMnS

# D.1.4.5.1 Background and goal of the use case

For an eMnS consumer to consume eMnS, the eMnS needs to be defined, created, and activated in SMO as available for requests from outside the administrative and trust boundaries of SMO. It is also necessary to implement and apply access constraint policies (e.g. access rights, requests rate limitations) to eMnS in accordance with the previous business agreement between E_NSSMS_C and E_NSSMS_P.

The eMnS definition relies on the capabilities of MnSs related to RAN slicing that are registered in SMO external exposure services. The definition includes sufficient information for eMnS consuming (e.g. public endpoint URI, version, metadata, protocol, authentication method, resource URIs, operations and their parameters, data format).

Depending on the use case eMnS may be associated with MnS either directly or indirectly. In case of indirect association eMnS may be an aggregation of a set of MnSs, of a subset of MnS capabilities or group of several MnS subsets.

eMnS may also be an abstraction formed by transformation to specific external data models, mapping, filtering and enrichment for data and operations of supporting MnSs, in that case publishing may also cover how eMnS is formed.

NOTE: For the given use case direct association of eMnS to MnS is assumed.

In general, service publishing includes manual activities that may be streamlined using various DevOps automation tools in conjunction with workflow management systems.

# D.1.4.5.2 Description

Pre-condition

Business agreement between E_NSSMS_C and E_NSSMS_P exists. SMO external exposure function uses account information of eMnS consumer to authenticate and authorize it.   
• SMO external exposure function has information about scope of management services eMnS consumer intends to consume.   
• SMO external exposure function has the registry records for producers of MnS related to RAN slicing that may be exposed externally.

# High level procedure

1. SMO administrator gets a task to make a new eMnS available for the E_NSSMS_C.

2. SMO administrator using various DevOps automation tools defines and create eMnS deployment package within SMO external exposure functions.

3. SMO administrator following business agreement information, information in eMnS consumer account data record and eMnS consumer intended scope of consumed management services defines and stores within SMO external exposure function access constraint policies to be applied to the eMnS consumer for the newly created eMnS.

4. SMO administrator deploys and activates an instance of eMnS for it to be available for for the requests from the outside the administrative and trust boundaries of SMO and task of eMnS publishing is reported as completed.

# Post-condition

eMnS deployment package is prepared and created within SMO external exposure functions. Access constraint policies to be applied to the eMnS consumer for the newly created eMnS are prepared and created within SMO external exposure functions. An instance of eMnS based on eMnS definition package is deployed and activated within SMO and is available for the consumption by the eMnS consumer from the outside of the administrative and trust boundaries of SMO.

NOTE: Depending on the progress of De-Coupled SMO or specific implementation need, these capabilities may reside in one of the SMO functions or realized with support of rApps.

# D.1.4.5.3 Potential requirements

REQ-SL-EXP-FUNxx SMO should support a capability to manage lifecycle (creation, modification, deletion) of the exposed management service deployment package that includes sufficient information for consuming that exposed management service (e.g. including but not limited to public endpoint URI, version, metadata, protocol, authentication method, resource URIs, operations and their parameters, data format).

REQ-SL-EXP-FUNxx SMO should support a capability to manage lifecycle of the access constraint policies (access rights, requests rate limits and other) to be applied to the exposed management service consumer for the exposed management service consumption.

REQ-SL-EXP-FUNxx SMO should support a capability to manage lifecycle (creation, modification, deletion) of the exposed management service instance.

Editor’s note: The above requirements are intentionally not yet numbered and will be numbered if/when they become normative requirements.

# D.1.4.6 Discovery of eMnS

# D.1.4.6.1 Background and goal of the use case

For the consumer of exposed management services to be aware of eMnS that are available for consumption, the external exposure function of the SMO needs to be able to support the capability and process of eMnS discovery. For eMnS to be discovered it needs first to be published. Discovery is provided to the authorized consumers of exposed management services.

Upon discovery, the consumer of exposed management services obtains information on producers and available instances of eMnSs, including service access information for each producer. It may also contain specific instructions on how requests data are expected to be secured and formatted.

A consumer of exposed management may discover available eMnS with a specific query containing filter criteria to SMO external exposure function or by getting a notification from SMO external exposure function on available eMnS matching notification subscription criteria.

NOTE: Access to discovery capabilities of SMO may be in itself a subject for the access constraint policies.

# D.1.4.6.2 Description

Pre-condition

There are existing trust relations between SMO external exposure function and eMnS consumer.   
eMnS consumer can reach SMO external exposure. SMO external exposure function has consumer account data record for eMnS consumer including credentials, roles, and authorized access rights.   
• eMnS instances are published.   
eMnS consumer does not have information about published eMnS instances or deems the previously stored information needs to be updated.

# High level procedure (see figure D.1.4.6.2-1)

1. eMnS consumer requests SMO external exposure function to discover a producer of specific eMnSs by providing filter criteria.   
2. SMO external exposure function applies filter criteria to the existing instances of eMnSs and its producers.   
3. SMO external exposure function provides a response with information on producers of matching eMnSs and available instances of eMnSs.

![](images/9011d6ec3cfba629ff7c81eb13e4a3718da905e0fe868343fbf1665b2a878409.jpg)

> **Image Summary:** (Summary not available)
  
Figure D.1.4.6.2-1: Flow of discovery of eMnS by eMnS consumer

# Post-condition

eMnS consumer has an updated information about published eMnS instances it is able to consume.

# D.1.4.6.3 Potential requirements

REQ-SL-EXP-FUNxx SMO should support a capability for an authorized consumer of exposed management services to discover published exposed management services.

REQ-SL-EXP-FUNxx SMO should support a capability for an authorized consumer of exposed management services to obtain information about published exposed management services based on criteria specified by that consumer of exposed management services.

REQ-SL-EXP-FUNxx SMO may support capability for an authorized consumer of exposed management services to subscribe to discovery events, get notifications (for example: update, removal, or creation of exposed management service instance in the scope of subscription) and to request health check.

Editor’s note: The above requirements are intentionally not yet numbered and will be numbered if/when they become normative requirements.

# Annex (informative): Change history/Change request (history)

<table><tr><td colspan="1" rowspan="1">Date</td><td colspan="1" rowspan="1">Revision</td><td colspan="1" rowspan="1">Description</td></tr><tr><td colspan="1" rowspan="1">2019.11.13</td><td colspan="1" rowspan="1">01.00.00</td><td colspan="1" rowspan="1">Draft for template</td></tr><tr><td colspan="1" rowspan="1">2020.01.02</td><td colspan="1" rowspan="1">01.00.01</td><td colspan="1" rowspan="1">Addition of slicing overview, RAN slice SLA assurance use case, general principles</td></tr><tr><td colspan="1" rowspan="1">2020.01.08</td><td colspan="1" rowspan="1">01.00.02</td><td colspan="1" rowspan="1">Addition of initial requirements and architecture overview</td></tr><tr><td colspan="1" rowspan="1">2020.01.13</td><td colspan="1" rowspan="1">01.00.03</td><td colspan="1" rowspan="1">Addition of reference slicing architecture section</td></tr><tr><td colspan="1" rowspan="1">2020.01.21</td><td colspan="1" rowspan="1">01.00.04</td><td colspan="1" rowspan="1">Addition of A1/E2/O1/O2 sections and updates to reference slicing architecture section,updates to references, abbreviations</td></tr><tr><td colspan="1" rowspan="1">2020.02.04</td><td colspan="1" rowspan="1">01.00.05</td><td colspan="1" rowspan="1">Addition of generic slice deployment option diagram/section, 3GPP-ETSl implementation,updated reference slicing architecture,</td></tr><tr><td colspan="1" rowspan="1">2020.02.10</td><td colspan="1" rowspan="1">01.00.06</td><td colspan="1" rowspan="1">Updated reference slicing architecture based on feedback, added notes on 3GPP 28.526VNF/PNF handling</td></tr><tr><td colspan="1" rowspan="1">2020.03.01</td><td colspan="1" rowspan="1">01.00.07</td><td colspan="1" rowspan="1">Updated architecture with SMO alignment discussion, ordered references, fixed table ofcontents issues, editorial updates</td></tr><tr><td colspan="1" rowspan="1">2020.03.11</td><td colspan="1" rowspan="1">01.00.08</td><td colspan="1" rowspan="1">Updates to various sections based on review feedback during WG1 approval process</td></tr><tr><td colspan="1" rowspan="1">2020.03.11</td><td colspan="1" rowspan="1">01.00</td><td colspan="1" rowspan="1">Final version 01.00</td></tr><tr><td colspan="1" rowspan="1">2020.04.20</td><td colspan="1" rowspan="1">02.00.01</td><td colspan="1" rowspan="1">Initial version of v2.0Document version number update to v02.00.01</td></tr><tr><td colspan="1" rowspan="1">2020.06.26</td><td colspan="1" rowspan="1">02.00.02</td><td colspan="1" rowspan="1">Addition of slice subnet management and provisioning use cases and requirements:NET.AO-2020.06.25-WG1-CR-0100-SliceManagementUseCases</td></tr><tr><td colspan="1" rowspan="1">2020.06.27</td><td colspan="1" rowspan="1">02.00.03</td><td colspan="1" rowspan="1">Addition of multi-vendor slices use case:KDDI.AO-2020.06.26-WG1-CR-0100-MultiVendorSlice-UC-CR-Summary</td></tr><tr><td colspan="1" rowspan="1">2020.06.27</td><td colspan="1" rowspan="1">02.00.04</td><td colspan="1" rowspan="1">Addition of NSsI resource allocation optimization use case:INT.AO-2020.06.25-WG1-CR-0100-NSSI-Rsrc-Opt-UC-CR-Summary</td></tr><tr><td colspan="1" rowspan="1">2020.06.28</td><td colspan="1" rowspan="1">02.00.05</td><td colspan="1" rowspan="1">Editorial changes, corrections</td></tr><tr><td colspan="1" rowspan="1">2020.07.13</td><td colspan="1" rowspan="1">02.00.06</td><td colspan="1" rowspan="1">Updates per WG1 review process:Correct reference numbers in section 3.1Correct minor mistakes/editorial updatesAdd handling of TN segment to modification and feasibility check use casesClarification updates to Requirements 13, 15</td></tr><tr><td colspan="1" rowspan="1">2020.07.16</td><td colspan="1" rowspan="1">02.00.07</td><td colspan="1" rowspan="1">Getting the version ready to be published externally (removal of trackchanges/comments)</td></tr><tr><td colspan="1" rowspan="1">2020.07.16</td><td colspan="1" rowspan="1">02.00</td><td colspan="1" rowspan="1">Final version 02.00</td></tr><tr><td colspan="1" rowspan="1">2020.10.22</td><td colspan="1" rowspan="1">03.00.01</td><td colspan="1" rowspan="1">Initial version of v3.0Document version number update to v03.00.01</td></tr><tr><td colspan="1" rowspan="1">2020.11.02</td><td colspan="1" rowspan="1">03.00.02</td><td colspan="1" rowspan="1">Addition of CR:</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Editorial updates</td></tr><tr><td colspan="1" rowspan="1">2020.11.13</td><td colspan="1" rowspan="1">03.00.03</td><td colspan="1" rowspan="1">Updates based on WG1 review comments</td></tr><tr><td colspan="1" rowspan="1">2020.11.13</td><td colspan="1" rowspan="1">03.00</td><td colspan="1" rowspan="1">Final version 03.00</td></tr><tr><td colspan="1" rowspan="1">2021.03.02</td><td colspan="1" rowspan="1">04.00.01</td><td colspan="1" rowspan="1">Initial version of v4.0Document version number update to v04.00.01</td></tr><tr><td colspan="1" rowspan="1">2021.03.06</td><td colspan="1" rowspan="1">04.00.02</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2021.03.01-WG1-CR-0001-Slicing_Transport_Networks_Section-v01</td></tr><tr><td colspan="1" rowspan="1">2021.03.06</td><td colspan="1" rowspan="1">04.00.03</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2021.03.01-WG1-CR-0002-O-RAN-Slicing-ONSSI-Allocation-v01</td></tr><tr><td colspan="1" rowspan="1">2021.03.06</td><td colspan="1" rowspan="1">04.00.04</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2021.03.01-WG1-CR-0003-O-RAN-Slicing-ONSSI-Deallocation-v01</td></tr><tr><td colspan="1" rowspan="1">2021.03.13</td><td colspan="1" rowspan="1">04.00</td><td colspan="1" rowspan="1">Final version 04.00</td></tr><tr><td colspan="1" rowspan="1">2021.07.10</td><td colspan="1" rowspan="1">05.00.01</td><td colspan="1" rowspan="1">Initial version of v5.0Document version number update to v05.00.01</td></tr><tr><td colspan="1" rowspan="1">2021.07.11</td><td colspan="1" rowspan="1">05.00.02</td><td colspan="1" rowspan="1">Addition of CR:RBBN.AO-2021.06.25-WG1-CR-0001-Annex-TN-Slicing-v06</td></tr><tr><td colspan="1" rowspan="1">2021.07.12</td><td colspan="1" rowspan="1">05.00.03</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2021.05.31-WG1-CR-0004-O-RAN-Slicing-ONSSI-Modification-v02</td></tr><tr><td colspan="1" rowspan="1">2021.07.19</td><td colspan="1" rowspan="1">05.00</td><td colspan="1" rowspan="1">Final version 05.00</td></tr><tr><td colspan="1" rowspan="1">2021.11.11</td><td colspan="1" rowspan="1">06.00.01</td><td colspan="1" rowspan="1">Initial version of v6.0Document version number update to v06.00.01</td></tr><tr><td colspan="1" rowspan="1">2021.11.12</td><td colspan="1" rowspan="1">06.00.02</td><td colspan="1" rowspan="1">Addition of relevant parts of CR:NC.AO-2021.07.20-WG1-CR-0001-NSSIResourceAllocationWithQuota-v04</td></tr><tr><td colspan="1" rowspan="1">2021.11.12</td><td colspan="1" rowspan="1">06.00.03</td><td colspan="1" rowspan="1">Correction of terminology used in NSSI optimization use case</td></tr><tr><td colspan="1" rowspan="1">2021.11.14</td><td colspan="1" rowspan="1">06.00.04</td><td colspan="1" rowspan="1">Addition of CR:NOK.AO.2021.10.13-WG1-NetworkSlicingArchitecture-TerminologyAwarenessEditorial updates to Appendix C</td></tr><tr><td colspan="1" rowspan="1">2021.11.14</td><td colspan="1" rowspan="1">06.00.05</td><td colspan="1" rowspan="1">Clean version for WG1 approval</td></tr><tr><td colspan="1" rowspan="1">2021.11.23</td><td colspan="1" rowspan="1">06.00.06</td><td colspan="1" rowspan="1">Updates to address WG1 review comments</td></tr><tr><td colspan="1" rowspan="1">2021.11.23</td><td colspan="1" rowspan="1">06.00</td><td colspan="1" rowspan="1">Final version 06.00</td></tr><tr><td colspan="1" rowspan="1">2022.03.26</td><td colspan="1" rowspan="1">06.00.07</td><td colspan="1" rowspan="1">Adopted new spec revision numbering per O-RAN Work ProceduresInitial version towards v07.00, starting with v06.00.07 per new revision numbering</td></tr><tr><td colspan="1" rowspan="1">2022.03.26</td><td colspan="1" rowspan="1">06.00.08</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2022.03.14-WG1-CR-0005-O-RAN-Slicing-ONSSI-Provisioning-WG6Details</td></tr><tr><td colspan="1" rowspan="1">2022.03.26</td><td colspan="1" rowspan="1">06.00.09</td><td colspan="1" rowspan="1">Addition of CR:RBBN.AO-2022.03.02-WG1-CR-0001-Annex-TN-Slicing-v02</td></tr><tr><td colspan="1" rowspan="1">2022.03.26</td><td colspan="1" rowspan="1">06.00.10</td><td colspan="1" rowspan="1">Changes accepted from v06.00.09Baseline for WG1 approval</td></tr><tr><td colspan="1" rowspan="1">2022.04.04</td><td colspan="1" rowspan="1">07.00</td><td colspan="1" rowspan="1">Final version 07.00</td></tr><tr><td colspan="1" rowspan="1">2022.07.24</td><td colspan="1" rowspan="1">07.00.01</td><td colspan="1" rowspan="1">Initial version towards v08.00, starting with v07.00.01 per O-RAN specification revisionnumbering process</td></tr><tr><td colspan="1" rowspan="1">2022.07.25</td><td colspan="1" rowspan="1">07.00.02</td><td colspan="1" rowspan="1">Addition of CR:NC.AO-2022.05.02-WG1-NC-0004-MultiOperatorRANSliceSubnetAnnexure-v02Editorial updates and corrections</td></tr><tr><td colspan="1" rowspan="1">2022.07.25</td><td colspan="1" rowspan="1">07.00.03</td><td colspan="1" rowspan="1">Update of the document to comply with the new O-RAN Technical Spec template</td></tr><tr><td colspan="1" rowspan="1">2022.07.25</td><td colspan="1" rowspan="1">07.00.04</td><td colspan="1" rowspan="1">All changes accepted, clean version for WG1 approval</td></tr><tr><td colspan="1" rowspan="1">2022.08.01</td><td colspan="1" rowspan="1">08.00</td><td colspan="1" rowspan="1">Final version 08.00</td></tr><tr><td colspan="1" rowspan="1">2022.11.10</td><td colspan="1" rowspan="1">08.00.01</td><td colspan="1" rowspan="1">Initial version towards v09.00, starting with v08.00.01 per O-RAN specification revisionnumbering processAddition of CR:NC.AO-2022.05.02-WG1-NC-0004-MultiOperatorSliceAnnexure-v04</td></tr><tr><td colspan="1" rowspan="1">2022.11.10</td><td colspan="1" rowspan="1">08.00.02</td><td colspan="1" rowspan="1">Addition of CR:NC.AO-2022.05.02-WG1-NC-0005-MultiOperatorSliceAnnexure-v04</td></tr><tr><td colspan="1" rowspan="1">2022.11.10</td><td colspan="1" rowspan="1">08.00.03</td><td colspan="1" rowspan="1">Addition of CR:NOK.AO-2022.10.14-WG1-CR-0000-NetworkSlicing-Editorials-v02</td></tr><tr><td colspan="1" rowspan="1">2022.11.13</td><td colspan="1" rowspan="1">08.00.04</td><td colspan="1" rowspan="1">Added O-RAN Release "R003" to document name, updated copyright to 2023 as thedocument will be published externally in 2023.All changes accepted, clean version for WG1 approval</td></tr><tr><td colspan="1" rowspan="1">2022.11.18</td><td colspan="1" rowspan="1">09.00</td><td colspan="1" rowspan="1">Final version 09.00</td></tr><tr><td colspan="1" rowspan="1">2023.03.14</td><td colspan="1" rowspan="1">09.00.01</td><td colspan="1" rowspan="1">Initial version towards v10.00, starting with v09.00.01 per O-RAN specification revisionnumbering process.Update of the spec to latest O-RAN TS template except for splitting the references toformative and informative. This split is planned to be made in next release of thedocument.</td></tr><tr><td colspan="1" rowspan="1">2023.03.14</td><td colspan="1" rowspan="1">09.00.02</td><td colspan="1" rowspan="1">Addition of CR:NC.AO-2022.12.05-WG1-CR-0007-ExtMnSConsumerRegistration&amp;AA-v02</td></tr><tr><td colspan="1" rowspan="1">2023.03.14</td><td colspan="1" rowspan="1">09.00.03</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.03.14-WG1-CR-0007-O-RAN-Slicing-Arch-Annex_Editorials-v01</td></tr><tr><td colspan="1" rowspan="1">2023.03.14</td><td colspan="1" rowspan="1">09.00.04</td><td colspan="1" rowspan="1">All changes accepted, clean version for WG1 approval</td></tr><tr><td colspan="1" rowspan="1">2023.03.24</td><td colspan="1" rowspan="1">09.00.05</td><td colspan="1" rowspan="1">WG1 review comments are addressed, and approval is completed. Ready for TSCapproval and publication.</td></tr><tr><td colspan="1" rowspan="1">2023.03.24</td><td colspan="1" rowspan="1">10.00</td><td colspan="1" rowspan="1">Final version 10.00</td></tr><tr><td colspan="3" rowspan="1">A L    AN CE</td></tr><tr><td colspan="1" rowspan="1">2023.04.27</td><td colspan="1" rowspan="1">10.00.01</td><td colspan="1" rowspan="1">Initial version towards v11.00, starting with v10.00.01 per O-RAN specification revisionnumbering process.Addition of CR:JNPR-2023.04.10-WG1-CR-0008-O-RAN-Slicing-Arch-ODR-References-Section-v02</td></tr><tr><td colspan="1" rowspan="1">2023.04.25</td><td colspan="1" rowspan="1">10.00.02</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.04.25-WG1-CR-0009-O-RAN-Slicing-Arch-ODR-References-Update-v01</td></tr><tr><td colspan="1" rowspan="1">2023.05.09</td><td colspan="1" rowspan="1">10.00.03</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.05.09-WG1-CR-0014-O-RAN-Slicing-Arch-ODR-References-Correction-v01</td></tr><tr><td colspan="1" rowspan="1">2023.05.09</td><td colspan="1" rowspan="1">10.00.04</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.05.09-WG1-CR-0015-O-RAN-Slicing-Arch-ODR-References-Section-v01</td></tr><tr><td colspan="1" rowspan="1">2023.05.09</td><td colspan="1" rowspan="1">10.00.05</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.05.09-WG1-CR-0016-O-RAN-Slicing-Arch-ODR-References-Update-v01</td></tr><tr><td colspan="1" rowspan="1">2023.05.11</td><td colspan="1" rowspan="1">10.00.06</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.05.09-WG1-CR-0017-O-RAN-Slicing-Arch-ODR-References-Wording-v02</td></tr><tr><td colspan="1" rowspan="1">2023.05.23</td><td colspan="1" rowspan="1">10.00.07</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.05.23-WG1-CR-0024-O-RAN-Slicing-Arch-ODR-Figures-References_and_Wording-v01</td></tr><tr><td colspan="1" rowspan="1">2023.06.06</td><td colspan="1" rowspan="1">10.00.08</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.06.06-WG1-CR-0027-O-RAN-Slicing-Arch-ODR-Tables-References_Headings_Corrections-v01</td></tr><tr><td colspan="1" rowspan="1">2023.06.06</td><td colspan="1" rowspan="1">10.00.09</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.06.06-WG1-CR-0028-O-RAN-Slicing-Arch-ODR-Notes-v02</td></tr><tr><td colspan="1" rowspan="1">2023.06.15</td><td colspan="1" rowspan="1">10.00.10</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.06.15-WG1-CR-0034-O-RAN-Slicing-Arch-ODR-Paragraphs-Referencing-v01</td></tr><tr><td colspan="1" rowspan="1">2023.07.03</td><td colspan="1" rowspan="1">10.00.11</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.07.03-WG1-CR-0039-O-RAN-Slicing-Arch-ODR-Modal-Verbs_Shall_Shal_not_Should_Should_not_Must_Must_not-v01</td></tr><tr><td colspan="1" rowspan="1">2023.07.03</td><td colspan="1" rowspan="1">10.00.12</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.07.03-WG1-CR-0040-O-RAN-Slicing-Arch-ODR-Modal-Verbs_Can_Cannot_May_Need_not-v01</td></tr><tr><td colspan="1" rowspan="1">2023.07.20</td><td colspan="1" rowspan="1">10.00.13</td><td colspan="1" rowspan="1">Addition of CR:NEC.AO-2023.06.19-WG1-CR-0009-eMnS-Publish-and-Discovery-v02</td></tr><tr><td colspan="1" rowspan="1">2023.07.20</td><td colspan="1" rowspan="1">10.00.14</td><td colspan="1" rowspan="1">Update of the spec to latest O-RAN TS templateCorrection of font types and spacing across the spec per ODR requirementsEditorial corrections</td></tr><tr><td colspan="1" rowspan="1">2023.07.20</td><td colspan="1" rowspan="1">10.00.15</td><td colspan="1" rowspan="1">Clean version for WG1 approval</td></tr><tr><td colspan="1" rowspan="1">2023.07.27</td><td colspan="1" rowspan="1">10.00.16</td><td colspan="1" rowspan="1">WG1 review comments are addressed, and approval is completed.</td></tr><tr><td colspan="1" rowspan="1">2023.07.27</td><td colspan="1" rowspan="1">10.00.17</td><td colspan="1" rowspan="1">All changes accepted, clean version.</td></tr><tr><td colspan="1" rowspan="1">2023.07.27</td><td colspan="1" rowspan="1">11.00</td><td colspan="1" rowspan="1">Final version 11.00</td></tr><tr><td colspan="1" rowspan="1">2023.11.01</td><td colspan="1" rowspan="1">11.00.01</td><td colspan="1" rowspan="1">Initial version towards v12.00, starting with v11.00.01 per O-RAN specification revisionnumbering process.Addition of CR:JNPR-2023.11.01-WG1-CR-0042-O-RAN-Slicing-Arch-ODR-FFS-Concepts-v01</td></tr><tr><td colspan="1" rowspan="1">2023.11.01</td><td colspan="1" rowspan="1">11.00.02</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.11.01-WG1-CR-0043-O-RAN-Slicing-Arch-ODR-Terms-Abbreviations-Corrections-v01</td></tr><tr><td colspan="1" rowspan="1">2023.11.03</td><td colspan="1" rowspan="1">11.00.03</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.11.03-WG1-CR-0044-O-RAN-Slicing-Arch-ODR-Editorial-Modifications-v02</td></tr><tr><td colspan="1" rowspan="1">2023.11.07</td><td colspan="1" rowspan="1">11.00.04</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.09.08-WG1-CR-0041-O-RAN-Slicing-Arch-Review-Comments-v01</td></tr><tr><td colspan="1" rowspan="1">2023.11.08</td><td colspan="1" rowspan="1">11.00.05</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.11.07-WG1-CR-0045-O-RAN-Slicing-Arch-ODR-Modal-Verbs-v03</td></tr><tr><td colspan="1" rowspan="1">2023.11.08</td><td colspan="1" rowspan="1">11.00.06</td><td colspan="1" rowspan="1">Clean version for WG1 approval</td></tr><tr><td colspan="1" rowspan="1">2023.11.16</td><td colspan="1" rowspan="1">11.00.07</td><td colspan="1" rowspan="1">WG1 review comments are addressed, and approval is completed.</td></tr><tr><td colspan="1" rowspan="1">2023.11.16</td><td colspan="1" rowspan="1">11.00.08</td><td colspan="1" rowspan="1">All changes accepted, clean version.</td></tr><tr><td colspan="1" rowspan="1">2023.11.16</td><td colspan="1" rowspan="1">12.00</td><td colspan="1" rowspan="1">Final version 12.00</td></tr><tr><td colspan="1" rowspan="1">2023.12.07</td><td colspan="1" rowspan="1">12.00.01</td><td colspan="1" rowspan="1">Initial version towards v13.00, starting with v12.00.01 per O-RAN specification revisionnumbering process.Addition of CR:JNPR-2023.12.05-WG1-CR-0048-O-RAN-Slicing-Arch-ODR-Clauses-Text_Modifications-Editorial_Corrections-v03</td></tr><tr><td colspan="1" rowspan="1">2024.01.29</td><td colspan="1" rowspan="1">12.00.02</td><td colspan="1" rowspan="1">Addition of CR:JNPR-2023.12.27-WG1-CR-0049-O-RAN-Slicing-Arch-ODR-Capital_Letters-Editorial_Changes-V01</td></tr><tr><td colspan="1" rowspan="1">2024.03.22</td><td colspan="1" rowspan="1">12.00.03</td><td colspan="1" rowspan="1">Addition of CR:NOK.AO-2024.03.12-WG1-CR-0007-ReservationFeasibilityCheck_v01.01</td></tr><tr><td colspan="1" rowspan="1">2024.03.22</td><td colspan="1" rowspan="1">12.00.04</td><td colspan="1" rowspan="1">Clean version for WG1 approval</td></tr><tr><td colspan="1" rowspan="1">2024.03.31</td><td colspan="1" rowspan="1">12.00.05</td><td colspan="1" rowspan="1">WG1 review comments are addressed, and approval is completed.</td></tr><tr><td colspan="1" rowspan="1">2024.03.31</td><td colspan="1" rowspan="1">12.00.06</td><td colspan="1" rowspan="1">All changes accepted, clean version.</td></tr><tr><td colspan="1" rowspan="1">2024.03.31</td><td colspan="1" rowspan="1">13.00</td><td colspan="1" rowspan="1">Final version 13.00</td></tr><tr><td colspan="1" rowspan="1">2024.06.25</td><td colspan="1" rowspan="1">13.00.01</td><td colspan="1" rowspan="1">Initial version towards v14.00, starting with v13.00.01 per O-RAN specification revisionnumbering process.Addition of CR:</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">NOK.AO-2024.05.02-WG1NSTG-CR0009-ProcedureStepLeaders_v02.00</td></tr><tr><td colspan="1" rowspan="1">2024.07.05</td><td colspan="1" rowspan="1">13.00.02</td><td colspan="1" rowspan="1">Clean version for WG1 approval</td></tr><tr><td colspan="1" rowspan="1">2024.07.18</td><td colspan="1" rowspan="1">13.00.03</td><td colspan="1" rowspan="1">WG1 review comments are addressed, and approval is completed.</td></tr><tr><td colspan="1" rowspan="1">2024.07.18</td><td colspan="1" rowspan="1">13.00.04</td><td colspan="1" rowspan="1">All changes accepted, clean version.</td></tr><tr><td colspan="1" rowspan="1">2024.07.18</td><td colspan="1" rowspan="1">13.01</td><td colspan="1" rowspan="1">Final version 13.01</td></tr><tr><td colspan="1" rowspan="1">2024.10.01</td><td colspan="1" rowspan="1">13.01.01</td><td colspan="1" rowspan="1">Initial version towards next release, starting with v13.01.01 per O-RAN specificationrevision numbering process.Addition of CRs:JNPR-2024.09.17-WG1-CR-0062-O-RAN-Slicing-Arch-ETSI_PAS_Comments_for_NSI_and_NSSI_Terms-v01JNPR-2024.09.17-WG1-CR-0063-O-RAN-Slicing-Arch-ETSI_PAS_Comments_for_RAN_Slice_Subnet_and_NSSI-v01JNPR-2024.09.23-WG1-CR-0064-O-RAN-Slicing-Arch-ETSI_PAS_Comments_RAN_Slice_Subnet_entire_spec-v01JNPR-2024.09.23-WG1-CR-0065-O-RAN-Slicing-Arch-ETSI_PAS_Comments_for_NSSI_to_the_entire_spec-v01</td></tr><tr><td colspan="1" rowspan="1">2024.11.04</td><td colspan="1" rowspan="1">13.01.02</td><td colspan="1" rowspan="1">Addition of CRs:JNPR-2024.10.22-WG1-CR-0071-O-RAN-Slicing-Arch-ETSI_PAS_Comments-v01JNPR.AO-2024.10.22-WG1-CR-0072-O-RAN-Slicing-Arch-Rel-18-Upgrade-28.530-v01JNPR.AO-2024.10.22-WG1-CR-0073-O-RAN-Slicing-Arch-Rel-18-Upgrade-23.003-v01JNPR.AO-2024.10.22-WG1-CR-0074-O-RAN-Slicing-Arch-Rel-18-Upgrade-22.261-v01JNPR.AO-2024.10.22-WG1-CR-0075-O-RAN-Slicing-Arch-Rel-18-Upgrade-28.526-v01JNPR.AO-2024.10.22-WG1-CR-0076-O-RAN-Slicing-Arch-Rel-18-Upgrade-28.532-v01JNPR.AO-2024.10.22-WG1-CR-0077-O-RAN-Slicing-Arch-Rel-18-Upgrade-28.552-v01JNPR.AO-2024.10.22-WG1-CR-0078-O-RAN-Slicing-Arch-Rel-18-Upgrade-ETSI-NFV-003-v01JNPR.AO-2024.10.22-WG1-CR-0079-O-RAN-Slicing-Arch-Rel-18-Upgrade-28.801-v01JNPR.AO-2024.10.22-WG1-CR-0080-O-RAN-Slicing-Arch-Rel-18-Upgrade-23.501-v01JNPR.AO-2024.10.22-WG1-CR-0081-O-RAN-Slicing-Arch-Rel-18-Upgrade-38.300-v01JNPR.AO-2024.10.22-WG1-CR-0082-O-RAN-Slicing-Arch-Rel-18-Upgrade-28.541-v01NOK.AO-2024.06.12-WG1NSTG-CR0008-ReservationFeasibilityCheck_v01.01</td></tr><tr><td colspan="1" rowspan="1">2024.11.15</td><td colspan="1" rowspan="1">13.01.03</td><td colspan="1" rowspan="1">Addition of CRs:JNPR.AO-2024.11.05-WG1-CR-0083-O-RAN-Slicing-Arch-Rel-18-Upgrade-32.300-v01</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">JNPR-2024.11.05-WG1-CR-0084-O-RAN-Slicing-Arch-Capitalization_Clauses_Titles-v01Updated copyright statement on the cover page and footer to 2025Editorial changes to align to O-RAN TS template v02.01Added 3GPP Release 18 related text to Normative and Informative References clausesEditorial updates</td></tr><tr><td colspan="1" rowspan="1">2024.11.21</td><td colspan="1" rowspan="1">13.01.04</td><td colspan="1" rowspan="1">Clean version for WG1 approval</td></tr><tr><td colspan="1" rowspan="1">2024.12.06</td><td colspan="1" rowspan="1">13.01.05</td><td colspan="1" rowspan="1">WG1 review comments are addressed, and approval is completed.</td></tr><tr><td colspan="1" rowspan="1">2024.12.06</td><td colspan="1" rowspan="1">13.01.06</td><td colspan="1" rowspan="1">All changes accepted, clean version.</td></tr><tr><td colspan="1" rowspan="1">2024.12.06</td><td colspan="1" rowspan="1">14.00</td><td colspan="1" rowspan="1">Final version 14.00</td></tr><tr><td colspan="1" rowspan="1">2025.01.29</td><td colspan="1" rowspan="1">14.00.01</td><td colspan="1" rowspan="1">Initial version towards next release, starting with v14.00.01 per O-RAN specificationrevision numbering process.Addition of CRs:JNPR-2024.12.06-WG1-CR-0085-O-RAN-Slicing-Arch-ETSI_PAS_Comments-v01JNPR-2024.12.10-WG1-CR-0086-O-RAN-Slicing-Arch-ETSI_PAS_Comments-v01</td></tr><tr><td colspan="1" rowspan="1">2025.03.20</td><td colspan="1" rowspan="1">14.00.02</td><td colspan="1" rowspan="1">Editorial updates to align to O-RAN TS template v03.00</td></tr><tr><td colspan="1" rowspan="1">2025.03.20</td><td colspan="1" rowspan="1">14.00.03</td><td colspan="1" rowspan="1">Clean version for WG1 approval</td></tr><tr><td colspan="1" rowspan="1">2025.03.28</td><td colspan="1" rowspan="1">14.01</td><td colspan="1" rowspan="1">Final version 14.01</td></tr></table>