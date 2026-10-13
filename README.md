# Machine Learning Projects

Notebooks from working through classical machine learning, deep learning and the Python data stack: implementations from scratch, library implementations, and small end-to-end projects.

Larger projects have their own repositories:

- [t5-text-summarizer](https://github.com/anirudhverma33/t5-text-summarizer): fine-tuned T5 for dialogue summarisation, served with FastAPI
- [rag-pipeline](https://github.com/anirudhverma33/rag-pipeline): a retrieval-augmented generation pipeline with LangChain, ChromaDB and a Groq-hosted LLM

## Projects

Results are the values printed in the saved notebook outputs, on each notebook's held-out test split.

| Project | Task | Models | Result |
|---|---|---|---|
| [CreditWise loan approval](<Minor Projects/Minor Project 1 (CreditWise Loan System)>) | Binary classification, 1,000 applications | Logistic regression, KNN, Gaussian Naive Bayes; imputation, encoding, scaling, feature engineering | Logistic regression after feature engineering: accuracy 0.88, precision 0.78, recall 0.84, F1 0.81 |
| [NovaGen health classification](<Bagging and Boosting/Project>) | Healthy/unhealthy classification, 9,800 records | Logistic regression, KNN, Random Forest, Gradient Boosting, soft voting | Random Forest: accuracy 0.938, recall 0.959 |
| [ShopSmart purchase prediction](<Decision Trees/Decision Tree Project>) | Purchase intent from 12,330 sessions | Pruned decision tree in a `ColumnTransformer` pipeline, grid search | F1 0.628 (grid search: 0.634) |
| [Employee turnover](<Logistic Regression/Project 2>) | Attrition classification | Logistic regression, L1 and L2 regularisation | L1: accuracy 0.870 |
| [House price prediction](<Linear Regression/house_price_predictor.ipynb>) | Regression, 2,919 houses | Linear regression | R² 0.37 |
| [ANN classification](<Deep Learning/ANN>) | Date-fruit variety, 7 classes | PyTorch feed-forward network | Accuracy 95.6% |
| [ANN regression](<Deep Learning/ANN>) | Power-plant energy output | PyTorch feed-forward network | R² 0.935 |
| [CNN on CIFAR-10](<Deep Learning/FNN>) | 10-class image classification | PyTorch CNN, 10 epochs | Accuracy 72.5% |
| [RNN sentiment analysis](<Deep Learning/RNN>) | IMDB review sentiment | NLTK preprocessing, TF-IDF, PyTorch RNN | Accuracy 85.2% |

## Topics

- **From scratch (NumPy):** KNN classifier and regressor, linear regression (gradient descent and OLS), logistic regression. See `Scratch Implementation/`.
- **Supervised:** linear, lasso and logistic regression, KNN, Naive Bayes, SVM (SVC/SVR), decision trees, random forests, AdaBoost, gradient boosting, XGBoost, heterogeneous ensembles.
- **Unsupervised:** K-means, hierarchical clustering, DBSCAN, PCA, isolation forest and local outlier factor for anomaly detection.
- **Deep learning (PyTorch):** a single neuron, ANNs, CNNs, RNNs.
- **Data tooling:** NumPy, Pandas, Matplotlib, Seaborn, REST APIs and web scraping (`requests`, BeautifulSoup), and a small Flask app.

## Data

Small datasets are included next to their notebooks. CIFAR-10 is downloaded automatically by `torchvision`. The IMDB review dataset (64 MB) is not included; download *IMDB Dataset of 50K Movie Reviews* from Kaggle into `Deep Learning/RNN/`.

---

More of my work: [anirudhverma33.github.io](https://anirudhverma33.github.io/)
