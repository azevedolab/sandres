# SAnDReS 2.0
Statistical Analysis of Docking Results and Scoring Functions 2.0 (SAnDReS 2.0)
https://azevedolab.net/sandres.php
<P>&nbsp;</P>
<B>Message posted on October 10, 2021.</B>    

SAnDReS 2.0 is now available for download. Right now, only Linux version. This month (October/2021), I will upload the new Windows versions.  
Thank you very much for your patience.

<P>&nbsp;</P>
                                            Dr. Walter F. de Azevedo, Jr.
                                            
<P>&nbsp;</P>
<P>&nbsp;</P>

<H2>Overview</H2>

SAnDReS is a free and open-source (GNU General Public License) computational environment for the development of machine-learning models for prediction of ligand-binding affinity. SAnDReS is also a tool for statistical analysis of docking simulations and evaluation of the predictive performance of computational models developed to calculate binding affinity. SAnDReS is an acronym for Statistical Analysis of Docking Results and Scoring Functions. We have successfully employed SAnDReS 1.0 to study coagulation factor Xa (Xavier et al., 2016), cyclin-dependent kinases (de Ávila et al., 2017; Levin et al., 2018; Volkart et al., 2019), HIV-1 protease (Pintro & de Azevedo, 2017), estrogen receptor (Amaral et al., 2018), cannabinoid receptor 1 (Russo & de Azevedo, 2019), and 3-dehydroquinate dehydratase (de Ávila & de Azevedo, 2018). Also, we used SAnDReS 1.0 to develop a machine-learning model to predict Gibbs free energy of binding for protein-ligand complexes (Bitencourt-Ferreira & de Azevedo Jr., 2018). 

<H2>Installing SAnDReS 2.0 without Installers (Linux)</H2>  

You need to have Python 3 installed on your computer to run SAnDReS. In addition, you also need NumPy, Matplotlib, scikit-learn, and SciPy. It is also necessary to have AutoDock Vina installed in your computer (available here: http://vina.scripps.edu/download.html).

You can make the installation process easier by installing Anaconda. 

Step 1. Install Anaconda (available here: https://www.anaconda.com/download/)

Step 2. Install AutoDock Vina (available here:  http://vina.scripps.edu/download.html)

Step 3. Download SAnDReS 2.0 (available here:https://github.com/azevedolab/sandres/raw/master/sandres2.zip)

Step 4. Download database for ligands with IC50 data (available here: )

Step 5. Download database for ligands with Kd data (available here: )

Step 6. Download database for ligands with Ki data (available here: )

Step 7. Unzip the all zipped files (sandres2.zip, IC50.zip, Kd.zip, and Ki.zip) 

Step 8. Copy sandres directory to wherever you want it.

Step 9. Copy IC50, Kd, and Ki directories to sandres2/misc/data/pdbqt.

Step 10. Open a terminal and cd to sandres2 directory.

then type: python run_program.py

This launches GUI window for SAnDReS 2.0. That´s it, good SAnDReS session. By November/2021 we will have a tutorial page for additional information about how to run SAnDReS. 

<H2>Related Publications</H2>

-Amaral MEA, Nery LR, Leite CE, de Azevedo Junior WF, Campos MM. Pre-clinical effects of metformin and aspirin on the cell lines of different breast cancer subtypes. Invest New Drugs. 2018; 36(5): 782–796.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/29392539">PubMed</a>

-Bitencourt-Ferreira G, de Azevedo Jr. WF. Development of a machine-learning model to predict Gibbs free energy of binding for protein-ligand complexes. Biophys Chem. 2018; 240: 63–69.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/29906639">PubMed</a>

-Bitencourt-Ferreira G, de Azevedo WF Jr. SAnDReS: A Computational Tool for Docking.In: de Azevedo Jr. W. (eds) Docking Screens for Drug Discovery. Methods in Molecular Biology, 2019; 2053:51-65. Humana, New York, NY doi: 10.1007/978-1-4939-9752-7_4.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/31452098">PubMed</a>

-De Ávila MB, Xavier MM, Pintro VO, de Azevedo WF. Supervised machine learning techniques to predict binding affinity. A study for cyclin-dependent kinase 2.  Biochem Biophys Res Commun. 2017; 494: 305-310.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/29017921">PubMed</a>  
   
-De Ávila MB, de Azevedo WF Jr. Development of machine learning models to predict inhibition of 3-dehydroquinate dehydratase. Chem Biol Drug Des. 2018; 92: 1468–1474.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/29676519">PubMed</a>

-Heck GS, Pintro VO, Pereira RR, de Ávila MB, Levin NMB, de Azevedo WF. Supervised Machine Learning Methods Applied to Predict Ligand-Binding Affinity. Curr Med Chem. 2017; 24(23): 2459-2470.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/28641555">PubMed</a>

-Levin NMB, Pintro VO, Bitencourt-Ferreira G, Mattos BB, Silvério AC, de Azevedo Jr. WF. Development of CDK-targeted scoring functions for prediction of binding affinity. Biophys Chem. 2018; 235: 1–8.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/29407904">PubMed</a>

-Pintro VO, Azevedo WF. Optimized Virtual Screening Workflow. Towards Target-Based Polynomial Scoring Functions for HIV-1 Protease. Comb Chem High Throughput Screen. 2017; 20(9): 820-827.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/29165067">PubMed</a>
  
-Russo S, De Azevedo WF. Advances in the Understanding of the Cannabinoid Receptor 1 - Focusing on the Inverse Agonists Interactions. Curr Med Chem. 2019; 26(10): 1908–1919.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/29667549">PubMed</a>

-Volkart PA, Bitencourt-Ferreira G, Souto AA, de Azevedo WF. Cyclin-Dependent Kinase 2 in Cellular Senescence and Cancer. A Structural and Functional Review. Curr Drug Targets. 2019; 20(7): 716-726.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/30516105">PubMed</a>

-Xavier MM, Heck GS, de Avila MB, Levin NM, Pintro VO, Carvalho NL, Azevedo WF Jr. SAnDReS a Computational Tool for Statistical Analysis of Docking Results and Development of Scoring Functions. Comb Chem High Throughput Screen. 2016; 19(10): 801-812.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/27686428">PubMed</a>
