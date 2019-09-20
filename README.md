# SAnDReS
Statistical Analysis of Docking Results and Scoring Functions (SAnDReS)
https://azevedolab.net/sandres.php
<P>&nbsp;</P>
<P>&nbsp;</P>
<H2>Citation</H2>
Please cite the following reference (Xavier et al., 2016) if SAnDReS program was useful.  

Xavier MM, Heck GS, de Avila MB, Levin NM, Pintro VO, Carvalho NL, Azevedo WF Jr. SAnDReS a Computational Tool for Statistical Analysis of Docking Results and Development of Scoring Functions. Comb Chem High Throughput Screen. 2016; 19(10): 801–812. <a href="https://www.ncbi.nlm.nih.gov/pubmed/27686428">PubMed</a>

<H2>Chapter of a Springer Nature Book About SAnDReS</H2> 
<P>&nbsp;</P>
<img src="https://media.springernature.com/w306/springer-static/cover-hires/book/978-1-4939-9752-7" align="left">
Bitencourt-Ferreira G, de Azevedo WF Jr. SAnDReS: A Computational Tool for Docking.In: de Azevedo Jr. W. (eds) Docking Screens for Drug Discovery. Methods in Molecular Biology, 2019; 2053:51-65. Humana, New York, NY doi: 10.1007/978-1-4939-9752-7_4.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/31452098">PubMed</a>&nbsp;&nbsp;&nbsp;<a href="https://link.springer.com/protocol/10.1007%2F978-1-4939-9752-7_4">Springer</a>

<P>&nbsp;</P>
<P>&nbsp;</P>
<P>&nbsp;</P>
<P>&nbsp;</P>
<P>&nbsp;</P>
<P>&nbsp;</P>
<P>&nbsp;</P>
<P>&nbsp;</P>

<H2>Overview</H2>

Make molecular docking reliable, fast, easy, free, and funny with SAnDReS. It is the easiest way to run dependable protein-ligand docking simulations. SAnDReS takes a different approach to docking; it focuses on the simulation of a system composed of an ensemble of crystallographic structures for which ligand binding affinity data is available. This experimental data is used to train a scoring function, specific for the biological system of interest (ensemble of structures with binding affinity data). In doing so, SAnDReS explores the scoring function space (Heck et al., 2017), selecting an adequate scoring function to predict binding affinity and to analyze docking results.  
SAnDReS is a free and open-source (GNU General Public License) computational environment for the development of machine-learning models for prediction of ligand-binding affinity. SAnDReS is also a tool for statistical analysis of docking simulations and evaluation of the predictive performance of computational models developed to calculate binding affinity. SAnDReS is an acronym for Statistical Analysis of Docking Results and Scoring Functions. We have successfully employed SAnDReS to study coagulation factor Xa (Xavier et al., 2016), cyclin-dependent kinases (de Ávila et al., 2017; Levin et al., 2018; Volkart et al., 2019), HIV-1 protease (Pintro & de Azevedo, 2017), estrogen receptor (Amaral et al., 2018), cannabinoid receptor 1 (Russo & de Azevedo, 2019), and 3-dehydroquinate dehydratase (de Ávila & de Azevedo, 2018). Also, we used SAnDReS to develop a machine-learning model to predict Gibbs free energy of binding for protein-ligand complexes (Bitencourt-Ferreira & de Azevedo Jr., 2018).   

<H2>Installing SAnDReS without Installers (Windows)</H2>  

You need to have Python 3 installed on your computer to run SAnDReS. In addition, you also need NumPy, Matplotlib, scikit-learn, and SciPy.

You can make the installation process easier by installing Anaconda. 

Step 1. Install Anaconda 32 bits (available here: https://www.anaconda.com/download/)

Step 2. Download SAnDReS 1.1.0 (available here:https://github.com/azevedolab/sandres/raw/master/sandres.zip )

Step 3. Unzip the zipped file (sandres.zip) 

Step 4. Copy sandres directory to c:\ .

Step 5. Open a command prompt window and type: cd c:\sandres

then type: python sandres1_GUI.py

This launches GUI window for SAnDReS. That´s it, good SAnDReS session. See tutorial page for additional information about how to run SAnDReS. You can also start SAnDReS clicking on the sandres.bat file. You may also create a shortcut for SAnDReS right clicking on the sandres.bat file.


<H3>DeltaG Dataset</H3>

Here you find a zip file (https://github.com/azevedolab/sandres/blob/master/Bitencourt-Ferreira_de_Azevedo_Jr_DeltaG_2018.zip) with all necessary files to generate a machine-learning model to predict Gibbs free energy of binding for protein-ligand complexes as described by Bitencourt-Ferreira & de Azevedo Jr., 2018.


<H3>HRIC<sub>50</sub> Dataset</H3>

Here you find a zip file (https://github.com/azevedolab/sandres/blob/master/de_Avila_et_al_HRIC50_Biochem_Biophys_Res_Commun_2017_494_1-2_305_310.zip) with all necessary files to generate a machine-learning model to predict the IC50 as described by de Ávila et al., 2017.


<H3>CDK IC<sub>50</sub> Dataset</H3>

Here you find a zip file (https://github.com/azevedolab/sandres/blob/master/Levin_et_al_CDK_IC50_Biophys_Chem_2018_2351_8.zip) with all necessary files to generate a machine-learning model to predict the IC50 for CDK as described by Levin et al., 2018.


<H3>CDK K<sub>i</sub> Dataset</H3>

Here you find a zip file (https://github.com/azevedolab/sandres/blob/master/Azevedo_2018_CDK_Ki.zip) with all necessary files to generate a machine-learning model to predict the inhibition constant (Ki) for CDK.


<H3>HIV-1 Protease Dataset</H3>

Here you find a zip file (https://github.com/azevedolab/sandres/blob/master/Pintro_Azevedo_HIV1_PR_Comb_Chem_High_Throughput_Screen_2017.zip) with all necessary files to generate a machine-learning model to predict the inhibition constant (Ki) for protease-ligand complexes as described by Pintro & de Azevedo Jr., 2017.

<H3>Factor Xa Dataset</H3>

Here you find a zip file (https://github.com/azevedolab/sandres/blob/master/Xavier_et_al_Xa_Comb_Chem_High_Throughput_Screen_2016_19_10_801_812.zip) with all necessary files to generate a machine-learning model to predict the inhibition constant (Ki) for coagulation factor Xa as described by Xavier et al., 2016.



<H2>Tutorials</H2>

https://azevedolab.net/tutorials-for-sandres.php


Please cite the following paper Xavier et al. 2016 when using SAnDReS

Xavier MM, Heck GS, de Avila MB, Levin NM, Pintro VO, Carvalho NL, Azevedo WF Jr. SAnDReS a Computational Tool for Statistical Analysis of Docking Results and Development of Scoring Functions. Comb Chem High Throughput Screen. 2016; 19(10): 801-812. 


<H2>Related Publications</H2>

-Amaral MEA, Nery LR, Leite CE, de Azevedo Junior WF, Campos MM. Pre-clinical effects of metformin and aspirin on the cell lines of different breast cancer subtypes. Invest New Drugs. 2018; 36(5): 782–796.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/29392539">PubMed</a>

-Bitencourt-Ferreira G, de Azevedo Jr. WF. Development of a machine-learning model to predict Gibbs free energy of binding for protein-ligand complexes. Biophys Chem. 2018; 240: 63–69.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/29906639">PubMed</a>

-Bitencourt-Ferreira G, de Azevedo WF Jr. SAnDReS: A Computational Tool for Docking.In: de Azevedo Jr. W. (eds) Docking Screens for Drug Discovery. Methods in Molecular Biology, 2019; 2053:51-65. Humana, New York, NY doi: 10.1007/978-1-4939-9752-7_4.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/31452098">PubMed</a>

-de Ávila MB, Xavier MM, Pintro VO, de Azevedo WF. Supervised machine learning techniques to predict binding affinity. A study for cyclin-dependent kinase 2.  Biochem Biophys Res Commun. 2017; 494: 305-310.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/29017921">PubMed</a>  
   
-de Ávila MB, de Azevedo WF Jr. Development of machine learning models to predict inhibition of 3-dehydroquinate dehydratase. Chem Biol Drug Des. 2018; 92: 1468–1474.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/29676519">PubMed</a>

-Heck GS, Pintro VO, Pereira RR, de Ávila MB, Levin NMB, de Azevedo WF. Supervised Machine Learning Methods Applied to Predict Ligand-Binding Affinity. Curr Med Chem. 2017; 24(23): 2459-2470.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/28641555">PubMed</a>

-Levin NMB, Pintro VO, Bitencourt-Ferreira G, Mattos BB, Silvério AC, de Azevedo Jr. WF. Development of CDK-targeted scoring functions for prediction of binding affinity. Biophys Chem. 2018; 235: 1–8.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/29407904">PubMed</a>

-Pintro VO, Azevedo WF. Optimized Virtual Screening Workflow. Towards Target-Based Polynomial Scoring Functions for HIV-1 Protease. Comb Chem High Throughput Screen. 2017; 20(9): 820-827.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/29165067">PubMed</a>
  
-Russo S, De Azevedo WF. Advances in the Understanding of the Cannabinoid Receptor 1 - Focusing on the Inverse Agonists Interactions. Curr Med Chem. 2019; 26(10): 1908–1919.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/29667549">PubMed</a>

-Volkart PA, Bitencourt-Ferreira G, Souto AA, de Azevedo WF. Cyclin-Dependent Kinase 2 in Cellular Senescence and Cancer. A Structural and Functional Review. Curr Drug Targets. 2019; 20(7): 716–726.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/30516105">PubMed</a>

-Xavier MM, Heck GS, de Avila MB, Levin NM, Pintro VO, Carvalho NL, Azevedo WF Jr. SAnDReS a Computational Tool for Statistical Analysis of Docking Results and Development of Scoring Functions. Comb Chem High Throughput Screen. 2016; 19(10): 801-812.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/27686428">PubMed</a>

