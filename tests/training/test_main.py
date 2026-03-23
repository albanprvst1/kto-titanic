import pytest
from unittest.mock import patch
from titanic.training.main import workflow

def test_workflow_runs_all_steps():
    # On simule (mock) load_data pour éviter l'appel S3 réel pendant les tests
    # On simule aussi les autres étapes pour tester uniquement l'enchaînement
    with patch('titanic.training.main.load_data') as mock_load, \
         patch('titanic.training.main.split_train_test') as mock_split, \
         patch('titanic.training.main.train') as mock_train, \
         patch('titanic.training.main.validate') as mock_validate:
        
        # On définit des retours fictifs pour chaque étape
        mock_load.return_value = "dist/data.csv"
        mock_split.return_value = ("xtrain.csv", "xtest.csv", "ytrain.csv", "ytest.csv")
        mock_train.return_value = "model.joblib"
        
        # Exécution du workflow
        workflow(
            input_data_path="all_titanic.csv",
            n_estimators=10,
            max_depth=5,
            random_state=42
        )
        
        # Vérifications : on s'assure que chaque fonction a été appelée
        assert mock_load.called
        assert mock_split.called
        assert mock_train.called
        assert mock_validate.called