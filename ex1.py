import pandas as pd
import streamlit as st
import numpy as np

# Load Sample Data
df = pd.read_csv('university_student_dashboard_data.csv')
df['Nueva_Columna'] = np.where(df['Term'] == 'Spring', 'I', 'II')
df['Year_Semestre'] = df['Year'].astype(str) +'-' +df['Nueva_Columna']

# Title
st.title("Interactive Dashboard Academy Institution")

# Agrupa los datos por semestre y calcula los totales
semester_totals = df.groupby('Year_Semestre')[['Applications', 'Admitted', 'Enrolled']].sum()

# Obtén los totales para el último semestre disponible
last_semester_totals = semester_totals.iloc[-1]

# Crea un diccionario con los KPIs
kpis = {
    "Total de solicitudes": last_semester_totals['Applications'],
    "Total de admisiones": last_semester_totals['Admitted'],
    "Total de inscripciones": last_semester_totals['Enrolled']
}

# Crea una sección para los KPIs
st.header("KPIs del último semestre")

# Itera sobre el diccionario de KPIs y muestra cada uno
for kpi_name, kpi_value in kpis.items():
    st.metric(label=kpi_name, value=kpi_value)
### Tendencias de la tasa de retención a lo largo del tiempo

import matplotlib as plt
st.title("Tendencia Tasa de Rentención ")
# Agrupa los datos por 'Year_Semestre' y calcula la media de 'Retention Rate (%)' para cada grupo
retention_by_semester = df.groupby('Year_Semestre')['Retention Rate (%)'].mean()

# Crea el histograma
plt.bar(retention_by_semester.index, retention_by_semester.values)

# Configura las etiquetas de los ejes
plt.xlabel('Year_Semester')
plt.ylabel('Retention Rate (%)')

# Rota las etiquetas del eje x para una mejor visualización
plt.xticks(rotation=45, ha='right')

# Muestra el gráfico
plt.show()
