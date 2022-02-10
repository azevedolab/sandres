# SAnDReS 2.0
Statistical Analysis of Docking Results and Scoring Functions 2.0 (SAnDReS 2.0)(https://azevedolab.net/sandres.php)
<P>&nbsp;</P>
SAnDReS 2.0 brings together the most advanced tools for protein-ligand docking simulation and machine-learning modeling. We have the newest version of AutoDock Vina, available in February 2022 (version 1.2.3), as a docking engine. Also, SAnDReS 2.0 uses the latest version of Scikit-Learn, available in February 2022 (version 1.0.2). It has 64 regression methods which allow us to explore the Scoring Function Space (SFS). This exploration of the SFS permits us to have an adequate machine-learning (ML) model for a targeted protein system. SAnDReS predicts binding affinity for a specific protein system with superior performance compared against classical scoring functions. In summary, SAnDReS 2.0 makes it possible for you to design a scoring function adequate to the protein system of your interest. 
<P>You need Python 3 installed on your computer to run SAnDReS 2.0. In addition, you need Matplotlib, NumPy, Scikit-Learn, SciPy, and XGBoost. It is also necessary to have MGLTools 1.5.7. You can make the installation of Python packages faster by installing Anaconda.</P>
<P>&nbsp;</P>
<P>&nbsp;</P>
SAnDReS 2.0 User's Guide is available here (Flipbook): https://heyzine.com/flip-book/6fb24027a3.html</P>
<P>&nbsp;</P>
<P>SAnDReS 2.0 User's Guide is available here (PDF): https://github.com/azevedolab/sandres/raw/master/sandres_users_guide_2022_02.pdf</P>
<P>&nbsp;</P>
<H2>Installing SAnDReS 2.0 (Linux)</H2>
<P>You should type all commands shown here in a Linux terminal. The easiest way to open a Linux terminal is to use the Ctrl+Alt+T key combination.</P>
<P><B>Step 1.</B> Download MGLTools 1.5.7 (https://ccsb.scripps.edu/mgltools/downloads/).</P>
<P>Type the following commands:
  <I> </I> <I>
  
    cd ~
    
    cp Downloads/mgltools_Linux-x86_64_1.5.7_install .

    chmod u+x mgltools_Linux-x86_64_1.5.7_install 

    ./mgltools_Linux-x86_64_1.5.7_install 
    
    rm mgltools_Linux-x86_64_1.5.7_install 
</I></P>
<P><B>Step 2.</B> Download Anaconda Installer for Linux (https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh).</P>
<P>Go to the directory where you have the installer file and type the following commands:
 
 <I> </I> <I>
  
    chmod u+x Anaconda3-2021.11-Linux-x86_64.sh
  
    ./Anaconda3-2021.11-Linux-x86_64.sh

  </I>Follow the instructions of the installer. You may use a newer installer, but be sure to have the right installer in the above command lines.

<P><B>Step 3.</B> To run SAnDReS 2.0 properly, you need Scikit-Learn 1.0.2. To be sure you have version 1.0.2, open a terminal and type the following commands:

 <I> </I> <I>
  
    python -m pip uninstall scikit-learn
 
    python -m pip install scikit-learn==1.0.2

 </I>
 <I> </I> <I></P>
</I><B>Step 4.</B> To install XGBoost (https://xgboost.readthedocs.io/en/latest/install.html#python), type the following command in a terminal:</P>

 <I> </I> <I>
  
    python -m pip install xgboost

 </I>
</I><P><B>Step 5.</B> Download SAnDReS 2.0 (https://github.com/azevedolab/sandres/raw/master/sandres2.zip). Copy the sandres2 zipped directory (sandres2.zip) to wherever you want it and unzip the zipped directory. 
<P>Type the following command:
 
 
 <I> </I> <I>
  
    unzip sandres2.zip

 </I><P></P>
 
  <P>cd to sandres2 directory then, type: 
<I> </I><I>
  
    python sandres2.py

   </I>
  <P>Now you have the GUI window for SAnDReS 2.0.</P>
  <img src="https://github.com/azevedolab/sandres/blob/e31a1a7524f27a448b58706599b861578794b57a/sandres_2_Linux_view_01.png", title="SAnDReS 2.0 Main Menu">
  
  <I>SAnDReS 2.0 Main Menu</I></img>
<P>That´s it, good SAnDReS session! By February 2022, we will have a tutorial page for additional information about how to run SAnDReS.</P>
  <P>&nbsp;</P>
  <P>&nbsp;</P>
   </I><H2>Installing SAnDReS 2.0 (Windows)</H2>  
<P><B>Step 1.</B> Install MGLTools 1.5.7 (https://ccsb.scripps.edu/mgltools/downloads/).</P>
<P><B>Step 2.</B> Install Anaconda (https://www.anaconda.com/download/). Right-click the Windows Start Menu icon and select the Anaconda prompt. From now on, insert all commands in an Anaconda prompt.</P>
<P><B>Step 3.</B> To run SAnDReS 2.0 properly, you need Scikit-Learn 1.0.2. To be sure you have version 1.0.2, open an Anaconda prompt and type the following commands:

 <I> </I> <I>
  
    python -m pip uninstall scikit-learn
 
    python -m pip install scikit-learn==1.0.2

 </I> 
</I><P><B>Step 4.</B> To install XGBoost (https://xgboost.readthedocs.io/en/latest/install.html#python), type the following command:</P>

 <I> </I> <I>
  
    python -m pip install xgboost

 </I>
<P><B>Step 5.</B> Download SAnDReS 2.0 (https://github.com/azevedolab/sandres/blob/master/sandres2_win.zip). Copy the sandres2_win zipped directory (sandres2_win.zip) to wherever you want it and unzip the zipped directory. 
<P>Open an Anaconda Prompt and cd to sandres2_win directory then, type: 

 <I> </I><I>
  
    python sandres2.py

   </I>
<P>Now you have the GUI window for SAnDReS 2.0.</P>
  <img src="https://github.com/azevedolab/sandres/blob/e31a1a7524f27a448b58706599b861578794b57a/sandres_2_Linux_view_01.png", title="SAnDReS 2.0 Main Menu">
  
  <I>SAnDReS 2.0 Main Menu</I></img>
<P>That´s it, good SAnDReS session! By February 2022, we will have a tutorial page for additional information about how to run SAnDReS.</P>
