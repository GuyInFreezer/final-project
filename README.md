# final-project

# Chatty Kathy AI Workout Companion

## Table of Contents
1. [Project Overview](#project-overview)
2. [Objectives](#objectives)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Data Collection and Preparation](#data-collection-and-preparation)
6. [Model Implementation](#model-implementation)
7. [Model Optimization](#model-optimization)
8. [Model Performance](#model-performance)
9. [GitHub Repository Structure](#github-repository-structure)
10. [Future Work](#future-work)
11. [Team Members](#team-members)

## Project Overview
Chatty Kathy is an AI-powered workout companion platform designed to provide personalized health coaching. The platform leverages synthetic data and advanced machine learning techniques to offer engaging, motivational, and customized workout experiences. Our goal is to promote fairness, inclusivity, and user engagement while mitigating biases and ensuring equitable treatment for all users.

## Objectives
- **Promote physical activity:** Encourage users to engage in regular exercise through personalized health coaching.
- **Ensure fairness and inclusivity:** Mitigate biases and provide equitable treatment for diverse user groups.
- **Enhance user engagement:** Use AI-driven interactions to make workouts more engaging and enjoyable.
- **Protect privacy:** Leverage synthetic data to maintain user privacy while providing effective recommendations.

## Features
- **Fairness-aware Algorithms:** Machine learning algorithms designed to minimize biases and ensure equitable treatment.
- **Diverse and Representative Data:** Synthetic data representing diverse demographic backgrounds and preferences.
- **Transparency and Explainability:** Transparent explanations for recommendations to build user trust.
- **User-Centric Design:** Involving diverse user groups in design and testing for inclusive feedback.
- **Continuous Improvement:** Ongoing monitoring and evaluation to refine the recommendation system.

## Technologies Used
- **Python:** Programming language for data processing and model implementation.
- **Jupyter Notebook:** Environment for data analysis and model training.
- **OpenAI GPT-3.5:** Used for generating synthetic data.
- **gTTS:** Used for Text-to-Speech.
- **dotenv:** For managing environment variables securely.
- **playsound:** Used to play the TTS audio file.

## Data Collection and Preparation
### Data Sources
- Synthetic data generated to simulate user behavior and preferences.
### Data Extraction
- Automated extraction of relevant data points using scripts.
### Data Cleaning
- Removal of noise and inconsistencies to ensure data quality.
### Data Transformation
- Converting data into a usable format for model training.

## Model Implementation
### Jupyter Notebook
- Detailed process from data extraction to transformation, with the cleaned data exported as CSV files for further analysis and model training.
### Model Initialization
- Setting up the AI model using Python.
### Training and Evaluation
- Iteratively training the model and evaluating its performance using metrics such as accuracy, precision, recall, and F1-score.
### Pre-trained Model
- Integration of pre-trained models to enhance accuracy.

## Model Optimization
### Optimization Process
- Iterative changes and enhancements to improve model performance.
### Evaluation Metrics
- Continuous evaluation using various metrics to track performance improvements.
### Documentation
- Detailed records of the optimization process documented in Python script.

## Model Performance
- Final performance metrics are based on mostly training loss, which is measured by MSE (Mean Squared Error).

## GitHub Repository Structure
- **Documents/**: Contains Presentation.
- **Images/**: Contains images if used in README.
- **Resources/**: Contains scripts and jsonl.
- **Sources/**: Contains codes.
- **README.md**: Project overview and documentation.
- **.gitignore**: List of files and directories to be ignored by Git.

## Future Work
- **Expand Dataset:** Incorporate more diverse and representative synthetic data.
- **Enhance Model:** Further refine the model to improve accuracy and performance.
- **User Feedback:** Continuously collect and integrate user feedback for iterative improvements.
- **New Features:** Explore additional features such as voice recognition and real-time feedback.

## Team Members
- Jay Requarth
- John Andrews
- Dr. Dick Davis II
- Nee Buntoum
- Nam Yeongjin
- Mat Nicholas
- Jana Avery

## Installation and Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-repo/ChattyKathy.git
   cd ChattyKathy
   ```
2. **Set up environment variables:**
   - Create a `.env` file in the root directory with your OpenAI API key and OpenWeather Map API key.
   ```env
   OPENAI_API_KEY=your-openai-api-key
   OPENWEATHERMAP_API_KEY = your-owm-api-key
   ```

## Usage
- **Main Program - Run Chatty Katty.py:**
   ```sh
   python "Chatty Katty.py"
   ```
- **Utility - Run via Jupyter Notebook**
- Open the notebook in your browser and follow the steps to preprocess data, train the model, and evaluate performance.

## License
This project is licensed under the MIT License.

