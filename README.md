# sandres
Statistical Analysis of Docking Results and Scoring Functions (SAnDReS)

http://sandres.net/

Overview

Make molecular docking reliable, fast, easy, free, and funny with SAnDReS. It is the easiest way to run dependable protein-ligand docking simulations. SAnDReS takes a different approach to docking; it focuses on the simulation of a system composed of an ensemble of crystallographic structures for which ligand binding affinity data is available. This experimental data is used to train a scoring function, specific for the biological system of interest (ensemble of structures with binding affinity data). In doing so, SAnDReS explores the scoring function space, selecting an adequate scoring function to predict binding affinity and to analyze docking results.

To summarize, we can say that SAnDReS is a free and open-source (GNU General Public License) computational environment for the development of machine-learning models for prediction of ligand-binding affinity. SAnDReS is also a tool for statistical analysis of docking simulations and evaluation of the predictive performance of computational models developed to calculate binding affinity. SAnDReS is an acronym for Statistical Analysis of Docking Results and Scoring Functions. We have successfully employed SAnDReS to study coagulation factor Xa (Xavier et al., 2016), cyclin-dependent kinases (de Ávila et al., 2017; Levin et al., 2018), HIV-1 protease (Pintro & de Azevedo, 2017), estrogen receptor (Amaral et al., 2018), cannabinoid receptor 1 (Russo & de Azevedo, 2018), and 3-dehydroquinate dehydratase (de Ávila & de Azevedo, 2018).     


Installing SAnDReS (Windows)  

You need to have Python 3 installed on your computer to run SAnDReS. In addition, you also need NumPy, Matplotlib, scikit-learn, and SciPy. You can make the installation process easier by installing pyzo.  

Step 1. Install the Pyzo IDE (http://www.pyzo.org/start.html)

Step 2. Install Python environment (http://www.pyzo.org/start.html#step-2-install-python-environment)

Step 3. Install Scientific packages needed to run SAnDReS.

To run Pyzo IEP go to c:\Program Files (x86)\pyzo directory and you will have the pyzo IEP. Double click on pyzo. In the Pyzo’s shell (IEP), type the following commands:

    conda install numpy

    conda install scipy pyqt matplotlib 

    conda install scikit-learn

Step 4. Download SAnDReS 1.1.0 (https://github.com/azevedolab/sandres/raw/master/sandres.zip)

Step 5. Unzip the zipped file (sandres.zip) 

Step 6. Copy sandres directory to c:\ .

Step 7. Open a command prompt window and type: cd c:\sandres

then type: python sandres1_GUI.py

This launches GUI window for SAnDReS. That´s it, good SAnDReS session. See tutorial page for additional information about how to run SAnDReS. You can also start SAnDReS clicking on the sandres.bat file. You may also create a shortcut for SAnDReS right clicking on the sandres.bat file. 


Tutorials

http://sandres.net/Tutorials.php


Please cite the following paper Xavier et al. 2016 when using SAnDReS

Xavier MM, Heck GS, de Avila MB, Levin NM, Pintro VO, Carvalho NL, Azevedo WF Jr. SAnDReS a Computational Tool for Statistical Analysis of Docking Results and Development of Scoring Functions. Comb Chem High Throughput Screen. 2016; 19(10): 801-812. 


Related Publications

de Ávila MB, de Azevedo WF Jr. Development of machine learning models to predict inhibition of 3-dehydroquinate dehydratase. Chem Biol Drug Des. 2018. doi: 10.1111/cbdd.13312     

Russo S, De Azevedo WF. Advances in the Understanding of the Cannabinoid Receptor 1 - Focusing on the Inverse Agonists Interactions. Curr Med Chem. 2018. doi: 10.2174/0929867325666180417165247     

Amaral MEA, Nery LR, Leite CE, de Azevedo Junior WF, Campos MM. Pre-clinical effects of metformin and aspirin on the cell lines of different breast cancer subtypes. Invest New Drugs. 2018. doi: 10.1007/s10637-018-0568-y  

Levin NMB, Pintro VO, Bitencourt-Ferreira G, Mattos BB, Silvério AC, de Azevedo Jr. WF. Development of CDK-targeted scoring functions for prediction of binding affinity. Biophys Chem. 2018; 235: 1–8. https://doi.org/10.1016/j.bpc.2018.01.004         

Freitas PG, Elias TC, Pinto IA, Costa LT, de Carvalho PVSD, Omote DQ, Camps I, Ishikawa T, Arcuri HA, Vinga S, Oliveira AL, Junior WFA, da Silveira NJF. Computational Approach to the Discovery of Phytochemical Molecules with Therapeutic Potential Targets to the PKCZ protein. Letters in Drug Design & Discovery 2018 DOI: 10.2174/1570180814666170810120150   

Pintro VO, Azevedo WF. Optimized Virtual Screening Workflow. Towards Target-Based Polynomial Scoring Functions for HIV-1 Protease. Comb Chem High Throughput Screen. 2017; 20(9): 820-827.              

de Ávila MB, Xavier MM, Pintro VO, de Azevedo WF. Supervised machine learning techniques to predict binding affinity. A study for cyclin-dependent kinase 2.  Biochem Biophys Res Commun. 2017; 494: 305-310.      

de Azevedo WF. Meet Our Editorial Board Member. Author(s): Walter Filgueira de Azevedo. Curr Bioinform. 2017; 12(5):385-386.          

Heck GS, Pintro VO, Pereira RR, de Ávila MB, Levin NMB, de Azevedo WF. Supervised Machine Learning Methods Applied to Predict Ligand-Binding Affinity. Curr Med Chem. 2017; 24(23): 2459-2470.     

Levin NM, Pintro VO, de Ávila MB, de Mattos BB, De Azevedo WF Jr. Understanding the Structural Basis for Inhibition of Cyclin-Dependent Kinases. New Pieces in the Molecular Puzzle. Curr Drug Targets. 2017; 18(9): 1104-1111.        
