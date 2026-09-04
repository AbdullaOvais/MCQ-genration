# O-RAN Work Group 1 (Use Cases and Overall Architecture) Spectrum Aggregation for Multi-Vendor Deployments

Copyright $\circledcirc$ ���� by the O-RAN ALLIANCE e.V.

The copying or incorporation into any other work of part or all of the material available in this document in any form without the prior written permission of O-RAN ALLIANCE e.V. is prohibited, save that you may print or download extracts of the material of this document for your personal use, or copy the material of this document for the purpose of sending to individual third parties for their information provided that you acknowledge O-RAN ALLIANCE as the source of the material and that you inform the third party that these conditions apply to them and that they must comply with them.

O-RAN ALLIANCE e.V., Buschkauler Weg ��, ����� Alfter, Germany Register of Associations, Bonn VR �����, VAT ID DE���������

Contents   
Foreword 4   
Modal verbs terminology 4   
Executive summary 4   
1 Scope 5   
2 References 5   
2.1 Normative references 5   
2.2 Informative references 5   
3 Definition of terms, symbols and abbreviations 6   
3.1 Terms 6   
3.2 Symbols 6   
3.3 Abbreviations 6   
4 Objectives and requirements 7   
4.1 Current challenges for spectrum aggregation in multi-vendor RAN 7   
4.2 Objectives 7   
5 Scenarios and considerations 8   
5.1 Overview 8   
5.2 Deployment scenarios 9   
5.2.1 Co-located deployments 9   
5.2.2 Non-co-located deployments 10   
5.2.3 Transport assumptions 12   
5.3 Considerations for spectrum aggregation techniques12   
5.3.1 UE considerations from network perspective 12   
5.3.2 Spectrum considerations 13   
5.3.3 Synchronization considerations 16   
5.3.4 Network management considerations 16   
5.3.5 RAN intelligence considerations 17   
5.3.6 Considerations for solution evaluation 17   
6 Spectrum aggregation solutions 18   
6.1 Overview 18   
6.2 Solution 1: Intra O-DU Carrier Aggregation 19   
6.2.1 Solution description 19   
6.2.2 Mapping to deployment scenarios and other consideration 21   
6.2.3 Impact analysis on specifications 21   
6.2.4 Feasibility and gain/complexity analysis 21   
6.3 Solution 2: Inter O-DU Carrier Aggregation 22   
6.3.1 Solution description 22   
6.3.2 Mapping to deployment scenarios and other consideration 27   
6.3.3 Impact analysis on specifications 28   
6.3.4 Feasibility and gain/complexity analysis 28   
6.4 Solution 3: Dual Connectivity 30   
6.4.1 Solution description 30   
6.4.2 Mapping to deployment scenarios and other consideration 31   
6.4.3 Impact analysis on specifications 32   
6.4.4 Feasibility and gain/complexity analysis 32   
7 Conclusions and recommendations 32   
7.1 Summary of evaluation 32   
7.2 Impact on standardization 36   
7.3 Recommendations 36   
Annex A: Xhaul delay considerations 37   
Annex B: Examples of multi-vendor Inter O-DU interface 39   
B.1 DL CA using an Inter O-DU interface 39   
B.� High-level description of Inter O-DU interface (D�) 39   
Annex C: Spectrum aggregation solution decision tree analysis 42   
Annex: Change history/Change request (history) 44

# Foreword

This Technical Report (TR) has been produced by O-RAN Alliance.

# Modal verbs terminology

In the present document "shall", "shall not", "should", "should not", "may", "need not", "will", "will not", "can" and "cannot" are to be interpreted as described in clause 3.2 of the O-RAN Drafting Rules (Verbal forms for the expression of provisions).

"must" and "must not" are NOT allowed in O-RAN deliverables except when used in direct citation.

# Executive summary

Spectrum aggregation across different bands plays an essential role for enhancing user experience and efficient use of frequency resources. As MNOs get access to new NR spectrum, they usually desire to aggregate the capacity across the different bands. The present document aims to identify practical scenarios for spectrum aggregation across equipment from multiple network equipment vendors. The spectrum aggregation scenarios cover a variety of deployment cases. The present document considers scenarios where different O-RAN NFs can be co-located or non-co-located. Supplementary spectrum aggregation scenarios such as SUL, SDL deployment are also covered. Different considerations for spectrum combinations, UE requirements and solution evaluation criteria are also documented.

To address spectrum aggregation in multi-vendor RAN deployment scenarios, three solutions are described: Intra O-DU CA, Inter O-DU CA, and Dual Connectivity. The solutions are mapped to different deployment scenarios and analyzed based on the evaluation criteria. While the Intra O-DU CA and Dual Connectivity scenarios are covered in existing O-RAN and �GPP specifications, the present document also covers the requirements for supporting a newly proposed Inter O-DU CA solution along with a brief outline for the solution architecture.

# 1 Scope

The contents of the present document are subject to continuing work within O-RAN and may change following formal O-RAN approval. Should the O-RAN Alliance modify the contents of the present document, it will be re-released by O-RAN with an identifying change of version date and an increase in version number as follows:

version xx.yy.zz

where:

xx: the first digit-group is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc. (the initial approved document will have $\scriptstyle \mathbf { X } \mathbf { X } = 0 \displaystyle 1$ ). Always 2 digits with leading zero if needed.   
yy: the second digit-group is incremented when editorial only changes have been incorporated in the document. Always 2 digits with leading zero if needed.   
zz:the third digit-group included only in working versions of the document indicating incremental changes during the editing process. External versions never include the third digit-group. Always 2 digits with leading zero if needed.

The present document describes different deployment scenarios that can benefit from spectrum aggregation in a multi-vendor network deployment. Various solutions for spectrum aggregation are also studied.

# 2 References

# 2.1 Normative references

Not applicable.

# 2.2 Informative references

References are either specific (identified by date of publication and/or edition number or version number) or nonspecific. For specific references, only the cited version applies. For non-specific references, the latest version of the referenced document (including any amendments) applies.

NOTE: While any hyperlinks included in this clause were valid at the time of publication, ORAN cannot guarantee their long-term validity.

The following referenced documents are not necessary for the application of the present document, but they assist the user with regards to a particular subject area.

<table><tr><td>[i.1]</td><td>3GPP TR 21.905: &quot;Vocabulary for 3GPP Specifications&quot;.</td></tr><tr><td>[i.2]</td><td>O-RAN.WG9.XTRP-REQ-v01.00: &quot;Xhaul Transport Requirements&quot;.</td></tr><tr><td>[i.3]</td><td>3GPP TS 38.801 v 14.0.0, 03/2017: &quot;Study on new radio access technology: Radio access architecture and interfaces&#x27;&quot;.</td></tr><tr><td>[i.4]</td><td>3GPP TS 38.300: &quot;5G; NR; NR and NG-RAN Overall description; Stage-2&quot;.</td></tr><tr><td>[i.5]</td><td>3GPP TS 38.101-1: &quot; NR; User Equipment (UE) radio transmission and receptior Part 1: Range 1 Standalone&quot;.</td></tr><tr><td>[i.6]</td><td>3GPP TS 38.133: &quot;NR; Requirements for support of radio resource management&#x27;</td></tr><tr><td>[i.7]</td><td>https://www.ericsson.com/en/blog/2021/6/what-why-how-5g-carrier-aggregation</td></tr></table>

[i.8] https://www.nokia.com/networks/mobile-networks/carrier-aggregation/   
[i.9] 3GPP TS 38.331: "5G; NR; Radio Resource Control (RRC) Protocol specification".   
[i.10] 3GPP TS 38.420: "5G; NG-RAN; Xn general aspects and principles".   
[i.11] 3GPP TS 38.101-3: "NR; User Equipment (UE) radio transmission and reception; Part 3: Range 1 and Range 2 Interworking operation with other radios".   
[i.12] 3GPP TS 38.473; F1 application protocol.   
[i.13] 3GPP TS 38.423; Xn application protocol.   
[i.14] O-RAN ALLIANCE O-RAN.WG4.CUS.0: "Control, User and Synchronization Plane Specification".   
[i.15] O-RAN ALLIANCE O-RAN.WG4.MP.0: "Management Plane Specification".   
[i.16] O-RAN ALLIANCE O-RAN.WG1. Use-Cases-Detailed-Specification: "Use Cases Detailed Specification".   
[i.17] O-RAN.WG1.OAD, "O-RAN Architecture Description".

# 3 Definition of terms, symbols and abbreviations

# 3.1 Terms

For the purposes of the present document, the terms given in [i.1], O-RAN WG1.OAD [i.17] and the following apply:

carrier aggregation: aggregation of two or more NR or E-UTRA component carriers in order to support wider transmission bandwidths.

Primary O-DU: O-DU where PCell is hosted for a particular UE.

Secondary O-DU: O-DU where SCell is hosted for a particular UE.

# 3.2 Symbols

For the purposes of the present document, the symbols given in [i.1] and the following apply:

NRB Transmission bandwidth configuration, expressed in units of resource blocks (for E-UTRA)

# 3.3 Abbreviations

For the purposes of the present document, the abbreviations given in [i.1], O-RAN WG1.OAD [i. 17] and the following apply:

C&M Plane Control and Management Plane   
C-RAN Centralized RAN   
C-RNTI Cell Radio Network Temporary Identifier   
D-RAN Distributed RAN   
EMS Element Management System   
MCG Master Cell Group   
MNO Mobile Network Operator   
Near-RT RIC Near real time RAN Intelligent Controller

Non-RT RIC Non-real time RAN Intelligent Controller PCI Physicall Cell Identity SCG Secondary Cell Group SMO Service Management and Orchestration vRAN Virtualized RAN

# 4 Objectives and requirements

# 4.1 Current challenges for spectrum aggregation in multivendor RAN

Spectrum aggregation across different bands plays an essential role for user experience and efficient use of frequency resources. As MNOs get access to new NR spectrum, they usually desire to aggregate the capacity across the different bands to improve the user experience. The coverage areas of different frequency bands can be very different. There has been interest from several companies for spectrum aggregation over multi-vendor RAN deployment, where different bands may have different component suppliers. In addition to a greenfield multi-vendor RAN deployment, how spectrum can be aggregated when a new band with a new supplier(s) is introduced in an existing network is an area of potential interest.

# 4.2 Objectives

The present document captures the outcome of the WG1 spectrum aggregation study across multi-vendor RAN equipment. The objective of the study is to document various deployment scenarios for spectrum aggregation and then describe solutions that map to these deployment scenarios. The solution evaluation under various considerations defined in the present document is also part of the study.

The detailed objectives of this study item are:

Capture and document multi-vendor deployment scenarios to support spectrum aggregation in various RAN configurations such as

a. Centralized RAN,   
b. Distributed RAN,   
c. Virtualized RAN,   
d. Legacy RAN (i.e., already deployed).

Capture and document spectrum aggregation use cases:

e. Intra-band contiguous and non-contiguous in FR1/FR2, f. Inter-band within and across FR1/FR2,   
g. Duplexing schemes (FDD/TDD).

Capture the spectrum considerations and UE considerations for different spectrum aggregation techniques.

Identify and document the evaluation criteria for the different spectrum aggregation techniques such as:

h. Minimize complexity, e.g., required interface bandwidth and latency, i. Minimize impact to inter-operability testing and standardization effort, j. Increase performance and lower latency,   
k. Minimize impact on O-RAN architecture,   
l. Minimize UE impact,   
m. Aligns with 3GPP RAN design,   
n. Increase spectral efficiency of combined carriers,   
o. Increase coverage,   
p. Address security concerns with different solutions.

Identify the different solutions possible for spectrum aggregation:

q. Dual connectivity,   
r. Intra O-DU CA (Multi O-RU or Shared O-RU), s. Inter O-DU CA.

Identify the different interfaces used for supporting the spectrum aggregation techniques such as

t. Xn Interface (Dual connectivity),   
u. F1 Interface (Dual connectivity),   
v. LLS interface (Intra O-DU CA),   
w. D2 Interface (Proposed interface to support Inter O-DU CA). Evaluate and compare the solutions defined in 5) against the evaluation criteria mentioned in 4).   
Briefly cover the outline of the proposed Inter O-DU CA solution.

# 5 Scenarios and considerations

# 5.1 Overview

In its most general form, deployed RAN network functions in an MNO's network can be sourced from a single-vendor or multiple vendors. The connectivity between the RAN logical functions may need to consider ideal and non-ideal transport scenarios. RAN deployments can also be mixed involving a combination of D-RAN, C-RAN and vRAN deployments.

Figure 5.1-1 shows the reference deployment architecture used in the present document. In addition to being purpose-built or virtualized, gNB network functions can be procured from multiple vendors. Depending on deployment factors, O-DUs can be connected to the same or different OCU-CPs and O-CU-UPs.

![](images/374bb120905874f2a877bdd79b4709bd77eea6e802da11c0cadd2323e3bc4e8b.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.1- SEQ myfig \\* ARABIC \s 51: Multi-vendor equipment deployment architecture

5.2 Deployment scenarios

5.2.1 Co-located deployments

# 5.2.1.1 Overview

This clause considers the deployment scenarios where relevant O-RAN network functions for aggregation of frequencies are co-located. In this use case, O-RAN NFs from multiple vendors, supporting the same or different band/duplexing capability are co-located. O-RAN NFs can be supporting a split RAN architecture, or it can be a monolithic integrated gNB. By supporting spectrum aggregation across the O-RAN NFs that are co-located, user throughput, cell coverage etc. can be improved.

Use cases based on different combinations of O-RAN NFs are described in clause 5.2.1.2 and 5.2.1.3.

Addition of new O-RAN NFs co-located with existing intra/inter-band O-RAN NFs supporting same/different duplexing capability

The following use case covers the scenario where spectrum aggregation is needed between the colocated O-RAN NFs.

An MNO can have network function such as O-CU-CP, O-CU-UP, O-DU and O-RU with either TDD or FDD or both duplexing capabilities installed at a cell site. To increase the capacity of the site, MNO may need to install a new cell which could be operating in the same/different band. In one deployment scenario, depicted in Figure 5.2.1.2-1, MNO deploys a new O-RU, from a new vendor, to add a new frequency band to the existing infrastructure. The new O-RU can be connected to the existing O-DU through open fronthaul, as shown in Figure 5.2.1.2-1(b). In some instances, hardware or software realizing the existing O-DU may be limited by capacity and cannot host the new cell. One of the options available for the MNO is to enhance the capacity of existing hardware or software. Another possibility is to install a new hardware or software for capacity enhancements. The new hardware can be integrated with the existing hardware to realize the same logical O-DU (as in Figure 5.2.1.2-1(b)), or it can realize a new logical O-DU operating in parallel to the first ODU as shown in Figure 5.2.1.2-1(c).

![](images/cb9e63b36ef8821b968fa8061d7a1c7878fa7a6251b9d0003632ecdd2a551ee2.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.2.1.2-SEQ myfig $\nwarrow$ ARABIC \s 51: Adding new O-RU to support a new frequency band or carrier in a co-located deployment. (a) existing deployment. (b) addition of new O-RU. (c) addition of new O-RU and O-DU.

In some other deployment scenarios, deployed O-DU(s) may have limited capacity, may only support one duplexing method or can support a limited set of subcarrier spacing for real-time processing. The MNO may choose to deploy a new O-DU vendor to support a new O-RU, e.g., vendor c as shown in Figure 5.2.1.2-2. If the MNO chooses to install a new O-DU, it can be supporting the same or different duplexing capability or subcarrier spacing. If O-CU-CP and O-CUUP are capable to handle the newly installed O-DU, the new O-DU can be connected to same OCU-CP and O-CU-UP. Otherwise, a new O-CU-CP and O-CU-UP may also need to be installed. The MNO can choose the O-CU-CPs, O-CU-UPs, O-DUs or O-RUs from the same vendor or different vendors.

![](images/4b84c148a555930045f1619072c730e917d70805dfdbbbaf77786859ce55fa6d.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.2.1.2-SEQ myfig \\* ARABIC \s 52: Spectrum aggregation in co-located O-DU

5.2.1.3 Co-located intra/inter-band monolithic gNBs with same or different duplexing capability

This use case covers the deployment scenario where a monolithic gNB is installed at cell site. As shown in Figure 5.2.1.3-1, to increase the user capacity with spectrum aggregation, the MNO can install additional hardware and software either to upgrade the capacity of exiting gNB or to support a new gNB operating in parallel to the existing gNB. The newly installed gNB can operate in the same band or different band as the existing gNB. Both the gNBs may also support same or different duplexing capability. The new gNB can be monolithic or disaggregated. By supporting spectrum aggregation between these gNBs, improved coverage and throughput can be achieved.

![](images/734dcda7d21b5fc8422c2b3a4287d50614ff937748b492509dbf85648121ce9a.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.2.1.3-SEQ myfig $\nwarrow$ ARABIC \s 51: Spectrum aggregation in co-located gNBs

# 5.2.2 Non-co-located deployments

This clause covers the deployment scenarios where aggregated frequencies are served by equipments that are not co-located.

In this use case, gNBs are supporting split RAN architecture and it is distributed into different ORAN network functions. O-CU-CP/O-CU-UP might be residing at a centralized location while ODUs may be located at cell site or at a central location. Two cases are considered for this scenario:

Single O-CU-CP and O-CU-UP connected to multiple O-DUs located at cell site.

Each O-DU at cell site is connected to different O-CU-CP and O-CU-UP.

In one deployment scenario, the network MNO may deploy a new O-RU from a different vendor, to add a new frequency band, that is not co-located with other O-RUs serving the same geographic area. As an example, currently deployed O-RUs in a network may serve a large area and the MNO may decide to serve a high-demand zone within the larger coverage area by deploying additional spectrum. This is shown in Figure 5.2.2-1 below. By supporting spectrum aggregation across all the O-RUs serving the same area, user throughput, cell coverage etc. can be improved.

![](images/929025541b3e744f041efea73025903e29bfdbf45bcab05c8a8857a50825519d.jpg)

> **Image Summary:** (Summary not available)


# Figure 5.2.2-SEQ myfig \\* ARABIC \s 51: Deploying additional O-RU in a non-colocated manner. (a) existing deployment. (b) addition of non-co-located O-RU connected to existing O-DU. (c) addition of non-co-located O-RU and O-DU.

In some other deployment scenarios, as shown in Figure 5.2.2-2 below, deployed O-DU(s) at each cell site may have limited capacity, or may only support one duplexing method, or can support a limited set of subcarrier spacing. There may also be some other O-DUs which are not co-located with the existing O-DUs. But these O-DUs can be used together to overcome the limitations of existing cell site deployment. All the O-DUs can be supporting the same or different duplexing capability. The O-Dus can be connected to the same or different O-CU-CPs and O-CU-UPs. Also, these O-DUs may be provided by the same vendor or different vendors. The band configuration also can be the same or different for all these O-DUs. By supporting spectrum aggregation across different cells served by same or different non-co-located network functions (O-RU, O-DU, O-CUCP, O-CU-UP), end user throughput and cell coverage of different frequency bands can be improved.

![](images/df9443d29ea83193a16a2541e23a4163f64aa252d215493e8f8a52362e1be639.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.2.2-SEQ myfig \\* ARABIC \s 52: Spectrum aggregation in non-co-located RAN components

# 5.2.3 Transport assumptions

This clause covers the aspect of connectivity between the different equipment for supporting spectrum aggregation to consider ideal and non-ideal transport considerations. Network devices can be connected directly or through L2/L3 switches within the range that meets delay requirements. There are multiple connectivity classes for the transport connecting the NFs. Some guidelines are provided in O-RAN Xhaul Transport Requirements document [i.2]. For more information on the latency requirements, see Annex A. The outlined solutions in the present document account for ideal and non-ideal transport scenarios.

# 5.3 Considerations for spectrum aggregation techniques

# 5.3.1 UE considerations from network perspective

Spectrum aggregation between RAN NFs can be achieved by multiple techniques such as carrier aggregation or dual connectivity. The usage of these techniques in a network are also dependent on UE capability. Different spectrum aggregation techniques can impact the UE performance differently. Use case considerations for UE performance and capabilities are discussed below.

Spectrum aggregation to maximize component carrier (CC) combinations based on UE capability: Number of carrier frequency combinations play an important role in spectrum aggregation; larger the number, better the throughput and coverage. UEs supporting different 3GPP releases differ in CC combination capabilities. Number of available CCs for spectrum aggregation depends on a particular spectrum aggregation technique. For example, UEs, which are supporting earlier R15 or R16 3GPP releases, may be limited in supporting CC combinations for some of the spectrum aggregation techniques based on the band and bandwidth considerations for the component carriers. This needs to be considered for both SA and NSA UEs.

UE power consumption: While considering spectrum aggregation techniques, power consumption by UEs at various distances from the cell site needs to be considered. Spectrum aggregation techniques should minimize impact on UE power consumption.

# 5.3.2 Spectrum considerations

# 5.3.2.1 Overview

Most commercial RAN deployments involve multiple frequency bands. Spectrum aggregation across different bands should consider frequency band characteristics (coverage, supported SCS, duplexing).

The following clauses cover use cases, such as (i) intra-band contiguous and non-contiguous in FR1/FR2, (ii) inter-band within and across FR1/FR2, and (iii) considerations for DL-UL link balance in high-frequency bands and different duplexing schemes (FDD/TDD).

# 5.3.2.2 Duplexing (FDD/TDD)

Spectrum usage is regulated into FDD and TDD domains. While FDD uses separate frequencies for the uplink and the downlink, TDD uses a single frequency for both uplink and downlink.

Generally, the unpaired spectrum for TDD is allocated in higher frequencies than FDD. The lowband FDD, due to physical propagation characteristics, offers a wider coverage area than the higherfrequency TDD spectrum. Typically, the low-band FDD is limited in capacity. Mid-band TDD has a higher bandwidth and capacity compared to the low-band FDD. However, mid-band TDD uplink coverage is more limited than the low-band FDD. Spectrum aggregation across FDD and TDD carriers can improve TDD cell coverage and deliver higher throughput than a TDD-only solution.

Figure 5.3.2.2-1 illustrates a possible way to aggregate the low-band FDD carrier (primary cell) and mid-band TDD carrier (secondary cell). By using the low-band FDD as the primary cell (PCell), the coverage-limiting UL data and control channels of the mid-band TDD carrier can be moved to the low-band FDD. This increases the overall mid-band cell coverage, which means that now the mid-band spectrum can be accessed by more users in the network. By using the mid-band TDD as secondary cell (SCell), the downlink throughput can be significantly improved. This use case provides the unique capability of aggregating low-band FDD and mid-band TDD for higher peak rates and increased cell coverage.

![](images/dac86e303b5ab4db5e8064198076e3970a6d56ce75a07769a2165637dac3e206.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.3.2.2-SEQ myfig $\nwarrow$ ARABIC \s 51: Aggregate low-band FDD carrier (PCell) and mid-band TDD carrier (SCell)

5.3.2.3 Maximize the number of CCs being aggregated irrespective of inter or intraband

MNO can access multiple carriers across various bands enabled by 5G in low, mid, and high frequencies. National regulators often grant additional spectrum licenses to MNOs in a phased manner. As a result, MNOs can offer services in multiple frequency bands and add spectrum in a phased manner at later dates including low, mid and high-frequency bands. To increase bandwidth and bitrate aggregation, MNOs need to consider spectrum aggregation from same or different vendor’s equipment, involving low, mid, and high-band cells with considerations on availability, functionality, cost etc. This enables the use of downlink for all aggregated cells while ensuring connection stability through a common uplink on the lower frequency aggregated carriers. The MNOs primarily benefit from leveraging the cumulative spectrum bandwidth of these allocations from different vendors to achieve higher date rates for end users.

Figure 5.3.2.3-1 illustrates a scenario where three co-located and overlaid cells are provided by different vendor equipment; a low-band carrier, a mid-band carrier, and a high-band carrier. Maximizing the number of CCs being aggregated can be considered for both NSA and SA scenarios.

![](images/37c616c5cb8d4db59bdfc3853aa8a4c67a4416f82723eef0633e3fcdccad1e60.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.3.2.3-SEQ myfig $\nwarrow$ ARABIC \s 51: Aggregate multiple cells from different vendor equipment   
Spectrum aggregation between low band and mid/high band

This use case covers the need of spectrum aggregation between low and mid/high band. Let us consider that the MNO has O-DUs/O-RUs operating on low band allocated to the MNO, deployed in the cell site. Later, the regulatory body allocates a new mid/high band spectrum to the same MNO. By supporting aggregation between low and mid/high band cells, the MNO can achieve better coverage for mid/high band and can improve the throughput for UEs connected to low band cells. If existing O-DU with low band is restricted by capacity issue and hence cannot host new cells with mid/high band, a new O-DU may be required to be installed to utilize the newly allocated band. Existing cell may be supporting low band FDD capability while new cells may be supporting high or mid band with TDD duplexing capability. The introduction of new mid/high band cells can reduce the capacity demand of the low band cell as UEs in good coverage conditions can be served by the new cell as shown in Figure 5.3.2.4-1.

![](images/b34b8cd3032ed772c767fb8128383a55da76abc3fe3d4f880ec7e6b725c47885.jpg)

> **Image Summary:** (Summary not available)
  
Figure 5.3.2.4-SEQ 1: Example of spectrum aggregation between low and mid/high band

Intra-band spectrum aggregation (contiguous or non-contiguous)

This use case covers the need of spectrum aggregation between the intra band cells. MNO deploys cells with spectrum allocated from Band B. Later more spectrum enable deployments also where the above requirements for time synchronization cannot be achieved.

# 5.3.4 Network management considerations

Network management aspects (FCAPS) need to be considered when new spectrum (intra/inter band, contiguous/non-contiguous, FDD/TDD) is added. A few possible scenarios wherein, either a new O-RAN NF needs to be added or existing O-RAN NF continues to support the additional spectrum are listed in Table 5.3.4-1.

Table 5.3.4- SEQ mytab \\* ARABIC \s5 1: Network management scenarios   

<table><tr><td rowspan=1 colspan=1>Scenario#</td><td rowspan=1 colspan=1>O-RU</td><td rowspan=1 colspan=1>O-DU</td><td rowspan=1 colspan=1>O-CU-CP</td><td rowspan=1 colspan=1>O-CU-UP</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>New</td><td rowspan=1 colspan=1>Existing</td><td rowspan=1 colspan=1>Existing</td><td rowspan=1 colspan=1>Existing</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>New</td><td rowspan=1 colspan=1>New</td><td rowspan=1 colspan=1>Existing</td><td rowspan=1 colspan=1>Existing</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>New</td><td rowspan=1 colspan=1>New</td><td rowspan=1 colspan=1>New</td><td rowspan=1 colspan=1>New</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>Existing</td><td rowspan=1 colspan=1>New</td><td rowspan=1 colspan=1>Existing</td><td rowspan=1 colspan=1>Existing</td></tr></table>

As discussed in previous clauses, network functions (O-RU, O-DU, O-CU-CP, O-CU-UP) can be from one or more vendors with any combination of them. These network functions (NFs) can be managed by EMS/NMS/SMO from one or multiple vendors. Orchestration and automation aspects for multi-vendor scenarios need to be considered as well. This is not addressed in the present document.

# 5.3.5 RAN intelligence considerations

RAN intelligence aspects can be considered when new spectrum (intra/inter band, contiguous/noncontiguous, FDD/TDD) is added. Impacts on Near-RT RIC and Non-RT RIC due to the multivendor scenarios already listed in clause 5.3.4 can be considered. This is not addressed in the present document.

# 5.3.6 Considerations for solution evaluation

When evaluating different solutions and techniques for spectrum aggregation with multi-vendor deployments, the following criteria is proposed:

1. Minimize complexity: Solution complexity in terms of network deployment is an important evaluation criterion. The bandwidth and latency requirements on the underlying transport are to be considered. A multi-vendor interface is designed to be well-defined with clear functional split.

Minimize impact to inter-operability testing and standardization effort: Efforts needed in the standardization process and inter-operability testing are important criteria in the evaluation of the solutions. In addition, standardizing multiple solution options addressing the same problem is not desirable.

Increase performance and lower latency: The solution(s) can be evaluated for maximizing utilization of available system capacity (e.g., maximize average and 5th percentile user throughput) and lowering experienced latency to end users.

Minimize impact on O-RAN architecture: Impact on O-RAN architecture is considered in the evaluation of the solution. There is a benefit in reusing existing interfaces as well as minimizing the impacts to existing O-RAN functions.

Minimize UE impact: The proposed solution(s) cannot include any changes to the UE specifications or lead to changes to the Uu interface.

Aligns with 3GPP RAN design: All solutions are to conform to existing 3GPP specifications and cannot introduce any new requirements on 3GPP specifications.

Increase spectral efficiency of combined carriers: The spectrum aggregation solution(s) are expected to maximize spectral efficiency of combined component carriers. Performance under ideal and non-ideal transport can be assessed.

Increase coverage and capacity: The spectrum aggregation solution(s) are expected to account for DL and UL path imbalance of high frequency carriers and enable extending the reach of high frequency carrier to as many UEs as possible, e.g., by using UL of a low frequency carrier for UL data traffic while DL data traffic is carried over the higher frequency band, thus increasing coverage and capacity.

Address security concerns with different solutions: If new interface(s) are defined, the security and integrity of data transfer over the interface are to be protected as specified by O-RAN WG11. The impact of the security requirements on the equipment and the underlying transport needs to be assessed.

Minimize energy consumption: The preferred solution(s) is the one that minimizes energy consumption while maintaining the required performance (user throughput, enhanced coverage, etc.). All potential solutions can be evaluated for expected energy consumption and performance trade-offs.

Minimize exchange of scheduling-specific information over open interfaces: The preferred solution is the one that minimizes exchange of the scheduling-related information over open interfaces and thus helps encourage differentiation in particular scheduler implementations.

# 6 Spectrum aggregation solutions

# 6.1 Overview

There are multiple techniques available for multi-vendor spectrum aggregation in 3GPP and ORAN. These techniques cover different use cases. However, not all the use case defined in clause 5.2.1 are covered due to limitations on existing interfaces.

Following Spectrum Aggregation techniques are defined in 3GPP Rel-15 for NR [i.4]:

2. Carrier Aggregation (CA)

Dual Connectivity (DC)

There are multiple interfaces that can be used to achieve the spectrum aggregation across multivendor components using above techniques. These interfaces are defined in 3GPP and O-RAN, and an additional interface is newly proposed below to provide additional functionality for multi-vendor interoperability.

1. Xn Interface (existing):

1.a. Dual connectivity with aggregation at PDCP level, for supporting spectrum aggregation, can be achieved using Xn Interface

1.b. Data exchange between primary node and secondary node takes place at PDCP PDU level.

2. F1 Interface (existing):

1.c. If multiple O-DUs are connected to the same O-CU-CP/O-CU-UP, F1 interface can be used to provide spectrum aggregation via DC technique.

1.d. If an O-DU supports multiple cells, each O-DU node can support CA simultaneously with DC. All the CA links will be within a single vendor O-DU in this case.

3. Open Fronthaul Interface (existing):

1.e. CA between cells of different O-RUs connected to a single O-DU can be achieved using O-FH interface.

1.f.The O-RUs and the O-DU can be provided by same or different vendors.

4. Inter O-DU Interface (proposal):

1.g. CA across cells supported in different vendor O-DUs can be achieved by a potential new interface between O-DUs. 1.h. Each O-DU can be connected to different or same vendor O-RUs. The ODUs can be connected to different or same vendor O-CU-CP/O-CU-UP.

There are several additional aspects of spectrum aggregation that impact the performance and need to be considered. One such example is the increase in traffic load in O-DUs due to larger bandwidth available to UEs. This can result in an imbalance in the loading of O-DUs that are implementing spectrum aggregation. Therefore, mobility load balancing (MLB) techniques are an important consideration for effective usage of spectrum aggregation.

The MLB feature is defined in 3GPP TS38.300 specification [i.4]. MLB is achieved by exchanging resource information among gNBs periodically and initiating handover procedure to redirect UE session to other gNBs as shown in Figure 6.1-1.

![](images/880cbffd07ebc2f1ac1d6c3e16c167cad309ddeb1d48ade923fada84d4912144.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.1- SEQ Figure \\* ARABIC 1: Mobility Load balancing between gNBs.

6.2 Solution 1: Intra O-DU Carrier Aggregation

6.2.1 Solution description

6.2.1.1 Intra O-DU multi O-RU carrier aggregation

In carrier aggregation, spectrum aggregation is achieved at O-DU level. Each O-DU can support multiple cells possibly through multiple O-RUs. The cell where UE is attached is called the Primary

Cell (PCell) for that UE while other cells used for carrier aggregation are called Secondary Cells (SCells).

In DL CA, the primary O-DU receives data from O-CU-UP and schedules the data between the PCell and SCells to transmit to the UE. The UE maintains multiple downlink links as per the number of component carriers (CCs) configured to receive data from gNB. Data received from SCells as well as from PCell is aggregated at MAC level in the UE and forwarded to higher layer. There is a single instance of PDCP, RLC, and other higher layers in the UE, when carrier aggregation is activated.

In UL CA, SCells and PCell receive UL data (PUSCH) separately from the UE. Data is then aggregated in the PCell and forwarded to the O-CU-UP. The UCI (PUCCH) can be transmitted on the component carriers configured for UL.

Both SCells and PCell are processed in a single O-DU which is connected with multiple O-RUs using the Open Fronthaul interface. The Open Fronthaul (and F1) interface enables multiple vendor options for an MNO to decide for deployment considerations as shown in Figure 6.2.1-1. Figure 6.2.1-1 shows the intra O-DU DL CA scenario, where the PCell is configured on a carrier served by O-RU1 and DL only SCell(s) are served by O-RUn. In this scenario, PUCCH is carried by the PCell. The UE transmits the PUCCH for PCell PDSCH as well as for SCell PDSCHs on PCell resources. The PUCCH is received by PCell in O-DU. If PUCCH for SCell is present, it is shared with SCells. The O-DU coordinates the sharing of the PUCCH between the PCell and the SCells configured for the UE.

![](images/4aa25fc9609a42408db8bf930cfe679195d8179359d9a0318d8d2f0133956d9a.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.2.1-SEQ myfig $\nwarrow$ ARABIC \s 51: Intra O-DU, Multi O-RU DL CA without UL CA.

Intra O-DU CA is implemented within a single O-DU. MLB is taken care of by existing F1/X2/Xn interface by doing intra O-DU handover or inter O-DU handover to other O-DU.

6.2.1.2 Intra O-DU Shared O-RU carrier aggregation

Shared O-RU reference architecture is shown in Figure 6.2.1.2-1, where a shared O-RU can share its resources (e.g., carriers) with two O-DUs. The Shared O-RU framework can be used in scenarios when a new O-RU deployment is also accompanied by an additional O-DU. Spectrum aggregation across cells supported by an O-DU is then achieved by carrier aggregation.

# Single MNO scenario

![](images/23a79ac60e196474b52f3e3fbab30ac4c2f0c292a0128dc26fce70ed0a8678e3.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.2.1.2- SEQ myfig \s 5 \\* ARABIC 1: Shared O-RU reference diagram.

Figure 6.2.1.2-2 shows how shared O-RU can be used in a multi-vendor O-DU/O-RU deployment to enable carrier aggregation of newly deployed spectrum with already deployed carriers. In Figure 6.2.1.2-2 (a), $\mathrm { O - R U } _ { 1 }$ , supporting for example carrier 1, is connected to $\mathrm { O - D U } _ { 1 }$ . To support new spectrum, $\mathrm { O - R U _ { n } }$ is added to the network. A new $\mathrm { O - D U _ { n } }$ can be installed from a different vendor, for example to handle carrier(s) supported by $\mathrm { O } { - } \mathrm { R } \mathrm { U } _ { \mathrm { n } }$ if $\mathrm { O - D U } _ { 1 }$ is resource constrained. The new O$\mathrm { D U } _ { \mathrm { n } }$ can also be connected to the $\mathrm { O - R U } _ { 1 }$ . O- $\mathrm { R U } _ { 1 }$ is then configured as shared O-RU and its resources (carriers) are shared between $\mathrm { O - D U } _ { 1 }$ and $\mathrm { O - D U _ { n } }$ . The UEs connected to $\mathrm { O - D U _ { n } }$ can use CA for carriers supported by $\mathrm { O - R U } _ { \mathrm { n } }$ and the shared carrier(s) of $\mathrm { O - R U } _ { 1 }$ . Even though $\mathrm { O - D U _ { n } }$ is supported by a different vendor, CA is still achieved among the multiple component carriers within the single vendor $\mathrm { O } { - } \mathrm { D } \mathrm { U } _ { \mathrm { n } }$ . In Figure 6.2.1.2-2 (b), a UE connected to $\mathrm { O - D U } _ { 1 }$ cannot be configured for carrier aggregation with carriers(s) from $\mathrm { O - R U } _ { \mathrm { n } }$ . UEs connected to $\mathrm { O - D U } _ { 1 }$ can be configured for carrier aggregation for the carriers supported in $\mathrm { O - D U } _ { 1 }$ (i.e., carriers supported by $\mathrm { O - R U } _ { 1 }$ and carriers supported by other O-RUs, not shown in figure, which are connected to the $\mathrm { O - D U _ { 1 , } }$ ).

![](images/07c889a2f7cef7c4ccaedd33fbdb6382b6fac1bfa39cfc965428132e71a230ff.jpg)

> **Image Summary:** (Summary not available)


# Figure 6.2.1.2- SEQ myfig $\nwarrow$ ARABIC \s 52: Shared O-RU can be used in multiple ODU deployments to enable CA. (a) Initial deployment. (b) Bands supported by O-RU1 and $\mathbf { O } \mathbf { - } \mathsf { R } \mathbf { U } _ { \mathsf { n } }$ can use CA.

6.2.2 Mapping to deployment scenarios and other consideration

This solution can cover all the deployment scenarios mentioned in clause 5.2.1. Spectrum aggregation when adding the new O-RU to an existing O-DU can be done by intra O-DU carrier aggregation. When a new logical O-DU is also added to an existing deployment (see Figure 5.2.1.2-1(c)), then intra O-DU CA can be realized using the shared O-RU framework as described in clause 6.2.1.2.

For non-co-located deployment use cases of clause 5.2.2, this solution can cover all scenarios if the fronthaul connecting the O-RU and O-DU has latency within the latency classes of High25, High75 of Table A-1. The High100 and High200 latency classes can also be supported depending on implementation and performance trade-offs.

3GPP TS 38.101 specification [i.5] defines the various NR band combinations and carrier components that can be used in DC and CA technologies within each frequency range (FR1 or FR2). Table 6.2.2-1 captures the number of NR band combinations supported for various 3GPP releases.

Table 6.2.2- SEQ mytab $\nwarrow$ ARABIC \s 51: Band combinations supported across different 3GPP releases.   

<table><tr><td rowspan=2 colspan=1>3GPP Release</td><td rowspan=1 colspan=2>Intra Band</td><td rowspan=1 colspan=2>2-Band, InterBand</td><td rowspan=1 colspan=2>3-Band, InterBand</td><td rowspan=1 colspan=2>4-Band, InterBand</td><td rowspan=1 colspan=2>5-Band, InterBand</td><td rowspan=1 colspan=1>SUL</td></tr><tr><td rowspan=1 colspan=1>CA</td><td rowspan=1 colspan=1>DC</td><td rowspan=1 colspan=1>CA</td><td rowspan=1 colspan=1>DC</td><td rowspan=1 colspan=1>CA</td><td rowspan=1 colspan=1>DC</td><td rowspan=1 colspan=1>CA</td><td rowspan=1 colspan=1>DC</td><td rowspan=1 colspan=1>CA</td><td rowspan=1 colspan=1>DC</td><td rowspan=1 colspan=1>CA</td></tr><tr><td rowspan=1 colspan=1>Rel 15 (38.101-1v15.23.0)</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>8</td></tr><tr><td rowspan=1 colspan=1>Rel 16 (38.101-1v16.17.0)</td><td rowspan=1 colspan=1>11 (contig) +8(non contig)</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>82</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>15</td></tr><tr><td rowspan=1 colspan=1>Rel 17 (38.101-1v17.11.0)</td><td rowspan=1 colspan=1>17 (contig.) +13 (non contig)</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>181</td><td rowspan=1 colspan=1>120</td><td rowspan=1 colspan=1>182</td><td rowspan=1 colspan=1>29</td><td rowspan=1 colspan=1>75</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>25</td></tr><tr><td rowspan=1 colspan=1>Rel 18 (38.101-1V18.3.0)</td><td rowspan=1 colspan=1>17 (contig) +14(non contig)</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>226</td><td rowspan=1 colspan=1>200</td><td rowspan=1 colspan=1>272</td><td rowspan=1 colspan=1>117</td><td rowspan=1 colspan=1>102</td><td rowspan=1 colspan=1>29</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>32</td></tr></table>

As shown in Table 6.2.2-1, NR CA has more band combinations compared to NR DC. Release 15 and Release 16 specify NR DC for inter frequency ranges (between FR1 and FR2) but not for bands/frequencies within a given frequency range (FR1 or FR2). For NR spectrum aggregation, Release 15 or Release 16 UEs can use NR DC across FR1 and FR2 but within each frequency range, they can only use CA. Since the UE has to maintain at least two separate uplink connections for DC, the UE power consumption is typically lower in CA (e.g., for DL only CA) where a single UL carrier can be used for all the carriers.

# 6.2.3 Impact analysis on specifications

Carrier aggregation for NR is defined in 3GPP specification [i.4]. In Intra O-DU carrier aggregation, the scheduler is residing in the single vendor O-DU and the vendor can implement proprietry algorithms to coordinate DL and UL resources and manage data transfer between PCell and SCells. There is no impact on any specification, as both the cells are running in the same O-DU and O-FH is a well-defined interface in O-RAN for O-DU and O-RU interoperability. The shared O-RU approach described in clause 6.2.1.2 uses existing O-FH to connect the existing O-RU with the new O-DU (see Figure 6.2.1.2-2). No new interfaces are needed. However, enhancements to CUS-Plane and M-Plane specifications [i.14], [i.15] might be needed to enable an

O-RU to connect with two O-DUs and for the O-RU to share its resources (carriers) dynamically between the two O-DUs for single MNO use case with carrier sharing. This resource partitioning (static or dynamic) use case of sharing carriers is described in clause 4.20.1.2, clause 4.20.2.2 and clause 4.20.3.2 of the O-RAN Use Cases Detailed Specification [i.16].

# 6.2.4 Feasibility and gain/complexity analysis

Table 6.2.4-1 captures the solution evaluation for intra O-DU carrier aggregation covering both multi-O-RU and shared O-RU sub use cases.

Table 6.2.4- SEQ mytab \s 5 \\* ARABIC 1: Evaluation of intra-O-DU CA   

<table><tr><td rowspan=1 colspan=1>Solution Evaluation Criteria</td><td rowspan=1 colspan=1>Remarks</td></tr><tr><td rowspan=1 colspan=1>Minimize complexity</td><td rowspan=1 colspan=1>No impact. Open FH is already a standard solution in O-RAN.</td></tr><tr><td rowspan=1 colspan=1>Minimize impact to inter-operability testing andstandardization effort</td><td rowspan=1 colspan=1>No impact. Already a standardized interface.</td></tr><tr><td rowspan=1 colspan=1>Increase performance and lower latency</td><td rowspan=1 colspan=1>Since spectrum aggregation is done at O-DU level,latency will be very low. Performance of spectrumaggregation is also better compared to DC.</td></tr><tr><td rowspan=1 colspan=1>Minimize impact on O-RAN architecture</td><td rowspan=1 colspan=1>No impact. Open FH is a standardized interface.</td></tr><tr><td rowspan=1 colspan=1>Minimize UE impact</td><td rowspan=1 colspan=1>No impact.</td></tr><tr><td rowspan=1 colspan=1>Aligns with 3GPP RAN design</td><td rowspan=1 colspan=1>Aligned (Open FH is not defined in 3GPP but is alignedwith the 3GPP standards for CA).</td></tr><tr><td rowspan=1 colspan=1>Increase spectral efficiency of combined carriers</td><td rowspan=1 colspan=1>Maximum possible for spectrum aggregation techniquesand allowed combinations.</td></tr><tr><td rowspan=1 colspan=1>Increase coverage and capacity</td><td rowspan=1 colspan=1>Maximum for any spectrum aggregation technique [i.7].</td></tr><tr><td rowspan=1 colspan=1>Address security concerns with different solutions</td><td rowspan=1 colspan=1>No impact. Already a standardized solution.</td></tr><tr><td rowspan=1 colspan=1>[Minimize energy consumption</td><td rowspan=1 colspan=1>In DL CA, single PUCCH on PCell an carry the HARQfeedback or CQI etc for all the carriers while in DC, it isdifferent PUcCH for both the carriers. Hence, energyconsumption by UE will be lesser in CA compared to DC[i.8]</td></tr><tr><td rowspan=1 colspan=1>Minimize exchange of scheduling-specificinformation over open interfaces</td><td rowspan=1 colspan=1>No impact. Monitoring of the Open FH does not offerinformation about MAC implementation. Monitoring ofmultiple Open FH does not change this situation.</td></tr></table>

# 6.3 Solution 2: Inter O-DU Carrier Aggregation

# 6.3.1 Solution description

In case the product/server realizing the O-DU is not capable of being upgraded to support new band or capability either because of software or hardware limitations, carrier aggregation still can be achieved by installing a new O-DU with the required capability or to increase the capacity. Newly installed O-DU can be provided by the same vendor or different vendors. For supporting CA, ODUs can be connected with a newly proposed O-RAN interface inter-connecting the two MAC layers. Details on how this solution can potentially be implemented is described below.

For supporting carrier aggregation across multi-vendor O-DUs which are running in different servers, existing interfaces Xn (at O-CU-CP/O-CU-UP level), F1 (between O-CU-CP/O-CU-UP and O-DU) and Open Fronthaul (between O-DU and multiple O-RU) cannot be used as none of the interfaces support connection between O-DUs. Hence, support for newly proposed interface

between O-DUs is required in this scenario. If existing O-DUs already support the interface or it can be supported by a software upgrade, carrier aggregation across O-DUs can be achieved. By supporting an inter O-DU interface for CA, MNO can benefit from all the benefits of spectrum aggregation through CA.

A Service Management & Orchestrator (SMO) configures O-DUs using O1 interface as shown in Figure 6.3.1-1. O-DUs and O-RUs need to be compatible from Management plane perspective. This is the requirement for interworking of newly installed O-DU with existing/new O-RU irrespective of inter O-DU CA. The O1 interface can be updated to bring additional information such as IP address of the O-DUs, C-RNTIs, or PCIs, that is needed for the functioning of inter O-DU interface. The inter O-DU interface can also be configured automatically based on self-detection of O-DUs supporting cells that can be aggregated.

![](images/3e93b055026147915535a7767863e3b225e403a7eaca842e2ea413705b755b9c.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.3.1-EQ myfig \\* ARABIC \s 51: O-DU configuration by SMO (modified from [i. 17] to show the new interface).

In Figure 6.3.1-2 O-DU1 is hosting primary cells while O-DU2… O-DUn are hosting SCells. The dotted colored interface is indicating the DL CA across O-DUs using the new interface (D2-C and D2-U). O-DU1 receives data from O-CU-UP and schedules DL Data with O-DU2 … O-DUn to transmit on SCells. If there is no UL CA supported, PUCCH for SCells and PCells shall be received by O-DU1 as shown in Figure 6.3.1-2. O-DU1 shall extract the relevant part of the PUCCH information such as CQI, HARQ feedback and forward it to SCells.

NOTE: 'n' is not equal to maximum number of aggregated component carriers, rather the maximum number of inter-connected O-DUs for a given deployment that are used for CA across relevant SCells.

![](images/d8f21f0c795c4bac1feef96cd43d70a70e2ddf57c3d7b0458f9ce90d58d266a2.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.3.1-EQ myfig $\nwarrow$ ARABIC \s 52: Inter O-DU DL Carrier Aggregation without UL CA.

At power up, each O-DU connects to its peer O-DUs based on the configuration received via O� interface. SCells from peer O-DUs can be added only if link establishment between the O-DUs is successful. Once a O-DU triggers the link establishment request towards another O-DU, it may accept or reject the request. If the request is rejected, pair of O-DUs can not be used for CA. On SCell addition from OCU-CP, primary O-DU shares the SCell information such as CRNTI, Cell ID of SCell, QoS, RLC configuration etc with secondary O-DUs supporting SCells. After successful addition of SCells from other O-DUs, SCells can be activated for the UE. At SCell activation, the primary O-DU, informs secondary O-DUs about CA activation so that data exchange can take place.

If UL CA is also enabled along-with DL CA, UE maintains multiple links for uplink data. UE transmits data on the respective SCells, which can belong to different O-DUs, depending on the scheduling of PUSCH in SCells. Data is then transferred from secondary O-DUs to the primary ODU for aggregation. The primary O-DU sends the aggregated data to O-CU-UP. In this case UCI for both PCell and SCell can also come multiplexed with PUSCH data on SCell depending on scheduling in the SCell.

As showing in Figure 6.3.1-3 & Figure 6.3.1-4, UE is connected to PCell running in the O-DU1 while SCells are running in the O-DU2 and the O-DUn. UE transmits the data on the cell(s) as scheduled by the PDCCH. SCell(s) receive PUSCH containing user data and control (UCI) information. Secondary O-DU (O-DUn) then forwards the user data and UCI information (for example HARQ feebdback, CQI) for PCell and SCells to the Primary O-DU (O-DU1). Primary ODU shares the UCI information with other secondary O-DUs (O-DU2). In Figure 6.3.1-3, UCI bits are scheduled on the primary O-DU (O-DU1). O-DU1 receives UCI information related to SCells. O-DU1 then parses and sends UCI information to O-DU2 and O-DUn if present. In Figure 6.3.1-4,, UCI is scheduled on secondary O-DUn multiplexed with PUSCH. The O-DUn receives the UL data along with the UCI information and shares UL Data and UCI information with the O-DU1. The ODU1 forwards UCI information to secondary O-DU2, if present.

![](images/a70092bee38dcacdd559965f309d3b0eefea88732aa4391927f76bd3e116b753.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.3.1-EQ myfig \\* ARABIC \s 53: Inter O-DU UL CA, PUCCH on PCell.

![](images/ae92c514a8c3513b97e6d8d3201f7c9527ffe05342cd5209d4d61244f63b6db0.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.3.1- SEQ myfig $\nwarrow$ ARABIC \s 54: Inter O-DU UL CA, PUCCH on SCell.

In the case of intra $\mathsf { g N B }$ , inter O-DU CA, MLB can be achieved through F1 interface. For MLB, one or more UEs can be handed over to other O-DUs. Handover can be done to both co-located and non-co-located O-DUs. Inter O-DU handover using F1 interface is defined in 3GPP specifications. Additionally, the new interface between O-DUs, if defined, also can be used to share the resource status information between the O-DUs so that the PCell can avoid activating SCells on the O-DU facing loading condition as shown in Figure 6.3.1-5 below.

![](images/b8cd2c9fbf0849baefacde100d6090b10d56be8c41c264aead015996ba43ddc2.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.3.1- SEQ 5: Mobility load balancing with intra gNB, inter O-Dus CA.

In the case of inter gNB, inter O-DU CA, MLB can be achieved via F1 and X2/Xn interface [i.12] [i.13]. On a condition triggering MLB, one or more UEs can be handed over to other O-DU. On detecting any MLB condition, O-DU can inform O-CU-CP about the resource status on F1 interface. Based on these reports, O-CU-CP can trigger X2/Xn handover towards another O-DU. All these procedures are defined in 3GPP specifications. Additionally, if secondary O-DU is loaded, interface between O-DUs can be used to report the resource condition to primary O-DU as shown in Figure 6.3.1-6 below. Primary O-DU can avoid SCell activation towards this O-DU to avoid loading with exchanging resource information such as “Radio Resource Status” IE defined in 3GPP TS 38.423 [i.13].

![](images/b4bc7b59dba89f070748edcff701e36054fb861efa154e5cb2845f71702246c6.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.3.1- SEQ myfig $\nwarrow$ ARABIC \s 56: Mobility load balancing with inter gNB, inter O-DUs CA.

Figure 6.3.1-7 shows the protocol stack for inter O-DU CA between two O-DUs. The RLC layer hosted in primary O-DU is common for both primary and secondary O-DU for a particular UE while MAC layer can be present in both primary and secondary O-DUs for a UE.

![](images/476d9b3cafec1d5a3cac35c02504d860df9d819e09be5fbf4e4e1c09e1f154d6.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.3.1- SEQ 7: Protocol stack in O-DUs for Inter O-DU CA.

There are two parts of the inter O-DU interface referred to as D2 here. D2-C: Exchange of Control information. SCTP can be used as transport protocol.

D2-U: Exchange of user data and PUCCH information. GTP-U is used for transport mechanisms.

# D2 Control Interface (D2-C):

D2-C functionality involves the establishment and management of the link between O-DUs. SCTP is used as transport protocol. Link establishment between O-DUs takes place before any UE is connected to the O-DU. Main functionality of D2-C includes:

Establish connection between O-DUs.

Connection establishment can happen as soon as the O-DU comes up.

SCell Addition/Deletion/Modification. It can be triggered on SCell addition/deletion/ modification for a particular UE.

Figure 6.3.1-8 indicates the sample message sequence for D2 link establishment. Figure 6.3.1-8 indicates the procedure and not the actual interface name or parameters.

![](images/9abff95ca5c70bd28f81f2cfea22f7759a9297b08f8b2066b98f6033d28d47af.jpg)

> **Image Summary:** (Summary not available)


# D2 User Interface (D2-U):

The D2-U part of the interface is responsible for user data and PUCCH/UCI information exchange between O-DUs. GTP-U is used as the transport protocol for this interface. Main functionality of D2-U includes:

Data exchange between primary and secondary O-DU.

For DL-CA, primary O-DU receives data from O-CU-UP. The PDCCH is scheduled on both the O-DUs independently, similar to Intra O-DU CA case.

For DL CA, PUCCH resource allocation is done by primary O-DU. PUCCH related information (e.g. PUCCH Resource Indicator etc), required to be encoded in PDCCH, is shared between the primary and secondary O-DUs. UCI information on PUCCH for all the O-DUs is received by primary O-DU. It then forwards the information related to an SCell to the respective secondary O-DU.

For UL CA, both PCell on primary O-DU and SCells on secondary O-DUs receive data from UE. After MAC layer processing, secondary O-DU sends UE UL data to the primary O-DU, which then forwards it to the RLC layer residing in the primary O-DU.

Figure 6.3.1-9 indicates the information exchange on D2-U interface.

![](images/de5f40fe72c2d4293b68e46f15e11d87b2c50db3253878fb2aac15964745780f.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.3.1- SEQ myfig \\* ARABIC \s 58: D2 link establishment.   
Figure 6.3.1- SEQ 9: D2-U usage.

For D2 interface configuration and management, existing O1 interface that brings O-DU configuration from SMO can be enhanced. The D2 interface can be defined in a manner similar to the 3GPP defined F1 interface: a control part D2-C to carry control related information and a user plane part D2-U carrying user data as described above. Existing security mechanism defined in WG11 e.g., IPSec or any other mechanism can be utilized for protecting D2 interface as well. Brief outlines of control and data plane procedures expected from D2 interface are also described in Figure 6.3.1-8 and Figure 6.3.1-9. An example of protocol stack split for supporting inter O-DU CA is also captured in Annex B.

As the interface between the O-DUs is kept at MAC sub-layer for user plane, this tends to reduce the bandwidth requirement. Bandwidth requirements for inter O-DU CA can be the same or lower then F1 bandwidth requirement. The D2 interface can be designed to accommodate the latency class High75, High100 & High200 as described in Table A-1. The total round trip transmission and processing delay is bounded by $5 0 0 ~ \mu \mathrm { s }$ . Coverage of mid/high band carrier can be improved if inter O-DU CA is supported between O-DUs with PCell on low band FDD carrier and SCell on mid/high band TDD carrier. This coverage improvement, due to PUCCH for mid/high band SCells being received on low band PCell, can be similar to the intra O-DU CA solution.

# 6.3.2 Mapping to deployment scenarios and other consideration

This solution can cover all the deployment scenarios mentioned in clause 5.2.1.2 and clause 5.2.2 if the latency requirement between O-DUs is maintained as mentioned in clause 6.3.1. Spectrum aggregation across multiple multi-vendor O-DUs, either in co-located or non-co-located scenarios, can be achieved with this solution. Band combinations for NR CA are defined in Table 6.2.2-1 in clause 6.2.2. Energy consumption at UE is similar to intra O-DU CA solution as defined in clause 6.2.2, but at the network side, energy consumption can be higher due to message exchange between O-DUs. SDL bands are low bands that can be used to increase the coverage and throughput. If an SDL band is allocated to the MNO and it is supported in a different O-DU, it can be used for CA using this interface. On allocation of SUL band, if support of the SUL band cannot be extended in existing O-DU(s), another O-DU supporting SUL carrier can be used to provide the switching between the carriers for better coverage and performance. The proposed interface can be used to support this switching.

# 6.3.3 Impact analysis on specifications

There is no direct standardized inter O-DU interface defined in existing 3GPP or O-RAN specifications. For supporting inter O-DU carrier aggregation, a new inter O-DU interface needs to be defined. For supporting multi-vendor inter O-DU CA, the following Table 6.3.3-1 captures all the WGs that will be impacted for supporting multi-vendor inter O-DU CA. Impact on each WG is also mentioned in the table.

Table 6.3.3- SEQ mytab \\* ARABIC \s 51: WGs and specifications impact of standardization of inter O-DU interface.   

<table><tr><td colspan="1" rowspan="1">#</td><td colspan="1" rowspan="1">WGS</td><td colspan="1" rowspan="1">Specifications</td><td colspan="1" rowspan="1">Objective description</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">WG1(UCTG)</td><td colspan="1" rowspan="1">O-RAN.WG1.Use-Cases-Detailed-Specification</td><td colspan="1" rowspan="1">UCTG specification for existing use cases suchas Shared O-RU, traffic steering may needsome updates.</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">WG1(ATG)</td><td colspan="1" rowspan="1">O-RAN.WG1.O-RAN-Architecture-Description</td><td colspan="1" rowspan="1">Existing architecture document need to beupdated to capture the newly proposedinterface between O-DUs.</td></tr><tr><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">WG5</td><td colspan="1" rowspan="1">O-RAN Interoperability TestSpecification (IOT)New Specification:O-RAN.WG5.O-DU-D2 Interface-Specification</td><td colspan="1" rowspan="1">New interface needs to be defined between O-DUs for supporting inter O-DU CA.D2 Interface document will capture C Plane, Uplane details as well synchronizationrequirement.Heartbeat management can be taken care of byD2 Interface.</td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">WG10</td><td colspan="1" rowspan="1">WG10 O-RAN O1 InterfaceSpecificationWG10 O-RAN O1 Network ResourceModel SpecificationWG10 O-RAN O1 PerformanceMeasurements Specification</td><td colspan="1" rowspan="1">O1 interface and IM/DM documents can beupdated to support configuration of the O-DUswith peer O-DUs information for supportingmulti-vendor inter O-DU CA.Existing yang model can be enhanced to bringin information such as IP address of peer O-DUs, RNTIs, PCI. Faults KPI can also beupdated in O1 interface documents.</td></tr><tr><td>5</td><td>WG11</td><td>O-RAN.WG11.Security-Requirements- Specification O-RAN Security Test Specifications</td><td>Security documents can be reviewed and updated to support the new interface between O-DUs. It can be considered as interface security.</td></tr></table>

# 6.3.4 Feasibility and gain/complexity analysis

Table 6.3.4-1 evaluates the Inter O-DU solution against the solution evaluation criteria listed in clause 5.3.

Table 6.3.4- SEQ mytab \s $5 1 \star$ ARABIC 1: Evaluation of Inter O-DU CA.   

<table><tr><td rowspan=1 colspan=1>Solution Evaluation Criteria</td><td rowspan=1 colspan=1>Comment</td></tr><tr><td rowspan=1 colspan=1>Minimize complexity</td><td rowspan=1 colspan=1>A new interface connecting multiple O-DUs needs to be defined for supportingspectrum aggregation. This requires defining a management interface for taskssuch as to establish and maintain O-DU relations, and SCell associations. A newsignaling protocol, for example, to add/remove UE context, transfer user planedata and data flow management is also needed. Time synchronization across O-DUs also need to be specified. Clause 6.3.1 covers more details on complexity.The bandwidth and latency requirements and their impact on performance ofcarrier aggregation also needs to be evaluated in detail at WI phase. Clause6.3.1 covers more details on bandwidth and latency requirement.</td></tr><tr><td rowspan=1 colspan=1>Minimize impact to Inter-operabilitytesting and standardization effort</td><td rowspan=1 colspan=1>A new interface requires additional inter-operability testing requirements.Standardization effort requires involving multiple WGs in O-RAN such as WG1,WG5, WG10, and WG11. In addition, other groups such as WG3 or WG6 may beinvolved to enable additional functionality.</td></tr><tr><td rowspan=1 colspan=1>Increase performance and lowerlatency</td><td rowspan=1 colspan=1>Performance will not only depend on the details of the signaling protocoldesigned for the new interface but also on the scheduling and flow controlpolicies of the aggregated SCells residing in different Dus. Flow misconfigurationcan adversely impact overall cell throughput. The underlying transport latencyamongst different O-DUs can impact CA performance compared with single O-DU solution. In general, intra O-DU CA is expected to have superior performancein terms of user and cellthroughput when compared with an inter O-DU solution.Therefore, the choice of interface termination points and solution design shouldtake this into consideration while exploring the potential solutions.Faster activation of CA helps in achieving better performance in bursty UL traficscenarios, though transport delay between O-DUs may impact it.</td></tr><tr><td rowspan=1 colspan=1>Minimize impact on O-RANarchitecture</td><td rowspan=1 colspan=1>A new interface needs to be defined in the O-RAN architecture between O-DUsand requires modification to the existing architecture. The impact on O-RANdepends on the solutions proposed for this new interface and detailedspecification would be done in WI. Initial impact on O-RAN architecture iscovered in clause 6.3.1.O1 interface need to be enhanced to support D2 interface configuration andLCM.</td></tr><tr><td rowspan=1 colspan=2>Minimize LE impact                   No impact, The solution is assumed to be transparent for the Ue</td></tr></table>

Minimize UE impact

<table><tr><td rowspan=1 colspan=1>Aligns with 3GPP RAN design</td><td rowspan=1 colspan=1>From the UE perspective, the solution is transparent and thus aligned with 3GPPCA architecture. However, to support new interface, MNOs would need to updatetheir O-DU software and/or hardware, depending on their currentimplementations to enable multi-vendor carrier aggregation. To support inter O-DU CA in beyond 5G, some changes might be required depending on thearchitecture of beyond 5G that need to be considered at the new RAN design.</td></tr><tr><td rowspan=1 colspan=1>Increase spectral efficiency ofcombined carriers</td><td rowspan=1 colspan=1>CA provides best spectral efficiency among known spectrum aggregationtechniques. However, proper design choices need to be made for the protocolsplit and interface termination points as different flow management andscheduling policies of disjoint schedulers can adversely impact performance.</td></tr><tr><td rowspan=1 colspan=1>Increase coverage and capacity</td><td rowspan=1 colspan=1>CA provides best coverage and capacity among known spectrum aggregationtechniques [i.7]. However, proper design choices need to be made for theprotocol split and interface termination points in order to obtain best coverageand capacity for multi-vendor carrier aggregation.</td></tr><tr><td rowspan=1 colspan=1>Address security concerns withdifferent solutions</td><td rowspan=1 colspan=1>The new interface needs a security analysis to be performed by WG11 to ensurethe interface has appropriate protections for confidentiality, integrity, availability,authentication, and authorization. This process typically takes one release trainand may result in normative requirements specified for the subsequent releasetrain. Analysis and recommended normative security requirements need to beshared with all WGs that are stakeholders for the new interface specification</td></tr><tr><td rowspan=1 colspan=1>Minimize energy consumption</td><td rowspan=1 colspan=1>For DL CA, a single PUCCH on PCell carries the HARQ feedback/CQI etc for allthe aggregated carriers while in DC each cell group has a separate carrier forUCl and hence energy consumption by UE wil be lower in CA compared to DC [i.8]. From a network perspective, the interface between two or more separate O-DUs can slightly elevate overall network power consumption compared to asingle O-DU CA; moreover, in certain deployments like vRANs, the flexibility andscalability offered by a multi-vendor inter-DU interface for CA should also betaken into account in the overall considerations on network energy consumption.</td></tr><tr><td rowspan=1 colspan=1>Minimize exchange of scheduling-specific information over openinterfaces</td><td rowspan=1 colspan=1>The new interface should be defined in such a way that scheduling specificinformation exchange is minimized between the nodes. The informationexchange depends on the details of the interface. Depending on the design, thenew interface could resemble O-FH and offer limited opportunity for obtainingscheduling information of the primary O-DU. Alternatively, it may require flowcontrol between the schedulers of involved O-DUs; this flow control mechanismmay be more detailed as compared to the flow control used for DC due to higherperformance requirements of CA.The mechanism&#x27; wil have to be general enough to handle various schedulers, butthis generality may handicap efficiency of the solution (as compared to intra O-DU CA).Proposed solution for the D2 interface is described in clause 6.3.1 and clause7.3. It outlines the information that may be shared between O-DUs for transfer ofuser data and control information.</td></tr></table>

# 6.4 Solution 3: Dual Connectivity

# 6.4.1 Solution description

Dual Connectivity (DC) is a well defined spectrum aggregation technique specified by 3GPP in TS 38.331 [i.9] and TS 38.420 [i.10]. F1 and Xn interfaces, as described in 3GPP TS 38.473 [i.12] and 3GPP TS 38.423 [i.13], provide connection between relevant RAN nodes. There are master node (MN) and secondary node (SN) that together are used to provide connectivity to the UE using Xn or F1 interface as shown in Figure 6.4.1-1 which results in better throughput. Data exchange takes place at PDCP PDU level in DC. O-DU is transparent for data transfer in DC technique. For ODUs, there are two separate links established in downlink and uplink direction for a particular UE for data and control (UCI) information exchange. Figure 6.4.1-1 indicates the DC between multiple O-CU-CPs/O-CU-UPs. O-CU-CP/O-CU-UP/O-DU or O-RU can be supported by the same vendor or different vendors.

![](images/0688e022afc100bd67167a3e5b945c2f0a5fa9919484c69994b581d4f056d63f.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.4.1- SEQ 1: DC across multiple O-CU-CP/O-CU-UP.

In addition, DC can also be used when a UE is connected to two O-DUs, O-DU1/O-RU1 from vendor "a" serving as MCG and the O-DU2/O-RU2 from vendor "b" serving as SCG, connected to the same O-CU-CP/O-CU-UP as shown in Figure 6.4.1-2. O-DU and O-RU can also be provided by the same vendor or different vendors.

![](images/07c57beeaad6c8adeee0a0b91aad7c3ccba9ecd68c1005f238addea83c794108.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.4.1- SEQ 2: DC with single O-CU-CP/O-CU-UP with multiple O-DUs.

DC can also be combined with CA to further improve coverage and throughput. In this case, both or either of the nodes providing DC connectivity will have their own CC legs for carrier aggregation. CA can be Intra O-DU as shown for the MN node or Inter O-DU as shown for the SN node in Figure 6.4.1-3 below. Both the CA techniques are described in clause 6.2 and clause 6.3. The related requirement and details for the CA solutions are described in the respective clauses and DC will not impose any new requirement for supporting this scenario.

![](images/9f94a71ffa08847b8347f93b9773d952a2ffd3a7e45319a84154a80f636e3137.jpg)

> **Image Summary:** (Summary not available)
  
Figure 6.4.1- SEQ 3: Intra/Inter O-DU DL CA with DC.

In the case of spectrum aggregation by DC, MLB can be done via F1 and X2/Xn interface.

# 6.4.2 Mapping to deployment scenarios and other consideration

Deployment use cases defined in clause 5.2.1.2, 5.2.1.3 and 5.2.2 for inter band spectrum aggregation can be supported with DC solution. 3GPP has defined lesser number of band combinations as compared to CA. This limits the benefits of spectrum aggregation in case MNO wants to apply them to legacy UEs. As there are multiple uplink links for DC, energy consumption at UE will be higher compared to DL CA but multiple UL links can also improve UL throughput.

# 6.4.3 Impact analysis on specifications

Xn and F1 interfaces are well defined in 3GPP specifications. There is no impact on O-RAN working groups.

# 6.4.4 Feasibility and gain/complexity analysis

Table 6.4.4-1 evaluates the Dual Connectivity solution with respect to solution evaluation criteria.

Table 6.4.4- SEQ mytab \s $5 1 ^ { \star }$ ARABIC 1: Evaulation of Dual Connectivity.   

<table><tr><td colspan="1" rowspan="1">Solution evaluation criteria</td><td colspan="1" rowspan="1">Remarks</td></tr><tr><td colspan="1" rowspan="1">Minimize complexity</td><td colspan="1" rowspan="1">No Impact. This is already standardized solution.</td></tr><tr><td colspan="1" rowspan="1">Minimize impact to inter-operabilitytesting and standardization effort</td><td colspan="1" rowspan="1">No Impact. This is already standardized solution.</td></tr><tr><td colspan="1" rowspan="1">Increase performance and lower latency</td><td colspan="1" rowspan="1">Performance depends on the MN-SN flow control which is at higherlevel at the PDCP layer.</td></tr><tr><td colspan="1" rowspan="1">Minimize impact on O-RAN architecture</td><td colspan="1" rowspan="1">No Impact. DC is a standard solution.</td></tr><tr><td colspan="1" rowspan="1">Minimize UE impact</td><td colspan="1" rowspan="1">No Impact. DC is a standard solution.</td></tr><tr><td colspan="1" rowspan="1">Align with 3GPP RAN design</td><td colspan="1" rowspan="1">No Impact. DC is a standard solution.</td></tr><tr><td colspan="1" rowspan="1">Increase spectral efficiency of combinedcarriers</td><td colspan="1" rowspan="1">Lesser number of band combinations for DC specified by 3GPP ascompared to CA [i.11].</td></tr><tr><td colspan="1" rowspan="1">Increase coverage and capacity</td><td colspan="1" rowspan="1">Coverage in DC is lesser compared to CA [i.7]. In DC, for eachcarrier, there is a separate UL PUCCH link for feedback on DL data.This limits the coverage of each DC carrier compared to CA.</td></tr><tr><td colspan="1" rowspan="1">Address security concerns with differentsolutions</td><td colspan="1" rowspan="1">No impact. DC is a standard solution.</td></tr><tr><td colspan="1" rowspan="1">Minimize energy consumption</td><td colspan="1" rowspan="1">In DC each carrier will have its own UL link for receiving UL data aswell as PUCCH. Due to multiple UL links, power consumption at UE ishigher compared to CA.</td></tr><tr><td colspan="1" rowspan="1">Minimize exchange of scheduling-specific information over openinterfaces</td><td colspan="1" rowspan="1">No information exchange as data split is at higher level.</td></tr></table>

# 7 Conclusions and recommendations

# 7.1 Summary of evaluation

In the present document different deployment scenarios are described which are relevant to spectrum aggregation. For a multi-vendor network deployment, the following spectrum aggregation solutions are documented.

Intra O-DU CA

Inter O-DU CA

Dual connectivity

Figure 7.1-1 summarizes the key properties of the three spectrum aggregation solutions. Intra O-DU CA relies on Open FH interface (PHY layer) which enables multi vendor O-RUs. Inter O-DU CA using the D2 interface interconnects the two MAC layers in separate O-DUs. Dual connectivity makes use of PDCP aggregation at the O-CU-UP level. Depening on deployment scenario, one of the three solutions or a combination thereof can be used for spectrum aggregation. A decision tree to help arrive at a solution, considering different deployment scenarios, is described in Annex C.

![](images/0889fed92edcccf76d8fca4ac2d47e7086636fdd5a28032dd8380ed727c5f870.jpg)

> **Image Summary:** (Summary not available)
  
Intra O-DU CA

![](images/d89671e0dc41830b2d54b2cdca76ca6b64ba5762c2a0adc43a31dd63006ed029.jpg)

> **Image Summary:** (Summary not available)
  
Inter O-DU CA

![](images/298f26f486843be7e7ad6662e71bb60ecc8e6efcb4fe71d7fcc3df4be03d56ed.jpg)

> **Image Summary:** (Summary not available)
  
Dual connectivity

# Figure 7.1- SEQ myfig \s 5 \\* ARABIC 1: High-level depiction of the three solutions.

Table 7.1-1 covers the mapping of different deployment scenarios with the various solutions defined in clause 6.

Table 7.1- SEQ mytab $\nwarrow$ ARABIC \s 51: Mapping with deployment scenarios.   

<table><tr><td rowspan=1 colspan=1>Deployment Scenario</td><td rowspan=1 colspan=1>DC</td><td rowspan=1 colspan=1>Intra O-DU CA</td><td rowspan=1 colspan=1>Inter O-DU CA</td></tr><tr><td rowspan=1 colspan=1>Co-located deployments</td><td rowspan=1 colspan=1>Supported.</td><td rowspan=1 colspan=1>Supported.</td><td rowspan=1 colspan=1>Supported.</td></tr><tr><td rowspan=1 colspan=1>Non-co-locateddeployments</td><td rowspan=1 colspan=1>Supported and capable ofsupporting distributed O-DUsconnected via non-idealbackhaul.</td><td rowspan=1 colspan=1>Supported with idealfronthaul.Fronthaul latency up toHigh200 can be supported.</td><td rowspan=1 colspan=1>Supported with idealtransport link or with latencyup to High200.</td></tr></table>

Table 7.1-2 captures the details of each solution against the considerations mentioned in clause 5.3.

Table 7.1- SEQ mytab \s $5 1 \star$ ARABIC 2: Considerations table.   

<table><tr><td colspan="1" rowspan="1">Considerations foreach solution</td><td colspan="1" rowspan="1">DC</td><td colspan="1" rowspan="1">Intra O-DU CA</td><td colspan="1" rowspan="1">Inter O-DU CA</td></tr><tr><td colspan="1" rowspan="1">UE considerations:Maximize CCcombinations based onUE capability</td><td colspan="1" rowspan="1">In 3GPP Rel 15 specifications,DC is supported only betweenFR1 and FR2 bands. Also, NRDC support was added later inRel 15 specification. Hence UEssupporting 3GPP Rel 15 UEs</td><td colspan="1" rowspan="1">As majority of the 5G UEs aresupporting 3GPP Rel 15.These UEs are also notsupporting NR-DC as well,hence CA can improve CCcombinations for spectrum</td><td colspan="1" rowspan="1">Current majority of the 5GUEs are supporting 3GPP Rel15. These UEs are also notsupporting NR-DC as well,hence CA can improve CCcombinations for spectrum</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">without NR-DC capability will belimited in CC combinations. Mostof the UEs in the market areSupporting 3GPP Rel 15 andEN-DC.</td><td colspan="1" rowspan="1">aggregation. (NOTE)</td><td colspan="1" rowspan="1">aggregation. (NOTE)</td></tr><tr><td colspan="1" rowspan="1">UE consideration:Energy consumption</td><td colspan="1" rowspan="1">In DC, two separate paths for UL&amp; DL direction, one for SCG andMCG, are always present. Ifthere is no UL data, presence oftwo UL links wil increase thepower consumption at UE.</td><td colspan="1" rowspan="1">Iin DL CA, multiple UL linksacross different carriers arenot required. Hence, this canreduce power consumption atUE.If DL and UL CA both areactive, power consumption atUE can be higher due to thepresence of 2 UL links.</td><td colspan="1" rowspan="1">In DL CA, multiple UL linksacross different carriers arenot required. Hence, this canreduce power consumption atUE.If DL and UL CA both areactive, power consumption atUE can be higher due topresence of 2 UL links.</td></tr><tr><td colspan="1" rowspan="1">Spectrumconsideration:FDD+TDD</td><td colspan="1" rowspan="1">Coverage of mid band wilimprove around 67% [i.7]</td><td colspan="1" rowspan="1">Coverage of mid band willimprove around 85% [i.7]</td><td colspan="1" rowspan="1">Coverage of mid band canimprove and may be similar tointra O-DU CA scenario.</td></tr><tr><td colspan="1" rowspan="1">Spectrumconsideration:SUL/SDL</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">SUL/SDL carrier in Intra O-DUCA can be used for coverageand performanceimprovement</td><td colspan="1" rowspan="1">SUL/SDL carrier in inter O-DUcan be used for coverage andperformance improvement.</td></tr><tr><td colspan="1" rowspan="1">Synchronizationconsideration</td><td colspan="1" rowspan="1">Both synchronous andasynchronous deployments aresupported.</td><td colspan="1" rowspan="1">All the carriers reside in thesame O-DU, therefore noadditional synchronizationrequirements apply.</td><td colspan="1" rowspan="1">Tight synchronization(maximum clock timingdifference cannot be largerthan 33 μs) between O-DUs isneeded for supporting interO-DU CA.</td></tr><tr><td colspan="1" rowspan="1">Network managementconsiderations</td><td colspan="1" rowspan="1">No additional considerations.</td><td colspan="1" rowspan="1">No additional considerations.</td><td colspan="1" rowspan="1">SMO can manage theinterface between O-DUs. Theexisting O1 interface betweenSMO and O-DU can beextended to bring in theconfiguration for functioning ofthe new interface.</td></tr><tr><td colspan="4" rowspan="1">NOTE: This is dependent on the UE capability support for different 3GPP releases and NR-DC, which can change infuture.</td></tr></table>

As there are multiple techniques that can be used for spectrum aggregation, evaluation criteria defined in clause 5.3.6 is used to evaluate each solution. Based on the evaluation criteria, Table 7.1-3 compares the three solutions.

Table 7.1- SEQ mytab \s $5 1 \star$ ARABIC 3: Comparison of solution evaluation.   

<table><tr><td colspan="1" rowspan="1">Solution evaluationcriteria</td><td colspan="1" rowspan="1">Dual connectivity</td><td colspan="1" rowspan="1">Intra O-DU CA</td><td colspan="1" rowspan="1">Inter O-DU CA</td></tr><tr><td colspan="1" rowspan="1">Minimize complexity</td><td colspan="1" rowspan="1">No impact.</td><td colspan="1" rowspan="1">No impact.</td><td colspan="1" rowspan="1">A new interface needs to bedefined between the O-DUs.</td></tr><tr><td colspan="1" rowspan="1">Minimize impact tointer-operabilitytesting andstandardization effort</td><td colspan="1" rowspan="1">No impact.</td><td colspan="1" rowspan="1">No impact.</td><td colspan="1" rowspan="1">As a new interface will be defined,it will have impact on inter-operability.</td></tr><tr><td colspan="1" rowspan="1">Increase performanceand lower latency</td><td colspan="1" rowspan="1">For non-ideal backhaul, DC isthe preferred solution.Forcell center condition,performance can be similar tointer O-DU CA as UL PUCCHreception on both MCG andSCG inks may not show anydegradation.In cell edge scenarios, theSCG PUCCH link might beimpacted and hence can</td><td colspan="1" rowspan="1">More optimal usage ofresources than any otherspectrum aggregationtechnique and thus results inhigher end userperformance. Lower latencyis achieved as spectrumaggregation is done in asingle O-DU.</td><td colspan="1" rowspan="1">Despite O-DU beinginterconnected via transportsystem satisfying the transportrequirement, the achievedperformance could potentially beiower than intra O-Du CA. Thisperformance degradation is seenas HARQ feedback from PCell toSCell will be delayed by thelatency of the underlying transportconnecting the O-DUs.</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">cause retransmissions. Thiswill impact the throughput.Also in this case, if SCG linkdrops, activation of the SCGlink will take longer due toRRC signaling, which canfurther impact theperformance.</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Different scheduler running in O-DUs may have impact onperformance and iatency.</td></tr><tr><td colspan="1" rowspan="1">Minimize impact onO-RAN architecture</td><td colspan="1" rowspan="1">No impact.</td><td colspan="1" rowspan="1">No impact.</td><td colspan="1" rowspan="1">Impact on multiple WGs e.g.,WG1, WG5, WG10, WG11 etc.</td></tr><tr><td colspan="1" rowspan="1">Minimize UE impact</td><td colspan="1" rowspan="1">No impact.</td><td colspan="1" rowspan="1">No impact.</td><td colspan="1" rowspan="1">No impact.</td></tr><tr><td colspan="1" rowspan="1">Aligns with 3GPP RANdesign</td><td colspan="1" rowspan="1">Aligned.</td><td colspan="1" rowspan="1">Aligned.</td><td colspan="1" rowspan="1">Aligned.</td></tr><tr><td colspan="1" rowspan="1">Increase spectralefficiency of combinedcarriers</td><td colspan="1" rowspan="1">Spectral eficiency of DC canbe lower in certain scenario(e.g when UE is powerlimited) due to presence ofseparate PUCCH link forSCG cell.</td><td colspan="1" rowspan="1">Spectral efficiency of CA canbe higher due to thereception of SCell PUCCHon PCell,CA can be activated fasterthan DC which enablesoptimal usage of availableresources and thusimproving the overallspectral efficiency.</td><td colspan="1" rowspan="1">Spectral efficiency of CA can behigher due to the reception ofSCell PUCCH on PCell.CA can be activated faster thanDC which enables optimal usageof available resources.However, in Inter O-DU case,delayed HARQ feedback receptionat SCell due to transport delayacross O-DUs and the need forflow co-ordination among differentschedulers can impact overallspectral efficiency.</td></tr><tr><td colspan="1" rowspan="1">Increase coverage andcapacity (Number ofusers)</td><td colspan="1" rowspan="1">Maintenance of two separateUL links, lowers the coverageand capacity gains comparedto Intra and Inter O-DU CA.</td><td colspan="1" rowspan="1">CA enables maximumcoverage and capacityextension of mid/high 'bandsby moving UL control to low/mid band.</td><td colspan="1" rowspan="1">Coverage and capacity gain ofinter O-Du CA is expected to besimilar to intra O-DU CA.</td></tr><tr><td colspan="1" rowspan="1">Address securityconcerns withdifferent solutions</td><td colspan="1" rowspan="1">DC is a well-defined solutionin 3GPP and ORAN so nonew security requirements.</td><td colspan="1" rowspan="1">Intra O-DU CA is a well-defined solution in 3GPPand ORAN so no newsecurity requirements.</td><td colspan="1" rowspan="1">Inter O-DU CA is a new solutionhence security aspects need to bedefined for the new interface.Existing techniques that are usedon F1 can be considered.</td></tr><tr><td colspan="1" rowspan="1">Minimize exchange ofscheduling-specificinformation over openinterfaces</td><td colspan="1" rowspan="1">No exchange of schedulinginformation as data exchangeis at higher level</td><td colspan="1" rowspan="1">No exchange of schedulinginformation as CA is withinone O-DU</td><td colspan="1" rowspan="1">The new interface can bedesigned such that the input forscheduling the UE (data buff ersize etc) can be exchangedwithout disclosing the proprietaryscheduling algorithms and policies.</td></tr></table>

As shown in Table 7.1-1, Table 7.1-2 and Table 7.1-3, for supporting spectrum aggregation across non-co-located nodes with non-ideal backhaul, DC is a preferred option. DC can support spectrum aggregation in non-synchronized components. It is a well defined solution in 3GPP and O-RAN. DC is the preferred option for spectrum aggregation between FR1 and FR2.

Table 7.1-2 indicates that CA has more band combinations (also see Table 6.2.2-1) defined in 3GPP specifications. Spectrum aggregation across intra band carriers cannot be achieved by NR DC. CA provides better coverage and capacity compared to DC for mid/high band aggregated with low band cells. If multiple cells are supported in single O-DU, intra O-DU CA with/without Shared O-RU solution can be utilized for spectrum aggregation across different bands to achieve the best coverage and capacity results with least energy consumption.

In a deployment scenario, where different frequency bands are supported in different O-DUs or if an O-DU instance cannot host further cells due to its processing limits, inter O-DU CA (assuming legacy O-DU can be upgraded to support new interface) can be used for achieving the benefits of carrier aggregation. This will be beneficial for both co-located and non-co-located deployments. The new interface between O-DUs can be specified within the transport latency requirements as described in clasue 6.3.1. Coverage and capacity (in terms of users) improvement can be similar to the intra O-DU CA solution. The new interface between O-DUs can provide further flexibility to the MNOs to install RAN NFs as per their need and from different vendors.

# 7.2 Impact on standardization

For intra O-DU CA multi-O-RU scenario and dual connectivity, there is no impact on any WG as it is specified in 3GPP and O-RAN specifications. For intra O-DU CA with shared O-RU, WG4 enhancements may be needed to support dynamic carrier sharing.

There is no direct standardized inter O-DU interface defined in 3GPP or in O-RAN. For supporting inter O-DU carrier aggregation, a new inter O-DU interface, referred to as D2, needs to be defined. Table 6.3.3-1 details the WGs and the specifications impact of standardizing the proposed interface. Based on the prior Open FH experience, the development timeline of D2 interface is expected to be about 2 years from the start of the work item until the specification can be considered robust enough for the implementation.

# 7.3 Recommendations

The objective of this study is to evaluate spectrum aggregation techniques (carrier aggregation and dual connectivity) in both co-located and non-co-located scenarios utilizing specific assessment criteria. As shown in Table 7.1-1, Table 7.1-2 and Table 7.1-3, dual connectivity is appropriate when a user equipment (UE) connects to two separate cells concurrently, typically with different frequencies (e.g., FR� and FR�) over nonideal backhaul links.

In intra O-DU CA (shared O-RU or multi-O-RU) O-DUs, O-RUs can be provided by different vendors. Intra O-DU CA provides the best coverage and capacity improvement in spectrum aggregation. It can be used in co-located scenarios or deployments where single O-DU will be supporting multiple cells connected to different O-RUs. For non-co-located deployment use cases of clause �.�.�, this solution can cover all scenarios if the fronthaul connecting the O-RU and O-DU has latency within the latency classes of High��, High�� of Table A-1. The High��� and High��� latency classes can also be supported depending on implementation and performance trade-offs.

Multi-vendor dual connectivity and intra O-DU CA are well-defined in �GPP specifications and are supported by O-RAN.

For catering to deployment scenarios where different frequency bands are supported in different O-DUs or if an O-DU instance cannot host further cells due to its processing limits, multi-vendor inter O-DU CA can be used for achieving the benefits of spectrum aggregation. This will be beneficial for both co-located and non-co-located deployments. This assumes that legacy O-DUs are upgradable to support the new inter O-DU interface.

# Annex A: Xhaul delay considerations

This annex presents the Xhaul (Fronthaul, Midhaul and Backhaul) one way delay requirements captured in O-RAN.WG9.XTRP-REQ-v01.00 [i.2].   
Table A-1 lists one-way delay requirements for fronthaul.

Table A- SEQ mytab \\* ARABIC 1: Fronthaul one-way delay requirement table, adapted from clause 7.2 of [i.2].   

<table><tr><td rowspan=1 colspan=1>Latency class</td><td rowspan=1 colspan=1>Max. one-way frame delayperformance</td><td rowspan=1 colspan=1>Use case</td></tr><tr><td rowspan=1 colspan=1>High25</td><td rowspan=1 colspan=1>25 μs</td><td rowspan=1 colspan=1>Ultra-low latency performance</td></tr><tr><td rowspan=1 colspan=1>High75</td><td rowspan=1 colspan=1>75 μS</td><td rowspan=1 colspan=1>For full NR performance with fiber lengths in 10km range</td></tr><tr><td rowspan=1 colspan=1>High100</td><td rowspan=1 colspan=1>100 μS</td><td rowspan=1 colspan=1>For full NR performance with fiber lengths in 10km range</td></tr><tr><td rowspan=1 colspan=1>High200</td><td rowspan=1 colspan=1>200 μs</td><td rowspan=1 colspan=1>For standard NR performance with fiber lengths in 10km range</td></tr><tr><td rowspan=1 colspan=1>High500</td><td rowspan=1 colspan=1>500 μs</td><td rowspan=1 colspan=1>Large latency installations &gt; 30 km</td></tr><tr><td rowspan=1 colspan=1>Medium</td><td rowspan=1 colspan=1>1 ms</td><td rowspan=1 colspan=1>User Plane (slow) &amp; C&amp;M Plane (fast)</td></tr><tr><td rowspan=1 colspan=1>Low</td><td rowspan=1 colspan=1>100ms</td><td rowspan=1 colspan=1>C&amp;M Plane</td></tr></table>

Table A-2 lists the one-way end to end Midhaul transport delay requirements.

# Table A- SEQ mytab $\nwarrow$ ARABIC 2: One-way end to end Midhaul transport delay table, adapted from clause 8.2 of [i.2].

<table><tr><td rowspan=1 colspan=1>Capability</td><td rowspan=1 colspan=1>Requirements</td><td rowspan=1 colspan=1>Notes</td></tr><tr><td rowspan=1 colspan=1>End to end Midhaul transportdelay (one way)</td><td rowspan=1 colspan=1>&lt;1.5 ms-10 ms [i.3]</td><td rowspan=1 colspan=1>Delay constraints for midhaul are derived mainly from thetarget service&#x27;s latency requirements, rather than specificrequirements of the Midhaul&#x27; s user or control planes. Asservice delay targets become tighter it may become necessaryto:1) Place Midhaul and Backhaul mobile components in closeproximity to each other to reduce the delay impact of thetransport network.2) Combine mobile functions together so 3GPP interfaces runinternally within a &quot;Network Function&quot; or within a data center toremove the delay impact associated with the WAN transportnetwork. For example, combining O-RU, O-DU and O-CU-CP/UP or combining the O-DU and O-CU-CP/UP functionstogether.</td></tr></table>

Table A-3 lists the one-way end to end Backhaul transport delay requirements.

Table A- SEQ mytab $\nwarrow$ ARABIC3: One-way end to end Backhaul transport delay requirements, adapted from clause 9.3 of [i.2].   

<table><tr><td colspan="1" rowspan="1">Capability</td><td colspan="1" rowspan="1">Requirements</td><td colspan="1" rowspan="1">Notes</td></tr><tr><td colspan="1" rowspan="1">End to end Backhaul transportdelay (one way)</td><td colspan="1" rowspan="1">1 ms – 50 ms servicedependent.</td><td colspan="1" rowspan="1">Delay constraint for Backhaul are derived mainly from the targetservice's latency requirements, rather than specific requirementsof the Backhaul's user or control planes. Asservice delay targets become tighter it may become necessaryto:1) Place Midhaul and Backhaul mobile components in closeproximity to each other to reduce the delay impact of thetransport network. For example, O-DU, O-CU-CP/UP and UPF</td></tr><tr><td></td><td></td><td>in the same data center. 2) Combine mobile functions together so 3GPP interfaces run internally within a "Network Function" or within a data center to</td></tr><tr><td></td><td></td><td>remove the delay impact associated with the WAN transport network. For example, combining O-RU, O-DU and O-CU-CP/ UP or combining the O-DU and O-CU-CP/UP functions together.</td></tr></table>

# Annex B: Examples of multi-vendor Inter O-DU interface

# B.1 DL CA using an Inter O-DU interface

In Figure B.1-1, DL CA between two O-DUs for 2 UEs are shown. In Figure B.1-1, 2 O-DUs are present in the system connected to the same O-CU-UP/O-CU-CP. O-DU1 is configured as PCell for UE1 while O-DU2 is configured as SCell. For UE2, O-DU2 is serving as PCell while O-DU1 is hosting the SCell.

As both the UEs are using O-DUs for inter O-DU CA, for UE1, RLC is hosted in O-DU1. Data is received from O-CU-UP by O-DU1 and data is shared with O-DU2 if SCell is activated. PUCCH for UE1 is also received by O-DU1 and then shared with O-DU2. For UE2, the same functionality will be observed in O-DU2 (hosting RLC, RRC connection management and receiving data from O-CU-UP.

![](images/02b938d7c12524e340f8c236eb57e98041ca8f4112d7259de90f51fd71de67da.jpg)

> **Image Summary:** (Summary not available)
  
Figure B.1- SEQ myfig $\nwarrow$ ARABIC \s 51: Inter O-DU CA for multiple UEs hosting PCells in different O-DUs.

# B.� High-level description of Inter O-DU interface (D�)

For supporting inter O-DU CA, a new interface between the O-DUs need to be defined. Figure B.2-1 below proposes the solution for inter O-DU CA where D� identifies the new interface.

![](images/f760a9e4d5d205f5bcc91bb4263052cde030e03018950afa20e0052eecd89ad6.jpg)

> **Image Summary:** (Summary not available)
  
Figure B.2- SEQ myfig \s 5 \\* ARABIC 1: D2 interface between O-DUs.

Interface between O-DUs can be defined such that transport requirement as defined in clause � can be met. Coverage and capacity improvement can be similar to the intra O-DU CA. A new interface between O-DUs can provide further flexibility to the MNOs to install RAN NFs as per their need and from different vendors.

There are two parts of the D� interface:

D�-C: Exchange of control information. SCTP can be used as transport protocol. Link establishment between O-DUs, SCell establishment/release can be taken care by the control part of the D� interface.

D�-U: Exchange of data and PUCCH information will be taken care of by the D�-U interface. GTP-U is used for transport mechanisms.

![](images/25af0a858b86c5cdda85e01686ed95437e64d0c310484d02c9c964a4ca8095a2.jpg)

> **Image Summary:** (Summary not available)
  
Figure B.2-2 shows a proposed message flow for the D� interface.

![](images/f4e218b403747c0850f6b1004f8d6418cc1c571754dfe2f00cbb05e2f8f5cf90.jpg)

> **Image Summary:** (Summary not available)


Figure B.2- SEQ myfig \s 5 \\* ARABIC 2: Message flow for D2 interface.

# Annex C: Spectrum aggregation solution decision tree analysis

A decision tree is a useful tool to represent decision processes involving multiple decision points along different paths leading to a set of options. It helps in representing decision process in graphical form for better understanding of the decision process. Figure C-1 represents the decision tree for spectrum aggregation solutions. It takes into account key considerations that are discussed at length in the present document. They are listed along with their various possible values below for quick reference:

Existing-new spectrum FR

FR1-FR1 FR1-FR2 FR2-FR2   
Aggregated spectrum type Contiguous Non-contiguous   
Deployed O-DU capability Supports new spectrum. Does not support new spectrum.   
Added O-DU capability. Supports new spectrum only. Supports new $^ +$ existing spectrum.   
Transport capability Delay/BW requirements met. Delay/BW requirements not met.   
Existing deployment SA NSA   
New spectrum duplex mode SDL/SUL TDD/FDD   
Specified combination DC CA

The inter O-DU CA solution has an impact on O-RAN standardization.

![](images/7bdc6e0a7ec3889c26435132cbb991c1a58f03f2dacd398b8f1aa3ff05236e6f.jpg)

> **Image Summary:** (Summary not available)
  
Figure C- SEQ myfig \s $5 1 \star$ ARABIC 1: Decision tree for spectrum aggregation solutions.

The decision tree represents key considerations for an MNO to choose an optimal solution from different spectrum aggregation solutions. These considerations sufficiently address the scope of the study. However, there may be other considerations beyond those mentioned here depending on specific MNO deployment scenarios.

Annex: Change history/Change request (history)   

<table><tr><td rowspan=1 colspan=1>Date</td><td rowspan=1 colspan=1>Revision</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>2023-06-22</td><td rowspan=1 colspan=1>00.04</td><td rowspan=1 colspan=1>Initial version approved by UCTG of WG1.</td></tr><tr><td rowspan=1 colspan=1>2023-07-01</td><td rowspan=1 colspan=1>00.04.01</td><td rowspan=1 colspan=1>Incorporated agreed Multi-Vendor equipment deployment architecture section fromERI-2023.06.14-WG1-D-UCTG-Spectrum-aggregation-scenarios-v01.pptxIncorporated CRs: SAM-0001, NOK-001, NOK-002.</td></tr><tr><td rowspan=1 colspan=1>2023-08-16</td><td rowspan=1 colspan=1>00.04.02</td><td rowspan=1 colspan=1>Incorporated CRs: MAV-0002, MAV-0003.</td></tr><tr><td rowspan=1 colspan=1>2023-08-30</td><td rowspan=1 colspan=1>00.04.03</td><td rowspan=1 colspan=1>Incorporated CRs: MAV-0001.</td></tr><tr><td rowspan=1 colspan=1>2023-09-19</td><td rowspan=1 colspan=1>00.04.04</td><td rowspan=1 colspan=1>Incorporated CRs: ERI-0078, ERI-0081, NOK-0004.</td></tr><tr><td rowspan=1 colspan=1>2023-09-19</td><td rowspan=1 colspan=1>00.05</td><td rowspan=1 colspan=1>Accepted all changes with attendant editorial clean-up.</td></tr><tr><td rowspan=1 colspan=1>2023-09-29</td><td rowspan=1 colspan=1>00.05.01</td><td rowspan=1 colspan=1>Incorporated CRs: NOK-003, SAM-0002, DIS-0001.</td></tr><tr><td rowspan=1 colspan=1>2023-10-12</td><td rowspan=1 colspan=1>00.05.02</td><td rowspan=1 colspan=1>Incorporated CRs: ERI-0086.</td></tr><tr><td rowspan=1 colspan=1>2023-10-16</td><td rowspan=1 colspan=1>00.05.03</td><td rowspan=1 colspan=1>Incorporated CRs: NOK-0006, NOK-0007.</td></tr><tr><td rowspan=1 colspan=1>2023-10-17</td><td rowspan=1 colspan=1>00.05.04</td><td rowspan=1 colspan=1>Editorial changes as agreed in O-RAN UCTG meeting.</td></tr><tr><td rowspan=1 colspan=1>2023-10-17</td><td rowspan=1 colspan=1>1.00</td><td rowspan=1 colspan=1>O-RAN WG1 approval of the document</td></tr><tr><td rowspan=1 colspan=1>2023-12-07</td><td rowspan=1 colspan=1>1.00.01</td><td rowspan=1 colspan=1>Incorporated CRs: SAM-0003.</td></tr><tr><td rowspan=1 colspan=1>2024-01-17</td><td rowspan=1 colspan=1>1.00.02</td><td rowspan=1 colspan=1>Incorporated CRs: MAV-0041.</td></tr><tr><td rowspan=1 colspan=1>2024-01-31</td><td rowspan=1 colspan=1>1.00.03</td><td rowspan=1 colspan=1>Incorporated CRs: MAV-0042.</td></tr><tr><td rowspan=1 colspan=1>2024-02-01</td><td rowspan=1 colspan=1>1.00.04</td><td rowspan=1 colspan=1>Incorporated CRs: MAV-0043.</td></tr><tr><td rowspan=1 colspan=1>2024-02-15</td><td rowspan=1 colspan=1>1.00.05</td><td rowspan=1 colspan=1>Incorporated CRs: MAV-0044.</td></tr><tr><td rowspan=1 colspan=1>2024-02-20</td><td rowspan=1 colspan=1>1.00.06</td><td rowspan=1 colspan=1>Incorporated CRs: MAV-0046, KDD-0002.</td></tr><tr><td rowspan=1 colspan=1>2024-03-12</td><td rowspan=1 colspan=1>1.00.07</td><td rowspan=1 colspan=1>Incorporated CRs: ERI-0126</td></tr><tr><td rowspan=1 colspan=1>2024-03-28</td><td rowspan=1 colspan=1>1.00.08</td><td rowspan=1 colspan=1>Incorporated CRs: MAV-0045, MAV-0048. Included editorial updates.</td></tr><tr><td rowspan=1 colspan=1>2024-04-24</td><td rowspan=1 colspan=1>1.00.09</td><td rowspan=1 colspan=1>Incorporated CRs: MAV-0047, MAV-0050, MAV-0049.</td></tr><tr><td rowspan=1 colspan=1>2024-05-08</td><td rowspan=1 colspan=1>1.00.10</td><td rowspan=1 colspan=1>Incorporated CRs: ERI-013.</td></tr><tr><td rowspan=1 colspan=1>2024-05-09</td><td rowspan=1 colspan=1>1.00.11</td><td rowspan=1 colspan=1>Incorporated CRs: SAM-0005. Includes editorial updates.</td></tr><tr><td rowspan=1 colspan=1>2024-05-30</td><td rowspan=1 colspan=1>1.00.12</td><td rowspan=1 colspan=1>Incorporated CRs: NOK-0250, MAV-0052, MAV-0053, MAV-0054, SAM-0006, SAM-0007.Includes resolution of review comments 1-41 and editorial updates.</td></tr><tr><td rowspan=1 colspan=1>2024-06-09</td><td rowspan=1 colspan=1>1.00.13</td><td rowspan=1 colspan=1>Incorporated editorial updates including review comments 42-44.</td></tr><tr><td rowspan=1 colspan=1>2024-06-10</td><td rowspan=1 colspan=1>1.00.14</td><td rowspan=1 colspan=1>Editorial updates.</td></tr><tr><td rowspan=1 colspan=1>2024-06-12</td><td rowspan=1 colspan=1>1.00.15</td><td rowspan=1 colspan=1>Editorial updates and corrections.</td></tr><tr><td rowspan=1 colspan=1>2024-07-01</td><td rowspan=1 colspan=1>1.00.16</td><td rowspan=1 colspan=1>Editorial updates and corrections.</td></tr><tr><td rowspan=1 colspan=1>2024-07-10</td><td rowspan=1 colspan=1>1.00.17</td><td rowspan=1 colspan=1>Editorial updates and corrections.</td></tr><tr><td rowspan=1 colspan=1>2024-07-10</td><td rowspan=1 colspan=1>2.00</td><td rowspan=1 colspan=1>Document ready for WG1 approval.</td></tr><tr><td rowspan=1 colspan=1>2024-07-25</td><td rowspan=1 colspan=1>2.00.01</td><td rowspan=1 colspan=1>Editorial corrections implementing WG1 voting period feedback.</td></tr><tr><td rowspan=1 colspan=1>2024-07-26</td><td rowspan=1 colspan=1>2.00.02</td><td rowspan=1 colspan=1>Table format correction implementing WG1 voting period feedback.</td></tr><tr><td rowspan=1 colspan=1>2024-07-26</td><td rowspan=1 colspan=1>3.00</td><td rowspan=1 colspan=1>Document approved by WG1.</td></tr></table>