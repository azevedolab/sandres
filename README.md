# SAnDReS 2.0
Statistical Analysis of Docking Results and Scoring Functions 2.0 (SAnDReS 2.0)(https://azevedolab.net/sandres.php)
<P>&nbsp;</P>
You need Python 3 installed on your computer to run SAnDReS 2.0. In addition, you need Matplotlib, NumPy, Scikit-Learn, SciPy, and XGBoost. It is also necessary to have MGLTools 1.5.7 installed on your computer. You can make the installation of Python packages faster by installing Anaconda. SAnDReS 2.0 has the most recent version of AutoDock Vina available in January 2022 (version 1.2.3) as a docking engine. SAnDReS 2.0 considers that you have installed on your computer the latest version of Scikit-Learn available in January 2022 (version 1.0.2). Please, see installation step 3 for issues related to the installation of Scikit-Learn version 1.0.2.
<P>&nbsp;</P>
<H2>Installing SAnDReS 2.0 (Linux) (Option 1)</H2>
<P>The easiest way to install all necessary packages to run SAnDReS 2.0 is to run this installer (https://github.com/azevedolab/sandres/raw/master/install).</P>
<P>You should type all commands shown here in a Linux terminal. To open a Linux terminal you may use the Ctrl+Alt+T key combination.</P>
<P><B>This installer considers that you DO NOT have anaconda3 installed on your computer. If you have anaconda3 installed, please uninstall it before running this installer.</B></P>
<P>To install SAnDReS 2.O, download the installer (https://github.com/azevedolab/sandres/raw/master/install) in the directory where you want to have SAnDReS 2.0 and type the following command:
    <I> </I> <I>
  
    ./install
    
</I></P>
<P>Follow all instructions of the installer.</P>
<P>After finishing the installation. Type the following commands:
      <I> </I> <I>
  
    cd sandres2
    python sandres2.py
    
</I></P>
<P>Now you have the GUI window for SAnDReS 2.0.</P>
  <img src="https://github.com/azevedolab/sandres/blob/e31a1a7524f27a448b58706599b861578794b57a/sandres_2_Linux_view_01.png", title="SAnDReS 2.0 Main Menu">
  
<P>&nbsp;</P>
<H2>Installing SAnDReS 2.0 (Linux) (Option 2)</H2>
<P>You should type all commands shown here in a Linux terminal. The easiest way to open a Linux terminal is to use the Ctrl+Alt+T key combination.</P>
<P><B>Step 1.</B> Download MGLTools 1.5.7 (https://ccsb.scripps.edu/mgltools/downloads/).</P>
<P>Type the following commands:
  <I> </I> <I>
  
    cd ~
    
    cp Downloads/mgltools_Linux-x86_64_1.5.7_install .

    chmod 777 mgltools_Linux-x86_64_1.5.7_install 

    ./mgltools_Linux-x86_64_1.5.7_install 
    
    rm mgltools_Linux-x86_64_1.5.7_install 

</I></P>
<P><B>Step 2.</B> Download Anaconda Installer for Linux (https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh).</P>
<P>Go to the directory where you have the installer file you downloaded and type the following commands:
 
 <I> </I> <I>
  
    chmod 777 Anaconda3-2021.11-Linux-x86_64.sh
  
    ./Anaconda3-2021.11-Linux-x86_64.sh

 </I><P>Follow the instructions of the installer.</P>
 <P>You may use a newer installer, but be sure to have the right name of the installer in the above command lines.</P>

<P><B>Step 3.</B> To run SAnDReS 2.0 properly, you need Scikit-Learn 1.0.2. To be sure you have version 1.0.2, open a terminal and run the following Python script (scikit_version.py)(https://github.com/azevedolab/sandres/blob/master/scikit_version.py).</P> 
<P>Type the following command:

 <I> </I> <I>
  
    python scikit_version.py

 </I><P></P>
 <I> </I> <I>
 </I></P>If you have version 1.0.2, go to the following step. Otherwise, you need to uninstall the current version and install version 1.0.2.  
<P>Type the following commands:

 <I> </I> <I>
  
    python -m pip uninstall scikit-learn
 
    python -m pip install scikit-learn==1.0.2

 </I><P></P> 
 <I> </I> <I>
</I></P><P><B>Step 4.</B> To install XGBoost (https://xgboost.readthedocs.io/en/latest/install.html#python), type the following command in a terminal:</P>

 <I> </I> <I>
  
    python -m pip install xgboost

 </I><P></P>
  
</I><P><B>Step 5.</B> Download SAnDReS 2.0 (https://github.com/azevedolab/sandres/raw/master/sandres2.zip). Copy the sandres2 zipped directory (sandres2.zip) to wherever you want it and unzip the zipped directory. 
<P>Type the following command:
 
 
 <I> </I> <I>
  
    unzip sandres2.zip

 </I><P></P>
 
  <P>cd to sandres2 directory then, type: 
<I> </I><I>
  
    python sandres2.py

   </I><P>&nbsp;</P>
  <P>Now you have the GUI window for SAnDReS 2.0.</P>
  <img src="https://github.com/azevedolab/sandres/blob/e31a1a7524f27a448b58706599b861578794b57a/sandres_2_Linux_view_01.png", title="SAnDReS 2.0 Main Menu">
  
  <I>SAnDReS 2.0 Main Menu</I></img>
<P>That´s it, good SAnDReS session! By February 2022, we will have a tutorial page for additional information about how to run SAnDReS.</P>
  <P>&nbsp;</P>
  <P>&nbsp;</P>
   </I><H2>Installing SAnDReS 2.0 (Windows)</H2>  
<P><B>Step 1.</B> Install MGLTools 1.5.7 (https://ccsb.scripps.edu/mgltools/downloads/)</P>
<P><B>Step 2.</B> Install Anaconda (https://www.anaconda.com/download/)</P>
<P><B>Step 3.</B> To run SAnDReS 2.0 properly, you need Scikit-Learn 1.0.2. To be sure you have version 1.0.2, with the Windows Start, select Anaconda Prompt (anaconda3) and run the following Python script (scikit_version.py)(https://github.com/azevedolab/sandres/blob/master/scikit_version.py). Type the following command in the Anaconda Prompt:

 <I> </I> <I>
  
    python scikit_version.py

 </I><P></P>
  If you have version 1.0.2, go to the following step. Otherwise, you need to uninstall the current version and install version 1.0.2.  
<P>Open an Anaconda Prompt and type the following commands: 
<I> </I> <I>
  
    python -m pip uninstall scikit-learn
 
    python -m pip install scikit-learn==1.0.2

 </I><P></P> 
 </P>
<P><B>Step 4.</B> To install XGBoost (https://xgboost.readthedocs.io/en/latest/install.html#python), type the following command:</P>

 <I> </I> <I>
  
    python -m pip install xgboost

 </I><P>
<P><B>Step 5.</B> Download SAnDReS 2.0 (https://github.com/azevedolab/sandres/blob/master/sandres2_win.zip). Copy the sandres2_win zipped directory (sandres2_win.zip) to wherever you want it and unzip the zipped directory. 
<P>Open an Anaconda Prompt and cd to sandres2_win directory then, type: 

 <I> </I><I>
  
    python sandres2.py

   </I><P>&nbsp;</P>

<P>Now you have the GUI window for SAnDReS 2.0.</P>
  <img src="https://github.com/azevedolab/sandres/blob/e31a1a7524f27a448b58706599b861578794b57a/sandres_2_Linux_view_01.png", title="SAnDReS 2.0 Main Menu">
  
  <I>SAnDReS 2.0 Main Menu</I></img>
<P>That´s it, good SAnDReS session! By February 2022, we will have a tutorial page for additional information about how to run SAnDReS.</P>
