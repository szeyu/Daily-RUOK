# Daily-RUOK
## Project for KitaHack 2024

## Our Team
### AI Cooking
### Group Members
- Sim Sze Yu
- Jonathan Siew
- Sayyid Syamil

## Sustainable Development Goal 3.4 (SDG 3.4) 
By 2030, reduce by one third premature mortality from non-communicable diseases through prevention and treatment and promote mental health and well-being

## Overview
The imperative achievement of Sustainable Development Goal 3 (SDG 3) - Good Health and Well-being is essential for fostering global emotional well-being. Prioritizing quality healthcare and overall well-being not only impacts physical health but also nurtures positive emotional states. Addressing mental health challenges and supporting emotional resilience establishes a foundation for societies to experience a higher quality of life. 
The "Daily RUOK" system, with its focus on daily check-ins and positive reflections, aligns seamlessly with SDG 3 by promoting emotional self-awareness and resilience. This holistic approach emphasizes the interconnectedness of mental and physical health, highlighting the necessity for comprehensive strategies to address emotional wellness in building a healthier and more sustainable global community.

## Specifications
### Personalised Emotional Support
"Daily RUOK" provides users with personalised responses, including advice, compliments, and motivational messages, tailored to their daily input.

### Comprehensive Emotional Data Recording
The system records and organizes user input over time, creating a comprehensive emotional well-being profile for each individual.

### Visualised Emotional Journey
Through intuitive graphical representations, such as graphs, the system visually illustrates the user's emotional journey. This allows users to track patterns, recognise trends, and observe their emotional progress over time.

### Positive Reflection Encouragement
Focusing on daily check-ins and encouraging positive reflections, the system actively promotes emotional self-awareness and resilience.

### Compassionate Companion
Acting as a compassionate companion, the "Daily RUOK" system guides individuals toward sustained emotional well-being and personal growth.

## Google Technology Used
## PaLM API (Maker Suite)
Google products that can be used to prototype and build generative AI applications.

## Specific Issues Faced:
### Interpreting Emotional Tone: 
Developing an algorithm that accurately discerns the emotional context from text inputs.

### Generating Appropriate Responses: 
Creating a response mechanism that is both relevant to the user's emotional state and offers constructive support or advice.

### Scalability: 
Ensuring the solution can handle a large number of users simultaneously without degradation in performance.

## Addressing the Challenge:
### Algorithm Development:
Approach: Utilizing Natural Language Processing (NLP) techniques to analyze user input.
Tools Used: Implementation of sentiment analysis using libraries like Palm API for deeper contextual understanding.
Technical Decision: Opting for a machine learning-based approach to ensure adaptability and accuracy in emotional tone interpretation.

### Response Generation:
Approach: Crafting a response generator that uses emotional analysis to create personalized messages.
Technical Decision: Integrating pre-defined response templates with dynamic content generation, ensuring responses are empathetic and varied.

### User Interface Integration:
Approach: Seamlessly integrating the backend emotional analysis and response system with the user interface.
Technical Decision: Choosing a responsive and intuitive frontend framework (Streamlit) that communicates effectively with the backend.

## Project’s Impact Using Cause and Effect
### Personalised Emotional Support:
Cause: Users receive tailored responses based on their daily input.
Effect: Enhanced emotional well-being through personalized advice, leading to reduced feelings of isolation and increased mental health awareness.

### Comprehensive Emotional Data Recording:
Cause: Systematic recording and organising of user input over time.
Effect: Users gain insights into their emotional patterns, fostering a proactive approach to mental health.

### Visualised Emotional Journey:
Cause: Graphical representations of emotional trends.
Effect: Users can easily track and understand their emotional progress, encouraging them to maintain positive mental health habits.

Positive Reflection Encouragement:
Cause: Daily check-ins focusing on positive reflections.
Effect: Boosted emotional resilience and self-awareness, leading to improved coping strategies in daily life.

### Compassionate Companion:
Cause: Guided support towards sustained emotional well-being.
Effect: Users feel supported and understood, which can be particularly beneficial for those lacking access to traditional mental health resources.

## Future Improvements
### Enhancing Features:
Integrate more comprehensive AI algorithms for deeper understanding and responses.
Incorporate features like mood-tracking, meditation guides, and stress-relief exercises.

### User Engagement:
Develop a community platform for shared experiences and support.
Organize virtual wellness workshops or webinars.

### Partnerships and Collaboration:
Partner with educational institutions, workplaces, and mental health organizations.
Collaborate with healthcare professionals for expert advice and validation.

### Marketing and Outreach:
Utilise social media and digital marketing to reach a wider audience.
Attend and present at tech and mental health conferences.

### Global Expansion:
Localise the app for different regions with multi-language support.
Understand and adapt to cultural differences in emotional well-being practices.

## Technical Architecture for Scaling
### Using PaLM API (Maker Suite):
The flexibility of Google's PaLM API allows for scaling up the AI component, managing larger datasets, and providing more nuanced responses.

### Cloud Infrastructure:
Leverage cloud computing for data storage and processing scalability.
Implement robust security measures for user data privacy.

### Modular Architecture:
Design the system with modular components to easily add new features.
Ensure backend and frontend scalability to handle increased traffic.

### API Integration:
Prepare for integrations with other health apps and platforms for a more holistic approach.
Use APIs for real-time data analysis and user feedback collection.

### Continuous Learning and Adaptation:
Implement machine learning algorithms that adapt and improve with more user data.
Regularly update the system based on user feedback and technological advancements.


## Link to Streamlit Web App
https://daily-ruok.streamlit.app/

## How to Use It?
### Step 1
Clone the repo by using
```
git init
git clone https://github.com/szeyu/Daily-RUOK.git
```

### Step 2
Install all the required package
(Recommend to create a new env to prevent collision of package)
```python
pip install -r requirements. txt
```

### Step 3
Open your anaconda prompt or python terminal

### Step 4
cd into the github folder directory

### Step 5
Run the following command
```
streamlit run dailyRUOK.py
```
