# SAnDReS 2.0.0
Statistical Analysis of Docking Results and Scoring Functions 2.0.0 (SAnDReS 2.0.0) 
<P>&nbsp;</P>
SAnDReS 2.0.0 (<a href="https://doi.org/10.1002/jcc.27449" title="de Azevedo WF Jr, Quiroga R, Villarreal MA, da Silveira NJF, Bitencourt-Ferreira G, da Silva AD, Veit-Acosta M, Oliveira PR, Tutone M, Biziukova N, Poroikov V, Tarasova O, Baud S. SAnDReS 2.0: Development of machine-learning models to explore the scoring function space. J Comput Chem. 2024 Oct 15;45(27):2333-2346. doi: 10.1002/jcc.27449. Epub 2024 Jun 20. PMID: 38900052.">de Azevedo Jr et al., 2024</a>) brings together the most advanced tools for protein-ligand docking simulation and machine-learning modeling. We have the AutoDock Vina 1.2 (<a href="https://pubmed.ncbi.nlm.nih.gov/34278794/" title = "Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: New Docking Methods, Expanded Force Field, and Python Bindings. J Chem Inf Model. 2021 Aug 23;61(8):3891-3898. doi: 10.1021/acs.jcim.1c00203. Epub 2021 Jul 19. PMID: 34278794; PMCID: PMC10683950.">Eberhardt et al., 2021</a>) as a docking engine. Also, SAnDReS 2.0.0 uses machine-learning methods available in the <a href="" title = "Scikit-Learn">Scikit-Learn</a> library (<a href="https://www.google.com/url?q=https%3A%2F%2Fdoi.org%2F10.48550%2FarXiv.1201.0490" title = "Pedregosa F, Varoquaux G, Gramfort A, Michel V, Thirion B, Grisel O, Blondel M, Prettenhofer P, Weiss R, Dubourg V, Verplas J, Passos A, Cournapeau D, Brucher M, Perrot M, Duchesnay E. Scikitlearn: Machine Learning in Python. J Mach Learn Res., 2011; 12:2825–2830. DOI: 10.48550/arXiv.1201.0490">Pedregosa et al., 2011</a>). It has 54 regression methods which allow us to explore the Scoring Function Space (SFS) (<a href="https://pubmed.ncbi.nlm.nih.gov/24124403/" title = "Ross GA, Morris GM, Biggin PC. One Size Does Not Fit All: The Limits of Structure-Based Models in Drug Discovery. J Chem Theory Comput. 2013 Sep 10;9(9):4266-4274. doi: 10.1021/ct4004228. Epub 2013 Aug 5. PMID: 24124403; PMCID: PMC3793897.">Ross et al., 2013</a>). This exploration of the SFS permits us to have an adequate machine-learning (ML) model for a targeted protein system. SAnDReS predicts binding affinity for a specific protein system with superior performance compared against classical scoring functions. In summary, SAnDReS 2.0.0 makes it possible for you to design a scoring function adequate to the protein system of your interest. 
<P>You need <a href="https://www.python.org/" title = "Python">Python 3</a> installed on your computer to run SAnDReS 2.0.0. In addition, you need <a href="https://pandas.pydata.org/" title = "Pandas">Pandas</a>, <a href="https://matplotlib.org/" title = "Matplotlib">Matplotlib</a>, <a href = "https://numpy.org/" title = "NumPy">NumPy</a>, <a href="https://scikit-learn.org/stable/" title = "Scikit-Learn">Scikit-Learn</a>, and <a href = "https://scipy.org/" title = "Scipy">SciPy</a>. It is also necessary to have <a href="https://ccsb.scripps.edu/adfr/downloads/" title="ADFRsuite 1.0 Linux 64 installer app">ADFRsuite version 1.0</a>. You can make the installation of Python packages faster by installing <a href="https://www.anaconda.com/download" title = "Anaconda">Anaconda</a>.</P>
<P>&nbsp;</P>
<H2>How to Cite SAnDReS 2.0</H2>

de Azevedo WF Jr, Quiroga R, Villarreal MA, da Silveira NJF, Bitencourt-Ferreira G, da Silva AD, Veit-Acosta M, Oliveira PR, Tutone M, Biziukova N, Poroikov V, Tarasova O, Baud S. SAnDReS 2.0: Development of machine-learning models to explore the scoring function space. J Comput Chem. 2024; 45(27): 2333–2346. [PubMed](https://pubmed.ncbi.nlm.nih.gov/38900052/) 
<P>&nbsp;</P>
<H2>Installing SAnDReS (Linux)</H2>
<P>You should type all commands shown here in a Linux terminal. The easiest way to open a Linux terminal is to use the Ctrl+Alt+T key combination.</P>
<P><B>Step 1.</B> Download <a href="https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh" title="Anaconda Installer for Linux">Anaconda Installer for Linux</a> or newer.</P>
<P>Go to the directory where you have the installer file and type the following commands:
<pre><I>    chmod u+x Anaconda3-2021.11-Linux-x86_64.sh
    ./Anaconda3-2021.11-Linux-x86_64.sh</I></pre>
<P>Follow the instructions of the installer.
</P>
<P><B>Step 2.</B> Download ADFRsuite version 1.0 (<a href="https://ccsb.scripps.edu/adfr/downloads/" title="ADFRsuite 1.0 Linux 64 installer app">ADFRsuite 1.0 Linux 64 installer app</a>).</P>
<P>Type the following commands:
<pre><I>    cd ~
    cp Downloads/ADFRsuite_Linux-x86_64_1.0_install .
    chmod a+x ADFRsuite_Linux-x86_64_1.0_install
    ./ADFRsuite_Linux-x86_64_1.0_install</I></pre>
<P>Follow the instructions of the installer. You need to add the path of ADFRsuite to your .bashrc (e.g.,PATH="/home/walter/ADFRsuite-1.0/bin:$PATH"). You need to change to your user.</P>
<P><B>Step 3.</B> To run SAnDReS 2.0 properly, you need <a href="https://scikit-learn.org/stable/" title="Scikit-Learn. Machine Learning in Python">Scikit-Learn</a> 1.5.2. To be sure you have version 1.5.2, open a terminal and type the following commands:
<pre><I>    python3 -m pip uninstall scikit-learn
    python3 -m pip install scikit-learn==1.5.2</I></pre>
<P><B>Step 4.</B> Download SAnDReS 2.0.0 <a href="https://github.com/azevedolab/sandres/raw/master/sandres2.zip" title="SAnDReS 2.0.0">here</a>. Copy the sandres2 zipped directory (sandres2.zip) to wherever you want it and unzip the zipped directory. 
<P>Type the following command:</P>
<pre><I>    unzip sandres2.zip</I></pre>
<P>cd to sandres2 directory then, type:</P>
<pre><I>python3 sandres2.py</I></pre>
<P>Now you have the GUI window for SAnDReS 2.0.0. That´s it, good SAnDReS session!</P>
