# O-RAN Test and Integration Focus Group

# End-to-End System Testing Framework Specification

# This is a re-published version of the attached final specification.

For this re-published version, the prior versions of the IPR Policy will apply, except that the previous requirement for Adopters (as defined in the earlier IPR Policy) to agree to an O-RAN Adopter License Agreement to access and use Final Specifications shall no longer apply or be required for these Final Specifications after 1st July 2022.

The copying or incorporation into any other work of part or all of the material available in this specification in any form without the prior written permission of O-RAN ALLIANCE e.V. is prohibited, save that you may print or download extracts of the material on this site for your personal use, or copy the material on this site for the purpose of sending to individual third parties for their information provided that you acknowledge O-RAN ALLIANCE as the source of the material and that you inform the third party that these conditions apply to them and that they must comply with them.

# O-RAN Test and Integration Focus Group

# End-to-End System Testing Framework Specification

Prepared by the O-RAN Alliance. Copyright $^ ©$ 2020 by the O-RAN Alliance.

# Revision History

<table><tr><td rowspan=1 colspan=1>Date</td><td rowspan=1 colspan=1>Revision</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>07/07/2020</td><td rowspan=1 colspan=1>01.00</td><td rowspan=1 colspan=1>First published version</td></tr></table>

# Contents

# Revision History ........

Chapter 1 Scope and Definitions .. 5

1.1 Scope...... ........................................................................................... ..5   
1.2 1.3 References ...................................................................................................................................................5Definitions and Abbreviations ......................................................................................................................5   
1.3.1 Definitions.... ........................................................................................................... ..5   
1.3.2 Abbreviations .... .................................................................................................................. .....6   
1.4 Revision Guideline.. ..............................................................................................................................6

Chapter 2 Introduction .....

Chapter 3 O-RAN Architecture and Deployment Scenarios.. . 9   
3.1 O-RAN Logical Architecture.. ..9   
3.2 O-RAN Cloud Deployment Scenarios.. .12

Chapter 4 O-RAN Deployment Blueprints ...... .15

4.1 Introduction .... ................................................................................ ..15   
4.2 System Profiles . ......................................................... ..15   
4.3 Subsystem Instance Profiles .... ..............................................................17   
4.3.1 Relationship between Subsystem Type and O-RAN network functions .... ..18   
4.4 Subsystem Pair Interoperability Profiles . ..19

# Chapter 5 O-RAN End-to-End (E2E) Testing Framework . .22

5.1 Stages and Sequence of Testing. ................................................... ..22   
5.2 Subsystem Testing ...... ................................................ ..25   
5.3 Subsystem Pairing and Open Interfaces Interoperability Testing........................................................... ..31   
5.4 E2E System Multi-vendors Interoperability Testing. .34   
5.4.1 Subsystem Replacement Testing . .35

# Chapter 6 O-RAN E2E Test Cases and KPIs... ..37

6.1 Introduction . ..37   
6.2 Use Cases and Services Requirements . ..37   
6.3 O-RAN Deployment Blueprint dependencies.... ..................... ..38   
6.4 Relevance of the 3GPP KPIs ........... ...... ....38   
6.4.1 3GPP KPIs defined for network monitoring, assessment, analysis, optimization and assurance.. ..38   
6.4.2 Applicability to RAN, RAN Slices, Users and Services ... ..39   
6.5 Relevance of the NGMN 5G Test Cases and KPIs . .......................................... ..39   
6.6 Test Conditions to be considered . ............................. ...40   
6.6.1 Multi-vendors interoperability.... ...................... ...40   
6.6.2 Functional, Performance including normal and abnormal conditions.. ................... ....41   
6.6.3 Radio channel variations and impacts on the overall system performance and QoE . ....41   
6.6.4 Management, Orchestration and Network Automation.. ................. ...41   
6.6.5 Additional considerations related to practical deployment aspects..... ............................................. ....42   
6.7 Test Scenarios and KPIs to be considered . ................................................................42   
6.7.1 Mobility Management.. ................................ ..42   
6.7.2 Deployability........ ........................................................... ....43

# Annex A: Operators’ inputs on Deployment Blueprints... ..44

A.1 Operator #1 inputs... ..44   
A.2 Operator #2 inputs.... ..49   
A.3 Operator #3 inputs... ..50   
A.4 Operator #4 inputs... ..51

Annex B: O-RAN Software Community inputs on Testing Methodology .. .54

B.1 O-RAN Software Community . ........................................................................... ..54   
B.2 OSC Development Cycles .... ........................................................................... ..54   
B.3 OSC Software and Test Deployment Architecture.................................................................................. ..55   
B.4 OSC Release Objectives.. ....................................................................... ..56   
B.5 OSC Testing ...... ............................................................................. ....56   
B.6 References .... ...57   
Annex C: Test Functions, Tools and Solutions for Subsystem and E2E System Testing.. ...58   
Annex D: References to O-RAN WG6 Cloud Deployment Scenarios. ....63   
Annex ZZZ: O-RAN Adopter License Agreement . ...................................................................... ....66   
Section 1: DEFINITIONS ...... ............................................................................. ...66   
Section 2: COPYRIGHT LICENSE..... .....................................................................................................................66   
Section 3: FRAND LICENSE.. ................................................................................................... .....66   
Section 4: TERM AND TERMINATION. ............................................................................................... ...67   
Section 5: CONFIDENTIALITY.....   
Section 6: INDEMNIFICATION.. ..................................................................... .....67   
Section 7: LIMITATIONS ON LIABILITY; NO WARRANTY ... .................................................................... .....67   
Section 8: ASSIGNMENT . ... .....................................................................................68   
Section 9: THIRD-PARTY BENEFICIARY RIGHTS. .................................................................................. ......68   
Section 10: BINDING ON AFFILIATES . ............................................................................. ...68   
Section 11: GENERAL ... .................................................................................... ......68

# Chapter 1 Scope and Definitions

# 1.1 Scope

This document is used to define the End-to-End System (E2E) Testing Framework for O-RAN Alliance.

# 1.2 References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

References are either specific (identified by date of publication, edition number, version number, etc.) or non-specific. For a specific reference, subsequent revisions do not apply. For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including a GSM document), a non-specific reference implicitly refers to the latest version of that document.   
[1] 3GPP TR 21.905: “Vocabulary for 3GPP Specifications”   
[2] O-RAN Operations and Maintenance Architecture, v03.00, April 2020, O-RAN Alliance   
[3] O-RAN Architecture Description, v02.00, August 2020, O-RAN Alliance   
[4] O-RAN Cloud Architecture and Deployment, v02.01, August 2020, O-RAN Alliance   
[5] O-RAN Cloud Platform Reference Design for Deployment Scenario B, v01.00, April 2020, O-RAN Alliance   
[6] O-RAN Fronthaul Control, User and Synchronization Plane Specification, v04.00, August 2020, O-RAN Alliance   
[7] O-RAN Fronthaul Management Plane Specification, v04.00, August 2020, O-RAN Alliance   
[8] O-RAN Use Cases and Deployment Scenarios White Paper, February 2020, O-RAN Alliance   
[9] 3GPP TS 28.554: “Management and orchestration; 5G end to end Key Performance Indicators (KPI)”   
[10] Definition of the Testing Framework for the NGMN 5G Pre-Commercial Network Trials, Version 3, July 2019, NGMN   
[11] O-RAN Indoor Picocell Hardware Architecture and Requirement (FR1 Only) Specification, v01.00, April 2019, O-RAN Alliance   
[12] O-RAN Deployment Scenarios and Base Station Classes for White Box Hardware, v01.00, December 2019, O-RAN Alliance

# 1.3 Definitions and Abbreviations

# 1.3.1 Definitions

For the purposes of the present document, the terms and definitions given in this section and the following listed references apply. A term defined in the present document takes precedence over the definition of the same term, if any, in the following listed references.

1. 3GPP TR 21.905 [1]   
2. O-RAN Operations and Maintenance Architecture [2]

O-RAN Deployment Blueprint: defined as the set of inputs which is used to describe a specific O-RAN deployment from several aspects. These aspects include the specification of the O-RAN deployment at the System level (e.g. architecture, performance metrics) as well as Subsystem level and the Interfaces between the specified Subsystems. This would then allow definition and documentation of the testing methodology and the test cases using the blueprint specification.

# 1.3.2 Abbreviations

For the purposes of the present document, the abbreviations given in 3GPP TR 21.905 [1] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in 3GPP TR 21.905 [1].

CNF Cloud-Native Network Function   
DUT Device Under Test   
E2E End to End   
FHGW Fronthaul Gateway   
FHM Fronthaul Multiplexer   
IUT Interface Under Test   
KPI Key Performance Indicator   
Near-RT RIC Near-Real Time RAN Intelligent Controller   
NMS Network Management System   
Non-RT RIC Non-Real Time RAN Intelligent Controller   
O-Cloud O-RAN Cloud Platform   
O-CU O-RAN Central Unit   
O-CU-CP O-RAN Central Unit – Control Plane   
O-CU-UP O-RAN Central Unit – User Plane   
O-DU O-RAN Distributed Unit   
O-eNB O-RAN eNB   
O-RAN Open RAN   
O-RU O-RAN Radio Unit   
OSC O-RAN Software Community   
PNF Physical Network Function   
RSAC Requirements and Software Architecture Committee   
SLA Service Level Agreement   
SMO Service Management and Orchestration   
SUT System Under Test   
VNF Virtual Network Function

# 1.4 Revision Guideline

This Technical Specification has been produced by the O-RAN Alliance.

The contents of the present document are subject to continuing work within O-RAN and may change following formal O-RAN approval. Should the O-RAN Alliance modify the contents of the present document, it will be re-released by ORAN with an identifying change of release date and an increase in version number as follows:

Release x.y.z where:

x the first digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc. (the initial approved document will have $\scriptstyle \mathbf { X } = 0 1$ ).   
y the second digit is incremented when editorial only changes have been incorporated in the document.   
z the third digit included only in working versions of the document indicating incremental changes during the editing process.

# Chapter 2 Introduction

This document defines the End to End (E2E) testing framework for comprehensive E2E testing and validation of the Open RAN (O-RAN) Systems ensuring robust interoperability and operate with high performance as intended in real-world deployments.

Figure 2-1 shows the focus on the O-RAN System as the System under Test (SUT) in the context of the E2E testing framework specified in this document and in relation to the E2E KPIs defined between the UEs and Services which will be further elaborated in this specification. Refer to [3] and Section 3.1 in this specification for more details on the O-RAN System.

![](images/7593ad389d58ee00b4422619434555f50e43fe332ee8d22ec3ad626d963cfdbf.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 2-1: Focus on O-RAN as the System under Test (SUT)

Mobile operators will likely plan for many different variants of O-RAN Systems depending on their strategies and use cases which they may be interested to test, deploy and evolve their O-RAN compliant networks over time. The E2E testing framework will therefore need to take into consideration the Operators’ O-RAN deployment variants given its influence on the scope of E2E testing.

The concept of O-RAN Deployment Blueprint is introduced in this specification and is used to describe the different deployment variants of O-RAN Systems for E2E system testability purposes. This document provides the definition of the O-RAN Deployment Blueprint template which contains the necessary descriptors to build O-RAN Deployment Blueprints.

A set of typical O-RAN Deployment Blueprints are defined using the most common deployment scenarios abstracted from various surveys which O-RAN Alliance has gathered from global operators. O-RAN Test and Integration Focus Group (TIFG) focuses on the definition of the E2E testing framework based on addressing the needs of these most common and probable deployment scenarios.

Operators and O-RAN Software Community (OSC) have submitted additional detailed inputs on their O-RAN Deployment Blueprints and testing practices respectively, to assist O-RAN Alliance with developing comprehensive E2E testing methodologies and test cases. These inputs are included in this specification for referencing purposes.

Chapter 3 starts with a brief introduction of the O-RAN logical architecture, O-RAN network functions and open interfaces between the O-RAN network functions. These O-RAN network functions and open interfaces are mapped to a list of the most considered use cases driven O-RAN cloud deployment scenarios.

Chapter 4 defines the O-RAN Deployment Blueprint, Template and its associated Profiles which are used to describe the O-RAN Deployment Blueprint. The O-RAN network functions and open interfaces are mapped to the various descriptors of the O-RAN Deployment Blueprint. Detailed definition of the various profiles’ templates will be considered in the future releases of this specification.

Chapter 5 details the O-RAN E2E Testing Framework by providing guidance on the Testing Methodology for holistic testing and evaluation of the O-RAN Deployment Blueprints ensuring that these Blueprints can be robustly tested and optimized, ensuring consistent high quality and performance in a deterministic, repeatable and reproducible manner across the entire technology lifecycle.

Chapter 6 provides guidance on the key considerations along with information to help guide testing and validating the O-RAN Deployment Blueprints with the relevant E2E Test Cases and KPIs. Recommendations on the specific E2E Test Cases and KPIs will be considered in the future releases of this specification.

Annex A lists the O-RAN Deployment Blueprints which have been submitted by global operators to O-RAN Alliance with the intention to assist with developing comprehensive E2E testing methodologies and test cases taking into considerations these submitted Blueprints.

Annex B provides an overview on the O-RAN Software Community (OSC) work and its current software releases and testing practices.

Annex C provides an example listing of the test functions and test tools and the applicability these test functions and tools for Subsystem and E2E System Testing.

Annex D references common deployment scenarios abstracted from various surveys which O-RAN Alliance has gathered from global operators and defined by WG6 (Orchestration and Cloudification WG).

The E2E testing framework specified in this document intend to fully leverage the Technical and Test specifications which the O-RAN Alliance Working Groups (WGs) have developed.

# Chapter 3 O-RAN Architecture and Deployment Scenarios

This chapter gives an overview of the O-RAN Logical Architecture, O-RAN network functions, open interfaces and a list of the most considered use cases driven O-RAN Deployment Scenarios which show how the O-RAN network functions are mapped to physical implementations in terms of how these network functions are realized as physical, virtual or cloud native network functions, aggregation/dis-aggregation of these network functions and where these network functions can be deployed in the network (e.g. Cell Site, Edge Cloud, Regional Cloud).

The information provided in this Chapter facilitates definition of the O-RAN Deployment Blueprint in Chapter 4. The ORAN Deployment Blueprint is used to further describe the O-RAN Deployment at the E2E System and Subsystem levels, and the Open Interfaces between the specified Subsystems. This would then allow definition and documentation of the testing methodology and the test cases using the Blueprint specification.

![](images/2a7a6758b9947bb1ff69b7fc9e2df785efd8367eb9fb53de8cca7191bbcc9299.jpg)

> **Image Summary:** {"image": "image_o_ran_architecture.png"}
  
Figure 3-1: O-RAN Logical Architecture, Deployment Scenarios and Deployment Blueprints

# 3.1 O-RAN Logical Architecture

Figure 3-2 shows the O-RAN logical architecture [3].

![](images/c8f0cd3af1b64fa82ba7d7d278a17b82997b0394e3e5be79f92479aa5919b98d.jpg)

> **Image Summary:** {"image": "image_20240502_143729.png"}
  
Figure 3-2: Logical Architecture of O-RAN [3]

Refer to O-RAN WG1 “O-RAN Architecture Description” Technical Specification [3] for more details on the definitions for the O-RAN network functions and open interfaces.

These O-RAN network functions and open interfaces are specified by different WGs in O-RAN Alliance.

Table 3-1 shows the listing of the O-RAN network functions and the WGs which are responsible for specifications of the various aspects of these O-RAN network functions.

Table 3-1: O-RAN network functions and WGs responsible for specification   

<table><tr><td colspan="2" rowspan="1">O-RAN networkO-RAN WG(s)function</td><td colspan="1" rowspan="1">O-RAN WG focus</td></tr><tr><td colspan="1" rowspan="3">O-RU</td><td colspan="1" rowspan="1">WG1</td><td colspan="1" rowspan="1">01 management services</td></tr><tr><td colspan="1" rowspan="1">WG4</td><td colspan="1" rowspan="1"> Open fronthaul CUS and M plane; Management PlaneO1 alignment work is in progress</td></tr><tr><td colspan="1" rowspan="1">WG7</td><td colspan="1" rowspan="1">Whitebox reference design</td></tr><tr><td colspan="1" rowspan="4">O-DU</td><td colspan="1" rowspan="1">WG1</td><td colspan="1" rowspan="1">01 management services</td></tr><tr><td colspan="1" rowspan="1">WG3</td><td colspan="1" rowspan="1">E2 node</td></tr><tr><td colspan="1" rowspan="1">WG4</td><td colspan="1" rowspan="1">Open fronthaul CUS and M plane; Management Plane</td></tr><tr><td colspan="1" rowspan="1">WG5</td><td colspan="1" rowspan="1">C and U-Plane profiles for F1O1 information and data models</td></tr><tr><td colspan="1" rowspan="3"></td><td colspan="1" rowspan="1">WG6</td><td colspan="1" rowspan="1">O-Clud API (including AAL APIs)</td></tr><tr><td colspan="1" rowspan="1">WG7</td><td colspan="1" rowspan="1">Whitebox reference design</td></tr><tr><td colspan="1" rowspan="1">WG8</td><td colspan="1" rowspan="1">Reference Stack: O-DU Software Architecture and APIs</td></tr><tr><td colspan="1" rowspan="6">O-CU-CP</td><td colspan="1" rowspan="1">WG1</td><td colspan="1" rowspan="1">01 management services</td></tr><tr><td colspan="1" rowspan="1">WG3</td><td colspan="1" rowspan="1">E2 node</td></tr><tr><td colspan="1" rowspan="1">WG5</td><td colspan="1" rowspan="1">C-Plane profiles for X2, Xn, F1, E1O1 information and data models</td></tr><tr><td colspan="1" rowspan="1">WG6</td><td colspan="1" rowspan="1">O-Cloud APIs (including AAL APIs)</td></tr><tr><td colspan="1" rowspan="1">WG7</td><td colspan="1" rowspan="1">Whitebox reference design</td></tr><tr><td colspan="1" rowspan="1">WG8</td><td colspan="1" rowspan="1">Reference Stack: O-CU-CP Software Architecture and APIs</td></tr><tr><td colspan="1" rowspan="6">O-CU-UP</td><td colspan="1" rowspan="1">WG1</td><td colspan="1" rowspan="1">01 management services</td></tr><tr><td colspan="1" rowspan="1">WG3</td><td colspan="1" rowspan="1">E2 node</td></tr><tr><td colspan="1" rowspan="1">WG5</td><td colspan="1" rowspan="1">U-Plane profiles for X2, Xn, F1C-Plane profile for E101 information and data models</td></tr><tr><td colspan="1" rowspan="1">WG6</td><td colspan="1" rowspan="1">O-Cloud APIs (including AAL APIs)</td></tr><tr><td colspan="1" rowspan="1">WG7</td><td colspan="1" rowspan="1">Whitebox reference design</td></tr><tr><td colspan="1" rowspan="1">WG8</td><td colspan="1" rowspan="1">Reference Stack: O-CU-UP Software Architecture and APIs</td></tr><tr><td colspan="1" rowspan="6">O-eNB</td><td colspan="1" rowspan="1">WG1</td><td colspan="1" rowspan="1">01 management services</td></tr><tr><td colspan="1" rowspan="1">WG3</td><td colspan="1" rowspan="1">E2 node</td></tr><tr><td colspan="1" rowspan="1">WG4</td><td colspan="1" rowspan="1">Open fronthaul CUS and M plane; Management Plane includes O1alignment</td></tr><tr><td colspan="1" rowspan="1">WG5</td><td colspan="1" rowspan="1">C and U-Plane profiles for X2, XnO1 information and data models</td></tr><tr><td colspan="1" rowspan="1">WG6</td><td colspan="1" rowspan="1">O-Cloud APIs (including AAL APIs)</td></tr><tr><td colspan="1" rowspan="1">WG7</td><td colspan="1" rowspan="1">Whitebox reference desin</td></tr><tr><td colspan="1" rowspan="1">O-Cloud</td><td colspan="1" rowspan="1">WG6</td><td colspan="1" rowspan="1">02O-Cloud APIs (including AAL APIs)</td></tr><tr><td colspan="1" rowspan="1">Near-Real Time RIC</td><td colspan="1" rowspan="1">WG1</td><td colspan="1" rowspan="1">01 management services</td></tr><tr><td>O-RAN network function</td><td>O-RAN WG(s)</td><td>O-RAN WG focus</td></tr><tr><td rowspan="5"></td><td></td><td>E2</td></tr><tr><td>WG3</td><td colspan="1">xApp Open APIs</td></tr><tr><td></td><td colspan="1">O1 information and data models</td></tr><tr><td>WG6</td><td colspan="1">O-Cloud APIs (including AAL APIs)</td></tr><tr><td>WG1</td><td colspan="1">O1 interface and common information/data models</td></tr><tr><td>SMO (including Non-Real Time RIC function)</td><td>WG2</td><td>A1</td></tr></table>

Table 3-2 shows the listing of the O-RAN Open Interfaces and the WGs which are responsible for the specifications for these O-RAN open interfaces.

Table 3-2: O-RAN Open Interfaces and WGs responsible for specification   

<table><tr><td colspan="1" rowspan="1">O-RAN interfaces</td><td colspan="1" rowspan="1">O-RAN WG(s)</td><td colspan="1" rowspan="1">O-RAN WG focus</td></tr><tr><td colspan="1" rowspan="1">A1</td><td colspan="1" rowspan="1">WG2</td><td colspan="1" rowspan="1">Specifies Control plane protocols for the logical interface betweenNon-RT-RIC function and near-RT-RIC function.</td></tr><tr><td colspan="1" rowspan="1">E1</td><td colspan="1" rowspan="1">WG5</td><td colspan="1" rowspan="1">3GPP defined logical interface between gNB-CU-CP and gNB-CU-UP. O-RAN wG5 reuses and adopts these principles and protocolstack defined by 3GPP for the O-CU-CP and the O-CU-UPfunctions, as well as for the definition of interoperability profilespecifications.</td></tr><tr><td colspan="1" rowspan="1">E2</td><td colspan="1" rowspan="1">WG3</td><td colspan="1" rowspan="1"> Specifies Control plane protocols for the logical interface betweennear-RT-RIC function and E2 Nodes for E2 functions.</td></tr><tr><td colspan="1" rowspan="1">F1-C</td><td colspan="1" rowspan="1">WG5</td><td colspan="1" rowspan="1">3GPP defined logical interface between gNB-CU-CP and gNB-DU.O-RAN WG5 reuses and adopts these principles and protocol stackdefined by 3GPP for the O-CU-CP and the O-DU functions, as wellas for the definition of interoperability profile specifications.</td></tr><tr><td colspan="1" rowspan="1">F1-U</td><td colspan="1" rowspan="1">WG5</td><td colspan="1" rowspan="1">3GPP defined logical interface between gNB-CU-UP and gNB-DU.O-RAN WG5 reuses and adopts these principles and protocol stackdefined by 3GPP for the O-CU-UP and the O-DU functions, as wellas for the definition of interoperability profile specifications.</td></tr><tr><td colspan="1" rowspan="1">01</td><td colspan="1" rowspan="1">WG1</td><td colspan="1" rowspan="1">Specifies Management plane interface between SMO and O-RANManaged Element.Noting that the Information and Data models for the O-RANManaged Elements are specified by their respective WGs shown inTable 3-1.</td></tr><tr><td colspan="1" rowspan="1">02</td><td colspan="1" rowspan="1">WG6</td><td colspan="1" rowspan="1"> Specifies Management plane interface between SMO and O-Cloud.</td></tr><tr><td colspan="1" rowspan="1">Open Fronthaul (OFH)</td><td colspan="1" rowspan="1">WG4</td><td colspan="1" rowspan="1">Specifies Open fronthaul interface between O-DU and O-RUincludes Control, User, Synchronization and Management Planes.Management Planes include both Hierarchical and Hybrid modes.Specifies Open fronthaul M-Plane between the O-RU and SMO forthe O-RU configured in Hybrid mode.</td></tr><tr><td colspan="1" rowspan="1">X2-C</td><td colspan="1" rowspan="1">WG5</td><td colspan="1" rowspan="1">3GPP defined logical interface for transmiting control plane information between eNBs or between eNB and en-gNB in EN-DCdeployment scenario. O-RAN WG5 reuses and adopts the principlesand protocol stack defined by 3GPP for the definition ofinteroperability profile specifications.</td></tr><tr><td colspan="1" rowspan="1">X2-U</td><td colspan="1" rowspan="1">WG5</td><td colspan="1" rowspan="1">3GPP defined logical interface for transmiting user plane information between eNBs or between eNB and en-gNB in EN-DCdeployment scenario. O-RAN wG5 reuses and adopts the principlesand protocol stack defined by 3GPP for the definition ofinteroperability profile specifications.</td></tr><tr><td colspan="1" rowspan="1">O-RAN interfaces</td><td colspan="1" rowspan="1">O-RAN WG(s)</td><td colspan="1" rowspan="2">O-RAN WG focus3GPP defined logical interface for transmitting control plane information between gNBs, ng-eNBs or between eNB and ng-gNB.O-RAN WG5 reuses and adopts the principles and protocol stackdefined by 3GPP for the definition of interoperability profilespecifications.</td></tr><tr><td colspan="1" rowspan="1">Xn-C</td><td colspan="1" rowspan="1">WG5</td></tr><tr><td colspan="1" rowspan="1">Xn-U</td><td colspan="1" rowspan="1">WG5</td><td colspan="1" rowspan="1">3GPP defined logical interface for transmitting user plane information between gNBs, ng-eNBs or between eNB and ng-gNB.O-RAN WG5 reuses and adopts the principles and protocol stackdefined by 3GPP for the definition of interoperability profilespecifications.</td></tr></table>

# 3.2 O-RAN Cloud Deployment Scenarios

This section gives a short introduction to each of the O-RAN Cloud Deployment Scenarios abstracted from inputs ORAN Alliance have received from global operators which have gathered the most interest and are of either current or relatively near-term interest that can be supported by the O-RAN specifications.

The key differences between these Cloud Deployment Scenarios are highlighted given that these are important factors to be taken into considerations when designing the O-RAN Deployment Blueprint template and the E2E testing methodologies in the next chapters of this specification.

Refer to O-RAN WG6 “Cloud Architecture and Deployment Scenarios for O-RAN Virtualized RAN” Technical Report [4] for more details.

Figure 3-3 shows a high-level comparison of O-RAN Cloud Deployment Scenarios for NR Standalone (SA) operation [4].

![](images/96a3dd0ec65bac1b1965b263dd565f63307f672c65889f5198d0d721ee25fab5.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 3-3: High Level Comparison of O-RAN Cloud Deployment Scenarios [4]

Few notes for clarification purposes on the O-RAN network functions and interfaces shown in Figure 3-3 and for the remaining of this section.

1. The O-CU and vO-CU referred in [4] should be considered as O-CU CP/UP and vO-CU CP/UP, respectively.   
2. O-RAN deployments with all Physical Network Function (PNF) based implementation may exist but are not shown in this figure as this figure shows cloud deployment scenarios with at least one O-RAN network function implemented on the O-Cloud.   
3. O-RAN deployments with PNF instead of VNF/CNF based implementation may exist but are not shown in this figure such as Scenario E with O-DU and O-RU implemented as PNFs (instead of VNF/CNF) at the Cell Site.   
4. Not all the O-RAN network functions and interfaces defined by O-RAN Alliance are shown in Figure 3-3. For example, the Non-Real Time RIC, SMO, O-CU-CP, O-CU-UP, O-eNB are not shown in this figure.

# NR Standalone (SA)

1. (SA) Scenario A shows the near-RT RIC, O-CU, and O-DU network functions virtualized and co-located on the same Edge Cloud platform. The O-RU deployed at the Cell site is not virtualized.   
2. (SA) Scenario B is similar to (SA) Scenario A, the only difference is that the Near-Real Time RIC in (SA) Scenario B is deployed on the Cloud Platform at the Regional cloud (as compared to the Edge cloud in (SA) Scenario A).   
3. (SA) Scenario C shows near-RT RIC, O-CU are virtualized on the same Regional Cloud platform and the ODU virtualized on an Edge Cloud platform   
4. (SA) Scenario C.1 shows a deployment variant of (SA) Scenario C adding the flexibility to be able to deploy parts of the O-CU-UP in the Edge Cloud platform in order to better support use cases such as differentiated performance requirements of the traffic types and network slices.   
5. (SA) Scenario C.2 shows a deployment variant of (SA) Scenario C adding the flexibility to be able to deploy additional O-DUs and O-CUs in the Edge Cloud platform to better support use cases such as differentiated performance requirements of the traffic types, network slices and RAN sharing.   
6. (SA) Scenario D shows a deployment variant of (SA) Scenario C, but in this case the O-DU functionality is supported by an O-RAN PNF rather than an O-Cloud.   
7. (SA) Scenario $\mathbf { E }$ shows a future state scenario assuming that the O-RU can be successfully virtualized and deployed with the O-DU in the same O-Cloud platform located at the Cell site. Near-RT RIC and O-CU are virtualized on the same Regional Cloud platform.   
8. (SA) Scenario F shows a future state scenario assuming that the O-RU can be successfully virtualized and deployed in the O-Cloud platform located at the Cell Site. The near-RT RIC, O-CU are virtualized on the same Regional Cloud platform and the O-DU virtualized on an Edge Cloud platform.

# NR Non-Standalone (NSA)

The following listed (NSA) Cloud Deployment scenarios are similar to the (SA) Cloud Deployment scenarios above listed with the LTE network functions (O-CU, O-DU) co-located with the NR network functions (O-CU, O-DU).

1. (NSA) Scenario A is similar to (SA) Scenario A with the addition of LTE network functions (O-CU, O-DU) virtualized and co-located on the same Edge Cloud platform as the NR network functions (O-CU, O-DU).   
2. (NSA) Scenario $\mathbf { B }$ is similar to (SA) Scenario B with the addition of LTE network functions (O-CU, O-DU) virtualized and co-located on the same Edge Cloud platform as the NR network functions (O-CU, O-DU).   
3. (NSA) Scenarios C, C.2 are similar to (SA) Scenario C, C.2 with the addition of LTE network function(s) (OCU) virtualized and co-located on the same Regional Cloud platform as the NR network function(s) (O-CU). The LTE network function(s) (O-DU) virtualized and co-located on the same Edge Cloud platform as the NR network function(s) (O-DU).   
4. (NSA) Scenario $\mathbf { D }$ is similar to (SA) Scenario D with the addition of LTE network function(s) (O-CU) virtualized and co-located on the same Edge Cloud platform as the NR network function(s) (O-CU). The LTE network function(s) (O-DU) is non-virtualized and co-located at the same Edge location as the NR network function(s) (O-DU).

Figures 3-4 and 3-5 show the Cloud Deployment Scenarios B from [4] for NR Standalone (SA) and Non-Standalone (NSA) operations, respectively. Refer to Annex D in this document for additional Cloud Deployment Scenarios figures.

Refer to [4] for the definitions and more details on the GW (Opt) node, RU, vO-CU, vO-DU shown in these figures. Refer to [5] for the Cloud Platform Reference Design for Deployment Scenario B.

![](images/99705d4fdec97be29810bd4f72dff29329eea9b43e7be3a62556c63519f1d698.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 3-4: Cloud Deployment Scenario B for SA operation [4]

![](images/a91166782bb486b6a5090b1154ad2e14ca9342b19fb688aa4d23203b2e812fa3.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 3-5: Cloud Deployment Scenario B for NSA operation [4]

Noting that all the Cloud Deployment Scenarios listed in [4] use the same set of O-RAN network functions and Open interfaces, while the key differences are with the

1. Use Cases and Services Requirements (e.g. network slicing, bandwidth, latency, reliability etc.).   
2. Network design considerations (e.g. transport capabilities such capacity, latency between Cell site, Edge and Regional cloud, operating spectrum bands etc.).   
3. NR deployment modes – SA, NSA.   
4. Network functions – Physical, Virtual, Cloudified implementation (e.g. taking into considerations O-Cloud solution availability with certain timeframes in mind).   
5. Co-locations of the various O-RAN network functions (e.g. vO-CU, vO-DU at the Edge Cloud in Scenario B).   
6. Co-located O-RAN network functions may be deployed as Integrated or Separated nodes.   
7. O-RAN network functions shown are logical functions which in deployment scenarios where more than a single O-RAN network functions are co-located, can be either implemented as an integrated Subsystem (combined vOCU and vO-DU at the Edge Cloud in Scenario B) or independent Subsystems (separate vO-CU and vO-DU at the Edge Cloud in Scenario B). Refer to Chapter 4 for the definition of the Subsystem.   
8. Locations of the O-RAN network functions at the Cell site, Edge cloud, Regional cloud.

# Chapter 4 O-RAN Deployment Blueprints

# 4.1 Introduction

This chapter provides the high-level definition of the O-RAN Deployment Blueprint template which contains the necessary descriptors to build the underlying O-RAN Deployment Blueprints.

The O-RAN Deployment Blueprint is defined as the set of inputs used to describe a specific O-RAN deployment from several aspects. These aspects include the specification of the O-RAN deployment at the System level (e.g. architecture, performance metrics) as well as Subsystem level and the Open Interfaces between the specified Subsystems. This would then allow definition and documentation of the testing methodology and the test cases using the blueprint specification.

Each of the O-RAN Deployment Blueprints can be described with

1. A single System Profile   
2. Two or more Subsystem Instance Profiles   
3. One or more Subsystem Pair Interoperability Profile(s)

![](images/c710947729f81868df54bec3cf975b4e5beacdae6b365895609905d072511a7b.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4-1 shows the relationship between Deployment Blueprint and its associated set of Profiles.   
Figure 4-1: Deployment Blueprint and the associated Profiles

# 4.2 System Profiles

The purpose of the System Profile is to describe the O-RAN Deployment Blueprint from the E2E system perspective.

A System Profile consists of System Architecture information and a set of System Profile parameters.

Figure 4-2 shows the scope of the System Profile in relation to the O-RAN Deployment Blueprint.

![](images/bfb4932175d822da6cd778c257fcb5a88c84d005c9c131eafb0c1daecb8ad2a7.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4-2: Scope of the System Profile in relation to the Deployment Blueprint

Note that the intent of Figure 4-2 is used to show the scope of the System Profile in relation to the Deployment Blueprint. It is not intending to show the actual O-RAN network functions and open interfaces which must be included in the System Profile for all the O-RAN Deployment Blueprints.

OFH indicated in Figure 4-2 includes WG4 CUS and M plane implementation and for M-Plane both the Hierarchical and Hybrid models. Refer to [6][7] for more details.

System Architecture Information shall include an Architecture diagram which is used to describe the Network and Network Slices Topology which consists of the

1. Subsystems involved   
2. Type of implementation of each Subsystem (e.g. as a Physical (PNF), Virtual (VNF) or Cloud-Native Network Function (CNF))   
3. Location where each of the Subsystems are expected to be deployed (e.g. Cell site, Edge site, Regional site, Core/Central site as appropriate)   
4. Interconnections and Cardinality between the Subsystems

The intent of this specification is to make references as much as possible to the list of Deployment Scenarios documented in O-RAN WG6 “Cloud Architecture and Deployment Scenarios for O-RAN Virtualized RAN” Technical Report [4].

Figure 3-4 shows an example of the System Architecture Diagram for Cloud Scenario B referenced from [4].

It should be noted that there can be O-RAN Deployment Blueprints which may be designed for deployment scenarios currently not specified in [4]. Examples can be an all PNF based O-RAN deployment, Non-Standalone (NSA) O-RAN deployment, different xApps implementation among others.

In addition to specifying the System Architecture diagram and information, it would be useful to specify the following listed System Profiles parameters which are used to describe the System level requirements for the Blueprints.

1. Services Requirements (e.g. eMBB, URLLC, mIoT, combinations of these)   
2. Use Cases (e.g. 3GPP use cases such as VoLTE/VoNR, O-RAN RIC-enabled use cases such as Traffic Steering, QoE Optimization, Massive MIMO Beamforming Optimization, RAN Sharing among others – refer to [8] for more details)   
3. Use Cases E2E Performance requirements of the Application, Services (e.g. data rate, latency, reliability, availability, deterministic networking including transmission latency etc.)   
4. Indoor or Outdoor deployment   
5. Radio Access Technologies (RAT) Types (e.g. 4G LTE/5G NR)   
6. 5G NR Deployment Options and Evolution (options of Standalone SA, Non-Standalone NSA)   
7. Spectrum Bands and Duplex Modes for 4G LTE/5G NR   
8. Cell Types (e.g. Macro, Micro, Pico, others)

9. Network and Network Slices Topology needing to include Cardinality, Network functions (xNFs), Transport (Tplane), Timing and Sync (S-Plane), Management (M Plane, MANO, SMO) 10. E2E Network Performance requirements of the RAN Network Functions, Slices and Management KPIs

# 4.3 Subsystem Instance Profiles

Each of the Subsystem in the Deployment Blueprint can be described with its Subsystem Instance Profile.

Figure 4-3 shows the scope of the Subsystem Instance Profile in relation to the O-RAN Deployment Blueprint.

![](images/b9eb942373039fd1d8f8b341e6c37deb842c0350f6b4a50e32c5ce93cb1d2c76.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 4-3: Scope of the Subsystem Instance Profile in relation to the Deployment Blueprint

Note that the intent of Figure 4-3 is used to show the scope of the Subsystem Instance Profile in relation to the O-RAN Deployment Blueprint. It is not intending to show the actual Subsystem Instance Profiles which must be included for all the O-RAN Deployment Blueprints.

OFH indicated in Figure 4-3 includes WG4 CUS and M plane implementation and for M-Plane both the Hierarchical and Hybrid models. Refer to [6][7] for more details.

A Subsystem Instance is defined to uniquely identify different implementations of a Subsystem Type.

For example, two O-RUs belonging to the same Subsystem Type (O-RU) which are optimally designed for Indoors versus Outdoors macro deployment scenarios will be considered as different Subsystem Instances as they would have different sets of capabilities and requirements defined for their respective purposes and therefore needing to be tested based on their respective sets of capabilities, requirements and KPIs.

The Subsystem Instance Profile is therefore dependent on the Subsystem Type.

The Subsystem Instance Profile should be specified to include the following information as defined in available technical and test specifications.

1. Features and capabilities   
2. Functional specifications   
3. Performance specifications (e.g. O-RU and O-DU sensitivity, QAM utilization, Spectral efficiency among   
others)   
4. Performance measurements – Parameters with optional nominal values

# 4.3.1 Relationship between Subsystem Type and O-RAN network functions

![](images/9bdf23a80a762d1937fa9d900083a6cc0e3e5043231ac38c4294dd6c7cd899fd.jpg)

> **Image Summary:** {"image": "data/images/o-ran_functions.png"}
  
Figure 4-4: Relationship between Subsystem Type and O-RAN Network Functions

The Subsystem Type is defined as the most fundamental building block / module of the O-RAN Deployment Blueprint which require robust interoperability testing as a Subsystem Instance in the O-RAN E2E testing framework. Therefore, the Subsystem Types may be different for different O-RAN Deployment Blueprints.

The relationship between Subsystem Type and O-RAN network functions can be described with the following scenarios

Scenario 1: A single Subsystem Type composed with a single O-RAN network function $\mathbf { M } { = } \mathbf { N } { = } 1$ ) • Scenario 2: A single Subsystem Type composed with more than a single O-RAN network function ( $\mathbf { M } { = } 1$ , $\mathrm { N } { > } 1$ ) • Scenario 3: A single O-RAN network function maps to more than a single Subsystem Type $_ { \mathrm { ( M > 1 } }$ , $\mathrm { N } { = } 1$ )

Examples of a single Subsystem Type composed with more than a single O-RAN network function

1. Combined O-CU-CP and O-CU-UP implemented as an integrated Subsystem such as what is shown in cloud deployment scenarios A and B in [4]   
2. Combined O-DU, O-CU-CP and O-CU-UP implemented as an integrated Subsystem such as what is shown in cloud deployment scenarios A and B in [4]   
3. Combined O-RU and O-DU implemented as an integrated Subsystem such as what is shown in cloud deployment scenario E in [4]

Examples of a single O-RAN network function mapped to more than a single O-RAN Subsystem Type

1. O-Cloud can consist of multiple Subsystems including the hardware, Acceleration Abstraction Layer (AAL)   
2. O-DU can consist of multiple Subsystems including L1 and L2 software stacks   
3. Near-Real Time RIC can consist of one or more xApps running on the Near-Real Time RIC

Tables 4-1, 4-2 and 4-3 show the example listings of the Subsystem Types and their relationships to the corresponding O-RAN network functions for scenarios 1, 2 and 3, respectively.

Additional Subsystem Types which are not shown in these tables can be implemented with its own composition of the ORAN network functions.

Table 4-1: Relationship of Subsystem Type to the O-RAN network functions $\mathbf { ( M = N { = } 1 }$ )   

<table><tr><td rowspan=1 colspan=1>Subsystem Type</td><td rowspan=1 colspan=2>O-RAN networkfunction                   Comments</td></tr><tr><td rowspan=1 colspan=1>O-RU</td><td rowspan=1 colspan=1>O-RU</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>FHM</td><td rowspan=1 colspan=1>O-RU</td><td rowspan=1 colspan=1>FHM is applicable in Shared Cell (FHM mode) defined inWG4 specifications [6][7].FHM is modelled as an O-RU with Open Fronthaulsupport (same as normal O-RU) and copy and combinefunction (additional to normal O-RU), but without radiotransmission/reception capability [6][7].</td></tr><tr><td rowspan=1 colspan=1>O-DU</td><td rowspan=1 colspan=1>O-DU</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>O-CU-CP</td><td rowspan=1 colspan=1>O-CU-CP</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>O-CU-UP</td><td rowspan=1 colspan=1>O-CU-UP</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>O-eNB</td><td rowspan=1 colspan=1>O-eNB</td><td rowspan=1 colspan=1></td></tr></table>

Table 4-2: Relationship of Subsystem Type to the O-RAN network functions $( { \bf M } { = } { \bf 1 } , { \bf N } { > } { \bf 1 } )$   

<table><tr><td rowspan=1 colspan=1>Subsystem Type</td><td rowspan=1 colspan=2>O-RAN networkCommentsfunction</td></tr><tr><td rowspan=1 colspan=1>O-Cloud</td><td rowspan=1 colspan=1>O-Cloud</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Near-Real Time RIC</td><td rowspan=1 colspan=1>Near-Real Time RIC</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Non-Real Time RIC</td><td rowspan=1 colspan=1>Non-Real Time RIC</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>SMO</td><td rowspan=1 colspan=1>SMO</td><td rowspan=1 colspan=1></td></tr></table>

Table 4-3: Relationship of Subsystem Type to the O-RAN network functions $( \mathbf { M } { \ > } \mathbf { 1 } , \mathbf { N } { = } \mathbf { 1 } )$   

<table><tr><td rowspan=1 colspan=1>Subsystem Type</td><td rowspan=1 colspan=2>O-RAN networkfunctions                  Reference to [4] as appropriate</td></tr><tr><td rowspan=1 colspan=1> Integrated O-CU-CP, O-CU-UP [NR]</td><td rowspan=1 colspan=1>O-CU-CP, O-CU-UP</td><td rowspan=1 colspan=1> Integrated O-CU-CP, O-CU-UP can be implemented as aSubsystem composed of O-CU-CP, O-CU-UP as shownin Scenarios A, B etc.</td></tr><tr><td rowspan=1 colspan=1>Integrated O-RU, O-DU[NR /LTE]</td><td rowspan=1 colspan=1>O-RU, O-DU</td><td rowspan=1 colspan=1>O-RU, O-DU can be implemented as a single Subsystemas shown in Scenario E for NR.</td></tr><tr><td rowspan=1 colspan=1>Integrated O-DU, O-CU-CP, O-CU-UP [NR]</td><td rowspan=1 colspan=1>O-DU, O-CU-CP, O-CU-UP</td><td rowspan=1 colspan=1>O-DU, O-CU-CP, O-CU-UP can be implemented as asingle Subsystem as shown in Scenarios A, B etc.</td></tr><tr><td rowspan=1 colspan=1> Integrated O-CU-CP, O-CU-UP, Near-Real TimeRIC</td><td rowspan=1 colspan=1>O-CU-CP, O-CU-UP,Near-Real Time RIC</td><td rowspan=1 colspan=1>Near-Real Time RIC, O-CU-CP, O-CU-UP can be implemented as a single Subsystem as shown in ScenarioCetc.</td></tr><tr><td rowspan=1 colspan=1>O-eNB [LTE]</td><td rowspan=1 colspan=1>O-RU, O-DU, CU</td><td rowspan=1 colspan=1>O-eNB can be implemented as a single O-RAN networkfunction (O-eNB) or composed with LTE O-RU, O-DU,CU.</td></tr></table>

<table><tr><td rowspan=1 colspan=1>Subsystem Type</td><td rowspan=1 colspan=2>O-RAN networkCommentsfunction</td></tr><tr><td rowspan=1 colspan=1>Hardware Acceleratorwith AccelerationAbstraction Layer (AAL)APIs</td><td rowspan=1 colspan=1>O-Cloud</td><td rowspan=1 colspan=1>Hardware Accelerator with Open API allowing NFsapplications to discover, configure, select and use (one ormore) acceleration functions provided by a givenaccelerator on the cloud platform.</td></tr><tr><td rowspan=1 colspan=1>xApps</td><td rowspan=1 colspan=1>Near-Real Time RIC</td><td rowspan=1 colspan=1>The xApp is designed to run on the near-RT RIC whichprovides Open APIs for A1, E2, Management, Controland Shared Data Layer (SDL).</td></tr><tr><td rowspan=1 colspan=1>O-DU L1 stack</td><td rowspan=1 colspan=1>O-DU</td><td rowspan=1 colspan=1>High Physical layer (L1) stack in O-DU which providesAPI&#x27;s to communicate with MAC Layer (L2) stack of O-DU.</td></tr><tr><td rowspan=1 colspan=1>O-DU L2 stack</td><td rowspan=1 colspan=1>O-DU</td><td rowspan=1 colspan=1>MAC Layer (L2) stack in O-DU which provides API&#x27;s tocommunicate with High Physical Layer (L1) stack andRLC Layer stack of O-DU.</td></tr></table>

# 4.4 Subsystem Pair Interoperability Profiles

Each pair of Subsystem Instances and the Open Interface between them can be described in the O-RAN Deployment Blueprint with its Subsystem Pair Interoperability Profile.

Figure 4-5 shows the scope of the Subsystem Pair Interoperability Profile in relation to the O-RAN Deployment Blueprint.

![](images/83b38a3911a7abcc5f413c6895071f91d12ae2e430f5f60daf0d40d5228959f7.jpg)

> **Image Summary:** {"image": "image.png"}
  
The circles at both ends of each line indicate the endpoints of each interface   
Figure 4-5: Scope of the Subsystem Pair Interoperability Profile in relation to the Deployment Blueprint

Note that the intent of Figure 4-5 is used to show the scope of the Subsystem Pair Interoperability Profile in relation to the O-RAN Deployment Blueprint. It is not intending to show the actual Subsystem Pair Interoperability Profile(s) which must be included for all the O-RAN Deployment Blueprints.

OFH indicated in Figure 4-5 includes WG4 CUS and M plane implementation and for M-Plane both the Hierarchical and Hybrid models. Refer to [6][7] for more details.

The Subsystem Pair Interoperability Profile is dependent on the pair of Subsystem Instances which are connected via an Interface under Test (IUT).

Subsystem Pair Interoperability Profile defined in the O-RAN Deployment Blueprint includes the Interoperability Test (IOT) Profile for a specific Open Interface implementation between two Subsystem Instances.

The Subsystem Pair Interoperability Profile should be specified to include the following information as defined in available O-RAN WGs technical and test specifications

1. Features and capabilities   
2. Functional specifications   
3. Performance specifications   
4. Performance measurements – Parameters with optional nominal values

Table 4-4 shows the mapping of Subsystem Pair Interoperability Profile to the respective O-RAN WGs.

Table 4-4: Subsystem Pair Interoperability Profile and respective O-RAN WGs   

<table><tr><td colspan="3" rowspan="1">Subsystem PairO-RAN WG(s)           O-RAN WG focus Interoperability Profiles</td></tr><tr><td colspan="1" rowspan="1">Open Fronthaul (OFH)</td><td colspan="1" rowspan="1">WG4</td><td colspan="1" rowspan="1">WG4 IOT profiles C/U/S/M Planes</td></tr><tr><td colspan="1" rowspan="1">X2</td><td colspan="1" rowspan="1">WG5</td><td colspan="1" rowspan="1">WG5 C and U Plane Profiles</td></tr><tr><td colspan="1" rowspan="1">Xn</td><td colspan="1" rowspan="1">WG5</td><td colspan="1" rowspan="1">WG5 C and U Plane Profiles</td></tr><tr><td colspan="1" rowspan="1">E1</td><td colspan="1" rowspan="1">WG5</td><td colspan="1" rowspan="1">WG5 C Plane Profiles (currently not available)Note: E1 not supported by existing WG5 specifications</td></tr><tr><td colspan="1" rowspan="1">F1-C/F1-U</td><td colspan="1" rowspan="1">WG5</td><td colspan="1" rowspan="1">WG5 C and U Plane Profiles</td></tr><tr><td colspan="1" rowspan="1">E2</td><td colspan="1" rowspan="1">WG3</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">A1</td><td colspan="1" rowspan="1">WG2</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">01</td><td colspan="1" rowspan="1">WG1</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">02</td><td colspan="1" rowspan="1">WG6</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">xApp (Near-RT RIC)</td><td colspan="1" rowspan="1">WG3</td><td colspan="1" rowspan="1">Open APIs for xApp</td></tr><tr><td colspan="1" rowspan="1">AAL</td><td colspan="1" rowspan="1">WG6</td><td colspan="1" rowspan="1"></td></tr></table>

# Chapter 5 O-RAN End-to-End (E2E) Testing Framework

This chapter describes the E2E testing methodology for the holistic testing and evaluation of the O-RAN Deployment Blueprints ensuring that these Blueprints can be robustly tested and optimized, ensuring consistent high quality and performance in a deterministic, repeatable and reproducible manner across the entire technology lifecycle.

Figure 5-1 shows the major phases of the technology lifecycle which will require testing and optimization.

In this version of the specification, the focus will be on the Lab Verification phase.

![](images/95170c4fda1adf37487bd7b0bf10d28ab3f3e7609a05f17a52b28d33e36c4669.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 5-1: Major Stages of the Technology Lifecycle

The proposed testing methodology involves Subsystem testing, Subsystem Pairing and Open Interfaces Interoperability testing and E2E System testing.

# 5.1 Stages and Sequence of Testing

Figure 5-2 shows the stages and sequence of testing which can be performed on the O-RAN Deployment Blueprint

1. Perform Subsystem Testing on each of the Subsystems defined in the Blueprint   
2. Perform Interoperability testing with pairs of Subsystems which have passed the Subsystem Testing stage   
3. Perform E2E System Testing after all Subsystem Pairs passed the Subsystem Pair Interoperability Testing stage

![](images/2322b09b54ce04f3aeff3ee0cd9c56bf01b304a08ccea19545b05ded5372bc5f.jpg)

> **Image Summary:** {"image": "image_o-ran_call_flow.png"}
  
Figure 5-2: Stages and Sequence of Testing to be performed on the O-RAN Deployment Blueprint

These various stages of testing can be performed (or repeated) for any modifications to the O-RAN Deployment Blueprint which can include one or more of the following conditions

1. New Subsystem vendors   
2. New releases of the software, firmware and/or hardware in any of the Subsystems   
3. Configuration changes to the software, firmware and/or hardware in any of the Subsystems

The modifications may or may not be accompanied with corresponding updates in the System profile, Subsystem Instance profiles, Subsystem Pair and Open Interfaces Interoperability profiles and therefore the test cases, performance measurements and KPIs.

The modifications are required to be thoroughly reviewed to be able to evaluate the impacts of these modifications to the corresponding modified Subsystem Instance and the Subsystems Pair and E2E System associated with the modified Subsystem Instance. The impact evaluation can then be applied to the design and selection of test cases within each of the Test Stages needing to be executed due to the modifications.

For example, a new release can be labelled as a major or minor release but it is only through detailed analysis of the modifications in this new release can help to determine the specific impacts and therefore test cases within each of the Test Stages needing to be executed for this new release.

Subsystem Replacement Testing is an implementation variant of E2E System Testing with one of Subsystems replaced in the E2E System Test environment while keeping the other Subsystems and all the test configurations the same. Subsystem Replacement Testing methodology is further discussed in Section 5.4.1.

Test Automation will be required to make the testing procedure extremely efficient as the Test Automation framework can be designed and used to handle repetitive, time-consuming tests which are required to be executed when any part of the Blueprint has been modified. This results in improved accuracy as automated tests perform the same steps precisely every time they are executed and create detailed reports. Test Automation is expected to be applied to all Stages of Testing shown in Figure 5-2.

Figure 5-3 shows the scope and relationship of Subsystem Testing, Subsystem Pairing and Open Interfaces testing and E2E System Testing.

![](images/cc5a97ae227112a669d7048bf845d5bca42e76c2a658103b203c18ad6992001d.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 5-3: Scope and Relationship of Subsystem, Subsystem Pairing and Open Interfaces, E2E System Testing

Few notes for clarification purposes on Figure 5-3

1. O-Cloud APIs and the Open APIs between the xApps and the Near-Real Time RIC can be Interfaces under Tests (IUTs) are not shown explicitly in Figure 5-3.   
2. O-RU can be implemented as a NR O-RU, LTE O-RU or Dual mode NR and LTE O-RU.   
3. OFH indicated includes WG4 CUS and M plane implementation and for M-Plane both Hierarchical and Hybrid models. Refer to [6][7] for more details.

![](images/bb6767c38ca6e8465480face56155a9b99fc23721f0baedbc7c97435bbc25316.jpg)

> **Image Summary:** {"image": "image_data"}
  
Figure 5-4 illustrates the concept of Subsystem Test, Subsystem Pair and Open Interface Test and System Testing using a multi-vendors setup example consisting of two O-RUs, one single O-DU and one single O-CU-CP/O-CU-UP.   
Figure 5-4: Example of Subsystem, Subsystem Pair/ Open Interface and System Testing

Noting that in this example, System Testing is performed for all the DUTs (used in this example) which have successfully completed Subsystem Testing, Subsystem Pair and Open Interfaces Interoperability Testing. The difference between System Testing and E2E System Testing is that the E2E System Testing is to be performed for all the Subsystems and Subsystem Pairs defined in an O-RAN Deployment Blueprint while System Testing can be performed for a subset of Subsystems and Subsystem Pairs defined in an O-RAN Deployment Blueprint.

# 5.2 Subsystem Testing

Subsystem Testing on each of the Subsystems defined in the O-RAN Deployment Blueprint is typically performed and passed before Interoperability Testing is to be performed for each of the Subsystem Pairs as defined in the Blueprint.

Subsystem testing should be performed with the requirements of the Subsystem specified in the respective Subsystem Instance Profile and Test Cases and KPIs defined by the WGs responsible for the specification of the Subsystem. Noting that each Subsystem can have Requirements, Test Cases and KPIs specified by one or more WGs.

Figure 5-5 shows a summarized view of the Subsystem, Subsystem Pair and Open Interfaces and the WGs responsible for the specification of each the Subsystem and Open Interfaces between the Subsystem Pairs.

![](images/1408b9b62c8ed5c65c26326f5812d9ad63e4b2005edb7ccd4de3a979c5016bfc.jpg)

> **Image Summary:** {"image": "image_3.png"}


# Figure 5-5: Summarized view of the Subsystem, Subsystem Pair Open Interfaces and the responsible WGs

OFH indicated in Figure 5-5 includes WG4 CUS and M plane implementation and for M-Plane both Hierarchical and Hybrid models. Refer to [6][7] for more details.

Table 5-1 shows the relationship between each of the Subsystem Types and the WGs responsible for various specifications aspects of these Subsystems.

Table 5-1: O-RAN Subsystems and WGs responsible for specifications   

<table><tr><td>Subsystem Type</td><td> Subsystem Implementation Option</td><td>WG and Specifications</td></tr><tr><td rowspan="7">O-RU</td><td>Separated/Integrated O-DU and O-RU</td><td>WG4: OFH CUS and M-plane specifications in cases where the O-DU and O-RU are implemented as</td></tr><tr><td>Management Plane – Hierarchical and Hybrid modes</td><td>separate nodes and they can either be co-located in the same or distributed locations</td></tr><tr><td>Shared Cell (FHM or Cascade mode)</td><td>WG4: OFH specifications (CUS &amp; M plane)</td></tr><tr><td>Whitebox</td><td>WG7</td></tr><tr><td>Management Plane – Hybrid mode (WG4 M Plane Hybrid mode, O1 alignment)</td><td>WG4: M-Plane specification; WG1: O1</td></tr><tr><td>Location (Cell Site)</td><td>WG6: Cell Site (if VNF/CNF) (for further study FFS)</td></tr><tr><td> Software and Hardware decoupling</td><td>WG6 (for further study FFS)</td></tr><tr><td>FHM</td><td>Shared Cell (FHM mode)</td><td>WG4: OFH specifications (CUSM plane)</td></tr><tr><td>O-DU</td><td>Management Plane</td><td>WG1: O1; WG5: O1; WG4: M-Plane specification (if the O-DU is not integrated with the O-RU)</td></tr><tr><td>Type</td><td>Subsystem Implementation Option</td><td>WG and Specifications</td></tr><tr><td rowspan="9"></td><td>Separated/Integrated O-DU and O-RU</td><td>WG4: OFH CUS and M-plane specifications in cases where the O-DU and O-RU are implemented as separate nodes and they can either be co-located in the same or distributed locations</td></tr><tr><td>Separated/Integrated O-DU and O-CU- CP/O-CU-UP</td><td colspan="1">wWG5: F1 C and U plane profiles where the O-DU and O-CU-CP/O-CU-UP are implemented as separate nodes and they can either be co-located in the same or</td></tr><tr><td>Software and Hardware decoupling</td><td colspan="1">distributed locations WG6</td></tr><tr><td>Reference Stack (PHY Hi, MAC/RLC)</td><td colspan="1">WG8: O-DU Software Architecture and APIs specifi cation</td></tr><tr><td>Accelerator decoupling (AAL)</td><td colspan="1">WG6</td></tr><tr><td>PNF, VNF, CNF</td><td colspan="1">WG6: VNF, CNF</td></tr><tr><td>Location (Cell, Edge site)</td><td colspan="1">WG6: VNF/CNF</td></tr><tr><td>Whitebox</td><td colspan="1">WG7</td></tr><tr><td>Near-Real time RIC support (counters and stats perspective, E2)</td><td colspan="1">WG3: E2; O-DU support for counters and stats perspective should be part of WG5</td></tr><tr><td rowspan="8">Integrated O- CU-CP,O- CU-UP1</td><td>Base functions</td><td>WG1: Management Plane (O1) WG5: O1 information and data models</td></tr><tr><td>Separated/Integrated O-DU and O-CU- CP/O-CU-UP</td><td colspan="1">WG5: F1 C and U plane profiles where the O-DU and O-CU-CP/O-CU-UP are implemented as separate nodes and they can either be co-located in the same or</td></tr><tr><td>Software and Hardware decoupling</td><td colspan="1">distributed locations WG6</td></tr><tr><td>Reference Stack (PDCP, RRC, SDAP − in SA mode)</td><td colspan="1">WG8: O-CU-CP/O-CU-UP Software Architecture and APIs specification</td></tr><tr><td>Accelerator decoupling (AAL)</td><td colspan="1">WG6</td></tr><tr><td>PNF, VNF, CNF</td><td colspan="1">WG6: VNF, CNF</td></tr><tr><td>NR Deployment Options NSA Option 3x, SA Option 2, others)</td><td colspan="1">WG5: X2 (NSA), Xn (SA)</td></tr><tr><td>Location (Edge, Regional site)</td><td colspan="1">WG6: VNF/CNF</td></tr><tr><td>Whitebox</td><td colspan="1">WG7</td></tr><tr><td>Near-Real time RIC support (counters and stats perspective, E2)</td><td colspan="1">WG3: E2; O-CU-CP/O-CU-UP support for counters</td></tr><tr><td rowspan="7"></td><td></td><td>and stats perspective should be part of WG5</td></tr><tr><td></td><td colspan="1">WG5: F1-C; E1 WG1: Management Plane (01)</td></tr><tr><td>Base functions</td><td colspan="1">WG5: O1 information and data models</td></tr><tr><td> Software and Hardware decoupling</td><td colspan="1">Note: E1 not supported by existing WG5 specifications</td></tr><tr><td></td><td colspan="1">WG6</td></tr><tr><td>Reference Stack (PDCP, RC)</td><td colspan="1">WG8: O-CU-CP/O-CU-UP Software Architecture and APIs specification</td></tr><tr><td>Accelerator decoupling (AAL)</td><td colspan="1">WG6</td></tr><tr><td>PNF, VNF, CNF NR Deployment Options (NSA Option 3x,</td><td colspan="1">WG6: VNF, CNF</td></tr><tr><td>SA Option 2, others)</td><td>WG5: X2 (NSA), Xn (SA)</td><td></td></tr><tr><td>Location (Edge, Regional site)</td><td>WG6: VNF/CNF</td><td></td></tr><tr><td>Whitebox</td><td>WG7</td><td></td></tr></table>

<table><tr><td></td><td rowspan=2 colspan=4>Subsystem     Subsystem Implementation Option        WG and SpecificationsTypeNear-Real time RIC support (counters and wG3: E2; O-CU-CP/O-CU-UP support for countersstats perspective, E2)                       and stats perspective should be part of wG5</td></tr><tr><td></td><td rowspan=1 colspan=1>Near-Real time RIC support (counters andstats perspective, E2)</td><td rowspan=1 colspan=1>wG3: E2; O-CU-CP/O-CU-UP support for countersand stats perspective should be part of wG5</td></tr><tr><td></td><td rowspan=10 colspan=2>O-CU-UP</td><td rowspan=1 colspan=1>Base functions</td><td rowspan=1 colspan=1>WG5: F1-U; E1WG1: Management Plane (O1)WG5: O1 information and data modelsNote: E1 not supported by existing WG5 specifications</td></tr><tr><td></td><td rowspan=1 colspan=1>Software and Hardware decoupling</td><td rowspan=1 colspan=1>WG6</td></tr><tr><td></td><td rowspan=1 colspan=1>Reference Stack (PDCP, SDAP – in SAmode)</td><td rowspan=1 colspan=1>WG8: O-CU-CP/O-CU-UP Software Architecture andAPIs specfication</td></tr><tr><td></td><td rowspan=1 colspan=1>Accelerator decoupling (AAL)</td><td rowspan=1 colspan=1>WG6</td></tr><tr><td></td><td rowspan=1 colspan=1>Management Plane (01)</td><td rowspan=1 colspan=1>WG1: 01</td></tr><tr><td></td><td rowspan=1 colspan=1>PNF, VNF, CNF</td><td rowspan=1 colspan=1>WG6: VNF, CNF</td></tr><tr><td></td><td rowspan=1 colspan=1>NR Deployment Options (NSA Option 3x,SA Option 2, others)</td><td rowspan=1 colspan=1>WG5: X2 (NSA), Xn (SA)</td></tr><tr><td></td><td rowspan=1 colspan=1>Location (Edge, Regional site)</td><td rowspan=1 colspan=1>WG6: VNF/CNF</td></tr><tr><td></td><td rowspan=1 colspan=1>Whitebox</td><td rowspan=1 colspan=1>WG7</td></tr><tr><td></td><td rowspan=1 colspan=1>Near-Real time RIC support (counters andstats perspective, E2)</td><td rowspan=1 colspan=1>WG3: E2; O-CU-CP/O-CU-UP support for countersand stats perspective should be part of WG5</td></tr><tr><td></td><td rowspan=9 colspan=2>O-eNB</td><td rowspan=1 colspan=1>Base functions</td><td rowspan=1 colspan=1>WG1: Management Plane (O1)</td></tr><tr><td></td><td rowspan=1 colspan=1>Separated/Integrated O-DU and O-RUManagement Plane – Hierarchical andHybrid modes</td><td rowspan=1 colspan=1>WG4: OFH CUS and M-plane specifications in caseswhere the O-DU and O-RU are implemented asseparate nodes and they can either be co-located in thesame or distributed locations</td></tr><tr><td></td><td rowspan=1 colspan=1> Soft ware and Hardware decoupling</td><td rowspan=1 colspan=1>WG6</td></tr><tr><td></td><td rowspan=1 colspan=1>Accelerator decoupling (AAL)</td><td rowspan=1 colspan=1>WG6</td></tr><tr><td></td><td rowspan=1 colspan=1>PNF, VNF, CNF</td><td rowspan=1 colspan=1>WG6: VNF, CNF</td></tr><tr><td></td><td rowspan=1 colspan=1> NR Deployment Options (NSA Option 3x)</td><td rowspan=1 colspan=1>WG5: X2 (NSA)</td></tr><tr><td></td><td rowspan=1 colspan=1>Location (Cell Edge, Regional site)</td><td rowspan=1 colspan=1>WG6: VNF, CNF</td></tr><tr><td></td><td rowspan=1 colspan=1>Whitebox</td><td rowspan=1 colspan=1>WG7</td></tr><tr><td></td><td rowspan=1 colspan=1>Near-Real time RIC support (counters andstats perspective, E2)</td><td rowspan=1 colspan=1>WG3: E2; O-CU-CP/O-CU-UP support for countersand stats perspective should be part of WG5</td></tr><tr><td></td><td rowspan=4 colspan=2>O-Cloud</td><td rowspan=1 colspan=1>Base functions</td><td rowspan=1 colspan=1>WG6: 02</td></tr><tr><td></td><td rowspan=1 colspan=1> Software and Hardware decoupling</td><td rowspan=1 colspan=1>WG6</td></tr><tr><td></td><td rowspan=1 colspan=1>Accelerator decoupling (AAL)</td><td rowspan=1 colspan=1>WG6</td></tr><tr><td></td><td rowspan=1 colspan=1>Location (Cell, Edge, Regional site)</td><td rowspan=1 colspan=1>WG6: VNF, CNF</td></tr><tr><td></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>Base functions</td><td rowspan=1 colspan=1>WG3: E2, xApp; WG2: A1</td></tr><tr><td rowspan=1 colspan=2>Near-Real</td><td rowspan=3 colspan=1>Near-RealTime RIC</td><td rowspan=1 colspan=1>PNF, VNF, CNF</td><td rowspan=1 colspan=1>WG6: VNF, CNF</td></tr><tr><td></td><td></td><td rowspan=1 colspan=1>Location (Edge, Regional ste)</td><td rowspan=1 colspan=1>WG6: VNF, CNF</td></tr><tr><td></td><td></td><td rowspan=1 colspan=1>xApps</td><td rowspan=1 colspan=1>WG3</td></tr><tr><td></td><td rowspan=2 colspan=2>Non-RealTime RIC</td><td rowspan=1 colspan=1>Base functions</td><td rowspan=1 colspan=1>WG2: A1</td></tr><tr><td></td><td rowspan=1 colspan=1>PNF, VNF, CNF</td><td rowspan=1 colspan=1>WG6: VNF, CNF</td></tr><tr><td></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>Location (Edge, Regiona ste)</td><td rowspan=1 colspan=1>WG6: VNF, CNF</td></tr><tr><td></td><td rowspan=1 colspan=2>SMO</td><td rowspan=1 colspan=1>Base functions</td><td rowspan=1 colspan=1>WG1: 01, 02</td></tr></table>

<table><tr><td>Subsystem Type</td><td> Subsystem Implementation Option</td><td>WG and Specifications</td></tr><tr><td>xApP</td><td>Base functions</td><td>WG3</td></tr><tr><td colspan="4">1 Refer to Table 4-2 for the mapping of Subsystem Type to O-RAN network functions</td></tr></table>

Performing Subsystem Testing on the O-DU for example will require Technical and Test specifications from

1. WG1 and WG5 for O1 Management Plane support (WG1 specifies the management services provided over the   
O1 interface, WG5 specifies the information/data models referencing 3GPP specifications where required)   
2. WG4 Open Fronthaul (OFH) CUS and M Planes (if the O-DU is not integrated with the O-RU)   
3. WG5 Open F1 (if the O-DU is not integrated with the O-CU-CP and O-CU-UP)   
4. WG6 Cloud Platform (if the O-DU is implemented as VNF/CNF running on a Cloud Platform)   
5. WG8 Software Architecture and APIs (if the O-DU is implemented using multi-vendors Reference stacks)   
6. WG6 Accelerator Abstraction Layer (AAL) (if the O-DU is implemented with Accelerator decoupling)   
7. WG3 Near-Real time RIC support (if E2 is to be implemented)

Performing Subsystem Testing on the O-RU for example will require Technical and Test specifications from

1. WG4 Open Fronthaul (OFH) CUS and M Planes (if the O-RU is not integrated with the O-DU)   
2. WG4 Open Fronthaul (OFH) CUS and M Planes (if the O-RU is configured in Shared Cell operation in either FHM or Cascade mode)   
3. WG1 and WG4 for O1 Management Plane support (WG1 specifies the management services provided over the O1 interface, WG4 specifies the information/data models referencing 3GPP specifications where required. Noting that O1 support for O-RU is still work in progress)   
4. WG7 Whitebox reference design (if the O-RU is implemented based on whitebox reference design)   
5. WG4 Near-Real time RIC support (if performance counters and statistics are required to support use cases enabled through Near-Real time RIC)

One of the key objectives of Subsystem testing is to validate the functionality of production grade DUT when the DUT is not operating in test mode and in few cases in standardized test mode as when required. One example of standardized test mode can be 3GPP test modes.

Hence it is important to ensure that the DUT is not negatively impacted with the utilization of internal functions solely to support Subsystem testing, i.e., DUT is not expected to be testing tools when deployed in production networks and therefore DUT should not be used as testing tool during Subsystem tests.

Subsystem tests are performed with a set of testing tools which are used to both apply active stimulus and as well as passive monitoring and measurements of the DUTs.

It is recommended for Subsystem testing to adopt a wraparound testing approach for each of the Subsystem as the Device under Test (DUT) and Interfaces under Test (IUT), therefore providing a testing framework for comprehensive evaluation and testing prior to Multi-vendors Interoperability (MV-IOT) Subsystem pairing and Open interfaces testing.

The wraparound testing approach involves emulating or using reference test platforms for the relevant Subsystems surrounding the Subsystem (DUT) as per defined in the O-RAN Deployment Blueprint. Reference test platforms can be Subsystems designed for commercial purpose or test applications which are used to support the wraparound test setup. For example, an O-Cloud reference test platform can be used to support wraparound testing of the virtualized/cloudified O-RAN network function designed to operate on the O-Cloud Subsystem.

This would obviously include the required Service Management and Orchestration (SMO) and necessary procedures to bring the DUT into Operational state.

Table 5-2 shows the relationship between each of the Subsystem Types and the surrounding Subsystems which are recommended to be emulated or using reference test platforms as part of the wrap around testing approach.

Table 5-2: Subsystem Types, Implementation Options and Surrounding Subsystems   

<table><tr><td colspan="1" rowspan="1">SubsystemType</td><td colspan="1" rowspan="1"> Subsystem Implementation Option</td><td colspan="1" rowspan="1">Surrounding Si bsystems which are recommended to support wraparound testing</td></tr><tr><td colspan="1" rowspan="5">O-RU</td><td colspan="1" rowspan="1">Separated/Integrated O-DU and O-RU</td><td colspan="1" rowspan="1">O-DU in cases where the O-DU and O-RU are implemented as separate nodes and they can either beco-located in the same or distributed locations</td></tr><tr><td colspan="1" rowspan="1">Shared Cell FHM)</td><td colspan="1" rowspan="1">FHM for CUS planes and NETCONF Client in O-DU/NMS for M plane</td></tr><tr><td colspan="1" rowspan="1">Shared Cell (Cascade mode)</td><td colspan="1" rowspan="1">For O-RU #1..#N in the cascaded chain. O-DU in thecase if O-RU #1 (DUT) is first in the chain closest to the O-DU; O-RU #N-1 in the case if O-RU #N (DUT) is last in the chain; For N &gt; 2 and X &lt; N, O-RU #X-1and O-RU #X+1 in the case if O-RU #X (DUT)</td></tr><tr><td colspan="1" rowspan="1">Whitebox</td><td colspan="1" rowspan="1">Reference Hardware Platform</td></tr><tr><td colspan="1" rowspan="1">Cloud Platform</td><td colspan="1" rowspan="1">Reference Cloud Platform (For further study FFS)</td></tr><tr><td colspan="1" rowspan="1">FHM</td><td colspan="1" rowspan="1">Shared Cell(FHM mode)</td><td colspan="1" rowspan="1">One or more O-RUs and One O-DU</td></tr><tr><td colspan="1" rowspan="10">O-DU</td><td colspan="1" rowspan="1">Management Plane</td><td colspan="1" rowspan="1">SMO (01)</td></tr><tr><td colspan="1" rowspan="1">Separated/Integrated O-DU and O-RU</td><td colspan="1" rowspan="1">One or more O-RUs in cases where the O-DU and O-RU are implemented as separate nodes and they caneither be co-located in the same or distributed locations</td></tr><tr><td colspan="1" rowspan="1">Separated/Integrated O-DU and O-CU-CP/O-CU-UP</td><td colspan="1" rowspan="1">O-CU-CP/O-CU-UP (F1-C/F1-U) in cases where theO-DU and O-CU-CP/O-CU-UP are implemented asseparate nodes and they can either be co-located in thesame or distributed locations</td></tr><tr><td colspan="1" rowspan="1">Separated O-CU-CP and O-CU-UP</td><td colspan="1" rowspan="1">O-CU-CP (F1-C) and O-CU-UP (F1-U)</td></tr><tr><td colspan="1" rowspan="1">Shared Cll (FHM)</td><td colspan="1" rowspan="1">FHM for CUS and M Plane. One or more O-RUs(NETCONF Server) for M-Plane</td></tr><tr><td colspan="1" rowspan="1">Shared Cell (Cascade mode)</td><td colspan="1" rowspan="1">O-RU#1</td></tr><tr><td colspan="1" rowspan="1">Whitebox</td><td colspan="1" rowspan="1">Reference Hardware Platform</td></tr><tr><td colspan="1" rowspan="1">Cloud Platform</td><td colspan="1" rowspan="1">Reference Cloud Platform</td></tr><tr><td colspan="1" rowspan="1">Accelerator decoupling (AAL)</td><td colspan="1" rowspan="1">AAL</td></tr><tr><td colspan="1" rowspan="1">Near-Real time RIC support</td><td colspan="1" rowspan="1">Near-Real time RIC (E2)</td></tr><tr><td colspan="1" rowspan="8">Integrated O-CU-CP, O-CU-UP1</td><td colspan="1" rowspan="1">Management Plane</td><td colspan="1" rowspan="1">SMO (01)</td></tr><tr><td colspan="1" rowspan="1">Separated/Integrated O-DU and O-CU-CP/O-CU-UP</td><td colspan="1" rowspan="1">One or more O-DUs (F1) in cases where the O-DU andO-CU-CP/O-CU-UP are implemented as separatenodes and they can either be co-located in the same ordistributed locations</td></tr><tr><td colspan="1" rowspan="1">Whitebox</td><td colspan="1" rowspan="1">Reference Hardware Platform</td></tr><tr><td colspan="1" rowspan="1">Cloud Platform</td><td colspan="1" rowspan="1">Reference Cloud Platform</td></tr><tr><td colspan="1" rowspan="1">Accelerator decoupling (AAL)</td><td colspan="1" rowspan="1">AAL</td></tr><tr><td colspan="1" rowspan="1">NR Deployment Option (NSA Option 3x,3a)</td><td colspan="1" rowspan="1">eNB (X2)</td></tr><tr><td colspan="1" rowspan="1">NR Deployment Option (SA Option 2)</td><td colspan="1" rowspan="1">gNB (Xn)</td></tr><tr><td colspan="1" rowspan="1">Near-Real time RIC support</td><td colspan="1" rowspan="1">Near-Real time RIC (E2)</td></tr><tr><td colspan="1" rowspan="3">O-CU-CP</td><td colspan="1" rowspan="1">Management Plane</td><td colspan="1" rowspan="1">SMO (01)</td></tr><tr><td colspan="1" rowspan="1">Separated O-CU-CP and O-CU-UP</td><td colspan="1" rowspan="1">One or more O-CU-UP (E1)Note: E1 not supported by existing WG5 specifications</td></tr><tr><td colspan="1" rowspan="1">Separated/Integrated O-DU and O-CU-CP</td><td colspan="1" rowspan="1">One or more O-DUs (F1-C) in cases where the O-DUand O-CU-CP are implemented as separate nodes and</td></tr><tr><td colspan="3" rowspan="1">Subsystem     Subsystem Implementation Option       Surrounding St            hich are recommendedType to support wraparound testing</td></tr><tr><td colspan="1" rowspan="16">O-CU-UP</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">they can either be co-located in the same or distributedlocations</td></tr><tr><td colspan="1" rowspan="1">Whitebox</td><td colspan="1" rowspan="1">Reference Hardware Platform</td></tr><tr><td colspan="1" rowspan="1">Cloud Platform</td><td colspan="1" rowspan="1">Reference Cloud Platform</td></tr><tr><td colspan="1" rowspan="1">Accelerator decoupling (AAL)</td><td colspan="1" rowspan="1">AAL</td></tr><tr><td colspan="1" rowspan="1"> NR Deployment Option (NSA Option 3x,3a)</td><td colspan="1" rowspan="1">eNB (X2)</td></tr><tr><td colspan="1" rowspan="1"> NR Deployment Option (SA Option 2)</td><td colspan="1" rowspan="1">gNB (Xn)</td></tr><tr><td colspan="1" rowspan="1">Near-Real time RIC support</td><td colspan="1" rowspan="1">Near-Real time RIC (E2)</td></tr><tr><td colspan="1" rowspan="1">Management Plane</td><td colspan="1" rowspan="1">SMO (01)</td></tr><tr><td colspan="1" rowspan="1">Separated O-CU-CP and O-CU-UP</td><td colspan="1" rowspan="1">O-CU-CP (E1)Note: E1 not supported by existing WG5 specifications</td></tr><tr><td colspan="1" rowspan="1">Separated/Integrated O-DU and O-CU-UP</td><td colspan="1" rowspan="1">One or more O-DUs (F1-U) in cases where the O-DUand O-CU-UP are implemented as separate nodes andthey can either be co-located in the same or distributedlocations</td></tr><tr><td colspan="1" rowspan="1">Whitebox</td><td colspan="1" rowspan="1">Reference Hardware Platform</td></tr><tr><td colspan="1" rowspan="1">Cloud Platform</td><td colspan="1" rowspan="1">Reference Cloud Platform</td></tr><tr><td colspan="1" rowspan="1">Accelerator decoupling (AAL)</td><td colspan="1" rowspan="1">AAL</td></tr><tr><td colspan="1" rowspan="1"> NR Deployment Option (NSA Option 3x)</td><td colspan="1" rowspan="1">eNB (X2)</td></tr><tr><td colspan="1" rowspan="1"> NR Deployment Option (SA Option 2)</td><td colspan="1" rowspan="1">gNB (Xn)</td></tr><tr><td colspan="1" rowspan="1">Near-Real time RIC support</td><td colspan="1" rowspan="1">Near-Real time RIC (E2)</td></tr><tr><td colspan="1" rowspan="5">O-eNB</td><td colspan="1" rowspan="1">Management Plane</td><td colspan="1" rowspan="1">SMO (01)</td></tr><tr><td colspan="1" rowspan="1">Whitebox</td><td colspan="1" rowspan="1">Reference Hardware Platform</td></tr><tr><td colspan="1" rowspan="1">Cloud Platform</td><td colspan="1" rowspan="1">Reference Cloud Platform</td></tr><tr><td colspan="1" rowspan="1">NR Deployment Option (NSA Option 3x)</td><td colspan="1" rowspan="1">eNB (X2)</td></tr><tr><td colspan="1" rowspan="1">Near-Real time RIC support</td><td colspan="1" rowspan="1">Near-Real time RIC (E2)</td></tr><tr><td colspan="1" rowspan="3">O-Cloud</td><td colspan="1" rowspan="1">Management Plane</td><td colspan="1" rowspan="1">SMO (O2)</td></tr><tr><td colspan="1" rowspan="1">Cloud Platform</td><td colspan="1" rowspan="1">O-RAN network functions operating on Cloud platforms − O-DU, O-CU-CP, O-CU-UP, O-eNB,Near-Real time RIC, Non-Real time RIC, SMO</td></tr><tr><td colspan="1" rowspan="1">Accelerator decoupling (AAL)</td><td colspan="1" rowspan="1">AAL</td></tr><tr><td colspan="1" rowspan="5">Near-RealTime RIC</td><td colspan="1" rowspan="1">Management Plane</td><td colspan="1" rowspan="1">SMO (01)</td></tr><tr><td colspan="1" rowspan="1">Cloud Platform</td><td colspan="1" rowspan="1">Reference Cloud Platform</td></tr><tr><td colspan="1" rowspan="1">E2 Nodes</td><td colspan="1" rowspan="1">E2 Nodes (E2) − O-DU, O-CU-CP, O-CU-UP, O-eNB</td></tr><tr><td colspan="1" rowspan="1">xApps</td><td colspan="1" rowspan="1">xApps</td></tr><tr><td colspan="1" rowspan="1">Non-Real time RIC support</td><td colspan="1" rowspan="1">Non-Real time RIC (A1)</td></tr><tr><td colspan="1" rowspan="3">Non-RealTime RIC</td><td colspan="1" rowspan="1">Management Plane</td><td colspan="1" rowspan="1">SMO (01)</td></tr><tr><td colspan="1" rowspan="1">Cloud Platform</td><td colspan="1" rowspan="1">Reference Cloud Platform</td></tr><tr><td colspan="1" rowspan="1">Near-Real time RIC support</td><td colspan="1" rowspan="1">Near-Real time RIC (A1)</td></tr><tr><td colspan="1" rowspan="1">SMO</td><td colspan="1" rowspan="1">Management Plane</td><td colspan="1" rowspan="1"> O-RAN Managed Element (O1)</td></tr><tr><td colspan="1" rowspan="1">xApP</td><td colspan="1" rowspan="1">Near-Real time RIC support</td><td colspan="1" rowspan="1">Near-Real ime RIC Platform and E2 Nodes (E2) - O-DU, O-CU-CP, O-CU-UP, O-eNB, Non-Real time RIC(A1)</td></tr></table>

Performing Subsystem Testing using the wraparound test approach on the O-DU for example may require emulating or using reference test platforms for the following surrounding O-RAN network functions

1. One or more O-RUs (Open Fronthaul OFH) in cases where the O-DU and O-RUs are implemented as separate nodes   
2. O-CU-CP/O-CU-UP (F1-C/F1-U) in cases where the O-DU and O-CU-CP/O-CU-UP are implemented as separate nodes   
3. In Separated O-CU-CP and O-CU-UP configuration - O-CU-CP (F1-C) and O-CU-UP (F1-U)   
4. In Shared Cell (FHM) configuration - FHM for CUS and M Plane (Open Fronthaul OFH). One or more O-RUs (NETCONF Server) for M-Plane   
5. In Shared Cell (Cascade) configuration - O-RU #1 (Open Fronthaul OFH)   
6. Reference Cloud Platform   
7. Near-Real time RIC (E2)   
8. SMO (O1)

Refer to the Subsystem Technical and Test specifications shown in Table 5-1 for more details on the recommended Subsystem Testing approach and detailed procedures.

![](images/f741cf2e994cb8676273f95a3342ab76de01821ab8668cbbf95e31fa19f0d65c.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 5-6 shows an example Wrap around testing setup with the O-DU configured in NR SA mode as the Subsystem under Test.   
Figure 5-6: Wrap around testing setup for O-DU as the Subsystem under Test

OFH indicated in Figure 5-6 includes WG4 CUS and M plane implementation and for M-Plane both Hierarchical and Hybrid models. Refer to [6][7] for more details.

# 5.3 Subsystem Pairing and Open Interfaces Interoperability Testing

Subsystem Pairing and Open Interfaces Interoperability testing is typically performed after the Subsystem testing on each of the Subsystems involved in the Pairing has been successfully completed and prior to E2E System Testing on all the Subsystems and Subsystems Pairs defined in the O-RAN Deployment Blueprint.

Subsystem Pairing and Open Interfaces testing should be performed with the requirements of the Subsystem Pair and Open Interfaces specified in the respective Subsystem Pair Interoperability Profiles and Test Cases and KPIs defined by the WGs responsible for the specification of the Open Interfaces and Interoperability Test (IOT) profiles.

Refer to the WGs’ Technical and Test specifications for the respective Open Interfaces shown in Table 3-2 for more details on the recommended Subsystem Pairing and Open Interfaces testing approach and detailed procedures.

One of the key objectives of Subsystem Pairing and Open Interfaces testing is to validate the functionality of production grade DUTs when all the DUTs are not operating in test modes. Hence it is important to ensure that the DUTs are not negatively impacted with the utilization of internal functions solely to support interoperability testing, i.e., DUTs are not expected to be testing tools when deployed in production networks and therefore DUTs should not be used as testing tools during interoperability tests.

Interoperability tests are performed with a set of testing tools which are used to both apply active stimulus and as well as passive monitoring and measurements of the DUTs.

It is recommended for Subsystem Pairing and Open Interfaces Interoperability testing to adopt a wraparound testing approach for each of the Subsystem Pair as the DUTs and Open Interface as the IUT, therefore providing a testing framework for comprehensive evaluation & testing prior to E2E System testing.

The wraparound testing approach involves emulating or using reference test platforms for the relevant Subsystems surrounding the Subsystem Pair as the DUTs and Open Interface as the IUT as per defined in the O-RAN Deployment Blueprint. Reference test platforms can be Subsystems designed for commercial purpose or test applications which are used to support the wraparound test setup. For example, an O-Cloud reference test platform can be used to support wraparound testing of the virtualized/cloudified O-RAN network function designed to operate on the O-Cloud Subsystem.

This would obviously include the required Service Management and Orchestration (SMO) and necessary procedures to bring the DUTs into Operational state.

Table 5-3 shows the relationship between each of the Subsystem Pair and Open Interfaces and the surrounding Subsystems which are recommended to be emulated or using reference test platforms as part of the wrap around testing approach.

Table 5-3: O-RAN Subsystem Pair and Open Interfaces and the surrounding Subsystems   

<table><tr><td colspan="1" rowspan="1">O-RAN OpenInterfaces</td><td colspan="2" rowspan="1">O-RAN            Surrounding Subsystems which are recommended to supportSubsystem Pairs   wraparound testing – if implemented (Interface)</td></tr><tr><td colspan="1" rowspan="1">A1</td><td colspan="1" rowspan="1">Non-RT RICfunction andNear-RT RICfunction</td><td colspan="1" rowspan="1">E2 nodes (E2); SMO (O1)O-Cloud reference platform (O-Cloud API)</td></tr><tr><td colspan="1" rowspan="1">E1</td><td colspan="1" rowspan="1">O-CU-CP and O-CU-UP</td><td colspan="1" rowspan="1">O-DU (F1); near-RT-RIC function (E2); SMO (O1)O-Cloud reference platform (O-Cloud API)Note: E1 not supported by existing WG5 specifications</td></tr><tr><td colspan="1" rowspan="1">E2</td><td colspan="1" rowspan="1">Near-RT RICfunction and E2Nodes for E2functions</td><td colspan="1" rowspan="1">Non-RT-RIC function (A1); SMO (O1)O-Cloud reference platform (O-Cloud API)If E2 node is O-CU-CP/O-CU-UP: O-DU (F1-C/F1-U, E2)If E2 node is O-DU: O-CU-CP/O-CU-UP (F1-C/F1-U, E2); O-RU (OFH); FHM (OFH)If E2 node is O-eNB: no additional requirements</td></tr><tr><td colspan="1" rowspan="1">F1-C</td><td colspan="1" rowspan="1">O-CU-CP and O-DU</td><td colspan="1" rowspan="1">O-CU-UP (E1); O-RU (OFH); FHM (OFH); near-RT-RIC function(E2); SMO (O1)O-Cloud reference platform (O-Cloud API)Note: E1 not supported by existing WG5 specifications</td></tr><tr><td colspan="1" rowspan="1">F1-U</td><td colspan="1" rowspan="1">O-CU-UP and O-DU</td><td colspan="1" rowspan="1">O-CU-CP (E1); O-RU (OFH); FHM (OFH); near-RT-RIC function(E2); SMO (O1)O-Cloud reference platform (O-Cloud API)Note: E1 not supported by existing WG5 specifications</td></tr><tr><td colspan="3" rowspan="1">O-RAN Open            O-RAN            Surrounding Subsystems which are recommended to supportInterfaces                Subsystem Pairs   wraparound testing – if implemented (Interface)</td></tr><tr><td colspan="1" rowspan="1">01</td><td colspan="1" rowspan="1">O-RAN ManagedElement andManagemententity (SMO)</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">02</td><td colspan="1" rowspan="1">SMO and O-Cloud</td><td colspan="1" rowspan="1">Management plane interface between SMO and O-Cloud</td></tr><tr><td colspan="1" rowspan="1">Open Fronthaul (OFH)CUS and M-Plane(Hierarchical and HybridModes)</td><td colspan="1" rowspan="1">O-DU and O-RU</td><td colspan="1" rowspan="1">O-CU-CP (F1-CP); O-CU-UP (F1-UP); near-RT-RIC function (E2);SMO(O1)O-Cloud reference platform (O-Cloud API) at the O-DU</td></tr><tr><td colspan="1" rowspan="1">Open Fronthaul (OFH)M-Plane (Hybrid Mode)</td><td colspan="1" rowspan="1">SMO and O-RU</td><td colspan="1" rowspan="1">O-DU (OFH)</td></tr><tr><td colspan="1" rowspan="1">X2-C</td><td colspan="1" rowspan="1">eNB and en-gNB</td><td colspan="1" rowspan="1">Near-Real Time RIC function (E2); SMO (O1)O-Cloud reference platform (O-Cloud API) at the O-CU-CP/O-CU-UP and O-DU</td></tr><tr><td colspan="1" rowspan="1">X2-U</td><td colspan="1" rowspan="1">eNB and en-gNB</td><td colspan="1" rowspan="1">Near-Real Time RIC function (E2); SMO (O1)O-Cloud reference platform (O-Cloud API) at the O-CU-CP/O-CU-UP and O-DU</td></tr><tr><td colspan="1" rowspan="1">Xn-C</td><td colspan="1" rowspan="1">eNB and ng-gNB</td><td colspan="1" rowspan="1">Near-Real Time RIC function (E2); SMO (O1)O-Cloud reference platform (O-Cloud API) at the O-CU-CP/O-CU-UP and O-DU</td></tr><tr><td colspan="1" rowspan="1">Xn-U</td><td colspan="1" rowspan="1">eNB and ng-gNB</td><td colspan="1" rowspan="1">Near-Real Time RIC function (E2); SMO (O1)O-Cloud reference platform (O-Cloud API) at the O-CU-CP/O-CU-UP and O-DU</td></tr></table>

Performing Subsystem Pairing and Open Interfaces Interoperability testing using the wraparound test approach on the ORU and O-DU for example may require emulating or using reference test platforms for the following surrounding O-RAN network functions

1. O-CU-CP (F1-C) and O-CU-UP (F1-U) in cases where the O-DU and O-CU-CP/O-CU-UP are implemented as   
separate nodes   
2. In Separated O-CU-CP and O-CU-UP configuration - O-CU-CP (F1-C) and O-CU-UP (F1-U)   
3. Reference Cloud Platform in cases where the O-RU and/or O-DU is implemented on Cloud Platforms   
4. Near-Real time RIC (E2)   
5. SMO (O1)

Noting that the OFH and the corresponding Management interfaces are the IUTs in this test setup. The rest of the interfaces which are used to connect the DUTs to the emulated network functions and/or reference test platforms are not the IUTs but required to support the wrap around testing approach.

Refer to the Subsystem Technical and Test specifications shown in Table 3-2 for more details on the recommended Subsystem Pairing and Open Interfaces Interoperability Testing approach and detailed procedures.

Figure 5-7 shows an example with the O-RU and O-DU configured in NR SA mode, as the Subsystem under Test and surrounding Subsystems which are recommended to be emulated or using reference test platforms for wrap around Subsystem testing approach.

![](images/36ae7a423a129b088c0be1db54b38abad3d262aeaa4ab2dc616e85629be74422.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 5-7: Wrap around testing setup for O-RU and O-DU as the Subsystem Pair under Test

OFH indicated in Figure 5-7 includes WG4 CUS and M plane implementation and for M-Plane both Hierarchical and Hybrid models. Refer to [6][7] for more details.

# 5.4 E2E System Multi-vendors Interoperability Testing

Multi-vendors interoperability (MV-IOT) system testing enables validation and verification of the entire O-RAN Deployment Blueprint as a complete E2E system under test (SUT).

E2E System testing should be performed after Subsystem Testing, Subsystem Pair and Open Interfaces Interoperability Testing have been successfully completed for all the Subsystems and Subsystem Pairs defined in an O-RAN Deployment Blueprint.

One of the key objectives of E2E System testing is to validate the functionality of production grade DUTs when all the DUTs in the SUT are not operating in test modes. Hence it is important to ensure that the DUTs are not negatively impacted with the utilization of internal functions solely to support interoperability testing, i.e., DUTs are not expected to be testing tools when deployed in production networks and therefore DUTs should not be used as testing tools during E2E System tests.

E2E System tests are performed with a set of testing tools which are used to both apply active stimulus and as well as passive monitoring and measurements of the DUTs.

It is recommended for System testing to adopt a wraparound testing approach for all the Blueprint defined Subsystems as DUTs and Open interface connecting these Subsystems as IUTs, therefore providing a testing framework for comprehensive evaluation and testing.

The wraparound testing approach involves using Test Equipment such as the UEs (test and/or emulated), Applications/Services (test and/or emulated) and Core network (test and/or emulated) as shown in Figure 5-8 below.

![](images/22832dfb5a242373588f7a50fda7465ea2ce7009ac6a2dd7801664595383bcd2.jpg)

> **Image Summary:** {"image": "image_637581.png"}
  
Figure 5-8: Wrap around testing setup for E2E System under Test (SUT)

OFH indicated in Figure 5-8 includes WG4 CUS and M plane implementation and for M-Plane both Hierarchical and Hybrid models. Refer to [6][7] for more details.

E2E System Testing should be performed with the test configuration from the following listed profiles

1. Subsystem Profiles for all the Subsystems (e.g. xApp supporting Dynamic Traffic Steering)   
2. Subsystem Pair IOT Profile for all the Subsystem Instance Pairs (e.g. OFH between the O-DU and O-RU)   
3. System Profile for the entire O-RAN Deployment Blueprint

Recommendations and considerations for E2E System Testing test cases and KPIs are further detailed in Chapter 6.

# 5.4.1 Subsystem Replacement Testing

One variant of the E2E System Testing which can be considered is the Subsystem Replacement Testing approach when the E2E System Testing is performed.

Subsystem Replacement Testing approach involves replacing one of Subsystems in the E2E System Test environment with the other Subsystems and all the test configurations remaining the same.

The Subsystem Replacement Testing approach can be useful for testing the following scenarios within the E2E System Testing environment as it is important to evaluate the compatibility and impact of such changes of the Subsystem to the entire E2E System specified per the O-RAN Deployment Blueprint

1. Testing multiple vendors offering the same Subsystem (instance)   
2. Testing upgrades (software/firmware/hardware) to a Subsystem (instance)   
3. Testing major parameters changes to a Subsystem (instance) which have been either determined or needing to be evaluated for potential System-wide impacts (e.g. expiry value of a certain timer which may have cascaded impact through the E2E system as per defined in the O-RAN Deployment Blueprint)

Subsystem Replacement Testing can be applied when a reduced scope of testing and set of test cases can be performed depending on the Subsystem replaced for any of the above listed scenarios. Scope reduction for the testing and test cases are typically determined through detailed impact analysis of the Subsystem (to be replaced) and scenarios.

In this case, prior to performing E2E System Testing (described in section 5.4), the Subsystem (to be replaced) must successfully complete both Subsystem Testing (described in section 5.2) and Subsystem Pair and Open Interfaces Interoperability Testing (described in section 5.3) based on the determined scope of testing and set of test cases.

![](images/fa4de45e02758162e8f775988e272e5735b7569f0073e13b5650ace3b0a65fa7.jpg)

> **Image Summary:** {
    "Entities": [
        "O-RU",
        "O-DU",
        "O-CU",
        "O-CU-CP",
        "O-CU-UP",
        "Near-RT RIC"
    ],

    "Relationships": [
        "O-RU → O-DU: Fronthaul (FH)",
        "O-DU → O-CU: Fronthaul (FH)",
        "O-CU-CP → Near-RT RIC: E2 interface",
        "O-CU-UP → Near-RT RIC: E2 interface"
    ],

    "Hierarchy": [
        "gNB = O-RU + O-DU + O-CU-CP + O-CU-UP"
    ],

    "Flows": [
    ],

    "Notes": [
        "1. Interfaces are indicated with the labels as depicted in the image.",
        "2. The depiction is a simplified architecture."
    ]
}
  
Figure 5-9 shows the wrap around testing setup for E2E System under Test with one of the Subsystems replaced. In this example, the O-DU subsystem is replaced as part of the E2E System Testing setup. Multiple vendors’ O-DUs can be tested in the same E2E System Testing environment with the other Subsystems in the E2E test environment remaining the same.   
Figure 5-9: Wrap around testing setup for E2E System under Test (SUT) with one Subsystem Replaced

OFH indicated in Figure 5-9 includes WG4 CUS and M plane implementation and for M-Plane both Hierarchical and Hybrid models. Refer to [6][7] for more details.

# Chapter 6 O-RAN E2E Test Cases and KPIs

# 6.1 Introduction

The O-RAN E2E testing framework aims to evaluate the entire O-RAN Deployment Blueprint holistically as a System under Test (SUT) based on a set of well-defined E2E Test Cases and Key Performance Indicators (KPIs).

The purpose of this Chapter is to outline the key considerations along with information to help guide testing and validating the O-RAN Deployment Blueprints with the relevant E2E Test Cases and KPIs.

The following considerations will be discussed in further details in the next sections in this Chapter

1. Use Cases and Services Requirements   
2. O-RAN Deployment Blueprint dependencies   
3. Relevance of 3GPP KPIs   
4. Relevance of NGMN 5G Test Cases and KPIs defined in [10]   
5. Test Conditions to be considered   
6. Test Scenarios and KPIs to be considered

# 6.2 Use Cases and Services Requirements

The selection of the E2E Test Cases and KPIs are determined mainly by 2 factors

1. Use Cases and Services   
2. O-RAN Deployment Blueprint which are optimized according to the Use Cases and Services requirements

Figure 6-1 shows a few examples for each of the major categories of use cases and services which are supported by 3GPP and O-RAN compliant networks.

![](images/4d51dc1cd7b105c2dd428704c1ba7896d427cf37152b01025152919bda647f1b.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 6-1: Examples of Use Cases/Services supported by 3GPP compliant and O-RAN RIC-enabled networks

To convince an operator to invest in O-RAN infrastructure, 3GPP and Operators’ Services which can be supported with 3GPP compliant networks must be well supported with O-RAN compliant networks.

It can therefore be expected that operators will require comprehensive system testing and evaluation to be performed on the O-RAN Deployment Blueprints using the E2E Test Cases and KPIs which are defined for the 3GPP and Operators’ Services that are of interest to them.

O-RAN Alliance has specified a set of prioritized use cases which can be only supported by O-RAN RIC-enabled networks. These use cases leverage the O-RAN architecture and demonstrates its unique benefits. Key benefits of O-RAN architecture include the ability to utilize machine learning systems and artificial intelligence back end modules to empower network intelligence through open and standardized interfaces / feeds in a multi-vendor network.

Operators will require guidance on the E2E Test Cases and KPIs which can be used to test and evaluate the performance for each of these RIC-enabled use cases in order to be able to quantify the benefits of implementing these use cases using O-RAN RIC-enabled networks as compared to networks without O-RAN RIC capabilities.

# 6.3 O-RAN Deployment Blueprint dependencies

An O-RAN Deployment Blueprint can consist of multiple Subsystems from possibly multiple vendors. The KPIs can be measured as E2E KPIs across any combinations of vendors and as well as Subsystems and Subsystems Pairs KPIs for the different Subsystems and the Open interfaces between the Subsystems respectively.

The specific Performance Measurements, KPIs and their respective values defined for Subsystem Testing, Subsystem Pair and Open Interfaces Testing and E2E System Testing will be dependent on the O-RAN Deployment Blueprints.

For example, from the E2E System Testing perspective, the beam forming system performance gain KPIs specified for outdoors macro cells would not be applicable for indoors small cells which may not require beam forming capabilities. Similarly, the beam forming performance gain measurements specified for the O-RUs which are designed and optimized for outdoors macro cells systems would not be applicable for O-RUs which are designed and optimized for indoors small cells.

It is therefore important to ensure that testing is performed for each of the

1. Subsystem Instances with their defined Subsystem Instance profiles and associated KPIs   
2. Subsystem Instances pairs with their defined Subsystem Pairs Interoperability profiles and associated KPIs   
3. System Deployment Blueprints with the defined E2E System KPIs

# 6.4 Relevance of the 3GPP KPIs

As highlighted in Section 6.2, operators will require validation of the O-RAN Deployment Blueprints that the overall 3GPP System characteristics is as expected.

In general, 3GPP defines two categories of RAN KPIs

1. Performance data for technology tests, trials, and evaluation such as in 3GPP TR 38.913. 2. Performance data for network monitoring, assessment, analysis, optimization, and assurance which will be further discussed in Section 6.4.1.

The same set of E2E KPI categories and KPIs which are defined for 3GPP compliant networks and services will be directly applicable for O-RAN compliant networks.

Additional considerations for the application of 3GPP defined KPIs for O-RAN Deployment Blueprint testing and verification will be discussed in Section 6.4.2.

# 6.4.1 3GPP KPIs defined for network monitoring, assessment, analysis, optimization and assurance

From the 3GPP system perspective, the E2E KPIs defined for network monitoring, optimization and assurance are typically defined for the following categories

1. Availability (e.g. cells ready to service connections)   
2. Accessibility (e.g. connection establishment rates, attempts/failures, latency)   
3. Integrity (e.g. throughput, latency, jitter, retransmission rates)   
4. Mobility (e.g. intra/inter RATs handover rates, interruption times for control / user planes)   
5. Reliability (e.g. amount of sent packets which are successfully delivered to the destination within the time   
constraint required by the target service, divided by the total number of sent packets)   
6. Retainability (e.g. drop rates for PDN/PDU sessions, call session)   
7. Utilization (e.g. resources utilization based on certain traffic conditions and profiles such as fronthaul, compute)   
8. Energy Efficiency (e.g. power consumption based on certain traffic conditions and profiles)

3GPP TS 28.554 [9] has defined a set of E2E KPI for the 5G System (5GS) and network slicing including the NR RAN and 5G Core (5GC).

# 6.4.2 Applicability to RAN, RAN Slices, Users and Services

3GPP KPIs are typically defined for 3GPP networks (RAN and Core), E2E network slices and 3GPP hosted services such as 3GPP voice services with VoLTE, EPS Fallback, VoNR and others.

Additional important KPIs dimensions which are required to be considered for O-RAN Deployment Blueprint testing and verification include

1. RAN Slices even though 3GPP has not yet standardized RAN slicing, this is one of the O-RAN use cases   
2. Users and Services QoS to be evaluated for Accessibility, Integrity, Mobility, Retainability   
3. Users and Services QoE to be evaluated

# 6.5 Relevance of the NGMN 5G Test Cases and KPIs

NGMN has developed a set of E2E Test Cases and KPIs which are designed to evaluate the performance of 3GPP 5G NR networks [10] with its work on the definition of the testing framework for NGMN’s Pre-Commercial 5G networks trials initiative.

The current published version of this NGMN document focuses on outdoors field testing of the 5G NR system configured in NSA EN-DC mode, which includes validation of the 5G NR radio interface, E2E KPIs and features which require E2E validation such as the E2E latency and E2E network slicing.

This set of NGMN defined E2E Test Cases and KPIs can be leveraged to a large extent for testing and validating the ORAN Deployment Blueprints in both the lab and field-testing environments.

Table 6-1 lists the E2E Test Cases and KPIs documented in [10] which should be referred to for more details.

Table 6-1: NGMN Pre-Commercial 5G networks trials E2E Test Cases and KPIs [10]   

<table><tr><td colspan="2" rowspan="1">Test Case focus            KPIs and Test Scenarios</td></tr><tr><td colspan="2" rowspan="1">Trial test requirements</td></tr><tr><td colspan="1" rowspan="1">Latency</td><td colspan="1" rowspan="1">Control Plane and User Plane Latency</td></tr><tr><td colspan="1" rowspan="1">User Throughput</td><td colspan="1" rowspan="1">Peak throughputThroughput at interference limited Cell edgeCell edge coverage throughputThroughput in different coverage conditions (link budget test)Throughput in different interference conditions (Average User Throughput)</td></tr><tr><td colspan="1" rowspan="1">Cell capacity</td><td colspan="1" rowspan="1">Cell peak throughputCell average throughput</td></tr><tr><td colspan="1" rowspan="1">Spectral efficiency</td><td colspan="1" rowspan="1">User and Cel Spectral fficiency</td></tr><tr><td colspan="1" rowspan="1">Coverage</td><td colspan="1" rowspan="1">Outdoor Single-cell CoverageOutdoor Multi-Cell Continuous CoverageOutdoor to Indoor CoverageIndoor Coverage</td></tr><tr><td colspan="1" rowspan="1">Mobility</td><td colspan="1" rowspan="1">Intra-Cell mobility testing Inter-Cell Mobility (Handover) Testing</td></tr><tr><td colspan="1" rowspan="1">Reliability</td><td colspan="1" rowspan="1"> Success probability of transmiting a set number of bytes within a certain delay</td></tr><tr><td>Test Case focus</td><td> KPIs and Test Scenarios</td></tr><tr><td rowspan="2">Retainability</td><td>Capability of the network to retain a service by a UE for a desired duration</td></tr><tr><td colspan="1">once the user is connected to the service - Call drop rate, Call setup complete rate, Dual connectivity drop rate</td></tr><tr><td>User experience</td><td>Examples Content Distribution Streaming Service QoE, Social Networking QoE, High Speed Internet QoE</td></tr><tr><td rowspan="2">Energy efficiency</td><td>UE energy efficiency</td></tr><tr><td colspan="1">Network energy efficiency</td></tr><tr><td rowspan="2"> Inter-RAT procedures</td><td>NSA Inter-RAT Mobility with PS Service</td></tr><tr><td colspan="1">SA Inter-RAT Mobility with PS Service</td></tr><tr><td rowspan="2">RAN architecture split</td><td>CU-DU Separation</td></tr><tr><td colspan="1">CP-UP Separation</td></tr><tr><td colspan="2"> Service or technology specific requirements</td></tr><tr><td>Location/Positioning service</td><td>EPS Scenario (Option 3), 5GS Scenario (NG-RAN)</td></tr><tr><td rowspan="9">Fixed wireless access</td><td>Average and peak throughput</td></tr><tr><td colspan="1">Meeting throughput speed tier guarantees</td></tr><tr><td colspan="1">End-to-end latency performance</td></tr><tr><td colspan="1">Beam tracking range (horizontal/azimuthal) for base station and CPE/UE antennas</td></tr><tr><td colspan="1">Quality of Service differentiation scenarios for Voice/video application</td></tr><tr><td colspan="1">Number of (active) users served per base station</td></tr><tr><td colspan="1">Geographic coverage area</td></tr><tr><td colspan="1">Robustness to environmental blockage (mm Wave)</td></tr><tr><td colspan="1">EPS Fall-back, Voice Over NR</td></tr></table>

# 6.6 Test Conditions to be considered

As highlighted in the earlier sections, the E2E System Test Cases and KPIs which are defined by 3GPP will be directly applicable for testing and validating the O-RAN Deployment Blueprints, while those defined by NGMN in [10] can be leveraged to a large extent for similar purpose.

However, it is important to take into considerations the following aspects when testing and validating O-RAN Deployment Blueprints

1. Multi-vendors interoperability   
2. Functional, Performance including normal and abnormal conditions   
3. Radio channel variations and impacts on the overall system performance and Quality of Experience (QoE)   
4. Management, Orchestration and Network Automation   
5. Additional considerations related to practical deployment aspects

# 6.6.1 Multi-vendors interoperability

As the O-RAN Deployment Blueprint can consist of multiple Subsystems from possibly multiple vendors, additional considerations for O-RAN focused system test scenarios, conditions and KPIs will be required to validate and evaluate the performance of multi-vendors interoperability in accordance to the O-RAN Deployment Blueprint definition.

For example if the O-RUs, O-DUs and O-CU-CPs/O-CU-UPs in an O-RAN Deployment Blueprint are provided by different vendors, then it would be important to ensure that the E2E KPIs are evaluated with the appropriate E2E test

cases and test scenarios which can be used to validate multi-vendors interoperability between these O-RAN network functions.

# 6.6.2 Functional, Performance including normal and abnormal conditions

Multi-vendors interoperability testing typically includes functional validation for handling normal conditions.

However, similar to how the 3GPP Radio Access Networks are expected to be tested and optimized for Performance and Abnormal conditions handling, operators would be expecting the O-RAN Deployment Blueprints to be tested and optimized in the same manner.

O-RAN Deployment Blueprints consisting of Subsystems from multiple vendors will therefore require Multi-vendors interoperability testing to include testing for Performance and Abnormal conditions handling.

Performance testing can be used to evaluate how well each individual Subsystem, each pair of Subsystem Instances and all the Subsystems in the O-RAN Deployment Blueprint inter-operate to achieve the best in class cost-performance ratio.

This can include quantifying the O-RAN Deployment Blueprint when Subsystems from multiple vendors inter-operate under Performance test conditions through

1. Performing testing using the same set of KPIs, for example examining if the latency figures can be achieved in performance testing conditions.   
2. Measuring resources utilization efficiency for example with Radio resource blocks, Open Fronthaul and xHaul transport, O-Cloud computing / networking / storage and power consumption / energy efficiency.

Abnormal testing will in some cases be required to be performed to validate fault management and zero-touch network automation techniques such as self-healing functions.

# 6.6.3 Radio channel variations and impacts on the overall system performance and QoE

Radio access networks should be tested with close to real-world radio channel conditions, variations of the channel conditions and mobility patterns in the lab environment for a proper evaluation of the overall system performance of the RAN and QoE of the services handled by the RAN.

For example testing key 3GPP RAN functions such as Radio resource, Beam / Cell level mobility management and advanced use cases defined by O-RAN such as Traffic Steering and Massive MIMO Beamforming Optimization will require the test environment to be setup with the appropriate network and slices topology, radio channel conditions, UEs distributions and mobility patterns, which otherwise these functions and use cases cannot be properly tested and evaluated.

Testing O-RAN Deployment Blueprints consisting of Subsystems from multiple vendors under the appropriate radio channel conditions and mobility patterns will be required to validate how well the multi-vendors Subsystems inter-operate under these test conditions.

# 6.6.4 Management, Orchestration and Network Automation

In general, operators require the Management & Orchestration (MANO) and Network Automation capabilities of thei networks to be robustly validated.

In order for operators to be able to deploy O-RAN networks and network slices which can consist of Subsystems from multiple vendors, multi-vendors interoperability testing will be required for validating the management and orchestration functions of all the Subsystems defined in the O-RAN Deployment Blueprints.

O-RAN Alliance has specified a set of prioritized use cases for O-RAN orchestration of virtualized RAN and the interfaces used for management and orchestration, in particular the O1 interface between the service management and orchestration framework and the RAN managed functions and the O2 interface between the service management and orchestration framework and the O-Cloud Infrastructure Management Services/Deployment Management Services that controls resource assignment for Virtualized Network Functions.

Operators will require guidance on the E2E Test Cases and KPIs which can be used to test and evaluate the functionality and performance for each of these orchestration use cases in order to be able to quantify the feasibility and benefits of deploying O-RAN compliant networks.

# 6.6.5 Additional considerations related to practical deployment aspects

In addition to performing testing based on 3GPP, ITU-T, IEEE specified functionalities, it is important as well to take into considerations the practical deployment aspects which operators will need to consider and therefore tested as part of the E2E Testing framework. These considerations include

1. Performance Evaluation and Monitoring   
2. Robustness, Resilience, Reliability, Security   
3. Troubleshooting and Root Cause Analysis (RCA)   
4. Practical Network Operating Conditions such as fronthaul transport loading and non-zero variable delays   
5. FCAPS including fault, configuration, accounting, performance, and security management   
6. System Deployment lifecycle (installs, upgrades)   
7. Virtualization, interaction with O-Cloud (NFVi), Management and Orchestration (MANO)   
8. Evolution towards Zero Touch Automation network management

System Deployment lifecycle (installs, upgrades) involves multiple phases of the System Deployment lifecycle which will include new installs and as well as future field upgrades scenarios such as

1. Performing software or firmware upgrades of the existing installed O-RAN Network Functions (e.g. increased performance, enhanced capabilities such as dynamic spectrum sharing, bug fixes and others)   
2. Installing new O-RAN Network Functions which are required to interoperate with existing installed O-RAN Network Functions (e.g. adding new O-RUs from a new vendor to the field operational O-DU currently serving O-RUs from the current vendor, new xApp to be installed onto the current near-RT RIC)   
3. Installing new or Replacing existing hardware (or O-Cloud) to support existing installed O-RAN Network Functions (e.g. adding, replacing storage, networking, computing resources)

It is therefore important to define testing templates ensuring that the essential testing is performed for the specific Subsystem Instances, Subsystem Instances Pairs and Open Interfaces and System Deployment Blueprint which are affected by the System Deployment lifecycle scenarios.

# 6.7 Test Scenarios and KPIs to be considered

A few examples of Test Scenarios and KPIs which are needing to be considered for testing O-RAN Deployment Blueprint consisting of Subsystems from multiple vendors are shared in more details in this section.

1. Mobility management   
2. Deployability

# 6.7.1 Mobility Management

Mobility management test cases may need to consider test scenarios which involve testing multi-vendors interoperability between Subsystems provided from multiple vendors.

Test scenarios can include intra O-RU (inter beams for intra cell and inter cells), inter O-RUs (intra O-DU), inter O-DUs (intra O-CU-CP/O-CU-UP), inter O-CU-CP/O-CU-UPs, Intra vs Inter RATs handovers in Idle and Connected modes.

Figure 6-2 shows an example of a test scenario which can be used to verify the interoperability aspects of mobility management in a multi-vendors O-RAN Deployment Blueprint test setup.

![](images/2db42c1c48c664cebe7e9e08049bb5fa6a6418cc082ee08efac2f8b4958c71ba.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure 6-2: Test Scenario for verifying multi-vendors interoperability aspect of Mobility Management

In this test scenario

1. UE is first connected through O-RU (R1), O-DU (D1), O-CU-CP/UP (C1)   
2. UE then moves towards O-RU (R2) which is an inter O-RU and intra O-DU mobility scenario   
3. UE then moves towards O-RU (R3) which is an inter O-RU and inter O-DU mobility scenario   
4. UE then moves towards O-RU (R4) which is an inter O-RU, inter O-DU and O-CU-CP/UP mobility scenario

The Mobility KPIs including handover attempts/success rates, interruption time (aka latency) to control, user plane and services plane, services performances such as packet losses, jitter and latency should be measured in order to validate that the services SLAs can be met while executing the test sequences.

# 6.7.2 Deployability

One of the key considerations for dis-aggregated RAN deployments is the requirements for the underlying transport network which will be dependent on the requirements of the Services and dis-aggregated RAN functions which will be required to interwork over the transport network segments.

These requirements are typically simulated, estimated, tested, measured, and validated for dis-aggregated RAN transport planning purposes.

O-RAN Deployment Blueprints will be required to go through similar process with the additional complexity that the Subsystems in the same O-RAN Deployment Blueprint may be provided by different vendors which may have different levels of influences on the transport requirements therefore needing to be tested and validated with test setup considerations outlined in Section 6.6.

The Integrity and Utilization KPIs including transport capacity/throughput, packet losses, jitter and latency should be measured during the testing process taking into considerations the following aspects

1. Capacity/throughput for Open fronthaul interface for transport planning purposes, which can vary depending on test scenarios and key factors such as radio conditions among others outlined in Section 6.6.3.   
2. Latency for transport planning purposes and delay management interoperability which can vary dependent on the transport options and can be impacting performance and users-services experiences.   
3. Resources Utilization based on test profiles which should include networking, computing, storage resources.

# Annex A: Operators’ inputs on Deployment Blueprints

Annex A lists the O-RAN Deployment Blueprint profiles which have been submitted by global operators to O-RAN Alliance to assist with developing comprehensive E2E testing methodologies and test cases taking into considerations these submitted profiles.

# A.1 Operator #1 inputs

# NR Deployment Options and Evolution

1. Step1: (NSA EN-DC) Option 3x (based on X2 interface and EPC)   
2. Step2: Step1 $^ +$ (SA 5G) Option 2   
3. Step3: Step2 $^ +$ (ng-LTE) Option 5/Option 7x (based on Xn interface and 5GC)

# Use Cases focuses

1. RAN Sharing   
2. Near-RT RIC (edge-cloud) Non-RT-RIC Use Cases (regional-cloud): Traffic Steering, QoE/QoS, Massive MIMO Beam Forming and Optimization

E2E Performance requirements of Application / Network Slices – references to NGMN Definition of the Testing Framework for the NGNM 5G Pre-Commercial Network Trials [10].

Table A-1: Operator #1 inputs - System Profile considerations   

<table><tr><td rowspan=1 colspan=3>System Profiles NSA Opt. 3x     NSA Opt. 7xconsiderations  (FR1)            (FR1)</td><td rowspan=1 colspan=1>SA Opt. 5 (FR1)</td><td rowspan=1 colspan=1>SA Opt. 2 (FR1)</td><td rowspan=1 colspan=1>SA Opt. 2 (FR2)</td></tr><tr><td rowspan=1 colspan=1>Service Priority</td><td rowspan=1 colspan=1>eMBB (NR andLTE)</td><td rowspan=1 colspan=1>eMBB (NR andLTE)</td><td rowspan=1 colspan=1>eMBB (LTE)</td><td rowspan=1 colspan=1>eMBB (NR),URLLC (NR)</td><td rowspan=1 colspan=1>eMBB (NR),URLLC (NR)</td></tr><tr><td rowspan=1 colspan=1>DeploymentScenarios</td><td rowspan=1 colspan=3>Outdoor Macro/Micro Cell and RAN Sharing</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>DeploymentOptions andEvolution</td><td rowspan=1 colspan=1>NSA EN-DCOption 3x withX2 between eNBand en-gNB; andEPC</td><td rowspan=1 colspan=1>NSA Option 7xwith Xn betweengNB and ng-eNB;and 5GC</td><td rowspan=1 colspan=1>(ng-LTE) SASOption 5 with 5GC</td><td rowspan=1 colspan=1>NR Standalone(SA) Option 2 with5GC</td><td rowspan=1 colspan=1>NR Standalone(SA) Option 2 with5GC</td></tr><tr><td rowspan=1 colspan=1>NR SpectrumBands</td><td rowspan=1 colspan=1>NR: FR1 -3.7GHz TDD, 700MHz FDDLTE:2.6GHz/1800MHz/800MHz FDD</td><td rowspan=1 colspan=1>NR: FR1 - 3.7 GHzTDD, 700 MHzFDDLTE:2.6GHz/1800MHz/800MHz FDD</td><td rowspan=1 colspan=1>2.6GHz/1800MHz/800MHz FDD</td><td rowspan=1 colspan=1>FR1 - 3.7 GHzTDD, 700 MHzFDD</td><td rowspan=1 colspan=1>FR2 - 26 GHz TDD</td></tr><tr><td rowspan=1 colspan=1>FigureReference</td><td rowspan=1 colspan=1>Figure A-1</td><td rowspan=1 colspan=1>Figure A-1</td><td rowspan=1 colspan=1>Figure A-2</td><td rowspan=1 colspan=1>Figure A-2</td><td rowspan=1 colspan=1>Figure A-3</td></tr><tr><td rowspan=1 colspan=1>Reference toWG6 CAD [4]</td><td rowspan=1 colspan=1>Based onScenario A inAppendix 7.1</td><td rowspan=1 colspan=1>Based on ScenarioA in Appendix 7.1</td><td rowspan=1 colspan=1>Based on ScenarioA in Section 6.1</td><td rowspan=1 colspan=1>Based on ScenarioA in Section 6.1</td><td rowspan=1 colspan=1>Based on ScenarioE in Section 6.1</td></tr></table>

![](images/b9cafff14ccfc411153516d60497a18cf5d26557c287fb59ab08c114621ecde7.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure A-1: Operator #1 Deployment Scenario #1 – NSA (FR1)

Note: W1 is specified in 3GPP Release 16 for ng-eNB only.

Refer to [4][11][12] for more details on the FHGW.

![](images/c9bf014c7d9a34d007d8cff71d58470ecae6ee3f2d51e36fe0ea5a15cfb030af.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure A-2: Operator #1 Deployment Scenario #2 – SA (FR1)

![](images/8153e8ac1b141f2fd051f8ee19a7584ec1009efae8f0539bf02b97b5b02060e0.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure A-3: Operator #1 Deployment Scenario #3 – SA (FR2)

Table A-2: Operator #1 inputs – Subsystem O-RU   

<table><tr><td rowspan=1 colspan=1>O-RU</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1>Integrated or</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1>Separated.In the case if the O-</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1>DU and O-RU are</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1> integrated, OFH is</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1>not available for</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=2 colspan=1>testing.In the case if the O-DU and O-RU areimplemented as</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1></td></tr><tr><td></td><td></td><td rowspan=1 colspan=4></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>separate nodes and</td></tr><tr><td></td><td></td><td></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=3></td><td rowspan=1 colspan=1>they can either be</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1>co-located in the</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1>same or distributed</td></tr><tr><td rowspan=1 colspan=1>ManagementPlane (WG4 MPlaneHierarchical,Hybrid mode,01)</td><td rowspan=3 colspan=7>WG4: M-Plane specification; WG1: 01PNFCell Site</td></tr><tr><td rowspan=1 colspan=1>PNF, VNF, CNF</td></tr><tr><td rowspan=1 colspan=1>Location</td></tr></table>

Table A-3: Operator #1 inputs – Subsystem FHGW   

<table><tr><td>FHGW</td><td>NSA Opt. 3x (FR1)</td><td>NSA Opt. 7x (FR1)</td><td>SA Opt. 5 (FR1)</td><td> SA Opt. 2 (FR1)</td><td>SA Opt. 2 (FR2)</td></tr><tr><td>7-2x&lt;-&gt;7-2x; 7-2x&lt;-&gt;8</td><td>7-2x &lt;-&gt;7-2x; 7-2x &lt;-&gt;8 (LTE)</td><td></td><td></td><td>7-2x&lt;-&gt;7-2x</td><td>7-2x&lt;-&gt;7-2x (if DU-RU not integrated)</td></tr></table>

Table A-4: Operator #1 inputs – Subsystem O-DU   

<table><tr><td rowspan=1 colspan=1>O-DU</td><td rowspan=1 colspan=4>NSA Opt. 3x       NSA Opt. 7x(FR1)                                     SA Opt. 5 (FR1)    SA Opt. 2 (FR1)(FR1)</td><td rowspan=1 colspan=1>SA Opt. 2 (FR2)</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1>Integrated or</td></tr><tr><td></td><td></td><td rowspan=1 colspan=3></td><td rowspan=1 colspan=1>Separated.</td></tr><tr><td></td><td></td><td rowspan=1 colspan=2></td><td></td><td rowspan=1 colspan=1>In the case if the O-</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1>DU and O-RU are</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1>integrated, OFH is</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1>not available fortesting.In the case if the O-</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td rowspan=3 colspan=1>DU and O-RU areimplemented asseparate nodes and</td></tr><tr><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1></td></tr><tr><td></td><td></td><td></td><td rowspan=1 colspan=2></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1>they can either beco-located in the</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1>same or distributed</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1>locations — WG4:OFH.</td></tr></table>

Table A-5: Operator #1 inputs – Subsystem O-CU-CP/ O-CU-UP   

<table><tr><td rowspan=1 colspan=1>O-DU</td><td rowspan=1 colspan=1>NSA Opt. 3x(FR1)</td><td rowspan=1 colspan=1>NSA Opt. 7x(FR1)</td><td rowspan=1 colspan=1>SA Opt. 5 (FR1)</td><td rowspan=1 colspan=1>SA Opt. 2 (FR1)</td><td rowspan=1 colspan=1>SA Opt. 2 (FR2)</td></tr><tr><td rowspan=2 colspan=1>Separated /Integrated O-DU and O-CU-CP/O-CU-UP</td><td rowspan=1 colspan=1>Separated</td><td rowspan=1 colspan=1>Separated</td><td rowspan=2 colspan=1>SeparatedWG5: W1</td><td rowspan=2 colspan=1>SeparatedWG5: F1</td><td rowspan=2 colspan=1>SeparatedWG5: F1</td></tr><tr><td rowspan=1 colspan=1>WG5: F1, W1</td><td rowspan=1 colspan=1>WG5: F1, W1</td></tr><tr><td rowspan=1 colspan=1>ManagementPlane (WG4 MPlaneHierarchical,Hybrid mode,01)</td><td rowspan=1 colspan=5>WG4: M-Plane specification; WG1: O1</td></tr><tr><td rowspan=1 colspan=1>PNF, VNF, CNF</td><td rowspan=1 colspan=4>WG6: VNF, CNF</td><td rowspan=1 colspan=1>PNF</td></tr><tr><td rowspan=1 colspan=1>O-Cloud</td><td rowspan=1 colspan=4>WG6: 02</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>Location (Cell,Edge site)</td><td rowspan=1 colspan=4>WG6: Edge</td><td rowspan=1 colspan=1>Cell</td></tr><tr><td rowspan=1 colspan=1>Near-Real timeRIC support(counters andstatsperspective, E2)</td><td rowspan=1 colspan=5>WG3: E2</td></tr></table>

Table A-6: Operator #1 inputs – Subsystem O-eNB   

<table><tr><td rowspan=1 colspan=1>O-CU-CP /O-CU-UP</td><td rowspan=1 colspan=5>NSA Opt. 3x       NSA Opt. 7x                              SA Opt. 2 (FR1)   SA Opt. 2 (FR2)SA Opt. 5 (FR1)(FR1)              (FR1)</td></tr><tr><td rowspan=1 colspan=1>Management</td><td rowspan=1 colspan=5>WG1: 01</td></tr><tr><td rowspan=2 colspan=1>Separated /Integrated / 0-DU and O-CU-CP/O-CU-UP</td><td rowspan=1 colspan=1>Separated</td><td rowspan=1 colspan=1>Separated</td><td rowspan=1 colspan=1>Separated</td><td rowspan=1 colspan=1>Separated</td><td rowspan=1 colspan=1>Separated</td></tr><tr><td rowspan=1 colspan=1>WG5: F1, W1</td><td rowspan=1 colspan=1>WG5: F1, W1</td><td rowspan=1 colspan=1>WG5: W1</td><td rowspan=1 colspan=1>WG5: F1</td><td rowspan=1 colspan=1>WG5: F1</td></tr><tr><td rowspan=1 colspan=1>PNF, VNF, CNF</td><td rowspan=1 colspan=5>WG6: VNF, CNF</td></tr><tr><td rowspan=1 colspan=1>O-Cloud</td><td rowspan=1 colspan=5>WG6: 02</td></tr><tr><td rowspan=1 colspan=1>NR DeploymentOptions (NSAOption 3x, SAOption 2,others)</td><td rowspan=1 colspan=1>WG5: X2 (NSA)</td><td rowspan=1 colspan=4>WG5: Xn (SA)</td></tr><tr><td rowspan=1 colspan=1>Location (Edge,Regional site))</td><td rowspan=1 colspan=5>WG6: Edge</td></tr><tr><td rowspan=1 colspan=1>Near-Real timeRIC support(counters andstatsperspective, E2)</td><td rowspan=1 colspan=5>WG3: E2</td></tr></table>

<table><tr><td rowspan=1 colspan=4>NSA Opt. 3x       NSA Opt. 7xO-eNB                                                        SA Opt. 5 (FR1)   SA Opt. 2 (FR1)   SA Opt. 2 (FR2)(FR1)              (FR1)</td></tr><tr><td rowspan=1 colspan=1>Management</td><td rowspan=1 colspan=1>WG1: 01</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>PNF, VNF, CNF</td><td rowspan=1 colspan=1>WG6: VNF, CNF</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>O-Cloud</td><td rowspan=1 colspan=1>WG6: 02</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td></tr></table>

Table A-7: Operator #1 inputs – Subsystem O-Cloud   

<table><tr><td rowspan=1 colspan=1>O-eNB</td><td rowspan=1 colspan=1>NSA Opt. 3x       NSA Opt. 7x(FR1)              (FR1)</td><td rowspan=1 colspan=2>SA Opt. 5 (FR1)   SA Opt. 2 (FR1)</td><td rowspan=1 colspan=1>SA Opt. 2 (FR2)</td></tr><tr><td rowspan=1 colspan=1>NR DeploymentOptions (NSAOption 3x, SAOption 2,others)</td><td rowspan=1 colspan=1>WG5: Xn (SA), X2 (NSA)</td><td rowspan=1 colspan=1>WG5: Xn (SA)</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>Location (Cell,Edge, Regionalsite)</td><td rowspan=1 colspan=2>WG6: Edge</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td></tr><tr><td rowspan=1 colspan=1>Near-Real timeRIC support(counters andstatsperspective, E2)</td><td rowspan=1 colspan=2>WG3: E2</td><td rowspan=1 colspan=1>N/A</td><td rowspan=1 colspan=1>N/A</td></tr></table>

Table A-8: Operator #1 inputs – Subsystem Near-Real Time RIC   

<table><tr><td>O-Cloud</td><td>NSA Opt. 3x (FR1)</td><td>NSA Opt. 7x (FR1)</td><td>SA Opt. 5 (FR1)</td><td>SA Opt. 2 (FR1)</td><td>SA Opt. 2 (FR2)</td></tr><tr><td>Management</td><td>WG6: 02</td><td></td><td></td><td></td><td></td></tr><tr><td>Location (Cell, Edge, Regional site)</td><td colspan="3">WG6: Edge, Regional</td><td></td><td></td></tr></table>

<table><tr><td rowspan=1 colspan=1>Near-RealTime RIC</td><td rowspan=1 colspan=1>NSA Opt. 3x       NSA Opt. 7x       SA Opt. 5 (FR1)    SA Opt. 2 (FR1)   SA Opt. 2 (FR2)(FR1)              (FR1)</td></tr><tr><td rowspan=1 colspan=1>Base functions</td><td rowspan=1 colspan=1>WG3: E2, xApp; WG2: A1</td></tr><tr><td rowspan=1 colspan=1>PNF, VNF, CNF</td><td rowspan=1 colspan=1>WG6: VNF, CNF</td></tr><tr><td rowspan=1 colspan=1>O-Cloud</td><td rowspan=1 colspan=1>WG6: 02</td></tr><tr><td rowspan=1 colspan=1>Location (Edge,Regional site)</td><td rowspan=1 colspan=1>WG6: Edge</td></tr><tr><td rowspan=1 colspan=1>xApps</td><td rowspan=1 colspan=1>Traffic Steering, QoE/QoS</td></tr><tr><td rowspan=1 colspan=1>Advanced usecases (such asNetworkSlicing)</td><td rowspan=1 colspan=1>Massive MIMO Beamforming Optimization (WG1), RAN sharing (WG1)</td></tr></table>

Table A-9: Operator #1 inputs – Subsystem Non-Real Time RIC   
Table A-10: Operator #1 inputs – Subsystem SMO   

<table><tr><td>Non-Real Time RIC</td><td>NSA Opt. 3x (FR1)</td><td>NSA Opt. 7x (FR1)</td><td>SA Opt. 5 (FR1)</td><td>SA Opt. 2 (FR1)</td><td>SA Opt. 2 (FR2)</td></tr><tr><td>Base functions</td><td>WG2: A1</td><td></td><td></td><td></td><td></td></tr><tr><td>PNF, VNF, CNF</td><td>WG6: VNF, CNF</td><td></td><td></td><td></td><td></td></tr><tr><td>Location (Edge, Regional site)</td><td>WG6: Regional</td><td></td><td></td><td></td><td></td></tr><tr><td>SMO</td><td>NSA Opt. 3x (FR1)</td><td>NSA Opt. 7x (FR1)</td><td>SA Opt. 5 (FR1)</td><td>SA Opt. 2 (FR1)</td><td>SA Opt. 2 (FR2)</td></tr><tr><td>Base functions</td><td>WG1: 01</td><td></td><td></td><td></td><td></td></tr></table>

Table A-11: Operator #1 inputs – Subsystem xApp   

<table><tr><td>xApps</td><td>NSA Opt. 3x (FR1)</td><td>NSA Opt. 7x (FR1)</td><td>SA Opt. 5 (FR1)</td><td>SA Opt. 2 (FR1)</td><td>SA Opt. 2 (FR2)</td></tr><tr><td>WG3 xApps</td><td>Traffic Steering, QoE/QoS</td><td></td><td></td><td></td><td></td></tr></table>

# A.2 Operator #2 inputs

# Deployment Scenario

1. Indoors Small Cell   
2. 5G NR FR1 2.6GHz, 4.9GHz – TDD   
3. Maximum Channel Bandwidth (CHBW) 100MHz   
4. Leverages WG4 Shared Cell feature with combination of both FHM and Cascade modes

# Deployment Options and Evolution

1. NR NSA Option 3x   
2. NR SA Option 2

# Subsystems

1. Phase 1: O-RU, FHGW, O-DU/O-CU-CP/O-CU-UP (integrated unit) and Server   
2. Phase 2: O-RU, FHGW, O-DU/O-CU-CP/O-CU-UP (integrated unit), AAL and Server

Refer to [4][11][12] for more details on the FHGW.

![](images/b5f7e8f2971cacbaab6c747ac94634b9fd42ca0cf13f017df405dceb9e635120.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure A-4: Operator #2 Deployment Scenario #1 (FR1) – Phase 1

![](images/93ba73ce03b5f588f4f68f7998a32b4726399f9e8106af7eff6a23d965047460.jpg)

> **Image Summary:** {"image": "image_of_5G_O-RAN_specification.png"}
  
Figure A-5: Operator #2 Deployment Scenario #1 (FR1) – Phase 2

# A.3 Operator #3 inputs

# Deployment Scenario

1. Outdoor Macro Cell Deployment   
2. 5G NR FR1 n66, n70, n71, n29, n26   
3. Total Channel Bandwidth (CHBW) 150MHz

# Deployment Options and Evolution

1. NR SA Option 2

# O-RAN Deployment Blueprints variants and corresponding Subsystems

1. Refer to Figure A-6: O-RU, O-DU at Cell site, O-CU-CP, and O-CU-UP at Regional cloud, AAL and Server   
2. Refer to Figure A-7: O-RU, O-DU at Local cloud, O-CU-CP, and O-CU-UP at Regional cloud, AAL and Server

# Use Cases focuses

1. White Box Hardware and Open Interfaces   
2. Near-RT RIC (edge-cloud) and Non-RT-RIC Use Cases (Regional cloud): Traffic Steering, QoS /QoE Optimization and Slicing   
3. Cloud Deployment

![](images/3229a7d9633504958fe0943479b885845d1e8361d6e5ed3fb78aeb6c5ee75369.jpg)

> **Image Summary:** {"image": "image.png"}
  
The circles at both ends of each line indicate the endpoints of each interface

![](images/7121b34e6b5a3135232929bafb1f8f73ee35496d21159f6bea3f7583c3dd2a2e.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure A-6: Operator #3 Deployment Scenario #1 – SA (FR1)   
Figure A-7: Operator #3 Deployment Scenario #2 – SA (FR1)

# A.4 Operator #4 inputs

# Deployment Scenario

1. Outdoor Small Cell, Outdoor Macro Cell, Indoors Small Cell   
2. 5G NR FR1 TDD (3.7GHz, 4.5GHz), 5G NR FR2 TDD (28GHz)   
3. Maximum Channel Bandwidth (CHBW) 100MHz for FR1 and 400MHz for FR2

# Deployment Blueprints variants and corresponding Subsystems

Table A-12: Operator #4 inputs – Deployment Blueprint variants   

<table><tr><td rowspan=1 colspan=1>Deploymentvariants</td><td rowspan=1 colspan=1>NSA Opt. 3x(NSA1)</td><td rowspan=1 colspan=1>NSA Opt. 3x(NSA2)</td><td rowspan=1 colspan=1>SA Opt. 2(SA1)</td><td rowspan=1 colspan=1>NSA Opt. 3x(NSA3)</td><td rowspan=1 colspan=1>NSA Opt. 3x(NSA4)</td><td rowspan=1 colspan=1>SA Opt. 2(SA2)</td></tr><tr><td rowspan=2 colspan=1>Subsystems</td><td rowspan=2 colspan=1>O-RU,Integrated O-DU/O-CU-CP/O-CU-UP</td><td rowspan=1 colspan=1>O-RU,Integrated O-</td><td rowspan=1 colspan=1>O-RU,</td><td rowspan=2 colspan=1>Integrated O-RU/O-DU, O-CU-CP/O-CU-UP</td><td rowspan=2 colspan=1>O-RU,Integrated O-DU/O-CU-CP/O-CU-UP,Near-RT RIC,xApps, SMO</td><td rowspan=2 colspan=1>O-RU,Integrated O-DU/O-CU-CP/O-CU-UP,O-Cloud, SMO</td></tr><tr><td rowspan=1 colspan=1>DU/O-CU-CP/O-CU-UP,(Shared Cell)FHM</td><td rowspan=1 colspan=1>Integrated O-DU/O-CU-CP/O-CU-UP</td></tr><tr><td rowspan=1 colspan=1>Interfacesunder Test</td><td rowspan=1 colspan=1>X2, OFH,WG4 M-PlaneHierarchical</td><td rowspan=1 colspan=1>X2, OFH, WG4M-PlaneHierarchical</td><td rowspan=1 colspan=1>OFH, WG4 M-PlaneHierarchical</td><td rowspan=1 colspan=1>X2, F1</td><td rowspan=1 colspan=1>X2, OFH, WG4M-PlaneHierarchical, A1E2 is an internalinterface</td><td rowspan=1 colspan=1>OFH, WG4 M-PlaneHierarchical,01,02, 0-Cloud APIs</td></tr><tr><td rowspan=1 colspan=1>PNF, VNF</td><td rowspan=1 colspan=1>All PNFs</td><td rowspan=1 colspan=1>All PNFs</td><td rowspan=1 colspan=1>All PNFs</td><td rowspan=1 colspan=1>All PNFs</td><td rowspan=1 colspan=1>All PNFs</td><td rowspan=1 colspan=1>Virtualized Integrated O-DU/O-CU-CP/O-CU-UPRest are PNFs</td></tr><tr><td rowspan=1 colspan=1>FigureReference</td><td rowspan=1 colspan=1>Figure A-8</td><td rowspan=1 colspan=1>Figure A-8</td><td rowspan=1 colspan=1>Figure A-9</td><td rowspan=1 colspan=1>Figure A-10</td><td rowspan=1 colspan=1>Figure A-11</td><td rowspan=1 colspan=1>Figure A-12</td></tr><tr><td rowspan=1 colspan=1>Reference toWG6 CAD[4]</td><td rowspan=1 colspan=1>Based onScenario A inAppendix 7.1</td><td rowspan=1 colspan=1>Based onScenario A inAppendix 7.1</td><td rowspan=1 colspan=1>Based onScenario A/B inSection 6.1</td><td rowspan=1 colspan=1>Based onScenario A/B inAppendix 7.1</td><td rowspan=1 colspan=1>Based onScenario A inAppendix 7.1</td><td rowspan=1 colspan=1>Based onScenario A/B inSection 6.1</td></tr></table>

![](images/b06cc41c5f4efbd54ba67199f79538fd6760300b19b4ad37d596ea0876f5c746.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure A-8: Operator $\# 4$ Deployment Scenario #1 – NSA

![](images/49b347021d8d0da58779a52432623b5b2806fcf32e0e9c798bd4449f7e50fea8.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure A-9: Operator $\# 4$ Deployment Scenario #2 – SA

![](images/6ea50b2337cca13ed5d46639c18cf20023d7bc2a2a0c2f1222b1fc7a91112933.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure A-10: Operator #4 Deployment Scenario #3 – NSA

![](images/d6cc00796e4307f4f535202b10a0f32b99f8d6eff03aa23d920a4f22c0949ec9.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure A-11: Operator #4 Deployment Scenario #4 – NSA

![](images/fd2256944274a20ebf3b3bb6f4ad13c5356babf8156dcee1ee9e556d94955ea0.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure A-12: Operator $\# 4$ Deployment Scenario #5 – SA

# Annex B: O-RAN Software Community inputs on Testing Methodology

This annex provides an overview on the O-RAN Software Community (OSC) work and its current software releases and testing practices. Refer to the OSC wiki site for the most current information (https://wiki.o-ran-sc.org/).

The O-CU referred in this annex should be considered as O-CU CP/UP.

# B.1 O-RAN Software Community

The O-RAN Software Community (OSC) is an open source software development project aimed at providing an open source implementation of an end-to-end RAN system following O-RAN Alliance architecture and specifications. The OSC is hosted by the Linux Foundation and funded by the O-RAN Alliance.

The OSC is led by a 12-member Technical Oversight Committee (TOC) with its current members representing AT&T, China Mobile, Deutsche Telekom, Ericsson, Nokia, NTT DOCOMO, Orange, Radisys and Verizon.

The working effort of the OSC is organized into the following development projects:

• Operations and Maintenance (OAM)   
• Non-Realtime RAN Intelligent Controller (NONRTRIC)   
• Near-Realtime RAN Intelligent Controller Platform (RIC)   
• Near-Realtime RAN Intelligent Controller Applications (RICAPP)   
• O-RAN Central Unit (OCU)   
• O-RAN Distributed Unit High (ODUHIGH)   
• O-RAN Distributed Unit LOW (ODULOW)   
• Simulations (SIM)   
• Infrastructure (INF)   
• Documentation (DOC)   
• Integration and Testing (INT)   
subcommittee(s)   
• Requirements and Software Architecture Committee (RSAC)

The OSC conducts its business on open communication and development platforms including Zoom teleconferencing bridge, Groups.io mailing lists, Confluence wiki, and Git/Gerrit source code repositories. All O-RAN SC information and O-RAN SC developed software can be accessed via resources listed in Annex B.6.

# B.2 OSC Development Cycles

The OSC developed software is released on a bi-annual schedule, first in May/June time frame and the second in November/December. The naming scheme of releases follows color names in alphabetical order, with individual release names selected by community member voting. The first four releases are named Amber, Bronze, Cherry, and Dawn. The OSC delivered its first release, Amber release, in November 2019.

The high-level objectives and use cases for the next release are usually selected by the RSAC during the later portion of the current release cycle. The first several weeks of each release cycle typically are for the design and planning phase where the high-level release objectives are designed into implementable features and tasks, which are distributed to the OSC development projects. Following the planning phase is the development phase, during which the development projects and teams implement the agreed-upon features. This phase is divided into three-week sprints where each sprint has its own more manageable implementation and testing goals. Finally, prior to the release of the software, it is the testing phase, during which the integrated system testing and end-to-end use case testing are conducted, and the viability and quality of the software are verified and evaluated.

After each release, the OSC also institutes a maintenance window for the new release during the design and planning phase of the next release cycle. Normally this time window is used only for fixing major problems discovered after the release.

# B.3 OSC Software and Test Deployment Architecture

The OSC projects are set up based on the O-RAN Alliance architecture.

Figure B-1 below shows the relationship between OSC projects and the O-RAN architecture components.

![](images/1bb2653c583c058c53c66a2ce8c4eb56b6893b0935cc4d270f6cde117c352400.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure B-1: Relationship between OSC projects and the O-RAN architecture components

Figure B-2 depicts how the delivered software components by the OSC projects are deployed in the OSC Integration and Testing lab for Bronze release testing.

The deployment is spread across two Kubernetes clusters and two bare metal servers. From right to left, the first Kubernetes cluster is the SMO cluster, for components developed by the Non-Realtime RIC and OAM projects. The second Kubernetes cluster is the RIC cluster, for deploying components and microservices developed by the Near Realtime RIC Platform and the Near-Realtime RIC Applications projects. One of the bare-metal servers is used for running O-DU (both O-DO LOW and O-DU HIGH), and the other for running O-RU stub for peering the Open Fronthaul connection to the O-DU, over a dedicated 40GE link.

![](images/dcdbf515745fdcfc63ed8f32d023bb10e62ecd9175c300ea8b4264cba9923259.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure B-2: Deployment of OSC projects components in the OSC Integration and Testing lab for Bronze release

# B.4 OSC Release Objectives

# Amber (achieved)

• O-RAN SC level

o Continuous Integration (CI) flow implemented and all source code repositories integrated into the CI auto building process.   
o Source code repositories build into binary artifacts (i.e. docker container images, libraries, OS ISO media).   
o Documentation framework established, initial documentation in place.

Selected projects

o Near-Real Time RIC Platform and Near-Real Time RIC Applications:

“one-click” deployable.   
Completing xApp deployment flow, (pre-spec) E2 setup and subscription flow.

# Bronze (work in progress)

• O-RAN SC level

$\bigcirc$ Unit Test and SONAR reporting framework established.

o All participating projects “one-click” deployable.

o RSAC use cases:

▪ Health-check: including A1 and (pre-spec) O1 health check.   
▪ Traffic Steering: steering decision based on E2 information and AI/ML algorithm.   
▪ O-DU integration: O-DU HIGH communicate with O-DU LOW via FAPI.

# B.5 OSC Testing

OSC testing effort is divided into five levels

1. Unit testing (UT)

o UT is performed by the developers by implementing test cases using programming language specific unit testing and static code analysis framework.

o UT is triggered automatically every time when there is source code change submitted into the code repository for review.   
o At OSC level the INT project team provides support for unit test and code scan (i.e. static code analysis) integration into Linux Foundation Continuous Integration flow, and result reporting into the SONAR Cloud platform. Using the reports, TOC sets quality gates such as percentage of code covered by unit test cases, no major issues discovered, etc.

2. Project level integrated testing (PIT)

o Each development project is expected to conduct project level integrated testing, where all software components developed by the project are deployed into a single system for testing internal flows.   
o PIT is expected to be conducted by individual project teams, at the end of each development sprints or other development milestones.   
o At OSC level the INT project team organizes sprint demonstration fests regularly where development project teams gather and demonstrate achieved features in the previous sprint, using project level system deployment in project team’s own testing and demonstration environment.   
o The INT project team is also working with individual development projects on Robot testing framework-based testing flows that are to be integrated into Linux Foundation Continuous Integration flow. Such test flows serve as regression tests for implementation updates and can be triggered automatically by the CI system on a regular basis (e.g. daily) or upon new code submission.

3. Project pairwise testing (PPT)

o For projects that deliver O-RAN architectural components that interact with each other, PPT is conducted to ensure communication compatibility.   
o PPT sessions are organized by the INT project team, using either community testing lab or self-arrange testing facilities by involved projects.

4. System integrated testing (SIT)

o SIT is whole OSC software testing where all OSC development components are deployed into a single system. SIT focuses on overall system health, inter-project communication and application compatibility, overall system deployment flow, and resource requirements.   
o SIT is conducted by the INT project team using OSC community testing lab.   
o SIT is conducted during the testing phase of each release cycle.   
o Robot test framework-based health check test flows used as automated regression test.

5. Use case testing (UCT)

o UCT is whole OSC software testing where all OSC development components are deployed into a single system. UCT tests OSC deployment that has passed SIT.   
o UCT is conducted by the INT project team using OSC community testing lab.   
o UCT is conducted during the testing phase of each release cycle.   
o UCT uses Open Testing Framework (OTF), a test flow definition and orchestration tool that is developed as a sub-project under the INT.

# B.6 References

1. OSC Resources

a) Wiki: http://wiki.o-ran-sc.org   
b) Source code: http://gerrit.o-ran-sc.org   
c) Project management: http://jira.o-ran-sc.org   
d) Docker image registry: nexus3.o-ran-sc.org:10004 and nexus3.o-ran-sc.org:10002   
e) SONAR reporting: https://www.sonarcloud.io./organizations/o-ran-sc/projects   
f) Mailing lists: https://lists.o-ran-sc.org/g/main   
g) Meeting calendar: https://lists.o-ran-sc.org/calendar (member sign-in required)

2. Robot Framework: https://robotframework.org

# Annex C: Test Functions, Tools and Solutions for Subsystem and E2E System Testing

Table C-1 shows an example listing of the test functions, tools and solutions which can be used to establish test bed setups for Subsystem testing, Subsystem Pairing and Open Interfaces Interoperability testing and E2E System testing of the ORAN Deployment Blueprints.

These test functions and test tools are classified into the following categories as they can be used for setting up the test environment, providing active stimulus functions and passive measurements for test results verification purposes.

1. Test Case Scenario Creation: used to setup the testing environment and the necessary testing conditions which are required for executing the test case.   
2. Test Case Validation: used to collect measurements, KPIs, logs, packet captures for verifying, substantiating, troubleshooting, and debugging test results.

A single test function and tool can be used for both Test Case Scenario Creation and Test Case Validation.

Few notes for clarification purposes on the example listings of test functions and tools listed in this Annex C

1. These are non-exhaustive listings i.e. test functions and tools which are not listed in this Annex C can be used where appropriate.   
2. Not all the test functions and tools listed will be required for all test scenarios and test cases.   
3. Test functions and tools listed can be implemented each as a standalone test tool or multiple of these test functions can be combined into a single test tool.   
4. Few of the test functions might be combined into a single test tool (standalone test function usage is not possible).   
5. Real or emulated network elements / network functions can be used where appropriate.

This example listing will be expanded in the next release of this specification.

Table C-1: Subsystem and System Testing – Example listing of Test Functions and Tools   

<table><tr><td>No.</td><td>Test Functions and Tools</td><td>Abbreviation</td><td>Test Case Scenario Creation</td><td>Test Case Validation</td><td>Purpose</td><td>Subsystem and Subsystem Pairing and Open Interfaces Interoperabiity Testing</td><td>E2E System Test</td></tr><tr><td>1</td><td>Test UEs with Test SIMs (LTE, NR NSA, NR SA)</td><td>Test UE</td><td>Yes</td><td>Yes</td><td>Used for test cases which require UEs interactions with the SUT. Test UEs are typically UEs which are designed for commercial or testing applications with certain test and diagnostic functions enabled for test and measurements</td><td>Yes</td><td>Yes</td></tr><tr><td>2</td><td>Multi UEs Emulator (LTE, NR NSA, NRSA)</td><td>M-UE Emu</td><td>Yes</td><td>Yes</td><td>purposes. Used for test cases which require UEs interactions with the SUT.</td><td>Yes</td><td>Yes</td></tr><tr><td>3</td><td>Test Core Network</td><td>Test Core</td><td>Yes</td><td>Yes</td><td>Used to terminate Test UEs and/or UEs emulator NAS</td><td>Yes</td><td>Yes</td></tr></table>

<table><tr><td rowspan=1 colspan=9>Subsystem andTest Case                                           SubsystemTest Functions       E2ETest CasePairing andNo.                      Abbreviation Scenario                    Purpose                                  Systemand ToolsValidationOpen InterfacesCreation                                                                 Test InteroperabiityTesting</td></tr><tr><td rowspan=4 colspan=1></td><td rowspan=4 colspan=1>(EPC, NSAEPC, 5GC)</td><td rowspan=4 colspan=1></td><td rowspan=4 colspan=1></td><td rowspan=3 colspan=2></td><td rowspan=1 colspan=1>protocol and tosupport corenetwork proceduresrequired for RAN(SUT) testing.</td><td rowspan=4 colspan=1></td><td rowspan=4 colspan=1></td></tr><tr><td rowspan=2 colspan=1>Test Core Networkare typically Core</td></tr><tr><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>Networks which aredesigned forcommercialapplications and canbe used for testingthe RAN.</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>Core NetworkEmulator(EPC, NSAEPC, 5GC)</td><td rowspan=1 colspan=1>Core Emu</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=2>Yes</td><td rowspan=1 colspan=1>Used to terminateTest UEs and/orUEs emulator NASprotocol and tosupport corenetwork proceduresrequired for RAN(SUT) testing.</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>Test eNB orgNB(NSA, SA)</td><td rowspan=1 colspan=1>Test eNB orTest gNB</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=2>Yes</td><td rowspan=1 colspan=1>Used for test caseswhich require eNBor gNB interactionwith DUT/SUT.</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>eNB or gNBEmulator(NSA, SA)</td><td rowspan=1 colspan=1>eNB Emu orgNB Emu</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=2>Yes</td><td rowspan=1 colspan=1>Used for test caseswhich require eNBor gNB interactionwith DUT/SUT.</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>O-RU Emulatortesting the O-DU</td><td rowspan=1 colspan=1>O-RU OFHEmu</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=2>Yes</td><td rowspan=1 colspan=1>Used for test caseswhich require O-DUSubsystem testing.</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>No</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>O-DU Emulatortesting the O-RU</td><td rowspan=1 colspan=1>O-DU OFHEmu</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=2>Yes</td><td rowspan=1 colspan=1>Used for test caseswhich require O-RUSubsystem testing.</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>No</td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>O-DU Emulatortesting the O-CU-CP/O-CU-UP</td><td rowspan=1 colspan=1>O-DU F1 Emu</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=2>Yes</td><td rowspan=1 colspan=1>Used for test caseswhich require O-CU-CP/O-CU-UPSubsystem testing.</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>No</td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=2 colspan=1>O-CU-CP/O-CU-UPEmulatortesting the O-DU</td><td rowspan=2 colspan=1>O-CU-CP/O-CU-UPF1-C/F1-UEmu</td><td rowspan=2 colspan=1>Yes</td><td rowspan=2 colspan=2>Yes</td><td rowspan=2 colspan=1>Used for test caseswhich require O-DUSubsystem testing(in the case of O-DUis implemented as astandalone O-DU).</td><td rowspan=2 colspan=1>Yes</td><td rowspan=2 colspan=1>No</td></tr><tr><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>E2 NodeEmulator (O-CU-CP/O-CU-UP, O-DU)</td><td rowspan=1 colspan=1>O-CU-CP/O-CU-UP E2Emu or O-DUE2 Emu</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=2>Yes</td><td rowspan=1 colspan=1>Used for test caseswhich require Near-Real Time RIC andxApps Subsystemstesting.</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>No</td></tr><tr><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>ApplicationTest Server (akaTrafficGenerator)</td><td rowspan=1 colspan=1>App Test Svror Traffic Gen</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=2>Yes</td><td rowspan=1 colspan=1>Used for test caseswhich require bi-directional(downlink anduplink) user plane</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td></tr></table>

<table><tr><td colspan="4" rowspan="3">Test Functions                   Test CaseNo.                     Abbreviation Scenarioand ToolsCreation</td><td colspan="2" rowspan="3">Test CaseValidation  Purpose</td><td colspan="1" rowspan="3">SubsystemPairing andOpen InterfacesInteroperabilityTesting</td><td></td></tr><tr><td></td></tr><tr><td colspan="1" rowspan="1">E2ESystemTest</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">transfer test(s) to beperformed betweenthe Application TestServer and Test UEsand/or UEsemulator.</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">NetworkImpairmentEmulator</td><td colspan="1" rowspan="1">NW ImpairGen</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">Used for test caseswhich requireselective packetimpairments such as(but not limited to)over the OpenFronthaul (OFH)interface, X2 andothers asappropriate.</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Yes</td></tr><tr><td colspan="1" rowspan="2">13</td><td colspan="1" rowspan="2">Packet DelayInsertionGenerator</td><td colspan="1" rowspan="2">Pkt Delay Gen</td><td colspan="1" rowspan="2">Yes</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">Used for test caseswhich requireselective insertion ofpacket delay such as(but not limited to)over the OpenFronthaul (OFH)interface and othersas appropriate.</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="2">Yes</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Noting that fixeddelay can bemanaged via aspecifi length offiber as well asusing dedicated testtool.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="2">14</td><td colspan="1" rowspan="2">Transport andSynchronizationTester</td><td colspan="1" rowspan="2">TransportSync Tester</td><td colspan="1" rowspan="2">Yes</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Used for test caseswhich requirepassive and activetesting of transportnetwork across thefronthaul, midhaul,backhaul andsidehaul (Xn, X2) −S-Plane timing and</td><td colspan="1" rowspan="2">Yes</td><td colspan="1" rowspan="2">Yes</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">sync verificationacross all O-RANcomponents in bothsubsystem andsystem test cases.Supports eCPRItesting for O-RU, O-DU, FHM and FTN.</td></tr><tr><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">RF Attenuators</td><td colspan="1" rowspan="1">RF Atten.</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">Used for test caseswhich require radiosignals attenuationand can alsoimprove impedancematch, ensuringpower transfer fromsource to load isoptimized.</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Yes</td></tr><tr><td colspan="8" rowspan="1">SubsysSubsystemTest Functions                   Test Case   Test Case                          Pairing and     E2ENo.and ToolsAbbreviationScenarioValidationPurposeOpen InterfacesSystemCreationTest InteroperabilityTesting</td></tr><tr><td colspan="1" rowspan="1">16</td><td colspan="1" rowspan="1">ChannelEmulator</td><td colspan="1" rowspan="1">Channel Emu.</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">Used for test caseswhich require radiochannel emulation /impairments.</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Yes</td></tr><tr><td colspan="1" rowspan="1">17</td><td colspan="1" rowspan="1">RF Chamber</td><td colspan="1" rowspan="1">RF Chamber</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">Used for Over theAir (OTA) RFconnectivity to theO-RU(whereapplicable).</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Yes</td></tr><tr><td colspan="1" rowspan="1">18</td><td colspan="1" rowspan="1">Spectrum andSignal Analyzer</td><td colspan="1" rowspan="1">SpecAn orSigAnalyzer</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Used for test caseswhich require radiosignal and spectrumanalysis.</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Yes</td></tr><tr><td colspan="1" rowspan="1">19</td><td colspan="1" rowspan="1">Signal CreationSoftware</td><td colspan="1" rowspan="1">SCS</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Used to createwaveforms tostimulate NR andLTE test signals.</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">No</td></tr><tr><td colspan="1" rowspan="1">20</td><td colspan="1" rowspan="1">SignalGenerator</td><td colspan="1" rowspan="1">SigGen or SigGenerator</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">Used for test caseswhich require radiosignal generation.</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">No</td></tr><tr><td colspan="1" rowspan="1">21</td><td colspan="1" rowspan="1">Test UELogging Tool</td><td colspan="1" rowspan="1">Test UELoger</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Used for test resultsand KPIs reportingwhen Test UEsis/are used.</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Yes</td></tr><tr><td colspan="1" rowspan="2">22</td><td colspan="1" rowspan="2">ProtocolAnalyzer</td><td colspan="1" rowspan="2">ProtocolAnalyzer</td><td colspan="1" rowspan="2">No</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="2">Used for passivemonitoring of theInterface under Test(IUT) for test resultsverification andtroubleshootingpurposes such as(but not limited to)over the OpenFronthaul (OFH)interface, X2 andothers asappropriate.Test Tool can besplit into PacketCapture andProtocol Decoderfunctions. Thesecapabilities can beimplemented as asingle integrated testtool or separate testtools.</td><td colspan="1" rowspan="2">Yes</td><td colspan="1" rowspan="2">Yes</td></tr><tr><td colspan="1" rowspan="1">Yes</td></tr><tr><td colspan="1" rowspan="1">23</td><td colspan="1" rowspan="1">IQ Analyzer</td><td colspan="1" rowspan="1">IQA</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Used to analyze IQdata on theFronthaul interface.</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Yes</td></tr><tr><td colspan="1" rowspan="1">24</td><td colspan="1" rowspan="1">NetworkSynchronizationTiming Source</td><td colspan="1" rowspan="1">NW SyncTiming Source</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">Used as networktimingsynchronizationsource such as thePrecision-Time-</td><td colspan="1" rowspan="1">Yes</td><td colspan="1" rowspan="1">Yes</td></tr></table>

<table><tr><td rowspan=1 colspan=14>Subsystem andSubsystemTest Case   Test Case                           Pairing andNo.AbbreviationScenarioPurposeOpen InterfacesTest Functionsand Tools                                         ValidationCreation InteroperabilityTesting</td><td rowspan=1 colspan=1>E2ESystemTest</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=4></td><td rowspan=1 colspan=3></td><td rowspan=1 colspan=3></td><td rowspan=1 colspan=1>Protocol (PTP)Grand Master.</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=10 colspan=1>25</td><td rowspan=10 colspan=1>Test Controller/Automation</td><td rowspan=5 colspan=4></td><td rowspan=1 colspan=3></td><td rowspan=1 colspan=3></td><td rowspan=1 colspan=1>Used for testingorchestration and</td><td rowspan=10 colspan=2>Yes               Yes</td></tr><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=3></td><td rowspan=1 colspan=1>automation which</td></tr><tr><td rowspan=5 colspan=3></td><td rowspan=5 colspan=3></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>includes test cases</td></tr><tr><td rowspan=2 colspan=1>selection,scheduling,configuration of theDUT, SUT, Testfunctions and Tools</td></tr><tr><td rowspan=2 colspan=3></td></tr><tr><td rowspan=5 colspan=4>TestController andAutomation</td><td rowspan=2 colspan=1>in accordance to theselected test cases</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=2 colspan=3>Yes</td><td rowspan=2 colspan=3>Yes</td><td rowspan=2 colspan=1>and test conditions.Test tool stepsthrough theprocedures of thetest cases based onthe current statusand conditions ofthe test casesexecution. Testresults are analyzed</td></tr><tr><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2></td></tr><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=3></td><td rowspan=1 colspan=1>and reported afterthe execution of thetest cases.</td></tr></table>

![](images/37c5457d0e0a4edb019dfe37855d0e152de379f79bf4e161ed798b2ec05adb62.jpg)

> **Image Summary:** {"image": "image_3.png"}
  
Figure C-1 shows an example with the wrap around testing setup for E2E System under Test (SUT) with the Test functions and tools abbreviations updated.   
Figure C-1: Wrap around testing setup for E2E System under Test (SUT) with Test Functions/Tools Abbreviations updated

# Annex D: References to O-RAN WG6 Cloud Deployment Scenarios

Annex D shows additional Cloud Deployment Scenarios from [4] for NR Standalone (SA) operation in Figures D-1 to D-7 and NR Non-Standalone (NSA) operation in Figures D-8 to D-11. Refer to [4] for up-to-date information and details on the Cloud Deployment Scenarios.

The O-CU and vO-CU referred in [4] should be considered as O-CU CP/UP and vO-CU CP/UP, respectively.

![](images/610f45302dda866f05f9b54abbf308b3fde2eeebee07afbdcea44d42b456d17b.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure D-1: Cloud Deployment Scenario A for SA operation [4]

![](images/463e1068c5f0a1b945e891a4417adf561cfc4a2b43babade5a915ee797dbfb39.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure D-2: Cloud Deployment Scenario C for SA operation [4]

10

![](images/2128bf63fea6d2c7c50dbc76c70d01121eb00cd7c799268aea899def138e798d.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure D-3: Cloud Deployment Scenario C.1 for SA operation [4]

11

![](images/7198c15e0abecc78d7790ace4a048e392bb6ca7512a0765aad1776416b38f6fe.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure D-4: Cloud Deployment Scenario C.2 for SA operation [4]

![](images/59bbc67c852ed416fb80aaf9b97faa570fae02a34342adfdeef8cd086e057e80.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure D-5: Cloud Deployment Scenario D for SA operation [4]

3

![](images/711d22311ea2e164e6fe29142b2fecb9011fe5b879f7df5035ea2696b01558eb.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure D-6: Cloud Deployment Scenario E for SA operation [4]

5

![](images/17c04704a2d48dbc10968290a8c4fc9642e00977a35056c33c6e480d71169cf0.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure D-7: Cloud Deployment Scenario F for SA operation [4]

![](images/ab8a03f99870c3c420faf0f4081f6cda61eafb9a7140dd03b04eb93dc6895695.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure D-8: Cloud Deployment Scenario A for NSA operation [4]

![](images/4e62901d42e73061e6e25001bc62462bff9c9caf48f07614326123462233175e.jpg)

> **Image Summary:** {"image": "image.png"}
  
Figure D-9: Cloud Deployment Scenario C for NSA operation [4]

![](images/d8dcc7d8d4abd998d13b9284d28e4df6475fd16a006af92702bab20a4d9c1c5b.jpg)

> **Image Summary:** {"query": "Okay, I'm ready. Please provide the image."}
  
Figure D-10: Cloud Deployment Scenario C.2 for NSA operation [4]

![](images/03819cc49d860013c38e004edde856836145f7b75fbf1dedee472c591824e453.jpg)

> **Image Summary:** {"image": "image_of_5g_architecture.png"}
  
Figure D-11: Cloud Deployment Scenario D for NSA operation [4]

# Annex ZZZ: O-RAN Adopter License Agreement

BY DOWNLOADING, USING OR OTHERWISE ACCESSING ANY O-RAN SPECIFICATION, ADOPTER AGREES TO THE TERMS OF THIS AGREEMENT.

This O-RAN Adopter License Agreement (the “Agreement”) is made by and between the O-RAN Alliance and the entity that downloads, uses or otherwise accesses any O-RAN Specification, including its Affiliates (the “Adopter”).

This is a license agreement for entities who wish to adopt any O-RAN Specification.

# Section 1: DEFINITIONS

1.1 “Affiliate” means an entity that directly or indirectly controls, is controlled by, or is under common control with another entity, so long as such control exists. For the purpose of this Section, “Control” means beneficial ownership of fifty $( 5 0 \% )$ percent or more of the voting stock or equity in an entity.

1.2 “Compliant Implementation” means any system, device, method or operation (whether implemented in hardware, software or combinations thereof) that fully conforms to a Final Specification.

1.3 “Adopter(s)” means all entities, who are not Members, Contributors or Academic Contributors, including their Affiliates, who wish to download, use or otherwise access O-RAN Specifications.

1.4 “Minor Update” means an update or revision to an O-RAN Specification published by O-RAN Alliance that does not add any significant new features or functionality and remains interoperable with the prior version of an O-RAN Specification. The term “O-RAN Specifications” includes Minor Updates.

1.5 “Necessary Claims” means those claims of all present and future patents and patent applications, other than design patents and design registrations, throughout the world, which (i) are owned or otherwise licensable by a Member, Contributor or Academic Contributor during the term of its Member, Contributor or Academic Contributorship; (ii) such Member, Contributor or Academic Contributor has the right to grant a license without the payment of consideration to a third party; and (iii) are necessarily infringed by a Compliant Implementation (without considering any Contributions not included in the Final Specification). A claim is necessarily infringed only when it is not possible on technical (but not commercial) grounds, taking into account normal technical practice and the state of the art generally available at the date any Final Specification was published by the O-RAN Alliance or the date the patent claim first came into existence, whichever last occurred, to make, sell, lease, otherwise dispose of, repair, use or operate a Compliant Implementation without infringing that claim. For the avoidance of doubt in exceptional cases where a Final Specification can only be implemented by technical solutions, all of which infringe patent claims, all such patent claims shall be considered Necessary Claims.

1.6 “Defensive Suspension” means for the purposes of any license grant pursuant to Section 3, Member, Contributor, Academic Contributor, Adopter, or any of their Affiliates, may have the discretion to include in their license a term allowing the licensor to suspend the license against a licensee who brings a patent infringement suit against the licensing Member, Contributor, Academic Contributor, Adopter, or any of their Affiliates.

# Section 2: COPYRIGHT LICENSE

2.1 Subject to the terms and conditions of this Agreement, O-RAN Alliance hereby grants to Adopter a nonexclusive, nontransferable, irrevocable, non-sublicensable, worldwide copyright license to obtain, use and modify O-RAN Specifications, but not to further distribute such O-RAN Specification in any modified or unmodified way, solely in furtherance of implementations of an O-RAN Specification.

2.2 Adopter shall not use O-RAN Specifications except as expressly set forth in this Agreement or in a separate written agreement with O-RAN Alliance.

# Section 3: FRAND LICENSE

3.1 Members, Contributors and Academic Contributors and their Affiliates are prepared to grant based on a separate Patent License Agreement to each Adopter under Fair Reasonable And Non- Discriminatory (FRAND) terms and conditions with or without compensation (royalties) a nonexclusive, non-transferable, irrevocable (but subject to Defensive Suspension), non-sublicensable, worldwide patent license under their Necessary Claims to make, have made, use, import, offer to sell, lease, sell and otherwise distribute Compliant Implementations; provided, however, that such license shall not extend: (a) to any part or function of a product in which a Compliant Implementation is incorporated that is not itself part of the Compliant Implementation; or (b) to any Adopter if that Adopter is not making a reciprocal grant to Members, Contributors and Academic Contributors, as set forth in Section 3.3. For the avoidance of doubt, the foregoing licensing commitment includes the distribution by the Adopter’s distributors and the use by the Adopter’s customers of such licensed Compliant Implementations.

3.2 Notwithstanding the above, if any Member, Contributor or Academic Contributor, Adopter or their Affiliates has reserved the right to charge a FRAND royalty or other fee for its license of Necessary Claims to Adopter, then Adopter is entitled to charge a FRAND royalty or other fee to such Member, Contributor or Academic Contributor, Adopter and its Affiliates for its license of Necessary Claims to its licensees.

3.3 Adopter, on behalf of itself and its Affiliates, shall be prepared to grant based on a separate Patent License Agreement to each Members, Contributors, Academic Contributors, Adopters and their Affiliates under Fair Reasonable And NonDiscriminatory (FRAND) terms and conditions with or without compensation (royalties) a nonexclusive, nontransferable, irrevocable (but subject to Defensive Suspension), non-sublicensable, worldwide patent license under their Necessary Claims to make, have made, use, import, offer to sell, lease, sell and otherwise distribute Compliant Implementations; provided, however, that such license will not extend: (a) to any part or function of a product in which a Compliant Implementation is incorporated that is not itself part of the Compliant Implementation; or (b) to any Members, Contributors, Academic Contributors, Adopters and their Affiliates that is not making a reciprocal grant to Adopter, as set forth in Section 3.1. For the avoidance of doubt, the foregoing licensing commitment includes the distribution by the Members’, Contributors’, Academic Contributors’, Adopters’ and their Affiliates’ distributors and the use by the Members’, Contributors’, Academic Contributors’, Adopters’ and their Affiliates’ customers of such licensed Compliant Implementations.

# Section 4: TERM AND TERMINATION

4.1 This Agreement shall remain in force, unless early terminated according to this Section 4.

4.2 O-RAN Alliance on behalf of its Members, Contributors and Academic Contributors may terminate this Agreement if Adopter materially breaches this Agreement and does not cure or is not capable of curing such breach within thirty (30) days after being given notice specifying the breach.

4.3 Sections 1, 3, 5 - 11 of this Agreement shall survive any termination of this Agreement. Under surviving Section 3, after termination of this Agreement, Adopter will continue to grant licenses (a) to entities who become Adopters after the date of termination; and (b) for future versions of O-RAN Specifications that are backwards compatible with the version that was current as of the date of termination.

# Section 5: CONFIDENTIALITY

Adopter will use the same care and discretion to avoid disclosure, publication, and dissemination of O-RAN Specifications to third parties, as Adopter employs with its own confidential information, but no less than reasonable care. Any disclosure by Adopter to its Affiliates, contractors and consultants should be subject to an obligation of confidentiality at least as restrictive as those contained in this Section. The foregoing obligation shall not apply to any information which is: (1) rightfully known by Adopter without any limitation on use or disclosure prior to disclosure; (2) publicly available through no fault of Adopter; (3) rightfully received without a duty of confidentiality; (4) disclosed by O-RAN Alliance or a Member, Contributor or Academic Contributor to a third party without a duty of confidentiality on such third party; (5) independently developed by Adopter; (6) disclosed pursuant to the order of a court or other authorized governmental body, or as required by law, provided that Adopter provides reasonable prior written notice to O-RAN Alliance, and cooperates with O-RAN Alliance and/or the applicable Member, Contributor or Academic Contributor to have the opportunity to oppose any such order; or (7) disclosed by Adopter with O-RAN Alliance’s prior written approval.

# Section 6: INDEMNIFICATION

Adopter shall indemnify, defend, and hold harmless the O-RAN Alliance, its Members, Contributors or Academic Contributors, and their employees, and agents and their respective successors, heirs and assigns (the “Indemnitees”), against any liability, damage, loss, or expense (including reasonable attorneys’ fees and expenses) incurred by or imposed upon any of the Indemnitees in connection with any claims, suits, investigations, actions, demands or judgments arising out of Adopter’s use of the licensed O-RAN Specifications or Adopter’s commercialization of products that comply with O-RAN Specifications.

# Section 7: LIMITATIONS ON LIABILITY; NO WARRANTY

EXCEPT FOR BREACH OF CONFIDENTIALITY, ADOPTER’S BREACH OF SECTION 3, AND ADOPTER’S INDEMNIFICATION OBLIGATIONS, IN NO EVENT SHALL ANY PARTY BE LIABLE TO ANY OTHER PARTY

OR THIRD PARTY FOR ANY INDIRECT, SPECIAL, INCIDENTAL, PUNITIVE OR CONSEQUENTIAL DAMAGES RESULTING FROM ITS PERFORMANCE OR NON-PERFORMANCE UNDER THIS AGREEMENT, IN EACH CASE WHETHER UNDER CONTRACT, TORT, WARRANTY, OR OTHERWISE, AND WHETHER OR NOT SUCH PARTY HAD ADVANCE NOTICE OF THE POSSIBILITY OF SUCH DAMAGES. O-RAN SPECIFICATIONS ARE PROVIDED “AS IS” WITH NO WARRANTIES OR CONDITIONS WHATSOEVER, WHETHER EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE. THE O-RAN ALLIANCE AND THE MEMBERS, CONTRIBUTORS OR ACADEMIC CONTRIBUTORS EXPRESSLY DISCLAIM ANY WARRANTY OR CONDITION OF MERCHANTABILITY, SECURITY, SATISFACTORY QUALITY, NONINFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, ERROR-FREE OPERATION, OR ANY WARRANTY OR CONDITION FOR O-RAN SPECIFICATIONS.

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