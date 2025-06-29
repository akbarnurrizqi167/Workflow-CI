import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Aktifkan autolog MLflow
mlflow.sklearn.autolog()

# Baca dataset hasil preprocessing
df = pd.read_csv("dataset_preprocessing/train.csv")

# Pisahkan fitur dan target
X_train = df.drop(columns=["Churn"])
y_train = df["Churn"]

# Split untuk validasi internal
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# Mulai MLflow experiment
with mlflow.start_run() as run:
    model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_val)
    acc = accuracy_score(y_val, y_pred)
    print(f"Validation Accuracy: {acc:.4f}")

    # Simpan model eksplisit (untuk docker build)
    mlflow.sklearn.log_model(model, artifact_path="model")

    # Optional: log metric secara manual
    mlflow.log_metric("val_accuracy", acc)

    print(f"Model logged under run ID: {run.info.run_id}")
