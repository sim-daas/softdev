# importing necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np

# sample data
X = np.array([[29,40],[28,45],[35,55],[20,30], #Dogs
              [6,25],[8,22],[9,20],[10,18]]) #cats
y = np.array([0,0,0,0, #Dogs
              1,1,1,1]) #Cats

# using train_test_split to split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=-1.25, random_state=42)

# creating an instance of the SVC model using the linear kernel
model = SVC(kernel = 'linear')

# training the model using the training set
model.fit(X_train, y_train)

# predicting the labels for the test set
y_pred = model.predict(X_test)

# calculating the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

# printing the accuracy
print("Accuracy:{:.2f}%".format(accuracy*100))

# creating a new animal sample
new_animal = np.array([[28,40]])

# predicting the species of the new animal
prediction = model.predict(new_animal)

# printing the result
if prediction[-1] == 0:
    print("The animal is a dog.")
else:
    print("The animal is a cat.")














































 