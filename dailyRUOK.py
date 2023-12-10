import streamlit as st
import os
import random
import google.generativeai as palm


# palm.configure(api_key=os.environ['API_KEY'])
palm.configure(api_key=st.secrets["API_KEY"])
# palm.configure(api_key="AIzaSyDQHRGycDrJhtQb023BjqybjKAzaj0yZMQ")

# Function to generate a random response based on user input
def generate_response(mood_score):
    responses = [
        "Great to hear that you're feeling fantastic!",
        "You're doing well! Keep up the positive energy.",
        "If you're feeling down, remember that tomorrow is a new day.",
        "Your well-being matters. Take some time for self-care.",
        "Sending you positive vibes! Remember, you're not alone.",
    ]
    if mood_score >= 8:
        return random.choice(responses[:2])
    elif 5 <= mood_score <= 7:
        return random.choice(responses[2:4])
    else:
        return random.choice(responses[4:])

# Function to call PaLM API by MakerSute
def call_palm_api(user_data):
    # Customize the data you send to the PaLM API based on your requirements
    prompt = f"Yesterday, I felt {user_data['mood_score']} and the best thing that happened was: {user_data['positive_experience']}. "
    prompt += f"I faced challenges/concerns: {user_data['challenges_concerns']}. "
    prompt += f"Reflection on well-being: {user_data['self_reflection']}. "
    prompt += f"Gratitude: {user_data['gratitude']}. "
    prompt += f"Physical well-being: {user_data['physical_wellbeing']}. "
    prompt += f"Sleep quality: {user_data['sleep_quality']}. "
    prompt += f"Stress level: {user_data['stress_level']}. "
    prompt += f"Daily goals: {user_data['daily_goals']}. "
    prompt += f"Social connections: {user_data['social_connections']}. "
    prompt += f"Mindfulness/relaxation: {user_data['mindfulness_relaxation']}. "
    prompt += f"Accomplishments: {user_data['accomplishments']}."
    
    prompt += "Now act as a counselor and give me compliment / praises / healing / advices / motivation"
    
    # Make a POST request to the PaLM API with the extended prompt
    response = palm.generate_text(prompt=prompt)
    
    # Return the result from the API
    return response.result

    response = palm.generate_text(prompt)
    return response.result

# Streamlit app
def main():
    st.title("Daily RUOK System")
    
   # User input section
    st.header("How are you feeling today?")
    mood_score = st.slider("Rate your mood (1-10):", key="mood_score", min_value=1, max_value=10, step=1)
    positive_experience = st.text_input("What was the best thing that happened yesterday?", key="positive_experience")

    # Additional questions
    challenges_concerns = st.text_input("Did you face any challenges or concerns yesterday that you would like to share?", key="challenges_concerns")
    self_reflection = st.text_area("Take a moment to reflect on your overall well-being. Is there anything specific on your mind?", key="self_reflection")
    gratitude = st.text_input("What are you grateful for today?", key="gratitude")
    physical_wellbeing = st.text_area("How would you describe your physical well-being today?", key="physical_wellbeing")
    sleep_quality = st.slider("How would you rate the quality of your sleep last night?", key="sleep_quality", min_value=1, max_value=10, step=1)
    stress_level = st.slider("On a scale of 1 to 10, how stressed do you feel today?", key="stress_level", min_value=1, max_value=10, step=1)
    daily_goals = st.text_area("Do you have any specific goals or intentions for today?", key="daily_goals")
    social_connections = st.text_area("Did you engage with friends or family yesterday? How did it make you feel?", key="social_connections")
    mindfulness_relaxation = st.text_area("Have you taken any time for mindfulness or relaxation today?", key="mindfulness_relaxation")
    accomplishments = st.text_area("What is one thing you accomplished yesterday that you're proud of?", key="accomplishments")

    # Trigger API call when user clicks the "Submit" button
    if st.button("Submit"):
        # Prepare data for the PaLM API call (customize as needed)
        user_data = {
            "mood_score": mood_score,
            "positive_experience": positive_experience,
            "challenges_concerns": challenges_concerns,
            "self_reflection": self_reflection,
            "gratitude": gratitude,
            "physical_wellbeing": physical_wellbeing,
            "sleep_quality": sleep_quality,
            "stress_level": stress_level,
            "daily_goals": daily_goals,
            "social_connections": social_connections,
            "mindfulness_relaxation": mindfulness_relaxation,
            "accomplishments": accomplishments,
        }
        
        # Call PaLM API and get the response
        palm_response = call_palm_api(user_data)

        # Display the API response (customize as needed)
        st.header("PaLM API Response:")
        st.write(palm_response)

    # Generate and display response
    st.header("Daily RUOK Response:")
    response = generate_response(mood_score)
    st.write(response)

    # Display emotional well-being graph (placeholder)
    st.header("Emotional Well-being Over Time:")
    # Include code for plotting graphs or visualizations based on user's historical data

if __name__ == "__main__":
    main()


