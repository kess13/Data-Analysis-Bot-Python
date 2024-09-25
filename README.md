This Telegram bot is designed to assist users with data entry, storage, visualization, and statistical analysis. Here's a detailed breakdown of its capabilities:

Data Entry and Storage:

Guided Data Entry: The bot guides users through a step-by-step process to input data such as net weight, price per liter, liters consumed, and miles driven.
Data Storage: Inputs are saved in an Excel file (result.xlsx). Each user’s data is stored with a timestamp to ensure accurate tracking.
Restart Process: Users can restart the data entry process with the /restart command, allowing them to re-enter data if necessary.

Data Visualization:
Graph Generation: Using the /graph command, the bot generates a graph from the stored data and sends it to the user. This is facilitated by the generate_graph function.
Dynamic Graphing: The bot pauses briefly to ensure the graph is generated before sending it, ensuring a smooth user experience.

Statistics Calculation:
Statistical Summaries: The bot calculates key statistics (maximum, minimum, average) for numerical columns in the Excel file using the /statistics command.
Detailed Reporting: A detailed message with the calculated statistics is sent to the user, providing insights into their data.

User Interaction and Commands:
/start Command: Welcomes the user and provides instructions on how to use the bot. It lists available commands and their purposes.
/EnterData Command: Initiates the data entry process, prompting the user to input required data step-by-step.
/restart Command: Restarts the data entry process for the user, ensuring they can correct any mistakes or update their information.
/statistics Command: Computes and sends statistical summaries of the data stored in the Excel file.
/graph Command: Generates and sends a graph based on the stored data, providing a visual representation of the information.

Interactive Menu:
Keyboard Markup: The bot uses a reply keyboard with buttons for easy access to commands like /restart, /EnterData, /statistics, and /graph.
