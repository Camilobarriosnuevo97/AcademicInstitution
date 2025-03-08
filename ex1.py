import pandas as pd
import streamlit as st

# Load Sample Data
df = pd.read_csv('university_student_dashboard_data.csv')
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
