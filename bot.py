
import os
# import json 
# from langchain.memory import ConversationSummaryMemory, ChatMessageHistory , ConversationBufferWindowMemory
# from langchain.chat_models import ChatOpenAI
# from langchain.prompts.chat import (
#     ChatPromptTemplate,
#     PromptTemplate,
#     SystemMessagePromptTemplate,
#     AIMessagePromptTemplate,
#     HumanMessagePromptTemplate,
# )
# from langchain.chains import LLMChain , ConversationChain
# from langchain.chains.question_answering import load_qa_chain
# from langchain.llms import OpenAI
# from langchain.prompts import PromptTemplate
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.memory import ConversationBufferMemory

# from langchain.memory import CassandraChatMessageHistory



os.environ["OPENAI_API_KEY"] = "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"


# gpt3 = ChatOpenAI(model_name="gpt-3.5-turbo")

# template = """
#         Context : Vedant Garode 
#         Pune | +918149336088 | Vedantgarode11@gmail.com
#         Summery
#         •	Profound expertise in JAVA, PYTHON, JAVASCRIPT, and SQL, coupled with a strong background in design and integration. Adept at employing intuitive problem-solving skills to develop efficient solutions.
#         •	Passionate about conceptualizing and launching novel projects. Proven ability to bridge the gap between business requirements and technical implementations, ensuring seamless and effective outcomes.
#         •	Aspiring to kickstart my professional journey as an entry-level software engineer.
#         Skills & Abilities
#         •	Programming Languages: C++, Java, Python, , JavaScript
#         •	Database: SQL, PL/SQL, MongoDB
#         •	Object-Oriented Programming (OOPs)
#         •	Back-end Web Development: PHP, Firebase
#         •	Blockchain Development: EtherJS , Metamask	•	Data Structures and Algorithms (DSA)
#         •	Cloud Services: Google Cloud
#         •	Front-end Web Development: ReactJS, HTML, JavaScript, CSS
#         •	Project Management
#         •	Collaboration Platform: Git , Github , Google Collab
#         Education
#         B.E. (BACHELOR OF ENGINEERING) ( 2019 - 2023 )
#         •	DY Patil Institute Of Technology , Pimpri ,Pune
#         •	Major - Computer Engineering	•	BE Aggregate - 9.35
#         •	Minor - Data Science Honors
#         HIGH SCHOOL  (2018 - 2019 )
#         •	Sir Parshurambhau College , Pune
#         •	General Science (PCM)	•	HSC Aggregate - 76.15%
#         MIDDLE SCHOOL  ( 2016 - 2017 )
#         •	Narayandas Laddha High School , Amravati	•	SSC Aggregate – 87.80
#         Projects
#         COMMUNOMY (COMMUNITY DRIVEN ECONOMY) (10/2022 - 06/2023)
#         •	Designed and developed a web application leveraging the potential of decentralized finance (DeFi) to empower individuals with early financial freedom. 
#         •	ReactJs , Firebase , JavaScript ,EtherJs

#         COMPANY MANAGEMENT  (06/2023 - 10/2023)
#         •	The project demonstrated strong problem-solving skills, creativity, and a deep understanding of computer vision and artificial intelligence concepts.
#         •	PHP ,MySQL ,HTML , CSS ,JS.

#         MEDIA CONTROLLER USING HAND GESTURE. 
#         •	The "Hand Gestures Media Player Control" project aims to develop an interactive and innovative media player application that allows users to control various functions using hand gestures.
#         •	Python , OpenCV  , Pandas .
#         Experience
#         CODING INTERN | TURITO | JAN 2023 – MAY 2023
#         •	During my tenure as a Java Coding and Assessment Instructor, I designed and developed a comprehensive curriculum that effectively taught students the fundamentals of Java programming, including Core Java, Java Swing, and JavaFX. 
#         •	By creating engaging instructional materials, coding exercises, and assessments, I was able to facilitate effective learning and practice among the students.
#         MACHINE LEARNING INTERN | SUVIDHA FOUNDATION  | JAN 2022 – MAY 2022
#         •	Utilized Convolutional Neural Network (CNN) architecture pretrained on sports dataset M1.
#         •	Designed and implemented a video summarization model to extract crucial information from lengthy videos.Successfully condensed videos into smaller clips while retaining essential content.
#         •	Demonstrated strong skills in deep learning, transfer learning, and video processing.

#         CERTIFICATES
#         ARCHITECTING WITH GOOGLE COMPUTE ENGINE (SPECIALIZATION) 
#         coursera.org/verify/specialization/9VE8MBX98VBZ
#         COMPLETE PYTHON BOOTCAMP
#         https://www.udemy.com/certificate/UC-9d669373-748f-43f4-a317- 110dbe345fa2/
#         C++ BOOTCAMP BASIC TO ADVANCE
#         https://www.udemy.com/certificate/UC-f73e5b24-b8dd-4e58-b3b0- 91ffeb1384cf/ 

#         LANGUAGES
#         ENGLISH 				 
#         Full Professional Proficiency             
#         HINDI
#         Professional Working Proficiency
#                                                             MARATHI 
#         Native or Bilingual Proficiency

#         External Links 
#         •	LINKDN : linkedin.com/in/vedant-garode-140b8a1b9
#         •	GITHUB : https://github.com/vedantgarode
#         •	LEETCODE : https://leetcode.com/spartex007/
#         •	PORTFOLIO : vedantgarode.github.io/Portfolio/
#         History :{chat_history} 
#         Profile: {human_input} 
#         Nexamind :""" 
# prompt = PromptTemplate(
#     input_variables=["chat_history", "human_input"], template=template
# )
# memory = ConversationBufferWindowMemory(k = 5 , memory_key="chat_history", input_key="human_input")

# chain = LLMChain(llm=gpt3,memory=memory, prompt=prompt)

# def conversation(human_input):
#     query = human_input
#     print (memory.load_memory_variables({}))
#     return chain.predict(human_input=query ,chat_history =memory.load_memory_variables({}) )  


# print(conversation("Hello"))






import openai

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

print(response['choices'][0]['message']['content'])