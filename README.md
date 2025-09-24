# Information Systems Analysis and Design - A Sharing Platform for Questions and Solutions for Students
## Activity Diagram and Use-Case Diagram
### General description of the system:
As part of a course in information systems analysis and design, we created a collaborative system designed for students from all academic institutions that allows for the uploading and sharing of solutions to questions, homework assignments, and tests.

The goal of the system is to provide an efficient and convenient platform for sharing knowledge, raising questions, and receiving solutions in a fast and focused manner.

| Topic                               | Current Situation                                                                 | With the System                                                                                                  |
|-------------------------------------|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Registration to the system          | There is no system to register to                                                 | Registration will be required to use the system. As part of the process, the student will provide their academic institution and connect it for transferring course information. |
| Uploading questions and solutions   | Sending messages in WhatsApp groups, emails to lecturers, responses only at certain times | A centralized database of questions and solutions within the system.                                              |
| Search in the system                | Searching on Google, searching in WhatsApp by topic                               | Questions will be organized by categories and topics. Search will be possible using keywords, topic, or upload date. |
| Automatic notifications on uploads  | Students need to ask others if they solved the same exercise/test                 | The student who uploaded a question will receive a personal notification for each solution added. Additionally, students can set personal preferences for notifications (e.g., by specific course). |
| AI-based system for inconsistency detection | It is not possible to know if there are contradictions between answers, manual comparison is required | The system will detect contradictions between solutions and alert both students and the system administrator (who will ensure one correct answer). It will also detect spam in uploaded questions and raise alerts accordingly. |

### Processes (in Hebrew):
#### 1. Asking questions and solutions - Current status: Sending messages in WhatsApp groups and emailing the lecturer:
<img width="913" height="894" alt="image" src="https://github.com/user-attachments/assets/c8e69408-5b98-4709-b152-efb9312364cb" />

#### 2. Search the system - the current situation: Search for the solution on Google:
<img width="681" height="1226" alt="image" src="https://github.com/user-attachments/assets/f689a8ed-5f7b-4553-bc9b-bf8bb88f57e6" />

#### 3. Automatic notification of uploading solutions and questions - Current situation: Checking with a friend by phone to see if he has the solution:
<img width="692" height="1042" alt="image" src="https://github.com/user-attachments/assets/4ca4fc75-e4ce-43e6-b20b-3da11f74da31" />

#### 4. Artificial Intelligence System for Identifying Inconsistencies - Current Status: Comparing Solutions Between Students:
<img width="904" height="1109" alt="image" src="https://github.com/user-attachments/assets/9af1fccc-05c2-4fcb-b256-49a30f59df28" />

### Objectives of Establishing the Information System:

1. Students will have access to all information from past courses, exercises, exams, etc.  
2. Information will be shared easily and quickly among students.  
3. Student learning will improve through an AI-based information quality rating system.  
4. The response time to students' questions will be significantly reduced.  
5. Students will be able to search for solutions in a more accurate and focused manner.

### Use Case Diagram (In Hebrew):
<img width="842" height="725" alt="image" src="https://github.com/user-attachments/assets/ffed0355-e0e2-46dd-90d3-bfb1d8ef1844" />

Explanation of the external system - a system of the academic institution itself that includes information on all courses (such as AFEKANET), feeds the new information system with course data.


## Data-Flow Diagram and Transactions
### Entity Glossary:
| Entities            | Functions                                                                 | Complex Functions                                           | Databases                           | Timers                                                         |
|----------------------|---------------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------|---------------------------------------------------------------|
| E1 - Student         | P6 - Retrieve student courses and register                                | P1 - Registration to the system                            | DS1 - Students                       | T1 - Trigger notification on question/solution upload          |
| E2 - System Admin    | P2 - Upload questions and solutions                                       | P2 - Upload questions and solutions                        | DS2 - Questions and solutions         | T2 - Trigger inconsistency detection algorithm between answers |
| E3 - External System | P3 - Search questions and solutions                                       | P3 - Search questions and solutions                        | DS3 - External course database        |                                                               |
|                      | P4 - Automatic notification on uploaded solutions and questions           | P4 - Automatic notification on uploaded solutions/questions | DS4 - Requests for questions/solutions |                                                               |
|                      | P5 - AI system for detecting inconsistencies in answers                   | P5 - AI system for detecting inconsistencies in answers     |                                      |                                                               |

### DFD diagrams (in Hebrew):
<img width="950" height="536" alt="image" src="https://github.com/user-attachments/assets/56dba961-5b34-4468-8595-289e8d069d91" />

<img width="940" height="450" alt="image" src="https://github.com/user-attachments/assets/52c64263-71eb-4a91-95f8-7c7df95a480f" />

<img width="940" height="492" alt="image" src="https://github.com/user-attachments/assets/5d242878-5051-4ac1-8d9e-e909ffb8eb28" />

<img width="940" height="496" alt="image" src="https://github.com/user-attachments/assets/30157241-fc7b-4700-90d1-c2253e89bc8c" />

<img width="940" height="501" alt="image" src="https://github.com/user-attachments/assets/b5aa0c46-0c2c-4345-87a9-af435156bcd1" />

<img width="940" height="450" alt="image" src="https://github.com/user-attachments/assets/6d1b0225-aa33-4598-906c-604c02bdae3d" />

<img width="940" height="426" alt="image" src="https://github.com/user-attachments/assets/69be4efe-272a-4e44-b975-80de96e7b9fb" />


## ERD:
<img width="839" height="1055" alt="image" src="https://github.com/user-attachments/assets/c5e9281e-7d9c-4a2b-84aa-3653d7e4729a" />

## Class Diagram:
<img width="963" height="599" alt="image" src="https://github.com/user-attachments/assets/f459a201-db82-4bc0-b0af-8a66a3e60747" />

### Encapsulation Considerations in the Project:

In our project, we worked with the approach where the attributes of each class are **private**, and the methods are **public**, in order to:  

- Protect sensitive data, e.g., passwords and user IDs.  
- Ensure correct logical relationships such as aggregation, composition, and inheritance.  
- Allow flexibility for future changes in the information system without breaking it.  

By working this way, we prevent the greatest threat to the information system (the user) from entering values that could crash the system.  
For example, the method `add_alert()` can validate whether a new alert is legitimate before adding it, which prevents errors.  

