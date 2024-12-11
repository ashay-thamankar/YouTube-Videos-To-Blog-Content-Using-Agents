# 🎥 YouTube to Blog Generator using Crew AI ✍️  

Effortlessly transform YouTube topics into insightful, engaging blog posts using the power of **Crew AI**! This application combines Streamlit for an intuitive UI with Crew AI for seamless task delegation, enabling users to generate blog content from a single topic.  

---

## ✨ Features  
- **Topic-Based Input**: Just provide a topic of interest, and let the app handle the rest.  
- **Automated Research**: Uses AI to extract relevant content from YouTube.  
- **Blog Writing**: Creates engaging blog posts based on YouTube content.  
- **End-to-End Workflow**: Combines research and writing tasks for a complete blog creation pipeline.  

---

## 🛠️ Tech Stack  

### Frontend  
- **Streamlit**: Simple and interactive UI to input topics and display results.  

### Backend  
- **Python**: Core programming language.  
- **Crew AI**: Framework for task orchestration and intelligent agent communication.  
- **YouTube Channel Search Tool**: Fetches relevant YouTube content based on topics.  

---

## 🔎 How It Works?  

1. **Input a Topic**: Users enter a topic in the UI (e.g., *AI advancements*).  
2. **AI-Driven Research**:  
   - An intelligent agent searches YouTube for relevant videos.  
   - Extracts meaningful insights from the video content.  
3. **Blog Generation**:  
   - Another agent summarizes and creates a well-written blog post based on the extracted insights.  
4. **Output**: The blog is displayed in markdown format, ready for use.  

---

## 🛠️ How to Run?  

### Steps  

1. **Clone the Repository** 🗂️  
   ```bash  
   git clone   
   cd  
   ```  

2. **Create a Conda Environment** 🐍  
   ```bash  
   conda create -n agents python=3.10 -y  
   conda activate agents  
   ```  

3. **Install the Requirements** 📦  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. **Set Environment Variables** 🔑  
   Create a `.env` file in the root directory with your OpenAI credentials:  
   ```ini  
   OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  
   ```  

5. **Start the Application** 🖥️  
   ```bash  
   streamlit run app.py  
   ```  

6. **Access the Application** 🌐  
   Open your browser and visit:  
   ```plaintext  
   http://localhost:5000  
   ```  

---

## 🖼️ Application UI  

- **Input Section**:  
   A clean text field to enter your desired topic for research.  
- **Blog Display**:  
   Outputs the generated blog in markdown format for easy copying or publishing.  

---

## 🚀 Future Enhancements  
- Integration with multiple blog publishing platforms.  
- Advanced content styling and formatting.  
- Support for multilingual blog generation.  

---

## 📄 License  
This project is licensed under the MIT License.  

---

## 💻 Author  
**Ashay Thamankar**  
- [GitHub](https://github.com/ashay-thamankar)  
- [LinkedIn](https://www.linkedin.com/in/ashay-thamankar)  

---

### 🎉 Happy Blogging with AI! 🚀  
