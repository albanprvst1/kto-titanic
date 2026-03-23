import logging
import os
from pathlib import Path
import boto3
import pandas as pd
from ydata_profiling import ProfileReport

# Configuration S3 / MinIO
MLFLOW_S3_ENDPOINT_URL = "https://minio-api-albanprvst-dev.apps.rm1.0a51.p1.openshiftapps.com"
AWS_ACCESS_KEY_ID = "minio"
AWS_SECRET_ACCESS_KEY = "minio123"

def load_data(path: str) -> str:
    logging.warning(f"load_data on path : {path}")
    
    # Création du dossier de destination
    local_dir = Path("./dist")
    local_dir.mkdir(parents=True, exist_ok=True)
    local_path = local_dir / "data.csv"
    
    logging.warning(f"Downloading to : {local_path}")

    # Client S3
    s3_client = boto3.client(
        "s3",
        endpoint_url=MLFLOW_S3_ENDPOINT_URL,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

    # Téléchargement depuis le bucket 'kto-titanic'
    s3_client.download_file("kto-titanic", path, str(local_path))
    
    # Lecture pour vérification et Profiling
    df = pd.read_csv(local_path)
    
    # Génération du rapport de profiling (optionnel)
    profile = ProfileReport(df, title=f"Profiling Report - {path}")
    profile.to_file(local_dir / "profile.html")

    # TRÈS IMPORTANT : On renvoie le chemin vers le fichier téléchargé
    return str(local_path)