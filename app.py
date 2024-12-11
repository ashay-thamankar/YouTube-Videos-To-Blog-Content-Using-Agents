import streamlit as st
from crewai_utils import initialize_crew

# Streamlit App
st.title("YouTube to Blog Generator using Crew AI")
st.subheader("Convert YouTube topics into insightful blogs!")

# Input fields for API Key and topic
# api_key = st.text_input("Enter your OpenAI API Key:", type="password")
topic_to_search = st.text_input("Enter the topic to search on YouTube:", "AI, Data Science, and GenAI advancements")

# Button to trigger blog generation
if st.button("Generate Blog"):
    if not topic_to_search:
        st.warning("The topic field cannot be empty.")
    else:
        st.info("Processing... Please wait while the blog is generated.")
        try:
            crew = initialize_crew()  # Pass the API key dynamically
            result = crew.kickoff(inputs={"topic": topic_to_search})

            # Display the blog content
            if result:
                st.success("Blog Generated Successfully!")
                st.markdown(result, unsafe_allow_html=True)  # Render blog as Markdown
            else:
                st.warning("Blog generation succeeded, but no output was returned.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
