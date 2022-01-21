# SAnDReS 2.0
Statistical Analysis of Docking Results and Scoring Functions 2.0 (SAnDReS 2.0)
https://azevedolab.net/sandres.php
<P>&nbsp;</P>
You need Python 3 installed on your computer to run SAnDReS 2.0. In addition, you need Matplotlib, NumPy, scikit-learn, SciPy, and XGBoost. It is also necessary to have MGLTools 1.5.7 installed on your computer. You can make the installation of Python packages faster by installing Anaconda. 
<P>&nbsp;</P>
<H2>Installing SAnDReS 2.0 (Linux)</H2>  
<B>Step 1.</B> Install Anaconda (available here: https://www.anaconda.com/download/)
<P>&nbsp;</P>
<B>Step 2.</B> Install MGLTools 1.5.7 (https://ccsb.scripps.edu/mgltools/downloads/)
<P>&nbsp;</P>
<B>Step 3.</B> To run SAnDReS 2.0 properly, you need Scikit-Learn 1.0.2. To be sure to have the right Scikit-Learn version to run SAnDReS 2.0, you open a terminal and run Python IDLE shell. Type the following command:
<P>&nbsp;</P>
<P><I>python3</I></P>
<P>&nbsp;</P>
Then you enter in the IDLE prompt:
<P><I>>>>import sklearn</P>
<P>>>>print(sklearn.__version__)</I></P>
You should get the following message: 
<P>1.0.2</P>
To exit the Python IDLE shell, you type:
<P><I>>>>quit()</I></P>
<P>&nbsp;</P>
If you have version 1.0.2, it is fine. Go to the following step. Otherwise, you need to uninstall the current version. You open a terminal and type the following commands:
<P>&nbsp;</P>
<P><I>python3 -m pip uninstall scikit-learn</I></P>
<P>&nbsp;</P>
Then you install the specific Scikit-Learn version 1.0.2:
<P>&nbsp;</P>
<P><I>python3 -m pip install scikit-learn==1.0.2</I></P>
<P>&nbsp;</P>
<B>Step 4.</B> Install XGBoost (available here: https://xgboost.readthedocs.io/en/latest/install.html#python)
<P>&nbsp;</P>
<B>Step 5.</B> Download SAnDReS 2.0 (available here: https://github.com/azevedolab/sandres/raw/master/sandres2.zip). Copy the sandres2 zipped directory (sandres2.zip) to wherever you want it and unzip the zipped directory. Type the following command:
<P>&nbsp;</P>
<P><I>unzip sandres2.zip</I></P>
<P>&nbsp;</P>
Open a terminal and cd to sandres2 directory then, type:
<P>&nbsp;</P>
<I>python sandres2.py</I> 
<P>&nbsp;</P>
Now we have the GUI window for SAnDReS 2.0. That´s it, good SAnDReS session. By February 2022, we will have a tutorial page for additional information about how to run SAnDReS.
<P>&nbsp;</P>
<P>&nbsp;</P>


<H2>Installing SAnDReS 2.0 (Windows)</H2>  
<B>Step 1.</B> Install Anaconda (available here: https://www.anaconda.com/download/)
<P>&nbsp;</P>
<B>Step 2.</B> Install MGLTools 1.5.7 (https://ccsb.scripps.edu/mgltools/downloads/)
<P>&nbsp;</P>
<B>Step 3.</B> To run SAnDReS 2.0 properly, you need Scikit-Learn 1.0.2. To be sure to have the right Scikit-Learn version to run SAnDReS 2.0, you open a command prompt and run Python IDLE shell. Type the following command:
<P>&nbsp;</P>
<P><I>python3</I></P>
<P>&nbsp;</P>
Then you enter in the IDLE prompt:
<P><I>>>>import sklearn</P>
<P>>>>print(sklearn.__version__)</I></P>
You should get the following message: 
<P>1.0.2</P>
To exit the Python IDLE shell, you type:
<P><I>>>>quit()</I></P>
<P>&nbsp;</P>
If you have version 1.0.2, it is fine. Go to the following step. Otherwise, you need to uninstall the current Scikit-Learn version. You open a command prompt and type the following commands:
<P>&nbsp;</P>
<P><I>python -m pip uninstall scikit-learn</I></P>
<P>&nbsp;</P>
Then you install the specific Scikit-Learn version 1.0.2:
<P>&nbsp;</P>
<P><I>python -m pip install scikit-learn==1.0.2</I></P>
<P>&nbsp;</P>
<B>Step 4.</B> Install XGBoost (available here: https://xgboost.readthedocs.io/en/latest/install.html#python)
<P>&nbsp;</P>
<B>Step 5.</B> Download SAnDReS 2.0 (available here: https://github.com/azevedolab/sandres/raw/master/sandres2.zip). Copy the sandres2 zipped directory (sandres2.zip) to wherever you want it and unzip the zipped directory. Open a command prompt and cd to sandres2 directory then, type:
<P>&nbsp;</P>
<I>python sandres2.py</I> 
<P>&nbsp;</P>
Now we have the GUI window for SAnDReS 2.0. That´s it, good SAnDReS session. By February 2022, we will have a tutorial page for additional information about how to run SAnDReS.
