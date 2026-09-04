# O-RAN Working Group 1 Massive MIMO Use Cases Technical Report

# This is a re-published version of the attached final specification.

For this re-published version, the prior versions of the IPR Policy will apply, except that the previous requirement for Adopters (as defined in the earlier IPR Policy) to agree to an O-RAN Adopter License Agreement to access and use Final Specifications shall no longer apply or be required for these Final Specifications after 1st July 2022.

The copying or incorporation into any other work of part or all of the material available in this specification in any form without the prior written permission of O-RAN ALLIANCE e.V. is prohibited, save that you may print or download extracts of the material on this site for your personal use, or copy the material on this site for the purpose of sending to individual third parties for their information provided that you acknowledge O-RAN ALLIANCE as the source of the material and that you inform the third party that these conditions apply to them and that they must comply with them.

# O-RAN Working Group 1 Massive MIMO Use Cases Technical Report

Copyright $©$ 2022 by O-RAN ALLIANCE e.V.

By using, accessing or downloading any part of this O-RAN specification document, including by copying, saving, distributing, displaying or preparing derivatives of, you agree to be and are bound to the terms of the O-RAN Adopter License Agreement contained in the Annex ZZZ of this specification. All other rights reserved.

Revision History   

<table><tr><td rowspan=1 colspan=1>Date</td><td rowspan=1 colspan=1>Revision</td><td rowspan=1 colspan=1>Author</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>2021.06.14</td><td rowspan=1 colspan=1>01.00.00</td><td rowspan=1 colspan=1>Nokia, Keysight</td><td rowspan=1 colspan=1>Document skeleton</td></tr><tr><td rowspan=1 colspan=1>2021.07.09</td><td rowspan=1 colspan=1>01.00.01</td><td rowspan=1 colspan=1>Nokia, Keysight</td><td rowspan=1 colspan=1>Update the ToC</td></tr><tr><td rowspan=1 colspan=1>2021.10.06</td><td rowspan=1 colspan=1>01.00.02</td><td rowspan=1 colspan=1>Editors</td><td rowspan=1 colspan=1>Added approved CRs</td></tr><tr><td rowspan=1 colspan=1>2021.10.08</td><td rowspan=1 colspan=1>01.00.03</td><td rowspan=1 colspan=1>Editors</td><td rowspan=1 colspan=1>Removed change marking</td></tr><tr><td rowspan=1 colspan=1>2021.11.02</td><td rowspan=1 colspan=1>01.00.04</td><td rowspan=1 colspan=1>Editors</td><td rowspan=1 colspan=1>Added additional approved CRs</td></tr><tr><td rowspan=1 colspan=1>2021.11.18</td><td rowspan=1 colspan=1>01.00.05</td><td rowspan=1 colspan=1>Editors</td><td rowspan=1 colspan=1>Added additional approved CRs</td></tr><tr><td rowspan=1 colspan=1>2021.12.01</td><td rowspan=1 colspan=1>01.00.06</td><td rowspan=1 colspan=1>Editors</td><td rowspan=1 colspan=1>Added additional approved CRs</td></tr><tr><td rowspan=1 colspan=1>2021.12.03</td><td rowspan=1 colspan=1>01.00.07</td><td rowspan=1 colspan=1>Editors</td><td rowspan=1 colspan=1>Added additional approved CRs</td></tr><tr><td rowspan=1 colspan=1>2021.12.08</td><td rowspan=1 colspan=1>01.00.08</td><td rowspan=1 colspan=1>Editors</td><td rowspan=1 colspan=1>Added aditional approved CRs</td></tr><tr><td rowspan=1 colspan=1>2021.12.12</td><td rowspan=1 colspan=1>01.00.09</td><td rowspan=1 colspan=1>Editors</td><td rowspan=1 colspan=1>Added additional approved CRs</td></tr><tr><td rowspan=1 colspan=1>2021.12.14</td><td rowspan=1 colspan=1>01.00.10</td><td rowspan=1 colspan=1>Editors</td><td rowspan=1 colspan=1>Added 1 missing CR, clean-up formatting, fixed font issues,removed comments, fixed minor grammaticals</td></tr><tr><td rowspan=1 colspan=1>2021.12.15</td><td rowspan=1 colspan=1>01.00.11</td><td rowspan=1 colspan=1>Editors</td><td rowspan=1 colspan=1>Added additional approved CRs, and agreed-upon changes duringcall on 12/15</td></tr><tr><td rowspan=1 colspan=1>2022.03.24</td><td rowspan=1 colspan=1>01.00.12</td><td rowspan=1 colspan=1>Editors</td><td rowspan=1 colspan=1>Changed title/header, corrected formatting and typos</td></tr><tr><td rowspan=1 colspan=1>2022.03.24</td><td rowspan=1 colspan=1>01.00.13</td><td rowspan=1 colspan=1>Editors</td><td rowspan=1 colspan=1>Changed title/header, corrected formatting and typos</td></tr><tr><td rowspan=1 colspan=1>2022.03.29</td><td rowspan=1 colspan=1>00.00.14</td><td rowspan=1 colspan=1>Editors</td><td rowspan=1 colspan=1>Fix title page, clean version for WG1 approval</td></tr><tr><td rowspan=1 colspan=1>2022.04.04</td><td rowspan=1 colspan=1>01.00</td><td rowspan=1 colspan=1>Editors</td><td rowspan=1 colspan=1>Spec renamed to v01.00 for publication</td></tr><tr><td rowspan=1 colspan=1>2022.05.12</td><td rowspan=1 colspan=1>01.00</td><td rowspan=1 colspan=1>Editors</td><td rowspan=1 colspan=1>Correction of one reference in Section 3.2.2.1.1</td></tr><tr><td rowspan=1 colspan=1>2022.06.01</td><td rowspan=1 colspan=1>01.00</td><td rowspan=1 colspan=1>Editors</td><td rowspan=1 colspan=1>Editorial improvements: Included line separations and page breaksto avoid e.g. table splits, completed table and figure captions,removed few section numbering higher than five digits and included two four digits sub-sections to enable automatic figureand table caption numbering, copy &amp; paste of one paragraph fromchapter 7 into section 3.1 to fill empty space, corrected cross-references and minor editorials</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

# Contents

Revision History ...... .2   
1 Introduction ...... ....6   
1.1 Scope .... .. 6   
1.2 References... ..... 6   
1.3 Definitions and Abbreviations ............... .................. ......... 7   
1.3.1 Definitions..... ......... 7   
1.3.2 Abbreviations .... ..... 8   
2 Objectives and Requirements .......................................................................................................... .........9   
2.1 Objectives ....... ....... 9   
2.2 Requirements .. .. 9   
3 GoB / L3 Mobility.........   
3.1 Overview ...... ...... 11   
3.2 Solution 1: Grid-of-Beams Beamforming (GoB BF) Optimization... ....... 11   
3.2.1 Problem Statement, Solution and Value Proposition . ...... 11   
3.2.2 Architecture/Deployment Options .... ...... 12   
3.2.3 Impact Analysis on O-RAN Working Groups .... .... 17   
3.2.4 Relation and Impact on 3GPP Specifications.... .... 19   
3.2.5 Feasibility and Gain/Complexity Analysis...... ..... 20   
3.3 Solution 2: Beam-based Mobility Robustness Optimization (bMRO) . ... 22   
3.3.1 Problem Statement, Solution, and Value Proposition .... ..... 22   
3.3.2 Architecture/Deployment Options ..... ....... 22   
3.3.3 Impact Analysis on O-RAN Working Groups .. . 26   
3.3.4 Relation and Impact on 3GPP Specification ...... ..... 28   
3.3.5 Feasibility and Gain/Complexity Analysis..... ....... 30   
3.4 Solution 3: AI/ML Based Initial Access (SS Burst Set), CSI-RS and DMRS Configuration Optimization.... 33   
3.4.1 Problem Statement and Value Proposition.... ....... 33   
3.4.2 Architecture/Deployment Options .... ............................. ......... 34   
3.4.3 Feasibility and Gain/Complexity Analysis... ... 54   
4 L1 / L2 Beam Management... ................................................. ...64   
4.1 Overview ..... ....... 64

# Solution 1: AI/ML-assisted Beam Selection Optimization.. . 64

4.2   
4.2.1 Problem Statement and Value Proposition.. ... 64   
4.2.2 Architecture/Deployment Options ..... ..... 65   
4.2.3 Impact Analysis on O-RAN Working Groups . ... 73   
4.2.4 Relation and Impact on 3GPP Specification ... ..... 74   
4.2.5 Feasibility and Gain/Complexity Analysis... ... 74   
5 Non-GoB Beamforming.... ...77   
5.1 Overview ...... ..... 77   
5.2 Solution 1: AI/ML-assisted non-GoB Optimization .... ..... 77   
5.2.1 Problem Statement and Value Proposition... ... 77   
5.2.2 Architecture/Deployment Options . ... 78   
5.2.3 Impact Analysis on O-RAN Working Groups . ..... 86   
5.2.4 Relation and Impact on 3GPP Specification ... ..... 87   
5.2.5 Feasibility and Gain/Complexity Analysis....... ..... 87   
6 MIMO DL Tx Power Optimization, MU-MIMO Pairing and MIMO mode selection..... ......91   
6.1 Overview ... ... 91   
6.2 MIMO optimization use-cases.... ..... 91   
6.2.1 Solution 1: Downlink Transmit power optimization .. ..... 91   
6.2.2 Solution 2: MU-MIMO Pairing Enhancement (User Separability or Pairing Control).. ..... 98   
6.2.3 Solution 3: MIMO mode selection (Mu-MIMO vs Su-MIMO selection optimization)... ... 112   
7 Comparison and Conclusions.... ..122   
7.1 Summary of Evaluation ..... . 124   
7.2 Impact on standardization.... . 125   
7.3 Synergies among new measurements (definition and/or reporting).. . 126   
Annex A Input and output data and its relation to 3GPP specification ....... .127   
Annex ZZZ: O-RAN Adopter License Agreement . .129   
Section 1: DEFINITIONS . . 129   
Section 2: COPYRIGHT LICENSE .. ..... 129   
Section 3: FRAND LICENSE . .... 130   
Section 4: TERM AND TERMINATION ................................................ ...... 130   
Section 5: CONFIDENTIALITY . . 131   
Section 6: INDEMNIFICATION ...... ...... 131

Section 7: LIMITATIONS ON LIABILITY; NO WARRANTY .. 131

Section 8: ASSIGNMENT .. . 131

Section 9: THIRD-PARTY BENEFICIARY RIGHTS . . 132

Section 10: BINDING ON AFFILIATES . . 132

Section 11: GENERAL. . 132

# 1 Introduction

# 1.1 Scope

This Technical Report has been produced by the O-RAN Alliance.

The contents of the present document are subject to continuing work within O-RAN and may change following formal O-RAN approval. Should the O-RAN Alliance modify the contents of the present document, it will be re-released by ORAN with an identifying change of release date and an increase in version number as follows:

Release xx.yy.zz

where:

xx the first two-digit value is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc. (the initial approved document shall have $\mathbf { X } \mathbf { X } { = } 0 1$ ).

yy the second two-digit value is incremented when editorial only changes have been incorporated in the document.

zz the third two-digit value is included only in working versions of the document indicating incremental changes during the editing process; externally published documents never have this third two-digit value included.

The present document provides a technical report on RIC-enabled massive MIMO use cases.

# 1.2 References

The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

References are either specific (identified by date of publication, edition number, version number, etc.) or   
non-specific.   
For a specific reference, subsequent revisions do not apply.   
For a non-specific reference, the latest version applies. In the case of a reference to a 3GPP document (including   
a GSM document), a non-specific reference implicitly refers to the latest version of that document in the same   
Release as the present document. [1] 3GPP TR 21.905: "Vocabulary for 3GPP Specifications". [2] MU-MIMO and CSI Feedback Performance of NR/LTE, Bishwarup Mondal et al., 2019 53rd Annual Conference on Information Sciences and Systems (CISS), 20-22 March 2019 [3] E. Bjornson, J. Hoydis, and L. Sanguinetti, Massive MIMO Networks: Spectral, Hardware, and Energy Efficiency. Foundations and Trends in Signal Processing, vol. 11, no. 3-4, pp. 154-655, 2017 [4] T. Marzetta, E Larsson, H. Yang, and H. Ngo, Fundamentals of Massive MIMO, Cambridge University Press, 2016 [5] Physical Layer Measurements 3GPP TS 38.215 V16.4.0 (2020-12)

# 1.3 Definitions and Abbreviations

# 1.3.1 Definitions

For the purposes of the present document, the terms and definitions given in TR 21.905 [1] and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in TR 21.905 [1]

Non-RT RIC (O-RAN non-real-time RAN Intelligent Controller): a logical function that enables non-real-time control and optimization of RAN elements and resources, AI/ML workflow including model training and updates, and policybased guidance of applications/features in Near-RT RIC.

Near-RT RIC (O-RAN near-real-time RAN Intelligent Controller): a logical function that enables near-real-time control and optimization of RAN elements and resources via fine-grained (e.g. UE basis, Cell basis) data collection and actions over E2 interface.

O-CU: O-RAN Central Unit: a logical node hosting RRC, SDAP and PDCP protocols.

O-CU-CP: O-RAN Central Unit – Control Plane: a logical node hosting the RRC and the control plane part of the PDCP protocol.

O-CU-UP: O-RAN Central Unit – User Plane: a logical node hosting the user plane part of the PDCP protocol and the SDAP protocol.

O-DU: O-RAN Distributed Unit: a logical node hosting RLC/MAC/High-PHY layers based on a lower layer functional split.

O-RU: O-RAN Radio Unit: a logical node hosting Low-PHY layer and RF processing based on a lower layer functional split. This is similar to 3GPP’s “TRP” or “RRH” but more specific in including the Low-PHY layer (FFT/iFFT, PRACH extraction).

O-eNB (O-RAN eNB): an eNB or ng-eNB that supports E2 interface.

O1: Interface between orchestration & management entities (Orchestration/NMS) and O-RAN managed elements, for operation and management, by which FCAPS management, Software management, File management and other similar functions shall be achieved.

SMO: Service Management and Orchestration system.

A1: Interface between Non-RT RIC and Near-RT RIC to enable policy-driven guidance of Near-RT RIC applications/functions, and support AI/ML workflow.

E2: Interface connecting the Near-RT RIC and one or more O-CU-CPs, one or more O-CU-UPs, and one or more O-DUs.

E2 Node: a logical node terminating E2 interface. In this version of the specification, ORAN nodes terminating E2 interface are:

- for NR access: O-CU-CP, O-CU-UP, O-DU or any combination - for E-UTRA access: O-eNB.

rApp: An application designed to run on the Non-RT RIC. Such modular application leverages the functionality exposed by the Non-RT RIC to provide added value services relative to intelligent RAN optimization and operation

xApp: An application designed to run on the Near-RT RIC. Such an application is likely to consist of one or more microservices and at the point of on-boarding will identify which data it consumes and which data it provides. The application is independent of the Near-RT RIC and may be provided by any third party. The E2 enables a direct association between the xApp and the RAN functionality.

O-Cloud: O-Cloud is a cloud computing platform comprising a collection of physical infrastructure nodes that meet ORAN requirements to host the relevant O-RAN functions (such as Near-RT RIC, O-CU-CP, O-CU-UP, and O-DU), the supporting software components (such as Operating System, Virtual Machine Monitor, Container Runtime, etc.) and the appropriate management and orchestration functions.

# 1.3.2 Abbreviations

For the purposes of the present document, the following abbreviations apply.

ML Machine Learning Non-RT RIC Non-real-time RAN Intelligent Controller Near-RT RIC Near-real-time RAN Intelligent Controller RAN Radio Access Network SMO Service Management and Orchestration

11

# 2 Objectives and Requirements

# 2.1 Objectives

This Technical Report captures the outcome of the WG1 UCTG Massive MIMO pre-normative phase. The objectives of the pre-normative phase are as follows:

study requirements, key issues, proposed solutions, benefits of the massive MIMO enhancements, study potential impact and required enhancements to O-RAN interfaces E2, O1, A1, FH M-plane, FH CUS-Plane, R1 and Near-RT RIC API, study potential impact and required enhancements on data models of all O-RAN entities, identify the any possible impact on Non-RT RIC architecture, Near-RT RIC architecture and AI/ML workflow.

The use cases studied in the Massive MIMO pre-normative phase include:

GoB optimization $( \mathrm { S S B } + \mathrm { C S I } { \mathrm { - R S } }$ based GoB), adaptive beam shaping and beam-based Mobility Robustness Optimization,   
Non-GoB optimization,   
L1/L2 beam management optimization,   
Additional use cases are DL and UL transmit power optimization, optimization of MU-MIMO co-scheduling through control of spatial separation thresholds, reference sequence optimization for minimization of contamination.

The use cases are applicable to FR1 as well as FR2. Algorithms discussed and analysed as part of the Massive MIMO pre-normative phase will be examples only and will not be part of any specification as outcome of this pre-normative phase or subsequent work items.

For each use case solution proposal, the detailed objectives are:

Review, evaluate applicability of, and select from existing deployment alternatives (Non-RT and/or Near-RT   
RIC) and AI/ML deployment scenarios and document respective findings.   
Review, evaluate, and select candidate(s) for normative standardization and document respective findings: o Analyze and evaluate input/output parameters of the algorithm, the impact of the control loop delay on the network performance (e.g., due to dynamic channel conditions) as well as the signaling overhead over the relevant interface, e.g., O1, E2. o Companies should provide simulation results for their mMIMO proposals to evaluate the performance benefits versus complexity taking into consideration E2 load and latency requirements for RIC and E2 node procedures. The availability of simulation results will not be used for gating in decision making. o Study and review additional simulation methodologies required for evaluating RIC-enabled mMIMO optimization approaches. Review and, if possible, leverage existing methodologies already established in 3GPP.

# 2.2 Requirements

mMIMO use cases should reuse the existing 3GPP measurements / measurement reporting for input data as well as the existing 3GPP configuration / provisioning management for the output data as much as possible.

If new measurements or configuration parameters are essential to support new mMIMO use cases, then these should preferably be based on parameters / variables / definitions / procedures that are already used in the 3GPP / O-RAN specifications.

If new measurements or configuration parameters are essential to support new mMIMO use cases, the current standardization approach (specifying the new measurement in 3GPP specifications and referring to in in O-RAN specifications) should be prioritized over inventing new standardization approaches.

# 3 GoB / L3 Mobility

# 3.1 Overview

Grid of Beam Optimization (GoB) provides an automated beam forming configuration tailored to the topology of the cell, the physical environment, as well as the distribution of users and traffic in a cell (e.g. wide beams might cover low-density areas while narrow beams might cover high-density areas). Beam-based Mobility Robustness Optimization (bMRO) is an autonomous self-optimizing algorithm that improves beam-based inter-cell mobility performance by applying beamspecific Cell Individual Offsets (CIO) on the handover triggers between neighbor cells, based on the analysis of beamAI/ML assisted network-wide (multi-gNB/TRP) optimizations framework proactively and autonomously infers optimal configuration per gNB/TRP for SS Burst Set, DMRS and CSI-RS based on available measurements, observations, and PIs at different nodes of the 3GPP NR and/or O-RAN access and core network elements.

# 3.2 Solution 1: Grid-of-Beams Beamforming (GoB BF) Optimization

# 3.2.1 Problem Statement, Solution and Value Proposition

Massive MIMO (mMIMO) is among the key methods to increase performance and QoS in 5G networks. Capacity enhancement is obtained by means of beamforming of the transmitted signals, and by spatially multiplexing data streams. Beamforming can increase the received signal power and simultaneously decrease the interference generated for other users, hence resulting in higher SINR and higher user throughputs. Grid-of-Beams (GoB) with the corresponding beam sweeping has been introduced to allow beamforming of the control channels used during initial access as well as for data transmission and reception, mainly for high frequency (but can be used also for the sub-6 GHz band) MIMO operation. The physical properties of the antenna array and its possible configurations characterize the span of the beams, namely the horizontal and vertical aperture in which beamforming is supported, and therefore the coverage area and the shape of the cell. mMIMO can be deployed in 5G macrocell clusters as well as in heterogeneous networks, where macro-cells and small cells co-exist and complement each other for better aggregated capacity and coverage. In order to obtain optimal beamforming and cell resources (Tx power, PRB) configuration, one will have to look at a multi-cell environment instead of a single cell. Moreover, different vendors may have different implementations in terms of the number of beams, the horizontal/vertical beam widths, azimuth and elevation range, to achieve the desired coverage. In a multi-node/multivendor scenario, centralized monitoring and control is required to offer optimal coverage, capacity and mobility performance as well as control over electromagnetic emissions in order to comply with regulatory requirements.

The problem associated with traditional mMIMO BF is that its performance is highly dependent on the choice of the BF pattern. Manual configuration is usually based on the empirical knowledge and manual test results of the domain expert(s) and is performed in a semi-static way. That is, (near-)real time contextual, per-site information (such as cell geometry change, user/traffic distribution, mobility patterns, seasonalities etc.) is taken into account in a suboptimal and non-real time way. This may cause one or more of the following problems:

1. High inter-cell interference.   
2. Unbalanced traffic between neighboring cells.   
3. Low performance at the cell edges or throughout the cell.   
4. Poor handover performance.

This solution proposes a framework that allows the operator to flexibly configure the mMIMO BF parameters in a cell or in a cluster of cells by means of policies and configuration assisted by machine learning (ML) techniques. The configuration optimization relies on contextual information and patterns such as the user distribution, traffic demand distribution, cell geometries, and mobility.

# 3.2.2 Architecture/Deployment Options

Option 1: Non-RT RIC Deployment

The Non-RT RIC hosts an rApp application whose task is to determine the suitable GoB configuration for a cell or a cluster of cells as a function of input metrics and of an operator objective. The underlying ML model is trained on historical data collected from a cell or a cluster of cells and its aim is to determine correlation patterns between mMIMO GoB configurations and performance metrics. The input data for GoB BF optimization training and inference can be comprised of antenna array parameters, UE mobility/spatial density data, (averaged) traffic density data, timing advance and Angle-of-Arrival measurements (for positioning estimation), power headroom (PH) reports, aggregated and/or preprocessed beam-based reference signal measurements (e.g. CSI reporting, covariance matrix), neighboring cells' beams/interference information, MDT measurement data, as well as performance measurements such as handover and beam failure statistics. The rApp knows O-RU specifics such as antenna array parameters, O-RU capabilities, beam file format (beamforming configuration update procedure) etc.

The output of the inference is the optimized GoB BF configuration, that is, the number of beams and either i) the beam directions, horizontal & vertical beam widths, and power allocation of beams, or ii) the beam weights.

Operator objectives regarding adaptive GoB may include desired coverage, defined in terms of the cell geometry (SSB beams), cell capacity requirements (CSI-RS beams), cell edge performance (e.g. minimum throughput per UE), minimum guaranteed throughput (independent of traffic density), weighted average RSRP requirements (e.g., the operator might wish to implement the strategy to cover low-density areas with wide beams and high-density areas with narrow beams), and desired fairness between cell edge and non-edge UEs.

@startuml   
Box "Personnel" #lightblue Actor "Operator" as RP   
End box   
box "Service Management & \nOrchestration Framework" #gold Participant "SMO & Non-RT RIC" as SMO Participant "rApps" as rAPP   
end box   
box "E2 Nodes" #lightpink collections "O-CUs" as OCU collections "O-DUs" as ODU   
end box   
box "O-RUs" #lightpink collections "O-RUs" as ORUs   
end box   
box "External" #lightseagreen Participant APP   
end box   
Autonumber   
activate RP   
activate APP   
activate SMO   
activate rAPP   
activate ODU   
|||   
group Data Collection

ODU $- >$ SMO : <<O1>> Data Collection OCU -> SMO : $< < 0 1 > >$ Data Collection APP -> SMO : <<EI>> Data Collection end group ML Training SMO --> rAPP: Data Retrieval rAPP --> rAPP: AI/ML model training end group ML Inference alt RP --> SMO: Optimization Trigger/Target else SMO --> SMO: Performance Degradation end SMO $- >$ rAPP: <<R1>> Update Model Request SMO -> rAPP: <<R1>> Data Retrieval rAPP --> rAPP: AI/ML model inference rAPP $- >$ SMO: $< < \mathbb { R } 1 > >$ Optimal mMIMO GoB Configuration end group GoB Configuration alt via O1 SMO $- >$ ODU: $< < 0 1 > >$ File ready notification to inform about file with new GoB configuration ODU $- >$ SMO: <<O1>> File-download request SMO $- >$ ODU: <<O1>> Accepted SMO -> ODU: $< < 0 1 > >$ Notification about successful file-download ref over ODU, ORUs: <<OFH-MP>> Download file with new GoB configuration ref over ODU, ORUs: gNB-DU Configuration Update ref over ODU, ORUs: <<OFH-MP>> Carrier deactivation ref over ODU, ORUs: <<OFH-MP>> New GoB Activation ODU -> ORUs: <<OFH-MP>> <rpc get> (o-ran-beamforming.yang) </rpc> ORUs -> ODU: <<OFH-MP>> <rpc reply> ... </rpc> ref over ODU, ORUs: gNB-DU Configuration Update ref over ODU, ORUs: <<OFH-MP>> Carrier activation else via OFH-MP ref over SMO, ORUs: <<OFH-MP>> Download file with new mMIMO GoB configuration SMO -> ODU: <<O1>> Notification about new GoB configuration file ref over ODU, ORUs: <<OFH-MP>> Carrier deactivation ref over ODU, ORUs: <<OFH-MP>> Activate new GoB configuration ODU -> ORUs: <<OFH-MP>> <rpc get> (o-ran-beamforming.yang) </rpc> ORUs $- >$ ODU: <<OFH-MP>> rpc reply ref over ODU, ORUs: <<OFH-MP>> Carrier activation end end group ML Performance Monitoring SMO --> SMO : Performance monitoring and evaluation SMO --> SMO : Fallback (e.g. restore configuration) SMO $- >$ ODU: <<O1>> Default/Fallback mMIMO configuration SMO --> rAPP : $< < \mathrm { R 1 } > >$ Model retraining and update end @enduml

![](images/c0d0eaf6645b615f68850ca3ade63b6f355209dbdc6f55312a0ec40489acb34b.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.2.2.1-1. Flow diagram of GoB BF Optimization

# Requirements

Required data:

1) Environment data: Cell site information (e.g., location, inter-site distance), BS system configuration (e.g., operating frequency, bandwidth, frame structure, transmit power, default beam weight configuration), complete set of mMIMO configurations, i.e., horizontal/vertical beamwidth adjustable range, azimuth/elevation angle adjustable range.

2) From E2 Nodes (O-CUs and O-DUs):

a) Essential: Measurement report options are forwarding UE’s CSI (CQI, PMI, LI, RI, CRI) feedback information or covariance matrix (or any other compressed form of the information) from the UEs or newly defined Performance Management counters in the cells of interest; the time granularity of data collection should be configurable and satisfy the requirement of the AI/ML model. Any of the three input parameter options coherently support the GoB optimization use case but might support different implementation and deployment options.

b) Optional: Network KPIs: cell downlink/uplink traffic load, RRC connection attempts, average RRC connected UEs, maximum RRC connected UE, DL/UL average active connections, DL/UL throughput, DL/UL spectral efficiency, NI (noise $^ +$ interference), PH reports; beam resource usage (transmitted power per beam/directions and associated PRB usage), beam-based handover and beam failure statistics.

3) From External:

a) Optional: User location related information, e.g. GPS information.

Table 3.2.2.1-1.   

<table><tr><td rowspan=1 colspan=6>Input Data Options</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source → Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>Report-ingPeriod</td><td rowspan=1 colspan=1>New     or     existingmeasurement/reportingspecification</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU → SMO</td><td rowspan=1 colspan=1>CSI report (CQI, PMI, LI, RI,CRI) per UE</td><td rowspan=1 colspan=1>CSIreport</td><td rowspan=1 colspan=1>~15min</td><td rowspan=1 colspan=1>Measurements defined in3GPP TS 38.214 (section5.2)New reportinge.g. 3GPPTS37.320 orO-RAN01/E2</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU → SMO</td><td rowspan=1 colspan=1>Channel covariance matrix (orany other compressed form ofthe information) per UE</td><td rowspan=1 colspan=1>Complexvalues</td><td rowspan=1 colspan=1>~15min</td><td rowspan=1 colspan=1>New measurement e.g.3GPPTS38.215or Ts38.314New reporting. e.g. 3GPPTS37.320or,O-RAN01/E2</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU → SMO</td><td rowspan=1 colspan=1>PM  counter  for  spatialdistribution of estimated trafficdensity</td><td rowspan=1 colspan=1>count</td><td rowspan=1 colspan=1>~15min</td><td rowspan=1 colspan=1>New measurement counterandnewreportinge.g.3GPP TS 28.552</td></tr></table>

Configuration data towards E2 Nodes:

Optimized GoB beam pattern related configuration parameter:

1) Towards O-DU a) via O1 transferring proprietary beamforming configuration files b) via Open FH M-Plane reading o-ran-beamforming YANG module.   
2) Towards O-RU a) via Open FH M-Plane transferring proprietary beamforming configuration file

Table 3.2.2.1-2.   

<table><tr><td rowspan=1 colspan=6>Output Data Options</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source     →Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>Config.Period*</td><td rowspan=1 colspan=1>(Target) Specification</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>SMO→ 0-DU</td><td rowspan=1 colspan=1>Proprietary          beamformingconfiguration file</td><td rowspan=1 colspan=1>file</td><td rowspan=1 colspan=1>~x hours</td><td rowspan=1 colspan=1>O-RAN.WG5.MPChapter 8</td></tr><tr><td rowspan=1 colspan=1>Open FHM-Plane</td><td rowspan=1 colspan=1>O-RU→0-DU</td><td rowspan=1 colspan=1>Beamforming weights or attributesvia YANG module</td><td rowspan=1 colspan=1>ValuesinIE</td><td rowspan=1 colspan=1>~x hours</td><td rowspan=1 colspan=1>O-RAN.WG4.MPSection 12.4.2</td></tr><tr><td rowspan=1 colspan=1>Open FHM-Plane</td><td rowspan=1 colspan=1>SMO→0-RU; O-DU →O-RU</td><td rowspan=1 colspan=1>Proprietary           beamformingconfiguration file</td><td rowspan=1 colspan=1>File</td><td rowspan=1 colspan=1>~x hours</td><td rowspan=1 colspan=1>O-RAN.WG4.MPSection 12.4.2</td></tr><tr><td rowspan=1 colspan=1>Open FHCUS-Plane</td><td rowspan=1 colspan=1>O-DU → 0-RU</td><td rowspan=1 colspan=1>Beamforming weights or attributes</td><td rowspan=1 colspan=1>ValuesinIE</td><td rowspan=1 colspan=1>~x hours</td><td rowspan=1 colspan=1>O-RAN-WG4.CUSSection 5.4.2</td></tr></table>

# ORAN Entity roles:

1) SMO & Non-RT-RIC

a) Collect the necessary configurations, performance indicators, and measurement reports from the E2 nodes (ODU and O-CU), triggered by Non-RT RIC or rApp if required.   
b) Transfer file including optimized mMIMO GoB parameters via O1 (to O-DU) or Open FH M-Plane (to O-RU) interface.   
c) Transfer collected data towards rApp.   
d) Retrieve necessary UE location related information, e.g. GPS coordinates, from the application layer for the purpose of i) training relevant rAPPs and ii) execution of relevant rAPPs.   
e) Monitor the performance of the respective cells; when the optimization objective fails, initiate fallback procedure and/or trigger the rAPP model retraining and re-optimization. Execute the inference/control loop periodically or event-triggered.

2) rApps

a) Retrieve necessary UE location related information, e.g. GPS coordinates, from the application layer for the purpose of training and execution of relevant AI/ML models. b) Infer an optimized GoB BF configuration. 3) O-DUs a) Collect and report to SMO KPIs related to user activity, traffic load and coverage, per beam/area, and information about beams and resource utilization. b) Apply GoB configuration received from the SMO over O1 or received from O-RU over Open FH M-Plane.

4) O-CU a) Collect and report to SMO KPI related to QoS performance and handover/beam failures statistics.   
5) O-RU a) Apply GoB configuration received from the SMO or from the O-DU over Open FH M-Plane.

Note: Aggregated and disaggregated gNB architecture is supported.

# 3.2.3 Impact Analysis on O-RAN Working Groups

Please note: This is an initial impact analysis as part of the WG1 UCTG work on mMIMO. The intention is to estimate the expected standardization effort within the O-RAN working groups. It is up to the WGs to decide how the mMIMO functionality should be specified in specifications of each WG.

WG1 (use cases, architecture)

• O-RAN.WG1.Use-Cases-Analysis-Report-v05.00 o Update use case 6: Massive MIMO Beamforming Optimization (Section 3.6) considering stage 1 and stage 2 decisions O-RAN.WG1.Use-Cases-Detailed-Specification-v05.00 o Update use case 6: Massive MIMO Beamforming Optimization (Section 3.6) considering stage 1 and stage 2 decisions

# WG2 (Non-RT RIC, A1, R1) Impact

O-RAN.WG2.Use-Case-Requirements-v04.00 o Add new use case 6: Massive MIMO Beamforming Optimization based on agreements from prenormative phase   
O-RAN.WG2.Non-RT-RIC-ARCH-TS-v01.00.02 o No impact identified o O-RAN.WG2.R1.GAP-v01.00.00: o Specifying retrieval of data collected, e.g., from the RAN over O1 or from external sources, towards the rApps is required (Step 4 in Figure 3.2.2.1-1). o Specifying the means of transmitting a GoB BF configuration, resulting from the ML execution/inference, from the rApp to the SMO and further via O1 to the RAN nodes, is required (Step 9 in Figure 3.2.2.1-1). o Not mMIMO use case specific impact: o Specifying ML Model deployment is required (Step 6 in Figure 3.2.2.1-1). o Specifying the means of transmitting an optimization target (or equivalent) to the rApp (ML Inference stage in Figure 3.2.2.1-1). o Specifying ML Model performance monitoring roles and procedures is required (Steps 19 and 22 in Figure 3.2.2.1-1). o Specifying the means of a fallback mechanism in case of unsatisfying rApp performance is required (Steps 20 and 23 in Figure 3.2.2.1-1).

# WG4 (O-FH) Impact

# O-RAN.WG4.MP.0-v07.00.00

o No impact identified   
o Background Upload and download of files (Sections 9 and 5.3) Update of beamforming configuration files (Section 12.4) Activation and deactivation of affected carriers (o-ran-uplane-conf.yang) Activation of beamforming configuration by indicating the stored file (rpc commands in oran-beamforming.yang module e.g. activate-beamforming-config)

Notification of beamforming information update (beamforming-information-update in o-ranbeamforming.yang module)

• O-RAN-WG4.CUS.0-v07.00

No impact identified   
Background ▪ Predefined beams (uploaded via M-Plane) can be used if update is supported by O-RU Dynamic beamforming control option, see Section 5.4.2 using Information Elements • ExtType $^ { = 1 }$ Beamforming Weights Extension Type, ExtType $^ { = 2 }$ : Beamforming Attributes Extension Type, • ExtType ${ \bf \tau } = 1 1$ : Flexible Beamforming Weights Extension Type, ExtType $_ { = 1 9 }$ : Section Compact multiple port beamforming information. Weight-based dynamic beamforming (Section 10.4.2), attribute-based dynamic beamforming (Section 10.4.3) and channel-information-based beamforming (Section 10.4.4) is supported

# WG5 (O1) Impact

• O-RAN.WG5.O-CU-O1.0-v01.00 and O-RAN.WG5.MP.0-v02.00 o Input parameter for GoB optimization are:

forward UEs CSI measurement reporting reporting of channel covariance matrix (or any other compressed form of the information) new Performance Measurement counters for spatial distribution of estimated traffic density

o Impact depends on the selected option and

is very limited when such measurements are specified in 3GPP specifications (related P counter in 3GPP TS 28.552, CSI and channel covariance matrix in TS 37.320 etc.) and WG specs refer to 3GPP specifications or is moderate if such measurements are defined in O-RAN specifications

o Background

Performance assurance management (Section 6) is aligned with O-RAN.WG10.O1- Interface.0-v05.00   
File Management (Section 8) to transfer performance data files as well as notification files from O-CU-CP/O-CU-UP to SMO and vice versa.   
Provisioning Management (Section 9 in O-RAN.WG5.O-CU-O1.0-v01.00 or Section 10 in ORAN.WG5.MP.0-v02.00) to configure trace/performance metric jobs (3GPP TS 28.622)

# WG10 (SMO, O1) Impact

O-RAN.WG10.O1-Interface.0-v05.00 o No impact identified o Background □ Provisioning management services is used to create/modify/delete/read/notify Managed Object Instance (MOI); this means instantiating performance metric jobs and trace jobs (Section 2.1) depending on the options: • performance assurance management services (Section 2.3) collect performance measurement data trace management services collect measurements per UE (Trace, MDT, RCEF and RLF reporting) (Section 2.4)

Summary: Impact on O-RAN specification will be very limited in case the input parameters for GoB optimization are specified in 3GPP and moderate if specified in O-RAN. The Open Fronthaul specification already supports file-based upload and download of GoB beam pattern on O-FH M-Plane as well as dynamic beamforming on O-FH CUS-Plane.

# 3.2.4 Relation and Impact on 3GPP Specifications

# Relation to 3GPP Coverage and Capacity Optimization (CCO)

In Rel. 16, 3GPP carried out a study item on “RAN-centric data collection and utilization for LTE and NR” which resulted in several measurements to be supported for NR and being defined in 3GPP TS 28.552. In particular the use case “Capacity and Coverage Optimization” (CCO) related to GoB optimization was investigated and documented in the associated 3GPP TR 37.816. The study recommended the CCO function to be considered for normative specification. 3GPP RAN3 currently discusses CCO as part of the Rel.17 Work Item on “Enhancements of Data Collection for SON/MDT in NR”. While work is ongoing the following working assumptions have been made in 3GPP RAN3#113-e:

LTE CCO function should be considered as baseline for NG-RAN CCO solution for dynamic coverage changes with an index-based solution for coverage switching among deployment options.   
In NG-RAN scenario, a NG-RAN node may send to a neighbor NG-RAN node a coverage modification list which includes deployment related information concerning the serving cells.   
Xn signalling for coverage modification shall exchange at least the following information: NG-RAN CGI, Cell Coverage State, Cell Deployment Status Indicator and Cell Replacing Info in NG-RAN NODE CONFIGURATION UPDATE.   
DU signals to CU coverage related configuration information. Whether to include SSB beam information (on top of cell info) is FFS.   
CSI-RS based beam coverage tuning is an optimization and is not covered as part of NR CCO for Rel-17. DU makes the final decision on which coverage configuration to use.

# Impact on 3GPP Specification

Inter-gNB signalling (Xn)

3GPP TS 38.423 NG-RAN; Xn Application Protocol (XnAP) o Information about the Cell and SSB Beam Coverage State might be exchanged between gNB DUs to identify the SSB beam deployment configuration enabled by the respective gNB DU o Target 3GPP Rel.17

Intra-gNB signalling (F1)

3GPP TS 38.473 38.473 NG-RAN; F1 Application Protocol (F1AP) o A Coverage Modification Notification might be sent from gNB DU to gNB CU as part of a configuration update message in case of changes on the Cell and SSB Beam Coverage State o Target 3GPP Rel. 17

gNB measurements

• 3GPP TS 38.314 NR; Layer 2 measurements o The channel covariance matrix might be specified as new L2 measurement in RAN2.

gNB measurement reporting

3GPP TS 37.320 UTRA and E-UTRA and NG Radio Access; Radio measurement collection for Minimization   
of Drive Tests (MDT); Overall description; Stage 2 o The new UE specific measurement reporting (channel covariance matrix and CSI feedback reporting) might be specified in the MDT framework in RAN2   
3GPP TS 28.552 Management and orchestration; 5G performance measurements   
New PM counters (e.g. spatial distribution of estimated traffic density or histogram of covariance matrix) might   
be specified in SA5

Summary: The related changes to 3GPP specifications for Inter- and Intra-gNB signalling are not essential to support GoB optimization in O-RAN. The related enhancements to 3GPP specifications for $\mathrm { g N B }$ measurements and measurement reporting are essential to support GoB optimization in O-RAN.

# 3.2.5 Feasibility and Gain/Complexity Analysis

# Trial Results

Trail setup:

Product: AirScale MAA 64T64R n78 200W • Frequency band: $3 . 5 \ : \mathrm { G H z }$ • Standard: NR TDD ● Number of base stations: 1 Total output power: 200 W • Sector opening angle: $1 2 0 ^ { \circ }$ • Number of UEs: 1 and 20 • Scenarios: UEs stationary as well as drive tests with shopping street • Number of TX/RX paths: 64T / 64R • Number of CSI-RS ports: 8 • TRx configuration: $4 \mathrm { x } 8 \mathrm { x } 2$ array (4 columns, 8 rows, 2polarizations) • Channel type: actual channel in the field

Trial results:

Baseline configuration: 6 beams uniformly horizontally spread with $6 ^ { \circ }$ down tilt

![](images/370e020bdc51dbfd7f447aa038c15327b77cd9f679f6c31f59f4c33997ee9fb1.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.2.5.1-1.

Scenario: Single UE Drive Test

![](images/4da7cdb8d4cdee8e80b7956e8a66d0fc725e05a996dba81411d220cd30179d97.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.2.5.1-2.

Weighted RSRP measurements - Single UE Drive Test • Scenario: 20 UEs drive tests including shopping street

![](images/7f1da0f7b51bb15c47a08bec64792e289b59b4966105c7f3de0f9ceef4ec17f0.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.2.5.1-3.

![](images/dbb13972b650ea68587f57665b5a2cee20fd6b9c494ae0b33d878337dadfa70a.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.2.5.1-4.

Weighted RSRP measurements – 20 UEs drive tests including shopping street

![](images/6e3d9ecf4b316e666246f2c2a466609656f7ed1596be588cf404c2e19e9e60b3.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.2.5.1-5.

The ML based beam pattern optimization algorithm can adapt to the traffic distribution and hence provides a significant gain in terms of weighted downlink RSRP. Uplink throughput enhancements are also expected since SSB beams are used for uplink receive beamforming.

# 3.3 Solution 2: Beam-based Mobility Robustness Optimization (bMRO)

# 3.3.1 Problem Statement, Solution, and Value Proposition

Mobility Robustness Optimization is a well-known SON concept. First supporting measurements have been specified in LTE in Release 9. Its principle is to configure a number of parameters in the eNB that can delay or advance the HO procedure between two neighboring cells. The two parameters are 1. the cell individual offset (CIO) and 2. the time-totrigger (TTT). One CIO value is a reference signal received power offset specific to one neighbor cell, stored in the eNB. The TTT value is a time offset specific to one neighbor cell, stored in the eNB.

By changing the CIO and the TTT, the operator may solve the following problems:

1. Unbalanced traffic between neighboring cells.   
2. Low performance of cell edge users.   
3. Poor handover performance.

In particular, the prime use of optimizing the CIO and the TTT values is reducing the number of anomalous or problematic HO events between neighbor cells.

In a 5G mMIMO cell/gNB whose coverage is provided not by a single beam but by several beams which radiate in different directions. Thus, from the UEs point of view, the border between two neighbor cells is not a single border anymore but degenerates to several beam cell (or beam beam) borders, where the one beam is radiated by the source gNB and another beam is radiated from the target gNB. In this scenario, using a single CIO+TTT value pair on a cell cell basis will be suboptimal, as one beam cell (or beam beam) border might require a different CIO+TTT configuration for optimal HOs than another beam cell (or beam→beam) border.

This solution proposes to employ beam-specific CIO and TTT values between neighbor cells, e.g., instead of a single CIO+TTT value pair for the cell1 cell2 border, to employ a CIO $^ +$ TTT value pair for the SourceCell[Beam1] TargetCell and SourceCell[Beam2] TargetCell borders.

The value of this solution is that the number of anomalous and problematic HOs can be resolved on a beam cell basis, i.e., with much finer granularity than with the legacy SON cell cell solution.

# 3.3.2 Architecture/Deployment Options

# Option 1

The Near-RT RIC may host an xApp to optimize inter-cell beam mobility such as bMRO. In this case the Near-RT RIC might for instance configure beam individual offsets and the beam individual TTT for inter-cell mobility decisions. The learning and the inference of the parameters may be done on individual beam cell (or beam beam) borders or collectively on a group of beam cell borders, depending on the implementation. The optimization might follow an operator/SMO defined objective (e.g., minimize number/rate of TE HOs, TL HOs, or ping-pong HOs; optimize for certain beam cell borders; constrained optimization based on other objectives etc.), and so might be triggered by a new operator/SMO defined optimization target, detection of performance degradation, or a change in the radio environment (e.g., change in the mMIMO Beam Pattern).

@startuml   
skinparam ParticipantPadding 5   
skinparam BoxPadding 10   
skinparam defaultFontSize 12   
Autonumber   
Box “SMO” #gold Participant SMO as “Operator/SMO” Participant NON as “Non-RT RIC”   
end box   
Box “O-RAN” #lightpink Participant NearRTRIC as “Near-RT RIC” Participant ORANnodes as "E2 Nodes"   
End box   
group Data Collection ORANnodes -> NearRTRIC : $< < \mathrm { E } 2 > >$ KPI/PM report Hnote over NearRTRIC mMIMO Beam Pattern Information is available Endhnote   
end   
group AI/ML Flow SMO -> NearRTRIC: $< < 0 1 > >$ Initialize/Provide ML Model ORANnodes $- >$ NearRTRIC: <<E2>> KPI/PM report Hnote over NearRTRIC mMIMO Beam Pattern Information is available Endhnote NearRTRIC $- >$ NearRTRIC: AI/ML model training NearRTRIC -> NearRTRIC: AI/ML model inference   
end   
group Configuration Update group alt 1 Hnote over NearRTRIC mMIMO Beam Pattern Change Endhnote end group alt 2 SMO $- >$ NearRTRIC: <<O1>> Optimization Trigger:\nNew optimization target end group alt 3 NearRTRIC $- >$ NearRTRIC: Optimization Trigger:\nPerformance degradation end NearRTRIC $- >$ ORANnodes: <<E2>> Configure new mobility parameters   
end   
group Performance Monitoring ORANnodes $- >$ NearRTRIC: $< < \tt E 2 > >$ KPI/PM report NearRTRIC $- >$ NearRTRIC: Performance monitoring and evaluation NearRTRIC $- >$ NearRTRIC: Fallback configuration (O) NearRTRIC $- >$ NearRTRIC: Model retraining and update   
end   
@enduml

![](images/d80be66810203a9e8b2fc41a7d3f9ad2c77352958bf69e8c4f684954606b2238.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.3.2.1-1. bMRO solution diagram

One of the necessary inputs for training and inference of the bMRO function is the (current) mMIMO Beam Pattern that is determined externally (in the SMO, in the Non-RT RIC, in the E2 Nodes, or in the Near-RT RIC by another function). The relevant mMIMO Beam Pattern Information must be available at the Near-RT RIC bMRO function both for training and inference. Depending on implementation, this can be achieved by transmission from the SMO (over O1), or by transmission from the E2 Nodes (over E2), or by combined transmission from the SMO and the E2 Nodes, or by communication between two Near-RT RIC functions. Moreover, depending on how the relevant mMIMO Beam Pattern Information is configured/determined, the necessary information may be transmitted separately and asynchronously (e.g., SMO transmits a list of mMIMO Beam Patterns for the next time period(s), while the E2 Nodes transmit the exact times of the mMIMO Beam Pattern changes and indicate the IDs of the mMIMO Beam Patterns in the list).

# Requirements

Table 3.3.2.1-1.   

<table><tr><td rowspan=1 colspan=6>Input Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source     →Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod*</td><td rowspan=1 colspan=1>(Target) Specification</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>O-CU → Near-RT RIC</td><td rowspan=1 colspan=1>Number of too early HOs from agiven beam to a given neighbor cell</td><td rowspan=1 colspan=1>count</td><td rowspan=1 colspan=1>~1 min</td><td rowspan=1 colspan=1>3GPP TS 28.552(Sec. 5.1.1.25)</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>O-CU → Near-RT RIC</td><td rowspan=1 colspan=1>Number of too late HOs from a givenbeam to a given neighbor cell</td><td rowspan=1 colspan=1>count</td><td rowspan=1 colspan=1>~1 min</td><td rowspan=1 colspan=1>3GPP TS 28.552(Sec. 5.1.1.25)</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>O-CU → Near-RT RIC</td><td rowspan=1 colspan=1>Number of attempted HOs from agiven beam to a given neighbor cell</td><td rowspan=1 colspan=1>count</td><td rowspan=1 colspan=1>~1 min</td><td rowspan=1 colspan=1>3GPP TS 28.552(Sec. 5.1.1.25)</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>O-CU → Near-RT RIC</td><td rowspan=1 colspan=1>Number of successful HOs from agiven beam to a given neighbor cell</td><td rowspan=1 colspan=1>count</td><td rowspan=1 colspan=1>~1 min</td><td rowspan=1 colspan=1>3GPP TS 28.552(Sec. 5.1.1.25)</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>O-CU → Near-RT RIC</td><td rowspan=1 colspan=1>Number of failed HOs from a givenbeam to a given neighbor cell</td><td rowspan=1 colspan=1>count</td><td rowspan=1 colspan=1>~1 min</td><td rowspan=1 colspan=1>3GPP TS 28.552(Sec. 5.1.1.25)</td></tr></table>

Table 3.3.2.1-2.   

<table><tr><td rowspan=1 colspan=6>Output Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source    →Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>Config.Period*</td><td rowspan=1 colspan=1>(Target) Specification</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>Near-RTRIC→O-CU</td><td rowspan=1 colspan=1>CIO for a given beam to a givenneighbor cell</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>trigger-based ≥ 1min</td><td rowspan=1 colspan=1>3GPP TS 38.331(Sec. 5.3.5, Sec. 5.5.4)</td></tr></table>

\*The period represents the baseline assumption for the gain/complexity analysis in this document. Faster reporting and reconfiguration periods or even different input data over $E 2$ for faster Near-RT RIC control loops are not excluded for the normative phase if seen beneficial.

1) SMO & Non-RT RIC

a) Trigger bMRO configuration. (O)   
b) Send bMRO configuration target to Near-RT RIC.   
c) Send mMIMO Beam Pattern related information (Beam Pattern configuration, Beam Pattern configuration list, Beam Pattern configuration switch timing/condition, Beam Pattern identifier etc.) to the Near-RT RIC. d) Trigger initiation of bMRO AI/ML Model training.   
e) Non-RT RIC   
f) Transfer the appropriate bMRO ML model to the Near-RT RIC over O1/O2.

2) Near-RT RIC

a) Retrieve necessary configurations, performance indicators, measurement reports and other data from E2 nodes for the purpose of training of relevant AI/ML models. Retrieve ML Models from the Non-RT RIC over O1/O2.   
b) Train the relevant AI/ML model using the collected data. FFS: Perform offline training of relevant AI/ML models.   
c) Use the trained AI/ML models to infer the correlation between the Grid-of-Beam configuration, handover, and beam failure statistics of multiple cells and beams, and to predict the optimal configuration of mobility parameters (e.g., beam individual offsets for beam mobility) for each cell/beam pair optionally according to a global optimization objective designed by the operator and retrieved from the SMO.   
d) Send the optimal per beam mobility parameter configurations to E2 nodes.   
e) Monitor the performance of the AI/ML model based on configurations, performance indicators, and measurement reports received from the RAN.   
f) Retrain the AI/ML model and re-optimize the beam mobility configurations based on the monitored performance and/or based on a switch of the Grid-of-Beam configuration.   
g) Execute the control loop periodically or event-triggered.   
h) Retrieve mMIMO Beam Pattern related information from the SMO.

3) E2 nodes

a) Collect and report to Near-RT RIC KPIs related to Grid-of-Beam configuration, handover and beam failure statistics.   
b) Apply L3 beam mobility parameter configuration following Near-RT RIC configuration.   
c) Send mMIMO Beam Pattern related information to the Near-RT RIC.

# Option 2

The bMRO optimization algorithm might also be hosted in Non-RT RIC. Same principles apply, whereas KPI reporting and configuration management over O1 interface will be used.

# 3.3.3 Impact Analysis on O-RAN Working Groups

Editor’s note: This is an initial impact analysis as part of the WG1 UCTG work on mMIMO. The intention is to estimate the expected standardization effort within the O-RAN working groups. It is up to the WGs to decide how the mMIMO functionality should be specified in specifications of each WG.

WG1 (use cases, architecture) Impact

O-RAN.WG1.Use-Cases-Analysis-Report-v05.00 o Update use case 6: Massive MIMO Beamforming Optimization (Section 3.6) considering stage 1 and stage 2 decisions   
O-RAN.WG1.Use-Cases-Detailed-Specification-v05.00

o Update use case 6: Massive MIMO Beamforming Optimization (Section 3.6) considering stage 1 and stage 2 decisions

WG2 (Non-RT RIC, A1) Impact O-RAN.WG2.Use-Case-Requirements-v04.00 o If seen as beneficial, add new use case 6: Massive MIMO Beamforming Optimization based on agreements from pre-normative phase O-RAN.WG2.AIML-v01.03 o Depending on implementation, add a deployment scenario involving offline training in the Near-RT RIC.   
WG3 (Near-RT RIC, E2) Impact • O-RAN.WG3.UCR-v01.00 o Add new use case 6: Massive MIMO Beamforming Optimization based on agreements from prenormative phase O-RAN.WG3.RICARCH-v02.00 o No impact identified o Background information ▪ bMRO is an xApp running in the Near-RT RIC bMRO is using Near-RT RIC services REPORT and POLICY and uses the E2 interface to a) get KPI/PM reports from the E2 Node and b) configure beam-based cell individual offsets as policy in the E2 Node. O-RAN.WG3.E2GAP-v02.00 o No impact identified o Background information bMRO xApp uses the E2 interface to a) get KPI/PM reports from the E2 Node and b) configure beam-based cell individual offsets as policy in the E2 Node. The following services of the E2 interface are used: 1. E2 KPI/PM report (Figure 3.3.2.1-1: step 3, step 9) using Near-RT RIC REPORT Service 2. E2 Configure new mobility parameters (Figure 3.3.2.1-1: step 8) using Near-RT RIC POLICY Service O-RAN.WG3.E2AP-v02.00 o No impact identified o Background information □ The following services of the E2 interface are used: 3. E2 KPI/PM report (Figure 3.3.2.1-1: step 3, step 9) using Near-RT RIC REPORT Service 4. E2 Configure new mobility parameters (Figure 3.3.2.1-1: step 8) using Near-RT RIC POLICY Service O-RAN.WG3.E2SM-RC-v01.01.00 or NEW: O-RAN.WG3.E2SM-CC Add RAN POLICY service “Mobility Robustness Optimization” with Policy Approach “Offset” to E2SM-RC (modify E2SM-RC to support cell specific signaling) or add this policy to a new Cell level/E2 Node level Control (i.e. E2SM-CC) O-RAN.WG3.E2SM-KPM-v02.00 o No direct impact identified ▪ Assuming the new measurements will be specified in 3GPP TS 28.552 Dependency on completion of bMRO functionality in 3GPP Rel.17 o Background ▪ The E2 Node (O-CU-CP) shall host the RAN Function “KPM Monitor”   
WG5 (O1) Impact   
Assuming data model (provisioning management) will be enhanced with beam individual offsets in 3GPP TS 28.541 (according to cellIndividualOffset in module _3gpp-nr-nrmnrcellrelation.yang)   
□ Assuming performance measurements in 3GPP TS 28.552 are enhanced to consider HO failures TooEarly, Too Late and ToWrongCell per beam;   
Assuming information about assignment of UE to beam is available at CU (using UE context messages specified in 3GPP TS 38.473 to indicate)

o Dependency in completion of bMRO functionality in 3GPP Rel.17 o Background

Performance management (Section 6) is aligned with O-RAN.WG10.O1-Interface.0-v05.00 File Management (Section 8) to transfer configuration files as well as performance data files and notification log files. Provisioning Management (Section 9 in O RAN.WG5.O-CU-O1.0-v01.00 and ORAN.WG5.MP.0-v02.00 or Section 10 in O-RAN.WG5.MP.0-v02.00) to transmit trigger, to configure beam individual offsets and to configure performance metric jobs (3GPP TS 28.622).

# WG10 (SMO, O1) Impact

O-RAN.WG10.O1-Interface.0-v05.00 o No impact identified o Background ▪ Provisioning management services (Section 2.1) allow configuration changes using NETCONF (TS 28.532, TS 28.541) Performance assurance management services (Section 2.3) collect performance measurement data for file reporting (File management services explained in Section 2.5) or data streaming

Summary: The impact on O-RAN specification is quite limited, assuming bMRO related KPIs are specified in 3GPP SA5. Work in O-RAN WGs can be minimized by referring to 3GPP specification as done today, e.g., E2SM-KPM, O RAN.WG5.O-CU-O1, O-RAN.WG10.O1.

# 3.3.4 Relation and Impact on 3GPP Specification

# 3GPP Mobility Robustness Optimization

LTE MRO is a well-known SON method that optimizes the mobility parameters and thereby minimizes the mobility related failures as well as unnecessary handovers (HOs). First the following radio link or handover failure causes are identified:

1. Too late handovers (TL)   
2. Too early handovers (TE)   
3. Handover to wrong cell   
4. Ping-pong (PP) handovers

For this purpose, eNBs and UEs evaluate radio link or handover failure related information. UEs might provide respective information after radio link re-establishment and neighbour eNBs might exchange respective failure indications.

SON MRO was first standardized in LTE Rel.9:

3GPP TS 36.902 E-UTRAN; SON Use Cases and Solutions 3GPP TS 36.300 E-UTRAN; Overall description stage 2 3GPP TS 36.423 E-UTRAN; X2 Application Protocol (X2AP) o New X2-AP procedures: Radio Link Failure Indication o New X2-AP procedure: Handover Report Indication 3GPP TS 36.331 E-UTRA; Radio Resource Control (RRC) o RLF report indication (UE assistance signalling for root cause analysis)

• 3GPP TS 32.425 Performance Management (PM); Performance measurements E-UTRAN o KPIs for Too-Late HOs (TL), Too-Early HOs (TE), HO to wrong cell, Ping-pong (PP) 3GPP TS 28.658 E-UTRAN Network Resource Model (NRM) Integration Reference Point (IRP); Information Service (IS) o Configuration management of MRO Cell Individual Offsets (CIO)

LTE Rel.10 specified that RLF Report will also be available after UE went to Idle mode (Re-establishment was not successful). LTE Rel.11 supports signalling between base stations for Inter-RAT support.

MRO functionality was added to NR and NG-RAN in Rel.16:

3GPP TS 38.300 E-UTRAN; Overall description stage 2   
3GPP TS 38.423 NG-RAN; Xn Application Protocol (XnAP)   
3GPP TS 38.331 NR; Radio Resource Control (RRC)   
3GPP TS 28.552 Management and orchestration; 5G performance measurements o KPIs for Too-Late HOs (TL), Too-Early HOs (TE), HO to wrong cell, Ping-pong (PP)   
3GPP TS 28.541 Management and orchestration; 5G Network Resource Model (NRM); Stage 2 and stage 3 o Configuration management of MRO Cell Individual Offsets (CIO)

NR and NG-RAN MRO includes connection failure due to intra-system as well as inter-system mobility, inter-system unnecessary HO as well as inter-system ping-pong handover.

Overall, LTE and NR MRO are essential mobility features that can reduce dominating radio link failures, make handover more robust and also reduce handover ping-pong effects by adapting cell individual offsets. 3GPP is also working to extent the concept to support mMIMO with beam-based approaches for MRO.

# Impact of bMRO on 3GPP Specification

gNB reporting

• 3GPP TS 28.552 Management and orchestration; 5G performance measurements o Beam-based KPIs for Too-Late HOs (TL), Too-Early HOs (TE), HO to wrong cell o CR S5-214485 submitted to 3GPP SA5 at 3GPP TSG-SA5 Meeting #138-e meeting, 23rd Aug 2021 - 31st Aug 2021; Conclusion: noted o CR S5-215326 submitted to 3GPP SA5 at 3GPP TSG-SA5 Meeting #139-e meeting, 11th Oct 2021 – 20th Oct 2021 o Target 3GPP Rel.17

3GPP TS 28.313 Management and orchestration; Self-Organizing Networks (SON) for 5G networks o Add beam based KPIs for too early handover failures, too late handover failures, handover failures to wrong cell o Target 3GPP Rel. 17

gNB configuration

3GPP TS 28.541 Management and orchestration; 5G Network Resource Model (NRM); Stage 2 and stage 3 o Beam-based configuration management of MRO Cell Individual Offsets (CIO) o CR S5-215328 (stage 2) and CR S5-215348 (stage 3) submitted to 3GPP SA5 at 3GPP TSG-SA5 Meeting #139-e meeting, 11th Oct 2021 – 20th Oct o Target 3GPP Rel.17

UE configuration and reporting

3GPP TS 38.331 NR; Radio Resource Control (RRC) protocol specification o Add UE configuration of beam-based individual offsets for MRO $\bigcirc$ Add UE reporting of last serving beam in the RLF report $\bigcirc$ CR on 3GPP TS 38.331 should be submitted to 3GPP RAN2

Intra-gNB signalling (F1)

3GPP TS 38.473 NG-RAN; F1 Application Protocol (F1AP)

o Signalling needed on F1AP to support the per-beam mobility setting change   
o TDoc 3GPP R3-213388 “Consideration on the CU-DU impacts of the per-beam mobility setting change” submitted to 3GPP TSG-RAN WG3 Meeting #113-e meeting, 16th – 27th August 2021   
o CR 3GPP R3-213389 “Enabling CU-DU information exchange to support per-beam mobility setting change” submitted to 3GPP TSG-RAN WG3 Meeting #113-e meeting, 16th – 27th August 2021   
o Target 3GPP Rel. 17

Summary: The related changes to 3GPP specifications for gNB reporting, gNB configuration and intra-gNB signalling are essential to support bMRO optimization in O-RAN. First CRs to 3GPP SA5 and RAN3 have been submitted as part of 3GPP Rel.17 and are currently being revised. Completion of bMRO in O-RAN can only take place after completion of bMRO in 3GPP, which should be considered in the mMIMO feature plan.

The related changes to 3GPP specifications for UE configuration and UE reporting are not essential to support bMRO optimization in O-RAN. Contribution to 3GPP RAN2 is still open and under discussion.

# 3.3.5 Feasibility and Gain/Complexity Analysis

# Simulation Results

Simulation setup:

7 site hexagonal grid scenario (3GPP TR38.901 Urban Micro, ISD=200m)   
center frequency: 28 GHz (FR2), bandwidth: $1 0 0 \mathrm { M H z }$   
16x8 antennas   
$8 { + } 4$ beams (8 narrow beams with lower down tilt, 4 broader beams with higher down tilt)   
4 simultaneous beams (maximum number of active beams for transmission within a cell used for spatial   
multiplexing)   
BS height: $1 0 \mathrm { m }$ , mechanical tilt: $9 ^ { \circ }$   
SSB beams with 15MHz bandwidth   
KPI period: 30 seconds   
Number of UEs: 630 UEs total (210 slow UEs + 420 street UEs)   
Traffic: full buffer

![](images/017e365c8f70398debb03377eadcdde0aec687646787bdd3599e7ea9e806c9a6.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.3.5.1-1.

A3 Trigger with $8 0 \mathrm { m s }$ TTT (time-to-trigger) and 2dB total offset, 60 ms L3 filtering

Simulation Results:

3 KPI periods $= 9 0$ s Reduction of the number of TE (too early) HOs and TL (too late) HOs:

![](images/7f066212f4bc95d04be630a020fd9fa91c27cc5cdd859c116834b2aa447f9184.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.3.5.1-2.

The beam-based MRO can reduce the number of total network TL failures by $9 0 \%$ compared to the baseline (no MRO) and by $5 8 \%$ compared to legacy MRO (left graph). The beam-based MRO can reduce the total number of network TE failures by $5 7 \%$ compared to the baseline and by $2 3 \%$ compared to legacy MRO (right graph).

• Reduction of total network outage rate and failures:

![](images/734a25662e36493e35f334061ea7cb8757eb535af59ae88295b04de63f41eadd.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.3.5.1-3.

The beam-based MRO can reduce the outage rate by $4 4 \%$ compared to the baseline and $1 7 \%$ compared to legacy MRO (left graph). The beam-based MRO can reduce the total network failure by $8 2 \%$ compared to the baseline and by $3 4 \%$ compared to legacy MRO (right graph).

Reduction of the rate of network ping-pong (PP) failures:

![](images/e0b34ac22620e51f2741a9f6fa1689c53919cebc55b4eabe383e14556f41c4c8.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.3.5.1-4.

The beam-based MRO can reduce the rate of PP handovers by $1 8 \%$ compared to the baseline and by $4 6 \%$ compared to legacy MRO (left graph). As the result of the reduction in the rate of PP handovers, the total frequency of HOs can be reduced by $1 5 \%$ compared to the baseline and by $1 3 \%$ compared to legacy MRO (right graph).

# Complexity Analysis

Analysis is provided relative the legacy LTE MRO implementation.

The computational complexity as well as the signalling overhead (reporting from the E2 Node (O-CU) as well as configuration towards the E2 Node (O-CU)) increases as follows:

Computational complexity: Ο([No. of beams] $x$ [MRO complexity]) Increase of signaling: Ο([No. of beams] x [MRO signalling])

The computational complexity may be reduced by enhanced proprietary implementations, e.g., forming virtual groups of beams with similar characteristics, e.g., neighbor beams covering the same street or area. With such an implementation the computational complexity can be reduced to:

Computational complexity: Ο([No. of beam groups] x [MRO complexity]) Increase of signaling: Ο([No. of beam groups] x [MRO signalling])

Overall computational complexity seems reasonable since the time frequency of inter-cell handover events is relatively low and even decreases with the introduction of beam-based MRO. Similarly, the necessary signaling frequency (KPI reporting as well as configuration of Cell Individual Offsets) is rather low, e.g., in the range of seconds in the worst case.

# 3.4 Solution 3: AI/ML Based Initial Access (SS Burst Set), CSI-RS and DMRS Configuration Optimization

3.4.1 Problem Statement and Value Proposition

3GPP NR based wireless cellular networks promises to provide leaner system design compared to its predecessors in a bid to improve spectral efficiency, power consumption performance and reduce interferences. Ultra-lean design aims to minimize “always on” reference signal transmissions in the downlink. Impact is more on Massive MIMO (mMIMO) system and networks where gNB/TRP should transmit downlink reference signals only when necessary. List of “always on” reference signals include synchronization signals (SS Burst Sets), CSI-RS TRS, CSI-RS Acquisition, DMRS and system broadcast information. Subsequent sections present AI/ML based optimization problem description with SS Burst Set configuration optimization which operates in slowest control loop (Non-RT RIC Control Loop) of the O-RAN architecture. Gradually problem statement is extended to CSI-RS and DMRS configuration optimizations operating in Near-RT RIC and O-DU control loops.

In beamformed Massive MIMO systems, initial access (IA) and time frequency tracking (TA) mechanisms require transmission of “Always On” signals SS Burst Sets periodically followed by CSI-RS TRS in the remaining part of the frame stricture. During initial access process, the UE detects a preferred SS/PBCH beam at preferred receive beam. UEs with beam correspondence support can use the same receive beam to transmit PRACH after receiving SIB1 on the scheduled SS/PBCH time-frequency grids. When beam correspondence is not supported, the UE repeats PRACH transmissions in different directions and then listen for the network response using the same beam used to detect the SS/PBCH. From the initial access procedure, a default beam pair is established. After SS burst based synchronization, the UE can start synchronizing with gNB/TRP using SS Block configuration dependent CSI-RS signals.

In large scale NR networks with thousands of gNB/TRPs deployed, system configurations derived manually using heuristic methodologies will directly impact the following aspects.

a) High power consumptions in both network and UEs leading increased network CAPX and reduced UE battery life respectively and b) Degraded utilization of time-frequency resources affecting e2e spectral efficiency of the system.

Issue is compounded by increase in IA latency and non-satisfactory reactive tracking performance KPI reports due to non-optimal configuration setting of large number of parameters available for SS bursts and CSI-RS TRS configuration supported in NR. UE could observe degraded tracking performances (and related other network KPIs) without appropriate CSI-RS planning. These are important network design aspects for massive MIMO systems with large carrier bandwidth and systems with carrier aggregation support where multiple BWPs are active with multiple time-frequency resource allocations for IA and TA reference signal transmissions. Typically, operators rely on skilled in the art manpower to suggest network wide configuration set which is prone to be sub-optimal. In addition to the demography, time dependent network usage parents have strong influence on designing optimal configuration sets which can lead to spectral and power efficient network design.

We propose AI/ML assisted network-wide (multi-gNB/TRP) optimization framework wherein AI/ML agent/engine can infer optimal SS Burst Set, CSI-RS TRS configurations per gNB/TRP based on multiple time, location, and usage dependent observations which are already available at different nodes of the NR access and core network elements {E2 Nodes (O-DUs, O-CUs), O-RU, SMO}. Optimizer capability can be extended to derive configurations other reference signals configurations including UE specific CSI-RS acquisition, and DMRS as well with additional observations or training data for the AI/ML agent/engine. Joint optimizations are also definite possibility which can be considered as extension of the use cases mentioned in this document. One example is jointly optimizing SSB and CSI-RS for faster beam acquisition operation in mmWave FR2 system.

At high-level goal of this class of optimization problem (involving SS Burst Set, CSI-RS, and DMRS) is to minimize reference signal transmissions based on 3GPP supported configuration/reconfigurations options available subject to constraints given below (not an exhaustive list):

a) Target KPIs (like IA latency, TA estimation accuracy, reactiveness, channel estimation accuracy etc.) within the working limit suggested by the operator.   
b) Mobility and HO KPIs targets (operator inputs) which could be different in different parts of the network.   
c) Enable faster/reduced set beam search in connected mode improving RLF performance.   
d) Optimal CSI-RS and DMRS density for target parameter estimation accuracy (e.g., Mean Square Error metric).

In the architecture/deployment options section, SS Burst Set optimization is used for Non-RT RIC framework and NearRT RIC deployment framework is used for CSI-RS and DMRS configuration optimizations.

# 3.4.2 Architecture/Deployment Options

# Option 1a: Non-RT RIC Based Training and Deployment (SS Burst Set Configuration Optimization)

In this class of architecture/deployment option, raw training data gathering, pre-processing them to generate AI/ML model training data, offline AI/ML model training and deployment are performed in the SMO/Non-Real Time RIC entity. Raw training data set are collected from the $\mathrm { T R P / g N B }$ or cluster of deployed TRP/gNBs which constitute the large-scale network deployment. By default, heterogeneous deployment is assumed supporting various slow time varying usage patterns in different parts of the network.

Offline trained AI/ML agent/engine will allow operator to deploy it in Non-RT-RIC (if necessary, in Near-Real Time RIC). AI/ML Agents can derive optimal per gNB/TRP configurations statically or semi-statically trigged by operator requirements or KPIs observations from the NR E2 nodes. It is expected that AI/ML engine/agent will generate same/similar inferences for a set of gNB/TRPs which are deployed at the same geographical neighbours having similar usage pattern (example set of gNB/TRPs deployed to support a busy street with moderate mobility).

SMO needs to collect required observations sets over different observation time windows to generate required training data set which necessitates O1, E2 and FH interface capability enhancements. Interface capabilities can be made scalable future requirements to support any additional observations required over O1 and E2 interfaces which can help in faster convergence of AI/ML agent/engine.

@startuml   
skinparam defaultFontSize 12   
Box "Personnel" #lightblue Actor "Operator" as OPERATOR   
End box   
Box "Service Management and Orchestration" #gold Participant "Data Collection and Control & Non-RT RIC" as SMO Participant "rAPP" as NRTRIC   
End box   
Box "O-RAN Nodes" #lightpink Participant "E2-Nodes(O-CUs & O-DUs)" as E2NODES Participant "O-RUs" as ORUs   
End box   
group Data Collection and Pre-Processing ORUs -> E2NODES : <<FH>> Observation, Mesaurement Data Collection E2NODES $- >$ SMO : $< < 0 1 > >$ Observation, Mesaurement Collection OPERATOR $- >$ SMO : Performance KPI Targets Inputs SMO $- >$ SMO : Data Pre-Processing and AI/ML Training Data Generation   
end   
group AI/ML Engine/Agent Training SMO -> SMO : AI/ML Engine/Agent Training   
end   
group Model Deployment and Inference Generation   
group Operator-Initiated SMO $- >$ NRTRIC : $< < \mathbb { R } 1 > >$ Model Deployment OPERATOR $- >$ SMO : KPI Targets/Deployment Updates SMO $- >$ NRTRIC : $< < \mathbb { R } 1 > >$ Model Data   
end   
group System Initiated SMO -> NRTRIC : $< < \mathrm { R 1 } > >$ PI Degradation & Alarms   
end SMO -> E2NODES : $< < 0 1 > >$ Measurement, Report Configuration E2NODES $- >$ SMO : <<O1>> Observation, Mesaurement Collection SMO -> NRTRIC : <<R1>> Model Data NRTRIC $- >$ NRTRIC : AI/ML Agent/Engine Inference NRTRIC $- >$ SMO : $< < \mathbb { R } 1 > >$ Updated Optimal Configs SMO -> E2NODES : <<O1>>Updated E2 Nodes Configurations E2NODES $- >$ ORUs : <<FH>> Updated O-RU Configurations   
end   
group ML Agent Performance Monitoring ORUs -> E2NODES : <<FH>> Data Collection E2NODES $- >$ SMO : KPIs, Measurment Report, Observations SMO $- >$ SMO : Performance Evaluation & Fallback Config Decision SMO -> E2NODES : $< < 0 1 > >$ Default/Fallback mMIMO Configuration E2NODES $- >$ SMO : $< < 0 1 > >$ Observation, Mesaurement Collection SMO $- >$ SMO : AI/ML Agent/Engine Re-Training Trigger   
end   
@enduml

![](images/222c26caed13daed9077f9b64274f92d5b0673806d968f4b7ec46a409c72ff18.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.4.2.1-1. Flow diagram for SS Burst Set Configuration Optimization

# Requirements for SS Burst Set Configuration Optimization

Required Observations for Training Data Set Generation

Initialization:

Table 3.4.2.1-1.   

<table><tr><td rowspan=1 colspan=6>Input/Output Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source     →Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod,granularity</td><td rowspan=1 colspan=1>New or existing config</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>O-DU → Non-RT RIC</td><td rowspan=1 colspan=1>Supported SSB and CSI-RSTRSconfigurations per cell</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>Initialization</td><td rowspan=1 colspan=1>3GPP TS38.331</td></tr><tr><td rowspan=1 colspan=1>M-Planevia SMO</td><td rowspan=1 colspan=1>O-RU → Non-RT RIC</td><td rowspan=1 colspan=1>Supported common beam configurationfrom O-RU per cell</td><td rowspan=1 colspan=1>File</td><td rowspan=1 colspan=1>Initialization</td><td rowspan=1 colspan=1>ExistingO-RAN.WG5.MPChapter 8</td></tr><tr><td rowspan=1 colspan=1>Open FHM-Plane</td><td rowspan=1 colspan=1>O-RU→ 0-DU</td><td rowspan=1 colspan=1>Beamforming weights or attributesvia YANG module per cell</td><td rowspan=1 colspan=1>valuesin IE</td><td rowspan=1 colspan=1>Initialization</td><td rowspan=1 colspan=1>O-RAN.WG4.MPSection 12.4.2</td></tr><tr><td rowspan=1 colspan=1>Open FHM-Plane</td><td rowspan=1 colspan=1>SMO → 0-RU; O-DU →O-RU</td><td rowspan=1 colspan=1>Inferred SSB beam configuration inspecified file per cell</td><td rowspan=1 colspan=1>file</td><td rowspan=1 colspan=1>Initialization</td><td rowspan=1 colspan=1>O-RAN.WG4.MPSection 12.4.2</td></tr><tr><td rowspan=1 colspan=1>Open FHCUS-Plane</td><td rowspan=1 colspan=1>O-DU→0-RU</td><td rowspan=1 colspan=1>SSB beam attributes per cell</td><td rowspan=1 colspan=1>valuesinIE</td><td rowspan=1 colspan=1>Initialization</td><td rowspan=1 colspan=1>O-RAN-WG4.CUSSection 5.4.2</td></tr><tr><td rowspan=1 colspan=1>OperatorIF   toSMO</td><td rowspan=1 colspan=1>SMO → Non-RT RIC</td><td rowspan=1 colspan=1>Maximum Initial Access Latencyfor given SSB Beam Configuration</td><td rowspan=1 colspan=1>ms</td><td rowspan=1 colspan=1>Initialization</td><td rowspan=1 colspan=1>KPI metric input by theoperatorNew KPI</td></tr></table>

Measurements/reports from E2 Nodes over O1 interface (AI/ML model training phase):

<table><tr><td rowspan=1 colspan=6>Input Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source      →Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod,granularity</td><td rowspan=1 colspan=1>New   or    existingmeasurement,Existing Specification(Section)</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>O-DU→ Non-RT RIC</td><td rowspan=1 colspan=1>SS reference signal received power(SS-RSRP) per UE</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>(nonreal-time,reportedeveryTwin*timewindow)</td><td rowspan=1 colspan=1>3GPP TS 38.215(Sec. 5.1.1)New reporting</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>O-DU → Non-RT RIC</td><td rowspan=1 colspan=1>CSI reference signal received power(CSI-RSRP) per UE</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>(nonreal-time,reportedeveryTwin * timewindow)</td><td rowspan=1 colspan=1>3GPP TS 38.215(Sec. 5.1.25)New reporting</td></tr></table>

Table 3.4.2.1-2.   

<table><tr><td>01 SMO</td><td>via</td><td>O-DU → Non- RT RIC</td><td>UL SRS RSRP measurement per UE</td><td>dBm</td><td>(non real- time, reported every Twin* time window)</td><td>3GPP TS 38.215 (Sec. 5.2.5) New reporting</td><td></td></tr><tr><td>01 SMO</td><td>via</td><td>O-CU → Non- RT RIC</td><td>Number of active UEs in NG-RAN (Number of RRC_CONECTED UEs) per cell</td><td>Integer</td><td>(non time, measured every</td><td>real- and reported Twin * time</td><td>3GPP TS28.552 Sections: 5.1.1.23 &amp; A.60 3GPP TS28.552 A.7</td></tr><tr><td>01 SMO</td><td>via</td><td>O-CU → Non- RT RIC</td><td>Cell Specific Offsets (HO) defined within measObjectNR per neighbor cell</td><td></td><td>(non real- time, reported every</td><td>Twin* time window)</td><td>3GPP TS 28.331 (Sec.5.3.4) New Reporting</td></tr><tr><td>01 SMO</td><td>via</td><td>O-DU → Non- RT RIC</td><td>PRACH correlation power for every received PRACH corresponding to each active SSB Beam Index</td><td></td><td>Non time, every reported in</td><td>real- for SSB Beam Index Twin * time window</td><td>New Measurement (Could be derived measurement at O-DU (derived based on the existing RA-report defined in RAN2, can standardized in SA5) New Reporting</td></tr><tr><td>01 SMO</td><td>via</td><td>O-DU → Non- RT RIC</td><td>Received PRACH instance number and corresponding receive beam index</td><td></td><td>Non time, every</td><td>real- for SSB Beam Index reported in T in * time window</td><td>3GPP TS 28.552-h40, subclause 5.1.1.20/ TS 38.314-g40, subclause 4.2.1.1 New Reporting</td></tr><tr><td>01 SMO</td><td>via</td><td>O-CU → Non- RT RIC</td><td>Network accessibility KPI per cell</td><td>Integer</td><td>Non time, reported every</td><td>real- Twin * time</td><td>3GPP TS 28.554 Section 6.2</td></tr><tr><td>01 SMO</td><td>via O-CU</td><td>→ Non- RT RIC</td><td>DL/UL throughput/spectral efficiency per slice</td><td>Float (kbit/se c)</td><td>Non time, reported every</td><td>Twin * time window</td><td>3GPP TS 28.554 Section 6.3.2 and section 6.3.3</td></tr></table>

Measurements/reports from E2 Nodes (inference phase):

Table 3.4.2.1-3.   

<table><tr><td rowspan=1 colspan=6>Input Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source      →Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod,granularity</td><td rowspan=1 colspan=1>New   or   existingmeasurement,Existing Specification(Section)</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>O-DU → Near-RT RIC</td><td rowspan=1 colspan=1>PRACH correlation power for everyreceived PRACH corresponding toeach active SSB Beam Index</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>ReportedeveryTwin-R  *timewindow</td><td rowspan=1 colspan=1>New Measurement(Could  be   derivedmeasurementatO-DU(derived basedon theexisting RA-report definedin RAN2,  can bestandardized in SA5)New Reporting</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>O-DU → Near-RT RIC</td><td rowspan=1 colspan=1>Received PRACH instance numberand corresponding beam index</td><td rowspan=1 colspan=1>Integer</td><td rowspan=1 colspan=1>ReportedeveryT inR *timewindow</td><td rowspan=1 colspan=1>3GPP TS 28.552-h40,subclause5.1.1.20/TS38.314-g40,   subclause4.2.1.1</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>O-CU → Non-RT RIC</td><td rowspan=1 colspan=1>Number of active UEs (mean, max)in   NG-RAN   (Number   ofRRC_CONECTED  UEs)  perdirection per cell</td><td rowspan=1 colspan=1>Integer</td><td rowspan=1 colspan=1>ReportedeveryTwin-R *timewindow</td><td rowspan=1 colspan=1>3GPP TS28.552Sections5.1.1.23&amp;A.60</td></tr></table>

${ \stackrel { * } { \mathop { \mathbf { T } } } _ { W i n } }$ is the predefined observation time window for offline training data collection.

$^ { * } T _ { W i n - R }$ is the predefined observation widow during inference generation, typically $T _ { W i n - R } \ \leq \ T _ { W i n }$

In addition to these observations and KPIs, Data Collection and Control Unit is expected to have access to the cell site deployment, configuration information and site-specific information for example gNB/TRP density, terrain type. A set of predefined algorithmic steps will take these raw observations as inputs and generate required training data set in prescribed format for the AI/ML engine/agent. AI/ML model will generate optimal SS Burst Set configuration and associated CSIRS configuration per gNB/TRP as inference.

Output Signalling towards E2 Nodes:

Table 3.4.2.1-4.   

<table><tr><td rowspan=1 colspan=6>Output Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source     →Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>Config.Period,granularity</td><td rowspan=1 colspan=1>New  or  existingconfig</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>SMO → O-DU</td><td rowspan=1 colspan=1>Inferred O-RU SS Burst Set (SS BlockNumber and SS Burst Periodicity andCSI-RS TRS Configuration</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Initialization,per O-RU</td><td rowspan=1 colspan=1>3GPP TS38.331IE:ServingCelIConfigCommon</td></tr></table>

# 3.4.2.1.1 O-RAN WG Impact Analysis

This use case focuses on O1, M-Plane (via SMO) interfaces for observations, measurements, KPIs collection. O-RAN specified R1 interface is used as one of the options for trained AI/ML model deployment as rAPP in Non-Real Time RIC. Another possibility is both offline AI/ML model training and model deployment can be done in the rAPP. In this case R1 interface is also used to transport training data to rAPP. Inference is communicated to E2 nodes (O-CU/O-DU) using R1 APIs and O1 interface (via SMO).

Impacts on O-RAN standards are identified below with the assumption that this is initial analysis report which is outcome of the massive MIMO pre-normative stage work. Captured impact analysis are based on latest published specifications of respective standards from identified O-RAN working groups.

# WG1 (use cases, architecture) Impact

a) O-RAN.WG1 - Use Cases Analysis Report o Based on the decision from pre-normative stage include this new use cases in the massive MIMO optimization UCTG document for Initial Access (SS Burst set configuration) configuration optimization problem.

b) O-RAN.WG1- Use Cases Detailed Specification

o Update use case specific details for Initial Access (SS Burst set configuration) massive-MIMO optimization considering pre-normative and normative stage decisions.

# WG2 (Non-RT RIC, R1) Impact

a) O-RAN.WG2 - Use Case Requirements

o Based on the necessity add Initial Access (SS Burst) Massive-MIMO optimization use-case based on agreements from pre-normative phase.   
o No impact on A1 interface is identified AI/ML model training is done in SMO/Non-Real Time RIC and trained model deployment is done in No-Real Time RIC as rAPP. Generated inference is communicated to E2 nodes (O-CU/O-DU) over O1 interface.

b) O-RAN.WG2 - AIML o No impact identified □ This use case is expected to be in line with standardized AI/ML workflow.

c) O-RAN.WG2 - Non-RT RIC Architecture & O-RAN.WG2 O-RAN Non-RT RIC: Functional Archite o No impact identified for the Non-Real Time RIC architecture and functional architecture specifications

o Incorporate the changes (if any) for R1 interface between the rAPPs and the non-RT RIC framework functions for following two rAPP deployment aspects.

Case 1: When AI/ML model is offline trained in SMO and deployed in Non-Real Time RIC as rAPP: Mechanism to deploy the model as rAPP over R1, inference communication over R1 and finally over O1 interface to E2 nodes (O-CU/O-DU)

Case 2: Alternatively, when AI/ML model is offline trained and deployed in the rAPP itself: Investigate AI/ML flow support for initial model load, training data transport to rAPP and inference communication to O1 via R1.

Background information:

SS Burst set configuration optimization AI/ML model is a micro service (rAPP) running in the Non-Real Time RIC.   
Non-Real Time RIC framework handles rAPP LCM.   
For model training data and inference communication from and to E2 nodes over O1 interface and M-plane interfaces are used.   
One of the feasible architectures is AI/ML model training in SMO or Non-Real Time RIC framework and trained AI/ML model deployment is done as rAPP. Alternative architecture for model training and deployment model is both are done in rAPP. R1 interface is used for model onboarding, training data set

transport. Inference data communication via O1 interface within the current Near-RT RIC framework.

a) No impact identified

# WG4 (CUS, M-Plane) Impact

a) No impact identified o Background information:

Over M-Plane interface SMO communicates/receives supported O-RU SSB beam configurations.   
These configurations are preprocessed with observations, measurements, KPIs data received over O1 interface to generate training data set which is used for offline AI/ML model training.

# WG5 (O1) Impact

a) O-RAN.WG5 - SMO - O-CU (O-RAN O1 Interface specification for O-CU-UP and O-CU-CP & O-RAN O1 Interface for O-CU-UP and O-CU-CP - YANG Models) ; SMO - O-DU (O-RAN O1 Interface specification for O-DU & O-RAN O1 Interface for O-DU 2.0 - YANG Models)

o Enhance O1 data model yang definitions for new measurements/ observations reporting required for SS Burst Set configuration optimization use case.

Data models/structures required for new measurement reports to the Non-Real Time RIC via SMO. Refer to the requirement section of this use case. L1/2 measurements: Analyse need for new data model definition over NETCONF for per cell or per UE measurement reporting (refer to requirement section for new reporting requirements). Counters: Add new data model to accommodate Number of active UEs in NG-RAN (Number of RRC_CONECTED UEs) over a predefined observation time window.

Based on the current understanding most of the measurements are specified in the 3GPP specifications except few like PRACH power measurement, which can be possibly derived based on the existing RA-reports thus can be proposed to 3GPP for standardized in SA5. New reporting will have to be incorporated into the O1 interface standard in terms of addition of new yang data models.

# WG10 (O1) Impact

a) O-RAN.WG10 - O-RAN Operations and Maintenance Architecture & O-RAN Operations and Maintenance Interface Specifications o No impact identified on the OAM architecture o Impacts on the O1 interface to O-RAN elements are identified in WG5 Background information Include data model enhancements to the O1 interface definitions for new measurements, observations required for SS Burst Set configuration optimization use case.

# O-RAN Standard Impact Summary:

Impacts on O-RAN WGs is identified in the following areas:

Introduce a set of new measurements/observations and reporting at O-DU and/or O-CU which are not defined in O-RAN specification already. New measurement/reporting are indicated in the requirement section of the use case.   
Incorporate changes in R1 interface specification for the case when model onboarding and training of AI/ML model is done in the rAPP microservice and,   
Implement potential changes to the O1 interfaces assuming other required KPIs are specified in 3GPP or O-RAN standards.

# 3.4.2.1.2 Relation and Impact on 3GPP Specification

UE- Specific Measurements and Reporting - From the requirement section, per UE specific measurements reporting which should be introduced in the upcoming release (e.g., RAN2 MDT trace specification, 3GPP TS 28.552 and related standards). We also propose that these new measurements should be taken up in the upcoming 3GPP RAN1 AI/ML discussion.

PRACH power measurement be derived based on the existing RA-report defined in RAN2, thus can be proposed to 3GPP for standardized in SA5.

New KPI - New KPI definition in 3GPP (e.g., Initial access latency value in case of SS Burst Set configuration optimization use case) need to be included in the future releases of 3GPP TS 32.425 Performance Management (PM); Performance measurements E-UTRAN specification.

Thus, during the normative work phase, changes for the R1 and O1 interface need to be worked out with respective WGs. Similarly, for any 3GPP specification dependencies, appropriate steps should be taken based on the agreed O-RAN MVPC Massive MIMO Optimization normative stage discussions points.

# Option 2a: Non-RT RIC Based Training and Near-RT RIC Deployment (DMRS and CSI-RS Configuration Optimizations)

For the class of use cases where few TTI level reaction time is necessary (example use cases are configuration optimization for CSI-RS ports allocation for acquisition in DL and UL, UE specific DMRS allocation in DL or UL etc.), offline trained AI/ML model need to be deployed in Near Real-Time RIC. In this architecture/deployment option, raw training data gathering, pre-processing them to generate AI/ML model training data set, and offline AI/ML model training are performed in the Data collection and control/Non-Real Time RIC entity and trained model deployment happens in Near-RT RIC. Raw training data set are collected from the $\mathrm { T R P / g N B }$ or cluster of deployed TRP/gNBs which constitute the large-scale network deployment. By default, heterogeneous network deployment is assumed supporting various usage patterns in different parts of the network.

Offline trained AI/ML agent/engine will allow operator to deploy it in Near-RT-RIC over O1 interface. AI/ML Agents can derive optimal per gNB/TRP configurations statically or semi-statically trigged by operator requirements or KPIs observations, measurements from E2 nodes. It is expected that AI/ML engine/agent will generate same/similar inferences for a set of gNB/TRPs which are deployed at the same geographical neighbours having similar usage pattern (example set of gNB/TRPs deployed to support a busy street with low to moderate mobility).

Data Collection and Control Unit collects required observations sets over different observation time windows to generate required training data set which necessitates O1, E2, and FH interface capability enhancements. Interface capabilities can be made scalable for future requirements to support any additional observations required over O1 and E2 interfaces which can help in faster convergence of AI/ML agent/engine.

@startuml   
skinparam defaultFontSize 12   
Box "Personnel" #lightblue Actor "Operator" as OPERATOR   
End box   
Box "Service Management and Orchestration" #gold Participant "Data Collection and Control" as SMO Participant "Non-RT RIC" as NRTRIC   
End box   
Box "O-RAN Nodes" #lightpink Participant "Near-RT RIC" as RTRIC Participant "E2-Nodes" as E2NODES Participant "O-RUs" as ORUs   
End box   
group Data Collection and Pre-Processing ORUs -> E2NODES : <<FH>> Observation, Mesaurement Data Collection E2NODES $- >$ SMO : $< < 0 1 > >$ Observation, Mesaurement Collection OPERATOR $- >$ SMO : Performance KPI Targets Inputs SMO -> SMO : Data Pre-Processing and AI/ML Training Data Generation   
end   
group ML Engine/Agent Training SMO -> NRTRIC : AI/ML Training Data NRTRIC $- >$ NRTRIC : AI/ML Engine/Agent Training   
end   
group Model Deployment and Inference Generation   
group Operator-Initiated OPERATOR $- >$ RTRIC : KPI Targets/Deployment Updates   
end   
group System Initiated SMO -> RTRIC : <<O1>> PI Degradation & Alarms   
end NRTRIC $- >$ RTRIC : <<O1>> Model Deployment SMO -> E2NODES : $< < 0 1 > >$ Measurement and Report Configuration SMO -> RTRIC : <<O1>> Traning Data (Optional) E2NODES ->RTRIC : <<E2>> Measure Reports Collection RTRIC $- >$ RTRIC : AI/ML Agent/Engine Inference RTRIC -> E2NODES : <<E2 $> >$ Updated Optimal Configs (E2 Nodes and O-RU Configurations) E2NODES -> ORUs : <<FH $\mathrm { . > > }$ Updated O-RU Configurations   
end   
group ML Agent Performance Monitoring E2NODES -> SMO : KPIs, Measurment Report, Observations RTRIC -> SMO : <<O1>> ML Performance Feedback ORUs -> E2NODES : <<FH>> Data Collection SMO $- >$ SMO : Performance Evaluation & Fallback Config Decision SMO -> E2NODES : $< < 0 1 > >$ Default/Fallback mMIMO Configuration E2NODES $- >$ SMO : <<O1>> Observation, Mesaurement Collection SMO -> NRTRIC : AI/ML Agent/Engine Re-Training Trigger   
end   
@enduml

![](images/21c2fc06328787b715654aac50e72bde16b7fc6e461f9a93fedc8e84615fa6b5.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.4.2.2-1. Flow diagram for CSI-RS and DMRS Configuration Optimization

# Requirements for CSI-RS and DMRS Configuration Optimization

a) DMRS Configuration Optimization: Required Observations for Training Data Set Generation

Initialization:

Table 3.4.2.2-1.   

<table><tr><td rowspan=1 colspan=6>Input/Output Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source     →Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>Config. Period,granularity</td><td rowspan=1 colspan=1>New or existingconfig</td></tr><tr><td rowspan=1 colspan=1>01Interfacevia SMO</td><td rowspan=1 colspan=1>O-DU → Non-RT RIC</td><td rowspan=1 colspan=1>Supported DMRS configuration per cell(example for PDSCH, IE DMRS-DownlinkConfig， for PUSCH IEDMRS-UplinkConfig) per cell</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Initialization</td><td rowspan=1 colspan=1>3GPP TS 38.331</td></tr><tr><td rowspan=1 colspan=1>01Interfacevia SMO</td><td rowspan=1 colspan=1>O-DU → Non-RT RIC</td><td rowspan=1 colspan=1>Supported SRS configuration per cell(SRS-Config IE) per cell</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>Initialization</td><td rowspan=1 colspan=1>3GPP TS 38.331</td></tr></table>

Measurements/reports from E2 Nodes over O1 interface (AI/ML model training phase):

Table 3.4.2.2-2.   

<table><tr><td rowspan=1 colspan=6>Input Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source      →Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod,granularity</td><td rowspan=1 colspan=1>New or existingmeasurement,ExistingSpecification(Section)</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>O-DU → Non-RT RIC</td><td rowspan=1 colspan=1>SRS reference signal receivedpower (SRS-RSRP) per UE</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>(non real-timefor     modeltraining)</td><td rowspan=1 colspan=1>3GPP TS 38.215(Sec. 5.1.19)New reporting</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>O-DU → Non-RT RIC</td><td rowspan=1 colspan=1>gNB Rx – Tx time difference (SRSbased) per UE</td><td rowspan=1 colspan=1>Sec</td><td rowspan=1 colspan=1>(non-real time,for     modeltraining)</td><td rowspan=1 colspan=1>3GPP TS 38.215(Sec. 5.2.3)New reporting</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>O-DU → Non-RT RIC</td><td rowspan=1 colspan=1>DMRS based SNR measurement atO-DU per UE</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>(non-real time,for     modeltraining)</td><td rowspan=1 colspan=1>New measurement andreporting</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>O-DU → Non-RT RIC</td><td rowspan=1 colspan=1>CSI reference signal received power(CSI-RSRP) per UE</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>(non real-timefor     modeltraining)</td><td rowspan=1 colspan=1>3GPP TS 38.215(Sec. 5.1.2)New reporting</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>O-CU → Non-RT RIC</td><td rowspan=1 colspan=1>Number of active UEs in NG-RAN(Number of RRC_CONECTEDUEs) per direction per cell</td><td rowspan=1 colspan=1>Integer</td><td rowspan=1 colspan=1>(nonreal-time,measuredeveryTwin * timewindow)</td><td rowspan=1 colspan=1>3GPP TS28.552Sections: 5.1.1.23 &amp;A.603GPP TS28.552 A.7</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>O-CU → Non-RT RIC</td><td rowspan=1 colspan=1>Network accessibility KPI per cell</td><td rowspan=1 colspan=1>Integer</td><td rowspan=1 colspan=1>(non real-time,measured1 everyTwi *  timewindow</td><td rowspan=1 colspan=1>3GPP TS 28.554Section 6.2</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>O-CU → Non-RT RIC</td><td rowspan=1 colspan=1>DL/ULnetworkthroughputperslice</td><td rowspan=1 colspan=1>Float(kbit/sec)</td><td rowspan=1 colspan=1>(nonreal-time,measuredeveryTwin * timewindow</td><td rowspan=1 colspan=1>3GPP TS 28.554Section6.3.2 andsection 6.3.3</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>O-DU → Non-RT RIC</td><td rowspan=1 colspan=1>DMRS/SRS based Doppler estimateper UE</td><td rowspan=1 colspan=1>Hz</td><td rowspan=1 colspan=1>(nonreal-time,measuredeveryTwin *  timewindow</td><td rowspan=1 colspan=1>Newmeasurementand reporting</td></tr></table>

1 Measurements/reports from E2 Nodes (inference phase):

Table 3.4.2.2-3.   

<table><tr><td rowspan=1 colspan=6>Input Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source      →Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod,granularity</td><td rowspan=1 colspan=1>New   or    existingmeasurement,Existing Specification(Section)</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>O-DU → Near-RT RIC</td><td rowspan=1 colspan=1>DMRS/SRS Doppler Estimate perUE</td><td rowspan=1 colspan=1>Hz</td><td rowspan=1 colspan=1>everyTwin-R   *timewindow</td><td rowspan=1 colspan=1>New measurement andreporting</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>O-CU → Near-RT RIC</td><td rowspan=1 colspan=1>Number of active UEs (mean, max) inNG-RAN       (Number      ofRRC_CONECTED  UEs)  perdirection per cell</td><td rowspan=1 colspan=1>Integer</td><td rowspan=1 colspan=1>ReportedeveryTwim-R   *timewindow</td><td rowspan=1 colspan=1>3GPP TS28.552Sections 5.1.1.23 &amp; A.603GPP TS28.552 A.7</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>O-DU → Near-RT RIC</td><td rowspan=1 colspan=1>DMRS based SNR measurementat O-DU per UE</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>everyTwin-R   *timewindow</td><td rowspan=1 colspan=1>NewMeasurementt andreporting</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>O-DU → Near-RT RIC</td><td rowspan=1 colspan=1>SRS reference signal receivedpower (SRS-RSRP) per UE</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>every SRSoccasion andaveragedover    Kreceptions</td><td rowspan=1 colspan=1>3GPP TS 38.215(Sec. 5.1.19)New reporting</td></tr></table>

4 Output Signalling towards E2 Nodes:

Table 3.4.2.2-4.   

<table><tr><td rowspan=1 colspan=6>Output Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source     →Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>Config.Period,granularity</td><td rowspan=1 colspan=1>New  or  existingconfig</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>Near-RT RIC →O-DU</td><td rowspan=1 colspan=1>DMRS configuration per cell (examplefor    PDSCH,    IE    DMRS-DownlinkConfig， for PUSCH IEDMRS-UplinkConfig) per cell</td><td rowspan=1 colspan=1>Index</td><td rowspan=1 colspan=1>Configuredevery T&gt;TWin-R</td><td rowspan=1 colspan=1>3GPP TS 38.331</td></tr></table>

${ \stackrel { * } { \mathop { \mathbf { T } } } _ { W i n } }$ is the predefined observation time window for offline training data collection.

$^ { * } T _ { W i n - R }$ is the predefined observation widow during inference generation, typically $T _ { W i n - R } \ \leq \ T _ { W i n }$

# (b) CSI-RS Configuration Optimization: Required Observations for Training Data Set Generation

Initialization:

Table 3.4.2.2-5.   

<table><tr><td rowspan=1 colspan=6>Input/Output Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source     →Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>Config.Period,granularity</td><td rowspan=1 colspan=1>New or existing config</td></tr><tr><td rowspan=1 colspan=1>01Interfacevia SMO</td><td rowspan=1 colspan=1>O-DU → Non-RT RIC</td><td rowspan=1 colspan=1>Supported CSI-RS configuration percell</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>Initialization</td><td rowspan=1 colspan=1>TS 138 331Section 6.3.2</td></tr><tr><td rowspan=1 colspan=1>01Interfacevia SMO</td><td rowspan=1 colspan=1>O-DU → Non-RT RIC</td><td rowspan=1 colspan=1> Supported SSB configuration per cell</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>Initialization</td><td rowspan=1 colspan=1>TS 138 331Section 6.3.2</td></tr></table>

Measurements/reports from E2 Nodes over O1 interface (AI/M model training phase):

Table 3.4.2.2-6.   

<table><tr><td colspan="9">Input Data</td></tr><tr><td>Interface</td><td>Source Target</td><td>→</td><td>Name/Description</td><td>Units</td><td colspan="2">Reporting Period, granularity</td><td>New measurement, (Section)</td><td>or existing Existing Specification</td></tr><tr><td>01 via SMO</td><td>O-DU RT RIC</td><td>→ Non-</td><td>SS reference signal received power (SS-RSRP) per UE</td><td>dBm</td><td>(non time model training)</td><td>real- for</td><td>3GPP TS 38.215 (Sec. 5.1.1) New reporting</td><td></td></tr><tr><td>01 via SMO</td><td>O-DU → Non- RT RIC</td><td></td><td>CSI reference signal received power (CSI-RSRP) per UE</td><td>dBm</td><td>(non time model training)</td><td>real- for</td><td>3GPP TS 38.215 (Sec.5.1.2) New reporting</td><td></td></tr><tr><td>01 via SMO</td><td>O-DU → Non- RT RIC</td><td></td><td>CSI Reports UE specific Channel Quality Index (CQI), Precoding matrix indicator (PMI), Rank Indicator (RI) per UE</td><td>CSI Report</td><td>(non-real time collection for model training)</td><td></td><td>3GPP TS 38.214 (Sec. 5.2.2) New reporting</td><td></td></tr><tr><td>01 via SMO</td><td>O-DU RT RIC</td><td>→ Non-</td><td>PRACH correlation power for every received PRACH corresponding to each active SSB Beam Index</td><td>dBm</td><td>(non time collection for training)</td><td>real- model</td><td>New Measurement (Could be measurement at O-DU (derived based on the existing RA-report defined in RAN2, standardized in SA5)</td><td>derived can be</td></tr><tr><td>01 via SMO</td><td>RT RIC</td><td>O-DU → Non-</td><td>Received PRACH instance number and corresponding beam index</td><td>Integer</td><td>Non time, every Beam Index within T in * time</td><td>real- for SSB</td><td>New Reporting 3GPP TS 28.552-h40, subclause 5.1.1.20/ TS 38.314-g40, 4.2.1.1</td><td>subclause</td></tr><tr><td>01 via SMO</td><td>O-CU RT RIC</td><td>→ Non-</td><td>Number of active UEs (mean, max) in NG-RAN (Number RRC_CONECTED UEs) per direction per cell</td><td>Integer of</td><td>window Reported every Twin-R time window</td><td>*</td><td>3GPP TS28.552 Sections 5.1.1.23 &amp; A.60 3GPP TS28.552 A.7</td><td></td></tr><tr><td>01 via SMO</td><td>O-CU → Non- RTRIC</td><td></td><td>Beam acquisition time per UE: UE reports beam measurement through CSI reports. gNB prepares an average beam acquisition time metric based on the per UE CSI reports in stages P2/P3</td><td>msec</td><td>(non time, measured every T in * time window</td><td>real-</td><td>New Report</td><td>Measurement &amp;</td></tr><tr><td>01 SMO</td><td>via O-CU RTRIC</td><td>→ Non-</td><td>DL/UL throughput per direction per cell Spectral efficiency can be computed from the throughput.</td><td>Float (kbit/se c)</td><td>(non time, measured every Twin * time window</td><td>real-</td><td>3GPP TS 28.554 Section 6.3.2 and section 6.3.3</td><td></td></tr></table>

Measurements/reports from E2 Nodes (inference phase):

Table 3.4.2.2-7.   

<table><tr><td rowspan=1 colspan=6>Input Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source      →Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod,granularity</td><td rowspan=1 colspan=1>New   or    existingmeasurement,Existing Specification(Section)</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>O-DU → Near-RT RIC</td><td rowspan=1 colspan=1>SS reference signal received power(SS-RSRP) per UE</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>MeasuredeveryTwin-R   *timewindow</td><td rowspan=1 colspan=1>3GPP TS 38.215(Sec. 5.1.1)New reporting</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>O-DU → Near-RT RIC</td><td rowspan=1 colspan=1>CSI reference signal received power(CSI-RSRP) per UE</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>MeasuredeveryTwin-R   *timewindow</td><td rowspan=1 colspan=1>3GPP TS 38.215(Sec. 5.1.2)New reporting</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>O-DU → Near-RT RIC</td><td rowspan=1 colspan=1>UE Specific Channel Quality Index(CQI), Precodingmatrixindicator (PMI), Rank Indicator (RI) per UE</td><td rowspan=1 colspan=1>Index/Number</td><td rowspan=1 colspan=1>MeasuredeveryTwin-R   *timewindow</td><td rowspan=1 colspan=1>3GPP TS 38.214(Sec. 5.2.2)New reporting</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>O-DU → Near-RT RIC</td><td rowspan=1 colspan=1>PRACH correlation power for everyreceived PRACH corresponding to eachactive SSB Beam Index</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>MeasuredeveryTWin-R   *timewindow</td><td rowspan=1 colspan=1>New Measurement(Could   be   derivedmeasurementat O-DU(derived based on theexisting RA-report definedin  RAN2,  can  bestandardized in SA5)New Reporting</td></tr></table>

${ \stackrel { * } { \mathop { \mathbf { T } } } _ { W i n } }$ is the predefined observation time window for offline training data set collection.

$^ { * } T _ { W i n - R }$ is the predefined observation widow during inference generation, typically $T _ { W i n - R } \ \leq \ T _ { W i n }$

For both DMRS and CSI-RS optimizations, in addition to the above measurements, observations and KPIs, Data Collection and Control module is expected to have access to the cell site deployment- configuration information and sitespecific information for example gNB/TRP density, terrain type. A set of predefined algorithmic steps will take these raw observations as inputs and generate required training data set in prescribed format for the AI/ML engine/agent. AI/ML model will generate optimal SS Burst Set configuration and associated CSI-RS configuration per gNB/TRP as inference.

Output Signalling towards E2 Nodes:

Table 3.4.2.2-8.   

<table><tr><td rowspan=1 colspan=6>Output Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source     →Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>Config.Period,granularity</td><td rowspan=1 colspan=1>New  or  existingconfig</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>Near-RT RIC →O-DU</td><td rowspan=1 colspan=1>Inferred CSI-RS configuration and relatedSSB configuration</td><td rowspan=1 colspan=1>Index</td><td rowspan=1 colspan=1>Non-realtime per gNB</td><td rowspan=1 colspan=1>TS 138 331Section 6.3.2</td></tr></table>

# 3.4.2.2.1 O-RAN WG Impact Analysis

This set of use case focus is on O1, M-Plane (via SMO) interfaces for observations, measurements, KPIs collection. ORAN specified O1 interface is used for trained AI/ML model deployment as xAPP in Near-Real Time RIC. Inference is communicated to E2 nodes (O-CU/O-DU) using E2 interface. Impacts on O-RAN standards are identified below with the assumption that this is initial analysis report which is outcome of the massive MIMO pre-normative stage work. Captured impact analysis are based on latest published specifications of respective standards from the identified O-RAN working groups.

# WG1 (use cases, architecture) Impact

a) O-RAN.WG1.Use Cases Analysis Report o Update the use case Massive MIMO Optimization - Non-Real Time RIC Training and Near Real Time RIC Deployment (CSI-RS and DMRS Configuration Optimization) considering pre-normative and normative stage decisions.   
b) O-RAN.WG1.Use Cases Detailed Specification o Update the use case details for Massive MIMO Optimization Non-Real Time RIC Training and Near Real Time RIC Deployment (CSI-RS and DMRS Configuration Optimization) considering prenormative and normative stage decisions.

# WG2 (Non-RT RIC, R1, A1) Impact

c) O-RAN.WG2 - Use Case Requirements o Add sub-use case details for the Non-Real Time RIC Training and Near Real Time RIC Deployment (CSI-RS and DMRS Configuration Optimization) considering pre-normative and normative stage decisions.   
d) O-RAN.WG2 - AIML o No impact identified ▪ This use case is expected to be in line with standardized AI/ML workflow.   
e) O-RAN.WG2 - Non-RT RIC Architecture & O-RAN.WG2 - Non-RT RIC ARCH TR o No impact identified for the Non-Real Time RIC architecture o Background information: CSI-RS and DMRS configuration optimization is an xAPP running in the Near-Real Time RIC after training in Non-Real Time RIC Near-Real Time RIC framework handles xAPP LCM. For model training data and inference communication from and to E2 nodes over O1 interface (via SMO) and M-plane interfaces are used.

f) A1 Interface o No impact identified

g) O-RAN.WG3- Use Case and Requirements o Add use case details for Non-RT RIC Training and Near RT RIC Deployment (CSI-RS and DMRS Configuration Optimization) considering agreements from pre-normative and normative phase approvals   
h) O-RAN.WG3. Near-RT RAN Intelligent Controller Near-RT RIC Architecture o No impact identified o Background information For CSI-RS and DMRS optimizations, trained AI/ML model is deployed as xAPP which will interface with E2 nodes (O-CU/O-DU) using E2 interface. xAPP uses Near-Real Time RIC services and E2 interfaces to a) get measurements, observations, PIs from the E2 Nodes for inference generation and b) configures DMRS or CSIRS in the E2 nodes.

i) O-RAN.WG3- Near-Real-time RAN Intelligent Controller Architecture & E2 General Aspects and Principles

o No impact identified   
o Background information ▪ Offline trained AI/ML model is deployed as xAPP which uses Near-Real Time RIC services and E2 interfaces to a) get measurements, observations, PIs from the E2 Nodes for inference generation and b) configures DMRS or CSI-RS in the E2 nodes.

O-RAN.WG3- Near-Real-time RAN Intelligent Controller, E2 Application Protocol

o Add new measurements and reporting to the E2 interface from E2 nodes (O-CU/O-DU) to Near-Real Time RIC during inference generation and subsequent inference communication to E2 nodes. o Background information DMRS/CSI-RS optimization xAPP uses E2 interface to a) get measurements, observations, KPIs from the E2 Nodes for inference generation and b) configures DMRS/CSI-RS in the E2 Nodes.   
k) O-RAN.WG3- Near-Real-time RAN Intelligent Controller E2 Service Model (KPM) o Enhance the interface for cell level KPM and other measurements used in CSI-RS and DMRS configuration optimization use cases during inference generation.   
l) O-RAN.WG3- Near-Real-time RAN Intelligent Controller E2 Service Model (Common, EC, NI) o Add new E2AP requirements for DMRS and CSI/RS o Identify definition of new E2SMs and required information models that may be required by for DMRS and CSI-RS configuration use cases and reflect them the next version of standard ORANWG3.E2SM. ▪ We also assuming all measurement are specified in 3GPP TS 28.552, 3GPP TS 28.554, 3GPP TS 38.215, 3GPP TS 38.214, TS 38 331, TS 37.320 and/or respective O-RAN standards

# WG5 (O1) Impact

m) O-RAN.WG5 - SMO - O-CU (O-RAN O1 Interface specification for O-CU-UP and O-CU-CP & O-RAN O1 Interface for O-CU-UP and O-CU-CP - YANG Models); SMO - O-DU (O-RAN O1 Interface specification for O-DU & O-RAN O1 Interface for O-DU 2.0 - YANG Models) o Enhance the yang data models due to new measurement/observations reporting listed for CSI-RS and DMRS configuration optimizations use cases requirement section

Based on the requirement section most of the measurements are specified in the 3GPP specification except couple of them like PRACH power measurement, DMRS based SNR measurement, Doppler, Beam acquisition time measurement etc. which need to be proposed to 3GPP for standardized in SA5. New reporting will have new data model definition on the O1 interface standard in terms of addition of new yang data models.

# WG10 (SMO, O1) Impact

n) O-RAN.WG10 - O-RAN Operations and Maintenance Architecture & O-RAN Operations and Maintenance Interface Specifications o No impact identified

# Summary of O-RAN WG Impacts:

Impacts on O-RAN WGs are identified in the following areas:

Introduce set of new UE/cell specific measurements/observations reporting at O-DU and/or O-CU which are not defined in O-RAN specification already as indicated in the requirement section of the respective use cases.   
Incorporate E2 interface specification improvements for new measurement data communication from E2 nodes to Near-Real Time RIC. Impacts described here is based on the assumption that required KPIs are specified in 3GPP or O-RAN standard.

Work in O-RAN WGs can be minimized by referring to the ongoing 3GPP and O-RAN specification as done today, e.g., E2SM-KPM, O RAN.WG5.O-CU-O1, O-RAN.WG10.O1.

# 3.4.2.2.2 Relation and Impact on 3GPP Specification

UE- Specific Measurements and Reporting - From the requirement section, per UE measurements and reporting have to be added to the upcoming release (R17/18) of 3GPP standards (e.g., RAN2 MDT trace specification, 3GPP TS 28.552 and related standards). These new measurements will be also taken up in the upcoming AI/ML 3GPP RAN1 activities.

PRACH power measurement be derived based on the existing RA-report defined in RAN2, thus can be proposed to 3GPP for standardized in SA5.

# Options 1b, 2b: E2 Node (O-CU) based AI/ML inference (Optimization of SS Burst Set, DMRS and CSI-RS Configuration)

In this architecture option, the AI/ML model training might also be hosted in Non-RT RIC in case of SS Burst Set and in Near-RT RIC in case of DM-RS and CSI-RS configuration, but with the difference that the AI/ML model is deployed in the O-CU where the inference is executed. In contrast to the Non-RT RIC-based deployment (option 1 - SS Burst Set configuration optimization) or Near-RT RIC based deployment (option 2 - DMRS/CSI-RS configuration optimization), this deployment scenario presents the opportunity for optimization with faster loop timing or in different deployment architectures. While a Non-/Near-RT RIC based solution might be preferable to coordinate across multiple gNBs, a OCU based inference solution might be preferred for disaggregated deployments where an O-CU controls a large number of O-DUs. Similarly, Non-/Near-RT RIC based solutions (option 1 or 2) might be preferred for slow loop timings while a O-CU based solution might be preferred for fast loop timings. Besides this difference, the same principles as previously described apply and the same performance gain can be expected.

The configuration is assumed to be a rather slow process for SS Burst Set reconfiguration. DM-RS and CSI-RS might be reconfigured more dynamically, but there are probably no additional performance gains of an O-CU based inference over a Near-RT RIC based inference. Nevertheless, the O1/E2 load to continuously transfer data for inference will be reduced and the algorithm might have access to a larger number of configuration parameters when hosted at the O-CU.

Therefore, the operator can leverage on the non-real time data collection capabilities of the O1/E2 interface (for offline ML training) plus the computational capacity (AI/ML framework) of the RIC(s) for ML training but perform the ML inference in the E2 Node. More specifically, the alternative architecture for SS Burst Set configuration optimization hosts ML training in the Non-Real Time RIC and inference in the E2 Node (O-CU) (Option 1b in Figure 3.4.2.3-1. middle). The alternative architecture for DMRS and CSI-RS configuration optimization hosts ML training in the NearReal Time RIC and inference in the E2 Node (O-CU) (Option 2b in Figure 3.4.2.3-1. right).

ML Deployment Scenario 1.5 (Technical Report O-RAN.WG2.AIML-v01.03) supports training in the Non-RT RIC and inference in the E2 Node. Training in the Near-RT RIC and inference in the E2 Node is a new deployment scenario still to be added to respective specifications. Related impact on O-RAN WGs is analyzed in section 3.4.2.3.1. 3GPP RAN WGs will start working on gNB hosted AI/ML algorithms in 3GPP Rel.18. More details are provided in 3GPP TR 37.817.

This O-RAN architecture option introduced in this section will complement the 3GPP AI/ML approach (i.e. model hosted in E2 Node) with RIC based training capabilities and the ability to deploy a trained ML model in the E2 node.

In both cases of ML training in Non- or Near-RT RIC, the ML model will be deployed via the O1 interface. This means in case of ML training in the Near-RT RIC, the trained ML model will be delivered from Near-RT RIC to SMO via O1 first and from SMO to E2 Node via O1 next. This ensures a common ML model deployment in the E2 nodes centrally controlled via the SMO. ML model training in the Near-RT RIC might be preferred in cases where the ML training relies on extensive RAN data provided via E2, which may not necessarily be available via O1. While Non-RT RIC training might be preferred for network specific ML models, Near-RT RIC might be preferred for cell specific ML models. A retraining of an existing network specific ML model with cell specific data in the Near-RT RIC can also be envisioned.

![](images/36bb8cfeaf9d07a79e6b35d6fb1efd2c26b966c4889ba17df8e750aaaa11072d.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.4.2.3-1. Left: O-RAN deployment options 1a and 2a. Middle, right: Deployment options 1b and 2b with ML inference in the RAN E2 Node.

# 3.4.2.3.1 Additional O-RAN Standardization Impact

WG2 (Non-RT RIC, A1, R1) Impact

O-RAN.WG2.AIML-v01.03

o Further specify deployment scenario 1.5, with training in the Non-RT RIC and inference in the E2 Node (Option 2a).   
o Specify a new deployment scenario with training (potentially for other than reinforcement ML tasks) in the Near-RT RIC, ML Model management in the Non-RT RIC, and inference in the E2 Node (Option 2b).

# WG5 (O1) Impact / WG10 (SMO, O1) Impact

No impact identified

o Trained ML Model transfer from Near-RT RIC to SMO as part of the ML Model management (Option 2b) – using file transfer.   
o Trained ML Model deployment from SMO to O-CU as part of the ML Model management (Options 2a and 2b) – using file transfer.

# Discussion of Architecture Options

Comparing architecture deployment Options 1a, 2a with 1b, 2b:

Table 3.4.2.4-1.   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Option 1a, 2a</td><td rowspan=1 colspan=1>Option 1b, 2b</td></tr><tr><td rowspan=1 colspan=1>ML Training location</td><td rowspan=1 colspan=1>Non-/Near- RT RIC</td><td rowspan=1 colspan=1>Non-/Near-RT RIC</td></tr><tr><td rowspan=1 colspan=1>ML Inference location</td><td rowspan=1 colspan=1>Non-/Near-RT RIC</td><td rowspan=1 colspan=1>E2 Node</td></tr><tr><td rowspan=1 colspan=1>Suitable deployments</td><td rowspan=1 colspan=1>Aggregated architecture orO-CUs controlling few DUs</td><td rowspan=1 colspan=1>Disaggregated architectures withO-CU controlling many O-DUs</td></tr><tr><td rowspan=1 colspan=1>E2 capacity requirements</td><td rowspan=1 colspan=1>high capacity &amp; continuous(ML training &amp; inference)</td><td rowspan=1 colspan=1>flexible capacity &amp; temporary(only for ML training)</td></tr><tr><td rowspan=1 colspan=1>E2 delay requirements</td><td rowspan=1 colspan=1>delay critical</td><td rowspan=1 colspan=1>not delay critical(offline training)</td></tr><tr><td rowspan=1 colspan=1>Control loop supported</td><td rowspan=1 colspan=1>slower</td><td rowspan=1 colspan=1>faster possible</td></tr><tr><td rowspan=1 colspan=1>Modelcomplexity   andoptimization scope</td><td rowspan=1 colspan=1>more complex models(incl. wide area optimization across O-CUs)</td><td rowspan=1 colspan=1>more simple models(optimization within the O-CU)</td></tr></table>

As can be seen from Table 3.4.2.4-1, the architecture options target different deployments with different requirements on E2 capacity and may differ in terms of the optimization scope.

This means both architecture options are viable options for SSB Burst Set, DM-RS and CSI-RS configuration optimization. The standard should not mandate the one or the other option, but it should be up to the vendor to make this decision on a per product basis. This leaves room for enhancements over time and for operators to choose different architectures for different deployment options.

# 3.4.3 Feasibility and Gain/Complexity Analysis

# Feasibility and Gain Analysis

# A. Near-RT RIC Deployment Architecture (SS Burst Set Configuration Optimization):

This section we present calculated peak SE gain trends with varying SS Burst Configurations, discusses suitability of using AI/ML based optimization techniques for choosing deployment specific, slow time varying optimal SS Bust Set configurations. Also, highlighted tradeoff between choosing lower SS Burst Set configuration and achievable SE gains while meeting initial access latency KPI target set by the operator.

# Goal of this discussion:

One aspect of presenting these results is to highlight the opportunity of significant SE gains when optimal configuration is chosen and applied to the gNB/TRP. Another aspect is to highlight the necessity of applying AI/ML based optimization techniques to these network performance optimization problems.

AI/ML based optimization techniques are ideally suitable for 3GPP NR network optimization problems. More and more automations are expected with growing network deployment and optimization complexity. ML based intelligent agents are equipped to handle complex optimizations with trade-offs between long-term and short-term benefits. AI/ML processes learns autonomously, without the human intervention with domain expertise making them ideally suitable for time varying network function optimizations.

# What result is presented:

Impact of SS Burst Set configuration optimization on system overhead resulting in gNB Spectral Efficiency gain and feasibility of using AI/ML techniques for such large parameter based constrained optimization problem.

Presented results are peak spectral efficiency gain trends when different and allowable SS Burst Set configurations (Number of SS Blocks in a SS Bust Set and SS Burst Set periodicity) are chosen. Observed peak spectral efficiency (SE) gains are the result of system overhead reduction. Job of the AI/ML optimizer is to infer an optimal SS Bust Set configuration based on the target deployment scenario and slow time varying network usage patterns constrained to initial access latency target set by the operator.

SE graphs are per gNB Peak SE results (ITU Document 5D/50-E 11 February 2020, 3GPP NR 38.336) for varying SS block number and SS Burst periodicity in 3GPP NR FR1 and FR2 systems with realistic parameters configurations ranges supported by 3GPP specifications for respective frequency bands.

One can observe from the presented results below that SE gain is maximum when lowest SS Burst Set configuration is chosen for the system (within the configuration range supported by 3GPP). However, this would lead to degraded Initial Access (IA) latency KPI. Thus, we need to opt for constrained optimization techniques to avoid increase in IA latency beyond operator mentioned limit. Another important aspect of the optimizer is to consider slow time varying network usage pattern and time varying UE distribution patterns which can be inferred from the available measurements, observations, PIs. Thus, the optimizer will provide slow time varying SS Burst Set configuration per gNB/TRP which will result in system overhead reduction and hence can achieve optimal SE gain per gNB.

AI/ML based constrained optimization techniques are ideally suitable for large-scale (multi-gNB/TRP) and multi-parameter constrained optimization problems and result in proactive and predictable solutions for realistic NR network deployment scenarios. Traditionally one fixed configuration is decided for the network by the skilled manpower and applied during deployment of the network hence results in inefficient network design.

# Tradeoff between SS Burst Set configuration optimization and SE improvement:

Directly selecting the lowest SS Burst Set configuration (without considering the network usage pattern) to reduce reference signaling overhead will result in reduced SS Block density in both time and frequency directions. This may result in (a) increased initial access latency, (b) reduced mobility support (L3 mobility performance), (c) inferior time and frequency tracking performance, (d)potentially clustered access to the network (impacting the L1/2 beam management (for GoB based MIMO schemes), (d) reduced PBCH transmission frequency in SSB and hence impact timely availability of the system information blocks.

Thus, the important role of an AI/ML optimization techniques is to constrain the SB Block optimization to meet KPI targets set by the operator. Example KPI based constrains are operator defined IA latency target and coverage, target mobility support by the network, beam management KPIs (tracking and acquisition performances). Inferences generated by the AI/ML engine will be usage dependent slow time varying configurations per gNB/TRP. Here optimization techniques should not exclude possibility of joint optimizations example SSB and CSI-RS when required.

# Example Peak-SE Computation Scenario Descriptions:

a) SE gain computational results are presented for three NR systems configurations:

1. FR2: BW = 100MHz, SCS =120KHz $2 . \mathrm { B W } = 9 0 \mathrm { M H z }$ FR1 (with 8 SS Block frequency domain multiplexing), $3 . \mathrm { B W } = 9 0 \mathrm { M H z }$ FR1 (with 12 SS Block frequency domain multiplexing),

b) 1 gNB Peak SE computation

c) 1 UE SU-MIMO in one sector   
d) Available DL antenna ports $> = \mathbf { M a x }$ layers supported by 3GPP NR specs for target system configuration   
e) Cell reference signal configurations are given in ITU Document 5D/50-E 11 February 2020

# 1. NR FR2 System Configuration (DL): SS Burst Set Configuration Optimization

NR Numerology: FR2,   
$\mathbf { B W } = 1 0 0 \mathbf { M H z }$ , $\mathrm { S C S } = 1 2 0 \mathrm { K H z } .$ ,   
Maximum allocated number $\mathrm { P R B } = 6 6 $   
Maximum modulation order $= 8$   
{Minimum, Maximum} SS Block number per SS Burst Supported: {8, 64}   
Maximum number of layers in DL: 6 (1 UE, SU-MIMO)   
Max coding rate: 0.9258   
SSBurst Set config optimization goals:

Reduce Number of SS Blocks/SS Burst Set through KPI optimization Reduce frequency of SS Burst Sending

![](images/d5354805c76e91ea960122fcbd51c8b66738b208486fc37f5ae3ed05ea2a6c91.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.4.3.1-1. Computed SE variation plot with SS Block configuration change {SS Block number and SS Burst Set periodicity}.

Achievable peak SE Improvement factor for the SSB resources saving ignoring potential performance degradation in this $\mathrm { g N B }$ is $2 0 0 \%$ .

Results shows high SE improvement possibility in mmWave systems when optimal SS Block configuration is adopted in each gNB/TRP. Application of AI/ML will help in predictive and proactive inferences with reduced system overhead.

# 2. NR FR1 System Configuration (DL): SS Burst Set Configuration Optimization

System Numerology: FR1

Maximum allocated number $\mathrm { P R B } = 2 4 5$

Maximum modulation order $= 8$

{Minimum, Maximum} SS Block number per SS Burst Supported: {1,8}

Maximum number of layers in DL: 8 (1 UE. SU-MIMO)

Multi-SS Block capability: 8 per slot (not shown in the figure)

Max coding rate: 0.9258

SSB Config optimization goals:

Reduce Number of SS Blocks/SS Burst Set by optimization Reduce frequency of SS Bust Sending

![](images/4d290bffcc2b500052d8e97d09ff79f803ffdee22d282358c1aa6abcedffdca1.jpg)

> **Image Summary:** (Summary not available)


# Figure 3.4.3.1-2. Spectral efficiency variation over SS Block number and SS Burst Set periodicity configurations plot for FR1 system with higher PRBs.

Achievable peak SE Improvement factor for the SSB resources saving ignoring potential performance degradation in this gNB is ${ \sim } 1 6 . 4 \%$ . Results shows noticeable SE improvement possibility in FR1 system when optimal SS Block configuration is adopted in each gNB/TRP. Application of AI/ML will help in predictive and proactive convergence.

# 3. NR FR1 System Configuration (DL): SS Burst Set Configuration Optimization

System Numerology: FR1

$$
\mathrm { B W } = 9 0 \mathrm { M H z } , \mathrm { S C S } = 3 0 \mathrm { K H z } ,
$$

Maximum allocated number $\mathrm { P R B } = 2 4 5$

Maximum modulation order $= 8$

{Minimum, Maximum} SS Block number per SS Burst Supported: {1,8}

Maximum number of layers in DL: 8

Multi-SS Block capability: 12 per slot (not shown in the figure)

# SSB Config optimization goals:

Reduce Number of SS Blocks/SS Burst Set by optimization Reduce frequency of SS Bust Sending

#

![](images/edb7d729c173bb8cc8aeb8bb875b151e66a159e8d8e203737cc06e9f11c8d0ac.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.4.3.1-3. SE variation over SS Block number and SS Burst Set periodicity configuration for FR1 system with FDM in SSB transmission.

SE plot shows significant gain (max $2 5 . 6 \%$ ) can be achieved in FR1 systems having multi-SSB SSB transmission even when large PRBs are used for data transmission. Note that in this scenario the number of SSB transmissions in frequency domain multiplexing is increased to 12.

Achievable peak SE Improvement factor for the SSB resources saving ignoring potential performance degradation in this $\mathrm { g N B }$ is ${ \sim } 2 5 . 6 \%$ .

# B. Use Case Motivation for Near-RT RIC Deployment Architectures:

For Near-RT RIC based architecture/deployment scenario use-cases, goal is to optimize CSI-RS and DMRS transmission configurations and CSI reporting configurations where applicable. Based on the observations, measurements and KPI targets (training data) and using appropriate constrained optimization techniques, AI/ML model/agent will train the model for Near-RT RIC deployment.

Deployed model can infer target usage specific optimal configurations for CSI-RS and DMRS which will minimize the system overhead and hence will provide SE gains. AI/ML inferred configuration are not necessarily the lowest configurations.

In line with SSB use-case scenario, to create motivation around Near-RT RIC deployment-based use cases, below we have presented achievable peak Spectral Efficiency results for individual DMRS and CSI-RS transmission configuration optimizations. Presented SE graphs are per gNB Peak SE results (ITU Document 5D/50-E 11 February 2020, 3GPP NR 38.336) with varying (a) DMRS transmission configurations and (b) CSI-RS transmission configurations following 3GPP NR (FR1 and FR2) standards with realistic system parameter configurations for respective frequency bands. It is also important that both DMRS and CSI-RS optimization techniques can be jointly applied to the system for a target deployment scenario and use cases to achieve improved SE performance.

a) DMRS Configuration Optimization: Example System Configuration   
Table 3.4.3.1-1. System configurations for FR1 and FR2 system to measure peak SE when DMIRS configuration is varied   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>NR FR1</td><td rowspan=1 colspan=1>NR FR2</td></tr><tr><td rowspan=1 colspan=1>BW &amp; SCS</td><td rowspan=1 colspan=1>90MHz, 30KHz</td><td rowspan=1 colspan=1>BW = 100MHz, SCS = 120KHz</td></tr><tr><td rowspan=1 colspan=1>Maximum PRB Number</td><td rowspan=1 colspan=1>245</td><td rowspan=1 colspan=1>66</td></tr><tr><td rowspan=1 colspan=1>Maximum Modulation Order</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>8</td></tr><tr><td rowspan=1 colspan=1>SS Block number per SS Burst</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>64</td></tr><tr><td rowspan=1 colspan=1>SS Burst Set Periodicity</td><td rowspan=1 colspan=1>20ms</td><td rowspan=1 colspan=1>20ms</td></tr><tr><td rowspan=1 colspan=1>SS Burst FDM</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>Maximum number of layers (DL)</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>6</td></tr><tr><td rowspan=1 colspan=1>Max coding rate</td><td rowspan=1 colspan=1>0.9258</td><td rowspan=1 colspan=1>0.9258</td></tr><tr><td rowspan=1 colspan=1>DMRS Type</td><td rowspan=1 colspan=1>Type-1, Single Symbol</td><td rowspan=1 colspan=1>Type-1, Single Symbol</td></tr><tr><td rowspan=1 colspan=1>DMRS Density (#RE/RB/Slot)</td><td rowspan=1 colspan=1>6,12,18,24</td><td rowspan=1 colspan=1>6,12,18, 24</td></tr></table>

![](images/e69b047dbed8b8d4cb16f81a952f17d2748b7fcacb44d2d2b24cfca82f765d5f.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.4.3.1-4. Peak SE variation over DMRS Density (#RE/RB/Slot) for Type 1, Single Symbol DMRS allocation for (a) FR1 and (b) FR2 systems with no FDM in SSB transmission.

For both FR1 and FR2, peak SE plots from Figure 3.4.3.1-4 shows noticeable SE improvement can be achieved with the system configurations indicated in Table 3.4.3.1-1. For FR1 max SE gain $1 6 . 7 \%$ and for FR2 max can be achieved is approximately $2 7 . 3 \%$ assuming lowest DMRS configuration is used, resulting in resources saving ignoring potential performance degradation in this gNB.

Directly configuring (without considering the network usage pattern) the lower configurations will degrade the channel estimation performance and related other parameter estimations accuracies, impact achievable throughput for higher mobility scenarios. Thus, one of the important jobs of the AI/ML engine is to take Operator's defined KPIs (parameter estimation accuracy targets, mobility support etc. which are usage dependent parameters), constrain the optimization to target KPIs from operator and infer suitable configurations.

b) CSI-RS Configuration Optimization: Example System Configuration   
Table 3.4.3.1-2. System configurations for FR1 and FR2 system to measure peak SE when CSI-RS configuration is varied   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>NR FR1</td><td rowspan=1 colspan=1>NR FR2</td></tr><tr><td rowspan=1 colspan=1>BW &amp; SCS</td><td rowspan=1 colspan=1>90MHz, 30KHz</td><td rowspan=1 colspan=1>BW = 100MHz, SCS = 120KHz</td></tr><tr><td rowspan=1 colspan=1>Maximum PRB Number</td><td rowspan=1 colspan=1>245</td><td rowspan=1 colspan=1>66</td></tr><tr><td rowspan=1 colspan=1>Maximum Modulation Order</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>8</td></tr><tr><td rowspan=1 colspan=1>SS Block number per SS Burst</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>8</td></tr><tr><td rowspan=1 colspan=1>SS Burst Set Periodicity</td><td rowspan=1 colspan=1>5ms</td><td rowspan=1 colspan=1>5ms</td></tr><tr><td rowspan=1 colspan=1>SS Burst FDM</td><td rowspan=1 colspan=1>$12r</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>Maximum number of layers (DL)</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>6</td></tr><tr><td rowspan=1 colspan=1>Max coding rate</td><td rowspan=1 colspan=1>0.9258</td><td rowspan=1 colspan=1>0.9258</td></tr><tr><td rowspan=1 colspan=1>DMRS Type</td><td rowspan=1 colspan=1>Type-1, Single Symbol</td><td rowspan=1 colspan=1>Type-1, Single Symbol</td></tr><tr><td rowspan=1 colspan=1>DMRS Density (#RE/RB/Slot)</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>24</td></tr><tr><td rowspan=1 colspan=1>CSI-RS Density (#RE/RB/Slot)</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>8</td></tr><tr><td rowspan=1 colspan=1>CSI-RS Tx in every kth Slot</td><td rowspan=1 colspan=1>4:320</td><td rowspan=1 colspan=1>4:640</td></tr></table>

![](images/c09e87d4ac06d2c1ecdc959527d8604929086405251ad57992d4b986456fe7b8.jpg)

> **Image Summary:** (Summary not available)
  
Figure 3.4.3.1-5. Peak SE variation over CSI-RS periodicity (#RE/RB/Slot) for (a) FR1 and (b) FR2 systems with FDM in SSB transmission.

![](images/1602393c31c081d36c09a803a5b802caaaf62821e954cb98be7b0ed53ac173a7.jpg)

> **Image Summary:** (Summary not available)


For both FR1 and FR2, peak SE plots from Figure 3.4.3.1-5 shows approximately $1 0 \%$ improvement can be achieved for the system with configurations as shown in Table 3.4.3.1-2. For FR1 max SE gain $1 0 . 8 4 \%$ and for FR2 max can be achieved is approximately $9 . 8 7 \%$ assuming lowest CSI-RS configuration is used which results in resources saving ignoring potential performance degradation in this gNB. For FR2 system, for the above peak SE plot, system uses number of SSB blocks as 8 and number of CSI-RS beams as 8 per SSB beam (joint SSB beam -CSI-RS beam acquisition).

Directly configuring (without considering the network usage pattern) lower CSI-RS acquisition/beam management configurations may degrade the CSI feedback quality which has direct impact on the achievable throughput (FR1) or may impact beam measurement performance (FR2). Thus, one of the important jobs of the AI/ML engine is to take Operator's defined KPIs (CSI accuracy, beam acquisition KPIs) and constrain the optimization with the target KPIs and infer suitable configuration.

3GPP NR standard allows max 32 port CSI-RS transmission. It is important to note that SSB beam and CSI-RS optimizations are closely related when SSB and CSI-RS are jointly used for beam measurement in NR FR2 systems. In this case FR2 system will be limited by max 8 SS Blocks transmission per SS Burst and each SS beam will have 8 CSIRS for P2 based beam measurement which is uses as scenario for SE calculations in Figure 3.4.3.1-5.

# Complexity

Complexity of AI/ML based optimization depends on the type of algorithm used for the optimization, size of the training data set, feature list length. Computational power and memory availability of the model training and inference host will also impact training and inference generation time. Typical learning algorithms have large model training time complexity compared to inference generation.

One example is with logistics regression based supervised learning algorithms, training phase time complexity is $O ( p ^ { 2 } n + p ^ { 3 } )$ and during prediction time complexity is $O ( p )$ where $p$ is the number of features and $n$ is the number of training example.

Thus, offline training of the AI/ML model is desirable and recommended in all the sub sub-uses cases presented herein (namely SS Burst Set, CSI-RS, and DMRS configuration optimization use cases).

Considering state of the art silicon technology availability in the network side we can assume that computation power (of the training and inference host) has improved significantly over last decade following Moor's Law, through multicore processor designs and parallel programming technology. Thus, large computation capacity at the model training and inference host are available for these optimizations' problems to run. Including training, inferences can be generated at rAPP $\scriptstyle \left( > = 1 \sec \right)$ ) and Near-RT RIC $\ : \cdot \ : < \ :$ 1sec) control loops efficiently with appropriate selection of training data sets size and feature list for AI/ML algorithms.

# 4 L1 / L2 Beam Management

# 4.1 Overview

In 5G NR, mmWave communication using a large bandwidth is one of the key technologies to achieve high-data rate and capacity improvement. However, mmWave frequencies are suffered from high propagation loss including unexpected signal blockages in a mobile environment. To overcome these challenges, directional-beam transmission enabled by hybrid analogue-digital beamforming with large scale antenna array is typically applied at BS side at least. Under this hybrid beamforming architecture, achieving fine beam alignment between BS and UE beams becomes a prerequisite for successful data transmission and reception. A set of Layer 1 (i.e., physical layer) and Layer 2 (i.e., medium access control layer) procedures to acquire and maintain a set of BS and/or UE beams for DL and UL transmission/reception is referred to as L1/L2 beam management. In 3GPP, the beam management procedures that control the determination and maintenance of the serving beam(s) for each UE within a cell has been firstly specified in Release 15. The O-RAN architecture offer opportunities to improve beam management performance by utilizing Non-RT RIC and/or Near-RT RIC to assist E2 nodes to realize intelligent solution.

# 4.2 Solution 1: AI/ML-assisted Beam Selection Optimization

# 4.2.1 Problem Statement and Value Proposition

The L1/L2 beam management procedures that establish and maintain the highly directional transmission link between BS and UE play an important role to enable high quality communications under mmWave frequencies. The current 3GPP 5G NR standard support good flexibility of UE-specific configuration in terms of beam measurement, beam report and beam indication. However, achieving accurate beam alignment between BS and UE is challenging and costly, and a trade-off between network performance improvement and signaling overhead need to be solved. Without employing frequent beam measurement and measurement report, connection between BS and UE may be easily interrupted due to UE movement or blockage, in particular under high mobility scenarios. However, the number of required resources for frequent beam measurement and measurement report will cause an overhead problem which may decrease the overall network throughput. Without an intelligent solution, the network has to face an either-or situation, either high reliability with large signaling overhead or small signaling overhead with poor reliability.

In recent years, application of AI/ML techniques in mobile communication networks has drawn a lot of interest. AI/ML techniques can be also used as a powerful tool which enable RAN to make quicker and smarter decision in the beam management related procedures, which will contribute to improved network performance in terms of throughput and reliability. In particular, how to improve the performance of beam acquisition and tracking based on the existing 5G NR standard should be considered. AI/ML-assisted solutions can be used to estimate the quality of SSB/CSI-RS beams based on limited beam measurement and/or UE geolocation information, which allows fast beam acquisition and beam failure recovery and ensures reliable radio link against blockage, especially in mmWave. AI/ML-assisted solutions can also be used to predict a future beam(set), beam switching events or blockage events based on historical measurement reports and/or UE geolocation information. Higher accuracy in beam tracking, lower signaling overhead and low latency in beam switching are essential to guarantee service continuity for UEs. The L1/L2 beam management optimization is particularly relevant for mmWave frequencies but may also be applicable for sub-6GHz frequencies.

Potential benefits of AI/ML assisted beam management will include signaling overhead reduction, latency reduction and reliability improvement.

# 4.2.2 Architecture/Deployment Options

# Option 1 – Non/Near-RT RIC based Beam Selection Optimization

To enable an intelligent beam management in the O-RAN architecture, interaction between SMO, Non-RT RIC, NearRT RIC and E2 nodes should be achieved. SMO needs to collect necessary KPIs, beam-related measurement from E2 nodes and enrichment information (e.g., UE geolocation information) from external application/server, if required, to support AI/ML model training and performance monitoring which is hosted by Non-RT RIC. In this case, Non-RT RIC can train the AI/ML model for beam management optimization based on beam-level measurements collected by UE measurement report and/or drive test and decide whether to re-train/fine-tune the AI/ML model based on the performance monitoring. Then the trained AI/ML model can be deployed to Near-RT RIC via O1 interface for beam management related inference.

The AI/ML model training and inference to support beam management optimization can be done for different objectives, such as, to reduce beam measurement overhead and to improve the connection reliability, depending on implementation and operator’s requirements. The beam management optimization for different objectives can follow the general process as shown below.

@startuml   
skinparam ParticipantPadding 4   
skinparam BoxPadding 8   
skinparam defaultFontSize 12   
Box “Service Management and Orchestration” #gold Participant CC as “Collection & Control” Participant NON as “Non-RT RIC”   
End box   
Box “O-RAN” #lightpink Participant NEAR as “Near-RT RIC” Participant RAN as “E2 Nodes”   
End box   
Box “External” #lightcyan Participant AS as “Application Server”   
End box   
group Data Collection CC $- >$ RAN : <<O1>>Request data collection for model training RAN $- >$ CC : <<O1>>Data collection group Opt: Enrichment Information Collection (for training) CC $- >$ AS : Request enrichment information AS -> CC : Enrichment information collection (UE position) end CC -> NON: Retrieval of collected data   
end   
group AI/ML Workflow NON $- >$ NON : AI/ML model training NON $- >$ NEAR : <<O1>>Deploy AI/ML model   
end   
group Opt:Enrichment Information Collection (for inference) CC $- >$ AS : Request enrichment information AS -> CC : Enrichment information collection (UE position) CC -> NON : Retrieval of collected data NON $- >$ NEAR : $< < \mathbb { A } 1 > >$ Enrichment information (UE position)   
end   
group E2 Control & Policy NEAR $- >$ RAN : <<E2>>Request data collection for model inference RAN $- >$ NEAR : <<E2>>Data collection NEAR $- >$ NEAR : AI/ML model inference NEAR $- >$ NEAR : E2 control or policy generation NEAR -> RAN : <<E2>>Control or policy message   
end   
group Performance Evaluation and Optimization CC -> RAN : <<O1>>Request data collection RAN $- >$ CC : <<O1>>Data collection group Opt: Enrichment Information Collection (for training) CC $- >$ AS : Request enrichment information AS -> CC : Enrichment information collection (UE position) end CC $- >$ NON : Retrieval of collected data NON $- >$ NON : Performance monitoring and evaluation NON $- >$ NON : AI/ML model retraining and update NON $- >$ NEAR : $< < 0 1 > >$ Update AI/ML model   
end   
@enduml

![](images/7f76efc49afab68432f568a6316e8959db8993b57f46afee98b41790c1b4c653.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4.2.2.1-1. Flow diagram for Non/Near-RT RIC based Beam Selection Optimization

An intelligent solution can be designed and implemented to optimize the beam selection for different objectives. For example, to guarantee the service continuity and eliminate the need for frequent beam measurement, especially for highmobility UE, the xApp deployed in Near-RT RIC can performs AI/ML model inference to support predictive beam switching. Specifically, the AI/ML model could be utilized to predict the changing trend of beams quality in future, which can help BS to perform proactive beam switching or determine a “high-probability” candidate beam set for further measurement. The process to support this example could be as follows,

• The E2 Node (O-DU) receives the following information from the UE o Periodic beam measurements (including L1-RSRP with corresponding CRI or SSBRI) which provide indication of the UE’s best beam ▪ Data regarding beam switch events for UEs which provides predictive intelligence on future beam switching events o Beam failure indications

Data regarding beam failure events which provides intelligence on beam-switching events to potentially be avoided   
E2 Node provides consolidated measurements and data to the Near-RT-RIC and the Non-RT-RIC (through   
SMO)   
Non-RT-RIC obtains other enrichment information (such as UE position and velocity) from an application server   
AI/ML model in Non-RT-RIC is trained based on measurement and enrichment data from (potentially) many E2   
Nodes   
Non-RT-RIC provides AI/ML model update to Near-RT-RIC   
Using the AI/ML model, the Near-RT-RIC provides control information to the E2 Node, specific to a particular   
UE, based on the UE’s historical beam measurement reports, as well as other possible enrichment information.   
The control information could include o New serving beam for UE, or a sequence of future serving beams each with time offsets o Updated beam measurement set for UE

# Requirements

Measurements/reports from E2 Nodes (for AI/ML model training and performance evaluation):

<table><tr><td rowspan=1 colspan=6>Input Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source    →Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod</td><td rowspan=1 colspan=1>Neworexistingmeasurement/reporting specification</td></tr><tr><td rowspan=1 colspan=1>01(viaSMO)</td><td rowspan=1 colspan=1>O-DU →Non-RT RIC</td><td rowspan=1 colspan=1>L1-RSRP measurement at UE-level (in the form of sequence)</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>~X hours/daysper cell(for training)</td><td rowspan=1 colspan=1>Existing definition:3GPP TS 38.214(Sec. 5.2.1.4.3)3GPP TS 38.215(Sec. 5.1.1  and5.1.2)New reporting</td></tr><tr><td rowspan=1 colspan=1>01 (viaSMO)</td><td rowspan=1 colspan=1>O-DU →Non-RT RIC</td><td rowspan=1 colspan=1>L1-SINR measurement at UE-level (in the form of sequence)</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>~X hours/daysper cell(for training)</td><td rowspan=1 colspan=1>Existing definition:3GPP TS 38.214(Sec. 5.2.1.4.4)3GPP TS 38.215(Sec.5.1.5 and5.1.6)New reporting</td></tr><tr><td rowspan=1 colspan=1>01(viaSMO)</td><td rowspan=1 colspan=1>O-DU →Non-RT RIC</td><td rowspan=1 colspan=1>CSI-RS Resource Indicator (CRI)and SS/PBCH Block Resource Indicator (SSBRI) at UE-level (inthe form of sequence)</td><td rowspan=1 colspan=1>Index</td><td rowspan=1 colspan=1>~X hours/daysper cell(for training)</td><td rowspan=1 colspan=1>Existing definition:3GPP TS 38.214(Sec. 5.2.1)New reporting</td></tr><tr><td rowspan=1 colspan=1>01 (viaSMO)</td><td rowspan=1 colspan=1>O-DU →Non-RT RIC</td><td rowspan=1 colspan=1>Average DL UE throughput ingNB</td><td rowspan=1 colspan=1>Kb/s</td><td rowspan=1 colspan=1>~x1hours/daysper cell(forperformanceevaluation)</td><td rowspan=1 colspan=1>Existingdefinitionand reporting:3GPP TS 28.552(Sec. 5.1.1.3.1)</td></tr><tr><td rowspan=1 colspan=1>01 (viaSMO)</td><td rowspan=1 colspan=1>O-DU →Non-RT RIC</td><td rowspan=1 colspan=1>Wideband CQI distribution</td><td rowspan=1 colspan=1>Integer</td><td rowspan=1 colspan=1>~X hours/daysper cell</td><td rowspan=1 colspan=1>Existing definitionand reporting:3GPP TS 28.552(Sec. 5.1.1.11.1)</td></tr></table>

Table 4.2.2.1-1.   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>(forperformanceevaluation)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>01(viaSMO)</td><td rowspan=1 colspan=1>O-DU →Non-RT RIC</td><td rowspan=1 colspan=1>MCS distribution in PDSCH</td><td rowspan=1 colspan=1>Integer</td><td rowspan=1 colspan=1>~X  hours/daysper cell(forperformanceevaluation)</td><td rowspan=1 colspan=1>Existing definitionand reporting:3GPP TS 28.552(Sec. 5.1.1.12.1)</td></tr><tr><td rowspan=1 colspan=1>01 (viaSMO)</td><td rowspan=1 colspan=1>O-DU →Non-RT RIC</td><td rowspan=1 colspan=1>Optional: Beam failure statisticsper cell or per beam</td><td rowspan=1 colspan=1>Count/percent</td><td rowspan=1 colspan=1>~X  hours/daysper cell(forperformanceevaluation)</td><td rowspan=1 colspan=1>New definition andreporting</td></tr></table>

Measurements/reports from E2 Nodes (for AI/ML model inference):

Table 4.2.2.1-2.   

<table><tr><td rowspan=1 colspan=6>Input Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source    →Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod</td><td rowspan=1 colspan=1>New or existingmeasurement/reporting specification</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>O-DU →Near-RT RIC</td><td rowspan=1 colspan=1>L1-RSRP measurement per UE</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>~per N x 100ms</td><td rowspan=1 colspan=1>Existing definition:3GPP TS 38.214(Sec. 5.2.1.4.3)3GPP TS 38.215(Sec. 5.1.1 and5.1.2)New reporting</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>O-DU →Near-RT RIC</td><td rowspan=1 colspan=1>L1-SINR measurement per UE</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>~per N x 100ms</td><td rowspan=1 colspan=1>Existing definition:3GPP TS 38.214(Sec. 5.2.1.4.4)3GPP TS 38.215(Sec. 5.1.5 and5.1.6)New reporting</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>O-DU →Near-RT RIC</td><td rowspan=1 colspan=1>CSI-RS Resource Indicator (CRI)and SS/PBCH Block ResourceIndicator (SSBRI) per UE</td><td rowspan=1 colspan=1>Index</td><td rowspan=1 colspan=1>~per N x 100ms</td><td rowspan=1 colspan=1>Existing definition:3GPP TS 38.214(Sec. 5.2.1)New reporting</td></tr></table>

Enrichment information from application server

The time granularity of these data collections should be configurable and satisfy the requirements of the AI/ML model

1 Output Signalling towards E2 Nodes:

Table 4.2.2.1-3.   

<table><tr><td rowspan=1 colspan=6>Output Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source    →Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod</td><td rowspan=1 colspan=1>New or existingconfigurationspecification</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>Near-RT RIC↓O-CU/DU</td><td rowspan=1 colspan=1>Control/policy related to beammanagement operations (examplesshown as below, details would beFFS)- Beam measurement/reporting:updated beam measurement set,reporting type and periodBeam indication: indicateserving beam for UE- Beam failure recovery: identifythe candidates beams for beamfailure recovery</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>~per N x 100ms</td><td rowspan=1 colspan=1>Existingconfiguration:3GPP TS 38.331(Sec. 6.3.2)Related IE (FFS):CSI-MeasConfigCSI-Report ConfigPDSCH-ConfigBeamFaliureRecoveryConfig3GPP TS 38.321(Sec. 6.1.3.14 and6.1.3.15)</td></tr></table>

1) SMO

a) Collect necessary KPIs, measurement reports and enrichment information (e.g., UE position) from E2 nodes and application server. b) Send collected data to Non-RT RIC for AI/ML model training and performance monitoring.

2) Non-RT RIC

a) Retrieve necessary KPIs, measurement reports and enrichment information (e.g., UE position) from SMO for purpose of constructing/training relevant AI/ML models and performance monitoring.   
b) Monitor performance of the AI/ML models based on the KPIs retrieved from SMO and decide whether to retrain/finetune and update the AI/ML models or not.   
c) Train the relevant AI/ML models using the retrieved data.   
d) Support deployment and update of the AI/ML models into Near-RT RIC over O1 interface.   
e) Support communication of policies and enrichment information to Near-RT RIC over A1 interface.

3) Near-RT RIC

a) Support deployment, update and execution of the AI/ML models from Non-RT RIC.   
b) Support interpretation and execution of the policies from Non-RT RIC.   
c) Collect necessary measurement reports from E2 nodes for the purpose of AI/ML model inference over E2 interface.   
d) Retrieve enrichment information from Non-NT RIC over A1 interface.   
e) Send control or policy message for beam management operation to E2 nodes.

4) E2 nodes

a) Support data collection with required granularity to SMO and Near-RT RIC over O1 and E2 interface. b) Apply L1/L2 beam management parameter configuration based on the control or policy message received from Near-RT RIC.

# Option 2 – E2 Node (O-DU) based Beam Selection Optimization

L1/2 beam management includes a large number of very fast real time functions closely related to the uplink and downlink scheduling in the baseband. The NR L2 scheduling working operates at Transmission Time Interval even lower than 1ms depending on the numerology. It is one of the most demanding and time critical function of the base station that, depending on the bandwidth, will have to handle transmission of multiple GBytes of data traffic. Examples of L1/L2 beam management use cases are beam sweeping, beam measurements, beam reporting, beam acquisition, beam pairing, beam refinement, beam switching, beam indication, beam recovery. Some beam management features may require operating in a faster loop timing than what the E2 loop between Near-RT RIC and E2 Node (e.g, O-DU) allows. Still, AI/ML assisted techniques could achieve substantial gains with acceptable computational costs. In some cases, the ML model might carry intelligence with a local scope, i.e., it adapted to patterns of a single cell on which it was trained.

Therefore, in another deployment option, the operator can leverage on the data collection capabilities of the E2 interface (for ML training) plus the computational capacity (AI/ML framework) of the RIC(s) for ML training, but perform the ML inference in the E2 Node, e.g., in the O-DU (Figure 4.2.2.2-1. middle). ML Deployment Scenario 1.5 (Technical Report O-RAN.WG2.AIML-v01.03) supports training in the Non-RT RIC and inference in the E2 Node. Training in the NearRT RIC and inference in the E2 Node is a new deployment scenario still to be added to respective specifications (Figure 3.4.2.3-1. right). Related impact on O-RAN WGs is analyzed in sections [FFS]. 3GPP RAN WGs will start working on gNB hosted AI/ML algorithms in 3GPP Rel.18. More details are provided in [FFS: 3GPP TR 37.817]. This O-RAN architecture option introduced in this section will complement the 3GPP AI/ML approach (i.e. model hosted in E2 Node) with RIC based training capabilities and the ability to deploy a trained ML model in the E2 node.

![](images/b5bcf044465f7236466eeb13ab1d1e4f4ac32d1104287dd0d2cf70cfc0dcebad.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4.2.2.2-1. Left: O-RAN deployment Option 1 with both training and inference in the Near-RT RIC. Middle and right: Deployment Options 2a and 2b with ML inference in the RAN node (O-DU) for faster control loop.

# 4.2.2.2.1 Additional O-RAN Standardization Impact

# WG2 (Non-RT RIC, A1, R1) Impact

O-RAN.WG2.AIML-v01.03

o Further specify deployment scenario 1.5, with training in the Non-RT RIC and inference in the E2 Node (Option 2a).   
o Specify a new deployment scenario with training (potentially for other than reinforcement ML tasks) in the Near-RT RIC, ML Model management in the Non-RT RIC, and inference in the E2 Node (Option 2b).

No impact identified.

o Trained ML Model transfer from Near-RT RIC to SMO as part of the ML Model management (Option   
2b) – using file transfer. o Trained ML Model deployment from SMO to O-DU as part of the ML Model management (Options   
2a and 2b) – using file transfer.

# Discussion of Architecture Options

Comparing architecture deployment options 1 and 2:

Table 4.2.2.3-1.   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Option 1</td><td rowspan=1 colspan=1>Option 2</td></tr><tr><td rowspan=1 colspan=1>ML Training location</td><td rowspan=1 colspan=1>Non-/Near- RT RIC</td><td rowspan=1 colspan=1>Non-/Near-RT RIC</td></tr><tr><td rowspan=1 colspan=1>ML Inference location</td><td rowspan=1 colspan=1>Near-RT RIC</td><td rowspan=1 colspan=1>E2 Node</td></tr><tr><td rowspan=1 colspan=1>E2 capacity requirements</td><td rowspan=1 colspan=1>high capacity &amp; continuous(ML training &amp; inference)</td><td rowspan=1 colspan=1>flexible capacity &amp; temporary(only for ML training)</td></tr><tr><td rowspan=1 colspan=1>E2 delay requirements</td><td rowspan=1 colspan=1>delay critical</td><td rowspan=1 colspan=1>not delay critical(offline traing)</td></tr><tr><td rowspan=1 colspan=1>Processing capabilities</td><td rowspan=1 colspan=1>higher capacity possible</td><td rowspan=1 colspan=1>capacity limited</td></tr><tr><td rowspan=1 colspan=1>Control loop supported</td><td rowspan=1 colspan=1>slower</td><td rowspan=1 colspan=1>faster</td></tr><tr><td rowspan=1 colspan=1>Scheduler integration of fastalgorithms</td><td rowspan=1 colspan=1>difficult</td><td rowspan=1 colspan=1>easier</td></tr><tr><td rowspan=1 colspan=1>Modelcomplexity   andoptimization scope</td><td rowspan=1 colspan=1>more complex models(incl. multi-cell optimization)</td><td rowspan=1 colspan=1>more simple models(mostly single cell optimization)</td></tr></table>

As can be seen from Table 4.2.2.3-1, the two architecture deployment options target different use cases, have different strengths and weaknesses. Requirements on $\mathrm { g N B }$ processing and on E2 delay and capacity are quite different. The same problem might be addressed with a single cell optimization or a multi-cell optimization, with a more or less complex ML model.

While the realization of $_ { \textrm L 1 / 2 }$ beam management algorithms might sometimes be limited to one of the options (e.g. due to delay or interface constrains), some algorithms might also possibly be realized with both options. Considering that L1/2 beam management techniques are very fast algorithms tightly integrated in the L2 scheduler design, it will be the vendor that evaluates the gain versus the complexity. While a small cell may have very limited processing and backhaul capabilities, a macro base station site might have such capability. This means both architecture options are viable options for L1/2 beam management algorithms and may even co-exist. The standard should not mandate the one or the other option, but it should be up to the vendor to make this decision. This leaves room for enhancements over time and for operators to choose different deployment options.

# 4.2.3 Impact Analysis on O-RAN Working Groups

Editor’s note: This is an initial impact analysis as part of the WG1 UCTG work on mMIMO. The intention is to estimate the expected standardization effort within the O-RAN working groups. It is up to the WGs to decide how the mMIMO functionality should be specified in specifications of each WG.

5 WG1 (use cases, architecture) Impact

• O-RAN.WG1.Use-Cases-Analysis-Report o Update use case 6: Massive MIMO Beamforming Optimization (Section 3.6)   
O-RAN.WG1.Use-Cases-Detailed-Specification o Update use case 6: Massive MIMO Beamforming Optimization (Section 3.6)

# WG2 (Non-RT RIC, A1) Impact

• O-RAN.WG2.Use-Case-Requirements o If seen as beneficial, add new use case 6: Massive MIMO Beamforming Optimization based on agreements from pre-normative phase O-RAN.WG2.A1TD o Support exchange of relevant Enrichment Information from Non-RT to Near-RT RIC

# WG3 (Near-RT RIC, E2) Impact

O-RAN.WG3.UCR o If seen as beneficial, add new use case 6: Massive MIMO Beamforming Optimization based on agreements from pre-normative phase • O-RAN.WG3.E2SM-KPM o For cell-level measurements that are specified in 3GPP (i.e. 3GPP TS 28.552), there would be minor or no direct specification impact. The optional new beam failure statistics might be specified in 3GPP or in O-RAN (FFS). o For UE-level L1/L2 measurements □ Option 1: If UE-level L1/L2 measurement reporting is added to the 3GPP specification (e.g. 3GPP TS37.320), E2 could refer to 3GPP specification and there will be minor or no direct specification impact. Option 2: If UE-level L1/L2 measurement reporting is not added to the 3GPP specifications, O-RAN specific reporting need to be added. Given that measurement definitions already exist in 3GPP, the impact will be minor (noting that E2SM-KPM has already extended the definitions of measurement counters in TS 28.552 to be able to be retrieved per UE level from RAN node).

• O-RAN.WG3.E2SM-RC or creation of new E2SM o Add new control/policy related to beam management operation

# WG5 (O1) Impact

# O-RAN.WG5.MP

o For cell-level measurements that are specified in 3GPP (i.e. 3GPP TS 28.552), there would be minor or no direct specification impact. The optional new beam failure statistics might be specified in 3GPP or in O-RAN (FFS).   
o For UE-level L1/L2 measurements Option 1: If UE-level L1/L2 measurement reporting is added to the 3GPP specification (e.g. 3GPP TS37.320), O1 could refer to 3GPP specification and there will be minor or no direct specification impact. □ Option 2: If UE-level L1/L2 measurement reporting is not added to or re-used from the 3GPP specifications, O-RAN would add reporting of these as an extension of O1. Given that measurement definitions already exist in 3GPP, the impact will be moderate,

Summary: The overall impact on O-RAN specifications is limited, since all the measurement definitions are already defined in 3GPP. There is a new cell level measurement beam failure statistic suggested that is optional. The detailed impact might further depend on if required enhancements of measurement reporting (especially UE-level L1/L2 measurements) will be specified in 3GPP or O-RAN specifications. There might be some common parts on specification impact among different sub-features, which may further reduce the overall workload in the normative phase.

# 4.2.4 Relation and Impact on 3GPP Specification

In 3GPP, the beam management procedures that control the determination and maintenance of the serving beam(s) for each UE within a cell has been firstly specified in Release 15 and further enhanced in Release 16 and 17. The existing 3GPP standard already support good flexibility of UE-specific configuration in terms of beam measurement/reporting, beam indication and beam failure recovery with regard to fundamental beam-based transmission/reception. To support the L1/L2 beam management optimization in O-RAN would mainly rely on the existing 3GPP standards, and the detailed impact is listed as below,

Data collection:

Cell-level measurements: The definition and reporting of essential measurements is already existing in 3GPP specification (3GPP TS 28.552). Whether and how to support the new measurements which is not essential could be FFS.   
UE-level L1/L2 measurements: The measurements definition is already existing in 3GPP specifications, and the measurements reporting might be added to the existing 3GPP MDT framework (3GPP TS 37.320) or might be added in a new AI/ML Data Collection framework currently discussed in 3GPP. Whether rely on 3GPP or introduce O-RAN specific reporting could be FFS.

Configuration/Control:

• The control will rely on the existing control signaling (3GPP TS 38.331/38.321)

# 4.2.5 Feasibility and Gain/Complexity Analysis

In mmWave bands, supporting good reliability of connectivity for high mobility UE is challenging. The network needs to rely on frequent beam measurement to track the rapid change of wireless channel, which will require significant signaling overhead. However, UEs with high mobility move along relatively fixed trajectory in many cases. For example, a vehicle traveling at high speed mostly will not suddenly change its driving direction. Therefore, although the optimal beam changes rapidly under the UE’s high-speed movement, the trend of change is predictable. The xApp deployed in Near-RT RIC can be used to perform AI/ML model inference to predict the changing trend of beams quality in future, which can help BS to reduce the frequency of beam measurements and/or reduce the number of measured beams.

# Simulation Results

The following part of this section presents the simulation results which show the benefits of beam prediction under an urban street scenario (depicted in Figure 4.2.5.1-1). Within the simulation, vehicular UEs moving along the urban street which is served by one BS, and the BS periodically sends reference signals on all the candidate beams to UE for beam measurement. In the case of the conventional beam switching solution, which is reactive, the BS will configure serving beam for UE according to the most recent beam measurement result. In the case of the AI/ML-based beam solution, which is proactive, the optimal serving beams (i.e., beams sequence with time offset) before the next time of beam measurement can be predicted accurately in advance based on the historical beam measurement report, so that the BS can configure serving beams for UE by following this prediction. The simulation assumptions and results are shown in Table 4.2.5.1-1 and Figure 4.2.5.1-2 respectively.

![](images/d7d2b9d395a84507d6f841f12b02cc38d479c38cb2b97489812948fec6467561.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4.2.5.1-1. Vehicular UEs moving along the urban street in both directions

Table 4.2.5.1-1. Simulation assumptions   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Value</td></tr><tr><td rowspan=1 colspan=1>Frequency band</td><td rowspan=1 colspan=1>28 GHz</td></tr><tr><td rowspan=1 colspan=1>Bandwidth</td><td rowspan=1 colspan=1>100MHz</td></tr><tr><td rowspan=1 colspan=1>BS Trans. power</td><td rowspan=1 colspan=1>33dBm</td></tr><tr><td rowspan=1 colspan=1>BS height</td><td rowspan=1 colspan=1>6m</td></tr><tr><td rowspan=1 colspan=1>BS antenna configuration (M x N)</td><td rowspan=1 colspan=1>8 x 16 antennas</td></tr><tr><td rowspan=1 colspan=1>Beam set configuration</td><td rowspan=1 colspan=1>64 beams uniformly distribute in horizontalwith 5 degrees down tilt</td></tr><tr><td rowspan=1 colspan=1>Beam measurement period</td><td rowspan=1 colspan=1>50/500/1000ms</td></tr><tr><td rowspan=1 colspan=1>Beam measurement report</td><td rowspan=1 colspan=1>Best beam index with L1-RSRP</td></tr><tr><td rowspan=1 colspan=1>UE velocity</td><td rowspan=1 colspan=1>60km/h</td></tr><tr><td rowspan=1 colspan=1>Mobility model</td><td rowspan=1 colspan=1>UEs moving along the urban street in bothdirections (moving trajectory is randomlygenerated with different starting/end point)</td></tr><tr><td rowspan=1 colspan=1>Channel model</td><td rowspan=1 colspan=1>Generated by ray-tracing based simulator</td></tr></table>

![](images/8e5fc8ec0e6cf65a512012ccb073f7cf4d030bbc9fac6348323fb09422b45da3.jpg)

> **Image Summary:** (Summary not available)
  
Figure 4.2.5.1-2. CDF of serving beams RSRP

The simulation result in Figure 4.2.5.1-2 shows the CDF curves of serving beams’ RSRP for the different beam measurement periods. It can be seen that the conventional beam switching solution (indicated by “Baseline”) heavily rely on the frequent beam measurement reports and the quality of selected beams are severely degraded according to the increase of measurement period. On the other hand, the AI/ML-based beam switching solution can predict the optimal beam with high accuracy only based on the historical beam measurement reports. By comparing the performance of these two solutions, it shows that the AI/ML-based solution can achieve near-optimal beam tracking performance under the condition of beam measurement period of $1 0 0 0 ~ \mathrm { { m s } }$ , while the conventional solution requires the beam measurement period of $5 0 ~ \mathrm { m s }$ . The signaling overhead of beam measurement in the AI/ML-based solution is reduced by as much as $9 5 \%$ compared to the conventional solution.

It is worth noting that the performance of simulated AI/ML-based solution do not sensitive to the latency introduced by E2 interface and/or E2-nodes/RIC processing time because the solution does not rely on very fast control loop.

# 5 Non-GoB Beamforming

# 5.1 Overview

Non-GoB Beamforming, unlike GoB beamforming, does not rely on predefined beam sets, instead beam weights are determined in real-time at the BS in response to channel measurements, offering the potential for optimum beam patterns to be determined. For downlink, this approach relies on reciprocity in the channel and is therefore primarily aimed at TDD systems. How well the system performs in practice depends on several factors including choice of beamforming algorithm, the channel conditions between BS and UE and the configuration of reference signals. The O-RAN architecture offer opportunities to improve the beamforming performance by utilizing both Non-RT RIC and Near-RT RIC to support intelligent optimization of the Non-GoB beamforming configuration.

# 5.2 Solution 1: AI/ML-assisted non-GoB Optimization

# 5.2.1 Problem Statement and Value Proposition

Non- Grid of Beams (non-GoB) beamforming approaches are an important class of beamforming algorithms for 5G mMIMO deployments, especially for fully digital, but also potentially for hybrid analog/digital, implementations in sub6GHz frequency bands. Typically Sounding Reference Symbol (SRS) based approaches are used, which rely on uplink/downlink correspondence, where uplink and downlink beam weights are computed “on the fly” in the O-DU / gNB based on channel measurements made using SRS, rather than selecting from a set of predefined beams. The calculated weights are transferred from O-DU / gNB to the O-RU using existing fronthaul mechanisms. SRS based beamforming is particularly attractive for massive MIMO arrays because accurate channel state information can be obtained at the gNB with potentially less overhead in the DL or UL channels. gNB uplink SRS measurements generally have no quantization loss associated with reduction of over the air signaling and are faster availability for downlink adaptation since measurement is done in gNB. On the other hand, SRS measurements might not always be recently available (due to SRS periodicity and/or limited bandwidth), or reliable, especially towards cell edge since the UE transmit power in the uplink is limited.

It should be noted that non-GoB algorithms are not standardized, instead these are vendor-specific proprietary algorithms. In addition, multiple algorithm modes or options may be implemented, where some modes may be more suited to particular conditions of the wireless channel, UE location/mobility, interference conditions, or to particular 3GPP configuration options such as SRS periodicity. Examples of beamforming modes include but are not limited to: the use of different SRS channel estimation algorithms; different weight calculation approaches (for example matched filter, Eigen, Zero-forcing beamforming); and different time or frequency granularity.

Non-GoB beamforming may be applicable to multiple MIMO modes (SIMO, SU-MIMO or MU-MIMO) on the downlink or uplink data channels (PDSCH/PUSCH). GoB beamforming will be used for other channels and may also be used for data channels in some cases where, for example, SRS measurement quality is poor.

The problem statement is therefore how a 3rd-party xApp may provide intelligent control over multiple supported nonGoB beamforming modes in order to recommend a preferred mode to a gNB / O-DU as a function of channel conditions, UE location, interference conditions, etc.

# 5.2.2 Architecture/Deployment Options

# Option 1

It is assumed in this description that SMO/Non-RT RIC is responsible for obtaining beamforming configuration information from the gNB / O-DU, and for model training, and model deployment of the xApp to the near-RT RIC. The near-RT RIC performs model inference and provides control messages to the gNB / O-DU. AI/ML-enabled control of non-GoB beamforming configuration options is performed in the xApp to optimize a measure of performance (for example UE throughput), given UE/cell conditions. It should be noted that the low-latency beamforming weight calculation loop still resides in DU. xApp sits outside/above this loop and recommends configuration on a slower basis than the weight calculation loop.

Referring to Figure 5.2.2.1-1, non-RT RIC first requests a report of supported beamforming configurations in the O-DU (referred to as “non-GoB mMIMO Config” in the diagram), and O-DU provides the requested report for the supported modes. This is done using the O1 interface, via SMO “Collection & Control” function, since non-RT does not terminate O1.

The reported information could be as simple as the number of modes supported $\left( = \mathrm { N } \right)$ . The modes are defined by the gNB / O-DU vendor. Optionally, there could be additional information provided, such as the circumstances in which use of each of the N modes is considered (by the $\mathrm { g N B }$ / O-DU) to be suitable (for example low or high mobility, low, medium or high SNR on (for example) SRS), which is illustrated in Table 5.2.2.1-1.

Table 5.2.2.1-1.   

<table><tr><td rowspan=1 colspan=1>Mode ID</td><td rowspan=1 colspan=1>UL or DL</td><td rowspan=1 colspan=1>SNR         range(low/med/high)</td><td rowspan=1 colspan=1>UE            Mobility(stationary/low/high)</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>:</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>N-1</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

GoB-based approaches could be included as supported modes, thus enabling switch between non-GoB and GoB operation where conditions favor GoB (for example at cell-edge).

Next, the Data Collection phase is entered, where non-RT RIC requests data collection from O-DU, again using O1 via the “Collection and Control” function. The O-DU responds with measurements over O1, such as SINR, the measurements being associated with each of the N beamforming modes (labelled “associated non-GoB mMIMO config” in the diagram). Specific measurements defined in 3GPP 28.522 may be re-used, for example, for downlink operation: Average DL UE throughput in gNB; Wideband CQI distribution; RSRQ measurement; RSRP measurement; SINR measurement. Information related to 3GPP configuration, such as SRS periodicity, is also reported.

During the data collection phase, enrichment data, such as information related to UE location and mobility, may also be collected from an Application Server. The non-RT RIC associates enrichment data with the corresponding O-DU measurements, such that both are available for each UE.

In the next step, the non-RT RIC trains AI/ML model(s) which will be used to predict relative performance between the N modes (or simply to predict the best mode) and deploys the trained models in xApp to near-RT RIC (over O1 or $\mathrm { O } 2 -$ to be determined by O-RAN).

Finally, models may be re-trained and re-deployed based on updated measurements sent between O-DU and non-RT RIC (via the “Collection and Control” entity) and on updated enrichment information.

@startuml   
skinparam ParticipantPadding 5   
skinparam BoxPadding 10   
skinparam defaultFontSize 12   
Box “Service Management and Orchestration” #gold Participant “Collection & Control” as smo Participant “Non-RT RIC” as non   
End box   
Box “O-RAN” #lightpink Participant near as “Near-RT RIC” Participant ran as “O-DU”   
End box   
Box “External” #lightcyan Participant “Application Server” as app   
End box   
group Non-GoB mMIMO Configuration Report non --> smo : Request non-GoB mMIMO Config smo --> ran : $< < 0 1 > >$ Request non-GoB mMIMO Config ran --> smo : $< < 0 1 > >$ Report non-GoB mMIMO Config smo --> non : Report non-GoB mMIMO Config   
end   
group Data Collection non --> smo : Request Training Data Collection smo --> ran : Non-GoB mMIMO Training Measurement Configuration ran --> smo : $< < 0 1 > >$ Data collection (measurements with associated non-GoB mMIMO config) app --> smo : Enrichment data collection (location/mobility) smo --> non : Retrieval of collected data   
end   
group ML workflow non $- >$ non : Association of Enrichment data with O-DU Measurements non $- >$ non : Training of ML models non $- >$ near: $< < 0 1 > >$ or $< < 0 2 > >$ Deploy AI/ML models   
end   
group Performance evaluation and optimization ran --> smo : $< < 0 1 > >$ Data collection (measurements with associated non-GoB mMIMO config) app --> smo : Enrichment data collection (location/mobility) smo $- >$ non : Data retrieval of RAN non $- >$ non : Performance monitoring & evaluation non $- >$ non : Model re-training/update non $- >$ near: $< < 0 1 > >$ or $< < 0 2 > >$ Update AI/ML models   
end   
@enduml

![](images/94e09760166f7567aa80e504e4fe584b896a8a5f92d72f3a754d2438d146fd96.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.2.2.1-1. Configuration Report, AI/ML training and deployment.

Referring to Figure 5.2.2.1-2, the near-RT RIC xApp performs AI/ML model inference using models previously deployed from non-RT RIC. Enrichment data is provided from non-RT RIC via A1, and measurements (such as SINR) and SRS configuration information is obtained from O-DU over E2. Association of measurements and enrichment data is performed by near-RT RIC. The recommended beamforming mode(s) (out of N) is provided from near-RT to O-DU over E2 (“mMIMO non-GoB control or policy message” in the diagram). The O-DU can then configure the non-GoB beamforming algorithm taking account of the mode received from near-RT RIC. In exceptional circumstances in case the O-DU is not able to apply the signaled mode then a failure indication could be returned by the O-DU. The xApp may maintain statistics about success/failure rates. Optionally, the beamforming mode recommendation may be selected by the near-RT RIC in order to improve the training data set, which could be used, for example, in the case of reinforcement learning based implementations.

@startuml   
skinparam ParticipantPadding 5   
skinparam BoxPadding 10   
skinparam defaultFontSize 12   
Box “Service Management and Orchestration” #gold Participant “Collection & Control” as smo Participant “Non-RT RIC” as non   
End box   
Box “O-RAN” #lightpink Participant near as “Near-RT RIC” Participant ran as “O-DU”   
End box   
Box “External” #lightcyan Participant “Application Server” as app   
End box   
app --> smo : Enrichment data collection (location/mobility)   
smo --> non : Retrieval of collected data   
non --> near : $< < \mathbb { A } 1 > >$ Enrichment data (location/mobility)   
group E2 control & Policy near --> ran : <<E2>> Non-GoB mMIMO Measurement Configuration ran --> near : $< < \tt E 2 > >$ Data collection (measurements) near $- >$ near: Association of Enrichment data with O-DU Measurements near $- >$ near : ML model inference near $- >$ near : E2 control or policy generation near -> ran: $< < \tt E 2 > >$ mMIMO non-GoB control or policy message   
end   
@enduml

![](images/cb7ce25f201329f7151bcec69423004cc3fbc1099c77c14f87b74608830c8dc7.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.2.2.1-2. AI/ML Inference

# 1 Requirements

Required data:

Initialization:

5

Table 5.2.2.1-2.   

<table><tr><td rowspan=1 colspan=6>Input/Output Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source     →Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>Config.      Period,granularity</td><td rowspan=1 colspan=1>New    orexistingconfig</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>Non-RT RIC →O-DU</td><td rowspan=1 colspan=1>Supported Non-GoB beamforming modesRequest</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Initialization, per gNB</td><td rowspan=1 colspan=1>New</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>O-DU→ Non-RT RIC</td><td rowspan=1 colspan=1> Supported Non-GoB beamforming modesResponse</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Initialization, per gNB</td><td rowspan=1 colspan=1>New</td></tr></table>

4

6 Training configuration:

Table 5.2.2.1-3.   

<table><tr><td rowspan=1 colspan=6>Input/Output Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source     →Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>Config.Period,granularity</td><td rowspan=1 colspan=1>New or existing config</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>Non-RT RIC →O-DU</td><td rowspan=1 colspan=1>Training configuration</td><td rowspan=1 colspan=1>*</td><td rowspan=1 colspan=1>~hours/days,per gNB</td><td rowspan=1 colspan=1>New</td></tr></table>

Note\*: to be elaborated during normative phase. One example is a schedule for the use of each beamforming mode for use during the training phase.

1 Measurements/reports from E2 Nodes (training phase):

Table 5.2.2.1-4.   

<table><tr><td rowspan=1 colspan=6>Input Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source      →Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod,granularity</td><td rowspan=1 colspan=1>New    or    existingmeasurement,Existing Specification(Section)</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>O-DU → Non-RT RIC</td><td rowspan=1 colspan=1>Average DL UE throughput in gNB withassociated non-GoB mMIMO mode</td><td rowspan=1 colspan=1>Kb/s +index</td><td rowspan=1 colspan=1>(non real-time  fortraining)</td><td rowspan=1 colspan=1>Existing definition3GPP TS 28.552(Sec. 5.1.1.3.1)Require new  per-UEreporting. New componentis associated1non-GoBmMIMO mode index</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>O-DU → Non-RT RIC</td><td rowspan=1 colspan=1>Average UL UE throughput in gNB withassociated non-GoB mMIMO mode</td><td rowspan=1 colspan=1>Kb/s +index</td><td rowspan=1 colspan=1>(non real-time   fortraining)</td><td rowspan=1 colspan=1>Existing definition3GPP TS 28.552(Sec. 5.1.1.3.3)Require new per-UEreporting. New componentis associated non-GoBmMIMO mode index</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>O-DU → Non-RT RIC</td><td rowspan=1 colspan=1>RSRQ L1 measurement(basedonSynchronization Signal)</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>(nonreal-time   fortraining)</td><td rowspan=1 colspan=1>Existing definition3GPP TS 38.133(Sec. 10.1.11)3GPP TS 38.215(Sec.5.1.3)New reporting</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>O-DU → Non-RT RIC</td><td rowspan=1 colspan=1>RSRP L1measurement (basedonSynchronization Signal)</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>(non real-time   fortraining)</td><td rowspan=1 colspan=1>Existing definition3GPP TS 38.133(Sec. 10.1.6)3GPP TS 38.215(Sec.5.1.1)New reporting</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>O-DU → Non-RTRIC</td><td rowspan=1 colspan=1>DL L1 SINR measurement (based onSynchronization Signal)</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>(nonreal-time   fortraining)</td><td rowspan=1 colspan=1>Existing definition3GPP TS 38.133(Sec. 10.1.16)3GPP TS 38.215(Sec.5.1.5)New reporting</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>O-DU → Non-RT RIC</td><td rowspan=1 colspan=1>UL SRS RSRP measurement</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>(nonreal-time   fortraining)</td><td rowspan=1 colspan=1>Existing definition3GPP TS 38.133(Sec. 13.3.1)3GPP TS 38.215(Sec. 5.2.5)New reporting</td></tr><tr><td rowspan=1 colspan=1>01   viaSMO</td><td rowspan=1 colspan=1>O-DU → Non-RT RIC</td><td rowspan=1 colspan=1>SRS configuration periodicity</td><td rowspan=1 colspan=1>slots</td><td rowspan=1 colspan=1>(non real-time  fortraining)</td><td rowspan=1 colspan=1>Existing definition3GPP TS 38.331(Sec. 6.3.2 SRS-Config-&gt;periodicityAndOffset&quot;)New reporting</td></tr></table>

1 Measurements/reports from E2 Nodes (inference phase):

Table 5.2.2.1-5.   

<table><tr><td rowspan=1 colspan=6>Input Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source      →Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>ReportingPeriod,granularity</td><td rowspan=1 colspan=1>New    or    existingmeasurement,Existing Specification(Section)</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>O-DU → Near-RT RIC</td><td rowspan=1 colspan=1>RSRQ L1 measurement (basedonSynchronization Signal)</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>~per N x100ms, perUE</td><td rowspan=1 colspan=1>Existing definition3GPP TS 38.133(Sec. 10.1.11)3GPP TS 38.215(Sec. 5.1.3)New reporting</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>O-DU → Near-RT RIC</td><td rowspan=1 colspan=1>RSRPL1 measurement (basedonSynchronization Signal)</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>~per N100ms, perUE</td><td rowspan=1 colspan=1>Existing definition3GPP TS 38.133(Sec. 10.1.6)3GPP TS 38.215(Sec. 5.1.1)New reporting</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>O-DU → Near-RT RIC</td><td rowspan=1 colspan=1>DL L1 SINR measurement (based onSynchronization Signal)</td><td rowspan=1 colspan=1>dB</td><td rowspan=1 colspan=1>~per NX100ms, perUE</td><td rowspan=1 colspan=1>Existing definition3GPP TS 38.133(Sec. 10.1.16)3GPP TS 38.215(Sec. 5.1.5)New reporting</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>O-DU → Near-RT RIC</td><td rowspan=1 colspan=1>UL SRS RSRP measurement</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>~per N x100ms, perUE</td><td rowspan=1 colspan=1>Existing definition3GPP TS 38.133(Sec. 13.3.1)3GPP TS 38.215(Sec. 5.2.5)New reporting</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>O-DU → Near-RT RIC</td><td rowspan=1 colspan=1>SRS configuration periodicity</td><td rowspan=1 colspan=1>slots</td><td rowspan=1 colspan=1>~per N x100ms, perUE</td><td rowspan=1 colspan=1>Existing definition3GPP TS 38.331(Sec. 6.3.2 &quot;SRS-Config-&gt;periodicityAndOffset&quot;)New reporting</td></tr></table>

Whether additional filtering of L1 measurements is required in O-DU is for further study during the normative phase.

Enrichment data from Application Server:

1. UE mobility (speed and direction)   
2. UE location   
3. The time granularity is an integer multiple of [1] second.

1 Output Signalling towards E2 Nodes:

Table 5.2.2.1-6.   

<table><tr><td rowspan=1 colspan=6>Output Data</td></tr><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source     →Target</td><td rowspan=1 colspan=1>Name/Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>Config.Period,granularity</td><td rowspan=1 colspan=1>New or existing config</td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>Near-RT RIC →O-DU</td><td rowspan=1 colspan=1>Non-GoB  control/policy  (non-GoBbeamforming mode)</td><td rowspan=1 colspan=1>index</td><td rowspan=1 colspan=1>~per N x100ms, perUE</td><td rowspan=1 colspan=1>New</td></tr></table>

ORAN Entity roles:

1) SMO

a) Support O1-based Request and Report of O-DU supported non-GoB mMIMO configurations (beamforming modes)   
b) Support O1-based Configuration and Collection of Training Measurement data / SRS configuration from ODU   
c) Enrichment Data Collection

2) Non-RT RIC

a) Issue Request and receive Report of O-DU non-GoB beamforming modes from O-DU through SMO   
b) Configuration and retrieval of Training Measurement Data from O-DU   
c) Enrichment Data Retrieval   
d) Perform association of Training Measurement Data and Enrichment Information   
e) Model training/re-training   
f) Model xApp deployment/re-deployment   
g) Send Enrichment Data to near-RT RIC over A1   
h) Performance monitoring and evaluation

3) Near-RT RIC

a) Retrieval of Enrichment Data over A1   
b) Retrieval of ML Models from the Non-RT RIC   
c) Retrieval of O-DU measurements/SRS configuration over E2   
d) Association of E2 Measurement Data and Enrichment Data   
e) Model inference by xApp   
f) Send non-GoB control/policy (recommendation of non-GoB beamforming mode) to O-DU over E2

4) E2 nodes

a) Respond to O1-based Request by sending Report of O-DU supported non-GoB mMIMO configurations (beamforming modes) over O1   
b) Respond to O1-based Configuration and Report of Training Measurement data / SRS configuration over O1   
c) Collect and report measurements (with associated beamforming mode)/SRS configuration over E2 to Near-RT RIC   
d) Apply non-GoB control/policy (non-GoB beamforming mode) received over E2

# 5.2.3 Impact Analysis on O-RAN Working Groups

Editor’s note: This is an initial impact analysis as part of the WG1 UCTG work on mMIMO. The intention is to estimate the expected standardization effort within the O-RAN working groups. It is up to the WGs to decide how the mMIMO functionality should be specified in specifications of each WG.

# WG2 (Non-RT RIC, A1) Impact

• O-RAN.WG2.Use-Case-Requirements o If seen as beneficial, add new use case: Massive MIMO non-Grid-of-Beams Beamforming Optimization based on agreements from pre-normative phase O-RAN.WG2.A1 TD o Support exchange of relevant Enrichment Data from non-RT to near-RT RIC

# WG3 (Near-RT RIC, E2) Impact

• O-RAN.WG3.UCR

o Add new use case: Massive MIMO non-Grid-of-Beams Beamforming Optimization based on agreements from pre-normative phase O-RAN.WG3.E2SM-KPM o Option 1: If UE specific L1/2 measurement reporting is added to the 3GPP specification (e.g. 3GPP TS37.320 section 5.4.1.), E2 will refer to 3GPP spec and there will be minor or no impact on E2SMKPM specifications. o Option 2: If UE specific L1/2 measurement reporting is not added to the 3GPP specifications, “O-RAN specific” measurements need to be added to E2SM-KPM. Considering that measurement definitions exist in 3GPP the effort will be minor, noting that E2SM-KPM has already extended the definitions of measurement counters in TS 28.522 to be able to be retrieved per UE level from RAN node. o Note that there will likely be some commonality with other use cases

O-RAN.WG3.E2SM-RC or any other suitable E2SM o Add new Non-GoB control/policy (non-GoB beamforming mode) in direction near-RT RIC to O-DU

# WG5 (O1) Impact

O-RAN.WG5.MP O1 Interface specification for O-DU o Option 1: If UE specific L1/2 measurement reporting is added to the 3GPP specification (e.g. 3GPP TS37.320 section 5.4.1.), O1 could refer to 3GPP spec and there could be very limited or no impact on O1 specifications. o Option 2: If UE specific L1/2 measurement reporting is not added to or re-used from the 3GPP specifications, O-RAN would add reporting of these as an extension of O1. As the measurement definitions already exist, the impact will be moderate. o Similarly, initialization/training configuration might also be specified in 3GPP and/or in O-RAN (using type “O-RAN WG5 modified model based on 3GPP SA5” as defined in chapter 10). Supported Non-GoB beamforming modes Request in direction SMO to O-DU Supported Non-GoB beamforming modes Response in direction O-DU to SMO Training configuration in direction SMO to O-DU (exact definition is FFS, one example being a schedule for the application of different beamforming modes during training phase).

Summary: The impact on O-RAN E2 specification is small. For O1, the impact on O-RAN specification is small in case measurement reporting/configuration management are specified in 3GPP and referred to by O-RAN specifications, and moderate if the reporting of new required per-UE L1/L2 measurements and related configuration management are specified in O-RAN.

# 5.2.4 Relation and Impact on 3GPP Specification

Per-UE L1/2 measurement reporting might be added to the existing 3GPP MDT framework or might be added in a new AI/ML Data Collection framework currently discussed in 3GPP.

The 3GPP MDT framework is defined in 3GPP TS37.320 for UMTS, LTE and NG Radio Access. There are UE specific signal measurements defined with reference to 3GPP TS38.215. The handling and management of MDT traces are specified in 3GPP TS32.421, TS32.422, TS32.423 as well as TS32.445, TS32.446 etc.

In terms of a new AI/ML motivated measurement framework, related work is already underway in 3GPP RAN3 and SA5, for example in the Study on enhancement for Data Collection for NR and EN-DC, which is being documented in 37.817. Further work might be considered, for example as proposed in the recent Study Item proposal (S5-215397, “New SID Study on measurement data collection to support RAN intelligence”). Support of new reporting of UE-specific L1/2 measurements in direction O-DU to non- RT RIC and near-RT RIC is therefore FFS.

In terms of configuration/control, it is FFS whether 3GPP will specify the following:

Supported Non-GoB beamforming modes Request in direction SMO to O-DU Supported Non-GoB beamforming modes Response in direction O-DU to SMO Training configuration in direction SMO to O-DU

The current working assumption is that these will first be specified by O-RAN WG5 in which case there is no dependency on 3GPP progress (noting however that additional instances are expected to be proposed to 3GPP for having alignment of the information models between 3GPP and O-RAN WG5).

# 5.2.5 Feasibility and Gain/Complexity Analysis

# Simulation Results

Simulation results are provided for the assumptions shown in Table 5.2.5.1-1.   
Table 5.2.5.1-1. Simulation Assumptions   

<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>Cell</td><td rowspan=1 colspan=1>Single cell, 120-degree sector, 300m radius</td></tr><tr><td rowspan=1 colspan=1>Channel model</td><td rowspan=1 colspan=1>Based on 3GPP non-line of sight CDL, with path gains and angles computed forrandom spatial placement of scatterers and static blockers.</td></tr><tr><td rowspan=1 colspan=1>Pathloss</td><td rowspan=1 colspan=1>Macro model per 3GPP TR 36.931</td></tr><tr><td rowspan=1 colspan=1>Angular spread at BS</td><td rowspan=1 colspan=1>~25 degrees</td></tr><tr><td rowspan=1 colspan=1>MIMO Mode</td><td rowspan=1 colspan=1>Downlink, SU-MIMO, 2 layers fixed (i.e. no adaptation of layers, pre-coding, noscheduling, etc.)</td></tr><tr><td rowspan=1 colspan=1>Beamforming modes</td><td rowspan=1 colspan=1>Mode 0: SRS-basedMode 1: GoB-based</td></tr><tr><td rowspan=1 colspan=1>Relative SNR DL PDSCH toUL SRS channel estimate</td><td rowspan=1 colspan=1>+10 dB, takes account of relative noise figures and output powers between gNB andUE (UL Transmit Power Control not modelled)</td></tr><tr><td rowspan=1 colspan=1>gNB antenna array</td><td rowspan=1 colspan=1>32 elements x 2 polarization panel antenna</td></tr><tr><td rowspan=1 colspan=1>UE antenna array</td><td rowspan=1 colspan=1>1 element x 2 polarizations</td></tr><tr><td rowspan=1 colspan=1>SRS periodicity</td><td rowspan=1 colspan=1>8 slots</td></tr><tr><td rowspan=1 colspan=1>Carrier Frequency</td><td rowspan=1 colspan=1>3.5 GHz</td></tr><tr><td rowspan=1 colspan=1>Output metric</td><td rowspan=1 colspan=1>Simulated channel capacity</td></tr></table>

Simulated downlink capacity for one example randomly dropped cell is shown for low $\left( 1 \mathrm { { k m } / h } \right)$ and high $\mathbf { 1 2 0 ~ k m / h } )$ (d mobility scenarios, in the heatmaps in Figure 5.2.5.1-1, and in CDFs of relative throughputs in Figure 5.2.5.1-2 and in Figure 5.2.5.1-3.

![](images/a53c58cc95446a8f0fcd803047a909f90e1fccc09672452ed7209b5cf7cb15e3.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.2.5.1-1. Heatmaps. Brighter colors represent higher throughputs.

b) High mobility

![](images/7658975d60af307dccaf70b297d4e520718d906c9eb711f0fc80768d0c74a11c.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.2.5.1-2. Relative PDSCH throughput CDF, low mobility.

2

3

![](images/d04ce16e90a6884bd379e0170f2530ae98fc1b56300ca97e031a82dc728daba7.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.2.5.1-3. Relative PDSCH throughput CDF, low mobility.

The achieved throughput depends on UE location and mobility. The throughput pattern is not uniform across angles due to random placement of scatterers and blockers within the cell.

Mode 0 performs best towards the center of the cell and mode 1 towards cell edge, however the cross-over point depends on mobility, with mode 0 performing worse in the high mobility scenario.

Table 5.2.5.1-2 and Table 5.2.5.1-3 compare average, 5-percentile and 95-percentile relative throughputs for PDSCH for modes 0 and 1, and for an ideal intelligent mode selection, for low and high mobility cases respectively. The opportunity for intelligent mode selection is a substantial increase in throughput relative to either a fixed configuration of mode-0 or mode-1.

It is worth noting that these results are for a single fixed assumed SRS periodicity (8 slots). The cross-over points between mode 0 and mode 1 would also likely have a dependency on SRS periodicity.

Table 5.2.5.1-2. Average, 5-percentile and 95-percentile relative PDSCH throughputs, low mobility   

<table><tr><td rowspan=1 colspan=1>Mode</td><td rowspan=1 colspan=1>RelativeAv. cellthroughput%</td><td rowspan=1 colspan=1>Relative 5-percentilecellthroughput%</td><td rowspan=1 colspan=1>Relative 95-percentilecellthroughput%</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>100.0000</td><td rowspan=1 colspan=1>100.0000</td><td rowspan=1 colspan=1>100.0000</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>72.8874</td><td rowspan=1 colspan=1>159.9304</td><td rowspan=1 colspan=1>55.7866</td></tr><tr><td rowspan=1 colspan=1>Ideal intelligentmode selection</td><td rowspan=1 colspan=1>102.2254</td><td rowspan=1 colspan=1>159.9304</td><td rowspan=1 colspan=1>100.0000</td></tr></table>

Table 5.2.5.1-3. Average, 5-percentile and 95-percentile relative PDSCH throughputs, high mobility   

<table><tr><td rowspan=1 colspan=1>Mode</td><td rowspan=1 colspan=1>RelativeAv.cellthroughput%</td><td rowspan=1 colspan=1>Relative 5-percentilecellthroughput%</td><td rowspan=1 colspan=1>Relative 95-percentilecellthroughput%</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>100.0000</td><td rowspan=1 colspan=1>100.0000</td><td rowspan=1 colspan=1>100.0000</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>99.4713</td><td rowspan=1 colspan=1>241.0834</td><td rowspan=1 colspan=1>70.7448</td></tr><tr><td rowspan=1 colspan=1>Ideal intelligentmode selection</td><td rowspan=1 colspan=1>114.3104</td><td rowspan=1 colspan=1>241.0834</td><td rowspan=1 colspan=1>100.0000</td></tr></table>

The fixed configuration of a GoB and non-GoB SU-MIMO mode (mode-0 or mode-1) provides one example of the potential benefit of a MIMO mode switching algorithm. The actual gain might be impacted by various factors not considered in this simulation as described in Table 5.2.5.1-1.

Although these initial simulation results do not include MU-MIMO scheduling or inter-cell interference, similar findings are expected for these conditions, some related simulated results can be found in [2] . One possibility, to be determined during the normative phase, is for beamforming mode control to be performed for multiple MIMO modes, for example, with one control for SU-MIMO, and one for MU-MIMO.

# 6 MIMO DL Tx Power Optimization, MU-MIMO Pairing and MIMO mode selection

# 6.1 Overview

Massive MIMO holds promise in significantly increasing capacity in practical wireless network environments. Capacity can depend on the wireless network environment (e.g., user velocity, etc.) and the desired quality of the user wireless experience. In many practical cases, the capacity of the cell can be increased by, for example, proper choice of parallel user groups, etc. On the other hand, increased number of parallel users can incur increased inter-user interference which can reduce the user quality. In order to properly balance this trade off operators need fundamental observations (aka, “dials”) to assess the network environment and the user quality for both the uplink and the downlink. Further, to optimize the capacity vs. quality for a given cell for a given time and user distribution, the operator needs fundamental parameters to be changed (aka, “knobs”). The following sections will describe three relevant use-cases and list a number of dials and knobs that we believe constitute a fundamental set for observations and manipulation of massive MIMO systems for both Grid of Beams (GoB) and Reciprocity based implementations.

To further optimize/automate the complex process, it is proposed that O-RAN interfaces be provided (dials and knobs) to enable a AI/ML model training and update, its inference, and finally the beam optimization to enhance the massive MIMO system performance observe and manipulate the massive MIMO system.

# 6.2 MIMO optimization use-cases

The use-cases described in the subsequent sections will show how dials and knobs (specifically referenced) can be used to optimize the three important use cases of downlink transmit power, MIMO pairing enhancement (user separability), and user MIMO mode selection (Mu-MIMO or Su-MIMO). Each use case will address the proposed solution, value proposition, use of specific dials and knobs, and where applicable the potential gains via analytical studies or simulation.

# 6.2.1 Solution 1: Downlink Transmit power optimization

# Problem Statement, Solution and Value Proposition

For general downlink precoding, the downlink transmit power is usually evenly distributed across the UEs. However, depending on the UE separability and path loss deltas, this may result in good cell capacity at the expense of individual UE quality. This can be due to a number of issues such as cell edge UEs having general downlink SINR issues (even without Mu-MIMO), poor UE separability between cell edge UEs, and poor uplink SINR resulting in degraded SRS which are a few example issues. The result of these issues can be manifested by observations of very poor individual UE SINRs (either downlink, uplink, or both) when running in a Mu-MIMO mode. Therefore, although the capacity of the cell has been significantly increased, certain customer experiences may become unacceptable in this Mu-MIMO mode.

The solution to the problem described above is to simply provide observations (“dials”) of UE performance in the form of periodic histograms of UE channel quality as well as the overall cell capacity in order to compute an optimal solution via AI/ML with control (knob) of the downlink minimum required SINR threshold to achieve a minimal UE quality requirement that is set by the operator. The minimum required SINR is a policy and thus doesn’t require real time AI/ML adjustment of transmit power directly but rather leaves this to the scheduler to adjust and optimize consistent with its numerous other priorities and requirements. This adjustment does not impact the normal iBLER (initial BLER) targets, or the CQI/MCS process of adapting the MCS to the UE indicated CQI. Since the received SINR will vary across UEs (see below) and even across PRBs due to frequency selective fading (where narrowband CQI is an option for operators) there is no explicit impact for PRBs. This concept can be extended to the uplink minimum SINR and can improve the uplink more in reciprocity Mu-MIMO modes since the performance in this mode is highly dependent on channel estimation accuracy which is directly influenced by the SRS quality. Performance in the uplink can be improved as shown in reference [3] when the channel quality increase can improve the interference rejection (gains are referenced in the performance section below).

The value of this observability and adjustability allows the operator to optimize the trade-off between cell capacity and individual user/customer quality which is essential to provide the best customer experience. The trade-off, for example, can reduce a very high cell centre data rate (which would likely be unnoticeable for the user) to allow more power to be allocated to the cell edge user (who is noticing low throughput and large latencies) to improve the cell edge data rate situation. The gains to the cell edge occur when specifically, the SINR is so low (e.g., - 10 dB) such that the MCS is low that the spectral efficiency is not sufficient to support the minimum throughput requirements needed by the customer and thus the operator. Based on inputs from the AI/ML system, the scheduler can improve this undesirable situation by reallocation of transmit power to meet minimum SINR requirements for these degraded users. Thus, the scheduler has a recommended policy that it may (or in special cases is not able to satisfy if UE buffer, latency, or other issues preclude) use as guidance for the scheduling of Mu-MIMO users.

In summary, the target of this use case is to improve the downlink post-pairing SINR for MU-MIMO UE to improve cell edge performance and overall cell throughput. The output of this use case is the Minimum Downlink Post-pairing SINR Threshold for MU-MIMO UEs and provided as additional input to the L2 scheduler to support this optimization. The use case does not suggest any specific behaviour. It is left to scheduler implementation how this target is achieved. The relation of this parameter to the 5QI QoS throughput attributes of this UE is ffs.

# Architecture/Deployment Options

The non-RT RIC trains and updates the specific Downlink transmit power control and optimization AI/ML models. Figure 6.2.1.2-1 reflects the functional dependencies of the AI/ML implementation framework. The MU-MIMO DL power control (MPC) rAPP performs optimization required. As shown in Figure 6.2.1.2-1, the rApp uses O1 interface measurement data (via SMO exposed services over R1 interface) for training the ML model. The MPC rApp running in the non-RT RIC uses O1 interface measurement data to optimize minimum downlink SINR threshold for MU-MIMO users at the O-CU or O-DU (as applicable) over O1 interface (via SMO exposed services over R1 interface).

The ML model driving the MPC rApp will utilize UE orthogonality and path loss delta data to understand the scenarios where there can be a set of UEs that have significantly degraded SINR, in addition to monitoring SINR from downlink CQI measurements. The output of the ML model will be a configuration recommendation for the minimum downlink SINR threshold for Mu-MIMO UEs.

![](images/c3d6d33bd17be338ac35d0ede95aa01f74fdfa57f0ffe32d6d2f70c888de76bb.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.2.1.2-1. High level architecture for MIMO power control use-case

![](images/ebf2c4bf692561ca15462256a51054e660d4afdaf1231be4b00a1048e78abcb4.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.2.1.2-2. Call Flow Diagram for MIMO power control use-case

In the call flow in Figure 6.2.1.2-2, the rApp can request the current MIMO configuration (e.g. downlink SINR threshold values) (steps 2-5), as well as current network measurements and KPIs (steps 7-10). The R1 interface is used by the rApp to communicate these requests to SMO, which in turn coordinates the collection via O1 interface. The AI/ML model that is part of the rApp will use the measurements to evaluate the current capacity and UE performance and if required, will generate a recommendation to update the SINR configuration (step 16). This new recommendation is sent to SMO via R1 interface, and finally communicated to the O-DU via O1 interface (step 18).

# Requirements

This section outlines the required measurement data (dials) that form the input of the optimization app and also the output control/configuration (knobs) that are to be fine-tuned to achieve the desired optimization objective.

Table 6.2.1.2-1. UE spatial separability dials   

<table><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source→Target</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>Measurement Period</td><td rowspan=1 colspan=1>Reference</td><td rowspan=1 colspan=1>New        orexistingmeasurement/reportingspecification</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>Paired UE Orthogonality Factor (minUE pair Cross Correlation Coefficient[0,1] for each K number of parallelUEs ) histogram(the cross correlation coefficient isdefined as E{hh*]E{h|^2} where h =channel estimate for a given UE)</td><td rowspan=1 colspan=1>dB(0,-50) forKvalues</td><td rowspan=1 colspan=1>1 .. 15 min.</td><td rowspan=1 colspan=1>[Dial09]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=3 colspan=1>01</td><td rowspan=3 colspan=1>O-DU→Non-RT RIC</td><td rowspan=3 colspan=1>Path Loss Delta distribution across allMu-MIMO UEs (percent vs. &lt; 1 dB, &lt;3 dB, &lt; 5 dB, &lt; 10 dB, &lt; 15 dB, &lt; 20dB, &lt; 30 dB, &gt; 30 dB)(the path loss may be estimated by thedownlink TX power minus the RSRPall normalized to the SCS tonebandwidth or be PHR reporting)</td><td rowspan=1 colspan=1>Percen</td><td rowspan=1 colspan=1>1 .. 15 min.</td><td rowspan=3 colspan=1>[Dial10]</td><td rowspan=3 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>t</td><td rowspan=2 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td></tr></table>

Table 6.2.1.2-2. Downlink MIMO quality dials   

<table><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>Downlink CQI Report histogram (oneCQI histogram (percent use vs. CQIindex) for each number of Mu-MIMOUEs in parallel (e.g., 1,2,3,.K) Seesection O (GoB) for other use cases.</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=2>1  …  15min.</td><td rowspan=1 colspan=1>[Dial18]</td><td rowspan=1 colspan=1>Measurementdefinition in3GPP     TS38.214Newmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>Zero Power reference measurementvalue per beam (average value – dBm)– Intercell Interference Measurements</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=2>1  …  15min.</td><td rowspan=1 colspan=1>[Dial20]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=3 colspan=1>01</td><td rowspan=3 colspan=1>O-DU→Non-RT RIC</td><td rowspan=3 colspan=1>Para. 5.1.6 (ref.[5]) CSI signal-to-noiseand interference ratio(CSI-SINR)histogram</td><td rowspan=3 colspan=1>Percent</td><td rowspan=2 colspan=2>1      15min.</td><td rowspan=1 colspan=1>[Dial21]</td><td rowspan=3 colspan=1>Measurementdefinition in3GPP    TS38.215Newmeasurementreporting</td></tr><tr><td rowspan=2 colspan=2>min.</td><td rowspan=2 colspan=1></td></tr><tr></tr></table>

Table 6.2.1.2-3. Downlink MIMO power control knobs   

<table><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source→Target</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>UnitS</td><td rowspan=1 colspan=1>ControlPeriod</td><td rowspan=1 colspan=1>Reference</td><td rowspan=1 colspan=1>New       orexistingconfig</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>Non-RTRIC→O-DU</td><td rowspan=1 colspan=1>Minimum  Downlinkpost-pairing SINR Threshold for MU-MIMO UEs(Operator set [0,,25])</td><td rowspan=1 colspan=1>Integer(dB)</td><td rowspan=1 colspan=1>1 .. 15 min.</td><td rowspan=1 colspan=1>[Knob02]</td><td rowspan=1 colspan=1>New</td></tr></table>

Note: It is FFS whether any of the listed measurements have any dependency on O-RU and if any information needs to be exchanged over O-RAN FH m-plane interface from O-RU to O-DU.

# O-RAN Entity roles:

1) SMO & Non-RT RIC a) Collect existing configuration and performance data from RAN b) Trigger AI/ML Model training/update and deployment as necessary c) Apply power control recommendations from rApp via R1 and O1 interface using config management service.   
2) O-CU a) Report current configuration and performance data to non-RT RIC rApp via O1 interface if requested by rApp.   
3) O-DU a) Report current configuration and performance data to non-RT RIC rApp via O1 interface. b) Apply power control related knobs based on rAPP recommendation.

# Impact Analysis on O-RAN WGs

Editor’s note: This is an initial impact analysis as part of the WG1 UCTG work on mMIMO. The intention is to estimate the expected standardization effort within the O-RAN working groups. It is up to the WGs to decide how the mMIMO functionality should be specified in specifications of each WG, and whether it will be part of existing or new set of specifications.

WG1 (use cases, architecture) Impact

Update WG1 use case analysis report and use-case detailed specification with downlink power control use case.   
No impact to existing architecture.

# WG2 (Non-RT RIC, A1, R1) Impact

Assess impact to A1 and R1 interfaces and non-RT RIC architecture, including AI/ML training and deployment.   
Add new use cases and corresponding requirements and specifications in case impact to A1 or R1 interfaces.

WG5 (O-CU and O-DU) Impact

Assess impact on O-CU and O-DU support for dials and knobs described in the use-case.

# WG10 (SMO, O1) Impact

Assess impact with PM coordination group and IM/DM coordination group on support of proposed dials (measurements) and knobs (configuration IM/DM) and incorporation in existing O1 interface models, as well as any required coordination with 3GPP

Summary: A detailed analysis of the specification impact is to be completed. There is large specification impact to specify new proposed measurement definitions and measurement reporting in 3GPP or in O-RAN. The impact of the required measurements and configurations will be reduced if they are already part of ongoing/upcoming O-RAN specifications (ffs) or are being considered for specification in other bodies such as 3GPP (ffs).

# Complexity/Gains

The simulation of 8 UEs in an urban setting (without intercell interference just to keep it simple) is shown in Figure 6.2.1.4-1 as a first step in simulation as next steps cell clusters are planned to be simulated as well to confirm intercell interference performance. It was based on uniform downlink TX power distribution and a generic zero forcing precoding algorithm (Green dots). Clearly the resulting downlink SINR is fairly uniform for most of the UEs except for UE#6 and UE#8 which tend toward the cell edge. The poor SINR of these two UEs can be mitigated by either monitoring the separability and potentially deleting them from the pairing with the other 6 UEs or by reallocating some of the power to the other UEs. In the cases where there may be excessive SINR for a near-center of the cell UE (not in this simulated case) the downlink TX power can be reallocated to benefit the cell edge UEs to bring them up to a minimum SINR for example. Specifically, general statistical trends of poor cell edge SINR will be detected by the measurements (dials) and optimized by the AI/ML to result in an appropriate minimum SINR threshold.

• Bandwidth = 20 MHz   
• 8x8 Antenna Array   
• 2 GHz frequency • Urban High Rise Base station height $= 2 0$ meters UE height $=$ all at ground level

![](images/b0b7d4db74de641cc1e0c3c53d5e3c751e79753a01c718d51291f273e55a8b76.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.2.1.4-1. SINR distribution for UEs from simulation

Thus, the gain is highly dependent on the distribution of the SINR per UE but clearly TX power can be reallocated to improve poorly performing UEs. However, the objective in this case is not to increase the capacity but to insure good overall customer experience.

The complexity of having histograms requires generally low complexity since it reduces the data rates across the O-RAN interfaces and keeps the high rate processing in the real-time capable processing hardware either in the DU or the RU with FPGA and CPU/GPU capabilities.

Other downlink (and uplink) power/SINR optimization is described in references Bjornson [3] and Marzetta [4] that either adjust downlink power directly or optimize SINR targets specifically for cell edge users and show good performances for minimum user throughputs (directly proportional to minimum SINR) of up to $1 0 0 \%$ for the downlink and $5 0 \%$ for the uplink [4].

# Summary

In summary, a difference in SINR as received by paired MU-MIMO UEs has been shown for a system without inter-cell interference. Further simulations at system level are under consideration. The gain of this use case in terms of cell edge and overall cell performance will depend on the actual L2 scheduler implementation and the consideration of this information by the L2 scheduler. A complexity analysis was not part of the pre-normative phase.

# 6.2.2 Solution 2: MU-MIMO Pairing Enhancement (User Separability or Pairing Control)

Problem Statement, Solution, and Value Proposition

Existing channel orthogonality between multiple users is a key criterion to create user separability and allow for the opportunity to share radio frequency resources simultaneously. Without so, residual interference will be too high to maintain adequate post pairing radio link signal quality levels required to sustain MU-MIMO mode assignments. With mobility there is an added demand to adjust beamforming weight assignments to not only maintain signal power levels at the user end (beam quality), but also to continuously limit the inter user interference experienced between users assigned with the same radio resource allocations. In the absence of creative solutions that capably and in a timely manner respond to the above-described challenges, the 5G massive MIMO deployment will fail to utilize the full capability of large antenna arrays powered by transceivers designed to transmit data channel signals towards a spatially confined direction. Schedulers will also fail to realize potential multiplexing gains as fewer radio resource blocks are shared between users within the same cell, reducing spectral efficiency.

Important too is the need to efficiently identify users with low demand for radio resources - sources of bursty traffic. An intelligent assessment of how best such users can be effectively paired, if at all, with other users needs to be predetermined by the radio intelligent controller. Channel estimation mechanisms that can be extrapolated in time and do not risk becoming stale so they can be utilized effectively to generate accurate weights and applied rapidly, is critical. For lower volume buffer data, an unacceptable gap in the above can create failure in MU-MIMO pairing. In summary, this use case suggests various measurement objects (aka dials) that are recommended as input into the AI/ML analytics Apps to optimally determine the outputs (aka knobs) required to optimize the MU-MIMO feature operation. The following section presents the input and output parameter and possible use in an AI/ML analytics App.

Scheduled UEs

1. Histogram of UEs with data in Buffer [Dial01]

a. If greater than “Threshold_High,” evaluate cell’s MU-MIMO pairing history and set status of cell as AI/ML optimization candidate.

2. # Of scheduled MU-MIMO UEs per TTI [Dial04] a. AI/ML shall aspire to improve or maintain pairing success rate b. Correlate to histogram of UEs with data in buffer

Include percent of UE pairs evaluated for orthogonality by the scheduler [Dial05]

4. AI/ML shall aspire to keep difference between 3. and $^ { 6 6 } \#$ Of scheduled MU-MIMO UEs per TTI” at a minimum by minimizing residual interference of paired UEs.

5. iBLER for MU-MIMO UEs [Dial06] a. AI/ML shall aspire to improve pre pair value vs post pair b. Delta iBLER should not exceed A dB, for a given pair size, for example.

6. TTI of Evaluation vs. TTI of Scheduled Pairing or the Offset [Dial08] a. For lower volume buffer data, an unacceptable gap in the above can create failure in MU-MIMO pairing

# UE Spatial Separability

1. Paired UE Orthogonality Factor [Dial09]

a. This is a measure of MU-MIMO performance sustainability. Spectral Efficiency will increase. It is an implicit reflection of residual interference among paired UEs.

2. Path Loss Delta [Dial10]

a. If orthogonality factor is high, and pathloss delta is high, AI/ML should be used due to an inherent decorrelation of channel between the served UEs, for a given spatial distribution.

Coherence Block

1. Coherence Time [Dial11] a. AI/ML is used to evaluate channel estimation reliability, to fit beamforming and MU-MIMO pairing process cycle into the coherence time.   
2. Coherence Bandwidth [Dial12] a. To maximize PRB/TTI assignment to MU-MIMO vs. SU-MIMO.

# Downlink MIMO Quality

1. Downlink CQI Report Histogram [Dial18] a. To safely scale the MU-MIMO pairing size – CQI is expected to fall with increase in pairing size. According to the CQI and number of candidates that exist, AI/ML shall intelligently optimize pairing.

2. ZP Reference Measurement Value per Beam [Dial20]

a. ZP CSI-RS is to be used for interference measurement (Indication of likely residual interference)

# Uplink MIMO Quality

1. Minimum, Average and Maximum Uplink SINR or Co-UE interference, Noise and External Interference level per UE to allow assessments of Uplink channel pairing decisions similar to the downlink [Dial22]   
2. Percent Time MU-MIMO UEs are at Maximum TX Power and $< 5$ PRB allows assessments of UL coverage [Dial24]

Frequency Reuse Factor for Pilots

1. Histogram of re-used Pilots (SRS) from neighbor cells [Dial25] a. Non-Real /Real Time RIC will work to assign different SRS to in-cell UEs to improve channel estimation performance

Uplink Covariance

1. Post Pilot Removal Uplink Covariance [Dial26]

a. Measure of channel orthogonality between MU-MIMO UEs and selection optimization, through channel estimation

Pilot and Coherence Block Joint Distribution [Dial27]

1. Histogram of Selected Pilot Sequence Length and Histogram of Selected Coherence Block a. AI/ML will impart intelligence into the robustness of the pilot signals used for channel estimation

Spectral Efficiency

1. MU-MIMO PRB Utilization Histogram [Dial30]

a. AI/ML will monitor to evaluate data Bytes transmitted, correlated to MU-MIMO pairing levels. This will be compared to BLER reports for pairing decisions.

2. Total PRB $\%$ Used Supporting MU-MIMO histogram [Dial31]

3. MU-MIMO PDCP Volume Histogram [Dial32] a. Required for spectral efficiency calculation

4. MU-MIMO Throughput DRB vs. MU-MIMO Layers [Dial33] a. Required to evaluate MU-MIMO pairing effectiveness and scalability

5. MU-MIMO Spectral Efficiency [Dial34] a. Required to evaluate MU-MIMO pairing effectiveness

With the above inputs, the AI/ML app will calculate the outputs to control the optimization of the Massive MIMO system below.

Uplink UE Transmit Power Control

1. Minimum Uplink SINR Threshold for MU-MIMO UEs [Knob01] a. Useful to ensure SRS reciprocity-based beamforming approach is effective

Downlink Transmit Power Allocation

1. Minimum Downlink SINR Threshold for MU-MIMO UEs [Knob02] a. This can be a variable based on traffic loading within a cell. A lower threshold can be tolerated, but greater than a cut-off threshold that is already existing as an implicit indicator (pre pairing evaluation) prior to pairing. It can also be a variable based upon the pairing size (Number of UEs in MU-MIMO mode, within same paired group)

# Parallel Scheduling Control

1. Uplink SINR Threshold [Knob03]   
2. Downlink SINR Threshold [Knob04]   
3. Minimum in-buffer PDU Count [Knob05] a. To minimize beamforming and MU-MIMO process overhead and scheduling delays   
4. Minimum projected TTIs required for scheduling [Knob06] a. To minimize beamforming and MU-MIMO process overhead and scheduling delays   
5. Threshold for pairing candidates’ SRS strength [Knob07] a. To make MU-MIMO beamforming more effective, especially for Zero Forcing technique.   
6. Maximum Number of Paired Candidates [Knob09 or Knob08]] a. A means to limit Pairing size based on evaluation metrics and performance of larger pairing sizes   
7. UE Pairing Selection Threshold Based on 5QI Threshold for Pairing [Knob10] a. Prioritizing pairing during congestion, based on 5QI QOS characteristics

SRS Sequence and Distribution

1. SRS Length [Knob10]   
2. SRS Sequence Partition [Knob11]

Both are required to optimize performance based upon channel estimation outcome, reflected in the orthogonality between paired users or their residual interference levels.

Quiescent Antenna Weight Application

1. Customizable set of Antenna Weights [Knob15] a. Optimization of array structure to improve spatial resolution of beams to support a wide distribution of MU-MIMO users.

Realizing that significant increases in network capacity generally require large capital outlays to increase the available spectrum and to purchase new equipment, the promise of Massive MIMO to increase the capacity and essentially the available spectrum usage efficiency by adopting approaches relying upon advanced antenna arrays, is strongly considered. However, such approaches at the same time add additional interference among the users that are simultaneously using the same spectrum. In fact, in general, more simultaneous users add more interference to each individual user and thus a careful balance between capacity and quality must be maintained or unhappy users can ‘churn’ to competitors.

The AI/ML assisted modeling and training output, along with the non-RT RIC based enhancement/inference, will strive to deliver end goal solution selections and system configuration options that upon adoption within the respective domains where they reside, realize an optimization framework that maximizes the potential of a MU-MIMO feature. Capacity augmentation will be realized by successfully assigning MU-MIMO layers to a greater number of users simultaneously, more often, and more uniformly across the serving area of each gNB. Dials that capture measurement values as appropriately defined in this document, and knobs which are configured to manage the operations of critical techniques that define the MU-MIMO feature and its underlying algorithms meant to enhance pairing capabilities, will provide the platforms for a successful implementation that realizes the following goals:

1) Increased spectral efficiency through the support of higher total throughput, by a factor more closely proportional to the number of layers supported by the DU   
2) Robust MU-MIMO layers with per link MCS that is closely reflective of power loss at transmitter, proportional to number of layers   
3) More resource blocks assigned to MU-MIMO mode

Particularly, AI/ML is used to optimize the network capacity utilizing a channel reciprocity-based approach vs. maintenance of the quality of the connection for each user with shared resources. Additionally presented is the approach that involves using a GoB-based solution, similar in objective to the reciprocity one, whereby balance between user quality and capacity realized, is aimed.

The dials needed to assess user quality generally consist of measuring the quality (SINR, CQI, etc.) of both the Uplink and Downlink for each user. Other metrics include the Uplink power margin for the user and the user mobility among many other factors (see following sections for a comprehensive list of many of them). Other metrics that provide assessments of capacity include the normal cell volume and cell throughputs along with congestion (active connected users with data in the buffer). For Massive MIMO the individual “user separability” impacts the MU-MIMO pairing performance (and thus capacity) such that the users cannot be arbitrarily paired or else low user spatial separability can mutually degrade the user link quality due to significant inter-user interference. Thus, user separability must be tracked and used to train the AI/ML component in to optimize the capacity while constrained to insure minimum levels of user quality. The AI/ML component, after training, will output “knobs” to appropriately adjust the capacity to attempt to meet the user volume, throughput, and latency demands. Examples of the knobs for reciprocity are the allocations of Downlink Transmit Power allocation among users (see Section 6.2.1 above), the assignment of levels of pairing or parallelism, assignment of modes of Su-MIMO vs. Mu-MIMO (see Section 6.2.3 below for more details), etc.

An alternative approach to the Reciprocity (mainly for TDD systems) based solution is the GoB approach, which relies upon using the downlink CSI-RS reference signal to estimate the downlink channel (CSI). Here, a quantized model of the CSI is fed back to the base station in order to make proper precoding decisions for the set of MU-MIMO users. This approach can make use of shadow fading CSI information (type I) that is estimated or even the combination of shadow and fast fading (type II) CSI information that is fed back with, of course, a larger required number of bits.

The dials section enumerates a list of the user feedback CSI information that should be monitored to assess the state of the channel and the quality of the channel (CQI, SINR, etc.). In addition, the link quality can also be associated with the choice of multiple downlink beams that are received by the user and these need to be properly monitored as well. In addition, various “sub-beam” modalities must be monitored that give more information about the beam characteristics (e.g., beam phase, etc.). In this case, the user beams (vs. the user channels for reciprocity) need to be assessed for “user separability” as well.

There are several methods that can be applied, after training in the ML/AI component, that can be used to ensure user quality while maximizing capacity. A “knobs” implementation that controls the beam shapes and power allocation (while assessing the user pairing degree) can be used to ensure user quality.

# Architecture/Deployment Options

The non-RT RIC trains and updates the specific MU-MIMO pairing enhancement AI/ML models. Figure 6.2.2.2-1 reflects the functional dependencies of the AI/ML implementation framework. The MU-MIMO Pairing Enhancement (MPE) rAPP performs optimization required to realize multiplexing gains through the sharing of PHY layer resource blocks between several end users who are in transmission while on the PDSCH. As shown Figure 6.2.2.2-1, the rApp uses O1 and $\mathrm { F H } \mathrm { m }$ -plane measurement data (via SMO exposed services). The MU-MIMO Pairing Enhancement rApp running in the non-RT RIC uses ${ \mathrm { O } } 1 / { \mathrm { F H } } { \cdot } { \mathrm { m } }$ data to optimize cell MU-MIMO layer realization by configuring O-RU over $\mathrm { F H } \mathrm { m }$ -plane or O-DU over O1 interface parameters (via SMO exposed services over R1 interface).

![](images/47257f89a1c053e2d131ffdd5322a4f8f5ce90cc87ce5c3c7a82a51a03de721c.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.2.2.2-1. O-RAN Architecture Diagram for MIMO pairing use-case

![](images/3fe0872f1a9a030f0428635d81a456dfe4dc96f27966e8bd7001b53c9d9cffee.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.2.2.2-2. Call Flow Diagram for MIMO pairing use-case

In the call in Figure 6.2.2.2-2, the rApp can request the current MIMO configuration listed in Table 6.2.2.2-12 (steps 2- 5), as well as current network measurements and KPIs listed in Table 6.2.2.2-1 to Table 6.2.2.2-11 (steps 7-10). The R1 interface is used by the rApp to communicate these requests to SMO, which in turn coordinates the collection via O1 interface. The AI/ML model that is part of the rApp will use the measurements to evaluate the current capacity and UE performance and if required, will generate a recommendation to update one or more of the identified configuration knobs (step 16). This new recommendation is sent to SMO via R1 interface, and finally communicated to the O-DU via O1 interface (step 18).

# Requirements

In order to achieve the value proposition described above, the key Massive MIMO KPIs or dials need to be monitored to assess the state of the system. A proposed set is discussed in the following sections.

All the dials/measurements listed here are required at a configurable granularity in multiples of 1 minute, ranging from 1 to 15 minutes.

Table 6.2.2.2-1. Scheduled UE dials   

<table><tr><td rowspan=1 colspan=1>Interface</td><td rowspan=1 colspan=1>Source→Target</td><td rowspan=1 colspan=1>Description</td><td rowspan=1 colspan=1>Units</td><td rowspan=1 colspan=1>Measurement Period</td><td rowspan=1 colspan=1>Reference</td><td rowspan=1 colspan=1>New     orexistingmeasurement/reportingspecification</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>Histogram of UEs with data in thebuffer.     If    greater    than&quot;Threshold_High,&quot;evaluate cell&#x27;sMU-MIMO pairing history and setstatus of cell as AI/ML optimizationcandidate.</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1 ..15 min.</td><td rowspan=1 colspan=1>[Dial01]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>Angle of Arrival or Beam IDhistogram. Only for GoB Feedback.</td><td rowspan=1 colspan=1>integer</td><td rowspan=1 colspan=1>1 .. 15 min.</td><td rowspan=1 colspan=1>[Dial03]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1># of scheduled MU-MIMO UEs perTTI (histogram of % UE=1, % UE=2,% UE = max limit (K))</td><td rowspan=1 colspan=1>percent</td><td rowspan=1 colspan=1>1 ..15 min.</td><td rowspan=1 colspan=1>[Dial04]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>Percent of UE pairs evaluated fororthogonalityby the scheduler(histogram, %=0, %=1, %=2, ….%=P)</td><td rowspan=1 colspan=1>percent</td><td rowspan=1 colspan=1>1 .. 15 min.</td><td rowspan=1 colspan=1>[Dial05]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>iBLER (initial Block Error Rate,BLER) for the MU-MIMO UEs</td><td rowspan=1 colspan=1>percent</td><td rowspan=1 colspan=1>1 .. 15 min.</td><td rowspan=1 colspan=1>[Dial06]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>UEs scheduled for Mu-MIMO pairing(histogram,%UE=0, %UE=1,…percent UE = K)</td><td rowspan=1 colspan=1>percent</td><td rowspan=1 colspan=1>1 .. 15 min.</td><td rowspan=1 colspan=1>[Dial07]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>TTI ofEvaluationVS.TTI ofScheduledpairing or the offset(histogram %TTI=1,%TTI=2.%TTI = 100)</td><td rowspan=1 colspan=1>Count</td><td rowspan=1 colspan=1>1 ..15 min.</td><td rowspan=1 colspan=1>[Dial08]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr></table>

Table 6.2.2.2-2. UE spatial separability dials   

<table><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>Paired UE Orthogonality Factor (minUE pair Cross Correlation Coefficient[0,1] for each K number of parallelUEs ) histogram</td><td rowspan=1 colspan=1>dB(0,…-50)forKvalues</td><td rowspan=1 colspan=1>1 .. 15 min.</td><td rowspan=1 colspan=1>[Dial09]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>Path Loss Delta distribution across allMu-MIMO UEs (percent vs. &lt; 1 dB, &lt;3 dB, &lt; 5 dB, &lt; 10 dB, &lt; 15 dB, &lt; 20dB, &lt; 30 dB, &gt; 30 dB)</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1 ..15 min.</td><td rowspan=1 colspan=1>[Dial10]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr></table>

Table 6.2.2.2-3. Coherence block dials   

<table><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>Coherence Time averaged over allpaired UEs(histogram of percenttimes; &lt; 1ms, &lt; 10 ms, &lt; 50 ms, &lt; 100ms, &lt;500 ms)</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1 .. 15 min.</td><td rowspan=1 colspan=1>[Dial11]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>Coherence Bandwidth averaged overall paired UEs (histogram of percent ofBWs &lt; 200 kHz, &lt; 1 MHz, &lt; 5 MHz,&lt; 10 MHz, &lt; 50 MHz, &lt; 100 MHz</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1 .. 15 min.</td><td rowspan=1 colspan=1>[Dial12]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>Average of paired UE Coherence Block= CoherenceTime    CoherenceBandwidth (histogram percent &lt; 100, &lt;500，&lt;1000，&lt;5000，&lt;10,000，&gt;10,000)</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1 .. 15 min.</td><td rowspan=1 colspan=1>[Dial13]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>Histogram of SRS periods commanded(percent &lt;2.5 ms, &lt;5 ms, &lt;10 ms, &lt;20ms, &lt;40 ms, &lt;100 ms, &lt; 200 ms, &lt; 400ms)</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1 ..15 min.</td><td rowspan=1 colspan=1>[Dial14]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr></table>

Table 6.2.2.2-4. Downlink MIMO quality dials   

<table><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>Downlink CQI Report histogram (oneCQI histogram (percent use vs. CQIindex) for each number of Mu-MIMOUEs in parallel (e.g., 1,2,3,.K). Seesection 0 (GoB) for other use cases.</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1 ..15 min.</td><td rowspan=1 colspan=1>[Dial18]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>ZP reference measurement value perbeam (average value − dBm)</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>1 .15 min.</td><td rowspan=1 colspan=1>[Dial20]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>Para. 5.1.6 (ref.[5]) CSI signal-to-noiseandiinterference ratio  (CSI-SINR)histogram</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1..15 min.</td><td rowspan=1 colspan=1>[Dial21]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr></table>

Table 6.2.2.2-5. Uplink MIMO quality dials   

<table><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU↓Non-RTRIC</td><td rowspan=1 colspan=1>Minimum, Average(linear), andMaximum Uplink SINR or Co-UEinterference, Noise and ExternalInterference Level per UE (Mu-MIMOpair histogram (SINR range: -10 dB to+ 30 dB) for 1,2, 3, ., K UEs)</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1  … 15min.</td><td rowspan=1 colspan=1>[Dial22]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>Percent time Mu-MIMO UEs are atmaximum TX power and &lt; 5 PRB</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1：15min.</td><td rowspan=1 colspan=1>[Dial24]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr></table>

Table 6.2.2.2-6. Frequency Reuse factor for Pilots dials   

<table><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>Histogram of re-used pilots (CSI-RSand SRS) from neighbor cells (reusedpilots = 0, 1, 2, .,M)</td><td rowspan=1 colspan=1>percent</td><td rowspan=1 colspan=1>1 ..15 min.</td><td rowspan=1 colspan=1>[Dial25]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr></table>

Table 6.2.2.2-7. Uplink covariance dials   

<table><tr><td>01</td><td>O-DU Post → Non- RT RIC</td><td>Pilot Removal Uplink Covariance (10 sec. average) per Mu- d MIMO UE vs. Pairing size 1.K (Section 3.3 for other use cases)</td><td>Fixe 1 .. 15 min. point</td><td>[Dial26]</td><td>New measurement definition New measurement reporting</td></tr></table>

Table 6.2.2.2-8. Pilot and Coherence Block Joint Distribution dials   

<table><tr><td>01</td><td>O-DU → Non- RT RIC</td><td>Histogram of Selected Pilot Sequence length (&lt;12, &lt;24, &lt;48,&lt;96, &lt;192, &lt;384, etc.) and histogram of Selected Coherence Block (&lt; 100, &lt; 500, &lt; 1000, &lt;5000, &lt;10,000, &lt;100,000, &gt; 100,000 symbols) joint histogram</td><td>perce nt</td><td>1 ..15 min.</td><td>[Dial27]</td><td>New measurement definition New measurement reporting</td></tr></table>

Table 6.2.2.2-9. Spectral Efficiency dials   

<table><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>MU-MIMO   PRB   UtilizationHistogram</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1     15min.</td><td rowspan=1 colspan=1>[Dial30]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>Total PRB % Used Supporting MU-MIMO histogram</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1 … 15min.</td><td rowspan=1 colspan=1>[Dial31]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>MU-MIMO    PDCP    Volumehistogram</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1      15min.</td><td rowspan=1 colspan=1>[Dial32]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>MU-MIMODRB(DL andUL)Throughput Histograms (min., ave.,and max.) (100 kbps, 200, kbps, etc.10 Gbps) vs. MU-MIMO layers(1,2,.., )</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1     15min.</td><td rowspan=1 colspan=1>[Dial33]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>MU-MIMO Spectral Efficiency(8*PDCP      Volume/(BW*PRButilization)， bits/sec./Hz histogramover measurement period,whereBW = bandwidth, Hz). Note: Allparallel/paired PRBs count as oneover a TTI</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1…1 5min.</td><td rowspan=1 colspan=1>[Dial34]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr></table>

Table 6.2.2.2-10. Beam Management Monitor dials   

<table><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>SSB Wide-beam (by Beam index)selected duringdata transmission(histogram of percent usage vs. beam index (e.g., 0-7 for 3-6 GHz))</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1 … 15min.</td><td rowspan=1 colspan=1>[Dial39]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>CRI-RSRP per Port (RSRP histogramfrom -130 to -70 dBm histogram in 2dB steps</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1  … 15min.0.5 - 1 secfor Near-RT</td><td rowspan=1 colspan=1>[Dial40]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>PMI index histogram for Type IIfeedback (percent usage per PMIindex)</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1  … 15min.</td><td rowspan=1 colspan=1>[Dial41]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>Type 2 Port Selection Codebook 2ndstage PMI reporting_ WidebandAmplitude co-efficient histogram usedmost (1, ½2, %4, 1/8, 1/16, 1/32, 1/64, 0)per beam</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1  …  15min.0.5 - 1 secfor Near-RT</td><td rowspan=1 colspan=1>[Dial42]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>Type 2 Port Selection Codebook 2ndstage PMI reporting-WidebandAmplitude co-efficient histogram usedleast (1, ½2, ½4, 1/8, 1/16, 1/32, 1/64, 0)per beam</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1  … 15min.0.5 - 1 secfor Near-RT</td><td rowspan=1 colspan=1>[Dial43]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>Type 2 Port Selection Codebook 2ndstage PMI reporting – Sub-band co-phasing &quot;phase shifts&#x27;&quot; maximum shiftper beam histogram</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1…15min.0.5 - 1 secfor Near-RT</td><td rowspan=1 colspan=1>[Dial44]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>Type 2 Port Selection Codebook 2ndstage PMI reporting – Sub-band co-phasing &quot;phase shifts&quot; minimum shiftper beam histogram</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1  … 15min.0.5 - 1 secfor Near-RT</td><td rowspan=1 colspan=1>[Dial45]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>Type 2 Port Selection Codebook 2ndstage PMI reporting – Sub-band co-phasing &quot;phase shifts&quot; most usedquantized value per beam histogram</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1 … 15min.0.5 - 1 secfor Near-RT</td><td rowspan=1 colspan=1>[Dial46]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr></table>

Table 6.2.2.2-11. TDD Channel Estimation dials   

<table><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RT RIC</td><td rowspan=1 colspan=1>Maximum Eigenvalue distribution ofthe uplink covariance matrix</td><td rowspan=1 colspan=1>Number</td><td rowspan=1 colspan=1>1 ..15 min.</td><td rowspan=1 colspan=1>[Dial47]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr></table>

Table 6.2.2.2-12. Links and layers dials   

<table><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>Total number of MU-MIMO pairedusers, counting by PRBs where pairinghappened, across all TTIs duringcollection interval</td><td rowspan=1 colspan=1>Number</td><td rowspan=1 colspan=1>1  … 15min.</td><td rowspan=1 colspan=1>[Dial48]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>Total number of PRBs supportingMU-MIMO mode, across all TTIsduring collection interval</td><td rowspan=1 colspan=1>Number</td><td rowspan=1 colspan=1>1  … 15min.</td><td rowspan=1 colspan=1>[Dial49]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>Avg. number of MU-MIMO layersassigned per TTI per PRB (PRBs withpairing)</td><td rowspan=1 colspan=1>Number</td><td rowspan=1 colspan=1>1  … 15min.</td><td rowspan=1 colspan=1>[Dial50]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>Histogram of Number of UEs in MU-MIMO mode (2,3,4..N) vs Avg.Number of1MU-MIMO layerssupported. Information derived perPRB where multiplexing is occurring,per TTI, over collection interval</td><td rowspan=1 colspan=1>Number</td><td rowspan=1 colspan=1>1      15min.</td><td rowspan=1 colspan=1>[Dial51]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>Histogram of DL MCS for MU- MIMO usage (percentage for MCS =1, 2, …., max.)</td><td rowspan=1 colspan=1>%</td><td rowspan=1 colspan=1>1. 15min.</td><td rowspan=1 colspan=1>[Dial52]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr></table>

Similar to the measurement and monitoring objective of the “dials” section, the control of key parameters is the objective of the “knobs” section. This allows the value proposition of allowing each operator to satisfy their respective unique optimality criteria via emerging AI/ML technologies.

<table><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>Non-RTRIC →O-DU</td><td rowspan=1 colspan=1>Uplink SINR threshold (for MU-MIMO eligibility)</td><td rowspan=1 colspan=1>Integer (dB)</td><td rowspan=1 colspan=1>15min.</td><td rowspan=1 colspan=1>[Knob03]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>Non-RTRIC →O-DU</td><td rowspan=1 colspan=1>Downlink SINR threshold (for MU-MIMO eligibility)</td><td rowspan=1 colspan=1>Integer (dB)</td><td rowspan=1 colspan=1>1 …15min.</td><td rowspan=1 colspan=1>[Knob04]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>Non-RTRIC →O-DU</td><td rowspan=1 colspan=1>Minimum in-buffer PDU count (ortraffic volume in Bytes) (buffer vol.selection requirement for scheduling,units = kbytes, FA = minute)</td><td rowspan=1 colspan=1>Integer(kbytes)</td><td rowspan=1 colspan=1>1…15min.</td><td rowspan=1 colspan=1>[Knob05]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>Non-RTRIC →O-DU</td><td rowspan=1 colspan=1>Minimum projected TTIs requiredfor scheduling (equivalent bufferTTIs required for scheduling, units =# TTI, FA = minute)</td><td rowspan=1 colspan=1>Integer,TTI</td><td rowspan=1 colspan=1>1 min.</td><td rowspan=1 colspan=1>[Knob06]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>Non-RTRIC →O-DU</td><td rowspan=1 colspan=1>Threshold for pairing candidates&#x27;SRS strength (units = dB relative tostandard, standard is settable in dBm)</td><td rowspan=1 colspan=1>Integer,dBm</td><td rowspan=1 colspan=1>1 … 15min.</td><td rowspan=1 colspan=1>[Knob07]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>Non-RTRIC →O-DU</td><td rowspan=1 colspan=1>Average number of paired candidates(units = 1,2,.,.)</td><td rowspan=1 colspan=1>Integer</td><td rowspan=1 colspan=1>1 …15min.</td><td rowspan=1 colspan=1>[Knob08]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>Non-RTRIC →O-DU</td><td rowspan=1 colspan=1>Maximum  numberofpairedcandidates (units = 1,2,,.)</td><td rowspan=1 colspan=1>Integer</td><td rowspan=1 colspan=1>1 …15min.</td><td rowspan=1 colspan=1>[Knob09]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>Non-RTRIC →O-DU</td><td rowspan=1 colspan=1>UE pairing selection threshold basedon 5QI threshold for pairing (units =1..)</td><td rowspan=1 colspan=1>integer</td><td rowspan=1 colspan=1>1 … 15min.</td><td rowspan=1 colspan=1>[Knob10]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>Non-RTRIC →O-DU</td><td rowspan=1 colspan=1>Quiescent    Antenna    WeightApplication</td><td rowspan=1 colspan=1>Vector</td><td rowspan=1 colspan=1>1  … 15min</td><td rowspan=1 colspan=1>[Knob21]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>Non-RT</td><td rowspan=1 colspan=1>Settable Number of SSB Beams /CSI-RS Resources</td><td rowspan=1 colspan=1>Integer</td><td rowspan=1 colspan=1>1 …15min</td><td rowspan=1 colspan=1>[Knob22]</td><td rowspan=1 colspan=1>Newmeasurementdefinition</td></tr></table>

Table 6.2.2.2-13. Output knobs (control) from MIMO pairing use-case   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>RIC →O-DU</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Newmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>Non-RTRIC →O-DU</td><td rowspan=1 colspan=1>Number of Refined/Narrow Beamsper SSB</td><td rowspan=1 colspan=1>Integer</td><td rowspan=1 colspan=1>11. 1 5min</td><td rowspan=1 colspan=1>[Knob23]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>Non-RTRIC →O-DU</td><td rowspan=1 colspan=1>Settable Reference CSI-RS VS Neighbor CSI-RS mapping for SSBsymbols</td><td rowspan=1 colspan=1>ListSet</td><td rowspan=1 colspan=1>1… 1 5min</td><td rowspan=1 colspan=1>[Knob24]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>Non-RTRIC →O-DU</td><td rowspan=1 colspan=1>CSI-RS Density</td><td rowspan=1 colspan=1>Value</td><td rowspan=1 colspan=1>1. 15min</td><td rowspan=1 colspan=1>[Knob25]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>Non-RTRIC →O-DU</td><td rowspan=1 colspan=1>Minimum     Downlink    SINRThreshold for MU-MIMO UEs</td><td rowspan=1 colspan=1>Value</td><td rowspan=1 colspan=1>1     15min</td><td rowspan=1 colspan=1>[Knob26]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>Non-RTRIC →O-DU</td><td rowspan=1 colspan=1>SRS Length</td><td rowspan=1 colspan=1>Number</td><td rowspan=1 colspan=1>1：15min</td><td rowspan=1 colspan=1>[Knob27]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>Non-RTRIC →O-DU</td><td rowspan=1 colspan=1>SRS Sequence Partition</td><td rowspan=1 colspan=1>GroupID</td><td rowspan=1 colspan=1>1…15min</td><td rowspan=1 colspan=1>[Knob28]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr></table>

Note: It is FFS whether any of the listed measurements have any dependency on O-RU and if any information needs to be exchanged over O-RAN FH m-plane interface from O-RU to O-DU.

# O-RAN Entity roles:

1) SMO & Non-RT RIC a) Collect existing configuration and performance data from RAN b) Trigger AI/ML Model training/update and deployment as necessary c) Apply MIMO pairing control recommendations from rApp via R1 and O1 interface using config management service.   
2) O-CU nodes a) Report current configuration and performance data to non-RT RIC rApp via O1 interface if requested.   
3) O-DU nodes a) Report current configuration and performance data to non-RT RIC rApp via O1 interface.   
b) Apply MIMO pairing control related knobs based on rAPP recommendation.

# Impact Analysis on O-RAN WGs

Editor’s note: This is an initial impact analysis as part of the WG1 UCTG work on mMIMO. The intention is to estimate the expected standardization effort within the O-RAN working groups. It is up to the WGs to decide how the mMIMO functionality should be specified in specifications of each WG, and whether it will be part of existing or new set of specifications.

WG1 (use cases, architecture) Impact

Update WG1 use case analysis report and use-case detailed specification with MU-MIMO pairing control use case. No impact to existing architecture.

# WG2 (Non-RT RIC, A1, R1) Impact

Assess impact to A1 and R1 interfaces and non-RT RIC architecture, including AI/ML training and deployment. Add new use cases and corresponding requirements and specifications in case there is an impact to A1 or R1 interfaces.

# WG5 (O-CU and O-DU) Impact

Assess impact on O-CU and O-DU support for dials and knobs described in the use-case.

# WG10 (SMO, O1) Impact

Assess impact with PM coordination group and IM/DM coordination group on support of proposed dials (measurements) and knobs (configuration IM/DM) and incorporation in existing O1 interface models, as well as any required coordination with 3GPP.

Summary: A detailed analysis of the specification impact is to be completed. There is large specification impact to specify new proposed measurement definitions and measurement reporting in 3GPP or in O-RAN. The impact of the required measurements and configurations will be reduced if they are already part of ongoing/upcoming O-RAN specifications (ffs) or are being considered for specification in other bodies such as 3GPP (ffs).

# 6.2.3 Solution 3: MIMO mode selection (Mu-MIMO vs Su-MIMO selection optimization)

In this section the use case pertaining to optimal selection of Su-MIMO vs. Mu-MIMO is addressed. We shall explicitly refer to various inputs (aka dials) that are recommended for input into the AI/ML analytics Apps in order to optimally determine the outputs (aka knobs) of the Mu-MIMO and Su-MIMO selection control.

# Problem Statement, Solution, and Value Proposition

A successful MU-MIMO operation involves the realization of as many orthogonal radio frequency channel links between multiple spatially separated users as possibly as supported by the implementation software at the digital domain. Key to such realization is the successful beamforming weight determination that enables not only the phase addition of multipath signals at the user receiver, but also the choice of precoding algorithms which limit the residual interference between the paired users. AI/ML driven solutions can optimize such selections, as captured also in Section 3.3. It can make sense for the scheduler to prioritize the assignment of radio resources to a MU-MIMO mode of operation during periods of congestion or when high latency requiring applications are supported (to free up other resources that can be assigned sooner). However, doing so at the expense of undesirably lower spectral efficiency on these assigned radio resources will reduce overall sector throughput levels and create poor user experience. It is important to find a means through the AI/ML agent to distinguish users and identify sectors where optimal operation means a greater assignment of SU-MIMO modes independently to users, especially those requiring higher throughput, using devices that are capable of supporting higher layer SU-MIMO count, and operating in an environment that sustains a greater channel rank.

In this section, the use case pertaining to the optimal selection of SU-MIMO vs. MU-MIMO for assignment to users to maximize the realized spectrum efficiency is addressed. We shall explicitly refer to various inputs (aka dials) that are recommended for input into the AI/ML analytics Apps in order to optimally determine the outputs (aka knobs) for the MU-MIMO and SU-MIMO mode selection control.

Indication of MIMO Type and Layers

1. Percent TTIs SU-MIMO vs. MU-MIMO vs Hybrid (TTI with SU-MIMO and MU-MIMO) [Dial15] a. AI/ML training will use this data to further optimize scheduler with the aim to increase overall cell spectral efficiency, based on pairing opportunities, data in buffer, larger SU-MIMO layer assignments etc.   
2. Joint Histogram of simultaneous MU-MIMO and SU-MIMO Layers assigned per PRB [Dial17] a. This joint histogram allows the operator to assess the Mu-MIMO layer performance and also the SuMIMO performance conditioned on the Mu-MIMO layer example shown below:

Table 6.2.3.1-1.   

<table><tr><td rowspan=1 colspan=1>Mu-MIMO/Su-MIMO</td><td rowspan=1 colspan=1>Su-MIMO Layer = 1</td><td rowspan=1 colspan=1>Su-MIMO Layer = 2</td><td rowspan=1 colspan=1>…</td><td rowspan=1 colspan=1>Su-MIMO Layer = M</td></tr><tr><td rowspan=1 colspan=1>Mu-MIMO Layer = 1</td><td rowspan=1 colspan=1>10%</td><td rowspan=1 colspan=1>20%</td><td rowspan=1 colspan=1>…</td><td rowspan=1 colspan=1>20%</td></tr><tr><td rowspan=1 colspan=1>Mu-MIMO Layer = 2</td><td rowspan=1 colspan=1>%</td><td rowspan=1 colspan=1>%</td><td rowspan=1 colspan=1>…</td><td rowspan=1 colspan=1>%</td></tr><tr><td rowspan=1 colspan=1>…</td><td rowspan=1 colspan=1>…</td><td rowspan=1 colspan=1>…</td><td rowspan=1 colspan=1>…</td><td rowspan=1 colspan=1>…</td></tr><tr><td rowspan=1 colspan=1>Mu-MIMO Layer = N</td><td rowspan=1 colspan=1>%</td><td rowspan=1 colspan=1>%</td><td rowspan=1 colspan=1>…</td><td rowspan=1 colspan=1>%</td></tr></table>

Optimization based upon AI/ML training might result in a joint histogram output reflecting a cell’s operation that has now moved more to the lower right side of Table 6.2.3.1-1, relative to the pre optimization scenario belonging some place to the left upper part of Table 6.2.3.1-1. AI/ML exercise might identify for various loading conditions and end user device counts, how much optimization is possible to move performance from current position to one of a higher level, in accordance with the dimensions of Table 6.2.3.1-1.

# Downlink MIMO Quality

1. Downlink CQI Report histogram (SU-MIMO) vs. chosen MCS/CQI index [Dial18] a. Histogram indicating higher CQI bias would mean that there is scope for scheduler to favor higher layer SU-MIMO assignment vs. MU-MIMO. Channel specific to cell, UE distribution favor and traffic loading is used for AI/ML training with this CQI report.

2. CSI signal-to-noise and interference ratio (CSI-SINR) histogram [Dial21] a. This metric gives an implicit indication of channel estimation reliability used for AI/ML training for GoB based MU-MIMO, using Type II feedback. If below a threshold, SU-MIMO can be prioritized over MU-MIMO. CSI-SINR can be used for mobility cases by imparting intelligence into the channel estimation confidence determination.

Uplink MIMO Quality

1. Minimum, Average (linear), and Maximum Uplink SINR per UE histogram (SINR range: -10 to $+ 3 0$ dB) (SUMIMO) [Dial23] is required to check uplink quality for SU-MIMO vs. MU-MIMO selection.

Condition Number

1. SU-MIMO Condition number in dB histogram (21 dB to 0 dB) [Dial28] a. High Condition numbers reported at high percentage of times will discourage the AI/ML training to recommend SU-MIMO assignment   
2. SU-MIMO Reported Rank distribution histogram (R $\operatorname { u n k } = 1 , \dots . . . , \operatorname { M a x } \mathrm { { R a n l } }$ k) [Dial29] a. Used to estimate the feasibility of higher layer support

Spectral Efficiency is constantly monitored to allow optimization using the following KPIs:

1. MU-MIMO vs. SU-MIMO PRB Utilization Histogram [Dial30] and [Dial35]   
2. MU-MIMO vs. SU-MIMO PDCP Volume histogram [Dial32] and [Dial36]   
3. MU-MIMO vs. SU-MIMO DRB (DL and UL) Throughput Histograms [Dial33] and [Dial37]   
4. MU-MIMO vs. SU-MIMO Spectral Efficiency [Dial34] and [Dial38]

The following will be the outputs or knobs for the optimization App:

MIMO Mode Setting

1. Operator shall be able to set any UE to either SU-MIMO only or MU-MIMO only by QCI threshold [Knob13] a. A shutout mechanism for UEs under adversarial conditions for either of the two MIMO modes, as appropriately decided based upon AI/ML training output and inference.   
2. Set SU-MIMO Rank – The Condition Number target [Knob14] a. If above an AI/ML (training outcome) determined threshold, and for UE buffer status, cell loading etc. MU-MIMO if viable, will be prioritized over SU-MIMO.

Beam Commands

1. CSI-RS Density [Knob20]

a. Can be increased or decreased based on CSI feedback reliability as assessed and set as a target by AI/ML non-real time RIC.

The reader is referred to Section 3.3 for an invaluable use case for selecting the Massive MIMO mode in each user environment. This use case can be expected to make feasible the ability to put priority upon MU-MIMO selection as a means towards achieving optimisation. However here we limit the scope to giving additional examples of how the subsequent list of dials and knobs can be exploited in various important use cases.

With increased loading Massive MIMO systems will incur rising levels of interference on the uplink from connected users and on the downlink from the gNB. In addition to normal SINR measurements, the diagnosis of interference from all spatial directions uniformly (white spatial noise) versus specific directions (spatially correlated noise) will be of interest and will require MIMO modes (SU-MIMO vs MU-MIMO) to be properly selected for assignment on a user basis. Such implementation will optimize the per user and per cell throughputs, taking into consideration channel orthogonality conditions rank realizable, and per user effective bandwidth requirement. Optimization will also factor into consideration the interaction and dependencies between multiple features or capabilities, such as carrier aggregation vs. beamforming capability and carrier aggregation vs. MU-MIMO assignments, for example.

Dials that indicate the type of spatial interference are included in the Uplink Covariance “dial” which is also required in the GoB handover use case in Section 3.3. Interference that could include inter-cell Pilot contamination must be identified and mitigated. Mitigation can be improved with pilot sequence tracking and distribution, as presented in the in the knobs section.

# Architecture/deployment Options

The non-RT RIC trains and updates the specific MIMO Mode Selection AI/ML models. Figure 6.2.3.2-1 reflects the functional dependencies of the AI/ML implementation framework. The MIMO Mode Selection (MMS) rAPP targets to optimize user throughput vs cell throughput. As shown in Figure 6.2.3.2-1, the rApp uses O1 and $\mathrm { F H ~ m }$ -plane measurement data (via SMO exposed services). The MMS rApp running in the non-RT RIC uses O1data to optimize cell MU-MIMO vs. SU-MIMO assignment by configuring O-DU over O1 interface parameters (via SMO exposed services over R1 interface).

![](images/e8463fad0a5effc4c8efceca198d94ed0e8325814e60abeac4320344b2e5ac43.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.2.3.2-1. O-RAN Architecture Diagram for MIMO mode selection use case

![](images/dae34c93605954b789a691126a488a891d0140108f7dfa4a35bf6dcadfcc64e3.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.2.3.2-2. Call Flow Diagram for MIMO mode selection use case

In the call in Figure 6.2.3.2-2, the rApp can request the current MIMO configuration listed in Table 6.2.3.2-6 (steps 2-5), as well as current network measurements and KPIs listed in Table 6.2.3.2-1 to Table 6.2.3.2-5 (steps 7-10). The R1 interface is used by the rApp to communicate these requests to SMO, which in turn coordinates the collection via O1 interface. The AI/ML model that is part of the rApp will use the measurements to evaluate the current capacity and UE performance and if required, will generate a recommendation to update one or more of the identified configuration knobs (step 16). This new recommendation is sent to SMO via R1 interface, and finally communicated to the O-DU via O1 interface (step 18).

# Requirements

In order to achieve the value proposition described above, the key Massive MIMO KPIs or dials need to be monitored to assess the state of the system.

All the dials/measurements listed here are required at a configurable granularity in multiples of 1 minute, ranging from 1 to 15 minutes.

Table 6.2.3.2-1. Dials for indication of MIMO types and layers   

<table><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>Percent TTIs SU-MIMO vs. MU-MIMOvs Hybrid (TTi with SU-MIMO and MU-MIMO)</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=2>1 .. 15 min.</td><td rowspan=1 colspan=1>[Dial15]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU↓Non-RTRIC</td><td rowspan=1 colspan=1>Histogram of percent usage vs. # ofMU-MIMO users (users = 2,. ..,K)</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=2>1 .. 15 min.</td><td rowspan=1 colspan=1>[Dial16]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>JointHistogramn of simultaneousMU-MIMOandSU-MIMO LayersassignedperPRB(MU-MIMOpercentage vs. MU-MIMO (layers1,..,N) and N SU-MIMO (layers1,..,M) histograms each conditionedon a given no. of MU-MIMO layers)</td><td rowspan=1 colspan=2>Percent</td><td rowspan=1 colspan=1>1…15min.</td><td rowspan=1 colspan=1>[Dial17]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr></table>

Table 6.2.3.2-2. Dials for downlink MIMO quality   

<table><tr><td rowspan=2 colspan=1>01</td><td rowspan=2 colspan=1>O-DU→Non-RTRIC</td><td rowspan=2 colspan=1>Downlink CQI Report 1histogram(one CQI histogram(percent use vs.CQI index) for each number of MU-MIMO UEs in parallel  (e.g.1,2,3,.K )(see Section 3.3 for otheruse cases)</td><td rowspan=2 colspan=1>Percent</td><td rowspan=1 colspan=1>1      15</td><td rowspan=2 colspan=1>[Dial18]</td><td rowspan=2 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>min.</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>ZP reference measurement value perbeam (average value – dBm)</td><td rowspan=1 colspan=1>dBm</td><td rowspan=1 colspan=1>1 …15min.</td><td rowspan=1 colspan=1>[Dial20]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>Para. 5.1.6 ([5]) CSI signal-to-noiseand interference ratio (CSI-SINR)histogram</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1…15min.</td><td rowspan=1 colspan=1>[Dial21]</td><td rowspan=1 colspan=1>Existingspecification[5]Newmeasurementreporting</td></tr></table>

Table 6.2.3.2-3. Dials for uplink MIMO quality   

<table><tr><td rowspan=2 colspan=1>01</td><td rowspan=2 colspan=1>O-DU→Non-RTRIC</td><td rowspan=2 colspan=1>Minimum, Average(linear), andMaximum Uplink SINR or Co-UEinterference, Noise and ExternalInterference Levelper UE (MU-MIMO pair histogram (SINR range: -10 dB to + 30 dB) for 1,2, 3, . ., KUEs)</td><td rowspan=2 colspan=1>Percent</td><td rowspan=1 colspan=1>1…15min.</td><td rowspan=2 colspan=1>[Dial22]</td><td rowspan=2 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>Percent time MU-MIMO UEs are atmaximum TX power and &lt; 5 PRB(Ref. [3])</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1…15min.</td><td rowspan=1 colspan=1>[Dial24]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr></table>

Table 6.2.3.2-4. Dials for condition number   

<table><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU →Non-RTRIC</td><td rowspan=1 colspan=1>SU-MIMO Condition number indB histogram (21 dB to 0 dB)</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1  … 15min.</td><td rowspan=1 colspan=1>[Dial28]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU →Non-RTRIC</td><td rowspan=1 colspan=1>SU-MIMO    Reported    Rankdistributionhistogram(Rank=1.,..Max Rank)</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1：15min.</td><td rowspan=1 colspan=1>[Dial29]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr></table>

Table 6.2.3.2-5. Dials for spectral efficiency   

<table><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>MU-MIMO   PRB   UtilizationHistogram</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1 …15min.</td><td rowspan=1 colspan=1>[Dial30]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>Total PRB % Used Supporting MU-MIMO histogram</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1 … 15min.</td><td rowspan=1 colspan=1>[Dial31]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>MU-MIMO    PDCP    Volumehistogram</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1 …15min.</td><td rowspan=1 colspan=1>[Dial32]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>MU-MIMO DRB (DL and UL)Throughput Histograms (min., ave.,and max.) (100 kbps, 200, kbps, etc.10 Gbps) vs. Mu-MIMO layers(1,2.. )</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1 … 15min.</td><td rowspan=1 colspan=1>[Dial33]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>MU-MIMO Spectral Efficiency(8*PDCP       Volume/(BW*PRButilization)， bits/sec./Hz histogramover measurement period, where Bw= bandwidth,Hz) note:allparallel/paired PRBs count as oneover a TTI</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1 …15min.</td><td rowspan=1 colspan=1>[Dial34]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>SU-MIMO   PRB   distributionhistogram</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1 … 15min.</td><td rowspan=1 colspan=1>[Dial35]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>SU-MIMO PDCP Volume (Mbytes)histogram</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1 …15min.</td><td rowspan=1 colspan=1>[Dial36]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>SU-MIMO DRB (DL and UL)Throughput (Kbits/sec.） Histogramas a function of Mu-MIMO layers (1,2,, )</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1 …15min.</td><td rowspan=1 colspan=1>[Dial37]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>O-DU→Non-RTRIC</td><td rowspan=1 colspan=1>SU-MIMO  Spectral  Efficiency(8*PDCP     Volume/(BW*PRB)utilization   ratio  (bits/sec./Hz)histogram over measurement period,where BW = bandwidth, Hz)</td><td rowspan=1 colspan=1>Percent</td><td rowspan=1 colspan=1>1…15min.</td><td rowspan=1 colspan=1>[Dial38]</td><td rowspan=1 colspan=1>NewmeasurementdefinitionNewmeasurementreporting</td></tr></table>

Similar to the measurement and monitoring objective of the “dials” section, the control of key parameters is the objective of the “knobs” section. This allows the value proposition of allowing each operator to satisfy their respective unique optimality criteria via emerging AI/ML technologies.

Must have: Settable SU-MIMO only or MU-MIMO only mode per class of user (e.g., QCI)

Must have: Specifiable threshold on condition number and SINR that dictates the scheduled SU-MIMO rank of any given user

Table 6.2.3.2-6. Knobs for MIMO mode setting and beam commands   

<table><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>Non-RTRIC →O-DU</td><td rowspan=1 colspan=1>Operator shall be able to set any UEto either SU-MIMO only or MU-MIMO only by QCI threshold</td><td rowspan=1 colspan=1>integer</td><td rowspan=1 colspan=1>1..15min.</td><td rowspan=1 colspan=1>[Knob13]</td><td rowspan=1 colspan=1>New</td></tr><tr><td rowspan=1 colspan=1>OI1</td><td rowspan=1 colspan=1>Non-RTRIC→O-DU</td><td rowspan=1 colspan=1>SetSU-MIMO Rank.      Thecondition number (ratio of the max.eigenvalue to min. eigenvalue) shallbe calculated internally in real timeand allow the operator to set a threshold based on condition numberthat is used to take the UE reportedSU-MIMO rank and convert to agNB transmitted rank</td><td rowspan=1 colspan=1>integer</td><td rowspan=1 colspan=1>1..15min.</td><td rowspan=1 colspan=1>[Knob14]</td><td rowspan=1 colspan=1>New</td></tr><tr><td rowspan=1 colspan=1>01</td><td rowspan=1 colspan=1>Non-RTRIC →O-DU</td><td rowspan=1 colspan=1>CSI-RS density (0.3, 1, 3, etc.)</td><td rowspan=1 colspan=1>Fixedpoint</td><td rowspan=1 colspan=1>1..15min.</td><td rowspan=1 colspan=1>[Knob20]</td><td rowspan=1 colspan=1>New</td></tr></table>

Note: It is FFS whether any of the listed measurements have any dependency on O-RU and if any information needs to be exchanged over O-RAN FH m-plane interface from O-RU to O-DU.

# O-RAN Entity roles:

1) SMO & Non-RT RIC a) Collect existing configuration and performance data from RAN b) Trigger AI/ML Model training/update and deployment as necessary c) Apply MIMO pairing control recommendations from rApp via R1 and O1 interface using config management service.   
2) O-CU nodes a) Report current configuration and performance data to non-RT RIC rApp via O1 interface if required.   
3) O-DU nodes a) Report current configuration and performance data to non-RT RIC rApp via O1 interface. b) Apply MIMO pairing control related knobs based on rAPP recommendation.

# Impact Analysis on O-RAN WGs

Editor’s note: This is an initial impact analysis as part of the WG1 UCTG work on mMIMO. The intention is to estimate the expected standardization effort within the O-RAN working groups. It is up to the WGs to decide how the mMIMO functionality should be specified in specifications of each WG, and whether it will be part of existing or new set of specifications.

Update WG1 use case analysis report and use-case detailed specification with MU-MIMO pairing control use case. No impact to existing architecture.

WG2 (Non-RT RIC, A1, R1) Impact

Assess impact to A1 and R1 interfaces and non-RT RIC architecture, including AI/ML training and deployment. Add new use cases and corresponding requirements and specifications in case there is an impact to A1 or R1 interfaces.

# WG5 (O-CU and O-DU) Impact

• Assess impact on O-CU and O-DU support for dials and knobs described in the use-case.

WG10 (SMO, O1) Impact

Assess impact with PM coordination group and IM/DM coordination group on support of proposed dials (measurements) and knobs (configuration IM/DM) and incorporation in existing O1 interface models, as well as any required coordination with 3GPP.

Summary: A detailed analysis of the specification impact is to be completed. There is large specification impact to specify new proposed measurement definitions and measurement reporting. The impact of the required measurements and configurations will be reduced if they are already part of ongoing/upcoming O-RAN specifications (ffs) or are being considered for specification in other bodies such as 3GPP (ffs).

# 7 Comparison and Conclusions

This Technical Report presents the results of the pre-normative phase mMIMO work item. Multiple mMIMO optimization algorithms have been analyzed, including beam-based Mobility Robustness Optimization, Grid of Beam Optimization, Non-Grid of Beam Optimization, L1/L2 Beam Management Optimization, AI/ML assisted optimized SS Burst Set, DMRS and CSI-RS configuration.

Beam-based Mobility Robustness Optimization (bMRO) is an autonomous self-optimizing algorithm that improves beambased inter-cell mobility performance by applying beam-specific Cell Individual Offsets (CIO) on the handover triggers between neighbor cells, based on the analysis of beam-specific mobility-related counters. The bMRO algorithm might be hosted in Non-RT RIC or Near-RT RIC. Based in mobility KPIs forwarded to the RIC from the O-CU, the RIC configures the beam-based CIO in the O-DUs. Simulation based evaluation shows a significant reduction in too early and too late handovers as well as a reduction of the total UE outage and mobility failure rate, as well as a reduced number of pingpong handovers. The gain was shown for a mixed mobility (UEs with $3 \ \mathrm { k m / h }$ and $3 0 \mathrm { k m } / \mathrm { h }$ ) scenario in an urban micro deployment according to 3GPP TR38.901. The computational complexity and signaling overhead are a multiple of that of the legacy cell-based MRO where the multiplier is the number of beams that are supported in a cell. Complexity and signaling overhead can be reduced by enhanced proprietary implementations, e.g., forming virtual groups of beams with similar characteristics. bMRO is suggested for normative standardization with the foreseen impact on O-RAN WGs as outlined in Section 3.3.3. There is a dependency on completion of 3GPP Rel.17 for the completion of stage 3 in O-RAN.

Grid of Beam Optimization (GoB) provides an automated beam forming configuration tailored to the topology of the cell, the physical environment, as well as the distribution of users and traffic in a cell (e.g. wide beams might cover low-density areas while narrow beams might cover high-density areas). The output of the algorithm are the optimized GoB BF configurations, that are, the number of beams and either i) the beam directions, horizontal & vertical beam widths, and power allocation of beams, or ii) the beam weights, transferred via the Open Fronthaul interface. The GoB algorithm might be hosted in Non-RT RIC or Near-RT RIC. First trial results show that the ML based beam pattern optimization algorithm can adapt to the traffic distribution and hence provides a significant gain in terms of weighted downlink RSRP. Uplink throughput enhancements are also expected since SSB beams are used for uplink receive beamforming. The gain was shown for NR TDD at $3 . 5 \ : \mathrm { G H z }$ with 1 to 20 UEs either stationary or with drive tests in a shopping street scenario. Different options for input parameters have been identified in the pre-normative phase, which are not supported by existing O-RAN and 3GPP specifications. The output parameters are supported by the existing O-RAN Open Fronthaul specification (i.e. O-FH M-Plane, O-FH CUS-Plane). GoB is suggested for normative standardization with the foreseen impact on O-RAN WGs as outlined in Section 3.2.3, while the preferred option for input parameter still needs to be analyzed and selected.

Non-GoB optimization makes use of AI/ML techniques to optimize the beamforming algorithm for each UE, depending on UE and cell conditions. Multiple beamforming algorithm options exist, including both Grid of Beams and Non-Grid of Beams, the latter typically involving beam weights being calculated based on SRS measurements. This itself comprises multiple different algorithm options, which can have differing relative performance depending on UE conditions, cell conditions, SRS configuration, etc. Therefore, it is important that the optimal choice of beamforming algorithm option is applied for each UE. The non-GoB use case takes into account that such beamforming algorithms are generally proprietary and vendor specific. Training is assumed to be cell-based, residing in non-RT RIC, making use of measurements reported from O-DU as well as enrichment data obtained externally, for example related to location and mobility. Inferencing is assuming to be hosted in an xApp in near-RT RIC, based on similar measurements as for training, the output of which is the control of the beamforming modes that should be applied for a given UE. The control may be specified separately for multiple MIMO options (e.g. SU and MU). The update rate is assumed to be 100s of ms, considerably slower than the MAC scheduling update rate. Initial simulation results for a simple SU-MIMO case demonstrate the opportunity for significant performance gains by tailoring beamforming mode to the UE conditions. Per-UE measurement reporting might be specified in 3GPP specifications (e.g. 3GPP TS37.320) and referred to in O1/E2 specifications with limited or no impact on O-RAN specifications. Or per-UE measurement reporting might be specified in O-RAN specifications with small impact on WG3 and potentially moderate impact WG5. Non-GoB is suggested for normative standardization with the foreseen impact on O-RAN WGs as outlined in 5.2.3.

In yet another optimization approach, AI/ML assisted network-wide (multi-gNB/TRP) optimizations framework proactively and autonomously infers optimal configuration per gNB/TRP for SS Burst Set, DMRS and CSI-RS based on available measurements, observations, and PIs at different nodes of the 3GPP NR and/or O-RAN access and core network elements. One of the preferred options is to train the AI/ML model offline in the SMO/Non-Real Time RIC. Trained model might be hosted in Non-Real Time RIC or Near-Real Time RIC depending on the selected optimization problem. For SS Burst Set configuration optimization, offline trained AI/ML model can be deployed in Non-Real Time RIC as rAPP. Based on the KPIs, observations and measurements from E2 nodes over O1 interface, inferred optimal SS Burst Set configuration is applied to E2 nodes (O-CU and/or O-DU) over O1 interface. Numerical analysis-based data presented as use case feasibility analysis shows that optimal configurations have potential to improve per-gNB/TRP spectral efficiency through saving time-frequency resources for both FR1 and FR2 systems with multiple transceiver chains. One of the design goals of the AI/ML optimizer is that it should target to limit the impacts on other system performances (e.g, initial access latency, maximum mobility support etc.) through operator defined KPI constrained optimization technique. Impacts on the R1 interface. For both DMRS and CSI-RS configuration optimization use cases, Near-Real Time RIC is considered as one of the preferred model deployment options. Optimal configurations can be generation every few tens of ms when needed by the E2 nodes. These configurations are UE specific. Trained model uses measurements, observations and PI generated by E2 nodes to derive the inference and applies back to E2 nodes over E2 interface. Numerical calculation-based analysis shows that optimal configurations can improve per-gNB/TRP spectral efficiency noticeably through saving time-frequency resources for both FR1 and FR2 systems with multiple transceiver chains. One important aspect of the optimizer is to limit the impacts on other system performances (e.g, maximum mobility support, time-frequency tracking accuracy etc.) through KPI (operator specified) constrained optimization techniques. Computational complexity for all three use cases described in this section depends on the size of training data set (measurement, observations and KPI data set) and the type of algorithm used. AI/ML assisted optimized SS Burst Set, DMRS and CSI-RS configuration is suggested for normative standardization with the foreseen impact on O-RAN WGs as outlined in section 3.4.2.1.1 and section 3.4.2.2.1.

L1/L2 Beam Management Optimization will contribute to improved network performance in terms of throughput and reliability by utilizing AI/ML techniques to enable RAN to make wiser decision on UE-specific beam management operations. The beam management optimization algorithm could be used to estimate or predict the quality of beams based on limited beam measurement reported from O-DU as well as enrichment information (e.g., UE position and velocity) obtained externally, which allows beam selection with high accuracy and ensures reliable radio link against blockage, especially in mmWave. The output of algorithm will be the optimized control/policy related to beam management operations, which may potentially involve the configuration of beam measurement/reporting, beam indication and beam failure recovery, could be further study in the normative phase. Initial simulation results which assumed high-mobility urban street scenario show that the AI/ML-based solution can ensure beam tracking accuracy while significantly reducing beam measurement overhead. Different deployment options were discussed and compared (e.g., the AI/ML model training and inference can be hosted in the Non-RT RIC and Near-RT RIC respectively, or the AI/ML model training can be hosted in Non/Near-RT RIC while the AI/ML inference can be hosted in the E2 Nodes), which demonstrate different strengths and weaknesses. L1/L2 Beam Management Optimization is suggested for normative standardization with the foreseen impact on O-RAN WGs as outlined in Section 4.2.3.

# 7.1 Summary of Evaluation

Table 7.1-1: Summary of Evaluation   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Solution</td><td rowspan=1 colspan=1>Means of evaluation</td><td rowspan=1 colspan=1>Summary of result</td><td rowspan=1 colspan=1>#of       InputParameters</td><td rowspan=1 colspan=1>#of       OutputParameters</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>GoB Optimization</td><td rowspan=1 colspan=1>Trial results with 1 to 20 UEs,stationary or drive test, shopping streetscenario</td><td rowspan=1 colspan=1>8.2 dB gain ofweighted RSRP</td><td rowspan=1 colspan=1>1(up to 3 optionsmight       bedefined)</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>bMRO Optimization</td><td rowspan=1 colspan=1>Detailed multi-cell system level simulation(incl. UE L3 mobility, detailed timers etc.)</td><td rowspan=1 colspan=1>Gain against legacy MRO58% less too-late HO23% less too-early HO</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>3a</td><td rowspan=1 colspan=1>GoB RRM SSB Opt.</td><td rowspan=1 colspan=1>Numerical RS overhead analysis based onavailable numerologies in the 3GPP NR</td><td rowspan=1 colspan=1>Max. potential gain (best vs. worst)numerology neglecting other impact</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>1 + 6(6 initialization)</td></tr><tr><td rowspan=1 colspan=1>3b</td><td rowspan=1 colspan=1>GoB RRM DMRS Opt.</td><td rowspan=1 colspan=1>Numerical RS overhead analysis based onavailable numerologies in the 3GPP NR</td><td rowspan=1 colspan=1>Max. potential gain (best vs. worst)numerology neglecting other impact</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>1 +2(2 initialization)</td></tr><tr><td rowspan=1 colspan=1>3c</td><td rowspan=1 colspan=1>GoB RRM CSI-RS Opt.</td><td rowspan=1 colspan=1>Numerical RS overhead analysis based onavailable numerologies in the 3GPP NR</td><td rowspan=1 colspan=1>Max. potential gain (best vs. worst)numerology neglecting other impact</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>1 + 2(2 initialization)</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>L1/2 Beam Management</td><td rowspan=1 colspan=1>Urban street with 1 gNB @ 28 GHz, simplifiedUE mobility (60km/h fixed)， different beammeasurement periods</td><td rowspan=1 colspan=1> No loss of beam measurement accuracyeven for reduced beam measurementperiod</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>1(output optionsffs)</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>Non-GoB Optimization</td><td rowspan=1 colspan=1>Simplified, single cell simulation, Singlesuboptimum SU-MIMO fixed 2 layers mode(GoB vs. non-GoB mode) for 1 km/h and 120km/h</td><td rowspan=1 colspan=1>Max.potential gain against a fixedsuboptimum MIMO mode1km/h: 2% av. &amp; 60% 5%tile TP120km/h: 14% av. &amp; 141% 5%tile TP</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>1 +3(2 initialization + 1training)(training config.ffs)</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>DL Tx Power Opt.</td><td rowspan=1 colspan=1>Simple single cell urban scenario at 2 GHzwith 8 UEs with no inter-cell interference</td><td rowspan=1 colspan=1>Different SINR received at UEs using MU-MIMO is shown. No results otherwise.</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>MU-MIMO User Pairing</td><td rowspan=1 colspan=1>No</td><td rowspan=1 colspan=1>No</td><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>16</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>SU-/MU-MIMO Switching</td><td rowspan=1 colspan=1>No</td><td rowspan=1 colspan=1>No</td><td rowspan=1 colspan=1>19</td><td rowspan=1 colspan=1>3</td></tr></table>

# 7.2 Impact on standardization

Table 7.2-1: Impact on standardization   

<table><tr><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1>Solution</td><td rowspan=2 colspan=1>#    of    newmeasurementdefinitions</td><td rowspan=2 colspan=1>#    of    newmeasurementreporting</td><td rowspan=2 colspan=1># of new outputparameterdefinition 1)</td><td rowspan=2 colspan=1># of new outputparameterconfiguration2)</td><td rowspan=2 colspan=1>O-RANimpactanalysis</td><td rowspan=2 colspan=1>3GPPimpact analysis</td><td rowspan=2 colspan=1>Suggested        splitbetween 3GPP /O-RAN</td><td></td></tr><tr><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>GoB Optimization</td><td rowspan=1 colspan=1>1or2</td><td rowspan=1 colspan=1>1or2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Detailed analysis.</td><td rowspan=1 colspan=1>O-RAN refers to 3GPPspec for measurements</td><td rowspan=1 colspan=1>(cid:)</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>bMROOptimization</td><td rowspan=1 colspan=1>5       (currentlydiscussed     in3GPP Rel.17)</td><td rowspan=1 colspan=1>5      (currentlydiscussed    in3GPP Rel.17)</td><td rowspan=1 colspan=1>1      (currentlydiscussed    in3GPP Rel.17)</td><td rowspan=1 colspan=1>1     (currentlydiscussed   in3GPP Rel.17)</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Detailed analysis.Rel.17     workongoing.</td><td rowspan=1 colspan=1>O-RAN refers to 3GPPspec for measurements</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>3a</td><td rowspan=1 colspan=1>GoB RRM SSBOpt.</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1 + 1 (init)</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>General analysis</td><td rowspan=1 colspan=1>O-RAN refers to 3GPPspec for measurements</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>3b</td><td rowspan=1 colspan=1>GoB RRM DMRSOpt.</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1 + 2 (init.)</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>General analysis</td><td rowspan=1 colspan=1>O-RAN refers to 3GPPspec for measurements</td><td rowspan=1 colspan=1>(cid:)</td></tr><tr><td rowspan=1 colspan=1>3c</td><td rowspan=1 colspan=1>GoB RRM CSI-RS Opt.</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1 + 2 (init.)</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>General analysis</td><td rowspan=1 colspan=1>O-RAN refers to 3GPPspec for measurements</td><td rowspan=1 colspan=1>(cid:)</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>L1/2       BeamManagement</td><td rowspan=1 colspan=1>1 (optional)</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>General analysis</td><td rowspan=1 colspan=1>2Options</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>Non-GoBOptimization</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>11 + 3 (init. +training)</td><td rowspan=1 colspan=1>1 +2(init.training)</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>General analysis</td><td rowspan=1 colspan=1>2 Options</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>DL Tx Power Opt.</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>ffs</td><td rowspan=1 colspan=1>ffs</td><td rowspan=1 colspan=1>ffss</td><td rowspan=3 colspan=1></td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>MU-MIMOUserPairing</td><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>ffss</td><td rowspan=1 colspan=1>ffs</td><td rowspan=1 colspan=1>ffs</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>SU/MU-MIMOSwitching</td><td rowspan=1 colspan=1>19</td><td rowspan=1 colspan=1>19</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>ffs</td><td rowspan=1 colspan=1>ffs</td><td rowspan=1 colspan=1>ffs</td></tr></table>

Note 1) An example for an output parameter definition is an Information Element as defined in the 3GPP RRC specification or any interface specification (e.g. Xn, NG). Note 2) An example for an output parameter configuration is an Information Element for $\mathrm { g N B }$ configuration as defined in the 5G Network Resource Model in 3GPP TS28.54

# 7.3 Synergies among new measurements (definition and/or reporting)

Table 7.3-1: Synergies among new measurements   

<table><tr><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Measuredat whichentity</td><td rowspan=1 colspan=1>UE or cell specificreporting</td><td rowspan=1 colspan=1>G0BOpt.</td><td rowspan=1 colspan=1>L1/2          BeamManagement</td><td rowspan=1 colspan=1>Non-GoBOpt.</td><td rowspan=1 colspan=1>SSB,    CSI-RS,DM-RS Opt.</td><td rowspan=1 colspan=1>MIMOOptimization</td><td rowspan=1 colspan=1>Measurementsynergies</td></tr><tr><td rowspan=1 colspan=1>CSIreport (e.gCQI, PMI, RI, LI,CRI)</td><td rowspan=1 colspan=1>UE report</td><td rowspan=1 colspan=1>per UE</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>x (histogram)</td><td rowspan=1 colspan=1>3 + 1</td></tr><tr><td rowspan=1 colspan=1>ChannelCovariance Matrix</td><td rowspan=1 colspan=1>O-DU</td><td rowspan=1 colspan=1>per UE</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>L1-RSRP (SSB orCSI based)</td><td rowspan=1 colspan=1>UE report</td><td rowspan=1 colspan=1>per UE</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>L1-SINR (SSB orCSI based)</td><td rowspan=1 colspan=1>UE report</td><td rowspan=1 colspan=1>per UE</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>x (histogram)</td><td rowspan=1 colspan=1>2+1</td></tr><tr><td rowspan=1 colspan=1>UL SRS RSRP</td><td rowspan=1 colspan=1>O-DU</td><td rowspan=1 colspan=1>per UE</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>x</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2</td></tr></table>

Note 1: Table 7.3-1 is limited to new input measurements mentioned in multiple proposals.

Note 2: The beam-based MRO proposal is not considered in Table 7.3-1, since it does not have commonalities in terms of input/output parameters with the other proposals.

# Annex A Input and output data and its relation to 3GPP specification

One of the objectives of the Massive MIMO pre-normative phase is to analyse and evaluate the set of input/output parameters for each Massive MIMO use case. Once identified, the impact on O-RAN specification as well as dependencies on 3GPP specifications should be analyzed. This annex provides some background information on how input/output parameters might relate to 3GPP specifications.

3GPP defines a very large number of measurements. Among others, these include:

Layer 1 (PHY) UE and gNB measurements o Signal strength and signal quality measurements o TS 38.215 NR; Physical layer measurements Layer 2 (MAC) UE measurements o Power headroom reporting and buffer status reporting o TS 38.321 NR; Medium Access Control (MAC) protocol specification Layer 2 (MAC) gNB measurements o Load, delay and packet loss rate measurements o TS 38.314 NR; Layer 2 measurements   
Layer 3 (RRC) UE measurements o Mobility measurements and measurement reporting o TS 38.331 NR; Radio Resource Control (RRC); Protocol specification

There are many more well-defined measurements often exchanged via peer to peer signalling embedded in various protocols. Over the generations 3GPP refined its specifications and extended the number of standardized measurements. For instance, the L2 gNB measurements have been specified with the introduction of 3GPP LTE. It can be assumed that most of the measurements as specified in 3GPP are implemented in the UE and at the network side. Besides the accurate specification for implementation, there are also extensive test specifications defined for each measurement, at least for UE measurement reporting.

Besides the measurements as such, also means for reporting measurements and other metrics towards the management system are defined. Current 3GPP specifications define different types of metrics. Most relevant specifications in this perspective are:

TS 28.552 specifies 5G Performance Measurements (PMs). These are counters aggregated, e.g., per DU, CU or per core function, for example an AMF Function. An example is the “Number of Active UEs in the DL per cell” which provides information about the mean number of active UEs in a cell.   
• TS 28.554 specifies 5G end to end Key Performance Indicators (KPIs). These specify further aggregation of the counters defined in TS 28.552. One example is the “maximum registered subscribers of network slice through AMF” (clause 6.2.6) where the subscribers in the AMF that are registered are aggregated per network slice.   
• TS 37.320 and TS 32.422 specify trace and minimization of drive test (MDT). Trace logs are messages per UE and MDT reports are measurements per UE. The defined MDT measurements for RRC_CONNECTED UEs are for instance RSRP, RSRQ, SINR, Power Headroom, PDCP SDU Data Volume, Average UE throughput, Packet Delay, Packet loss rate etc. Also logging of MDT measurements of RRC_IDLE or RRC_INACTIVE UEs are specified.

O-RAN commonly uses 3GPP measurement definitions, measurement procedures, and data models as defined by the respective 3GPP specifications and by reusing defined data models such as defined YANG models. Some examples are:

• O-RAN.WG1.O1-Interface.0-v04.00 o Procedures for Performance Data File Reporting and for Performance Data Streaming are specified in 3GPP TS 28.532 o The Information Object Classes (IOC) for collection of management data including PM, KPI, Trace and MDT are specified in 3GPP TS 28.622 (stage 2) and TS 28.623 (stage3).

o Trace and MDT Management Services are specified in 3GPP TS 32.421, TS 32.422 and TS 32.423. The functions and procedures of Immediate and Logged MDT are described in 3GPP TS 37.320.   
O-RAN.WG3.E2SM-KPM-v02.00 o Refers to measurement definitions provided in 3GPP TS 28.552 for NR and 3GPP TS 32.425 for LTE   
• O-RAN: O-RAN.WG5.MP.0-v02.00 o Performance data file reporting, data streaming and measurement job control as defined in ORAN.WG1.O1-Interface.0-v04.00 O RAN.WG5.O-CU-O1.0-v01.00 o Fault Supervision Management Services of O1 Interface contains Fault Supervision MnS as specified in 3GPP TS28.545 o AlarmList IOC and AlarmRecord data type refer to 3GPP TS28.622. The corresponding solution sets (stage 3) for YAML and YANG are specified in 3GPP TS 28.623 o O-CU-CP and O-CU-UP follow 3GPP SA5 data models and YANG modules as specified in 3GPP TS28.541

Similar principles are applied for configuration / provisioning management, where services and data models from 3GPP (e.g. as defined in 3GPP TS 28.532 or 3GPP TS 28.541) are commonly reused over O-RAN interfaces such as O1 and E2. Some examples are:

O-RAN.WG3.E2SM-RC-v01.01.00 o RAN Parameters for Control Action refer to RAN parameters defined in 3GPP specifications such as 3GPP TS 28.541, TS 38.331, TS 38.423 TS 38.463, TS 38.473 etc.   
O RAN.WG5.O-CU-O1.0-v01.00 o The SMO configuration of O-DU is based on 3GPP SA5 data models and YANG modules specified in 3GPP TS 28.541.   
O-RAN.WG5.MP.0-v02.00 o The SMO configuration of O-CU-CP and O-CU-UP is based on 3GPP SA5 data models and YANG modules specified in 3GPP TS 28.541.

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

2.1 Subject to the terms and conditions of this Agreement, O-RAN Alliance hereby grants to Adopter a nonexclusive, nontransferable, irrevocable, non-sublicensable, worldwide copyright license to obtain, use and modify O-RAN Specifications, but not to further distribute such O-RAN Specification in any modified or unmodified way, solely in furtherance of implementations of an O-RAN

Specification.

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

EXCEPT FOR BREACH OF CONFIDENTIALITY, ADOPTER’S BREACH OF SECTION 3, AND ADOPTER’S INDEMNIFICATION OBLIGATIONS, IN NO EVENT SHALL ANY PARTY BE LIABLE TO ANY OTHER PARTY OR THIRD PARTY FOR ANY INDIRECT, SPECIAL, INCIDENTAL, PUNITIVE OR CONSEQUENTIAL DAMAGES RESULTING FROM ITS PERFORMANCE OR NON-PERFORMANCE UNDER THIS AGREEMENT, IN EACH CASE WHETHER UNDER CONTRACT, TORT, WARRANTY, OR OTHERWISE, AND WHETHER OR NOT SUCH PARTY HAD ADVANCE NOTICE OF THE POSSIBILITY OF SUCH DAMAGES. O-RAN SPECIFICATIONS ARE PROVIDED “AS IS” WITH NO WARRANTIES OR CONDITIONS WHATSOEVER, WHETHER EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE. THE O-RAN ALLIANCE AND THE MEMBERS, CONTRIBUTORS OR ACADEMIC CONTRIBUTORS EXPRESSLY DISCLAIM ANY WARRANTY OR CONDITION OF MERCHANTABILITY, SECURITY, SATISFACTORY QUALITY, NONINFRINGEMENT, FITNESS FOR ANY PARTICULAR PURPOSE, ERROR-FREE OPERATION, OR ANY WARRANTY OR CONDITION FOR O-RAN SPECIFICATIONS.

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