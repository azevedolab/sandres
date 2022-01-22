# SAnDReS 2.0
Statistical Analysis of Docking Results and Scoring Functions 2.0 (SAnDReS 2.0)(https://azevedolab.net/sandres.php)
<P>&nbsp;</P>
You need Python 3 installed on your computer to run SAnDReS 2.0. In addition, you need Matplotlib, NumPy, scikit-learn, SciPy, and XGBoost. It is also necessary to have MGLTools 1.5.7 installed on your computer. You can make the installation of Python packages faster by installing Anaconda. 
<P>&nbsp;</P>
<H2>Installing SAnDReS 2.0 (Linux)</H2>  
<P><B>Step 1.</B> Install Anaconda (https://www.anaconda.com/download/)</P>
<P><B>Step 2.</B> Install MGLTools 1.5.7 (https://ccsb.scripps.edu/mgltools/downloads/)</P>
<P><B>Step 3.</B> To run SAnDReS 2.0 properly, you need Scikit-Learn 1.0.2. To be sure you have version 1.0.2, you open a terminal (command prompt) and run the following Python script (scikit_version.py)(https://github.com/azevedolab/sandres/blob/master/scikit_version.py). Type the following command:
<P><I>python scikit_version.py</I></P>
  If you have version 1.0.2, go to the following step. Otherwise, you need to uninstall the current version and install version 1.0.2. 
<P>You open a terminal and type the following commands: 

  <I>python -m pip uninstall scikit-learn</I>

  <I>python -m pip install scikit-learn==1.0.2</I>
<P><B>Step 4.</B> Install XGBoost (https://xgboost.readthedocs.io/en/latest/install.html#python)</P>
<P><B>Step 5.</B> Download SAnDReS 2.0 (https://github.com/azevedolab/sandres/raw/master/sandres2.zip). Copy the sandres2 zipped directory (sandres2.zip) to wherever you want it and unzip the zipped directory. 
<P>Type the following command: 
 
 <I>unzip sandres2.zip</I></P>
<P>Open a terminal and cd to sandres2 directory then, type: 

  <I>python sandres2.py</I></P> 
<P>&nbsp;</P>
  <P>Now you have the GUI window for SAnDReS 2.0.</P>
  <img src="https://github.com/azevedolab/sandres/blob/e31a1a7524f27a448b58706599b861578794b57a/sandres_2_Linux_view_01.png", title="SAnDReS 2.0 Main Menu">
  
  SAnDReS 2.0 Main Menu</img>
<P>That´s it, good SAnDReS session! By February 2022, we will have a tutorial page for additional information about how to run SAnDReS.</P>
