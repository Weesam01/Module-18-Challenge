# Module-18-Challenge
In this repository you will find a .py file named Pychain, in this file we are a fintech engineer who’s working at one of the five largest banks in the world. We were recently promoted to act as the lead developer on their decentralized finance team. My task is to build a blockchain-based ledger system, complete with a user-friendly web interface. This ledger will allow partner banks to conduct financial transactions (that is, to transfer money between senders and receivers) and to verify the integrity of the data in the ledger.
# Part 1 Create a Record Data Class
We will define a new Python data class named Record. 
Define a new class named Record.
Add the dataclass decorator immediately before the Record class definition.
Add an attribute named sender of type str.
Add an attribute named receiver of type str.
Add an attribute named amount of type float.

# Part 2 Modify the Existing Block Data Class to Store Record Data
In this part we will rename the data attribute in the Block class to record, and then set it to use an instance of the new Record class that i created in the previous section. 
In the Block class, renamed the data attribute to record.
Set the data type of the record attribute to Record.

# Part 3 Add Relevant User Inputs to the Streamlit Interface
In this section, we will create input areas to capture the sender, receiver, and amount for each transaction in the Block record. 
Delete the input_data variable from the Streamlit interface.
Add an input area where you can get a value for sender from the user.
Add an input area where you can get a value for receiver from the user.
Add an input area where you can get a value for amount from the user.

# Part 4  Test the PyChain Ledger by Storing Records

Lastly, testing my PyChain ledger and user interface by running Streamlit application and storing mined blocks in my PyChain ledger. Then test the blockchain validation process by using my PyChain ledger.

Enter values for the sender, receiver, and amount. 
Verify the block contents and hashes in the Streamlit drop-down menu. 
Test the blockchain validation process by using the web interface. 


![Alt text](Images/Pic5.PNG)
![Alt text](Images/Pic5.PNG)
![Alt text](Images/Pic5.PNG)
