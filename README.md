# Daily-RUOK
## Project for KitaHack 2024

**Team: AI Cooking**
- Sim Sze Yu
- Jonathan Siew
- Sayyid Syamil

## Sustainable Development Goal 3.4 (SDG 3.4) 
*By 2030, reduce by one third premature mortality from non-communicable diseases through prevention and treatment and promote mental health and well-being.*

## Overview
Achieving Sustainable Development Goal 3 (SDG 3) - Good Health and Well-being is crucial for fostering global emotional well-being. Prioritizing quality healthcare not only impacts physical health but also nurtures positive emotional states. The "Daily RUOK" system aligns seamlessly with SDG 3 by promoting emotional self-awareness and resilience.

## Specifications
1. **Personalised Emotional Support**
   - Daily RUOK provides users with personalized responses, including advice, compliments, and motivational messages tailored to their daily input.

2. **Comprehensive Emotional Data Recording**
   - The system records and organizes user input over time, creating a comprehensive emotional well-being profile for each individual.

3. **Visualised Emotional Journey**
   - Intuitive graphical representations visually illustrate the user's emotional journey, allowing users to track patterns and observe progress over time.

4. **Positive Reflection Encouragement**
   - Focusing on daily check-ins and encouraging positive reflections, the system actively promotes emotional self-awareness and resilience.

5. **Compassionate Companion**
   - Acting as a compassionate companion, the "Daily RUOK" system guides individuals toward sustained emotional well-being and personal growth.

## Google Technology Used
- **PaLM API (Maker Suite)**
  - Google products used to prototype and build generative AI applications.

## Specific Issues Faced:
1. **Interpreting Emotional Tone**
   - Developing an algorithm that accurately discerns the emotional context from text inputs.

2. **Generating Appropriate Responses**
   - Creating a response mechanism that is relevant to the user's emotional state and offers constructive support or advice.

3. **Scalability**
   - Ensuring the solution can handle a large number of users simultaneously without degradation in performance.

## Addressing the Challenge:
1. **Algorithm Development**
   - Utilizing Natural Language Processing (NLP) techniques to analyze user input.
   - Implementation of sentiment analysis using libraries like Palm API for deeper contextual understanding.

2. **Response Generation**
   - Crafting a response generator that uses emotional analysis to create personalized messages.
   - Integrating pre-defined response templates with dynamic content generation.

3. **User Interface Integration**
   - Seamlessly integrating the backend emotional analysis and response system with the user interface.
   - Choosing a responsive and intuitive frontend framework (Streamlit) that communicates effectively with the backend.

## Project’s Impact Using Cause and Effect
- **Personalised Emotional Support**
  - *Cause*: Users receive tailored responses based on their daily input.
  - *Effect*: Enhanced emotional well-being through personalized advice, leading to reduced feelings of isolation and increased mental health awareness.

- **Comprehensive Emotional Data Recording**
  - *Cause*: Systematic recording and organizing of user input over time.
  - *Effect*: Users gain insights into their emotional patterns, fostering a proactive approach to mental health.

- **Visualised Emotional Journey**
  - *Cause*: Graphical representations of emotional trends.
  - *Effect*: Users can easily track and understand their emotional progress, encouraging them to maintain positive mental health habits.

- **Positive Reflection Encouragement**
  - *Cause*: Daily check-ins focusing on positive reflections.
  - *Effect*: Boosted emotional resilience and self-awareness, leading to improved coping strategies in daily life.

- **Compassionate Companion**
  - *Cause*: Guided support towards sustained emotional well-being.
  - *Effect*: Users feel supported and understood, particularly beneficial for those lacking access to traditional mental health resources.

## Future Improvements
1. **Enhancing Features**
   - Integrate more comprehensive AI algorithms for deeper understanding and responses.
   - Incorporate features like mood-tracking, meditation guides, and stress-relief exercises.

2. **User Engagement**
   - Develop a community platform for shared experiences and support.
   - Organize virtual wellness workshops or webinars.

3. **Partnerships and Collaboration**
   - Partner with educational institutions, workplaces, and mental health organizations.
   - Collaborate with healthcare professionals for expert advice and validation.

4. **Marketing and Outreach**
   - Utilize social media and digital marketing to reach a wider audience.
   - Attend and present at tech and mental health conferences.

5. **Global Expansion**
   - Localize the app for different regions with multi-language support.
   - Understand and adapt to cultural differences in emotional well-being practices.

## Technical Architecture for Scaling
- **Using PaLM API (Maker Suite)**
  - The flexibility of Google's PaLM API allows for scaling up the AI component, managing larger datasets, and providing more nuanced responses.

- **Cloud Infrastructure**
  - Leverage cloud computing for data storage and processing scalability.
  - Implement robust security measures for user data privacy.

- **Modular Architecture**
  - Design the system with modular components to easily add new features.
  - Ensure backend and frontend scalability to handle increased traffic.

- **API Integration**
  - Prepare for integrations with other health apps and platforms for a more holistic approach.
  - Use APIs for real-time data analysis and user feedback collection.

- **Continuous Learning and Adaptation**
  - Implement machine learning algorithms that adapt and improve with more user data.
  - Regularly update the system based on user feedback and technological advancements.

## Link to Streamlit Web App
[Daily RUOK Web App](https://daily-ruok.streamlit.app/)

## How to Use It?
**Step 1**
Clone the repo by using:
```bash
git init
git clone https://github.com/szeyu/Daily-RUOK.git
```

**Step 2**
Install all the required packages. It is recommended to create a new virtual environment to prevent package collisions. Run the following command:
```bash
pip install -r requirements.txt
```

**Step 3**
Open your Anaconda prompt or Python terminal.

**Step 4**
Change directory (cd) into the GitHub folder directory.

**Step 5**
Run the following command to start the application:
```bash
streamlit run dailyRUOK.py
```
Now, you should be able to access and use the "Daily RUOK" system through the provided Streamlit web app link.
