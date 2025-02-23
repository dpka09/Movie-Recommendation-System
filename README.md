**Model deploy using Streamlit on Render Platform**

In this project I have implemented a content based movie recommender system. The algorithm recommends products that are similar to the ones a user has preferred in the past. This similarity (generally cosine similarity) is computed from the data we have about the items as well as the past preferences of the user.

**How it works:**

![](https://miro.medium.com/v2/resize:fit:792/1*P63ZaFHlssabl34XbJgong.jpeg)

**Live Demo**


https://github.com/user-attachments/assets/b84517ce-726e-4a4a-bbdb-e0c1d218d958


**Content Based Filtering**

They suggest similar items based on a particular item. This filter applies item metadata, such as genre, director, description, actors, etc. for films in recommending these items. The fundamental idea behind such recommender systems is that if someone liked a particular item, he or she will like an item with a similar nature.

**How to get the API key for images?**
Create an account in https://www.themoviedb.org/, click on the API link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your API sidebar once your request is approved.

![](https://user-images.githubusercontent.com/31500911/143419982-2d726687-84d6-4616-8d09-833f732c92b2.png)


**Similarity Score :**
How does it decide which item is most similar to the item user likes? Here we use the similarity scores.
It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

![similarity score](https://github.com/user-attachments/assets/d34ea079-88b0-44ca-8f57-562712b8a6f1)


**How Cosine Similarity works? :**
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

![](https://user-images.githubusercontent.com/31500911/143417796-8602832b-aac9-4f4f-b930-b753dc050981.png)

**Sources of the datasets :**
I have used the TMDB 5000 movies dataset to build the model

You can collect dataset from https://www.kaggle.com/tmdb/tmdb-movie-metadata



