# sandres
Statistical Analysis of Docking Results and Scoring Functions (SAnDReS)

http://sandres.net/


Overview 
Make molecular docking reliable, fast, easy, free, and funny with SAnDReS. It is the easiest way to run dependable protein-ligand docking simulations. SAnDReS takes a different approach to docking; it focuses on the simulation of a system composed of an ensemble of crystallographic structures for which ligand binding affinity data is available. This experimental data is used to train a scoring function, specific for the biological system of interest (ensemble of structures with binding affinity data). In doing so, SAnDReS explores the scoring function space (Heck et al., 2017), selecting an adequate scoring function to predict binding affinity and to analyze docking results.  
SAnDReS is a free and open-source (GNU General Public License) computational environment for the development of machine-learning models for prediction of ligand-binding affinity. SAnDReS is also a tool for statistical analysis of docking simulations and evaluation of the predictive performance of computational models developed to calculate binding affinity. SAnDReS is an acronym for Statistical Analysis of Docking Results and Scoring Functions. We have successfully employed SAnDReS to study coagulation factor Xa (Xavier et al., 2016), cyclin-dependent kinases (de Ávila et al., 2017; Levin et al., 2018), HIV-1 protease (Pintro & de Azevedo, 2017), estrogen receptor (Amaral et al., 2018), cannabinoid receptor 1 (Russo & de Azevedo, 2018), and 3-dehydroquinate dehydratase (de Ávila & de Azevedo, 2018).     

Installing SAnDReS without Installers (Windows)  
Alternatively, you may follow the instructions below.

You need to have Python 3 installed on your computer to run SAnDReS. In addition, you also need NumPy, Matplotlib, scikit-learn, and SciPy.

You can make the installation process easier by installing Anaconda. 

Step 1. Install Anaconda (available here: https://www.anaconda.com/download/)

Step 2. Download SAnDReS 1.1.0 (available here:https://github.com/azevedolab/sandres/raw/master/sandres.zip )

Step 3. Unzip the zipped file (sandres.zip) 

Step 4. Copy sandres directory to c:\ .

Step 5. Open a command prompt window and type: cd c:\sandres

then type: python sandres1_GUI.py

This launches GUI window for SAnDReS. That´s it, good SAnDReS session. See tutorial page for additional information about how to run SAnDReS. You can also start SAnDReS clicking on the sandres.bat file. You may also create a shortcut for SAnDReS right clicking on the sandres.bat file.



Tutorials

http://sandres.net/Tutorials.php


Please cite the following paper Xavier et al. 2016 when using SAnDReS

Xavier MM, Heck GS, de Avila MB, Levin NM, Pintro VO, Carvalho NL, Azevedo WF Jr. SAnDReS a Computational Tool for Statistical Analysis of Docking Results and Development of Scoring Functions. Comb Chem High Throughput Screen. 2016; 19(10): 801-812. 


Related Publications

de Ávila MB, Xavier MM, Pintro VO, de Azevedo WF. Supervised machine learning techniques to predict binding affinity. A study for cyclin-dependent kinase 2.  Biochem Biophys Res Commun. 2017; 494: 305-310.  

de Ávila MB, de Azevedo WF Jr. Development of machine learning models to predict inhibition of 3-dehydroquinate dehydratase. Chem Biol Drug Des. 2018. doi: 10.1111/cbdd.13312     

Amaral MEA, Nery LR, Leite CE, de Azevedo Junior WF, Campos MM. Pre-clinical effects of metformin and aspirin on the cell lines of different breast cancer subtypes. Invest New Drugs. 2018. doi: 10.1007/s10637-018-0568-y  

Levin NMB, Pintro VO, Bitencourt-Ferreira G, Mattos BB, Silvério AC, de Azevedo Jr. WF. Development of CDK-targeted scoring functions for prediction of binding affinity. Biophys Chem. 2018; 235: 1–8. https://doi.org/10.1016/j.bpc.2018.01.004         

Pintro VO, Azevedo WF. Optimized Virtual Screening Workflow. Towards Target-Based Polynomial Scoring Functions for HIV-1 Protease. Comb Chem High Throughput Screen. 2017; 20(9): 820-827.              
    
Heck GS, Pintro VO, Pereira RR, de Ávila MB, Levin NMB, de Azevedo WF. Supervised Machine Learning Methods Applied to Predict Ligand-Binding Affinity. Curr Med Chem. 2017; 24(23): 2459-2470.     
  
Russo S, De Azevedo WF. Advances in the Understanding of the Cannabinoid Receptor 1 - Focusing on the Inverse Agonists Interactions. Curr Med Chem. 2018. doi: 10.2174/0929867325666180417165247     

Xavier MM, Heck GS, de Avila MB, Levin NM, Pintro VO, Carvalho NL, Azevedo WF Jr. SAnDReS a Computational Tool for Statistical Analysis of Docking Results and Development of Scoring Functions. Comb Chem High Throughput Screen. 2016; 19(10): 801-812. 

