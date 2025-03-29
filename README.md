# 🎢 Simulación del Problema de Monty Hall con Flask

Esta aplicación web permite ejecutar simulaciones del **Problema de Monty Hall** y visualizar la probabilidad de ganar cambiando de puerta. Está desarrollada en **Flask** con una interfaz HTML sencilla e interactiva.

---

## 📌 Características

✅ Simula el problema de Monty Hall con un número configurable de intentos.  
✅ Calcula la probabilidad de ganar si el jugador cambia de puerta.  
✅ Interfaz web con un formulario intuitivo.  
✅ Aplicación desarrollada con Flask y estilizada con CSS.  

---

## 🚀 Instalación y Ejecución

### 1️⃣ Clonar el repositorio

```sh
git clone https://github.com/tu_usuario/monty-hall-flask.git
cd monty-hall-flask
```

### 2️⃣ Instalar dependencias

Asegúrate de tener **Python 3.8+** instalado y luego ejecuta:

```sh
pip install -r requirements.txt
```

### 3️⃣ Ejecutar la aplicación

```sh
python app.py
```

La aplicación estará disponible en:  
👉 **http://127.0.0.1:5000/**  

---

## 🛠️ Tecnologías utilizadas

- **Flask** → Framework web en Python.  
- **NumPy** → Para cálculos de probabilidad.  
- **HTML + CSS** → Interfaz web.  

---

## 🖥️ Uso de la aplicación

1. Ingresa un número de simulaciones (ej. 10,000).  
2. Haz clic en **"Ejecutar Simulación"**.  
3. Verás el resultado de la probabilidad de ganar si cambias de puerta.  

Ejemplo de resultado:  
```
Se realizaron 10000 simulaciones.
Probabilidad de ganar al cambiar de puerta: 0.667
```

---

## 📝 Estructura del proyecto

```
/monty-hall-flask
│── app.py                  # Código principal de Flask
│── requirements.txt         # Dependencias del proyecto
│── README.md                # Documentación del proyecto
│── /static
│   ├── style.css            # Estilos CSS para la interfaz
│── /templates
│   ├── index.html           # Página principal con formulario y resultados
```

---

## 🌟 Mejoras futuras

✅ Incluir gráficos con **Matplotlib** para visualizar la probabilidad.  
✅ Agregar opción para simular el juego sin cambiar de puerta.  
✅ Mejorar la interfaz con Bootstrap o Tailwind CSS.  

---

## 📝 Autor


- Brayan Diaz Valencia - Samuel - Nicolas - GHS

