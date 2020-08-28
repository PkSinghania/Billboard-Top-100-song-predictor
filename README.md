# Billboard-Top-100-song-predictor
The model predicts whether a song will come into the billboard hot-100 chart or not.
We have used the spotfy, billboard and lyrics genius APIS for scrapping the data.
We are extracting the audio features using Spotify APi, the hot-100 chart of billboard for 20 years using billboard api and lyrics of song using lyrics genius api. 
We have used multithreading to speed up the process. 
Firstly, the model is trained on audio features only. The accuracy was 79% but the f1- score was not good.
Then we used the lyrics also to train the model which have increased the f1-score a lot on validation set.
