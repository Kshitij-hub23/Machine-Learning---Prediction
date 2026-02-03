Shroff, Kshitij Sandeep, 22408587

Project Title: Football Players Analyser

GitLab Repository: https://mygit.th-deg.de/ks23587/ai-assistant-project-kshitij-shroff

Wiki: https://mygit.th-deg.de/ks23587/ai-assistant-project-kshitij-shroff/-/wikis/home

Screencast: https://drive.google.com/file/d/1EOxLvoMaOLGVv1Hy-AnE-kRghM5JnQce/view?usp=sharing

Project Description: This project analyzes football player data from the FIFA 21 dataset and provides two main components. First, a prediction app estimates a player’s market value, overall rating, and potential based on key attributes. This includes an Augmented Predictor that incorporates commercial metrics, such as Instagram followers, to estimate a player's marketability alongside technical skill. Second, a Streamlit chatbot lets users ask natural language questions about players and clubs, answering directly from the FIFA 21 dataset using both text and voice interaction. The chatbot can listen to spoken queries via speech recognition and respond with synthesized speech in addition to on‑screen text.

Installation:

Python version – 3.12.x in a virtual environment is recommended so that audio libraries work reliably.

Required packages: pip install pandas pip install numpy pip install matplotlib pip install scikit-learn pip install streamlit pip install SpeechRecognition pip install PyAudio pip install gTTS pip install joblib

Data: The project uses the FIFA 21 complete player dataset, which contains around 19,000 players and over 100 attributes. It also utilizes an augmented version of this data to include social media metrics for commercial value analysis. Dataset link: https://www.kaggle.com/datasets/stefanoleone992/fifa-21-complete-player-dataset

Basic Usage: Prediction App: Enter player characteristics such as age, height, weight, preferred foot, pace, shooting, passing, dribbling, defending, physicality, stamina, and strength. The app uses trained regression models to predict the player’s market value, overall rating, and potential rating. The Augmented Model specifically allows users to adjust a "Fame" slider (Instagram followers) to see how commercial popularity impacts market valuation compared to pure on-pitch performance.

Football Chatbot: Type questions such as “Messi stats”, “top players for pace” or “random player”. The chatbot uses keyword rules and fuzzy name matching to find players or clubs in the FIFA 21 dataset. It returns a fixed set of core attributes or squad averages in a conversational format. A “🎙️ Start Voice Input” button allows users to speak queries; speech recognition turns the spoken input into text, and the reply is both shown in the chat and can be spoken aloud using the text‑to‑speech button.