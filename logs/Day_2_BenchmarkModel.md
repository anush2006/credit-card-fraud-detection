**Day 4:**



**Agenda:**

* Data pre-processing and Model training : Benchmark Model



**ML model chosen: SVM**

**Reason:** 

* From the EDA we noticed that there is no clear linear separation between fraud and non-fraud cases. Because of this simple linear models like Linear Regression or Logistic Regression are not suitable here.
* KNN also does not look useful because the PCA scatter did not show any clean clusters or centroids that could guide neighbor-based decisions. If the data points are all mixed together KNN would mostly result in centroids too close to be distinguished properly.
* So the next reasonable model to start with is SVM. Since SVM can use nonlinear kernels(RBF), it can shift the problem into a higher-dimensional space where the classes have a chance to separate better. SVM allows class weight adjustment, which helps deal with the imbalance between fraud and non-fraud samples while training.
* It should be noted that this is just a BENCHMARK model and hence will serve as a baseline for other improved models.



**Other models:**

* Naive Bayes

Naive Bayes assumes that each feature affects the output independently.

But from the correlation map we saw that many features are actually related to each other, so this assumption doesn’t really hold for this dataset.

Because of that, Naive Bayes cannot be expected to perform well here.

Perhaps a weak baseline to prove that simple assumptions don’t work for this problem. Expected to perform marginally worse than SVM. 



* Decision Trees

The next model worth trying is a Decision Tree.

This works better than linear models because it learns split-based rules like “if this feature is below this value, classify as fraud,” which fits non-linear patterns way better. It can also apply class weighting, so it shouldn’t ignore fraud cases like simpler models might. Overall, it seems like a good step up from the earlier models.



* Random Forest

Random Forest basically improves on Decision Trees by using a bunch of trees instead of relying on just one. Since a single tree can overfit or make biased decisions, using lots of them trained on different random subsets of data and features helps smooth things out and improves accuracy.

So it should perform better and be more stable than a single decision tree.



* XGBoost

XGBoost also works with trees, but instead of training them all separately like Random Forest, it builds trees one after another where each new tree fixes the mistakes of the previous one. Since we saw earlier that fraud patterns are noisy, this should help the model learn those harder cases better. 

So XGBoost should ideally give better performance than Random Forest, especially because of how it focuses on correcting errors over time.


**Training and Results:**


Testing C variation



OUTPUT 1:

Default C and gamma values

Loading dataset...

Dataset loaded successfully.

Features and target variable separated.

Dataset split into training and testing sets.

Training the SVM model...

Making predictions on the test set...

Evaluating the model...

Confusion Matrix:

\[\[56708   156]

&nbsp;\[   24    74]]



Classification Report:

&nbsp;             precision    recall  f1-score   support



&nbsp;          0     0.9996    0.9973    0.9984     56864

&nbsp;          1     0.3217    0.7551    0.4512        98



&nbsp;   accuracy                         0.9968     56962

&nbsp;  macro avg     0.6607    0.8762    0.7248     56962

weighted avg     0.9984    0.9968    0.9975     56962



OUTPUT 2:


C=1 , gamma=0.01



Loading dataset...

Dataset loaded successfully.

Features and target variable separated.

Dataset split into training and testing sets.

Training the SVM model...

Making predictions on the test set...

Evaluating the model...

Confusion Matrix:

\[\[56298   566]

&nbsp;\[   15    83]]



Classification Report:

&nbsp;             precision    recall  f1-score   support



&nbsp;          0     0.9997    0.9900    0.9949     56864

&nbsp;          1     0.1279    0.8469    0.2222        98



&nbsp;   accuracy                         0.9898     56962

&nbsp;  macro avg     0.5638    0.9185    0.6085     56962

weighted avg     0.9982    0.9898    0.9935     56962



OUTPUT 3:

C=5 , gamma=0.01



Loading dataset...

Dataset loaded successfully.

Features and target variable separated.

Dataset split into training and testing sets.

Training the SVM model...

Making predictions on the test set...

Evaluating the model...

Confusion Matrix:

\[\[56583   281]

&nbsp;\[   18    80]]



Classification Report:

&nbsp;             precision    recall  f1-score   support



&nbsp;          0     0.9997    0.9951    0.9974     56864

&nbsp;          1     0.2216    0.8163    0.3486        98



&nbsp;   accuracy                         0.9948     56962

&nbsp;  macro avg     0.6106    0.9057    0.6730     56962

weighted avg     0.9983    0.9948    0.9962     56962


**C=5 is the best trade off so far**



Testing gamma variation



OUTPUT 4:

C=5 , gamma =0.1

Loading dataset...

Dataset loaded successfully.

Features and target variable separated.

Dataset split into training and testing sets.

Training the SVM model...

Making predictions on the test set...

Evaluating the model...

Confusion Matrix:

\[\[56845    19]

&nbsp;\[   51    47]]



Classification Report:

&nbsp;             precision    recall  f1-score   support



&nbsp;          0     0.9991    0.9997    0.9994     56864

&nbsp;          1     0.7121    0.4796    0.5732        98



&nbsp;   accuracy                         0.9988     56962

&nbsp;  macro avg     0.8556    0.7396    0.7863     56962

weighted avg     0.9986    0.9988    0.9987     56962





OUTPUT 5:



C=5 , gamma=0.05



Loading dataset...

Dataset loaded successfully.

Features and target variable separated.

Dataset split into training and testing sets.

Training the SVM model...

Making predictions on the test set...

Evaluating the model...

Confusion Matrix:

\[\[56819    45]

&nbsp;\[   36    62]]



Classification Report:

&nbsp;             precision    recall  f1-score   support



&nbsp;          0     0.9994    0.9992    0.9993     56864

&nbsp;          1     0.5794    0.6327    0.6049        98



&nbsp;   accuracy                         0.9986     56962

&nbsp;  macro avg     0.7894    0.8159    0.8021     56962

weighted avg     0.9986    0.9986    0.9986     56962




**BEST F1 SCORE SO FAR**



OUTPUT 6:



C=5 , gamma=0.02



Loading dataset...

Dataset loaded successfully.

Features and target variable separated.

Dataset split into training and testing sets.

Training the SVM model...

Making predictions on the test set...

Evaluating the model...

Confusion Matrix:

\[\[56737   127]

&nbsp;\[   23    75]]



Classification Report:

&nbsp;             precision    recall  f1-score   support



&nbsp;          0     0.9996    0.9978    0.9987     56864

&nbsp;          1     0.3713    0.7653    0.5000        98



&nbsp;   accuracy                         0.9974     56962

&nbsp;  macro avg     0.6854    0.8815    0.7493     56962

weighted avg     0.9985    0.9974    0.9978     56962



Summary \& Results:

After tuning, it became clear that gamma had a much stronger impact on model behaviour than C.

Lower gamma values produced higher recall but at the cost of more false positives.

Increasing gamma improved precision but sharply reduced recall, meaning more fraud cases were missed.

Among tested settings, gamma = 0.01 with C = 5 delivered the best fraud detection performance because it maximized recall (~82%) while maintaining acceptable precision levels.



**FINAL BASELINE:**
     
**RECALL:** 0.8163
**F1:** 0.3486
**PRECISION:** 0.2216

This output is preferred as missing fraud cases it much worse than flagging actual cases as fraud as it is generally not acceptable to miss fraud cases. This is situation specific hence this is chose as baseline.

