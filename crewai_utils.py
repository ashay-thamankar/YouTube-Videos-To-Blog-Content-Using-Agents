from crewai_tools import YoutubeChannelSearchTool
from crewai import Agent, LLM, Task, Crew, Process
import os
from dotenv import load_dotenv
load_dotenv()

def initialize_crew():
    """
    Initialize the Crew AI setup with the provided OpenAI API key.
    """
    # Initialize LLM with the provided API key
    llm = LLM(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))

    # Initialize YouTube tool
    yt_tool = YoutubeChannelSearchTool(allow_url_input=False)  # Topic-based search

    # Create agents
    blog_researcher = Agent(
        role='Blog researcher from YouTube Videos',
        goal='Get relevant content for the topic {topic} from YouTube',
        verbose=True,
        memory=True,
        backstory=(
            "Expert in understanding AI, Data Science, Machine Learning, "
            "and GenAI videos, providing detailed suggestions."
        ),
        tools=[yt_tool],
        llm=llm,
        allow_delegation=True
    )

    blog_writer = Agent(
        role='Blog Writer',
        goal='Narrate compelling tech stories based on the topic {topic}',
        verbose=True,
        memory=True,
        backstory=(
            "Skilled in simplifying complex topics, creating engaging narratives "
            "that educate and inspire."
        ),
        tools=[yt_tool],
        llm=llm,
        allow_delegation=False
    )

    # Define tasks
    research_task = Task(
        description=(
            "Extract detailed information for the topic {topic} from YouTube. "
            "Analyze the content and provide insights."
        ),
        expected_output="A comprehensive 3-paragraph report based on the topic's content.",
        tools=[yt_tool],
        agent=blog_researcher
    )

    write_task = Task(
        description=(
            "Summarize the content for the topic {topic} and create blog content."
        ),
        expected_output="A well-written blog summarizing the topic's content with references to related channels.",
        agent=blog_writer,
        async_execution=False,
        output_file='new-blog-post.md'
    )

    # Create crew
    crew = Crew(
        agents=[blog_researcher, blog_writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
        memory=True,
        cache=False,  # Disable caching to ensure fresh outputs for each input
        max_rpm=100,
        share_crew=True
    )

    return crew
