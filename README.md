# SAnDReS 2.0
Statistical Analysis of Docking Results and Scoring Functions 2.0 (SAnDReS 2.0)
https://azevedolab.net/sandres.php
<P>&nbsp;</P>
<H2>Overview</H2>
SAnDReS (Statistical Analysis of Docking Results and Scoring functions) draws inspiration from several protein systems that we have been working on in the last decades. These projects began in the 1990s with pioneering studies focused on intermolecular interactions between cyclin-dependent kinase (CDK) (EC 2.7.11.22) and inhibitors (de Azevedo et al., 1996; de Azevedo et al., 1997). SAnDReS is a free and open-source (GNU General Public License) computational environment for the development of machine-learning models (Bitencourt-Ferreira & de Azevedo, 2019; Bitencourt-Ferreira et al., 2021; Bitencourt-Ferreira, Rizzotto et al., 2021) for the prediction of ligand-binding affinity (Xavier et al., 2016; Bitencourt-Ferreira & de Azevedo, 2019; Veit-Acosta & de Azevedo, 2021). We developed SAnDReS using Python programming language, and SciPy, NumPy, scikit-learn (Pedregosa et al., 2011), and Matplotlib libraries as a computational tool to explore the scoring function space (Heck et al., 2017; Bitencourt-Ferreira & de Azevedo, 2019). SAnDReS 1.0 has been applied to several protein systems and has over 80 citations. SAnDReS 2.0 is now available to download (Linux version available here: https://azevedolab.net/resources/sandres2.zip).

<P>&nbsp;</P>

<H2>Installing SAnDReS 2.0 (Linux)</H2>  
You need Python 3 installed on your computer to run SAnDReS 2.0. In addition, you also need Matplotlib, NumPy, scikit-learn, SciPy, and XGBoost. It is also necessary to have AutoDock Vina installed on your computer. You can make the installation of Python packages faster by installing Anaconda. 
<P>&nbsp;</P>
Step 1. Install Anaconda (available here: https://www.anaconda.com/download/)
<P>&nbsp;</P>
Step 2. Install AutoDock Vina (available here: http://vina.scripps.edu/download.html)
<P>&nbsp;</P>
Step 3. Install XGBoost (available here: https://xgboost.readthedocs.io/en/latest/install.html#python)
<P>&nbsp;</P>
Step 4. Download SAnDReS 2.0 (available here: https://azevedolab.net/resources/sandres2.zip). Unzip the zipped directory (sandres2.zip) and move the sandres2 directory to wherever you want it.
<P>&nbsp;</P>
Step 5. Open a terminal and cd to sandres2 directory then, type: python run_program.py 
<P>&nbsp;</P>
Now we have the GUI window for SAnDReS 2.0. That´s it, good SAnDReS session. By November 2021, we will have a tutorial page for additional information about how to run SAnDReS.
<P>&nbsp;</P>
<P>&nbsp;</P>
<H2>References</H2>

-Bitencourt-Ferreira G, de Azevedo WF Jr. SAnDReS: A Computational Tool for Docking. Methods Mol Biol. 2019; 2053: 51–65.   <a href="https://pubmed.ncbi.nlm.nih.gov/31452098/">PubMed</a>   

-Bitencourt-Ferreira G, de Azevedo WF Jr. Machine Learning to Predict Binding Affinity. Methods Mol Biol. 2019; 2053: 251–273.   <a href="https://pubmed.ncbi.nlm.nih.gov/31452110/">PubMed</a>   

-Bitencourt-Ferreira G, de Azevedo WF Jr. Exploring the Scoring Function Space. Methods Mol Biol. 2019; 2053: 275–281.   <a href="https://pubmed.ncbi.nlm.nih.gov/31452111/">PubMed</a>   

-Bitencourt-Ferreira G, da Silva AD, de Azevedo WF Jr. Application of Machine Learning Techniques to Predict Binding Affinity for Drug Targets. A Study of Cyclin-Dependent Kinase 2. Curr Med Chem. 2021; 28(2): 253–265.   <a href="https://pubmed.ncbi.nlm.nih.gov/31729287/">PubMed</a>   

-Bitencourt-Ferreira G, Rizzotto C, de Azevedo Junior WF. Machine Learning-Based Scoring Functions. Development and Applications With SAnDReS. Curr Med Chem. 2021; 28(9): 1746–1756.   <a href="https://pubmed.ncbi.nlm.nih.gov/32410551/">PubMed</a>   

-De Azevedo WF Jr, Mueller-Dieckmann HJ, Schulze-Gahmen U, Worland PJ, Sausville E, Kim SH. Structural basis for specificity and potency of a flavonoid inhibitor of human CDK2, a cell cycle kinase. Proc Natl Acad Sci U S A. 1996; 93(7): 2735–2740.   <a href="https://pubmed.ncbi.nlm.nih.gov/8610110/">PubMed</a>   

-De Azevedo WF, Leclerc S, Meijer L, Havlicek L, Strnad M, Kim SH. Inhibition of cyclin-dependent kinases by purine analogues: crystal structure of human cdk2 complexed with roscovitine. Eur J Biochem. 1997; 243(1-2): 518–526.   <a href="https://pubmed.ncbi.nlm.nih.gov/9030780/">PubMed</a>

-Heck GS, Pintro VO, Pereira RR, de Ávila MB, Levin NMB, de Azevedo WF. Supervised Machine Learning Methods Applied to Predict Ligand-Binding Affinity. Curr Med Chem. 2017; 24(23): 2459–2470.   <a href="https://pubmed.ncbi.nlm.nih.gov/28641555/">PubMed</a>   

-Pedregosa F, Varoquaux G, Gramfort A, Michel V, Thirion B, Grisel O, Blondel M, Prettenhofer P, Weiss R, Dubourg V, Verplas J, Passos A, Cournapeau D, Brucher M, Perrot M, Duchesnay E. Scikit-learn: Machine Learning in Python. J Mach Learn Res. 2011; 12: 2825–2830.   <a href="https://www.jmlr.org/papers/volume12/pedregosa11a/pedregosa11a.pdf">PDF</a>    

-Veit-Acosta M, de Azevedo Junior WF. The Impact of Crystallographic Data for the Development of Machine Learning Models to Predict Protein-Ligand Binding Affinity. Curr Med Chem. doi: 10.2174/0929867328666210210121320.   <a href="https://pubmed.ncbi.nlm.nih.gov/33568025/">PubMed</a>   
  
-Xavier MM, Heck GS, de Avila MB, Levin NM, Pintro VO, Carvalho NL, Azevedo WF Jr. SAnDReS a Computational Tool for Statistical Analysis of Docking Results and Development of Scoring Functions. Comb Chem High Throughput Screen. 2016; 19(10): 801–812.   <a href="https://www.ncbi.nlm.nih.gov/pubmed/27686428">PubMed</a>
