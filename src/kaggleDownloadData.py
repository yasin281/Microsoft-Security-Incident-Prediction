import os
import pandas as pd
from sklearn.model_selection import train_test_split
from kagglehub import dataset_download

def create_reduced_file(original_file_path, reduced_file_path, target_column, sample_size=10000):
    """
    Crea un archivo reducido a partir del archivo original aplicando undersampling estratificado.

    :param original_file_path: Ruta al archivo original.
    :param reduced_file_path: Ruta donde se guardará el archivo reducido.
    :param target_column: Nombre de la columna objetivo para estratificación.
    :param sample_size: Tamaño del conjunto reducido.
    """
    df_original = pd.read_csv(original_file_path)
    print(f"El archivo original tiene {len(df_original)} filas.")
    
    # Realizar undersampling estratificado
    df_reduced, _ = train_test_split(
        df_original,
        train_size=sample_size,
        stratify=df_original[target_column],
        random_state=42
    )
    
    df_reduced.to_csv(reduced_file_path, index=False)
    print(f"Archivo reducido creado con {len(df_reduced)} filas manteniendo proporciones de clases.")

# Configuración de rutas
dataset_folder = os.getcwd()
reduced_file_path = os.path.join(dataset_folder, 'microsoft_Reduced.csv')

if not os.path.exists(reduced_file_path):
    file_path = dataset_download("Microsoft/microsoft-security-incident-prediction")
    original_file_path = os.path.join(file_path, "GUIDE_Test.csv")
    
    create_reduced_file(original_file_path, reduced_file_path, target_column='IncidentGrade')
else:
    df_reduced = pd.read_csv(reduced_file_path)
    print(f"Archivo cargado con {len(df_reduced)} filas.")

print(df_reduced.head())
