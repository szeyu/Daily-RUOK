import streamlit as st
import os
import datetime
import random
import google.generativeai as palm
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# palm.configure(api_key=os.environ['API_KEY'])
palm.configure(api_key=st.secrets["API_KEY"])

# past record of emotional well-being score
past_scores = [60,76,83,80,75]

# Generate smoothed line graph
def smooth_line_graph(scores):
    x = np.arange(len(scores))
    x_smooth = np.linspace(x.min(), x.max(), 300)
    spl = make_interp_spline(x, scores, k=3)
    y_smooth = spl(x_smooth)
    return x_smooth, y_smooth

def displayGraph():
    # Display the original and smoothed line graphs
    x_smooth, y_smooth = smooth_line_graph(past_scores)

    fig, ax = plt.subplots()
    ax.plot(x_smooth, y_smooth, label="Smoothed Line", color='blue')
    ax.scatter(range(len(past_scores)), past_scores, label="Original Scores", color='red')
    ax.set_xlabel("Day")
    ax.set_ylabel("Emotional Well-being Score")

    # Display the plot using Streamlit
    st.pyplot(fig)

# Function to generate a random response based on user input
def generate_response(mood_score):
    responses = [
        "Great to hear that you're feeling fantastic! 😊",
        "You're doing well! Keep up the positive energy. 👍",
        "If you're feeling down, remember that tomorrow is a new day. 🌈",
        "Your well-being matters. Take some time for self-care. 🌺",
        "Sending you positive vibes! Remember, you're not alone. 🌟",
    ]
    if mood_score >= 8:
        return random.choice(responses[:2])
    elif 5 <= mood_score <= 7:
        return random.choice(responses[2:4])
    else:
        return random.choice(responses[4:])

# Function to call PaLM API by MakerSute
def call_palm_api(user_data, objective):
    # Customize the data you send to the PaLM API based on your requirements
    # Create a new prompt based on the sequence of user_data
    prompt = ""
    for key, value in user_data.items():
        if value == "":
            continue
        prompt += f"{key.replace('_', ' ').capitalize()}: {value}. "
    
    prompt += objective
    
    # Make a POST request to the PaLM API with the extended prompt
    response = palm.generate_text(prompt=prompt)
    
    # Return the result from the API
    return response.result

# Streamlit app
def main():
    st.title("Daily RUOK System 😊")
    
   # User input section
    st.header("How are you feeling today? 🌟")
    mood_score = st.slider("Rate your mood (1-10):", key="mood_score", min_value=1, max_value=10, step=1)
    sleep_quality = st.slider("How would you rate the quality of your sleep last night? (1-10)", key="sleep_quality", min_value=1, max_value=10, step=1)
    stress_level = st.slider("On a scale of 1 to 10, how stressed do you feel today?", key="stress_level", min_value=1, max_value=10, step=1)
    physical_wellbeing = st.slider("How would you describe your physical well-being today? (1-10)", key="physical_wellbeing", min_value=1, max_value=10, step=1)
    mindfulness_relaxation = st.slider("Have you taken any time for mindfulness or relaxation today? (1-10)", key="mindfulness_relaxation", min_value=1, max_value=10, step=1)

    # Get the current day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    current_day = datetime.datetime.now().weekday()

    # Define fixed questions for each day
    questions_by_day = {
        0: "positive_experience",
        1: "self_reflection",
        2: "daily_goals",
        3: "accomplishments",
        4: "challenges_concerns",
        5: "gratitude",
        6: "social_connections"
    }

    # Get the question for the current day
    questions_for_today = questions_by_day.get(current_day, "")

    # Display the question for the current day
    st.write(f"{questions_for_today.capitalize()}:")

    # Display other questions using sliders
    positive_experience = st.text_input("What was the best thing that happened yesterday? 🌈", key="positive_experience") if questions_for_today == "positive_experience" else ""
    challenges_concerns = st.text_input("Did you face any challenges or concerns yesterday that you would like to share? 💪", key="challenges_concerns") if questions_for_today == "challenges_concerns" else ""
    self_reflection = st.text_area("Take a moment to reflect on your overall well-being. Is there anything specific on your mind? 🤔", key="self_reflection") if questions_for_today == "self_reflection" else ""
    gratitude = st.text_input("What are you grateful for today? 🙏", key="gratitude") if questions_for_today == "gratitude" else ""
    daily_goals = st.text_area("Do you have any specific goals or intentions for today? 🎯", key="daily_goals") if questions_for_today == "daily_goals" else ""
    social_connections = st.text_area("Did you engage with friends or family yesterday? How did it make you feel? 👫", key="social_connections") if questions_for_today == "social_connections" else ""
    accomplishments = st.text_area("What is one thing you accomplished yesterday that you're proud of? 🚀", key="accomplishments") if questions_for_today == "accomplishments" else ""


    # Trigger API call when user clicks the "Submit" button
    if st.button("Submit"):
        # Prepare data for the PaLM API call (customize as needed)
        user_data = {
            "mood_score": mood_score,
            "sleep_quality": sleep_quality,
            "stress_level": stress_level,
            "physical_wellbeing": physical_wellbeing,
            "mindfulness_relaxation": mindfulness_relaxation,

            "positive_experience": positive_experience,
            "challenges_concerns": challenges_concerns,
            "self_reflection": self_reflection,
            "gratitude": gratitude,
            "daily_goals": daily_goals,
            "social_connections": social_connections,
            "accomplishments": accomplishments,
        }
        
        # Call PaLM API and get the response
        palm_response = call_palm_api(user_data, "Now act as a counselor and give me motivtion and advice")
        emotionalScore = call_palm_api(user_data, "Rate my emotional well-being in a score of 100. I just want you to output the number only")
        past_scores.append(emotionalScore)

        # Display the API response (customize as needed)
        st.header("Your Score Today:")
        st.subheader(emotionalScore)

        # Display the API response (customize as needed)
        st.header("PaLM API Response:")
        st.write(palm_response)

    # Generate and display response
    st.header("Daily RUOK Response:")
    response = generate_response(mood_score)
    st.write(response)

    # Display emotional well-being graph (placeholder)
    st.header("Emotional Well-being Over Time:")
    # plotting graphs or visualizations based on user's historical data
    displayGraph()

if __name__ == "__main__":
    main()


