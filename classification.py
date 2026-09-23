# ============================================
# Project 2: Data Classification Using AI
# DecodeLabs Industrial Training Kit
# Algorithm: K-Nearest Neighbors (KNN)
# ============================================

# --- Imports ---
# datasets.load_iris -> gives us the built-in Iris dataset (no CSV needed)
# train_test_split    -> splits data into training and testing sets
# StandardScaler      -> scales features so no single feature dominates
# KNeighborsClassifier-> the actual classification algorithm (KNN)
# metrics tools        -> to check how good our model actually is
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# ============================================
# STEP 1: LOAD AND UNDERSTAND THE DATASET
# ============================================
# The Iris dataset has 150 samples, 3 classes (Setosa, Versicolor, Virginica),
# and 4 features (sepal length, sepal width, petal length, petal width).
iris = datasets.load_iris()
X = iris.data          # the 4 measurements (features)
y = iris.target        # the flower type (0, 1, or 2) — what we want to predict

print("Dataset shape:", X.shape)                # (150, 4)
print("Classes:", iris.target_names)            # ['setosa' 'versicolor' 'virginica']
print("Sample row:", X[0], "-> label:", y[0])
print("-" * 50)


# ============================================
# STEP 2: SPLIT INTO TRAINING AND TESTING SETS
# ============================================
# 80% of the data is used to TRAIN the model.
# 20% is held back to TEST how well it actually learned.
# random_state=42 makes the shuffle reproducible (same split every run).
# stratify=y keeps the class proportions balanced in both sets.
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])
print("-" * 50)


# ============================================
# STEP 3: FEATURE SCALING (The Gatekeeper Rule)
# ============================================
# KNN measures DISTANCE between points, so features with bigger
# numeric ranges would unfairly dominate the distance calculation.
# StandardScaler transforms every feature to mean=0, variance=1.
#
# IMPORTANT: we .fit() the scaler ONLY on training data, then just
# .transform() the test data — this avoids "leaking" test data
# information into the training process.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# ============================================
# STEP 4: TRAIN THE MODEL (Instantiate -> Fit)
# ============================================
# n_neighbors=5 means: for each new point, look at its 5 closest
# neighbors in the training data and take a majority vote on the class.
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)   # the model "memorizes" the training map


# ============================================
# STEP 5: PREDICT ON UNSEEN TEST DATA
# ============================================
predictions = model.predict(X_test_scaled)


# ============================================
# STEP 6: OUTPUT VALIDATION
# ============================================
# Accuracy alone can be misleading (the "Accuracy Mirage"), so we also
# check the Confusion Matrix and F1 Score for a fuller picture.
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report (Precision, Recall, F1 Score):")
print(classification_report(y_test, predictions, target_names=iris.target_names))


# ============================================
# STEP 7: PREDICT A BRAND-NEW SAMPLE (Bonus)
# ============================================
# Try classifying a flower the model has never seen before.
new_flower = [[5.1, 3.5, 1.4, 0.2]]   # looks like a Setosa
new_flower_scaled = scaler.transform(new_flower)
predicted_class = model.predict(new_flower_scaled)
print("\nNew flower prediction:", iris.target_names[predicted_class[0]])
