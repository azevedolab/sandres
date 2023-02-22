# SAnDReS 2.0.0
Statistical Analysis of Docking Results and Scoring Functions 2.0.0 (<a href="https://azevedolab.net/sandres.php" title="SAnDReS 2.0.0">SAnDReS 2.0.0</a>
<P>&nbsp;</P>
SAnDReS 2.0.0 brings together the most advanced tools for protein-ligand docking simulation and machine-learning modeling. We have the newest version of AutoDock Vina, available in February 2023 (version 1.2.3), as a docking engine. Also, SAnDReS 2.0.0 uses the latest version of Scikit-Learn, available in February 2023 (version 1.2.0). It has 54 regression methods which allow us to explore the Scoring Function Space (SFS). This exploration of the SFS permits us to have an adequate machine-learning (ML) model for a targeted protein system. SAnDReS predicts binding affinity for a specific protein system with superior performance compared against classical scoring functions. In summary, SAnDReS 2.0.0 makes it possible for you to design a scoring function adequate to the protein system of your interest. 
<P>You need Python 3 installed on your computer to run SAnDReS 2.0.0. In addition, you need Pandas, Matplotlib, NumPy, Scikit-Learn, and SciPy. It is also necessary to have ADFRsuite version 1.0. You can make the installation of Python packages faster by installing Anaconda.</P>
<P>&nbsp;</P>
<H2>Installing SAnDReS (Linux)</H2>
<P>You should type all commands shown here in a Linux terminal. The easiest way to open a Linux terminal is to use the Ctrl+Alt+T key combination.</P>
<P><B>Step 1.</B> Download <a href="https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh" title="Anaconda Installer for Linux">Anaconda Installer for Linux</a> or newer.</P>
<P>Go to the directory where you have the installer file and type the following commands:
 
 <I> </I> <I>
  
    chmod u+x Anaconda3-2021.11-Linux-x86_64.sh
  
    ./Anaconda3-2021.11-Linux-x86_64.sh

  </I>Follow the instructions of the installer. You may use a newer installer, but be sure to have the right installer in the above command lines.

<P><B>Step 2.</B> Download ADFRsuite version 1.0 (<a href="https://ccsb.scripps.edu/adfr/downloads/" title="ADFRsuite 1.0 Linux 64 installer app">ADFRsuite 1.0 Linux 64 installer app</a>).</P>
<P>Type the following commands:
  <I> </I> <I>
  
    cd ~
    
    cp Downloads/ADFRsuite_Linux-x86_64_1.0_install .

    chmod a+x ADFRsuite_Linux-x86_64_1.0_install

    ./ADFRsuite_Linux-x86_64_1.0_install

</I>Follow the instructions of the installer. You need to add the path of ADFRsuite to your .bashrc (e.g.,PATH="/home/walter/ADFRsuite-1.0/bin:$PATH"). You need to change to your user.
</P>
<P><B>Step 3.</B> To run SAnDReS 2.0 properly, you need <a href="https://scikit-learn.org/stable/" title="Scikit-Learn. Machine Learning in Python">Scikit-Learn</a> 1.2.0. To be sure you have version 1.2.0, open a terminal and type the following commands:

 <I> </I> <I>
  
    python3 -m pip uninstall scikit-learn
 
    python3 -m pip install scikit-learn==1.2.0

 </I>
 <I> </I> <I></P>
</I><P><B>Step 4.</B> Download SAnDReS 2.0.0 <a href="https://github.com/azevedolab/sandres/raw/master/sandres2.zip" title="SAnDReS 2.0.0">here</a>. Copy the sandres2 zipped directory (<a href="https://github.com/azevedolab/sandres/raw/master/sandres2.zip" title="SAnDReS 2.0.0">sandres2.zip</a>) to wherever you want it and unzip the zipped directory. 
<P>Type the following command:
 
 
 <I> </I> <I>
  
    unzip sandres2.zip

 </I><P></P>
 
  <P>cd to sandres2 directory then, type: 
<I> </I><I>
  
    python3 sandres2.py

   </I>
  <P>Now you have the GUI window for SAnDReS 2.0.0.</P>
<P>That´s it, good SAnDReS session!</P>
  <P>&nbsp;</P>
