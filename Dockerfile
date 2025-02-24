#Dockerfile
FROM python:3.9
WORKDIR /app
RUN python -m pip install \
    pandas \
    scikit-learn \
    joblib \
    pytest
COPY main.py .
COPY random_forest_model.pkl .
COPY src/data_processing.py .
COPY src/modelo_RF.py .
COPY src/predicciones.py .
COPY test/test_data_processing.py .
COPY test/test_modelo_RF.py .
COPY test/test_predicciones.py .
ENTRYPOINT [ "python", "main.py" ]
CMD [] 