# Python script to show the current version of installed Scikit-Learn
#
################################################################################
# Dr. Walter F. de Azevedo, Jr.                                                #
# https://azevedolab.net/                                                      #
# January 12, 2022                                                             #
################################################################################
#
# Import package
import sklearn

# Get version
scikit_learn_version = sklearn.__version__

# Show version
print("\nCurrent version of Scikit-Learn: {}.".format(scikit_learn_version))

# Check version
if scikit_learn_version != "1.0.2":
    # Set up additional message
    msg_out = "\nYou need version 1.0.2 of Scikit-Learn to run SAnDReS 2.0. "
    msg_out += "\nYou have to uninstall the current version and install "
    msg_out += "version 1.0.2."
    msg_out += "\n\nOpen a terminal (command prompt) and "
    msg_out += "type the following commands: "
    msg_out += "\npython -m pip uninstall scikit-learn"
    msg_out += "\npython -m pip install scikit-learn==1.0.2"

else:
    # Set up additional message
    msg_out = "\nYou have version 1.0.2 of Scikit-Learn adequate "
    msg_out += "to run SAnDReS 2.0."

# Show additional message
print(msg_out)