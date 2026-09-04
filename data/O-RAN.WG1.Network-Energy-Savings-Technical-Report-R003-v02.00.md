# O-RAN Work Group 1 (Use Cases and Overall Architecture)

# Network Energy Saving Use Cases Technical Report

Copyright $\circledcirc$ 2023 by the O-RAN ALLIANCE e.V.

# Contents

Foreword.. 5

Modal verbs terminology ............................ .......................................................................................................5   
1 Scope ........... ............................................................................................................................................6   
2 References ................. .......... ....................... ..................................................................................... .......6   
2.1 Informative references ......... ............................................................................................ 6   
3 Definition of terms, symbols and abbreviations...... ......................................................................... .....7   
3.1 3.2 Terms .................Symbols ............. ................................................................................................... ...... 7...... 7   
............................................................................................................................ 7   
4 Objectives and Requirements... ....... .....8   
4.1 Objectives ......... ............................................................................................................ ....... 8   
4.2 Requirements ..................................................................................................................................................... 9   
5 Carrier and Cell Switch Off/On ........ ........................................................................................10   
5.1 Problem Statement, Solution and Value Proposition ....................................................................................... 10   
5.2 Architecture/Deployment Options ........ ........................................................................................................... 11   
5.2.1 Option 1: Non-RT RIC Deployment .......................................................................................................... 11   
5.2.1.1 Description and UML Diagram ............................................................................................................ 11   
5.2.1.2 O-RAN Entity Roles............................................................................................................................. 14   
5.2.1.3 Input/Output Data Requirements .......................................................................................................... 14   
5.2.1.3.1 Summary ........... ..................................................................................................................... 14   
5.2.1.3.2 Detailed Input Requirements .......................................................................................................... 15   
5.2.1.3.3 Detailed Output Requirements ........................................................................................................ 18   
5.2.2 Option 2: Near-RT RIC Deployment ......................................................................................................... 19   
5.2.2.1 Description and UML Diagram ............................................................................................................ 19   
5.2.2.2 O-RAN Entity Roles...... ...................................................................................................................... 22   
5.2.2.3 Input/Output Data Requirements .......................................................................................................... 22   
5.2.2.3.1 Summary ....... .................................................................................................................. 22   
5.2.2.3.2 Detailed Input Requirements .......................................................................................................... 24   
5.2.2.3.3 Detailed Output Requirements ........................................................................................................ 27   
5.3 Impact Analysis on O-RAN Work Groups ...................................................................................................... 27   
5.4 Relation and Impact on 3GPP Specifications .................................................................................................. 29   
5.4.1 Relation to 3GPP RAN Specifications ....................................................................................................... 29   
5.4.2 Ongoing Work in 3GPP Rel.18 RAN........ ................................................................................................. 29   
5.4.3 Impact on 3GPP RAN Specifications ........ ........................................................................................... 30   
5.4.4 Relation to 3GPP System Architecture Specifications ............................................................................... 30   
5.4.5 Ongoing Work in 3GPP Rel.18 System Architecture .. .............................................................................. 31   
5.4.6 Impact on 3GPP System Architecture Specifications ................................................................................ 31   
5.5 Gain Analysis.............. ............................................................ 31   
5.5.1 Cell and Carrier Switch Off/On Energy Saving for 4T4R O-RU............................................................... 33   
5.5.2 Cell and Carrier Switch Off/On Energy Saving for 64T64R O-RU ........................................................... 34   
5.6 Feasibility Analysis.......... ............................................................. 35   
6 RF Channel Reconfiguration... .................................................................................36   
6.1 Problem Statement, Solution and Value Proposition ....................................................................................... 36   
6.2 Architecture/Deployment Options ................................................................................................................... 37   
6.2.1 Option 1: Non-RT RIC Deployment .......................................................................................................... 37   
6.2.1.1 Description and UML Diagram ............................................................................................................ 38   
6.2.1.2 O-RAN Entity Roles............................................................................................................................. 41   
6.2.1.3 Input/Output Data Requirements .......................................................................................................... 41   
6.2.1.3.1 Summary ......................................................................................................................................... 41   
6.2.1.3.2 Detailed Input Requirements .......................................................................................................... 43   
6.2.1.3.3 Detailed Output Requirements ........................................................................................................ 47   
6.2.2 Option 2: Near-RT RIC Deployment ......................................................................................................... 47   
6.2.2.1 Description and UML Diagram .. . 48   
6.2.2.2 O-RAN Entity Roles...................... ........................................................................................ . 51   
6.2.2.3 Input/Output Data Requirements. . 52   
6.2.2.3.1 Summary ...... ..................................................................................... . 52   
6.2.2.3.2 Detailed Input Requirements .... ........................................................................ . 53   
6.2.2.3.3 Detailed Output Requirements ........................................................................................................ 56   
6.3 6.4 Impact Analysis on O-RAN Work Groups ...................................................................................................... 56Relation and Impact on 3GPP Specifications .................................................................................................. 58   
6.5 Gain Analysis........... ....................................................... . 58   
6.5.1 RF Channel Reconfiguration ES Gain Analysis for 4T4R O-RU ..... ............................................ ... 58   
6.5.2 RF Channel Reconfiguration ES Gain Analysis for 64T64R O-RU . ...................................... . 60   
6.6 Feasibility Analysis.......... .................................................................. 61   
6.6.1 Continuous operation during RF Channel Reconfiguration .... ............................................ ... 61   
6.6.2 Impact on Coverage ................ ..................................................... ..... 61   
6.6.3 Impact and Relation to UE specific Base Station Algorithms.. . 61   
6.6.4 Limited O-RU / O-DU Capabilities .... ....................................................... ........ 61   
7 Advanced Sleep Mode Selection... ............................................................... ....62   
7.1 Problem Statement, Solution and Value Proposition ... ............................................................................ ..... 62   
7.2 Architecture/Deployment Options ............. ............................................................................. 64   
7.2.1 Option 1: Training and Inference in Non-RT RIC . . 64   
7.2.1.1 Description and UML Diagram ..... .................................................................... ..... 65   
7.2.1.2 O-RAN Entity Roles..... ......................................... . 69   
7.2.1.3 7.2.2 Void ...................................................................................................................................................... 69Option 2: Training in Non-RT RIC and Inference in Near-RT RIC .......................................................... 69   
7.2.2.1 Description and UML Diagram ....... ............................................. ... 70   
7.2.2.2 O-RAN Entity Roles.... ............................................................................... . 74   
7.2.2.3 Void ........ ........................................................... .. 74   
7.3 Impact Analysis on O-RAN Work Groups ..... ................................................................................ . 75   
7.4 Relation and Impact on 3GPP Specifications . ............................................................... . 76   
7.5 7.6 Void ............................Feasibility Analysis..... ................................................. ... 76... 76   
7.6.1 Impact to Continuous Operation during Advance Sleep Modes . .. 76   
7.6.2 7.6.3 Impact to Coverage .................................................................................................................................... 76Impact and Relation to Vendor Specific Scheduling Algorithms............................................................... 77   
7.6.4 Limited O-RU/O-DU Capabilities ............ ......................................................................... 77   
8 O-Cloud Resource Energy Saving Mode ..... ..................................................... ....78   
8.1 Sub Use Case 1: O-Cloud Node Shutdown .... . 78   
8.1.1 Problem Statement, Solution and Value Proposition . .................................................................... .. 78   
8.1.2 Architecture/Deployment Option .... .................................................................. . 79   
8.1.2.1 Description and UML Diagram ............................................................................................................ 81   
8.1.2.2 8.1.2.3 O-RAN Entity Roles............................................................................................................................. 85Void ...................................................................................................................................................... 85   
8.1.3 Impact Analysis on O-RAN Work Groups ....................................................................................... . 86   
8.1.4 Relation and Impact on 3GPP Specifications ................................................................................... . 86   
8.1.5 Void.............. ........................................................................................ . 86   
8.1.6 Feasibility Analysis ..... ........................................................................................ . 86   
8.1.6.1 Service Continuity during NF relocation....... ............................................................................ . 86   
8.1.6.2 Pooling vs. Scaling Gains ........ ....................................................................... ... 86   
8.1.6.3 8.2 Start-up Time for Scale Out Operation ................................................................................................. 86Sub Use Case 2: O-Cloud CPU Energy Saving Mode..................................................................................... 87   
8.2.1 Problem Statement, Solution and Value Proposition ....................................................................... . 87   
8.2.2 Architecture/Deployment Option .......... ................................................................................................... 88   
8.2.2.1 Description and UML Diagram .. .......................................................... ... 89   
8.2.2.2 8.2.2.3 O-RAN Entity Roles...... Void ............ .................................................................................... ... 92... 92   
8.2.3 Impact Analysis on O-RAN Work Groups ...... ........................................................................... . 92   
8.2.4 Relation and Impact on 3GPP Specifications..... ............................................................................ . 92   
8.2.5 Void....................... ......................................................... . 93   
8.2.6 Feasibility Analysis ........... ........................................... ... 93   
8.2.6.1 Not to Restrict Fast CPU Energy Saving Mode Switching . . 93

9 Summary and Conclusion .. ..94

Annex A (Informative): Design Principles for NES Features ... ..96

Annex B (Informative): Load profile and O-RU functional blocks . ..98

Annex C (Informative): O1 interface principles.. ..100

Annex D (Informative): Examples of Advanced Sleep Modes .. .104

Revision history.............. ..105

History .... .105

# Foreword

This Technical Report (TR) has been produced by O-RAN Alliance.

# Modal verbs terminology

In the present document "shall", "shall not", "should", "should not", "may", "need not", "will", "will not", "can" and "cannot" are to be interpreted as described in clause 3.2 of the O-RAN Drafting Rules (Verbal forms for the expression of provisions).

"must" and "must not" are NOT allowed in O-RAN deliverables except when used in direct citation.

# 1 Scope

The contents of the present document are subject to continuing work within O-RAN and may change following formal O-RAN approval. Should O-RAN modify the contents of the present document, it will be re-released by O-RAN with an identifying change of release date and an increase in version number as follows:

Version x.y.z where:

x the first digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc. (the initial approved document will have $\scriptstyle \mathbf { X } = 0 1$ ).   
y the second digit is incremented when editorial only changes have been incorporated in the document.   
z the third digit included only in working versions of the document indicating incremental changes during the editing process.

The present document provides a technical report on Network Energy Saving use cases.

# 2 References

# 2.1 Informative references

References are either specific (identified by date of publication and/or edition number or version number) or non-specific. For specific references, only the cited version applies. For non-specific references, the latest version of the referenced document (including any amendments) applies.

NOTE: While any hyperlinks included in this clause were valid at the time of publication, O-RAN cannot guarantee their long-term validity.

The following referenced documents are not necessary for the application of the present document but they assist the user with regard to a particular subject area.

[1] 3GPP TR 21.905, Vocabulary for 3GPP Specifications   
[2] ETSI ES 203 228, Environmental Engineering (EE); Assessment of mobile network energy efficiency   
[3] O-RAN Technical Specification, O-RAN Architecture Description   
[4] O-RAN Technical Specification, Non-RT RIC Architecture   
[5] O-RAN Technical Report, Cloud Architecture and Deployment Scenarios for O-RAN Virtualized RAN   
[6] O-RAN Technical Specification, Use Cases Detailed Specification   
[7] 3GPP TS 28.554, Management and orchestration; 5G end to end Key Performance Indicators (KPI)   
[8] 3GPP TS 28.310, Management and orchestration; Energy efficiency of 5G   
[9] 3GPP TS 38.300, NR; NR and NG-RAN Overall Description, Stage-2   
[10] ETSI ES 202 706-1, Metrics and measurement method for energy efficiency of wireless access network equipment; Part 1: Power consumption - static measurement method

[11] 3GPP TS 28.541, Management and orchestration; 5G Network Resource Model (NRM); Stage 2 and stage 3

[12] 3GPP TS 28.552, Management and orchestration; 5G performance measurements [13] 3GPP TS 32.425, Telecommunication management; Performance Management (PM); Performance measurements Evolved Universal Terrestrial Radio Access Network (E-UTRAN)

[14] 3GPP TS 32.451, Telecommunication management; Key Performance Indicators (KPI) for Evolved Universal Terrestrial Radio Access Network (E-UTRAN); Requirements

[15] 3GPP TS 32.551, Telecommunication management; Energy Saving Management (ESM); Concepts and requirements

[16] 3GPP TS 38.331, NR; Radio Resource Control (RRC); Protocol specification [17] O-RAN Technical Specification, O-RAN Outdoor Macrocell Hardware Architecture and Requirements (FR1)

[18] O-RAN Technical Specification, O-RAN Operations and Maintenance Interface Specification [19] 3GPP TR 38.864, Study on network energy savings for NR [20] O-RAN Technical Specification, O2 Interface General Aspects and Principles

# 3 Definition of terms, symbols and abbreviations

# 3.1 Terms

For the purposes of the present document, the terms and definitions given in 3GPP TR 21.905 [1] and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in 3GPP TR 21.905 [1].

Energy Efficiency: relation between the useful output and energy/power consumption as defined in ETSI ES 203 228 [2]

Energy Consumption: integral of power consumption over time as defined in ETSI ES 202 706-1 [10]

# 3.2 Symbols

No symbol is defined in this TR.

# 3.3 Abbreviations

For the purposes of this document, the abbreviations given in 3GPP TR 21.905 [1], 3GPP TS 38.300 [9], ETSI ES 203 228 [2], O-RAN.WG1.O-RAN-Architecture-Description [3], O-RAN.WG6.CADS [5] apply.

# 4 Objectives and Requirements

# 4.1 Objectives

This Technical Report captures the outcome of the WG1 UCTG Network Energy Saving pre-normative phase. The objectives of the pre-normative phase are as follows:

study and investigate all required counters/KPI’s for monitoring and reporting of Energy Consumption and Energy Efficiency in real time for all O-RAN defined nodes such as O-RU, O-DU, O-CU as well as 3GPP defined logical components of network such as Cell, Carrier, gNB,   
study requirements, key issues, proposed solutions, benefits of the Energy Saving proposals, study potential impact and required enhancements to O-RAN interfaces such as E2, O1, A1, FH Mplane, FH CUS-Plane, R1, and Near-RT RIC API,   
study potential impact and required enhancements on data models of all O-RAN entities,   
identify the any possible impact on Non-RT RIC architecture, Near-RT RIC architecture and AI/ML workflow.

The use cases studied in the NES pre-normative phase are:

Carrier and Cell Switch Off/On RF Channel Reconfiguration Off/On Advanced Sleep Mode Selection O-Cloud Resource Energy Saving Mode

Algorithms discussed and analyzed as part of the Network ES pre-normative phase will be examples only and will not be part of any specification as outcome of this pre-normative phase or subsequent work items.

For each use case solution proposal, the detailed objectives are:

Review, evaluate applicability of, and select from existing deployment alternatives (Non-RT and/or   
Near-RT RIC) and AI/ML deployment scenarios and document respective findings: • Evaluate energy savings gains based on a E2 Node/O-RU/PNF/VNF energy consumption model using evaluation metrics/KPIs and including assessment of impact on network and user performance. Study on a per sub-use case basis potential impact and enhancements on O-RAN interfaces (e.g. O1, O2, A1, E2, O-FH) in terms of required input data and output configuration data. Review existing counters, KPIs, and data models as specified/studied in 3GPP. Study potential enhancements on existing counters, KPIs, and data models or define new counters, KPIs, and data models of all involved O-RAN entities.

NES use cases should reuse the existing 3GPP measurements and measurement reporting for input data as well as the existing 3GPP configuration and provisioning management for the output data as much as possible.

If new measurements or configuration parameters are essential to support new NES use cases, then these should preferably be based on parameters, variables, definitions and procedures that are already used in the 3GPP/ORAN specifications. The current standardization approach (specifying the new measurement in 3GPP specifications and referring to it in O-RAN specifications) should be prioritized over inventing new standardization approaches.

# 4.2 Requirements

This TR shall capture Energy consumption and Energy Efficiency related counters and KPIs including the following:

# O-RU Specific KPIs

Energy Efficiency and power consumption KPIs provided by real-time metering.

# O-CU/O-DU Hardware & Software / O-Cloud Software & Platform KPIs

O-CU/O-DU hardware (e.g., CPU, accelerators, NIC cards, fans and power supply, etc.) shall have the capability to measure and report power consumption values to the O-Cloud. The O-Cloud software shall be able to collect measurement data at the hardware component level (e.g., CPU, NIC, accelerator card, fans and power supply, etc.) and provide power, energy and environmental (PEE) parameters/KPIs. O-Cloud shall be able to report EE through O2 interface to the SMO or through North-Bound Interfaces (NBI) to external tools.   
The O-Cloud software shall be able to provide PEE parameters/KPIs at the workload level (e.g., pod, O-CU/O-DU CNF, etc.), as well as for the O-Cloud platform software components themselves. OCloud shall be able to report energy efficiency through O2 interface to the SMO or through NBI to external tools.   
O-CU and O-DU shall provide CNF level energy efficiency counters/KPIs (e.g., power consumption, Traffic load, data volume, throughput), which shall be reported through O1 interface to the SMO or through NBI to external tools.

# 5 Carrier and Cell Switch Off/On

# 5.1 Problem Statement, Solution and Value Proposition

Mobile networks often utilize multiple frequency layers (carriers) to cover the same service area. At low load, i.e. when the expected traffic volume is lower than a fixed threshold, ES can be achieved by switching off one or more carriers or entire cells without impairing the user experience. UEs previously served by the carrier or cell will be offloaded by the E2 Node to a new target carrier or cell prior to the switch off.

However, the switch off/on decisions are not a trivial task. There are conflicting targets between system performance and energy savings. Other carriers and/or cells will have to serve the additional traffic and traffic is changing over time. E2 Nodes support a number of techniques effecting energy consumption which might also be load dependent. While energy savings for the switched off carrier and/or cell is maximized, the overall energy consumption of the network might even increase.

Carrier and cell switch off/on control by the Non-RT or Near-RT RIC can consider overall network energy efficiency instead of local optimization. The switch off/on decision can optionally be made by an AI/ML model within the inference host, deployed at the Non-RT RIC (deployment option 1) or at the Near-RT RIC (deployment option 2) to further improve decision making. Among others, the AI/ML models' functionality may include prediction of future traffic, user mobility, and resource usage and may also predict expected energy efficiency enhancements, resource usage, and network performance for different ES optimization states.

Before switching off/on carrier(s) and/or cell(s), the E2 Node may need to perform some preparation actions for off switching (e.g. check ongoing emergency calls and warning messages, to enable, disable, modify Carrier Aggregation and/or Dual Connectivity, to trigger HO traffic and UEs from cells/carriers to other cells or carriers, informing neighbour nodes via X2/Xn interface etc.) as well as for on switching (e.g., cell probing, informing neighbour nodes via X2/Xn interface etc.).

# 5.2 Architecture/Deployment Options

5.2.1 Option 1: Non-RT RIC Deployment

In option 1, decision making, potentially including AI/ML Model Training and Inference, is done at the NonRT RIC.

# 5.2.1.1 Description and UML Diagram

Table 5.2.1.1-1: Carrier and Cell Switch Off/On: AI/ML inference via Non-RT RIC   

<table><tr><td rowspan=1 colspan=1>Use Case Stage</td><td rowspan=1 colspan=1>Evolution / Specification</td><td rowspan=1 colspan=1>&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td rowspan=1 colspan=1>Goal</td><td rowspan=1 colspan=1>Enable Carrier and Cell switch offon Energy Saving functions in theNetwork by means of configuration parameter change and Actionscontrolled by Non-RT RIC and allow for Al/ML-based solutions.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Actors and Roles</td><td rowspan=1 colspan=1>Non-RT RIC acting as inference host for Energy Savings decisionmaking.E2 Node and O-RU are the subject of action for configurationenforcement.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Assumptions</td><td rowspan=1 colspan=1>O1 interface connectivity is established.Open FH M-Plane interface is established between E2 Node and O-RUand/or SMO and O-RU directly.Network is operational.Non-RT RIC has knowledge about overlapping carriers/cells and thecoverage of those carriers/cells (e.g., which carrier/cell is a coveragelayer and which is a capacity layer).</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Pre-conditions</td><td rowspan=1 colspan=1>The operator has set the targets for Energy Saving functions in the Non-RT RIC.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Begins when</td><td rowspan=1 colspan=1>Operator enables the optimization functions for carrier and cell switchoff/on Energy Saving functions and E2 Node and O-RU becomeoperational.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 1 (M)</td><td rowspan=1 colspan=1>SMO initiates specific measurement data collection request towards E2Node and O-RU (via E2 Node and O-FH) for Al/ML model training andinference.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 2 (M)</td><td rowspan=1 colspan=1>E2 Node and O-RU send the configured measurement data to SMOperiodically or event based.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 3 (M)</td><td rowspan=1 colspan=1>Non-RT RiC retrieves the collected measurement data for processing.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 4 (M)</td><td rowspan=1 colspan=1>Non-RT RIC trains the Al/ML models with the collected data. TrainedAl/ML models are deployed, configured, and activated.Non-RT RIC constantly monitors(i) performance and energy consumption of the E2 Node(s)(i) energy consumption of O-RU(s)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 5 (M)</td><td rowspan=1 colspan=1>Based on the AI/ML inference the Non-RT RIC may request the SMO toconfigure E2 Node to prepare and execute cell or carrier switch off/on.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 6 (M)</td><td rowspan=1 colspan=1>SMO instructs E2 Node via O1 interface to perform the receivedrequest(s) from the Non-RT RIC. O-RU is informed about the updatedO-RU configuration via Open FH M-Plane interface by E2 Node. E2Node will notify SMO once cell or carrier switch off/on is completed.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 7 (M)</td><td rowspan=1 colspan=1>Non-RT RIC continuously analyzes performance of Al/ML model. Ifenergy saving objectives are not achieved, it may decide to initiatefallback mechanism, and/or Al/ML model update or retraining.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Ends when</td><td rowspan=1 colspan=1>E2 Node becomes non-operational or when the operator disables theoptimization functions for Energy Saving.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Exceptions</td><td rowspan=1 colspan=1>None.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Post Conditions</td><td rowspan=1 colspan=1>Non-RT RIC continues closed-loop monitoring of Energy Saving functionat E2 Node and O-RU.E2 Node(s) and O-RU(s) operate using the newly deployedparameters/models and state (off/on).</td><td rowspan=1 colspan=1></td></tr></table>

@startuml   
Skin rose   
skinparam defaultFontSize 12   
autonumber

Box "Service Management & \n Orchestration Framework" #gold

Participant "Collection & Control" as SMO Participant "Non-RT RIC" as NRTRIC

End box

Box "O-RAN Nodes" #lightpink Participant "Near-RT RIC" as RTRIC Participant "E2-Nodes" as E2NODES Participant "O-RUs" as ORUs

End box

group Data Collection   
autonumber 1.1   
SMO -> E2NODES $< < 0 1 > >$ Data collection request for Energy Saving E2NODES -> ORUs <<FH>> Data collection request for Energy Saving

autonumber 2.1

ORUs $- >$ E2NODES : <<FH>> Measurement Data Collection for Energy Saving E2NODES -> SMO $< < 0 1 > >$ Measurement Data Collection for Energy Saving autonumber 3   
SMO $- >$ NRTRIC : Data retrieval

end

group Data Analysis Training and Inference autonumber 4.1

NRTRIC $- >$ NRTRIC : Performance and Energy Consumption Monitoring \n(E2 Node(s) & ORU(s)) NRTRIC $- >$ NRTRIC : AI/ML Model training and inference

end

autonumber 5   
group Actor Decision Making NRTRIC -> SMO : Request to prepare and execute \nfor carrier(s) and cell(s) switch   
off/on

autonumber 6.1

SMO <-> E2NODES : <<O1>> E2-Node parameter configurations and recommendation for carrier(s) and cell(s) switch off/on, \nmessage response and/or notification of execution.

E2NODES <-> ORUs : <<FH>> Update O-RU Configurations \nand notification of update

autonumber 7

NRTRIC $- >$ NRTRIC : Performance analysis of AI/ML model \n(with possible actions, e.g. fallback, re-training) end

@enduml

![](images/42b0a97e924c5f45ab2de0567d2cdf9a7d246ed1ffd3f2513b2015de099004d5.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.2.1.1-1: Carrier and Cell Switch Off/On flow diagram: AI/ML inference via Non-RT RIC

# 5.2.1.2 O-RAN Entity Roles

1) Non-RT RIC

a) Collect configurations, performance indicators and measurement reports (e.g., cell load related information and traffic information, EE/EC measurement reports, geolocation information) from SMO, E2 Nodes and O-RUs (forwarded by SMO), for the purpose of decision making, optionally using training and inference of AI/ML models that assist such EE/ES functions.   
b) (Optionally) Trigger EE/ES AI/ML model training/retraining.   
c) (Optionally) Deploy, update, configure EE/ES AI/ML models in Non-RT RIC.   
d) Analyze the received data from SMO, E2 Nodes, and O-RUs to determine EE/ES optimization (i.e. if carriers or cells are recommended to be switched off/on), optionally using AI/ML models   
e) Signal updated configurations for EE/ES optimization to E2 Nodes (O-CU) via R1/O1.

# 2) E2 Node

a) Report cell configuration, performance indicators and measurement reports (e.g., cell load related information and traffic information, EE/EC measurement reports) to SMO via O1 interface.   
b) Perform actions required for EE/ES optimization o e.g. check ongoing emergency calls and warning messages, perform some preparation actions for Off Switching (e.g., to enable, disable, modify Carrier Aggregation and/or Dual Connectivity, to trigger HO traffic and UEs from cells/carriers to other cells or carriers, informing neighbour nodes via X2/Xn interface etc.) as well as for On Switching (e.g., cell probing, informing neighbour nodes via X2/Xn interface etc.) and make final decision on switch off/on and notify SMO via O1 about performed actions

# 3) O-RU

a) Report EC and EE related information via Open FH M-Plane interface to O-DU or alternatively to SMO directly.   
b) Support actions required to perform EE/ES optimization. o updated carrier configuration (i.e. activation, deactivation or sleep)

# 5.2.1.3 Input/Output Data Requirements

# 5.2.1.3.1 Summary

# Input Data

1) E2 Node to SMO/Non-RT RIC

➢ Carrier/cell characteristics   
➢ EE/EC measurement reports   
➢ Load statistics per cell and per carrier   
➢ UE mobility information including cell or beam level measurements (e.g. RSRP, RSRQ, SINR)   
➢ Energy consumption

2) O-RU to E2 Node

Power consumption metrics: Mean total/per carrier power consumption, mean total/per carrier transmit power

# Output Data

1) SMO to E2 Node

Carrier(s) and/or cell(s) recommended to be switched off/on

# 5.2.1.3.2 Detailed Input Requirements

Initialization:

Table 5.2.1.3-1: Initialization   

<table><tr><td rowspan=1 colspan=6>Input Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source /Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod</td><td rowspan=1 colspan=1>Existing /New Definitions</td></tr><tr><td rowspan=2 colspan=1>R1</td><td rowspan=2 colspan=1>SMO / rApp</td><td rowspan=1 colspan=1>Optimization target forCarrier/Cell Switch Off/On</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>manual oreventtriggered</td><td rowspan=1 colspan=1>New</td></tr><tr><td rowspan=1 colspan=1>E.g., (average or max) NG-RANdata Energy Efficiency</td><td rowspan=1 colspan=1>bit/J</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3GPP TS 28.554 [7] (C1. 6.7.1)</td></tr><tr><td rowspan=2 colspan=1>O1, R1</td><td rowspan=2 colspan=1>E2 Node (O-DU) / SMO /rApp</td><td rowspan=1 colspan=1>Carrier/cell characteristics</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>manual oreventtriggered(e.g. SMOfeatureactivation,E2 Nodestartup /failure /reconfig.)</td><td rowspan=1 colspan=1>New</td></tr><tr><td rowspan=1 colspan=1>E.g., physical location, transmitdirection, carrier frequency,coverage parameters, configuredtransmit power, beam width,coverage shape, tilt, azimuth,carrier-cell mapping, carrier-HWmapping</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3GPP TS 28.541 [11] (C1.4.3.6, 4.3.38, 4.3.39, 4.3.40,4.3.74)O-RAN.WG5.O-DU-O1 (Sec.10), O-RAN-WG5.O-CU-O1(Sec. 9)</td></tr></table>

AI/ML Model Training:

Table 5.2.1.3-2: AI/ML Model Training   

<table><tr><td rowspan=1 colspan=6>Input Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source / Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod</td><td rowspan=1 colspan=1>Existing Definitions</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / sMO/rApp</td><td rowspan=1 colspan=1>DL PDCP SDU Data Volume perinterface (Data Volume in DLdelivered from O-CU-UP to O-DU, per PLMN, per QoS level,per slice, per Interface (F1-U, Xn-U, X2-U))</td><td rowspan=1 colspan=1>Mbit</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.3.6.2.3)</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / sMO /rApp</td><td rowspan=1 colspan=1>UL PDCP SDU Data Volume perinterface (Data Volume in ULdelivered to O-CU-UP from O-DU, per PLMN, per QoS level,per slice, per Interface (F1-U, Xn-U, X2-U))</td><td rowspan=1 colspan=1>Mbit</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.3.6.2.4)</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / sMO/rApp</td><td rowspan=1 colspan=1>RSRQ measurement per SSB percell</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12] (C1.5.1.1.31)</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / sMO/rApp</td><td rowspan=1 colspan=1>RSRP measurement per SSB percell</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.22)</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / sMO /rApp</td><td rowspan=1 colspan=1>SINR measurement per SSB percell</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.32)</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / SMO /rApp</td><td rowspan=1 colspan=1>Energy consumption</td><td rowspan=1 colspan=1>kWh</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.19.3)</td></tr><tr><td rowspan=1 colspan=1>O-FH (M-Plane)orO-FH (M-Plane),01, R1</td><td rowspan=1 colspan=1>O-RU / O-DUorO-RU / O-DU /SMO /rApp</td><td rowspan=1 colspan=1>Power consumed by hardwarecomponent</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12] (Cl.5.1.1.19.2)Reporting:O-RAN.WG4.MP(Sec. B.1, B.5)</td></tr><tr><td rowspan=1 colspan=1>O-FH (M-Plane)orO-FH (M-Plane),01, R1</td><td rowspan=1 colspan=1>O-RU / O-DUorO-RU / O-DU /SMO / rApp</td><td rowspan=1 colspan=1>Transmit power</td><td rowspan=1 colspan=1>mW</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement and reporting:O-RAN.WG4.MP(Sec. B.1, B.2.1)</td></tr></table>

Input Decision Making / AI/ML Inference:

Table 5.2.1.3-3: Input Decision Making / AI/ML Inference   

<table><tr><td rowspan=1 colspan=6>Input Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source / Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod</td><td rowspan=1 colspan=1>Existing Definitions</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / SMO /rApp</td><td rowspan=1 colspan=1>Data Volume in DL delivered from O-CU-UP to O-DU, per PLMN, per QoSlevel, per slice, per Interface (F1-U,Xn-U, X2-U)</td><td rowspan=1 colspan=1>Mbit</td><td rowspan=1 colspan=1>&gt; min</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.3.6.2.3)</td></tr><tr><td rowspan=1 colspan=1>O1, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / sMO/rApp</td><td rowspan=1 colspan=1>Data Volume in UL delivered to O-CU-UP from O-DU, per PLMN, perQoS level, per slice, per Interface (F1-U, Xn-U, X2-U)</td><td rowspan=1 colspan=1>Mbit</td><td rowspan=1 colspan=1>&gt; min</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.3.6.2.4)</td></tr><tr><td rowspan=1 colspan=1>O1, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / SMO /rApp</td><td rowspan=1 colspan=1>RSRQ measurement per SSB per cell</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>&gt;min</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12] (C1. 5.1.1.31)</td></tr><tr><td rowspan=1 colspan=1>O1, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / sMO /rApp</td><td rowspan=1 colspan=1>RSRP measurement per SSB per cell</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>&gt;min</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.22)</td></tr><tr><td rowspan=1 colspan=1>O1, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / SMO/rApp</td><td rowspan=1 colspan=1>SINR measurement per SSB per cell</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>&gt;min</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.32)</td></tr><tr><td rowspan=1 colspan=1>O1, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / sMO/rApp</td><td rowspan=1 colspan=1>Energy consumption</td><td rowspan=1 colspan=1>kWh</td><td rowspan=1 colspan=1>&gt;min</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.19.3)</td></tr><tr><td rowspan=1 colspan=1>O-FH (M-Plane)orO-FH (M-Plane),01, R1</td><td rowspan=1 colspan=1>O-RU / O-DUorO-RU / O-DU /SMO / rApp</td><td rowspan=1 colspan=1>Power consumed by hardwarecomponent</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>&gt; min</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.19.2)Reporting:O-RAN.WG4.MP(Sec. B.1, B.5)</td></tr><tr><td rowspan=1 colspan=1>O-FH (M-Plane)orO-FH (M-Plane),01, R1</td><td rowspan=1 colspan=1>O-RU / O-DUorO-RU / O-DU /SMO / rApp</td><td rowspan=1 colspan=1>Transmit power</td><td rowspan=1 colspan=1>mW</td><td rowspan=1 colspan=1>&gt;min</td><td rowspan=1 colspan=1>Measurement andreporting:O-RAN.WG4.MP(Sec. B.1, B.2.1)</td></tr></table>

# 5.2.1.3.3 Detailed Output Requirements

Output Decision Making / AI/ML Inference:

Table 5.2.1.3-4: Output Decision Making / AI/ML Inference   

<table><tr><td rowspan=1 colspan=6>Output Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source / Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>Config.Period</td><td rowspan=1 colspan=1>Existing Definitions</td></tr><tr><td rowspan=2 colspan=1>O1, R1</td><td rowspan=2 colspan=1>rApp / SMO /E2 Node (O-CU)</td><td rowspan=1 colspan=1>Candidate carrier(s) / cells (s)recommended for energy saving toenter energySaving state (e.g., 3GPPTs 28.310 [8] Sec. 6.2.2)</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>&gt;min</td><td rowspan=1 colspan=1>3GPP TS 28.541 [11](C1. 4.3.63)O-RAN-WG5.O-CU-01(Sec.9)</td></tr><tr><td rowspan=1 colspan=1>Candidate carrier(s) / cell (s) forcompensation (e.g., 3GPP TS 32.551[15] compensatingForEnergySaving,optional))</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>&gt; min</td><td rowspan=1 colspan=1>-</td></tr><tr><td rowspan=1 colspan=1>O1, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / sMO /rApp</td><td rowspan=1 colspan=1>Confirmation (Success/Failure)</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>eventtriggered</td><td rowspan=1 colspan=1>3GPP TS 28.310 [8] (C1.6.2.2)</td></tr><tr><td rowspan=1 colspan=1>O-FH (M-Plane)</td><td rowspan=1 colspan=1>E2 Node (O-DU) / O-RU</td><td rowspan=1 colspan=1>Updated carrier configuration (i..,activation, deactivation, or sleep)</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>&gt;min</td><td rowspan=1 colspan=1>O-RAN.WG4.MP(Sec. 15.3.2)</td></tr></table>

# 5.2.2 Option 2: Near-RT RIC Deployment

In option 2, decision making, potentially using AI/ML Model Inference, is done at Near-RT RIC. While AI/ML Model Training might be hosted in Non-RT or Near-RT RIC, the description below is based on AI/ML Model Training in the Non-RT RIC.

# 5.2.2.1 Description and UML Diagram

Table 5.2.2.1-1: Carrier and Cell Switch Off/On: AI/ML inference via Near-RT RIC   

<table><tr><td rowspan=1 colspan=1>Use Case Stage</td><td rowspan=1 colspan=1>Evolution / Specification</td><td rowspan=1 colspan=1>&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td rowspan=1 colspan=1>Goal</td><td rowspan=1 colspan=1>Enable Carrier and Cell switch off/on Energy Saving functions in theNetwork by means of configuration parameter change and Actionscontrolled by Near-RT RIC and allow for Al/ML-based solutions.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Actors and Roles</td><td rowspan=1 colspan=1>Non-RT RIC acting as Al/ML model management entity.Near-RT RIC acting as inference host for Energy Savings decisionmaking.E2 Node and O-RU are the subject of action for configurationenforcement.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Assumptions</td><td rowspan=1 colspan=1>O1 connectivity is established between the SMO with E2 Node, andNear-RT RIC and Non-RT RIC.E2 interface connectivity is established between E2 Node and Near-RTRIC.A1 interface is established between Non-RT RIC and Near-RT RIC.Open FH M-Plane interface is established between E2 Node and O-RU.Network is operational.Near-RT RIC has knowledge about overlapping carriers/cells and thecoverage of those cariers/cells (e.g, which carrier/cell is a coveragelayer and which is a capacity layer).</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Pre-conditions</td><td rowspan=1 colspan=1>The operator has set the targets for Energy Saving function in the Non-RT RIC.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Begins when</td><td rowspan=1 colspan=1>The operator enables the optimization functions for carrier and cellswitch&#x27; off/on Energy Saving functions and E2 Node and O-RU becomeoperational.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 1 (M)</td><td rowspan=1 colspan=1>SMO initiates specific measurement data collection request towards E2Node and O-RU for Al/ML model training.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 2 (M)</td><td rowspan=1 colspan=1>E2 Node and O-RU send the configured measurement data to SMOperiodically or event based.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 3 (M)</td><td rowspan=1 colspan=1>Non-RT RiC retrieves the collected measurement data for processing</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 4 (M)</td><td rowspan=1 colspan=1>Non-RT RIC trains the Al/ML models with the collected data. TrainedAl/ML models are deployed, configured, and activated in the Near-RTRIC.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 5 (M)</td><td rowspan=1 colspan=1>SMO may trigger EE/ES optimization and might provide policies guidingthe Near-RT RIC EE/ES function via O1 and/or via Non-RT RIC and A1interface.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 6 (M)</td><td rowspan=1 colspan=1>Near-RT RIC constantly monitors(i) performance and energy consumption of the E2 Node(s)(ii) energy consumption of O-RU(s)Based on the Al/ML inference, considering optimization policies, theNear-RT RIC may request the E2 Node to prepare and execute cell orcarrier switch off/on. E2 Node may request O-RU Node to prepare andexecute cell or carrier switch off/on. E2 Node will notify Near-RT RIConce cell or carrier switch off/on is completed.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Ends when</td><td rowspan=1 colspan=1>E2 Node becomes non-Operational or when the operator disables theoptimization functions for Energy Saving.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Exceptions</td><td rowspan=1 colspan=1>None.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Post Conditions</td><td rowspan=1 colspan=1>Near-RT RIC continues closed-loop monitoring of Energy Savingfunction at E2 Node and O-RU.E2 Node and O-RU operate using the newly deployedparameters/models and state (off/on).</td><td rowspan=1 colspan=1></td></tr><tr><td></td><td></td><td rowspan=1 colspan=1></td></tr></table>

@startuml   
skin rose   
skinparam defaultFontSize 12   
autonumber

Box "Service Management & \n Orchestration Framework" #gold

Participant "Collection & Control" as SMO Participant "Non-RT RIC" as NRTRIC

End box

Box "O-RAN Nodes" #lightpink Participant "Near-RT RIC" as RTRIC Participant "E2-Nodes" as E2NODES Participant "O-RUs" as ORUs

End box

group Data Collection   
autonumber 1.1   
SMO -> E2NODES : <<O1>> Data collection request for Energy Saving E2NODES -> ORUs <<FH>> Data collection request for Energy Saving ORUs -> E2NODES <<FH>> Measurement Data Collection for Energy Saving E2NODES $- >$ SMO : $< < 0 1 > >$ Measurement Data Collection for Energy Saving autonumber 3   
SMO $- >$ NRTRIC : Data retrieval

end

autonumber 4.1 group AI/ML workflow

NRTRIC $- >$ NRTRIC : AI/ML Model training NRTRIC $- >$ RTRIC : <<O1>> or <<O2>> Deploy AI/ML model

end

autonumber 5.1   
group Optimization Trigger and Policy alt SMO $- >$ RTRIC : <<O1>> Optimization Trigger/Targe else NRTRIC $- >$ RTRIC : <<A1>> A1 Policy end   
end

end @enduml

![](images/c1f7153ce3f62936a1c0b1f7eb474daf9e809e12938e6c0f950f522f65ca5ac0.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.2.2.1-1: Carrier and Cell Switch Off/On flow diagram: AI/ML inference via Near-RT RIC

# 5.2.2.2 O-RAN Entity Roles

1) Non-RT RIC

a) (Optionally) Collect configurations, performance indicators and measurement reports (e.g., cell load related information and traffic information, EE/EC measurement reports, geolocation information) from SMO, E2 Nodes and O-RUs (forwarded by SMO), for the purpose of training AI/ML models that assist such EE/ES functions.   
b) (Optionally) Trigger EE/ES AI/ML model training/retraining.   
c) (Optionally) Deploy, update, configure EE/ES AI/ML models, in Near-RT RIC via O1/O2 interface.   
d) Provide optimization trigger, optimization targets and intent-based policies (e.g., set energy target to $50 \%$ of peak power consumption) to Near-RT RIC via R1/O1 or A1 interface.

# 2) Near-RT RIC

a) Collect configurations, performance indicators and measurement reports (e.g., cell load related information and traffic information, EE/EC measurement reports) from E2 Nodes.   
b) (Optionally) Receive EE/ES AI/ML model for deployment via O1 or O2 interface.   
c) Receive EE/ES related configuration management via O1 interface and/or policies via A1 interface for consideration during optimization.   
d) Analyze the received data from E2 Nodes and perform AI/ML model inference to determine EE/ES. optimization (i.e. if carriers or cells are recommended to be switched off/on) considering the optimization targets/policies.   
e) Provide policies or required information to E2 Node (O-CU) via E2 to trigger actions for EE/ES optimization.

# 3) E2 Node

a) Report cell configuration, performance indicators and measurements reports (e.g., cell load related information and traffic information, EE/EC measurement reports) per cell/carrier via O1 interface to SMO and via E2 interface to Near-RT RIC.   
b) Perform actions required for EE/ES optimization o e.g. check ongoing emergency calls and warning messages, perform some preparation actions for Off Switching (e.g., to enable, disable, modify Carrier Aggregation and/or Dual Connectivity, to trigger HO traffic and UEs from cells/carriers to other cells or carriers, informing neighbour nodes via X2/Xn interface etc.) as well as for On Switching (e.g., cell probing, informing neighbour nodes via X2/Xn interface etc.) and make final decision on switch off/on and notify Near-RT RIC via E2 about performed actions

# 4) O-RU

a) Report EC and EE related information via Open FH M-Plane interface to O-DU or alternatively to SMO directly.   
b) Support actions required to perform EE/ES optimization. $\bigcirc$ updated carrier configuration (i.e. activation, deactivation or sleep)

# 5.2.2.3 Input/Output Data Requirements

# 5.2.2.3.1 Summary

# Input Data

1) E2 Node to SMO/Non-RT RIC (training) and Near-RT RIC (decision making/inference)

➢ Carrier/cell characteristics ➢ EE/EC measurement reports ➢ Load statistics per cell and per carrier

UE mobility information including cell or beam level measurements (e.g., RSRP, RSRQ, SINR) Energy Consumption

2) O-RU to E2 Node

Power consumption metrics: Mean total/per carrier power consumption, mean total/per carrier transmit power

# Output Data

1) Near-RT RIC to E2 Node

Carrier(s) and/or cell(s) recommended to be switched off/on

# 5.2.2.3.2 Detailed Input Requirements

Initialization:

Table 5.2.2.3-1: Initialization   

<table><tr><td rowspan=1 colspan=6>Input Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source / Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod</td><td rowspan=1 colspan=1>Existing / NewDefinitions</td></tr><tr><td rowspan=2 colspan=1>01</td><td rowspan=2 colspan=1>SMO / Near-RTRIC</td><td rowspan=1 colspan=1>Optimization target forCarrier/Cell Switch Off/On</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>manual oreventtriggered</td><td rowspan=1 colspan=1>New</td></tr><tr><td rowspan=1 colspan=1>E.g., (average or max) NG-RANdata Energy Efficiency</td><td rowspan=1 colspan=1>bit/J</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3GPP TS 28.554 [7] (Cl.6.7.1)</td></tr><tr><td rowspan=2 colspan=1>E2, O1,R1</td><td rowspan=2 colspan=1>E2 Node (O-DU) / Near-RTRIC / SMO /rApp</td><td rowspan=1 colspan=1>Carrier/cell characteristics</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>manual oreventtriggered(e.g., MOfeatureactivation, E2Node startup/ failure /reconfig.)</td><td rowspan=1 colspan=1>New</td></tr><tr><td rowspan=1 colspan=1>E.g., physical location, transmitdirection, carrier frequency,coverage parameters, configuredtransmit power, beam width,coverage shape, tilt, azimuth,carrier-cell mapping, carrier-HWmapping</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3GPP TS 28.541 [11] (Cl.4.3.6,4.3.38, 4.3.39,4.3.40, 4.3.74)O-RAN.WG5.O-DU-O1(Sec. 10), O-RAN-WG5.O-CU-O1 (Sec. 9)</td></tr></table>

AI/ML Model Training:

Table 5.2.2.3-2: AI/ML Model Training   

<table><tr><td rowspan=1 colspan=6>Input Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source / Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod</td><td rowspan=1 colspan=1>Existing Definitions</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-DU) / SMO/rApp</td><td rowspan=1 colspan=1>DL PDCP SDU Data Volume perinterface (Data Volume in DLdelivered from O-CU-UP to O-DU, perPLMN, per QoS level, per slice, per Interface (F1-U, Xn-U, X2-U))</td><td rowspan=1 colspan=1>Mbit</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.3.6.2.3)</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-DU) / SMO/rApp</td><td rowspan=1 colspan=1>UL PDCP SDU Data Volume perinterface (Data Volume in ULdelivered to O-CU-UP from O-DU, perPLMN, per QoS level, per slice, perInterface (F1-U, Xn-U, X2-U))</td><td rowspan=1 colspan=1>Mbit</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.3.6.2.4)</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-DU) / SMO /rApp</td><td rowspan=1 colspan=1>RSRQ measurement per SSB per cell</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.31)</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-DU) / SMO/rApp</td><td rowspan=1 colspan=1>RSRP measurement per SSB per cell</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.22)</td></tr><tr><td rowspan=1 colspan=1>O1, R1</td><td rowspan=1 colspan=1>E2 Node (O-DU) / sMO /rApp</td><td rowspan=1 colspan=1>SINR measurement per SSB per cell</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.32)</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-DU) / SMO /rApp</td><td rowspan=1 colspan=1>Energy consumption</td><td rowspan=1 colspan=1>kWh</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.19.3)</td></tr><tr><td rowspan=1 colspan=1>O-FH (M-Plane)d)orO-FH (M-Plane),O1, R1</td><td rowspan=1 colspan=1>O-RU / O-DUorO-RU / O-DU /SMO / rApp</td><td rowspan=1 colspan=1>Power consumed by hardwarecomponent</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.19.2)Reporting:O-RAN.WG4.MP(Sec. B.1, B.5)</td></tr><tr><td rowspan=1 colspan=1>O-FH (M-Plane))orO-FH (M-Plane),01, R1</td><td rowspan=1 colspan=1>O-RU / O-DUorO-RU /O-DU /SMO / rApp</td><td rowspan=1 colspan=1>Transmit power</td><td rowspan=1 colspan=1>mW</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement andreporting:O-RAN.WG4.MP(Sec. 10.2, B.1, B.2.1)</td></tr></table>

Input Decision Making / AI/ML Inference:

Table 5.2.2.3-3: Input Decision Making / AI/ML Inference   

<table><tr><td rowspan=1 colspan=6>Input Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source / Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod</td><td rowspan=1 colspan=1>Existing / NewDefinitions</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>E2 Node (O-DU) / Near-RTRIC</td><td rowspan=1 colspan=1>Data Volume in DL delivered from O-CU-UP to O-DU, per PLMN, per QoSlevel, per slice, per Interface (F1-U,Xn-U, X2-U). In case of split gNBarchitecture.</td><td rowspan=1 colspan=1>Mbit</td><td rowspan=1 colspan=1>∼ per N x100ms</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552[12](C1. 5.1.3.6.2.3)Reporting:O-RAN.WG3.E2SM-KPM</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>E2 Node (O-DU) Near-RTRIC</td><td rowspan=1 colspan=1>Data Volume in UL delivered to O-CU-UP from O-DU, per PLMN, perQoS level, per slice, per Interface F1-U, Xn-U, X2-U). In case of split gNBarchitecture.</td><td rowspan=1 colspan=1>Mbit</td><td rowspan=1 colspan=1>∼ per Nx100ms</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.3.6.2.4)Reporting:O-RAN.WG3.E2SM-KPM</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>E2 Node (O-DU) / Near-RTRIC</td><td rowspan=1 colspan=1>RSRQ measurement per SSB per cell</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>∼ per N x100ms</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.31)Reporting:O-RAN.WG3.E2SM-KPM</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>E2 Node (O-DU) / Near-RTRIC</td><td rowspan=1 colspan=1>RSRP measurement based on SSB perUE</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>~ per Nx100ms</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.22)Reporting:O-RAN.WG3.E2SM-KPM</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>E2 Node (O-DU) / Near-RTRIC</td><td rowspan=1 colspan=1>SINR measurement based on SSB perUE</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>~ per N x100ms</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.32)Reporting:O-RAN.WG3.E2SM-KPM</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>E2 Node (O-DU) / Near-RTRIC</td><td rowspan=1 colspan=1>Energy consumption</td><td rowspan=1 colspan=1>kWh</td><td rowspan=1 colspan=1>∼ per N x100ms</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.19.3)New reporting: E2</td></tr><tr><td rowspan=1 colspan=1>O-FH (M-Plane)</td><td rowspan=1 colspan=1>O-RU / O-DU</td><td rowspan=1 colspan=1>Power consumed by hardwarecomponent</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>~ per N x100ms</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.19.2)Reporting:O-RAN.WG4.MP(Sec. B.1, B.5)</td></tr><tr><td rowspan=1 colspan=1>O-FH (M-Plane)</td><td rowspan=1 colspan=1>O-RU /O-DU</td><td rowspan=1 colspan=1>Transmit power</td><td rowspan=1 colspan=1>mW</td><td rowspan=1 colspan=1>∼ per N x100ms</td><td rowspan=1 colspan=1>Measurement andreporting:O-RAN.WG4.MP(Sec. 10.2, B.1, B.2.1)</td></tr></table>

# 5.2.2.3.3 Detailed Output Requirements

Output Decision Making / AI/ML Inference:

Table 5.2.2.3-4: Output Decision Making / AI/ML Inference   

<table><tr><td rowspan=1 colspan=6>Output Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source / Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>Config.Period</td><td rowspan=1 colspan=1>Existing / NewDefinitions</td></tr><tr><td rowspan=2 colspan=1>E2</td><td rowspan=2 colspan=1>Near-RT RIC /E2 Node (O-CU)</td><td rowspan=1 colspan=1>Candidate carrier(s) / cells (s)recommended for energy saving toenter energySaving state (e.g., 3GPPTs 28.310 [8] Sec. 6.2.2)</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>&gt;min</td><td rowspan=1 colspan=1>3GPP TS 28.541 [11](C1. 4.3.63)New configuration: E2</td></tr><tr><td rowspan=1 colspan=1>Candidate carrier(s) / cell (s) forcompensation (e.g., 3GPP TS 32.551[15] compensatingForEnergySaving,optional)</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>&gt;min</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>E2 Node (O-CU) / Near-RTRIC</td><td rowspan=1 colspan=1>Confirmation (Success/Failure)</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>eventtriggered</td><td rowspan=1 colspan=1>3GPP TS 28.310 [8] (C1.6.2.2)</td></tr><tr><td rowspan=1 colspan=1>O-FH (M-Plane)</td><td rowspan=1 colspan=1>E2 Node (O-DU) / O-RU</td><td rowspan=1 colspan=1>Updated carrier configuration (i.e.activation, deactivation, or sleep)</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>&gt;min</td><td rowspan=1 colspan=1>O-RAN.WG4.MP(Sec. 15.3.2)</td></tr></table>

# 5.3 Impact Analysis on O-RAN Work Groups

This is an initial impact analysis as part of the WG1 UCTG Network Energy Saving work on Carrier and Cell Switch Off/On use case. The intention is to estimate the expected standardization effort within the ORAN work groups. It is up to the WGs to decide how Carrier and Cell Switch Off/On use case functionality should be specified in specifications of each WG.

<table><tr><td rowspan=1 colspan=1>#</td><td rowspan=1 colspan=1>WGs/FGs</td><td rowspan=1 colspan=1>Spec. No</td><td rowspan=1 colspan=1>Objective description</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>WG1 (Usecase)</td><td rowspan=1 colspan=1>O-RAN.WG1.NES-USE-CASES-TRO-RAN.WG1.Use-Cases-Detailed-Specification</td><td rowspan=1 colspan=1>Update WG1 NES use case analysis report and use-case detailed specification with Carrier and CellSwitch Off/On use case. No impact to existingarchitecture.</td></tr><tr><td rowspan=4 colspan=1>2</td><td rowspan=4 colspan=1>WG2(Non-RTRIC, A1,R1)d</td><td rowspan=1 colspan=1>O-RAN.WG2.R1GAPO-RAN.WG2.R1UCRO-RAN.WG2.R1TD (TBD)</td><td rowspan=1 colspan=1>Updates to R1 services and procedures for Carrierand Cell Switch Off/On use case</td></tr><tr><td rowspan=1 colspan=1>O-RAN.WG2.Non-RT-RIC-ARCH</td><td rowspan=1 colspan=1>No impact identified</td></tr><tr><td rowspan=1 colspan=1>O-RAN.WG2.Use-Case-Requirements</td><td rowspan=1 colspan=1>Specifying Carrier and Cel Switch Off/On use caseand its requirements in WG2 UCR specification</td></tr><tr><td rowspan=1 colspan=1>O-RAN.WG2.A1GAPO-RAN.WG2.A1TD</td><td rowspan=1 colspan=1>Review and implement potential requirements forpolicy driven implementation 2nd deployment optionof Carrier and Cell Switch Off/On use case captured in WG2 UCR specification.</td></tr><tr><td rowspan=6 colspan=1>3</td><td rowspan=6 colspan=1>WG3(Near-RTRIC, E2)</td><td rowspan=1 colspan=1>O-RAN.WG3.UCR</td><td rowspan=1 colspan=1>Specifying 2nd deployment option of Carrier andCell Switch Off/On use case and its requirements inWG3 UCR specification</td></tr><tr><td rowspan=1 colspan=1>O-RAN.WG3.RICARCH</td><td rowspan=1 colspan=1>No impact identified</td></tr><tr><td rowspan=1 colspan=1>O-RAN.WG3.E2GAP</td><td rowspan=1 colspan=1>No impact identified</td></tr><tr><td rowspan=1 colspan=1>O-RAN.WG3.E2AP</td><td rowspan=1 colspan=1>No impact identified</td></tr><tr><td rowspan=1 colspan=1>O-RAN.WG3.E2SM-RC orNEW: O-RAN.WG3.E2SM-CC</td><td rowspan=1 colspan=1>Identify and specify RAN E2 actions necessary for2nd deployment option of Carrier and Cell SwitchOff/On use case through E2 Node</td></tr><tr><td rowspan=1 colspan=1>O-RAN.WG3.E2SM-KPM</td><td rowspan=1 colspan=1>Identify and specify RAN E2 measurement requiredanalysis of ES and EC for 2nd deployment option ofCarrier and Cell Switch Off/On use case throughNear-RT RIC</td></tr><tr><td rowspan=2 colspan=1>4</td><td rowspan=2 colspan=1>WG4(O-FH)</td><td rowspan=1 colspan=1>O-RAN.WG4.MP</td><td rowspan=1 colspan=1>Review and specify requirements for M-Plane.Identify and specify relevant impacts on M-Plane forboth Hierarchical and hybrid model to accommodatemanagement features requirements towards O-RU.Define O-RU Energy efficiency KPIs and counters.</td></tr><tr><td rowspan=1 colspan=1>O-RAN-WG4.CUS</td><td rowspan=1 colspan=1>Review and specify requirements for CUS-Plane.Identify and specify relevant impacts on CUS Planeand data model to support various Tx/Rx ArrayCarrier Off/On.</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>WG5(01)</td><td rowspan=1 colspan=1>O-RAN.WG5.O-DU-O1O-RAN.WG5.O-CU-01O-RAN.WG5.MP</td><td rowspan=1 colspan=1>Identify specific O-DU operational and data modelaspects of the feature content including the interfacebetween SMO and O-DU, and the one betweenSMO and O-CU. Make appropriate changes to theO-DU data model and other WG5 specifications asneeded.</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>WG10</td><td rowspan=1 colspan=1>O-RAN.WG10.O1-InterfaceO-RAN.WG10.OAM-ArchitectureO-RAN.WG10.Information Model andData Models</td><td rowspan=1 colspan=1>Review, identify enhancements and update therelevant impacts on O1 interface and IM/DM tosupport Carrier and Cell Switch Off/On use case.</td></tr></table>

# 5.4 Relation and Impact on 3GPP Specifications

# 5.4.1 Relation to 3GPP RAN Specifications

<table><tr><td rowspan=1 colspan=1>Specs</td><td rowspan=1 colspan=1>Release</td><td rowspan=1 colspan=1>Title</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>TR36.927</td><td rowspan=1 colspan=1>LTERel.10</td><td rowspan=1 colspan=1>Study on Potentialsolutions for energysaving for E-UTRAN</td><td rowspan=1 colspan=1>Study on energy saving for E-UTRAN.</td></tr><tr><td rowspan=1 colspan=1>TS36.300andotherspecs</td><td rowspan=1 colspan=1>LTERel.10</td><td rowspan=1 colspan=1>E-UTRAN; Overalldescription; Stage 2</td><td rowspan=1 colspan=1>Support of LTE energy saving by cell/carrier of/on switching.The switch-off decision might be taken by the capacity boostercell autonomously or may be centrally controlled by OAM. TheeNB may initiate handover with appropriate root cause valuesand thereby inform its neighbour cells about the future switchoff. The load of the neighbour cells may also be monitored byload information exchange over X2. Before switching off, allpeer eNBs can be informed about the switch off over the X2interface. For the switch off a Deactivation Indication wasadded to the ENB CONFIGURATION UPDATE procedure.For switch on a CELL ACTIVATION REQUEST/RESPONSEprocedure was introduced in LTE Rel.10. The autonomousswitch on decision is more difficult to realize particularly forsmall cells. Even with high load on the coverage cell, it is notobvious if there are UEs in the vicinity of such small cells.</td></tr><tr><td rowspan=1 colspan=1>TS36.300andotherspecs</td><td rowspan=1 colspan=1>LTERel.11</td><td rowspan=1 colspan=1>E-UTRAN; Overalldescription; Stage 2</td><td rowspan=1 colspan=1>LTE Rel.11 defined respective S1 messages for Inter-RAT (i.e.GERAN, UMTS) support.</td></tr><tr><td rowspan=1 colspan=1>TR36.887</td><td rowspan=1 colspan=1>LTERel.12</td><td rowspan=1 colspan=1>Study on energy savingenhancement for E-UTRAN</td><td rowspan=1 colspan=1>Study on energy saving enhancements for E-UTRAN.</td></tr><tr><td rowspan=1 colspan=1>TS36.300andotherspecs</td><td rowspan=1 colspan=1>LTERel.15</td><td rowspan=1 colspan=1>E-UTRAN; Overalldescription; Stage 2</td><td rowspan=1 colspan=1>EN-DC CONFIGURATION UPDATE procedure was specifiedto support LTE-NR Dual Connectivity in the Non-StandaloneConfigurations.</td></tr><tr><td rowspan=1 colspan=1>TS38.300andotherspecs</td><td rowspan=1 colspan=1>5GRel.15</td><td rowspan=1 colspan=1>NR and NG-RANOverall description;Stage-2</td><td rowspan=1 colspan=1>Support of 5G energy saving by cell/carrier off/on switching.Similar functionality as defined for LTE. E-UTRA or NR cellproviding additional capacity via single or dual connectivity.</td></tr></table>

# 5.4.2 Ongoing Work in 3GPP Rel.18 RAN

The following study is conducted in 3GPP Rel.18 in RAN. This includes:

Definition of a base station energy consumption model   
Definition of an evaluation methodology and KPIs   
Study and identify techniques on the gNB and UE side to improve network energy savings in terms of   
both BS transmission and reception

<table><tr><td rowspan=1 colspan=1>Reference</td><td rowspan=1 colspan=1>Release</td><td rowspan=1 colspan=1>Title</td><td rowspan=1 colspan=1>Documentation and impact onSpecifications</td></tr><tr><td rowspan=1 colspan=1>FS_Netw_Energy_NR</td><td rowspan=1 colspan=1>5G Rel.18</td><td rowspan=1 colspan=1>Study on networkenergy savings for NR</td><td rowspan=1 colspan=1>Results will be captured in 3GPP TR38.864 [19].</td></tr></table>

While 3GPP RAN WG1 is leading this study item, RAN WG3 will study aspects of information exchange/coordination over network interfaces such as X2/Xn. For this purpose, RAN WG3 also considers Enhanced Carrier/Cell Switch Off/On mechanisms.

# 5.4.3 Impact on 3GPP RAN Specifications

Non-RT or Near-RT RIC controlled Cell Switch Off/On is not considered to have any impact on 3GPP RAN specifications.

5.4.4 Relation to 3GPP System Architecture Specifications   

<table><tr><td rowspan=1 colspan=1>Specs</td><td rowspan=1 colspan=1>Release</td><td rowspan=1 colspan=1>Title</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>TR36.927</td><td rowspan=1 colspan=1>LTERel.10</td><td rowspan=1 colspan=1>Study on EnergySavings Management</td><td rowspan=1 colspan=1>Study on Energy Savings Management</td></tr><tr><td rowspan=1 colspan=1>TS32.551andotherspecs</td><td rowspan=1 colspan=1>LTERel.10</td><td rowspan=1 colspan=1>Energy SavingManagement (ESM);Concepts andrequirements</td><td rowspan=1 colspan=1>Concepts and requirements for ESM. According to 3GPP TS32.551, the energy saving procedure initiating capacity boostercell, to enter or exit &quot;energySaving&quot; state, should be able toinitiate energy saving compensation activation and/ordeactivation on one or multiple cells or network elements. 3GPPTS 32.425 [13] defines the measurements and 3GPP TS 32.451[14] defines the KPIs.</td></tr><tr><td rowspan=1 colspan=1>TR32.834</td><td rowspan=1 colspan=1>LTERel.11</td><td rowspan=1 colspan=1>Study on OAM aspectsof inter-RAT EnergySaving</td><td rowspan=1 colspan=1>Inter-RAT aspects of Energy Saving. The following RATs areconsidered in this study: GSM, UMTS, LTE, CDMA.</td></tr><tr><td rowspan=1 colspan=1>TR23.866</td><td rowspan=1 colspan=1>LTERel.12</td><td rowspan=1 colspan=1>Study on SystemEnhancements forEnergy Efficiency</td><td rowspan=1 colspan=1>Study on System Enhancements for Energy Efficiency</td></tr><tr><td rowspan=1 colspan=1>TR32.856</td><td rowspan=1 colspan=1>5GRel.15</td><td rowspan=1 colspan=1>Study on OAM supportfor assessment ofenergy efficiency inmobile accessnetworks</td><td rowspan=1 colspan=1> Support for ETSI metrics and methods for energy efficiencyassessment and related measurements. Principles for monitoringequipment power, energy and environmental parameters. 2G,3G and 4G have been covered.</td></tr><tr><td rowspan=1 colspan=1>TS28.310andotherspecs</td><td rowspan=1 colspan=1>5GRel.16</td><td rowspan=1 colspan=1>Energy efficiency of5G</td><td rowspan=1 colspan=1>This TS defines solutions and requirements forData Volume collection Power,Power, Energy and Environmental (PEE) measurementcollectionEnergy Saving use casesThe Energy Saving use case defines the scenario of energysaving by switching off capacity booster cells when the trafficdemand is low and re-activate them on a need basis. The energysaving consists of two scenarios where the capacity booster cellgNB is fully or partially overlaid by the candidate cell(s).The configuration of energy saving policies for these solutions is defined in 3GPP TS 28.541 [11]. The measurements related todata volume and PEE measurements are defined in 3GPP TS28.552 [12]. The Energy Efficiency related KPIs are defined inTS 28.554 [7].</td></tr></table>

# 5.4.5 Ongoing Work in 3GPP Rel.18 System Architecture

Energy saving compensation activation and deactivation procedures for LTE are defined in 3GPP TS 32.551 [15] as:

Energy saving compensation activation: procedure to increase the coverage area for the candidate cell(s). Energy saving compensation deactivation: procedure to decrease a previously increased coverage area.

This procedure is not defined yet for energy saving procedures for 5G, and hence 3GPP TS 28.310 [8] needs to be enhanced to introduce this procedure for 5G networks. Related study and work items are existing.

<table><tr><td rowspan=1 colspan=1>Reference</td><td rowspan=1 colspan=1>Release</td><td rowspan=1 colspan=1>Title</td><td rowspan=1 colspan=1>Documentation and impact onSpecifications</td></tr><tr><td rowspan=1 colspan=1>FS_EE5G_Ph2</td><td rowspan=1 colspan=1>5G Rel.18</td><td rowspan=1 colspan=1>Study on new aspectsof EE for 5G networksPhase 2</td><td rowspan=1 colspan=1>Results will be captured in 3GPP TR28.913 Study on new aspects of EEfor 5G networks phase 2.</td></tr><tr><td rowspan=1 colspan=1>EE5GPLUS_Ph2</td><td rowspan=1 colspan=1>5G Rel.18</td><td rowspan=1 colspan=1>Enhancements of EEfor 5G Phase 2</td><td rowspan=1 colspan=1>Specification enhancements areexpected for the following 3GPPspecifications: TS 28.310 [8], TS28.552 [12], Ts 28.554 [7] and TS28.541 [11].</td></tr></table>

# 5.4.6 Impact on 3GPP System Architecture Specifications

Non-RT or Near-RT RIC controlled Cell Switch Off/On is not considered to have any impact on 3GPP System Architecture specifications.

# 5.5 Gain Analysis

An operator can expect strong energy savings, and thus OPEX savings, by using Carrier/Cell Switching in a network with multiple frequency layers. The exact power saving strongly depends on network deployment details, cell configuration (e.g., configured bandwidth, common channels etc.), used hardware, and network load. Multiple frequency layers may or may not use the same power amplifier in the RF module. Major power savings are naturally obtained when some power amplifiers can be switched off completely.

Numerical analysis based on an estimated power saving per carrier / cell to be switched off might provide a good estimate of the expected savings. O-RU power consumption might be categorized into power consumption related to:

1. user channels' load (e.g., traffic on uplink/downlink shared channels),   
2. common signals and channels' load (e.g., SSB transmissions, Reference Signals, broadcast channel,   
paging channel etc.),   
3. regular PA operational power (i.e., the required energy to power up the power amplifier),   
4. regular operational power (i.e., the required energy to power up the radio module).

Power consumption related to (1), (2) and (3) scales with the number of transmission paths as illustrated in Figure 5.5-1.

![](images/a1d7cbccd56e339c7f88ae5682952d411d1fa5c4b8ffee09ca31a603457e584c.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.5-1: O-RU power saving for a 4TX4RX sector configuration

Considering that the requested traffic (1) needs to be transmitted in one of the remaining carriers/cells and that regular operational power (4) will be required after carrier/cell switch off, the power savings of the Carrier/Cell Switch algorithm is mainly related to the power consumption of (2) and (3).

The yearly energy savings might be calculated as follows:

$$
Y e a r l y P o w e r S a v i n g [ M W h ] = \frac { O \ – R U P o w e r S a v i n g [ W ] } { 1 . 0 0 0 . 0 0 0 } \ast \frac { P o w e r S a v i n g H o u r s [ h ] } { d a y } \ast \# d a y
$$

Two example calculations, simplifying the factors as cited above and ignoring deployment, cell configuration, hardware specifics and load dependencies, are provided in the table below:

Table 5.5-1: Simplified power savings calculation examples   

<table><tr><td rowspan=1 colspan=1>Factor</td><td rowspan=1 colspan=1>Value</td><td rowspan=1 colspan=1>Value</td></tr><tr><td rowspan=1 colspan=1>O-RU power savings during switch off</td><td rowspan=1 colspan=1>100W</td><td rowspan=1 colspan=1>200W</td></tr><tr><td rowspan=1 colspan=1>Number of hours of switch off per day</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>Number of O-RUs</td><td rowspan=1 colspan=1>10000</td><td rowspan=1 colspan=1>20000</td></tr><tr><td rowspan=1 colspan=1>Yearly energy saving [MWh]</td><td rowspan=1 colspan=1>730</td><td rowspan=1 colspan=1>5840</td></tr></table>

To be more specific considering deployment, cell configuration, antenna type, hardware and load dependencies of the O-RU power consumption, computational analysis results for two example scenarios are provided. The calculations are based on the load profile and the power consumption categorization of O-RU functional blocks as outlined in Annex B.

Energy savings gain from Carrier and Cell Switch Off/On would be equivalent to power consumption of the O-RU hardware components that can be shut down or put into energy savings mode during low traffic load. As illustrated in Figure 5.5-2, major energy savings gain would be derived from shutting down RF Processing Unit and Digital Processing Unit (depending on the antenna configuration), while FH Processing Unit, Power Unit and other components would still be fully or partially functioning, and the power consumption would stay more or less consistent during the switching off period.

![](images/a13adf0d41ec52a7f2a9df3473a0bbe543e0e77ba5ed236392bef95ba64d212b.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.5-2: Energy savings for O-RU

# 5.5.1 Cell and Carrier Switch Off/On Energy Saving for 4T4R O-RU

The energy saving gain from Carrier and Cell Switch Off/On is analyzed based on the system parameters in Table 5.5.1-1 and the example power profile considering power consumption from operational experience provided in Table 5.5.1-2.

Table 5.5.1-1: O-RU Configuration for ES gain analysis   

<table><tr><td rowspan=1 colspan=1>No. of antennas</td><td rowspan=1 colspan=1>4T4R</td></tr><tr><td rowspan=1 colspan=1>No. of layers</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>Bandwidth</td><td rowspan=1 colspan=1>100 MHz</td></tr><tr><td rowspan=1 colspan=1>Carrier frequency</td><td rowspan=1 colspan=1>3.5 GHz</td></tr><tr><td rowspan=1 colspan=1>Tx power per antenna</td><td rowspan=1 colspan=1>30W</td></tr><tr><td rowspan=1 colspan=1>Technology</td><td rowspan=1 colspan=1>5G NR</td></tr></table>

Table 5.5.1-2: Example power profile for 4T4R O-RU   

<table><tr><td rowspan=1 colspan=1>Operating Load (Traffic)</td><td rowspan=1 colspan=1>Total O-RU (W)</td><td rowspan=1 colspan=1>ORANFronthaulProcessingUnit (W)</td><td rowspan=1 colspan=1>DigitalProcessing Unit(W)</td><td rowspan=1 colspan=1>RFProcessingUnit (W)</td><td rowspan=1 colspan=1>Power Unit &amp;othercomponents(W)</td></tr><tr><td rowspan=1 colspan=1>Busy hour load</td><td rowspan=1 colspan=1>550</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>495</td><td rowspan=1 colspan=1>20</td></tr><tr><td rowspan=1 colspan=1>Low load</td><td rowspan=1 colspan=1>200</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>145</td><td rowspan=1 colspan=1>20</td></tr><tr><td rowspan=1 colspan=1>Sleep (Energy Savings State)</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>5~10</td><td rowspan=1 colspan=1>0~5</td><td rowspan=1 colspan=1>0~15</td><td rowspan=1 colspan=1>15~20</td></tr><tr><td rowspan=1 colspan=1> Energy saving gain</td><td rowspan=1 colspan=1>150~180</td><td rowspan=1 colspan=1>0~5</td><td rowspan=1 colspan=1>20~25</td><td rowspan=1 colspan=1>130~145</td><td rowspan=1 colspan=1>0~5</td></tr></table>

Compared to the low load scenario, energy savings of up to $1 5 0 { \sim } 1 8 0 \ \mathrm { W }$ per O-RU can be achieved in the energy saving state. An example calculation for yearly energy saving potential considering a shutdown of 10000 O-RUs during 3 hours per day is provided in Table 5.5.1-3.

Table 5.5.1-3: Power saving calculation example for 4T4R O-RU   

<table><tr><td rowspan=1 colspan=1>Factor</td><td rowspan=1 colspan=1>Value</td></tr><tr><td rowspan=1 colspan=1>O-RU power savings during switch off (low load) [W]</td><td rowspan=1 colspan=1>150~180</td></tr><tr><td rowspan=1 colspan=1> Number of hours of switch off per day (50% of low load period)</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>Number of O-RUs</td><td rowspan=1 colspan=1>10000</td></tr><tr><td rowspan=1 colspan=1>Yearly energy saving [MWh]</td><td rowspan=1 colspan=1>1643~1971</td></tr></table>

# 5.5.2 Cell and Carrier Switch Off/On Energy Saving for 64T64R O-RU

The energy saving gain from Carrier and Cell Switch Off/On is analyzed based on the system parameters in Table 5.5.2-1 and the example power profile considering power consumption from operational experience provided in Table 5.5.2-2.

Table 5.5.2-1: O-RU Configuration for ES gain analysis   

<table><tr><td rowspan=1 colspan=1>No. of antennas</td><td rowspan=1 colspan=1>64T64R</td></tr><tr><td rowspan=1 colspan=1>No. of layers</td><td rowspan=1 colspan=1>16</td></tr><tr><td rowspan=1 colspan=1>Bandwidth</td><td rowspan=1 colspan=1>100MHz</td></tr><tr><td rowspan=1 colspan=1>Carrier frequency</td><td rowspan=1 colspan=1>3.5 GHz</td></tr><tr><td rowspan=1 colspan=1>Tx power per antenna</td><td rowspan=1 colspan=1>30W</td></tr><tr><td rowspan=1 colspan=1>Technology</td><td rowspan=1 colspan=1>5G NR</td></tr></table>

Table 5.5.2-2: Example power profile for 64T64R O-RU   

<table><tr><td rowspan=1 colspan=1>Operating Load (Traffic)</td><td rowspan=1 colspan=1>Total O-RU (W)</td><td rowspan=1 colspan=1>ORANFronthaul Processing Unit(W)</td><td rowspan=1 colspan=1>DigitalProcessingUnit (W)</td><td rowspan=1 colspan=1>RFProcessingUnit (W)</td><td rowspan=1 colspan=1>Power Supply &amp;othercomponents (W)</td></tr><tr><td rowspan=1 colspan=1>Busy hour load</td><td rowspan=1 colspan=1>1100</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>200</td><td rowspan=1 colspan=1>800</td><td rowspan=1 colspan=1>50</td></tr><tr><td rowspan=1 colspan=1>Low load</td><td rowspan=1 colspan=1>400</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>200</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>50</td></tr><tr><td rowspan=1 colspan=1>Sleep (Energy Savings State)</td><td rowspan=1 colspan=1>60~140</td><td rowspan=1 colspan=1>30~50</td><td rowspan=1 colspan=1>0~20</td><td rowspan=1 colspan=1>0~20</td><td rowspan=1 colspan=1>30~50</td></tr><tr><td rowspan=1 colspan=1>Energy saving gain</td><td rowspan=1 colspan=1>260~340</td><td rowspan=1 colspan=1>0~20</td><td rowspan=1 colspan=1>180~200</td><td rowspan=1 colspan=1>80~100</td><td rowspan=1 colspan=1>0~20</td></tr></table>

Compared to the low load scenario, energy savings of 260-340 W per O-RU can be achieved in the energy saving state. Example calculations for yearly energy saving potential considering a shutdown of 10000 ORUs during 3 hours per day are provided in Table 5.5.2-3.

Table 5.5.2-3: Power saving calculation examples for 64T64R O-RU   

<table><tr><td rowspan=1 colspan=1>Factor</td><td rowspan=1 colspan=1>Value</td></tr><tr><td rowspan=1 colspan=1>O-RU power savings during switch off (low load) [W]</td><td rowspan=1 colspan=1>260~340</td></tr><tr><td rowspan=1 colspan=1> Number of hours of switch off per day (50% of low load period)</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>Number of O-Rus</td><td rowspan=1 colspan=1>10000</td></tr><tr><td rowspan=1 colspan=1>Yearly energy saving [MWh]</td><td rowspan=1 colspan=1>2847~3723</td></tr></table>

# 5.6 Feasibility Analysis

No challenges concerning feasibility have been identified during the pre-normative phase.

# 6

# RF Channel Reconfiguration

# 6.1 Problem Statement, Solution and Value Proposition

In mobile networks mMIMO antennas are used for beamforming techniques to enhance cell capacity and throughput. In order to achieve beamforming, O-RUs need to concentrate the power amplifiers at the radome by combining radiating elements. At low load, i.e., when the expected traffic volume or number of connected users are lower than the configured threshold, ES can be achieved by reducing the power consumption of ORUs by switching off certain $\mathrm { T x } / \mathrm { R x }$ arrays. For example, 32 out of $6 4 \mathrm { T x } / \mathrm { R x }$ Arrays of an O-RU can be switched off in a digital mMIMO architecture and correspondingly the number of spatial layers and SSBs can be reduced. The procedure (involvement of respective O-RAN interfaces) of the RF Channel Reconfiguration depends on the management architecture model (hybrid or hierarchical) and the deployment option. The reconfiguration decision can be made by an AI/ML model within the inference host deployed at the Non-RT RIC (denoted as deployment Option 1), or at the Near-RT RIC (denoted as deployment option 2). Among others the AI/ML models may include prediction of future traffic, user mobility, and resource usage and may also predict expected energy efficiency enhancements, resource usage, and network performance for different ES optimization states.

The main aim of RF Channel Reconfiguration is to perform O-RU Tx/Rx Array selection. However, Tx/Rx Array reselection may require modifying the maximum number of spatial streams, the number of SSB Beams or the O-RU Antenna transmit power. Hence the overall scope of RF Channel Reconfiguration includes the actions listed in Table 6.1-1.

Table 6.1-1: Actions in the context of RF Channel Reconfiguration   

<table><tr><td rowspan=1 colspan=1>Action Name</td><td rowspan=1 colspan=1>Explanation</td><td rowspan=1 colspan=1>Possible Implementation Method</td></tr><tr><td rowspan=1 colspan=1>O-RU Tx/Rx Arrayselection</td><td rowspan=1 colspan=1>O-RU Tx/Rx Array selection meansswitching off certain Tx/Rx Arrays orArray elements to reduce powerconsumption of O-RU.Reselecting Rx/Tx Arrays may impactcell coverage.</td><td rowspan=1 colspan=1>O-RU reports all supported Tx/Rx Arrayselections to O-DU or to SMO via OpenFH M-Plane.Based on traffic load and user distributionthe Non-RT/Near RT RIC will optimizeTx/Rx Array selection.</td></tr><tr><td rowspan=1 colspan=1>Modification of numberof SU/MU MIMO spatialstreams or data layers</td><td rowspan=1 colspan=1>The maximum number of spatialstreams may depend on the O-RUTx/Rx Array selection, and it may benecessary to be modified along with anew Tx/Rx Array selection.A reduction of the number of spatialstreams without Tx/Rx Array selectionis not excluded as in certain scenariosthe energy consumption of O-RUand/or O-DU may be reduced byturning off certain processing units ofFPGA/GPUs, by running at a lowerclock speed or turning off CPU/GPUcores along with reduced processingrequirements.</td><td rowspan=1 colspan=1>O-RU may report the maximum numberof supported spatial streams for eachTx/Rx Array selection. For example, 16spatial streams for 64 Tx/Rx and 8 spatialLayers for 32 Tx/Rx.Based on the traffic load and the userdistribution the O-RU will be instructedabout the maximum number of spatialstreams to be used. Hence, the O-RUand/or O-DU may be able turn off certainprocessing units that would be required toprocessing a higher number of spatialstreams.</td></tr><tr><td rowspan=1 colspan=1>Modification of thenumber of SSB beams</td><td rowspan=1 colspan=1>The number of SSB beams may dependon the O-RU Tx/Rx Array selectionand the number of spatial streams.Hence it may be necessary to adapt thenumber of SSB beams.</td><td rowspan=1 colspan=1>The number of SSB beams is controlledby the O-DU. Hence the O-DU can beinstructed via Non-RT/Near-RT RIC toset the number of SSB beams based onTx/Rx Array selection.</td></tr><tr><td rowspan=1 colspan=1>Modify the O-RUAntenna Transmit power</td><td rowspan=1 colspan=1>The maximum O-RU total transmitpower may depend upon the O-RUTx/Rx Array selection; hence it mayneed to be modified along with Tx/RxArray selection to compensate forreduced coverage in the downlink.</td><td rowspan=1 colspan=1>The O-RU power is configured per TxArray. Hence, the modification may notbe required when O-RU Tx/Rx Arrayselection from 64 Tx/Rx to 32 Tx/Rx.However, if possible, O-RU Tx powercan be increased to compensate forreduced coverage.</td></tr></table>

# 6.2 Architecture/Deployment Options

# 6.2.1 Option 1: Non-RT RIC Deployment

In option 1, decision making, potentially including AI/ML Model Training and Inference, is done at the NonRT RIC.

# 6.2.1.1 Description and UML Diagram

Table 6.2.1.1-1: RF Channel Reconfiguration: AI/ML inference via Non-RT RIC   

<table><tr><td rowspan=1 colspan=1>Use Case Stage</td><td rowspan=1 colspan=1>Evolution / Specification</td><td rowspan=1 colspan=1>&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td rowspan=1 colspan=1>Goal</td><td rowspan=1 colspan=1>Enable RF Channel Reconfiguration Energy Saving functions in theNetwork by means of configuration parameter change and actionscontrolled by Non-RT RIC to enable Al/ML-based solutions.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Actors and Roles</td><td rowspan=1 colspan=1>Non-RT RIC acting as inference host for Energy Savings decisionmaking.E2 Node and O-RU are the subject of action for configurationenforcement.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Assumptions</td><td rowspan=1 colspan=1>O1 interface connectivity is established between E2 Nodes and SMO.Open FH M-Plane interface is established between E2 Node and O-RU or between O-RU and SMO.Network is operational.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Pre-conditions</td><td rowspan=1 colspan=1>The operator has set the targets for Energy Saving functions in theNon-RT RIC (rApp).Capability of O-RU to support various RF Channel Reconfigurationactions.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Begins when</td><td rowspan=1 colspan=1>The operator enables the optimization functions for RF ChannelReconfiguration Energy Saving and E2 Node and O-RU becomeoperational</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Steps 1.1, 1.2, 1.3,1.4 (M)</td><td rowspan=1 colspan=1>Non-RT RIC initiates specific measurement data collection request through SMO via O1 towards E2 Node or via Open FH M-Plane directlytowards O-RU for Al/ML model training for Energy Saving optimization</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Steps 2.1, 2.2, 2.3,2.4 (M)</td><td rowspan=1 colspan=1>E2 Node and O-RU send the configured measurement data to SMOperiodically or event based for Non-RT RIC processing. Non-RT RICretrieves data through SMO from E2 Node and from O-RU.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 3 (M)</td><td rowspan=1 colspan=1>Non-RT RIC retrieves the collected measurement data for processing.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Steps 4.1, 4.2, 4.3(M)</td><td rowspan=1 colspan=1>Non-RT RIC trains the Al/ML models with the collected data. TrainedAl/ML models are deployed and activated in the Non-RT RIC.Non-RT RIC constantly monitors performance and energyconsumption of the E2 Node and the O-RU for inference, such as cellload related and trafic information, EE/EC measurement reports,geolocation information etc.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 5 (M)</td><td rowspan=1 colspan=1>Based on the Al/ML inference, the Non-RT RIC may request the SMOto configure E2 Node (O-DU) and execute RF ChannelReconfiguration for ES/EE optimization.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Steps 6.1, 6.2, 6.3,6.4 (M)</td><td rowspan=1 colspan=1>SMO instructs E2 Node via O1 to perform the received request(s) fromNon-RT RICi.  O-RU Tx/Rx Array selection.ii. Modify the numbér of SU/MU MIMO spatial streams or datalayers.ii.  Modify the number of SSB beams.iv. Modify O-RU Antenna Transmit power.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 7 (M)</td><td rowspan=1 colspan=1>Non-RT RIC continuously monitors the performance of Al/ML model. Ifenergy saving objectives are not achieved, it may decide to initiatefallback mechanism, and/or Al/ML model update or retraining.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Ends when</td><td rowspan=1 colspan=1> If E2 Node becomes non-operational or when the operator disables theoptimization functions for Energy Saving.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Exceptions</td><td rowspan=1 colspan=1>None</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Post Conditions</td><td rowspan=1 colspan=1>Non-RT RIC continues closed loop monitoring of Energy Savingfunction for E2 Node and O-RU.E2 Node and O-RU operate using the newly deployed parameters andstate.</td><td rowspan=1 colspan=1></td></tr></table>

@startuml   
skinparam defaultFontSize 12   
autonumber   
Box "Service Management & \n Orchestration Framework" #gold   
Participant “Collection & Control” as smo   
Participant " Non-RT RIC" as NRTRIC   
End box Box "O-RAN Nodes" #lightpink Participant "Near-RT RIC" as RTRIC Participant "E2-Node" as E2NODES Participant "O-RU" as ORUs

End box

autonumber 1.1   
group Data Collection   
alt via O1   
smo -> E2NODES : $< < 0 1 > >$ Data collection request for Energy Saving   
E2NODES -> ORUs : <<FH>> Data collection request   
Else via OFH-MP   
smo -> E2NODES : <<O1>> Data collection request for Energy Saving   
smo -> ORUs <<OFH-MP>> Data collection request   
end   
autonumber 2.1   
alt Via O1   
ORUs -> E2NODES : <<FH>> Measurement Data Collection   
E2NODES -> smo : <<O1>> Measurement Collection for Energy Saving   
Else via OFH-MP   
ORUs -> smo : <<FH>> Measurement Data Collection   
E2NODES -> smo : $< < 0 1 > >$ Measurement Collection for Energy Saving   
End   
autonumber 3   
smo $- >$ NRTRIC : $< < 0 1 > >$ Data Retrieval   
end   
group Data Analysis Training and Inference   
autonumber 4.1 NRTRIC $- >$ NRTRIC : AI/ML Model training NRTRIC $- >$ NRTRIC : Deploy & activate trained AI/ML Model for inferencing NRTRIC $- >$ NRTRIC : Monitoring & Analysis of Energy Efficiency \n & Consumption (E2   
Node & O-RU)   
autonumber 5   
group Actor Decision Making

NRTRIC $- >$ smo : Request to prepare and execute RF Channel Reconfiguration \nenforecement for Energy saving autonumber 6.1

end   
autonumber 7   
NRTRIC $- >$ NRTRIC : Performance analysis of AI/ML model \n(with possible actions, e.g. fallback, re-training)   
end   
@enduml

![](images/ba258a0679f21d820e74d1389decf634c7a575d5cfc42992c34abde18c77cef1.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.2.1.1-1: RF Channel Reconfiguration flow diagram: AI/ML inference in Non-RT RIC

# 6.2.1.2 O-RAN Entity Roles

1) SMO (including Non-RT RIC)

a) Collect necessary cell configurations, performance indicators and measurement reports (e.g., cell load related and traffic information, EE/EC measurement reports, geolocation information) from E2 Node and O-RU, for the purpose of training and inference of AI/ML models that assist in the EE/ES functions.

b) Trigger EE/ES AI/ML model training/retraining.

c) Deploy, update, and configure EE/ES AI/ML models d) Analyze the data received from E2 Nodes and O-RU to determine RF Channel Reconfiguration actions for EE/ES, i.e., O-RU Tx/Rx Array selection, modification of the number of SSB beams, modification of the O-RU Antenna Transmit power, modification of the number of SU/MU MIMO spatial streams or data layers using AI/ML models.

e) Signal updated RF Channel Reconfiguration and execution of optimization actions to E2 Node via O1 Interface.

# 2) E2 Node

a) Report necessary cell configurations, performance indicators, and measurement reports (e.g., cell load related and traffic information, EE/EC measurement reports) to SMO via O1 interface.   
b) Perform actions required to perform RF Channel Reconfiguration (i.e., O-RU Tx/Rx Array selection, modification of the number of SSB beams, modification of the O-RU Antenna Transmit power, modification of the number of SU/MU MIMO data layers or spatial streams) as part of EE/ES optimization.

# 3) O-RU

a) Report EC and EE related information over Open FH M-Plane to O-DU or alternatively to SMO directly.   
b) Perform actions required to be performed due to RF Channel Reconfiguration (i.e., O-RU Tx/Rx Array selection, modification of the number of SSB beams, modification of the O-RU Antenna Transmit power, modification of the number of SU/MU MIMO spatial streams or data layers) as part of EE/ES optimization.

# 6.2.1.3 Input/Output Data Requirements

# 6.2.1.3.1 Summary

# Input Data

1) SMO and E2 Node

➢ Load statistics per cell and per carrier, such as number of active users, average number of RRC connections, average number of scheduled active users per TTI, PRB utilization, DL/UL Cell/User throughput, PMI/CSI reports.   
➢ Latency statistics per cell (if URLLC slices are involved, latency is used in the EE definition, 3GPP TS 28.554 [7]).

# 2) O-RU

Power consumption metrics: Mean total/per carrier power consumption, mean total/per carrier transmit power.

Information on supported Tx/Rx Array selections along with power consumption (site/O-RU input power needed for certain EE KPIs)

# Output Data

1) SMO to E2 Node

RF Channel Reconfiguration actions which can include, $\bigcirc$ O-RU Tx/Rx Array selection $\bigcirc$ Modify the number of SU/MU MIMO spatial streams or data layers $\bigcirc$ Modify the number of SSB beams $\bigcirc$ Modify O-RU Antenna Transmit power

# 6.2.1.3.2 Detailed Input Requirements

Initialization:

Table 6.2.1.3-1: Initialization   

<table><tr><td colspan="6" rowspan="1">Input Data</td></tr><tr><td colspan="1" rowspan="1">Interface</td><td colspan="1" rowspan="1">Source /Target</td><td colspan="1" rowspan="1">Name/Description</td><td colspan="1" rowspan="1">Units</td><td colspan="1" rowspan="1">ReportingPeriod</td><td colspan="1" rowspan="1">Existing / NewDefinitions</td></tr><tr><td colspan="1" rowspan="2">R1</td><td colspan="1" rowspan="2">SMO / rApp</td><td colspan="1" rowspan="1">Optimization target for RF ChannelReconfiguration</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">manual orevent triggered</td><td colspan="1" rowspan="1">New</td></tr><tr><td colspan="1" rowspan="1">E.g., (average or max) NG-RAN dataEnergy Efficiency</td><td colspan="1" rowspan="1">bit/J</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">3GPP TS 28.554 [7](C1. 6.7.1)</td></tr><tr><td colspan="1" rowspan="1">R1</td><td colspan="1" rowspan="1">SMO / rApp</td><td colspan="1" rowspan="1">Maximum Initial Access Latency forgiven SSB Beam Configuration</td><td colspan="1" rowspan="1">ms</td><td colspan="1" rowspan="1">Initialization</td><td colspan="1" rowspan="1">New: KPI metric input by the operator</td></tr><tr><td colspan="1" rowspan="2">O1, R1</td><td colspan="1" rowspan="2">O-DU / SMO/rApP</td><td colspan="1" rowspan="1">Carrier/cell characteristics</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">manual orevent triggered(e.g. MOfeatureactivation, E2Nodestartup/failure/reconfig.)</td><td colspan="1" rowspan="1">New</td></tr><tr><td colspan="1" rowspan="1">E.g., physical location, transmitdirection, carrier frequency, coverageparameters, configured transmitpower, beam width, coverage shape,tilt, azimuth, carrier-cel mapping,carrier-HW mapping</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">3GPP TS 28.541 [11](C1. 4.3.6, 4.3.38,4.3.39, 4.3.40,4.3.74)O-RAN.WG5.O-DU-O1 (Sec. 10), O-RAN-WG5.O-CU-01 (Sec.9)</td></tr><tr><td colspan="1" rowspan="1">O-FH (M-Plane)orO-FH (M-Plane), 01,R1</td><td colspan="1" rowspan="1">O-RU /O-DUorO-RU/O-DU/ SMO / rApp</td><td colspan="1" rowspan="1">Supported common beamconfiguration from O-RU per cell</td><td colspan="1" rowspan="1">file</td><td colspan="1" rowspan="1">Initialization</td><td colspan="1" rowspan="1">O-RAN.WG5.MP(Sec. 8.1)</td></tr><tr><td colspan="1" rowspan="1">O-FH (M-Plane)</td><td colspan="1" rowspan="1">O-RU / O-DU</td><td colspan="1" rowspan="1">Beamforming weights or attributesvia YANG module per cell</td><td colspan="1" rowspan="1">valuesinIE</td><td colspan="1" rowspan="1">Initialization</td><td colspan="1" rowspan="1">O-RAN.WG4.CUS(Sec. 12.4.2)</td></tr><tr><td colspan="1" rowspan="1">R1, O1, O-FH (M-Plane)orO-FH (M-Plane)</td><td colspan="1" rowspan="1">rApp / SMO /O-DU / O-RUorO-DU /O-RU</td><td colspan="1" rowspan="1"> Inferred SSB beam configuration inspecifi ed fi le per cell</td><td colspan="1" rowspan="1">file</td><td colspan="1" rowspan="1">Initialization</td><td colspan="1" rowspan="1">O-RAN.WG4.CUS(Sec. 12.4.2)</td></tr><tr><td colspan="1" rowspan="1">01, R1</td><td colspan="1" rowspan="1">O-DU / SMO/rApp</td><td colspan="1" rowspan="1">Supported SSB and CSI-RS TRSconfigurations per cell</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">Initialization</td><td colspan="1" rowspan="1">3GPP TS 38.331 [16](Sec. 6.3.2)</td></tr><tr><td colspan="1" rowspan="1">O-FH (M-Plane), O1,R1</td><td colspan="1" rowspan="1">O-RU / O-DU/ SMO / rApp</td><td colspan="1" rowspan="1">O-RU reports all offered Tx/RxArrays</td><td colspan="1" rowspan="1">file</td><td colspan="1" rowspan="1">Initialization</td><td colspan="1" rowspan="1">New Definitionrequired in O-RAN.WG5.MPO-ran-uplane-conf.yang moduleO-ran-beamforming.yangmodule</td></tr><tr><td colspan="1" rowspan="1">O-FH (M-Plane)</td><td colspan="1" rowspan="1">O-RU / O-DU</td><td colspan="1" rowspan="1">O-RU reports all offered Tx/RxArrays</td><td colspan="1" rowspan="1">valuesin IE</td><td colspan="1" rowspan="1">Initialization</td><td colspan="1" rowspan="1">New Definitionrequired in O-RAN.WG4.MPO-ran-uplane-conf.yang moduleO-ran-beamforming.yangmodule</td></tr></table>

AI/ML Model Training:

Table 6.2.1.3-2: AI/ML Model Training   

<table><tr><td rowspan=1 colspan=6>Input Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source / Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod</td><td rowspan=1 colspan=1>Existing / NewDefinitions</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / sMO/rApp</td><td rowspan=1 colspan=1>DL PDCP SDU Data Volume per interface (Data Volume in DLdelivered from O-CU-UP to O-DU,per PLMN, per QoS level, per slice,per Interface (F1-U, Xn-U, X2-U))</td><td rowspan=1 colspan=1>Mbit</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.3.6.2.3)</td></tr><tr><td rowspan=1 colspan=1>01,R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / sMO /rApp</td><td rowspan=1 colspan=1>UL PDCP SDU Data Volume per interface (Data Volume in ULdelivered to O-CU-UP from O-DU,per PLMN, per QoS level, per slice, per Interface (F1-U, Xn-U, X2-U))</td><td rowspan=1 colspan=1>Mbit</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.3.6.2.4)</td></tr><tr><td rowspan=1 colspan=1>01,R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / SMO/ rApp</td><td rowspan=1 colspan=1>Number of active UEs in NG-RAN(Number of RRC_CONECTEDUEs) per cell</td><td rowspan=1 colspan=1>Integer</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](Sec. 5.1.1.23, A7,A.60)</td></tr><tr><td rowspan=1 colspan=1>01,R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / sMO/rApp</td><td rowspan=1 colspan=1>RSRQ measurement per SSB per cell</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12] (C1. 5.1.1.31)</td></tr><tr><td rowspan=1 colspan=1>O1,R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / sMO /rApp</td><td rowspan=1 colspan=1>RSRP measurement per SSB per cell</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.22)</td></tr><tr><td rowspan=1 colspan=1>O1,R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / SMO /rApp</td><td rowspan=1 colspan=1>SINR measurement per SSB per cell</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>&gt;min</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.32)</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / SMO /rApp</td><td rowspan=1 colspan=1>Energy consumption</td><td rowspan=1 colspan=1>kWh</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.19.3)</td></tr><tr><td rowspan=1 colspan=1>O-FH (M-Plane)d)orO-FH (M-Plane),01, R1</td><td rowspan=1 colspan=1>O-RU / O-DUorO-RU /O-DU /SMO /rApp</td><td rowspan=1 colspan=1>Power consumed by O-RU or itshardware components</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS28.552 [12](C1. 5.1.1.19.2)Reporting:O-RAN.WG4.MP(Sec. B.1, B.5)</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-DU) / SMO/rApp</td><td rowspan=1 colspan=1>Over the air transmit power by O-RUas calculated in O-DUNote: This measurement is required to calculate energy efficiency of O-RU.</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>New Measurement andNew Reportingrequired in O-RAN.WG5.MP</td></tr></table>

Input Decision Making / AI/ML Inference:

Table 6.2.1.3-3: Input Decision Making / AI/ML Inference   

<table><tr><td rowspan=1 colspan=6>Input Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source / Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod</td><td rowspan=1 colspan=1>Existing / NewDefinitions</td></tr><tr><td rowspan=1 colspan=1>01,R1</td><td rowspan=1 colspan=1>E2 Node (O-CU)/ SMO / rApp</td><td rowspan=1 colspan=1>DL PDCP SDU Data Volume per interface (Data Volume in DLdelivered from O-CU-UP to O-DU,per PLMN, per QoS level, per slice, per Interface (F1-U, Xn-U, X2-U))</td><td rowspan=1 colspan=1>Mbit</td><td rowspan=1 colspan=1>&gt;min</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.3.6.2.3)</td></tr><tr><td rowspan=1 colspan=1>01,R1</td><td rowspan=1 colspan=1>E2 Node (O-CU)/ SMO/rApp</td><td rowspan=1 colspan=1>UL PDCP SDU Data Volume per interface (Data Volume in ULdelivered to O-CU-UP from O-DU,per PLMN, per QoS level, per slice,per Interface (F1-U, Xn-U, X2-U))</td><td rowspan=1 colspan=1>Mbit</td><td rowspan=1 colspan=1>&gt;min</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.3.6.2.4)</td></tr><tr><td rowspan=1 colspan=1>O1, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU)/ SMO/ rApp</td><td rowspan=1 colspan=1>Number of active UEs in NG-RAN (Number of RRC_CONECTED UEs)per cell</td><td rowspan=1 colspan=1>Integer</td><td rowspan=1 colspan=1>&gt;min</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](Sec. 5.1.1.23, A.7,A.60)</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU)/ MO/rApp</td><td rowspan=1 colspan=1>RSRQ measurement per SSB per cell</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>&gt;min</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.31)</td></tr><tr><td rowspan=1 colspan=1>01,R1</td><td rowspan=1 colspan=1>E2 Node (O-CU)/ MO/rApp</td><td rowspan=1 colspan=1>RSRP measurement per SSB per cell</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>&gt;min</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.22)</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU)/ MO/ rApp</td><td rowspan=1 colspan=1>SINR measurement per SSB per cell</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>&gt;min</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.32)</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU)/ SMO / rApp</td><td rowspan=1 colspan=1>Energy consumption</td><td rowspan=1 colspan=1>kWh</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.19.3)</td></tr><tr><td rowspan=1 colspan=1>O-FH (M-Plane)orO-FH (M-Plane),O1, R1</td><td rowspan=1 colspan=1>O-RU / O-DUorO-RU /O-DU /SMO / rApp</td><td rowspan=1 colspan=1>Power consumed by O-RU or itshardware components</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.19.2)Reporting:O-RAN.WG4.MP(Sec. B.1, B.5)</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-DU)/ SMO / rApp</td><td rowspan=1 colspan=1>Over the air transmit power by O-RUas calculated in O-DUNote: This measurement is requiredto calculate energy efficiency of O-RU.</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>New Measurement andNew Reportingrequired in O-RAN.WG5.MP</td></tr></table>

# 6.2.1.3.3 Detailed Output Requirements

Output Decision Making / AI/ML Inference:

Table 6.2.1.3-4: Output Decision Making / AI/ML Inference   

<table><tr><td rowspan=1 colspan=6>Output Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source / Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod</td><td rowspan=1 colspan=1>Existing / NewDefinitions</td></tr><tr><td rowspan=3 colspan=1>O-FH (M-Plane)</td><td rowspan=3 colspan=1>O-DU / O-RU</td><td rowspan=1 colspan=1>Candidate O-RU&#x27;s appropriate arrayselection</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>&gt; min</td><td rowspan=1 colspan=1>O-RAN.WG4.MP0-ran-uplane-conf.yang</td></tr><tr><td rowspan=1 colspan=1>Maximum number of Max SU/MUMIMO spatial streams or data layers</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>&gt;min</td><td rowspan=1 colspan=1>New Definition required in O-RAN.WG4.MP</td></tr><tr><td rowspan=1 colspan=1>Recommended O-RU AntennaTransmit power</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>&gt; min</td><td rowspan=1 colspan=1>O-RAN.WG4.MPurn:o-ran:uplane-confModulegain</td></tr><tr><td rowspan=4 colspan=1>R1, 01</td><td rowspan=4 colspan=1>rApp / SMO/O-DU</td><td rowspan=1 colspan=1>Candidate O-RU&#x27;s appropriate arrayselection</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>&gt; min</td><td rowspan=1 colspan=1>New Definition requiredin WG2 R1 and O-RAN.WG5.O-DU-01</td></tr><tr><td rowspan=1 colspan=1>Maximum number of Max SU/MUMIMO spatial streams or data layers</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>&gt;min</td><td rowspan=1 colspan=1>New Definition required in O-RAN.WG4.MP</td></tr><tr><td rowspan=1 colspan=1>Inferred O-RU SS Burst Set (SS BlockNumber and SS Burst Periodicity) andCSI-RS TRS Configuration</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>Initialization</td><td rowspan=1 colspan=1>3GPP TS 38.331 [16]IE:ServingCellConfigCommon</td></tr><tr><td rowspan=1 colspan=1>Recommended O-RU AntennaTransmit power</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>&gt; min</td><td rowspan=1 colspan=1>O-RAN.WG4.MPurn:o-ran:uplane-confModulegain</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-DU) / SMO/rApp</td><td rowspan=1 colspan=1>Confirmation (Success/Failure)</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>eventtriggered</td><td rowspan=1 colspan=1>New</td></tr></table>

# 6.2.2 Option 2: Near-RT RIC Deployment

In option 2, decision making, potentially using AI/ML Model Inference, is done at Near-RT RIC. While AI/ML Model training might be hosted in the Non-RT or in the Near-RT RIC, the description below is based on AI/ML Model Training in the Non-RT RIC.

# 6.2.2.1 Description and UML Diagram

Table 6.2.2.1-1: RF Channel Reconfiguration: AI/ML inference via Near-RT RIC   

<table><tr><td rowspan=1 colspan=1>Use Case Stage</td><td rowspan=1 colspan=1>Evolution / Specification</td><td rowspan=1 colspan=1>&lt;&lt;Uses&gt;&gt;Relateduse</td></tr><tr><td rowspan=1 colspan=1>Goal</td><td rowspan=1 colspan=1>Enable RF Channel Reconfiguration Energy Saving functions in the Networkby means of configuration parameter change and actions controlled by Near-RT RIC and allow for Al/ML-based solutions.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Actors and Roles</td><td rowspan=1 colspan=1>Near-RT RIC acting as inference host for Energy Savings decision making.E2 Node and O-RU are the subject of action for configuration enforcement.SMO/Non-RT RiC acting as policy maker or trigger for ES optimization inNear-RT RIC.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Assumptions</td><td rowspan=1 colspan=1>O1 interface connectivity is established between E2 Node, Near-RT RIC, andSMO.E2 interface connectivity is established between E2 Node and Near-RT RIC.A1 interface is established between Non-RT RIC and Near-RT RIC.Open FH M-Plane interface is established between E2 Node and O-RU orbetween O-RU and SMO.Network is operational.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Pre-conditions</td><td rowspan=1 colspan=1>The operator has set the targets for the Energy Saving function in the Non-RT RIC (rApp).Capability of O-RU for various RF Channel Reconfiguration actions.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Begins when</td><td rowspan=1 colspan=1>Operator enables the optimization functions for RF Channel ReconfigurationEnergy Saving and E2 Node and O-RU become operational.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Steps 1.1,1.2, 1.3(M)</td><td rowspan=1 colspan=1>SMO initiates specific measurement data collection request towards E2Node and O-RU for Al/ML model training for Energy Saving optimization.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Steps 2.1, 2.2, 2.3,2.4 (M)</td><td rowspan=1 colspan=1>E2 Node and O-RU send the configured measurement data to SMOperiodically or event based for Non-RT RIC processing.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 3 (M)</td><td rowspan=1 colspan=1>Non-RT RIC retrieves the collected measurement data for processing.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Steps 4.1, 4.2, 4.3(M)</td><td rowspan=1 colspan=1>Non-RT RIC trains the Al/ML models with the collected data. Trained Al/MLmodels are deployed and activated in Near-RT RIC through SMO over O1 orO2 Interface. Non-RT RIC constantly monitors performance and energy consumption ofthe E2 Node and the O-RU for inference, such as cel load related and trafficinformation, EE/EC measurement reports, geolocation information etc.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Steps 5.1, 5.2 (M)</td><td rowspan=1 colspan=1>SMO may trigger RF Channel Reconfiguration in the Near-RT RIC via O1interface or optionally Non-RT RIC may provide policies via A1 interfaceguiding the Near-RT RIC RF Channel Reconfiguration EE/ES function.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Steps 6.1, 6.2, 6.3,6.4, 6.5, 6.6 (M)</td><td rowspan=1 colspan=1>Based on the Al/ML inference in Near-RT RIC, considering optimizationpolicies, the Near-RT RIC may request the E2 Node to prepare and executeRF Channel Reconfiguration.E2 Node may request O-RU to prepare and execute RF ChannelReconfiguration changes such as,i.  O-RU Tx/Rx Array selectioni. Modification of the number of SU/MU MIMO spatial streams ordata layers.ii.  Modification of the number of SSB beams.iv. Modification of the O-RU Antenna Transmit power.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Steps 7.1, 7.2 (M)</td><td rowspan=1 colspan=1>Based on performance analysis of Al/ML model, Non-RT RIC may updateAIML model in Near-RT RIC.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Ends when</td><td rowspan=1 colspan=1>E2 Node becomes non-operational or when the operator disables theoptimization functions for Energy Saving.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Exceptions</td><td rowspan=1 colspan=1>None</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Post Conditions</td><td rowspan=1 colspan=1>Non-RT RIC continues closed loop monitoring of Energy Saving function forE2 Node and O-RU.E2 Node and O-RU operate using the newly deployed parameters/modelsand state.</td><td rowspan=1 colspan=1></td></tr></table>

@startuml   
skin rose   
skinparam defaultFontSize 15   
autonumber   
Box "Service Management & \n Orchestration Framework" #gold   
Participant “Collection & Control” as smo   
Participant " Non-RT RIC" as NRTRIC   
End box   
Box "O-RAN Nodes" #lightpink   
Participant "Near-RT RIC" as RTRIC   
Participant "E2-Nodes" as E2NODES   
Participant "O-RUs" as ORUs   
End box   
autonumber 1.1   
group Data Collection   
alt via O1   
smo -> E2NODES : $< < 0 1 > >$ Data collection request for Energy Saving   
E2NODES -> ORUs : <<FH>> Data collection request   
Else via OFH-MP   
smo -> ORUs : <<OFH-MP>> Data collection request   
end   
autonumber 2.1   
alt Via O1   
ORUs -> E2NODES : <<FH>> Measurement Data Collection   
E2NODES -> smo : $< < 0 1 > >$ Measurement Collection for Energy Saving   
Else via OFH-MP   
ORUs -> smo : <<FH>> Measurement Data Collection   
E2NODES -> smo : $< < 0 1 > >$ Measurement Collection for Energy Saving   
End   
autonumber 3   
smo $- >$ NRTRIC : $< < 0 1 > >$ Data Retrieval   
end   
autonumber 4.1   
group AI/ML workflow   
NRTRIC $- >$ NRTRIC : AI/ML Model training   
NRTRIC $- >$ NRTRIC : Monitoring & Analysis of Energy Efficicincy \n & Consumption (E2 Nodes & O-RU)(s   
NRTRIC $- >$ RTRIC : $< < 0 1 > >$ or $< < 0 2 > >$ Deploy AI/ML model   
end   
autonumber 5.1   
group Optimization Trigger and Policy   
alt via O1   
smo $- >$ RTRIC : $< < 0 1 > >$ Optimization Trigger/Target   
else via A1   
NRTRIC --> RTRIC : $< < \mathbb { A } 1 > >$ Intent based Policy   
end   
autonumber 6.1   
group Actor Data Collection & Decision Making   
RTRIC -> E2NODES : $< < \mathrm { E } 2 > >$ Data collection request for Energy Saving   
E2NODES -> ORUs : <<FH>> Data collection request for Energy Saving   
ORUs -> E2NODES : <<FH>> Measurement Data Collection for Energy Saving   
E2NODES $- >$ RTRIC : $< < \mathrm { E } 2 > >$ Measurement Data Collection for Energy Saving   
RTRIC $- >$ RTRIC: AI/ML model inference   
RTRIC -> E2NODES: <<E2>> RF Channel Reconfiguration \nenforecement for Energy saving E2NODES -> ORUs: <<FH>> Updated O-RU Configurations   
autonumber 6.1   
group AI/ML workflow   
NRTRIC $- >$ NRTRIC : Performance analysis of AI/ML model \n(with possible actions, e.g. fallback, re-training)   
NRTRIC $- >$ RTRIC : $< < 0 1 > >$ or $< < 0 2 > >$ Update AI/ML model   
end

![](images/deaaf5900d8801b04fa88d1c35a9b0b64c3b575ba660e33f6309c75f5a0ac5ba.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.2.2.1-1: RF Channel Reconfiguration flow diagram: AI/ML inference in Near-RT RIC

# 6.2.2.2 O-RAN Entity Roles

1) SMO (including Non-RT RIC)

a) Collect necessary cell configurations, performance indicators and measurement reports (e.g., cell load related and traffic information, EE/EC measurement reports, geolocation information) from E2 Node and O-RU, for the purpose of training AI/ML models that assist in the EE/ES functions.   
b) Trigger and perform EE/ES AI/ML model training/retraining.   
c) Analyze the data received from E2 Node and O-RU to trigger optimization for RF Channel Reconfiguration.   
d) Provide optimization trigger, optimization targets, and A1 policies (e.g., change of Tx/Rx Array Selection based on $50 \%$ peak power consumptions) to Near-RT RIC via O1 or A1 interface.

# 2) Near-RT RIC

a) Collect necessary cell configurations, performance indicators and measurement reports (e.g., cell load related and traffic information, EE/EC measurement reports) from E2 Nodes and O-RU.   
b) Receive EE/ES AI/ML model for deployment via O1 or O2.   
c) Receive EE/ES related configuration management via O1 interface and/or policies via A1 interface for consideration during optimization.   
d) Analyze the data received from E2 Node and perform AI/ML model inference to determine RF Channel Reconfiguration actions for EE/ES (e.g., O-RU Tx/Rx Array Selection, modification of the number of SSB beams, modification of the O-RU Antenna Transmit power, modification of the number of SU/MU MIMO spatial streams or data layers) to be performed considering the optimization targets/policies.   
e) Provide policies and/or required information over E2 interface to trigger actions for EE/ES optimization.

3) E2 Node

a) Report necessary cell configurations, performance indicators and measurement reports (e.g., cell load related and traffic information, EE/EC measurement reports) to SMO via O1 interface and to Near-RT RIC via E2 or O1 Interface.   
b) Perform O-RU Tx/Rx Array Selection, modification of the number of SSB beams, modification of the O-RU Antenna Transmit power, modification of the number of SU/MU MIMO spatial streams or data layers as part of RF Channel Reconfiguration actions for EE/ES optimization.

# 4) O-RU

a) Report EC and EE related information over Open FH M-Plane interface to O-DU or alternatively to SMO directly.   
b) Perform actions required to perform O-RU RF Channel Reconfiguration as part of EE/ES optimization.   
c) Perform actions such as O-RU Tx/Rx Array Selection, modification of the number of SSB beams, modification of the O-RU Antenna Transmit power, modification of the number of SU/MU MIMO spatial streams or data layers as part of RF Channel Reconfiguration actions for EE/ES optimization.

# 6.2.2.3 Input/Output Data Requirements

6.2.2.3.1 Summary

# Input Data

1) SMO and E2 Node

➢ Load statistics per cell and per carrier, such as number of active users, average number of RRC connections, average number of scheduled active users per TTI, PRB utilization, DL/UL Cell/User throughput, PMI/CSI reports.   
➢ Latency statistics per cell (if URLLC slices are involved, latency is used in the EE definition, 3GPP TS 28.554 [7]).

# 2) O-RU

Power consumption metrics: Mean total/per carrier power consumption, mean total/per carrier transmit power.   
Information of O-RU for supported Tx/Rx Array selection along with power consumption (site/O-RU input power needed for certain EE KPIs).

# Output Data

1) Non-RT RIC to Near RT RIC ➢ O1 Configuration (i.e., ES optimization trigger/target) OR ➢ A1 Policy for ES optimization

2) Near-RT RIC to E2 Node to O-RU

RF Channel Reconfiguration actions which can include, $\bigcirc$ O-RU Tx/Rx Array selection $\bigcirc$ Modification of the number of SU/MU MIMO spatial streams or data layers o Modification of the number of SSB beams $\bigcirc$ Modification of the O-RU Antenna Transmit power

# 6.2.2.3.2 Detailed Input Requirements

Initialization:

Table 6.2.2.3-1: Initialization   

<table><tr><td rowspan=1 colspan=6>Input Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source / Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod</td><td rowspan=1 colspan=1>Existing / NewDefinitions</td></tr><tr><td rowspan=2 colspan=1>01</td><td rowspan=2 colspan=1>SMO / Near-RTRIC</td><td rowspan=1 colspan=1>EE Optimization target for RFChannel Re-configuration</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>manual orevent triggered</td><td rowspan=1 colspan=1>New</td></tr><tr><td rowspan=1 colspan=1>E.g. (average or max) NG-RAN dataEnergy Efficiency</td><td rowspan=1 colspan=1>bit/J</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3GPP TS 28.554 [7](C1. 6.7.1)</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>SMO / Near-RTRIC</td><td rowspan=1 colspan=1>Maximum Initial Access Latency forgiven SSB Beam Configuration</td><td rowspan=1 colspan=1>ms</td><td rowspan=1 colspan=1>Initialization</td><td rowspan=1 colspan=1>New: KPI metric input by the operator</td></tr><tr><td rowspan=2 colspan=1>E2,01,R1</td><td rowspan=2 colspan=1>E2 Node (O-DU) Near-RTRIC / SMO/rApp</td><td rowspan=1 colspan=1>Carrier/cell characteristics</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>manual orevent triggered(e.g. SMOfeatureactivation, E2Nodestartup/failure/reconfig.)</td><td rowspan=1 colspan=1>New</td></tr><tr><td rowspan=1 colspan=1>E.g. physical location, transmitdirection, carrier frequency, coverageparameters, configured transmitpower, beam width, coverage shape,tilt, azimuth, carrier-cell mapping,carrier-HW mapping</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3GPP TS 28.541 [11](C1. 4.3.6, 4.3.38,4.3.39,4.3.40,4.3.74)</td></tr><tr><td rowspan=1 colspan=1>O-FH (M-Plane)</td><td rowspan=1 colspan=1>O-RU / O-DU</td><td rowspan=1 colspan=1>Supported common beamconfiguration from O-RU per cell</td><td rowspan=1 colspan=1>file</td><td rowspan=1 colspan=1>Initialization</td><td rowspan=1 colspan=1>O-RAN.WG5.MP(Chapter 8)</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>O-DU / Near-RT RIC</td><td rowspan=1 colspan=1>Supported SSB and CSI-RS TRSconfigurations per cell</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>Initialization</td><td rowspan=1 colspan=1>3GPP TS 38.331 [16](Sec. 6.3.2)</td></tr><tr><td rowspan=1 colspan=1>O-FH (M-Plane),01, R1</td><td rowspan=1 colspan=1>O-RU / O-DU /SMO /rApp</td><td rowspan=1 colspan=1>O-RU reports all offered Tx/RxArrays</td><td rowspan=1 colspan=1>file</td><td rowspan=1 colspan=1>Initialization</td><td rowspan=1 colspan=1>New Definitionrequired in O-RAN.WG5.MPO-ran-uplane-conf.yang moduleO-ran-beamforming.yangmodule</td></tr><tr><td rowspan=1 colspan=1>O-FH (M-Plane)</td><td rowspan=1 colspan=1>O-RU / O-DU</td><td rowspan=1 colspan=1>O-RU reports all offered Tx/RxArrays</td><td rowspan=1 colspan=1>valuesinIE</td><td rowspan=1 colspan=1>Initialization</td><td rowspan=1 colspan=1>New Definitionrequired in O-RAN.WG4.MPO-ran-uplane-conf.yang module0-ran-beamforming.yangmodule</td></tr></table>

AI/ML Model Training:

Table 6.2.2.3-2: AI/ML Model Training   

<table><tr><td rowspan=1 colspan=6>Input Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source /Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod</td><td rowspan=1 colspan=1>Existing/NewDefinitions</td></tr><tr><td rowspan=1 colspan=1>O1, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / sMO/rApp</td><td rowspan=1 colspan=1>DL PDCP SDU Data Volume per interface (Data Volume in DL deliveredfrom O-CU-UP to O-DU, per PLMN,per QoS level, per slice, per Interface(F1-U, Xn-U, X2-U))</td><td rowspan=1 colspan=1>Mbit</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.3.6.2.3)</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / SMO/rApp</td><td rowspan=1 colspan=1>UL PDCP SDU Data Volume per interface (Data Volume in UL delivered to O-CU-UP from O-DU, per PLMN,per QoS level, per slice, per Interface(F1-U, Xn-U, X2-U))</td><td rowspan=1 colspan=1>Mbit</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.3.6.2.4)</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / sMO/ rApp</td><td rowspan=1 colspan=1>Number of active UEs in NG-RAN (Number of RRC_CONECTED UEs)per cell</td><td rowspan=1 colspan=1>Integer</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](Sec. 5.1.1.23, A.7,A.60)</td></tr><tr><td rowspan=1 colspan=1>O1, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / sMO/rApp</td><td rowspan=1 colspan=1>RSRQ measurement per SSB per cell</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.31)</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / sMO/ rApp</td><td rowspan=1 colspan=1>RSRP measurement per SSB per cell</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>(nn-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.22)</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / MO/rApp</td><td rowspan=1 colspan=1>SINR measurement per SSB per cell</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>&gt;min</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.32)</td></tr><tr><td rowspan=1 colspan=1>O1, R1</td><td rowspan=1 colspan=1>E2 Node (O-DU) / SMO/rApp</td><td rowspan=1 colspan=1>Energy consumption</td><td rowspan=1 colspan=1>kWh</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.19.3)</td></tr><tr><td rowspan=1 colspan=1>O-FH (M-Plane)orO-FH (M-Plane),01, R1</td><td rowspan=1 colspan=1>O-RU / O-DUorO-RU / O-DU/ SMO /rApp</td><td rowspan=1 colspan=1>Power consumed by O-RU or itshardware components</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.19.2)Reporting:O-RAN.WG4.MP(Sec. B.1, B.5)</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-DU) / SMO/rApp</td><td rowspan=1 colspan=1>Over the air Transmit power by O-RUNote: This measurement is required tocalculate energy efficiency of O-RU.</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>New Measurement andNew Reportingrequired in O-RAN.WG5.MP</td></tr><tr><td rowspan=1 colspan=1>01, R1</td><td rowspan=1 colspan=1>E2 Node (O-CU) / sMO/rApp</td><td rowspan=1 colspan=1>Number of active UEs in NG-RAN (Number of RRC_CONECTED UEs)per cell</td><td rowspan=1 colspan=1>Integer</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](Sec. 5.1.1.23, A.7,A.60)</td></tr></table>

Input Decision Making / AI/ML Inference:

Table 6.2.2.3-3: Input Decision Making / AI/ML Inference   

<table><tr><td rowspan=1 colspan=6>Input Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source / Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod</td><td rowspan=1 colspan=1>Existing / NewDefinitions</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>E2 Node (O-CU) / Near-RTRIC</td><td rowspan=1 colspan=1>DL PDCP SDU Data Volume per interface (Data Volume in DLdelivered from O-CU-UP to O-DU, perPLMN, per QoS level, per slice, per Interface (F1-U, Xn-U, X2-U))</td><td rowspan=1 colspan=1>Mbit</td><td rowspan=1 colspan=1>per N x100ms</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.3.6.2.3)</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>E2 Node (O-CU) / Near-RTRIC</td><td rowspan=1 colspan=1>UL PDCP SDU Data Volume perinterface (Data Volume in ULdelivered to O-CU-UP from O-DU, perPLMN, per QoS level, per slice, per Interface (F1-U, Xn-U, X2-U))</td><td rowspan=1 colspan=1>Mbit</td><td rowspan=1 colspan=1>per N x100ms</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.3.6.2.4)</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>E2 Node (O-CU) / Near-RTRIC</td><td rowspan=1 colspan=1>Number of active UEs in NG-RAN (Number of RRC_CONECTED UEs)per cell</td><td rowspan=1 colspan=1>Integer</td><td rowspan=1 colspan=1>per N x100ms</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](Sec. 5.1.1.23, A.7,A.60)</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>E2 Node (O-DU) / Near-RTRIC</td><td rowspan=1 colspan=1>PRACH correlation power for everyreceived PRACH corresponding toeach active SSB Beam Index</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>per N x100ms</td><td rowspan=1 colspan=1>New Measurement andNew Reporting: Themeasurement at O-DUmay be delivered</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>E2 Node (O-CU) / Near-RTRIC</td><td rowspan=1 colspan=1>RSRQ measurement per SSB per cell</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>per Nx100ms</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.31)</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>E2 Node (O-CU) / Near-RTRIC</td><td rowspan=1 colspan=1>RSRP measurement per SSB per cell</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>per N x100ms</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.22)</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>E2 Node (O-CU) / Near-RTRIC</td><td rowspan=1 colspan=1>SINR measurement per SSB per cell</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>per N x100ms</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.32)</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>E2 Node (O-CU) / Near-RTRIC</td><td rowspan=1 colspan=1>Energy consumption</td><td rowspan=1 colspan=1>kWh</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.19.3)</td></tr><tr><td rowspan=1 colspan=1>O-FH (M-Plane)orO-FH (M-Plane), E2</td><td rowspan=1 colspan=1>O-RU / O-DUorO-RU / O-DU /Near-RT RIC</td><td rowspan=1 colspan=1>Power consumed by O-RU or itshardware components</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>Measurement:3GPP TS 28.552 [12](C1. 5.1.1.19.2)Reporting:O-RAN.WG4.MP(Sec. B.1, B.5)</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>E2 Node (O-DU) / Near-RTRIC</td><td rowspan=1 colspan=1>Over the air Transmit power by O-RUNote: This measurement is required tocalculate energy efficiency of O-RU.</td><td rowspan=1 colspan=1>W</td><td rowspan=1 colspan=1>(non-realtime fortraining)</td><td rowspan=1 colspan=1>New Measurement andNew Reportingrequired in O-RAN.WG5.MP</td></tr></table>

# 6.2.2.3.3 Detailed Output Requirements

Output Decision Making / AI/ML Inference:

Table 6.2.2.3-4: Output Decision Making / AI/ML Inference   

<table><tr><td rowspan=1 colspan=6>Output Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source / Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod</td><td rowspan=1 colspan=1>Existing / NewDefinitions</td></tr><tr><td rowspan=3 colspan=1>O-FH (M-Plane)</td><td rowspan=3 colspan=1>O-DU / O-RU</td><td rowspan=1 colspan=1>Candidate O-RU&#x27;s appropriate Arrayselection</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>&gt; min</td><td rowspan=1 colspan=1>O-RAN.WG4.MPo-ran-uplane-conf.yang</td></tr><tr><td rowspan=1 colspan=1>Maximum number of Max SU/MUMIMO spatial streams or data layers</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>&gt; min</td><td rowspan=1 colspan=1>New Definition requiredin O-RAN.WG4.MP</td></tr><tr><td rowspan=1 colspan=1>Recommended O-RU AntennaTransmit power</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>&gt; min</td><td rowspan=1 colspan=1>O-RAN.WG4.MPurn:o-ran:uplane-confModulegain</td></tr><tr><td rowspan=4 colspan=1>E2</td><td rowspan=4 colspan=1>Near-RT RIC /O-DU</td><td rowspan=1 colspan=1>Candidate O-RU&#x27;s appropriate Arrayselection</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>&gt; min</td><td rowspan=1 colspan=1>New Definition required in WG2 R1 and O-RAN.WG5.O-DU-01</td></tr><tr><td rowspan=1 colspan=1>Maximum number of Max SU/MUMIMO spatial streams or data layers</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>&gt; min</td><td rowspan=1 colspan=1>New Definition requiredin O-RAN.WG4.MP</td></tr><tr><td rowspan=1 colspan=1>Inferred O-RU SS Burst Set (SS BlockNumber and SS Burst Periodicity) andCSI-RS TRS Configuration</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>Initialization</td><td rowspan=1 colspan=1>3GPP TS 38.331 [16]IE:ServingCellConfigCommon</td></tr><tr><td rowspan=1 colspan=1>Recommended O-RU AntennaTransmit power</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>&gt;min</td><td rowspan=1 colspan=1>O-RAN.WG4.MPurn:o-ran:uplane-confModulegain</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>E2 Node (O-DU) / Near-RTRIC</td><td rowspan=1 colspan=1>Confirmation (Success/Failure)</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>eventtriggered</td><td rowspan=1 colspan=1>New</td></tr></table>

# 6.3 Impact Analysis on O-RAN Work Groups

This is an initial impact analysis as part of the WG1 UCTG Network Energy Saving work on RF Channel Reconfiguration use case. The intention is to estimate the expected standardization effort within the O-RAN work groups. It is up to the WGs to decide how RF Channel Reconfiguration functionality should be specified in specifications of each WG.

<table><tr><td rowspan=1 colspan=1>#</td><td rowspan=1 colspan=1>WGs/FGs</td><td rowspan=1 colspan=1>Spec. No</td><td rowspan=1 colspan=1>Objective description</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>WG1 (Usecase)</td><td rowspan=1 colspan=1>O-RAN.WG1.NES-USE-CASES-TRO-RAN.WG1.Use-Cases-Detailed-Specification</td><td rowspan=1 colspan=1>Update WG1 NES use case analysis report and use-case detailed specification with RF ChannelReconfiguration use case. No impact to existingarchitecture</td></tr><tr><td rowspan=4 colspan=1>2</td><td rowspan=4 colspan=1>WG2(Non-RTRIC,A1,R1)d</td><td rowspan=1 colspan=1>O-RAN.WG2.R1GAPO-RAN.WG2.R1UCRO-RAN.WG2.R1TD (TBD)</td><td rowspan=1 colspan=1>Updates to R1 services and procedures for RFChannel Reconfiguration use case</td></tr><tr><td rowspan=1 colspan=1>O-RAN.WG2.Non-RT-RIC-ARCH</td><td rowspan=1 colspan=1>Reviewing procedures to implement RF ChannelReconfiguration use cases and generatecorresponding A1 policies/updates of O1 and O2-related services via R1 interface, if any.</td></tr><tr><td rowspan=1 colspan=1>O-RAN.WG2.Use-Case-Requirements</td><td rowspan=1 colspan=1>Specifying RF Channel Reconfiguration use caseand its requirements in WG2 UCR specification</td></tr><tr><td rowspan=1 colspan=1>O-RAN.WG2.A1GAPO-RAN.WG2.A1TD</td><td rowspan=1 colspan=1>Reviewing requirement for policy driven implementation 2nd deployment option of RFChannel Reconfiguration use case captured indocument.</td></tr><tr><td rowspan=6 colspan=1>3</td><td rowspan=6 colspan=1>WG3(Near-RTRIC, E2)</td><td rowspan=1 colspan=1>O-RAN.WG3.UCR</td><td rowspan=1 colspan=1>Specifying RF Channel Reconfiguration use caseand its requirements in WG3 UCR specification</td></tr><tr><td rowspan=1 colspan=1>O-RAN.WG3.RICARCH</td><td rowspan=1 colspan=1>No impact identified</td></tr><tr><td rowspan=1 colspan=1>O-RAN.WG3.E2GAP</td><td rowspan=1 colspan=1>No impact identified</td></tr><tr><td rowspan=1 colspan=1>O-RAN.WG3.E2AP</td><td rowspan=1 colspan=1>No impact identified</td></tr><tr><td rowspan=1 colspan=1>O-RAN.WG3.E2SM-RC orNEW: O-RAN.WG3.E2SM-CC</td><td rowspan=1 colspan=1>Identify and specify RAN E2 actions necessary forRF Channel Reconfiguration use case speciallymodifying mMIMO layer, Power, Tx/Rx Arrayselections, number of SsB Beams through E2 Nodetowards O-RU.</td></tr><tr><td rowspan=1 colspan=1>O-RAN.WG3.E2SM-KPM</td><td rowspan=1 colspan=1>Identify and specify RAN E2 measurement requiredanalysis of ES and EC for RF ChannelReconfiguration optimization through Near-RT RIC</td></tr><tr><td rowspan=2 colspan=1>4</td><td rowspan=2 colspan=1>WG4(O-FH)Impact</td><td rowspan=1 colspan=1>O-RAN.WG4.MP</td><td rowspan=1 colspan=1>Identify the relevant impacts on M-Plane for bothHierarchical and hybrid model to accommodatemanagement features requirements towards O-RU.Define O-RU Energy efficiency KPIs and counters.</td></tr><tr><td rowspan=1 colspan=1>O-RAN-WG4.CUS</td><td rowspan=1 colspan=1>Identify the relevant impacts on CUS-Plane and datamodel to support various Tx/Rx Array selections.</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>WG5(01)Impact</td><td rowspan=1 colspan=1>O-RAN.WG5.O-DU-01O-RAN.WG5.O-CU-01O-RAN.WG5.MP</td><td rowspan=1 colspan=1>Identify specific O-DU operational and data modelaspects of the feature content including the interfacebetween SMO and -O-DU, and the one betweenSMO and O-CU. Make appropriate changes to theO-DU data model and other WG5 specifications asneeded.</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>WG7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>WG7 needs to provide reference architecture of O-RU which supports Tx/Rx Array selection.Study energy savings gains from Tx/Rx arrayselection including limiting maximum number oflayers.</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>WG10</td><td rowspan=1 colspan=1>O-RAN.WG10.O1-InterfaceO-RAN.WG10.OAM-ArchitectureO-RAN.WG10.Information Model andData Models</td><td rowspan=1 colspan=1>Identify the relevant impacts on O1 interface tosupport RF Channel Reconfiguration use case andIM/DM to capture requirements for use cases.</td></tr></table>

# 6.4 Relation and Impact on 3GPP Specifications

3GPP RAN does a Rel.18 study on network energy savings for NR (i.e. FS_Netw_Energy_NR, see Sec. 5.4.2 for details). Within this study 3GPP RAN WGs consider related techniques such as RU Tx/Rx array selection, modification of number of SSB beams, adaptation of RU transmit power etc.

# 6.5 Gain Analysis

The potential of energy savings from RF Channel Reconfiguration is dependent upon several factors such as network deployment, traffic pattern/load, user distribution, antenna type and specific O-RU architecture etc. Computational analysis results for two example scenarios, one for 4T4R O-RU and one for 64T64R O-RU, are provided below. The calculations are based on the load profile and the power consumption categorization of O-RU functional blocks as outlined in Annex B.

Energy savings gain from RF Channel Reconfiguration would be equivalent to power consumption of the ORU hardware components that can be shut down or put into energy savings mode when the number of active antennas is reduced. As illustrated in Figure 6.5-1, energy savings gain would mostly be derived from partial shutdown of the RF Processing Unit and Digital Processing Unit (depending on the antenna configuration), while other functional modules such as O-RAN Fronthaul Processing Unit, Power Supply Unit and some other components would still be fully or partially functioning, and the power consumptions would be more or less consistent irrespective of the number of active antennas.

![](images/9d8fe2cc8d766e599597167f0913d048ea4b6c014642437f6dea2b66d8248835.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.5-1: Energy savings for RF Channels

# 6.5.1 RF Channel Reconfiguration ES Gain Analysis for 4T4R O-RU

When the traffic load is low, a 4T4R O-RU might be scaled down to 2T2R such that some part of the RF components in the O-RU might be switched off to save energy. When scaling down from 4T4R to 2T2R, RF Processing Unit for the two RF channels to be switched off might be shut down as illustrated in Figure 6.5.1- 1.

![](images/500bee664580f52072dc00357c9e7981e90d3d1ad952379414dc603381a4b57b.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.5.1-1: O-RU power saving for RF Channel Reconfiguration

The energy saving gain from reducing the number of RF channels from 4T4R to 2T2R is analyzed based on the system parameters in Table 6.5.1-1 and the example O-RU power profile considering power consumption from operational experience provided in Table 6.5.1-2.

Table 6.5.1-1: O-RU Configuration for ES gain analysis   

<table><tr><td rowspan=1 colspan=1>No. of antennas</td><td rowspan=1 colspan=1>4T4R</td></tr><tr><td rowspan=1 colspan=1>No. of layers</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>Bandwidth</td><td rowspan=1 colspan=1>100 MHz</td></tr><tr><td rowspan=1 colspan=1>Carrier frequency</td><td rowspan=1 colspan=1>3.5 GHz</td></tr><tr><td rowspan=1 colspan=1>Tx power per array element</td><td rowspan=1 colspan=1>30W</td></tr><tr><td rowspan=1 colspan=1>Technology</td><td rowspan=1 colspan=1>5G NR</td></tr></table>

Table 6.5.1-2: Example power profile for 4T4R O-RU   

<table><tr><td rowspan=1 colspan=1>Operating Load(Traffic)</td><td rowspan=1 colspan=1>Configuration</td><td rowspan=1 colspan=1>Total O-RU (W)</td><td rowspan=1 colspan=1>ORANFronthaulProcessingUnit (W)</td><td rowspan=1 colspan=1>DigitalProcessingUnit (W)</td><td rowspan=1 colspan=1>RFProcessingUnit (W)</td><td rowspan=1 colspan=1>Power Unit&amp; othercomponents(W)</td></tr><tr><td rowspan=1 colspan=1>Busy hour Load</td><td rowspan=1 colspan=1>4T4R</td><td rowspan=1 colspan=1>550</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>495</td><td rowspan=1 colspan=1>20</td></tr><tr><td rowspan=1 colspan=1>Low load</td><td rowspan=1 colspan=1>4T4R</td><td rowspan=1 colspan=1>200</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>145</td><td rowspan=1 colspan=1>20</td></tr><tr><td rowspan=1 colspan=1>Low load</td><td rowspan=1 colspan=1>2T2RRF ChannelReconfigurationES Mode</td><td rowspan=1 colspan=1>120</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>75</td><td rowspan=1 colspan=1>17</td></tr><tr><td rowspan=1 colspan=1>Maximum energysaving gain</td><td rowspan=1 colspan=1>2T2R vs. 4T4R(low load)</td><td rowspan=1 colspan=1>80</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>70</td><td rowspan=1 colspan=1>3</td></tr></table>

Compared to the low load scenario, a maximum energy savings of up to $8 0 \mathrm { W }$ per O-RU can be achieved. Achievable energy savings might be lower and might vary in practice. Besides an impact on receive signal quality and spectral efficiency, also coverage and beam characteristics will be affected. A lower spectral efficiency may for instance increase overall transmission time of the active UEs when transmitting a packet.

An example calculation for yearly energy saving potential considering a shutdown of 10000 O-Rus during 3 hours per day is provided in Table 6.5.1-3.

Table 6.5.1-3: Power saving calculation example for 4T4R O-RU   

<table><tr><td rowspan=1 colspan=1>Factor</td><td rowspan=1 colspan=1>Value</td></tr><tr><td rowspan=1 colspan=1>RU power savings during RF channel switch off(low load) [W]</td><td rowspan=1 colspan=1>80</td></tr><tr><td rowspan=1 colspan=1>Number of hours of switch off per day (50% of low load period)</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>Number of O-RUs</td><td rowspan=1 colspan=1>10000</td></tr><tr><td rowspan=1 colspan=1>Yearly energy saving [MWh]</td><td rowspan=1 colspan=1>876</td></tr></table>

# 6.5.2 RF Channel Reconfiguration ES Gain Analysis for 64T64R O-RU

The energy saving gain from RF Channel Reconfiguration of a 64T64R O-RU to 32T32R is analyzed based on the system parameters in Table 6.5.2-1 and the example O-RU power profile considering power consumption from operational experience provided in Table 6.5.2-2.

Table 6.5.2-1: O-RU Configuration for ES gain analysis   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Normal Mode</td><td rowspan=1 colspan=1>RF Channel Reconfiguration ES</td></tr><tr><td rowspan=1 colspan=1>Configuration</td><td rowspan=1 colspan=1>64T64R</td><td rowspan=1 colspan=1>32T32R</td></tr><tr><td rowspan=1 colspan=1>No. of layers</td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>8</td></tr><tr><td rowspan=1 colspan=1>Bandwidth</td><td rowspan=1 colspan=1>100MHz</td><td rowspan=1 colspan=1>100MHz</td></tr><tr><td rowspan=1 colspan=1>Carrier frequency</td><td rowspan=1 colspan=1>3.5 GHz</td><td rowspan=1 colspan=1>3.5 GHz</td></tr><tr><td rowspan=1 colspan=1>Tx power per array element</td><td rowspan=1 colspan=1>3W</td><td rowspan=1 colspan=1>3W</td></tr></table>

Table 6.5.2-2: Example power profile for 64T64R O-RU   

<table><tr><td rowspan=1 colspan=1>OperatingLoad(Traffic)</td><td rowspan=1 colspan=1>O-RU RFChannelConfiguration</td><td rowspan=1 colspan=1>Total O-RUPowerConsumption(W)</td><td rowspan=1 colspan=1>ORANFronthaulProcessingUnit (W)</td><td rowspan=1 colspan=1>DigitalProcessingUnit (W)</td><td rowspan=1 colspan=1>RFProcessingUnit (W)</td><td rowspan=1 colspan=1>Power Supply &amp;othercomponents (W)</td></tr><tr><td rowspan=1 colspan=1>Busy hourload</td><td rowspan=1 colspan=1>64T64R</td><td rowspan=1 colspan=1>1120</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>200</td><td rowspan=1 colspan=1>800</td><td rowspan=1 colspan=1>70</td></tr><tr><td rowspan=1 colspan=1>Low load</td><td rowspan=1 colspan=1>64T64R</td><td rowspan=1 colspan=1>520</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>200</td><td rowspan=1 colspan=1>200</td><td rowspan=1 colspan=1>70</td></tr><tr><td rowspan=1 colspan=1>Low load</td><td rowspan=1 colspan=1>32T32RRF ChannelReconfigurationES Mode</td><td rowspan=1 colspan=1>290</td><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>55</td></tr><tr><td rowspan=1 colspan=1>Maximumenergysaving gain</td><td rowspan=1 colspan=1>64T64R vs.32T32R(low load)</td><td rowspan=1 colspan=1>230</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>15</td></tr></table>

Compared to the low load scenario, a maximum energy saving gain of up to $2 3 0 \mathrm { W }$ per O-RU can be achieved. As stated before, the achievable energy savings might be lower and might vary in practice.

An example calculation for yearly energy saving potential considering a shutdown of 10000 O-RUs during 3 hours per day is provided in Table 6.5.2-3.

Table 6.5.2-3: Power saving calculation example for 64T64R O-RU   

<table><tr><td rowspan=1 colspan=1>Factor</td><td rowspan=1 colspan=1>Value</td></tr><tr><td rowspan=1 colspan=1>RU power savings during RF channel switch off(low load) [W]</td><td rowspan=1 colspan=1>230</td></tr><tr><td rowspan=1 colspan=1>Number of hours of switch off per day (50% of low load period)</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>Number of O-RUs</td><td rowspan=1 colspan=1>10000</td></tr><tr><td rowspan=1 colspan=1>Yearly energy saving [MWh]</td><td rowspan=1 colspan=1>2519</td></tr></table>

# 6.6 Feasibility Analysis

# 6.6.1 Continuous operation during RF Channel Reconfiguration

Changing configuration of O-RU such as shutting down 32 TRX of the 64TRX for the purpose of energy savings may impact the existing users if it requires full or partial reset of O-RU, hence care should be exercised on how the reconfiguration of antenna array is performed.

# 6.6.2 Impact on Coverage

The coverage during TRX switch should be maintained as much as possible. A reduction of transceiver chains may impact the number of transmitted SSB beams, the beam shapes, as well as the overall transmit power, affecting the various downlink physical channels. A limited coverage might result in reduced user throughput, radio link failures, beam failures, and call drops.

# 6.6.3 Impact and Relation to UE specific Base Station Algorithms

A TRX switch might impact the cell coverage and the beam characteristics. This sudden change in radio channel characteristics might affect UE specific base station algorithms (e.g., inner and outer loop link adaptation, power control, beam selection, adaptive MIMO, channel quality reporting etc.) and may result in a transitory phase until transmission can be continued or is stabilized.

It is up to the proprietary scheduler algorithm to handle such events most efficiently. Scheduling (e.g. user selection, resource allocation), adaptive MIMO (e.g. MIMO mode, spatial streams and layers) and link adaptation (e.g. Coding/Modulation Scheme, transmit power) will be adjusted instantaneously every scheduling instance and transmission time interval by the base station without time constrained external control.

# 6.6.4 Limited O-RU / O-DU Capabilities

The capabilities of the O-RU in terms of configurable antenna arrays, transition times, as well as the capabilities of the O-DU scheduling respective antenna arrays with the various MIMO transmission modes may be limited. Hence, respective capabilities are required to be known. The capabilities between the different array configurations may differ significantly in terms of supported SU/MU MIMO modes as well as in terms of supported MIMO layers, streams etc.

# Advanced Sleep Mode Selection

7.1 Problem Statement, Solution and Value Proposition

This Use Case describes a method to achieve intelligent energy saving by optimizing the sleep mode via RIC-based guidance.

# Background

O-RU and E2 Nodes (O-CU, O-DU) may implement various Sleep Modes (SMs). The SMs are enabled by Non-RT RIC/SMO and/or Near-RT RIC. When enabled, the E2 Nodes select among the SMs considering their capabilities, the actual traffic situation, and the network conditions. Different SM operate at different time scales (e.g., symbol, slot, frame).

# Problem Statement

In a single vendor network where components are not disaggregated, the O-RU's capabilities are well-known within the E2 Node, allowing for autonomous execution of sleep modes. However, implementing sleep modes in O-RAN requires the O-DU and O-CU to understand the sleep mode capabilities of the O-RU, including the number and depth of sleep modes. Also, Near/Non-Real-Time RIC need to be aware of the ODU and O-CU capabilities to drive policies related to sleep modes. For optimization, O-RU and O-DU need to report energy efficiency related measurements and KPIs from which the power saving can be observed. To achieve this, effective communication and coordination between all components is necessary.

# Solution

In this solution the O-RU will expose its SM capabilities to the O-DU in the initial configuration phase. Next, the O-DU will expose a set of commonly supported SMs to the SMO (over O1) and Non-RT RIC (via SMO and R1) and/or the Near-RT RIC (over E2) which is available for utilization during operation. Information exposed towards the Non-RT and/or Near-RT RIC will include a unique identifier of each SM, and additional operational parameters, e.g., minimum duration of activation, transition times between SMs, whether to be applied on UL/DL, etc.

Moreover, the Non-RT RIC and/or Near-RT RIC will collect for the different SMs data related to network load and performance, cell configuration, and energy/power consumption.

Based on the above two sets of information the Non-RT RIC and/or Near-RT RIC train an ML model, which will infer optimized SM utilization range (i.e., a set of SMs the O-DU may dynamically select from at a given or pre-defined time), which is then transmitted to the O-DU as a guidance. Based on the optimized (allowed) SM utilization range, O-DU will select specific SMs.

Depending on the SMs, O-RU and O-DU may apply such SM selection internally or O-RU may apply a SM based on O-DU request. For instance, O-RU may (or may not) apply a micro sleep internally, while O-DU may (or may not) internally adjust its scheduling strategy to maximize possible O-RU micro sleep periods considering O RU SM capabilities. Energy saving is thus obtained during regular operation when O-DU schedules data in a more optimized way. O-DU may for example prioritize time-domain scheduling over frequency domain scheduling or may compress data transmission to increase the number of symbols or slots without data. O-DU cannot enforce the O-RU to apply its micro sleep due to the fast internal operation and Near-RT RIC may not be able to enforce O-DU to adjust its internal scheduling strategy. The energy saving gains can be observed by monitoring respective Energy Efficiency KPIs.

In the alternative on request operation, O-DU may for instance configure the O-RU to switch off a certain part of the O-RU to support a deep sleep operation considering the timing constraints as communicated during the capability exchange. Energy saving is thus obtained when O-RU applies a new configuration as requested by O-DU.

# Value Proposition

Firstly, the Non-RT RIC and/or Near-RT RIC based AI/ML algorithm may extend the time period or increase the granularity during which the E2 Nodes are allowed to select from their implemented SMs.

Secondly, this solution allows for an optimized SMs selection in a multi-vendor O-RU/O-DU deployment, by the O-RU/O-DU exposing the required information as part of their SM capabilities.

# 7.2 Architecture/Deployment Options

# 7.2.1 Option 1: Training and Inference in Non-RT RIC

In this deployment option, the Non-RT RIC retrieves the E2 Node SM capabilities over O1 and R1 via SMO, collects the necessary data from the E2 Nodes and trains an ML model, which is then deployed in the rApp. Inference of the optimized SM utilization range is provided as guidance by the rApp. Additionally, external parties (such as prediction rApps or external application servers) may provide additional information for optimization.

# 7.2.1.1 Description and UML Diagram

Table .2.1.1-1: Advanced Sleep Mode Selection: Training and Inference in Non-RT RIC   

<table><tr><td rowspan=1 colspan=1>Use Case Stage</td><td rowspan=1 colspan=1>Evolution / Specification</td><td rowspan=1 colspan=1>&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td rowspan=1 colspan=1>Goal</td><td rowspan=1 colspan=1>Provide optimized SM utilization range as guidance to the O-DU and allowfor optimized SM selection in O-DU / O-RU.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Actors and Roles</td><td rowspan=1 colspan=1>SMO/Non-RT RIC: Retrieval of E2 Node SM capabilities.SMO/Non-RT RIC: Data collection for ML model training and MLmodel deployment.Non-RT RIC: Network data collection and analysis, and inference ofSM utilization range guidance provided to O-DU.O-DU: Expose common O-DU/O-RU SM capabilities over O1.O-RU: Expose SM related capabilities to O-DU.(Optional) Additional parties: Providing additional data for optimization.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Assumptions</td><td rowspan=1 colspan=1>O-RU and O-DU expose the necessary information about theiravailable SMs capabilities.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Pre- conditions</td><td rowspan=1 colspan=1>All relevant functions and components are instantiated and available.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Begins when</td><td rowspan=1 colspan=1>The operator has enabled or has set targets for SM utilization guidancerApp.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 1.1, 1.2 (M)</td><td rowspan=1 colspan=1>O-RU transmits to O-DU its SM capabilities. O-DU decides on a commonset of O-DU/O-RU SM capabilities to utilize during operation.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 1.3 (M)</td><td rowspan=1 colspan=1>O-DU transmits information about the available O-DU/O-RU SM capabilitiesto Non-RT RIC/SMO, including minimal operational information.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 2.1, 2.2 (M), 2.3(0)Step 2.4, 2.5 (M), 2.6(0)Step 2.7 (M)</td><td rowspan=1 colspan=1>Data collection request from SMO to E2 Nodes (M) and external entities (O)for training and inference.Data collection from E2 Nodes (M) and external entities (O) for training inSMO/Non-RT RIC.Non-RT RIC retrieves data for training and inference.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 3.1, 3.2, 3.3 (M)</td><td rowspan=1 colspan=1>Based on continuous/periodically collected data, Non-RT RIC trains theAl/ML model and deploys it. Non-RT RIC performs inference using theAI/ML model.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 4.1 (M)Step 4.2, 4.3 (0),Step 4.4, 4.5, 4.6 (0)</td><td rowspan=1 colspan=1>Non-RT RIC provides SM utilization guidance via SMO and O1 to O-DU.O-DU considers Non-RT RIC&#x27;s SM utilization guidance in its updatedscheduling strategy and O-RU applies SM selection internallyBased on Non-RT RIC&#x27;s SM utilization guidance, O-DU alternatively selectsa SM, O-DU requests a new SM configuration by O-RU over O-FH and O-RU applies the new SM configuration.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Ends when</td><td rowspan=1 colspan=1>Operator disables or changes targets for SM utilization guidance rApp.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Exceptions</td><td rowspan=1 colspan=1>None identified.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Post-conditions</td><td rowspan=1 colspan=1>Non-RT RIC continues to monitor the energy consumption and efficiencyand the RAN performance by collecting and monitoring the relevant dataover O1.</td><td rowspan=1 colspan=1></td></tr></table>

@startuml   
skinparam defaultFontSize 12   
autonumber   
Box "SMO" #gold Participant “Collection & Control” as COLL Participant “Non-RT RIC” as NON   
End box   
Box "O-RAN" #lightpink Participant "O-CU" as OCU Participant "O-DU" as ODU   
End box   
Box "O-RU" #turquoise Participant “O-RU” as ORU   
End box   
Box "EXT" #lightcyan Participant “EXT” as EXT   
End box   
$= =$ Initialization $= =$   
autonumber 1.1 ORU $- >$ ODU : <<O-FH>> SM capabilities ODU $- >$ ODU : SM capability decision ODU $- >$ COLL : $< < 0 1 > >$ SM capability information exposure ODU $- >$ NON : $< < \mathrm { E } 2 > >$ SM capability information exposure   
$= =$ Data Collection $= =$   
autonumber 2.1   
Group Data for training and for inference   
Loop COLL $- >$ OCU : $< < 0 1 > >$ Data collection request COLL $- >$ ODU : $< < 0 1 > >$ Data collection request COLL $- >$ EXT : Data collection request OCU $- >$ COLL : $< < 0 1 > >$ Data retrieval ODU $- >$ COLL : $< < 0 1 > >$ Data retrieval EXT $- >$ COLL : Data retrieval COLL $- >$ NON : Data retrieval   
End loop   
End group   
$= =$ AI/ML Flow $= =$   
autonumber 3.1 NON $- >$ NON : AI/ML model training NON $- >$ NON : AI/ML model deployment   
Loop NON $- >$ NON : AI/ML model inference   
End Loop   
$= =$ SM Guidance (Loop) $= =$   
autonumber 4.1 NON $- >$ COLL: Guidance to utilize SM COLL $- >$ ODU: $< < 0 1 > >$ Guidance to utilize SM   
group Configuration Update group alt1 ODU $- >$ ODU: Updated scheduling strategy ORU $- >$ ORU: Internal SM selection end group alt2 ODU $- >$ ODU: SM selection ODU $- >$ ORU: <<O-FH>> Request new \nSM configuration ORU $- >$ ORU: Apply new SM configuration end   
end

![](images/a8a0d1ffbdb8f15991b9f2ecbaee9c23682ea85dc811356ed373c696c181f4c6.jpg)

> **Image Summary:** (Summary not available)
  
Figure .2.1.1-1: Flow diagram for SM Selection, ML model training in the Non-RT RIC

# 7.2.1.2 O-RAN Entity Roles

1) SMO (including Non-RT RIC)

a) Receive common SM capability information and additional operational parameters from O-DU.   
b) Subscribe to and retrieve necessary performance indicators (incl. Energy Efficiency KPIs), measurement reports, UE context information, RAN configurations, and SM usage data from E2 Nodes via the O1 interface for the purpose of AI/ML model training, inference, and performance monitoring.   
c) Optionally, i) collect enrichment information from Application servers and associate enrichment information with collected measurements and configurations, ii) collect prediction or optimization related information from other rApps.   
d) Perform AI/ML model training and deployment.   
e) Send SM utilization guidance for Sleep Mode optimization to E2 Nodes over O1.

2) E2 Nodes (O-DU in disaggregated architecture)

a) Support retrieving the O-RU SM capabilities and additional operational parameters from O-RU via O-FH.   
b) Support reporting the common O-DU/O-RU SM capabilities and additional operational parameters to SMO over O1.   
c) Support reporting of necessary performance indicators (incl. Energy Efficiency KPIs), measurement reports, UE context information, RAN configurations, and SM usage data with required granularity to SMO via the O1 interface.   
d) Receive SM utilization guidance from the SMO via the O1interface.   
e) Adjust scheduling strategy (to allow O-RU to internally update its used SMs configuration) or alternatively perform SM selection based on SM utilization guidance received from the SMO.   
f) Optionally, request O-RU over O-FH to update its used SM configuration (e.g., switch off a certain O-RU functionality).

# 3) O-RU

a) Support reporting the O-RU SMs capabilities and additional operational parameters to O-DU via OFH.   
b) Internally apply SM selection or alternatively receive over O-FH and apply O-DUs request for updated SM configuration.

# 7.2.1.3 Void

# 7.2.2 Option 2: Training in Non-RT RIC and Inference in Near-RT RIC

In this deployment option, the Non-RT RIC retrieves the E2 Node SM capabilities over O1 and R1 via SMO, collects the necessary data from the E2 Nodes and trains an ML model, which is then deployed in the rApp. Inference of the optimized SM utilization range is provided as guidance by the rApp. Additionally, external parties (such as prediction rApps or external application servers) may provide additional information for optimization.

# 7.2.2.1 Description and UML Diagram

Table .2.2.1-1: Advanced Sleep Mode Selection: Training in Non-RT RIC and Inference in Near-RT RIC   

<table><tr><td>Use Case Stage</td><td>Evolution / Specification</td><td>&lt;&lt;Uses&gt;&gt; Related use</td></tr><tr><td>Goal</td><td>Provide optimized SM utilization range as guidance to the O-DU and allow for optimized SM selection in O-DU/O-RU.</td><td></td></tr><tr><td>Actors and Roles</td><td>SMO/Non-RT RIC: Retrieval of E2 Node SM capabilities. SMO/Non-RT RIC: Data collection for ML model training and ML model deployment. Near-RT RIC (xApp): Network data collection and analysis, and inference of SM utization range guidance provided to O-DU. O-DU: Expose common O-DU/O-RU SM capabilities over O1/E2. O-RU: Expose SM related capabilities to O-DU.</td><td></td></tr><tr><td>Assumptions</td><td>(Optional) Additional parties: Providing additional data for optimization. O-RU and O-DU expose the necessary information about their</td><td></td></tr><tr><td>Pre- conditions</td><td>available SMs capabilities. All relevant functions and components are instantiated and available.</td><td></td></tr><tr><td>Begins when</td><td>The operator has enabled or has set targets for SM utilization guidance</td><td></td></tr><tr><td></td><td>xApp. O-RU transmits to O-DU its SM capabilities. O-DU decides on a common</td><td></td></tr><tr><td>Step 1.1, 1.2 (M)</td><td>set of O-DU/O-RU SM capabilities to utilize during operation. O-DU transmits information about the available O-DU/O-RU SM capabilities</td><td></td></tr><tr><td>Step 1.3, 1.4 (M) Step 2.1, 2.2 (M), 2.3</td><td>to Non-RT RIC/SMO and Near-RT RIC, including minimal operational information. Data collection request from SMO to E2 Nodes (M) and external entities (O)</td><td></td></tr><tr><td>(0) Step 2.4, 2.5 (M), 2.6</td><td>for training. Data collection from E2 Nodes (M) and external entities (O) for training in</td><td rowspan="3"></td></tr><tr><td>(0) Step 2.7 (M)</td><td>SMO. Non-RT RIC retrieves data for training.</td></tr><tr><td>Step 2.8, 2.9 (M), 2.10 (0)</td><td>Data collection request from Near-RT RIC to E2 Nodes (M) and external entities (O) for inference.</td></tr><tr><td>Step 2.11, 2.12 (M), 2.13(0)</td><td>Data collection from E2 Nodes (M) and external entities (O) to Near-RT RIC for inference.</td><td rowspan="3"></td></tr><tr><td>Step 3.1, 3.2, 3.3 (M)</td><td>Based on continuous/periodically collected data, Non-RT RIC trains the AI/ML model and deploys it to Near-RT RIC via O1/O2. Near-RT RIC performs inference using the Al/ML model.</td></tr><tr><td>Step 4.1 (M) Step 4.2, 4.3 (0),</td><td>Near-RT RIC provides SM utilization guidance via E2 to O-DU. O-DU considers Near-RT RIC&#x27;s SM utilization guidance in its updated</td></tr><tr><td></td><td>scheduling strategy and O-RU applies SM selection internally.</td><td rowspan="2"></td></tr><tr><td>Step 4.4, 4.5, 4.6 (0)</td><td>Based on Near-RT RIC&#x27;s SM utilization guidance, O-DU alternatively selects a SM, O-DU requests a new SM configuration by O-RU over O-FH and O- RU applies the new SM configuration.</td></tr><tr><td></td><td>Operator disables or changes targets for SM utilization guidance xApp.</td><td></td></tr><tr><td>Ends when Exceptions</td><td>None identified.</td><td></td></tr><tr><td></td><td>Near-RT RIC/Non-RT RIC continues to monitor the energy consumption and</td><td></td></tr><tr><td>Post-conditions</td><td>efficiency and the RAN performance by collecting and monitoring the relevant data over E2/01.</td><td></td></tr></table>

@startuml   
skinparam defaultFontSize 12   
autonumber   
Box "SMO" #gold Participant “Collection & Control” as COLL Participant “Non-RT RIC” as NON   
End box   
Box "O-RAN" #lightpink Participant “Near-RT RIC” as NEAR Participant "O-CU" as OCU Participant "O-DU" as ODU   
End box   
Box "O-RU" #turquoise Participant “O-RU” as ORU   
End box   
Box "EXT" #lightcyan Participant “EXT” as EXT   
End box   
$= =$ Initialization $= =$   
autonumber 1.1 ORU $- >$ ODU : <<O-FH>> SM capabilities ODU $- >$ ODU : SM capability decision ODU $- >$ COLL : $< < 0 1 > >$ SM capability information exposure ODU $- >$ NEAR : $< < \mathrm { E } 2 > >$ SM capability information exposure   
$= =$ Data Collection $= =$   
autonumber 2.1   
Group Data for training COLL $- >$ OCU : <<O1>> Data collection request COLL $- >$ ODU : $< < 0 1 > >$ Data collection request COLL $- >$ EXT : Data collection request OCU $- >$ COLL : $< < 0 1 > >$ Data retrieval ODU -> COLL : $< < 0 1 > >$ Data retrieval EXT $- >$ COLL : Data retrieval COLL $- >$ NON : Data retrieval   
End group   
Group Data for inference NEAR $- >$ OCU : $< < \mathrm { E } 2 > >$ Data collection request NEAR $- >$ ODU : $< < \mathrm { E } 2 > >$ Data collection request NEAR $- >$ EXT : Data collection request   
Loop OCU $- >$ NEAR : $< < \tt E 2 > >$ Data retrieval ODU $- >$ NEAR : $< < \mathrm { E } 2 > >$ Data retrieval EXT $- >$ NEAR : Data retrieval   
End Group   
End Loop   
$= =$ AI/ML Flow $= =$   
autonumber 3.1 NON $- >$ NON : AI/ML model training NON $- >$ NEAR : $< < 0 1$ /O2>> AI/ML model deployment   
Loop NEAR $- >$ NEAR: AI/ML model inference   
End Loop   
$= =$ SM Guidance (Loop) $= =$   
autonumber 4.1 NEAR $- >$ ODU: $< < \mathrm { E } 2 > >$ Guidance to utilize SM   
group Configuration Update group alt1 ODU $- >$ ODU: Updated scheduling strategy

ORU - $- >$ ORU: Internal SM selection end group alt2 ODU $- >$ ODU: SM selection ODU $- >$ ORU: <<O-FH $\mathrm { . > > }$ Request new \nSM configuration ORU $- >$ ORU: Apply new SM configuration end @enduml

![](images/ecd4818e1f351f8adc4e13a923ceaa4951c2457c89407527eb284523f928089e.jpg)

> **Image Summary:** (Summary not available)
  
Figure .2.2.1-1: Flow diagram for SM Selection in the Near-RT RIC, ML model training in the Non-RT RIC

# 7.2.2.2 O-RAN Entity Roles

1) SMO (including Non-RT RIC)

a) Receive common SM capability information and additional operational parameters from O-DU.   
b) Subscribe to and retrieve necessary performance indicators (incl. Energy Efficiency KPIs), measurement reports and RAN configurations from E2 Nodes via the O1 interface for the purpose of AI/ML model training and performance monitoring.   
c) Perform AI/ML model training and deployment.   
d) Optionally, i) collect enrichment information from Application servers and associate enrichment information with collected measurements and configurations, ii) collect prediction or optimization related information from other rApps.

# 2) Near-RT RIC (xApp)

a) Receive common SM capability information and additional operational parameters from O-DU.   
b) Subscribe to and retrieve necessary performance indicators (incl. Energy Efficiency KPIs), measurement reports, UE context information, RAN configurations, and SM usage data from E2 Nodes via the E2 interface for the purpose of AI/ML model inference, and performance monitoring.   
c) Optionally, i) collect enrichment information from Application servers and associate enrichment information with collected measurements and configurations, ii) collect prediction or optimization related information from other xApps (Near-RT RIC internally) or rApps.   
d) Send SM utilization guidance via a policy message for Sleep Mode optimization to E2 Nodes via the E2 interface.

3) E2 Nodes (O-DU in disaggregated architecture)

a) Support retrieving the O-RU SM capabilities and additional operational parameters from O-RU via O-FH.   
b) Support reporting the common O-DU/O-RU SM capabilities and additional operational parameters to Near-RT RIC over E2 and to SMO over O1.   
c) Support reporting of necessary performance indicators (incl. Energy Efficiency KPIs), measurement reports, UE context information, RAN configurations, and SM usage data with required granularity to Near-RT RIC via the E2 interface and SMO via the O1 interface.   
d) Receive SM utilization guidance via policy message from the Near-RT RIC via the E2 interface.   
e) Adjust scheduling strategy (to allow O-RU to internally update its used SMs configuration) or alternatively perform SM selection based on SM utilization guidance received from the Near-RT RIC.   
f) Optionally, request O-RU over O-FH to update its used SM configuration (e.g., switch off a certain O-RU functionality).

# 4) O-RU

a) Support reporting the O-RU SMs capabilities and additional operational parameters to O-DU via OFH.   
b) Internally apply SM selection or alternatively receive over O-FH and apply O-DUs request for updated SM configuration (e.g., switch off a certain O-RU functionality).

# 7.2.2.3 Void

# 7.3 Impact Analysis on O-RAN Work Groups

This is an initial impact analysis as part of the WG1 UCTG Network Energy Saving work on Advance Sleep Mode Selection use case. The intention is to estimate the expected standardization effort within the O-RAN working groups. It is up to the WGs to decide how Advance Sleep Mode Selection use case functionality should be specified in specifications of each WG.

<table><tr><td colspan="1" rowspan="1">#</td><td colspan="1" rowspan="1">WGs/FGs</td><td colspan="1" rowspan="1">Spec. No</td><td colspan="1" rowspan="1">Objective description</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">WG1 (Usecase)</td><td colspan="1" rowspan="1">O-RAN.WG1.NES-USE-CASES-TRO-RAN.WG1.Use-Cases-Detailed-Specification</td><td colspan="1" rowspan="1">Update WG1 NES use case analysis report and use-case detailed specification with Advance SleepMode Selection use case. No impact to existingarchitecture</td></tr><tr><td colspan="1" rowspan="4">2</td><td colspan="1" rowspan="4">WG2(Non-RTRIC, A1,R1)</td><td colspan="1" rowspan="1">O-RAN.WG2.R1GAPO-RAN.WG2.R1UCRO-RAN.WG2.R1TD (TBD)</td><td colspan="1" rowspan="1">Updates to R1 services and procedures for AdvancedSleep Mode Selection use case</td></tr><tr><td colspan="1" rowspan="1">O-RAN.WG2.Non-RT-RIC-ARCH</td><td colspan="1" rowspan="1">Reviewing procedures to implement Advanced Sleep Mode Selection use case and generate correspondingA1 policies/updates of O1 and O2-related servicesvia R1 interface, if any.</td></tr><tr><td colspan="1" rowspan="1">O-RAN.WG2.Use-Case-Requirements</td><td colspan="1" rowspan="1">Specifying Advanced Sleep Mode Selection use caseand its requirements in WG2 UCR specification</td></tr><tr><td colspan="1" rowspan="1">O-RAN.WG2.A1GAPO-RAN.WG2.A1TD</td><td colspan="1" rowspan="1">Reviewing requirement for policy drivenimplementation of Advance Sleep Mode Selection</td></tr><tr><td colspan="1" rowspan="6">3</td><td colspan="1" rowspan="6">WG3(Near-RTRIC, E2)</td><td colspan="1" rowspan="1">O-RAN.WG3.UCR</td><td colspan="1" rowspan="1">Specifying Advanced Sleep Mode Selection use caseand its requirements in WG3 UCR specification</td></tr><tr><td colspan="1" rowspan="1">O-RAN.WG3.RICARCH</td><td colspan="1" rowspan="1">No impact identified</td></tr><tr><td colspan="1" rowspan="1">O-RAN.WG3.E2GAP</td><td colspan="1" rowspan="1">No impact identified</td></tr><tr><td colspan="1" rowspan="1">O-RAN.WG3.E2AP</td><td colspan="1" rowspan="1">No impact identified</td></tr><tr><td colspan="1" rowspan="1">O-RAN.WG3.E2SM-RC orNEW: O-RAN.WG3.E2SM-CC</td><td colspan="1" rowspan="1">Identify and specify RAN E2 actions necessary for implementation of Advance Sleep Mode Selectionfrom E2 Node towards O-RU.</td></tr><tr><td colspan="1" rowspan="1">O-RAN.WG3.E2SM-KPM</td><td colspan="1" rowspan="1">Identify and specify RAN E2 measurement requiredanalysis of ES and EC for Advance Sleep ModeSelection through Near-RT RIC</td></tr><tr><td colspan="1" rowspan="2">4</td><td colspan="1" rowspan="2">WG4(O-FH)Impact</td><td colspan="1" rowspan="1">O-RAN.WG4.MP</td><td colspan="1" rowspan="1">Identify the relevant impacts on M-Plane for bothhierarchical and hybrid model to accommodatemanagement features requirements towards O-RU.Define O-RU Energy efficiency KPIs and counters.</td></tr><tr><td colspan="1" rowspan="1">O-RAN-WG4.CUS</td><td colspan="1" rowspan="1">Identify the relevant impacts on CUS-Plane and datamodel to support various Advance Sleep ModeSelection use case.</td></tr><tr><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">WG5(01)Impact</td><td colspan="1" rowspan="1">O-RAN.WG5.O-DU-O1O-RAN.WG5.O-CU-01O-RAN.WG5.MP</td><td colspan="1" rowspan="1">Identify specific O-DU operational and data modelaspects of the feature content including the interfacebetween SMO and O-DU, and the one between SMO and O-CU. Make appropriate changes to theO-DU data model and other WG5 specifications asneeded.</td></tr><tr><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="1">WG7</td><td colspan="1" rowspan="1">WG7 Energy Savings TR</td><td colspan="1" rowspan="1">WG7 needs to provide reference architecture of O-RU which supports Advance Sleep Mode Selectionuse case.</td></tr><tr><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">WG10</td><td colspan="1" rowspan="1">O-RAN.WG10.O1-InterfaceO-RAN.WG10.OAM-ArchitectureO-RAN.WG10.Information Model andData Models</td><td colspan="1" rowspan="1">Identify the relevant impacts on O1 interface tosupport Advanced Sleep Mode Selection use casesand IM/DM to capture requirements.</td></tr></table>

# 7.4 Relation and Impact on 3GPP Specifications

Within the 3GPP Rel.18 RAN WG1 led study item on network energy saving 3GPP agreed on three Power States for evaluation purpose Micro, Light and Deep Sleep as documented in TR 38.864 [19]. The states represent a simplified model for simulation and evaluation purpose only and have not been part of the normative work in Rel.18. The examples of Advanced Sleep Modes are shown in Annex D.

<table><tr><td rowspan=1 colspan=1>Reference</td><td rowspan=1 colspan=1>Release</td><td rowspan=1 colspan=1>Title</td><td rowspan=1 colspan=1>Documentation and impact onSpecifications</td></tr><tr><td rowspan=1 colspan=1>FS_Netw_Energy_NR</td><td rowspan=1 colspan=1>5G Rel.18</td><td rowspan=1 colspan=1>Study on networkenergy savings for NR</td><td rowspan=1 colspan=1>Results will be captured in 3GPP TR38.864 [19].</td></tr></table>

3GPP TSG RAN 98-e approved a new Rel.18 WID: Network energy savings for NR (RP-223540) which includes following objective.

2. Specify enhancement on cell DTX/DRX mechanism including the alignment of cell DTX/DRX and UE DRX in RRC_CONNECTED mode, and inter-node information exchange on cell DTX/DRX [RAN2, RAN1, RAN3]

• Note: No change for SSB transmission due to cell DTX/DRX.   
• Note: The impact to IDLE/INACTIVE UEs due to the above enhancement should be avoided.

While 3GPP standards concentrate on enhancing the co-ordination between UE and gNB for cell DTX/DRX operation, O-RAN Advanced Sleep Mode Selection focuses on co-ordinating O-RU and O-DU based on Non-RT/Near-RT RIC policy.

7.5 Void

# 7.6 Feasibility Analysis

# 7.6.1 Impact to Continuous Operation during Advance Sleep Modes

Advanced Sleep Modes that are limited to symbol level are not expected to have a significant impact on user performance. However, longer sleep modes that involve shutting down more components or reducing their activity for longer periods of time may impact user performance such as increased latency and/or reduced data transfer rates.

# 7.6.2 Impact to Coverage

If an O-RU transmission is suspended temporarily (e.g., some kind of deep sleep modes), UEs may be unable to connect to $\mathrm { g N B }$ due to missing synchronization, measurements and/or system information, hence the coverage in the area may be impacted. The impact might be mitigated by intelligent configuration and/or using multiple carriers.

# 7.6.3 Impact and Relation to Vendor Specific Scheduling Algorithms

O-RU and O-DU may implement their own sleep modes. However, adjustments may be needed to align with ES/EE policies from Non-RT/Near-RT RIC. Operators need to balance user/cell performance against energy savings, and E2 Nodes (O-DU/O-CU) may require additional functionality to implement these policies.

# 7.6.4 Limited O-RU/O-DU Capabilities

The O-RU and O-DU may have limitations in terms of implementing sleep modes capabilities. It is up to implementation how many Advanced Sleep Modes are supported in O-RU or O-DU. Furthermore, the generic solution should support the transmission of operational parameters from O-RU to O-DU, e.g., minimum duration of activation of SMs, transition times between sleep modes, whether to be applied on UL/DL, etc.

# 8

# O-Cloud Resource Energy Saving Mode

In O-RAN split option $7 . 2 \mathrm { x }$ major signal processing is performed by O-DU and O-CU. Hence, O-DU and OCU hardware components consume energy to maintain a certain level of system availability even in case of low or no traffic load on VNFs or CNFs. As more and more operators adopt virtualized or containerized architecture, there is a strong need to have solution(s) for energy saving in the O-Cloud. The O-Cloud Resource Energy Saving Mode use case should cover various components of the O-Cloud such as CPU/GPU, accelerators, NIC cards and other components at node level.

The aim of this use case is to enable energy savings in the O-Cloud by reducing the power consumption of various O-Cloud components without impairing the network performance. Given the network status, the OCloud components' power consumption can be optimized through actions such as adaptive shutdown of hardware, scaling out Network Functions, and optimization of CPU/FPGA power, memory usage, CPU frequency, etc. By using multi-dimensional data (e.g., traffic load data at E2 Nodes, load over O-Cloud in terms of compute/storage) the Non-RT RIC can configure changes towards the O-Cloud.

The time scale for the control of O-Cloud Resource Energy Saving Mode solutions is Non-Real Time.

# 8.1 Sub Use Case 1: O-Cloud Node Shutdown

8.1.1 Problem Statement, Solution and Value Proposition

This use case describes a method to perform O-Cloud Energy Saving by shutting down physical O-Cloud Node(s) in idle times through Non-RT RIC.

When O-Cloud Node is operating at low load, then the deployed Network Functions or its microservices can be relocated or shut down or blocked from starting on the node in order to free up the node. Moving VNFs or CNFs within O-Cloud and/or evacuating the O-Cloud Nodes are O-Cloud internal functionalities which might be triggered by the SMO.

Idle O-Cloud Nodes can be shut down to reduce energy consumption during low-load times. Non-RT RIC subscribes to O2 data via SMO, which, among others, includes configuration of O-Cloud Nodes (e.g., K8s cluster, resource pools, NF-pod-node associations). Non-RT RIC provides guidance to the SMO. The SMO monitors O-Cloud and E2 Node resources based on O1/O2 data and requests shut down (scale in) or add OCloud resources via O2ims (scale out) based on Non-RT RIC guidance. O-Cloud (IMS) will estimate if sufficient O-Cloud resources are remaining or are available to serve respective requests. After execution or rejection of respective requests O-Cloud (IMS) will communicate its actions via O2ims.

![](images/1066e2545707f1b0eb0b6277b15892d97e56bb5337f8a81a3633ffcee1fc9fa3.jpg)

> **Image Summary:** (Summary not available)
  
Figure 8.1.1-1: O-Cloud energy saving by O-Cloud pod relocation and node shutdown1

A Node is the smallest unit of a computing hardware, such as a physical or virtual machine. Programs running on Nodes are packaged as containers. One or more containers form a structure are called a pod. A pod might comprise functionalities supporting one or multiple cells or parts of one or multiple cells. As shown in Figure 8.1.1-1, O-Cloud Node 1 has one VNF pod deployed which can be relocated to the O-Cloud Node 2, which would make O-Cloud Node 1 idle. Post relocation of the VNF pod, the idle O-Cloud Node 1 can be shut down to reduce energy consumption.

Non-RT RIC will use O1 and O2 data to provide guidance for shutdown decision. For example, O-Cloud resource utilization matrices such as CPU, memory, and storage utilization can be analyzed by using OCloud Monitoring Service telemetry. Such data can be correlated with RAN related load and energy consumption information obtained per Network Function via the O1 interfaces.

# 8.1.2 Architecture/Deployment Option

Background information on O-Cloud architecture and management: Federated O-Cloud Orchestration and Management (FOCOM), Network Function Orchestrator (NFO), Infrastructure Management Services (IMS) and Deployment Management Services (DMS) are defined in O-RAN.WG6.O2-GA&P [20]. The FOCOM is responsible for accounting and asset management of the resources in the cloud. The NFO is responsible for orchestrating the assembly of the network functions as a composition of NF deployments in the O-Cloud. The IMS is responsible for management of the O-Cloud resources and the software which is used to manage those resources, and the DMS is responsible for management of NF deployments into the O-Cloud.

In this deployment option, decision making for O-Cloud Node Shutdown configuration and guidance, potentially including AI/ML model training and inference, is done at the SMO/Non-RT RIC. The overall mechanism is shown in Figure 8.1.2-1.

![](images/bce2840d7d93c05990fbe380c3b5912f3cde63abbe166915ee93fc2ec948a196.jpg)

> **Image Summary:** (Summary not available)
  
Figure 8.1.2-1: Cloud Resource Energy Saving via SMO/Non-RT RIC

# 8.1.2.1 Description and UML Diagram

Table 8.1.2.1-1: O-Cloud Node Shutdown: AI/ML inference via Non-RT RIC   

<table><tr><td rowspan=1 colspan=1>Use Case Stage</td><td rowspan=1 colspan=1>Evolution / Specification</td><td rowspan=1 colspan=1>&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td rowspan=1 colspan=1>Goal</td><td rowspan=1 colspan=1>Shutting down O-Cloud Nodes during idle times or low load scenario forenergy saving purpose.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Actors and Roles</td><td rowspan=1 colspan=1>SMO (FOCOM): Receives guidance from Non-RT RIC and generatesoptimized configurations towards O-Cloud.SMO (NFO): Receives guidance from Non-RT RIC and generatesoptimized configurations towards O-Cloud.Non-RT-RIC (rApp): Trains Al/ML models and generates guidance.O-Cloud (IMS): Executes changes recommended by SMO/FOCOM.O-Cloud (DMS): Executes changes recommended by SMO/NFO.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Assumptions</td><td rowspan=1 colspan=1>The &quot;Service Request&quot; from Non-RT RIC to the FOCOM includes theidentifiers of the O-Cloud Node(s) to be evacuated or shut down.The “Service Request&quot; from Non-RT RIC to the NFO includes theidentifiers of the NFs to be modified.Non-RT RIC (rApp) subscribed to receive notifications from SMO.SMO (FOCOM and NFO) gets guidance from Non-RT RIC (rApp).</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Pre-conditions</td><td rowspan=1 colspan=1>All relevant functions and components are instantiated and available.Non-RT RIC can receive configurations, load and performancemeasurements from E2 Nodes via O1 and telemetry data from O-Cloudvia O2.O-Cloud ensures that relocation of NF pod from one Node to anotherNode does not impair network services.O-Cloud ensures that NF Pod shutdown does not impair networkservices related to that NF.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Begins when</td><td rowspan=1 colspan=1>The operator has enabled or has set targets for O-Cloud Node Shutdown.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 1.1, 1.2, 1.3,1.4 (M)</td><td rowspan=1 colspan=1>Network Function (applications) related data is subscribed to and receivedover O1 interface, for example traffic load of NF, NF utilization, NF energyconsumption etc.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 2.1, 2.2, 2.3,2.4, 2.5, 2.6, 2.7, 2.8(M)</td><td rowspan=1 colspan=1>O-Cloud utilization matrices (such as CPU, Memory, Storage utilization) andNF placement are acquired by Non-RT RIC from O-Cloud via SMO frameworkover O2 interface.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 3.1, 3.2 (0)</td><td rowspan=1 colspan=1>Non-RT RIC trains the Al/ML models with the collected data. Trained Al/MLmodels are deployed and activated in the Non-RT RIC. Non-RT RICconstantly monitors performance and energy consumption of the O-CloudNodes, NF deployments, as well as cell load related and traffic data, EE/ECmeasurement reports etc.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 4.1, 4.2, 4.3, 4.4,4.5, 4.6 (M)</td><td rowspan=1 colspan=1>Non-RT RIC provides guidance to FOCOM and NFO to modify NFdeployments and to evacuate the specific O-Cloud Node(s).NFO requests the DMS over O2dms to modify NF deployment.FOCOM requests the IMS using O2ims interface to evacuate one or more O-Cloud Nodes after modification (shutdown, relocation etc.) of NFdeployments.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 5.1, 5.2, 5.3 (O)</td><td rowspan=1 colspan=1>IMS notifies SMO that the O-Cloud Node(s) evacuation is completed (orrejected).</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 6.1, 6.2, 6.3, (M)</td><td rowspan=1 colspan=1>Non-RT RIC provides guidance to FOCOM, then FOCOM configures IMS toshutdown Node(s).</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 7 (M)</td><td rowspan=1 colspan=1>IMS shuts down the requested O-Cloud Node(s).</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 8.1, 8.2, 8.3 (M)</td><td rowspan=1 colspan=1>IMS notifies SMO that O-Cloud Node(s) shut down is completed.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Ends when</td><td rowspan=1 colspan=1>O-Cloud Node(s) have been shut down.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Exceptions</td><td rowspan=1 colspan=1>None identified.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Post-conditions</td><td rowspan=1 colspan=1>O-Cloud Node(s) may be shut down for energy saving.SMO/Non-RT RiC continues to monitor the load on the O-Cloud and RANdata by collecting and monitoring the relevant performance and matricesusing O1 and 02.</td><td rowspan=1 colspan=1></td></tr></table>

skinparam defaultFontSize 12   
autonumber   
Box “O-Cloud Platform” #lightseagreen participant “IMS” as IMS participant “DMS” as DMS   
End box   
Box "Service Management & \n Orchestration Framework" #gold Participant “FOCOM” as FOCOM Participant “NFO” as NFO Participant “OAM Functions” as OAM Participant " Non-RT RIC & rApp" as nRT   
End box   
Box "O-RAN" #lightpink Participant "E2-Nodes" as E2N   
End box   
$= =$ O1 & O2 Data Collection $= =$   
autonumber 1.1   
note over nRT,OAM   
User traffic load on NF(O-DU/O-CU), NF(O-DU/O-CU)Resource utilization etc. data to   
retreieved   
End note nRT $- >$ OAM : Data subscription request   
Loop OAM $- >$ E2N : $< < 0 1 > >$ Data subscription request E2N -> OAM :<<O1>>Data Retrieval OAM $- >$ nRT : Data Retrieval   
End Loop   
Note over nRT,IMS   
O2ims & O2dms telemetry, configurations such as CPU,Memory, Storage utilization,O-Cloud   
Node configurations etc   
End note   
autonumber 2.1 nRT $- >$ FOCOM : Data collection request nRT $- >$ NFO : Data collection request FOCOM $- >$ IMS : $< < 0 2$ ims>> Data collection request NFO $- >$ DMS : <<O2dms>> Data collection request   
Loop IMS $- >$ FOCOM : $< < 0 2$ ims>> Data retrieval DMS $- >$ NFO : <<O2dms>> Data retrieval FOCOM $- >$ nRT : Data retrieval NFO $- >$ nRT : Data retrieval   
End Loop   
$= =$ AI/ML Flow $= =$   
autonumber 3.1 nRT $- >$ nRT: AI/ML model training nRT $- >$ nRT: AI/ML model inference   
$= =$ O-Cloud Node Evacuation (Optional) $= =$   
Note over nRT,FOCOM   
Draning request to be included with necessary O-Cloud Node identifiers   
End note   
autonumber 4.1 nRT $- >$ FOCOM: Guidance to evacuate O-Cloud Node nRT $- >$ NFO: Guidance to modify NF deployment NFO $- >$ DMS: <<O2dms>> Modify NF deployment FOCOM $- >$ IMS:<<O2ims>> Evacuate O-Cloud Node   
Loop for each \nNF Deployment DMS -> DMS: NF Modification   
End Loop   
Loop for each \nO-Cloud Node IMS $- >$ IMS: Evacuate O-Cloud Node   
End Loop   
autonumber 5.1 DMS $- >$ NFO :<<O2dms>> Completion of NF \n deployment modification IMS $- >$ FOCOM : $< < 0 2$ ims>> Completion \nof O-Cloud Node Evacuation

NFO $- >$ nRT : Notify completion of NF \ndeployment modification FOCOM $- >$ nRT : Notify completion \nof O-Cloud Node Evacuation

$= =$ O-Cloud Node Shutdown $= =$   
Note over nRT , FOCOM   
Shutdown request to be included with necessary O-Cloud Node identifiers   
End note   
autonumber 6.1 nRT $- >$ FOCOM: Guidance to shutdown O-Cloud node FOCOM $- >$ IMS: $< < 0 2$ ims>> Shutdown O-Cloud Node   
autonumber 7   
Loop For each\n O-Cloud Node IMS $- >$ IMS: Perform shutdown\n of O-Cloud Node   
End Loop   
autonumber 8.1 IMS $- >$ FOCOM: :<<O2ims>>Completion of shutdown\n of O-Cloud Node FOCOM $- >$ nRT: Notify shutdown of O-Cloud Node

@enduml

![](images/fb94d64b545b1d5c681f5540c399f1dfac7aaadff74fd59c15ef4d6ac9463ade.jpg)

> **Image Summary:** (Summary not available)
  
Figure 8.1.2.1-1: Flow diagram for O-Cloud Node shutdown

# 8.1.2.2 O-RAN Entity Roles

1) Non-RT RIC (rApp)

a) Collect configurations, performance indicators and power consumption information from E2 Nodes and O-Cloud Nodes via SMO, for the purpose of decision making, optionally using training and inference of AI/ML models that assist such EE/ES functions.   
b) Collect O-Cloud configuration data from O2 via SMO / from FOCOM and from NFO including policies applied to O-Cloud.   
c) Provide guidance towards FOCOM to evacuate or shut down O-Cloud Nodes.   
d) (Optionally) Deploy, update, configure and trigger execution of EE/ES AI/ML models.

2) E2 Node

a) Report KPIs and measurements related to load and power consumption information to SMO via O1 interface.

3) O-Cloud (DMS)

a) Report NF deployment information to SMO via O2dms interface.   
b) Apply NF deployment configurations received over O2dms.   
c) Provide feedback on NF deployment modification actions.

4) O-Cloud (IMS)

a) Report infrastructure and deployment telemetry data to SMO via O2 interface. For example, OCloud Node configuration, health status, server memory utilization and I/O load overtime, CPU, network, and memory usage.   
b) Apply configurations received over O2ims related to O-Cloud Node draining and shutdown as part of O-Cloud energy saving optimization.   
c) Provide feedback post completion or non-completion of actions to SMO.

# 5) SMO (NFO)

a) Collect the necessary configurations and NF deployment data from O-Cloud triggered by Non-RT RIC and forward information towards Non-RT RIC.   
b) Decide about optimized O-Cloud deployment configuration based on guidance received from NonRT RIC to modify NF deployments. Send optimized O-Cloud deployment configuration to O-Cloud via O2dms interface.   
c) Monitor the NF deployment of O-Cloud NF via O2dms and report to Non-RT RIC.

6) SMO (FOCOM)

a) Collect the necessary configurations, performance indicators, and measurement reports data from OCloud triggered by Non-RT RIC and forward information towards Non-RT RIC.   
b) Decide about optimized O-Cloud configuration based on guidance received from Non-RT RIC to evacuate or shut down O-Cloud Nodes. Send optimized O-Cloud Node configuration to O-Cloud via O2ims interface.   
c) Monitor the performance of O-Cloud Nodes via O2ims and report to Non-RT RIC.

# 8.1.2.3 Void

# 8.1.3 Impact Analysis on O-RAN Work Groups

No detailed impact analysis has been conducted during this study.

NOTE 8.1-1 should be resolved by WG6 during normative phase.

# 8.1.4 Relation and Impact on 3GPP Specifications

No specific relation and impact on 3GPP specifications have been identified during the study.

# 8.1.5 Void

# 8.1.6 Feasibility Analysis

# 8.1.6.1 Service Continuity during NF relocation

NF pod relocation between cluster nodes involves shutting down the NF pod on its original node and starting a new NF pod on another node. In order to avoid impairment of the network performance and service continuity, it has to be guaranteed that all functionalities and traffic allocated to the original NF pod are reallocated before shutdown.

# 8.1.6.2 Pooling vs. Scaling Gains

Nodes can be shut down only if all pods running on them are shut down. O-Cloud Node Shutdown will result in concentration of pods on a fewer number of nodes, which also decreases resiliency and robustness.

# 8.1.6.3 Start-up Time for Scale Out Operation

Scale out operation after node shutdown involves startup of several pieces of hardware, initialization of its operating system and virtualization layers, configuring it as a cluster node, and adding it to the cluster as a node. Overall, this sequence of procedures can take several minutes. Therefore, Energy Saving procedures and resiliency/robustness procedures are to be optimized jointly.

NOTE 8.1-1: To be assessed by WG6, how fast reconfigurations of the O-Cloud Node Shutdown by SMO / Non-RT RIC can be applied in the O-Cloud and if there is any specific requirement.

# 8.2 Sub Use Case 2: O-Cloud CPU Energy Saving Mode

# 8.2.1 Problem Statement, Solution and Value Proposition

This use case describes a method of O-Cloud Energy Saving in which preferred CPU Energy Saving modes can be configured by SMO/Non-RT RIC. CPU Energy Saving modes, implemented by the vendor or standardized, may correspond to different CPU energy saving states (related to, e.g., CPU frequency, voltage, certain sleep modes) that can be controlled externally for CPU Power Management. O-Cloud might for instance be configured with a range (or utilization factor) of allowed or suggested CPU Energy Saving modes. O-Cloud is allowed to do fast adaptations of the CPU Energy Saving modes autonomously (e.g., based on instantaneous load of one or multiple CPUs) within that range. Alternatively, O-Cloud might be configured with a maximum CPU Energy Saving mode. O-Cloud is allowed to select among Energy Saving modes up to the maximum O-Cloud Energy Saving mode autonomously. By this, energy savings can be maximized, while still limiting the impact on QoS/user experience (e.g., potential latency impact on user plane traffic). The operator is allowed to control and tune O-Cloud energy saving gains versus O-Cloud performance.

Examples for CPU Energy Saving modes are the control of CPU frequency/voltage (P-state) and/or certain C-state of the O-Cloud Node CPUs as explained in the following.

# CPU frequency (P-State):

P-States provide a way to scale the CPU frequency and voltage to reduce the power consumption of the CPU. The number of available P-States can vary with the type of CPU, even those from the same family, or one can change the corresponding frequency of the CPU. P-states can typically be limited or disabled in a system’s firmware such as UEFI/BIOS.

Frequency of the CPU (P-State) can be dynamically changed based on the load on the O-Cloud Node and thus O-Cloud Node energy consumption can be modified. The decision to select a desired CPU frequency (PState) can be done by examining the current operational CPU frequency (P-State), CPU utilization and other related O2 and O1 (Traffic) telemetry from the O-Cloud instance.

P-State or CPU Frequency can be changed for the whole CPU (all cores) as well as for individual cores of a CPU.

# C-State:

C-States are usually starting in C0, which is the normal CPU operating mode, i.e., the CPU is $100 \%$ turned on. With increasing CNumber, the CPU sleep mode is deeper, i.e., more circuits are turned off and more time is required to return the CPU back to C0 mode, i.e., to wake-up. Each mode is named individually and several of them have sub-modes with different power saving and thus wake-up time levels.

Example C-states:

C0 is the operational state, meaning that the CPU is $100 \%$ turned on. • C1 is the first idle state. • C2 is the second idle state.

At the O-Cloud Node CPU level, power usage can be controlled in various ways. One way is by controlling the C-State of the CPU in CPE idle condition. C-States reflect the capability of an idle processor to turn off unused components to save power.

The decision of desired C-State must consider the NF deployment distribution on the O-Cloud instance and might involve consolidating the deployments on the limited set of O-Cloud Nodes based on O2 telemetry analysis such as CPU utilization, memory utilization, etc.

C-State can be changed at the CPU level, or at the individual core level of that CPU.

# 8.2.2 Architecture/Deployment Option

In this deployment option, decision making for CPU Energy Saving Mode utilization control, potentially including AI/ML Model Training and Inference, is done at the Non-RT RIC. The overall mechanism is shown in Figure 8.2.2-1.

![](images/7fb74a39aebcde26d8aa43eedf1e104482ffea8867311332e5a151d56879b6c9.jpg)

> **Image Summary:** (Summary not available)
  
Figure 8.2.2-1: O-Cloud CPU Energy Saving Mode via SMO/Non-RT RIC

NOTE 0-1: The interface between Non-RT RIC and FOCOM is for illustrative purposes, subject to further modification by WG1 ATG architecture specifications.

NOTE 0-2: To be studied by WG2 if rApp has all information from O-Cloud to generate the updated guidance towards FOCOM.

# 8.2.2.1 Description and UML Diagram

Table 8.2.2.1-1: O-Cloud CPU Energy Saving Mode: AI/ML inference via Non-RT RIC   

<table><tr><td rowspan=1 colspan=1>Use Case Stage</td><td rowspan=1 colspan=1>Evolution / Specification</td><td rowspan=1 colspan=1>&lt;&lt;Uses&gt;&gt;Related use</td></tr><tr><td rowspan=1 colspan=1>Goal</td><td rowspan=1 colspan=1>Optimizing CPU Energy Saving Mode for power management of the O-Cloud Node CPUs (e.g., to preferably use low power mode when CPU isidle or operating at low load).</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Actors and Roles</td><td rowspan=1 colspan=1>SMO/FOCOM: Receives guidance from Non-RT RIC and generatesoptimized configurations towards O-Cloud.Non-RT RIC (rApp): Trains Al/ML models and generates guidance.O-Cloud (IMS): Executes changes recommended by SMO/Non-RT RIC.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Assumptions</td><td rowspan=1 colspan=1>The &quot;Service Request&quot; to the FOCOM includes the identifiers of the O-Cloud Node(s) to be controlled. Non-RT RIC (rApp) has subscribed to receive notifications from SMO.SMO (FOCOM) gets guidance from Non-RT RIC (rApp), where rAppmay host the algorithm(s) that determine to control the CPU EnergySaving Mode.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Pre- conditions</td><td rowspan=1 colspan=1>All relevant functions and components are instantiated and available.Non-RT RIC can receive configurations, load, performancemeasurements from RAN nodes via the O1 and telemetry data from O-Cloud via O2.Changes of the CPU Energy Saving Mode(s) within the O-Cloud areenabled from O-Cloud Node BIOS/UEFI.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Begins when</td><td rowspan=1 colspan=1>The operator has enabled or has set targets for this CPU Energy SavingMode control.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 1.1, 1.2, 1.3 (M)</td><td rowspan=1 colspan=1>Collection of traffic load and utilization and RAN configurations relatedNetwork function (O-DU and O-CU) data over O1 interface.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 2.1, 2.2, 2.3, 2.4,2.5,2.6, 2.7, 2.8 (M)</td><td rowspan=1 colspan=1>O-Cloud Node telemetry and inventory, for example CPU utilization,supported and currently used CPU Energy Saving Mode etc. over O2interface to be acquired from SMO.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 3.1, 3.2 (0)</td><td rowspan=1 colspan=1>Non-RT RIC optionally trains the Al/ML models with the collected data.Trained Al/ML models are deployed and activated in the Non-RT RIC. Non-RT RIC constantly monitors RAN performance and energy consumption ofthe O-Cloud Nodes for inference; for example, load related and trafficinformation, EE/EC measurement reports, CPU, Memory, Storage utization,etc.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 4.1, 4.2 (M)</td><td rowspan=1 colspan=1>Non-RT RIC provides guidance to FOCOM, then FOCOM configures IMSwith preferred CPU Energy Saving Mode(s) for the CPU of O-Cloud Node(s).NOTE: CPU cores of specific O-Cloud Node might be identified in guidanceor O2 configuration.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 5 (M)</td><td rowspan=1 colspan=1>IMS applies optimized CPU Energy Saving Mode of each O-Cloud Node tothe configured CPU Energy Saving Mode.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Step 6.1, 6.2, 6.3 (M)</td><td rowspan=1 colspan=1>IMS notifies SMO and SMO notifies Non-RT RIC that change of EnergySaving Mode utilization is completed.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Ends when</td><td rowspan=1 colspan=1>CPU Energy Saving Mode has been changed.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Exceptions</td><td rowspan=1 colspan=1>None identified.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Post-conditions</td><td rowspan=1 colspan=1>Based on the load on the O-Cloud Nodes, the desired CPU Energy Savingmode is changed. Thus, CPU Energy Saving mode (e.g., CPU frequency (P-State) and/or C-State of CPU) is optimized for or energy saving purposes.</td><td rowspan=1 colspan=1></td></tr></table>

@startuml   
autonumber   
Box “O-Cloud Platform” #lightseagreen participant “IMS” as IMS participant “DMS” as DMS   
End box   
Box "Service Management & \n Orchestration Framework" #gold Participant “FOCOM” as FOCOM Participant “NFO” as NFO Participant “OAM ” as OAM Participant “NonRT RIC” as nRT   
End box   
Box "O-RAN" #lightpink Participant "E2-Nodes" as E2N   
End box   
$= =$ O1 & O2 Data Collection $= =$   
autonumber 1.1   
note over nRT,OAM   
User Traffic Load, RAN configurations related to Network functions (O-DU & O-CU) data to   
be retrieved   
End note nRT -> OAM : Data subscription request   
Loop OAM $- >$ E2N : $< < 0 1 > >$ Data subscription request E2N -> OAM : $< < 0 1 > >$ Data retrieval OAM $- >$ nRT : Data retrieval   
End Loop   
Note over nRT,IMS   
O2ims & O2dms telemetry & inventory such as supported CPU Energy Saving Modes and status,   
CPU utilization, current operational CPU Power, Frequency, Voltage etc of O-Cloud node to   
be retrieved   
End note   
autonumber 2.1 nRT $- >$ FOCOM : Data collection request FOCOM $- >$ IMS : $< < 0 2$ ims>> Data collection request nRT $- >$ NFO : Data collection request NFO $- >$ DMS : <<O2dms>> Data collection request   
Loop IMS $- >$ FOCOM : $< < 0 2$ ims>> Data retrieval DMS $- >$ NFO : <<O2dms>> Data retrieval FOCOM $- >$ nRT : Data retrieval NFO $- >$ nRT : Data retrieval   
End Loop   
$= =$ AI/ML Flow $= =$   
autonumber 3.1 nRT $- >$ nRT: AI/ML model training nRT $- >$ nRT: AI/ML model inference   
$= =$ CPU Energy Saving Mode Optimization $= =$   
autonumber 4.1 nRT $- >$ FOCOM: Guidance of CPU Energy Saving Mode FOCOM $- >$ IMS: <<O2ims>> Configure CPU Energy Saving Mode   
autonumber 5   
Loop For each O-Cloud Node IMS $- >$ IMS: Perform Change of CPU Energy Saving Mode   
End Loop   
autonumber 6.1 IMS -> FOCOM: <<O2ims>> Notify change of CPU Energy Saving Mode of O-Cloud Node FOCOM $- >$ nRT: Notify change of CPU Energy Saving Mode of O-Cloud Node   
@enduml

![](images/e8caec1cf683b9f2672775f72285aa35217f598123642b3fc37c7b2f01ea7610.jpg)

> **Image Summary:** (Summary not available)
  
Figure 8.2.2.1-1: Flow diagram for O-Cloud CPU Energy Saving Modes

# 8.2.2.2 O-RAN Entity Roles

1) Non-RT RIC (rApp)

a) Collect configurations, performance indicators and power consumption information from SMO, E2 Nodes and O-Cloud Nodes, for the purpose of decision making, optionally using training and inference of AI/ML models that assist such EE/ES functions.   
b) Collect O-Cloud configuration data from FOCOM including supported CPU Energy Saving Modes and planned policies or configuration changes towards O-Cloud.   
c) Collect O-Cloud configuration data from NFO including NF deployment configuration and planned policies and configuration changes towards O-Cloud.   
d) Provide guidance to FOCOM to change CPU Energy Saving Mode.   
e) (Optional) Deploy, update, configure and trigger execution of EE/ES AI/ML models.

NOTE 0-3: Framework and procedure for guidance from Non-RT RIC to NFO/FOCOM within SMO to be studied in WG1 ATG.

2) E2 Node

a) Report KPIs and measurements related to load and power consumption information to SMO via O1 interface.

3) O-Cloud (including IMS and DMS)

a) Report infrastructure telemetry data to SMO via O2 interface, for example O-Cloud Node health status, server memory utilization and I/O load over time and deployment telemetry data like CPU, network, and memory usage etc.   
b) Apply configurations received over O2ims related to CPU Energy Saving Mode.   
c) Provide feedback post completion or non-completion of actions to SMO and/or to Non-RT RIC through SMO.

# 4) SMO (FOCOM/NFO)

a) Collect the necessary configurations, performance indicators, and measurement reports data from RAN nodes and O-Cloud triggered by Non-RT RIC and forward information towards Non-RT RIC.   
b) Decide about optimized O-Cloud configuration based on guidance received by Non-RT RIC to optimize CPU Energy Saving Mode utilization. Send optimized O-Cloud Node configuration to OCloud via O2ims interface.   
c) Monitor the performance of O-Cloud Nodes via O2ims and RAN Network functions via O1; when the optimization objective fails, initiate fall-back procedure; meanwhile, trigger the AI/ML model retraining, data analytics and optimization in Non-RT RIC.

# 8.2.2.3 Void

# 8.2.3 Impact Analysis on O-RAN Work Groups

No detailed impact analysis has been conducted during this study.

NOTE 8.2-1 through NOTE 8.2-4 shall be resolved by WG1 ATG, WG2 and WG6 during normative phase.

# 8.2.4 Relation and Impact on 3GPP Specifications

No specific relation and impact on 3GPP specifications have been identified during the study.

8.2.5 Void

# 8.2.6 Feasibility Analysis

# 8.2.6.1 Not to Restrict Fast CPU Energy Saving Mode Switching

O-Cloud has instantaneous knowledge about O-Cloud resource and energy consumption and is therefore capable of fast adaptions. Moreover, different energy saving features might be available and run on different time scales, with different latency requirements. SMO/Non-RT RIC configurations should not restrict the OCloud from utilizing other (faster) energy saving features in case those are deemed optimal in the given context and decrease the energy consumption.

NOTE 8.2-4: To be assessed by WG6, how fast reconfigurations of the CPU Energy Saving Mode by SMO/FOCOM can be applied in the O-Cloud, and if there is any specific requirement.

# 9 Summary and Conclusion

In the O-RAN WG1 UCTG Network Energy Saving pre-normative phase, Network Energy Saving use cases have been analyzed. This Technical Report presents the results of the pre-normative phase Network Energy Saving work item.

Carrier and Cell Switch Off/On is a technique which enables turning off cells/carriers in case there is no load/UEs in the respective cell/carrier, and the neighboring cells/carriers can take over the expected additional load. The algorithm to trigger off/on switching may be hosted in the Non-RT RIC or in the NearRT RIC. Performance, load, resource utilization, and energy/power consumption related KPIs are forwarded to the RIC from the E2 Nodes and O-RUs, and the RIC-based applications determine recommendations for cells/carriers to be switched off (energySavingState). Ultimately, the switch-off operations are performed by the E2 Node (O-CU) since additional critical operations are required which are handled by the O-CU. While for the Non-RT RIC deployment all input/output parameters are existing, enhancements to the E2 interface are required when the algorithm is hosted by the Near-RT RIC. Numerical analysis shows a high potential of this energy saving technique for overall Network Energy Saving. No challenges on feasibility have been identified. Carrier and Cell Switch Off/On is suggested for normative standardization with the foreseen impact on O-RAN WGs as outlined in Section 5.3.

RF Channel Reconfiguration is a technique which enables O-RU to be requested to perform Tx/Rx Array selection. At low load, i.e., when the expected traffic volume or number of connected users are lower than the configured threshold, the power consumption of O-RUs can be reduced by switching off certain $\mathrm { T x } / \mathrm { R x }$ arrays. For example, 32 out of $6 4 \mathrm { T x } / \mathrm { R x }$ Arrays of an O-RU can be switched off in a digital mMIMO architecture. The algorithm to trigger RF Channel Reconfiguration may be hosted in the Non-RT RIC or in the Near-RT RIC. Respective KPIs are collected by the Near-RT/non-RT RIC from the E2 Nodes and ORUs, to be used by the xApps/rApps to determine recommendations for RF Channel Reconfiguration to be executed by the E2 Nodes. Numerical analysis shows a large potential of this energy saving technique for overall Network Energy Saving. Some feasibility aspects are listed in Section 6.6 which should be considered during normative phases in relevant WGs. RF Channel Reconfiguration is suggested for normative standardization with the foreseen impact on O-RAN WGs as outlined in Section 6.3.

Advanced Sleep Modes typically refer to standardized or implementation specific intelligent energy saving techniques in the RAN. The Advanced Sleep Mode Selection use case is a technique which achieves more granular energy saving by optimizing the range of allowed sleep modes in the O-DU/O-RU via RIC-based guidance. Two architecture/deployment options have been identified, 1) Training and Inference in Non-RT RIC, and 2) Training in Non-RT RIC and Inference in Near-RT RIC. In both options, the Non-RT RIC retrieves the E2 Node Sleep Mode capabilities over O1 and R1 via SMO, collects the necessary data from the E2 Nodes and trains an ML model, which is then deployed: for option 1) in the rApp, and for option 2) in the Near-RT RIC (xApp). In option 1) inference of the optimized Sleep Mode utilization range is provided as guidance by the rApp, while in option 2) by the Near-RT RIC (xApp). Some feasibility aspects are listed in Section 7.6 which should be considered during normative phases in relevant WGs. Advanced Sleep Mode Selection is suggested for normative standardization with the foreseen impact on O-RAN WGs as outlined in Section 7.3.

O-Cloud Resource Energy Saving Mode comprises a set of techniques which enable energy savings in the OCloud by reducing the power consumption of various O-Cloud components without impairing the network performance. Two sub use cases have been identified, O-Cloud Node Shutdown and O-Cloud CPU Energy Saving Mode. The O-Cloud Node Shutdown use case is a method for reducing O-Cloud energy consumption by focusing NF deployments on a fewer number of (physical) O-Cloud Nodes and thereby potentially freeing up physical resources. Thereafter, shutting down the idle physical nodes is achieved through guidance from Non-RT RIC to FOCOM. The O-Cloud CPU Energy Saving Mode use case is a method for reducing the OCloud energy consumption by guiding the available CPU-internal energy saving states via guidance provided by Non-RT RIC to FOCOM. Some feasibility aspects are listed in Section 8.1.6 and Section 8.2.6, respectively, which should be considered during normative phases in relevant WGs. O-Cloud Resource Energy Saving Mode is suggested for normative standardization with the foreseen impact on O-RAN WGs as outlined in Section 8.1.3 and Section 8.2.3.

Implementation of NES features should ensure stable and conflict-free network operation. Ideas on design principles for NES applications facilitating appropriate conflict mitigation are outlined in Annex A.

O-RAN O1 interfaces are used for exchange of data for analysis and provisioning of configuration changes in the O-RAN Nodes. How Network Energy Saving use cases utilize the O1 interface for such purpose is described in Annex C in a generic way.

# Annex A (Informative): Design Principles for NES Features

Efficient and stable utilization of NES features requires an intelligent automation and optimization framework, leveraging on collected KPIs and data analytics with AI/ML algorithms. The SMO, the Non-RT RIC and the Near-RT RIC have an essential role in orchestrating energy saving mechanisms across the overall RAN infrastructure. Network operators should be able to control each NES feature at SMO level, for instance by scheduling the activation and deactivation of such features over pre-defined time periods. Intelligent management and orchestration of O-CU, O-DU and O-Cloud resources are required. For example, optimized traffic steering will allow for a dynamic adaptation of active hardware resources.

NES features will differ in their algorithmic solutions with respect to the considered scales, both temporal and spatial. In order to harmonize different features, first a concise scale evaluation is required.

The higher the number of different NES features being deployed in a radio network, the higher the probability of conflicts between actions initiated by individual NES solutions. These kinds of conflicts can be minimized or avoided by either by a respective conflict coordination entity controlling the actions of each NES function during activation, or by an appropriate design of the NES functions facilitating conflict free coexistence, e.g., by deploying NES solutions with diverging time scales.

Currently rApp conflict management is not specified in O-RAN. Therefore, it may be investigated whether the xApp conflict mitigation approach could be expanded to apply for rApps as well. Furthermore, definition of rules for conflict mitigation – to be derived from the design guidelines – is essential.

# Scales of Energy Saving Algorithms

Three different scales of energy saving algorithms are identified:

# 1. Decoupled case

In this case locality in time and (network) space is assumed which leads to local decision-making. Stability of operation is ensured by appropriately chosen hysteresis values. Decoupled NES features are investigated with respect to their potential of being overruled by non-local optimization algorithms. Example use cases are carrier and cell switch on/off and RF channel re-configuration.

# 2. Non-locality in time

Such an algorithm requires a robust forecast. Traffic load is considered being the principal steering basis for this kind of NES features. A generic traffic forecast with statistical guarantees as a generally available feature is essential. This information should be available in the SMO, and not in a dedicated rApp/xApp. An example use case would be switching off network entities during the night.

# 3. Non-locality in space

Earlier research showed the energy saving potential of nearest-neighbour handover algorithms in order to shut off specific cells. Coverage and capacity distinction will assure MNO’s legal obligations and product considerations.

# Solution approach

Temporal and spatial scales of NES solutions need to be specified by App vendors. Concurrent update intervals in capturing the respective data lead to placing the respective Apps in the Non-RT RIC or the NearRT RIC. App “twins” are possible.

# Detecting and Gauging Potential Conflicts

In order to achieve scale-separation and conflict-free optimization hierarchies, NES features have to be charted and given a measure for their potential to figure in non-local optimization strategies. This measure derives from nearest-neighbour interaction of the feature and HW-induced hysteresis requirements. Decoupled NES features are investigated with respect to their potential of being overruled by non-local optimization algorithms (see above).

Potential conflict and instability cases are for instance switching oscillations, SON-like conflicts between different AI/ML procedures for NES features, or SON-like conflicts between NES features and other use cases (e.g., QoE Optimization, Traffic Steering, Massive MIMO Beamforming Optimization, …).

# Design Guidelines

Stability of network operation is key and to be considered first in place. Thus, non-local NES features with inherent instability risks according to the above analysis are to be deprioritized. To that end, proposed Apps are to be evaluated with regard to operational destabilization, and appropriate measures are to be derived.

Secondly the outcome, i.e. the potential for optimization, is to be taken into account. Off-line studies equip MNOs with aggregate estimates of NES effects within the representative time and space intervals. An NES feature with a higher potential of energy savings should overrule those with lower energy saving ability.

Appropriate harmonization between different Apps is essential. MNOs may derive criteria for rApps/xApps in order to ensure conflict-free energy saving hierarchies which App vendors are encouraged to comply to. Prior study work regarding conflict resolution in SON can be used to harmonize AI/ML Apps with different cost functions (use cases) but overlapping or identical action spaces.

# Annex B (Informative): Load profile and O-RU functional blocks

Generally, it is up to the operator to define a load distribution profile reflecting the situation in the network. For the calculation of the average power/energy consumption, weighting factors based on a daily (24 hours) load distribution profile given in Table C-1 as described in ETSI ES 202 706-1 [10] has been used.

Table B-1: Load level durations for daily average calculation   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Low load</td><td rowspan=1 colspan=1>Medium load</td><td rowspan=1 colspan=1>Busy hour load</td></tr><tr><td rowspan=1 colspan=1>Duration/day</td><td rowspan=1 colspan=1>6 hours</td><td rowspan=1 colspan=1>10 hours</td><td rowspan=1 colspan=1>8 hours</td></tr></table>

In Figure B-1 through B-4 as described in ORAN.WG7.OMAC-HAR [17], high-level functional block diagrams for an 4T4R/8T8R and mMIMO O-RUs are shown, depicting the major HW/SW components. Accordingly, the power consumption can be roughly categorized into the following parts:

1. Digital Processing Unit   
2. RF Processing Unit   
3. FH Processing Unit   
4. Power Unit & Other Components

![](images/47e061d9766b8cafd4607741b08903b7afff3925f70ba372df5cf9fbfb6a1485.jpg)

> **Image Summary:** (Summary not available)
  
Figure B-1: Generic O-RU -2x Functional Module Diagram of 4T4R/8T8R

![](images/0c21c0f0e3ba52f08516bf4940077e84017c68e646069dc541ce1b17f99c6d47.jpg)

> **Image Summary:** (Summary not available)
  
Figure B-2: mMIMO NxM T NxM R O-RU igh Level System Architecture #1

![](images/7c386fa756079b6f9c7baef9acaa1984fa0bc78b9070ddc01d6045cb8d214c7f.jpg)

> **Image Summary:** (Summary not available)
  
Figure B-3: mMIMO NxM T NxM R O-RU igh Level System Architecture #2

![](images/f22e33f6dd87eb0f40dafaff1fe51b58cac21d4e082ec93f7c5b72054f351d8a.jpg)

> **Image Summary:** (Summary not available)
  
Figure B-4: mMIMO NxM T NxM R O-RU igh Level System Architecture #3

# Annex C (Informative): O1 interface principles

# C.1: Overview

O-RAN O1 interfaces are used for exchange of data for analysis and provisioning of configuration changes in the O-RAN Nodes (Near-RT RIC, E2 Nodes, O-RUs) required for O-RAN use cases. This informative annex describes the general principles how Network Energy Saving use cases utilize the O1 interface for such purpose in a generic way.

# C.2: O1 interface usage for data collection

The following message flow describes the usage of O1 interface of the Performance Assurance Management Services (see in Section 2.3 Error! Reference source not found.) for data collection.

@startuml   
Skin rose   
skinparam defaultFontSize 12   
autonumber   
Box "Service Management & \n Orchestration Framework" #gold Participant "SMO" as SMO   
End box   
Box "O-RAN Nodes" #lightpink Participant "O-RAN Node" as ORANNODES Participant "PerfMetricJob" as JOB   
End box   
$= =$ Data Collection $= =$   
ref over SMO : Decision making on data collection \t   
autonumber 1.1   
SMO $- >$ ORANNODES : $< < 0 1 > >$ Data collection job creation\   
\n\t\tNETCONF edit-config create   
ref over ORANNODES : Data collection job creation   
ORANNODES $- >$ JOB $\star \star$ : Create   
loop while the PerfMetricJob is active   
JOB $< - >$ ORANNODES: Collect data   
JOB $- >$ SMO : $< < 0 1 > >$ Report data   
ref over SMO: Process data \t   
end   
@enduml

![](images/04b05a381c761251180dd0b279e6c86865768af38b827cd2b5bccb16dc7ef286.jpg)

> **Image Summary:** (Summary not available)
  
Figure C-1: O1 interfaces usage for data collection

O1 Interfaces are used in the data collection flow as described below:

1. In Step 1.1, the Performance Assurance Management Services (see Section 2.3 Error! Reference source not found.) are used to initiate performance measurement data collection. SMO, in the role of Performance Assurance MnS Consumer, sends request to O-RAN Nodes, in the role of Performance Assurance MnS Producer, for collection and retrieval of measurement data. The O1 interface for this procedure is described in Section 2.3.3 Error! Reference source not found.. The Performance Assurance MnS Consumer may specify the reporting mechanism as data file reporting or data streaming.

2. In Step 1.2, O-RAN Nodes internally perform actions to create data collection job, to collect the requested data.

3. While the data collection job is active, the O-RAN Nodes collect the requested data (in Step 1.3). When the request data is ready, O-RAN Nodes send the collected measurement data to the SMO (in Step 1.4). Depending on the reporting mechanism specified by the SMO in Step 1.1, the O-RAN Nodes shall send the measurement data as data file or data streaming. The O1 interface for this procedure is described in Section 2.3.1 Error! Reference source not found. and 2.3.2 Error! Reference source not found. respectively.

4. SMO, after the retrieval of the measurement data, may internally perform further processing of the data and decision making required for use case.

# C.3: O1 interface usage for configuration changes

The following message flow describes the usage of O1 interface of the Provisioning Management Services (see Section 2.1 Error! Reference source not found.) for configuration changes.

@startuml   
Skin rose   
skinparam defaultFontSize 12   
autonumber   
Box "Service Management & \n Orchestration Framework" #gold Participant "SMO" as SMO   
End box   
Box "O-RAN Nodes" #lightpink Participant "O-RAN Node" as ORANNODES   
End box   
$= =$ Configuration changes $= =$   
ref over SMO: Decision making on necessary configuration changes \t   
autonumber 1.1   
SMO $- >$ ORANNODES: $< < 0 1 > >$ NETCONF edit-config create, replace or delete   
ref over ORANNODES: Applying configuration changes   
SMO <-- ORANNODES: $< < 0 1 > >$ NETCONF rpc-reply <OK> or <rpc-error>   
ref over SMO: Update configuration information \t   
|||   
@enduml

![](images/9ba723425dd6f4295550a0721e6f8e7baa8501a7cff7a50f139f114387d02a47.jpg)

> **Image Summary:** (Summary not available)
  
Figure C-2: O1 interfaces usage for configuration changes

O1 Interfaces are used in the configuration changes as described below:

1. In Step 1.1, the Provisioning Management Services (see Section 2.1 Error! Reference source not found.) are used to modify the parameters. SMO, in the role of Provisioning MnS Consumer, sends the request to configure parameters to the O-RAN Nodes, in the role of Provisioning MnS Producer, using the O1 interface described in Section 2.1.3 Error! Reference source not found..

2. The changes are applied to the O-RAN Nodes. O-RAN Nodes may internally update the configurations across internal nodes.

3. In Step 1.2, O-RAN Nodes send the response to the SMO using the O1 interface described in Section 2.1.3 Error! Reference source not found. to indicate the result of the operation in Step 1.1.

4. SMO may read the values of the configuration parameters at any time using the O1 interface described in Section 2.1.5 Error! Reference source not found. and may subscribe to notification using the O1 interface described in Section 2.1.10 Error! Reference source not found. to receive notifications related to any changes to the configuration parameters with the O1 interface described in Section 2.1.9 Error! Reference source not found..

5. SMO may internally update the configuration information across internal nodes.

# Annex D (Informative): Examples of Advanced Sleep Modes

The O-RAN specifications may be able to offer the flexibility to support different types of O-RUs with varying sleep mode capabilities, including the number of sleep modes available, their depth, and wake-up times. These sleep modes may range from shallow modes such as Symbol and Slot to deeper modes like Radio Frame or even longer durations in seconds. Depending on the sleep mode, different entities might be in control of selection. For instance, O-RU may internally execute Symbol to Slot level sleep modes, while O-DU might be responsible for controlling sleep modes from Slot to Radio Frame. Furthermore, Non-RT or Near-RT RIC may provide the operational range of Sleep Mode selection or may provide control for longer sleep modes.

Within the 3GPP Rel.18 study item on Network Energy Savings for NR, the following power states have been captured in Section 5.1 of 3GPP TR 38.864 [19] for evaluation purpose. Energy consumption mode for BS:

1. Micro sleep power state with instantaneous (i.e. per symbol basis) transition time   
2. Light sleep power state with transition times between 6 ms and 640 ms   
3. Deep sleep power state with transition times between $5 0 \mathrm { m s }$ to 10 sec

# Revision history

<table><tr><td rowspan=1 colspan=1>Date</td><td rowspan=1 colspan=1>Revision</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>2023.02.07</td><td rowspan=1 colspan=1>01.00.01</td><td rowspan=1 colspan=1>Removed v01.00 historyInitial version towards v02.00Agreed CR captured:- NOK-2023.01.24-ORAN-CR-0037-UC4_CPUPowerModes_WG6_WG2_ATG_Feedback_v02.docx- NOK-2023.01.26-ORAN-CR-0038-UC4_OCloud_NodeShutdown_WG2_ATG_WG6_Feedback_v02.docxNOTE: This version contains the following agreed CRs which have not been reflected inv01.00 publication.- NOK-2022.09.19-ORAN-CR-0009-UC4_O-Cloud Energy Saving Modes v07.docx- NOK-2022.09.19-ORAN-CR-0008-UC4_O-Cloud Node Shutdown v02.docx</td></tr><tr><td rowspan=1 colspan=1>2023.03.07</td><td rowspan=1 colspan=1>01.00.02</td><td rowspan=1 colspan=1>Agreed CR captured:- VIA.AO-2023.02.28-ORAN-CR-0040-Conclusions for Phase 2_v01.docx- VIA.AO-2023.02.28-ORAN-CR-0039-Editorial Corrections for Phase 2_v02.docx VIA-2023.03.02-ORAN-CR-0041-Editorial Corrections for UC1-2_v01.docxRMI.AO-2023.03.02-ORAN-CR-0038-UseCase3_Advance Sleep Modes_v03.docxNOK-2023.02.23-ORAN-CR-0036-UC3_ASMOptimization_DeploymentOption1_v03.docxNOK-2023.02.23-ORAN-CR-0035-UC3_ASMOptimization_DeploymentOption2_v03.docxEditorial corrections</td></tr><tr><td rowspan=1 colspan=1>2023.03.10</td><td rowspan=1 colspan=1>01.00.03</td><td rowspan=1 colspan=1>Voided Section 7.2.1.3, 7.2.2.3, 7.2.5, 8.1.2.3, 8.1.5, 8.2.2.3, 8.2.5Editorial correctionsClean version for WG1 approval</td></tr><tr><td rowspan=1 colspan=1>2023.03.22</td><td rowspan=1 colspan=1>01.00.04</td><td rowspan=1 colspan=1>Captured WG1 review comments- Table 7.2.1.1-1: Corrected extra node &quot;Non&quot;- &quot;Energy Savings decision making function&quot;and &quot;configuration enforcement function&quot;corrected as &quot;inference host for Energy Savings decision making&quot; and &quot;the subject ofaction for configuration enforcement&quot;Editorial corrections</td></tr><tr><td rowspan=1 colspan=1>2023.03.23</td><td rowspan=1 colspan=1>02.00</td><td rowspan=1 colspan=1>Clean version for TSC approval and publication</td></tr></table>

# History

<table><tr><td rowspan=1 colspan=1>Date</td><td rowspan=1 colspan=1>Revision</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>2022.11.19</td><td rowspan=1 colspan=1>01.00</td><td rowspan=1 colspan=1>v01.00 publication</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td></td></tr></table>