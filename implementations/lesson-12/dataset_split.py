from sklearn.model_selection import train_test_split

X = list(range(100))
y = [x*2 for x in X]

X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)

X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

print("Training Set:", len(X_train))
print("Validation Set:", len(X_val))
print("Test Set:", len(X_test))