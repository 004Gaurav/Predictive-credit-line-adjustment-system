import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name="Predictive credit line adjustment system"

list_of_files=[
    f"src/Predictive credit line adjustment system/__init__.py",
    f"src/Predictive credit line adjustment system/components/__init__.py",
    f"src/Predictive credit line adjustment system/components/data_ingestion.py",
    f"src/Predictive credit line adjustment system/components/data_transformation.py",
    f"src/Predictive credit line adjustment system/components/model_trainer.py",
    f"src/Predictive credit line adjustment system/components/model_monitering.py",
    f"src/Predictive credit line adjustment system/pipelines/__init__.py",
    f"src/Predictive credit line adjustment system/pipelines/training_pipeline.py",
    f"src/Predictive credit line adjustment system/pipelines/prediction_pipeline.py",
    f"src/Predictive credit line adjustment system/exception.py",
    f"src/Predictive credit line adjustment system/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

# Assuming list_of_files is already defined
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # Check if file doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass  # Create an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
