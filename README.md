# clean-energy-storage-optimization
To guide an AI coding agent (like GitHub Copilot or Claude Code) without installing anything locally, your  should act as an agentic instruction manual. It needs to outline the project’s goal, architectural constraints, and step-by-step instructions so the AI can build and run the project entirely in the cloud. [1, 2, 3, 4, 5]  
Here is the exact framework to paste into your  to guide the agent: 
Clean Energy Storage Optimization 
🤖 Project Overview & Constraints 
This project is an interactive data dashboard and optimization engine for a grid-tied clean energy storage system. 

• Environment: Built entirely in a cloud IDE (GitHub Codespaces or Google IDX) [2, 3]. 
• Tech Stack: Python, Pandas, CVXPY (Optimization), Streamlit (Dashboard), and Plotly (Visualization) [11]. 
• Rule: Do NOT ask the user to install any local dependencies. All operations must run within the cloud environment. [6, 7, 8]  

🛠️ Required Cloud Tech Stack (Phase 1) 
To ensure the environment is ready for coding, verify that the following libraries are installed in the cloud terminal: 
📊 Development Roadmap 
Instruct the agent to follow these phases sequentially: 
Phase 2: Data Gathering & Processing Pipeline 

• Task: Fetch and clean historical grid data (e.g., from OpenEI or Kaggle datasets) [12]. 
• Outputs:  
• Agent Guidelines: Create a robust pandas script to parse timestamps, fill missing data, normalize grid prices, and save outputs in a clean format ready for modeling. [9]  

Phase 3: Battery Optimization Math Model 

• Task: Formulate a Linear Program using  to maximize energy arbitrage. 
• Outputs:  
• Agent Guidelines: Set up the constraints for battery state of charge (SoC), charging/discharging limits, and round-trip efficiency. Ensure the math minimizes costs based on the time-series price data from Phase 2. 

Phase 4: Interactive Dashboard Deployment 

• Task: Build an interactive UI using  and . 
• Outputs:  
• Agent Guidelines: The dashboard must allow users to toggle variables like battery size and max charge rate. Display clear charts of electricity prices, charge/discharge events, and cumulative cost savings. [10]  

🚀 How to Run the Project in the Cloud 

1. Click the green Code button on the GitHub repository. 
2. Select Codespaces -&gt; Create codespace on main. 
3. Once the environment loads, open the built-in terminal. 
4. Launch the Streamlit dashboard by running: 


