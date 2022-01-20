# SAnDReS 2.0
Statistical Analysis of Docking Results and Scoring Functions 2.0 (SAnDReS 2.0)
https://azevedolab.net/sandres.php
<P>&nbsp;</P>
<P>&nbsp;</P>
<H2>Installing SAnDReS 2.0 (Linux)</H2>  
You need Python 3 installed on your computer to run SAnDReS 2.0. In addition, you also need Matplotlib, NumPy, scikit-learn, SciPy, and XGBoost. It is also necessary to have MGLTools 1.5.7 installed on your computer. You can make the installation of Python packages faster by installing Anaconda. 
<P>&nbsp;</P>
Step 1. Install Anaconda (available here: https://www.anaconda.com/download/)
<P>&nbsp;</P>
Step 2. Install MGLTools 1.5.7 (https://ccsb.scripps.edu/mgltools/downloads/)
<P>&nbsp;</P>
Step 3. Install Scikit-Learn 1.0.2 (available here: https://scikit-learn.org/stable/index.html). To be sure to have the right Scikit-Learn version to run SAnDReS 2.0, you may uninstall the current version typing:
<P>&nbsp;</P>
<P><I>python3 -m pip uninstall scikit-learn</I></P>
<P>&nbsp;</P>
Then you install the specific Scikit-Learn version:
<P>&nbsp;</P>
<P><I>python3 -m pip install scikit-learn==1.0.2</I></P>
<P>&nbsp;</P>
To check the Scikit-Learn you have, you may type:
<P>&nbsp;</P>
<P><I>python3</I></P>
<P>&nbsp;</P>
Then you enter:
<P><I>>>> import sklearn
>>> print(sklearn.__version__)</I></P>
You should get: 1.0.2
To exit, you type:<I>>>> quit()</I>
<P>&nbsp;</P>
Step 4. Install XGBoost (available here: https://xgboost.readthedocs.io/en/latest/install.html#python)
<P>&nbsp;</P>
Step 5. Download SAnDReS 2.0 (available here: https://github.com/azevedolab/sandres/raw/master/sandres2.zip). Copy the sandres2 zipped directory (sandres2.zip) to wherever you want it and unzip the zipped directory. Type the following command:<I> unzip sandres2.zip </I>
<P>&nbsp;</P>
Step 6. Open a terminal and cd to sandres2 directory then, type:<I> python run_program.py </I> 
<P>&nbsp;</P>
Now we have the GUI window for SAnDReS 2.0. That´s it, good SAnDReS session. By February 2022, we will have a tutorial page for additional information about how to run SAnDReS.
<P>&nbsp;</P>
<H2>Installing SAnDReS 2.0 (Windows)</H2>  
<P>&nbsp;</P>
Step 1. Install Anaconda (available here: https://www.anaconda.com/download/)
<P>&nbsp;</P>
Step 2. Install MGLTools 1.5.7 (available here: https://ccsb.scripps.edu/mgltools/downloads/)
<P>&nbsp;</P>
<P>&nbsp;</P>
Step 3. Install Scikit-Learn 1.0.2 (available here: https://scikit-learn.org/stable/index.html). To be sure to have the right Scikit-Learn version to run SAnDReS 2.0, you may uninstall the current version. Open a prompt command and type: 
<P>&nbsp;</P>
<P><I>python -m pip uninstall scikit-learn</I></P>
<P>&nbsp;</P>
Then you install the specific Scikit-Learn version:
<P>&nbsp;</P>
<P><I>python -m pip install scikit-learn==1.0.2 </I></P>
<P>&nbsp;</P>
To check the Scikit-Learn you have, you may type:
<P>&nbsp;</P>
<P><I>python</I></P>
<P>&nbsp;</P>
Then you enter:
<P><I>>>> import sklearn
>>> print(sklearn.__version__)</I></P>
You should get: 1.0.2
To exit, you type:<I>>>> quit()</I>
<P>&nbsp;</P>
Step 4. Install XGBoost (available here: https://xgboost.readthedocs.io/en/latest/install.html#python)
<P>&nbsp;</P>
Step 5. Download SAnDReS 2.0 (available here: https://github.com/azevedolab/sandres/raw/master/sandres2_win.zip). Copy the sandres2_win zipped directory (sandres2_win.zip) to wherever you want it and unzip the zipped directory.
<P>&nbsp;</P>
Step 6. Open a prompt command and cd to sandres2_win directory then, type: python run_program.py 
<P>&nbsp;</P>
Now we have the GUI window for SAnDReS 2.0. That´s it, good SAnDReS session. By February 2022, we will have a tutorial page for additional information about how to run SAnDReS. This version has been tested on Windows 10.
<P>&nbsp;</P>
<P><B>Note:</B> SAnDReS 2.0 uses AutoDock Vina 1.2.3 as docking engine (https://github.com/ccsb-scripps/AutoDock-Vina) and Scikit-Learn 1.0.2 for machine-learning modeling. <B>Please, be sure to have Scikit-Learn 1.0.2 installed on you computer!</B></P>
