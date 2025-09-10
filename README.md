---
# 📄 README - Proyecto 1: Analizador Léxico en Python

## 📌 Descripción

Este proyecto implementa un **analizador léxico** en Python, desarrollado desde cero y sin utilizar librerías externas.
El programa recibe un archivo `.py` como entrada y devuelve en consola una lista de **tokens** válidos con su lexema, línea y columna, o en caso de encontrar un símbolo no permitido, reporta un **error léxico** indicando la posición.

El proyecto fue diseñado siguiendo las especificaciones del documento de la materia.

---

## 📂 Estructura del proyecto

```
Proyecto1/
├── caso1.py             # Caso de prueba 1 (90.00.50)
├── caso2.py             # Caso de prueba 2 (1¬239)
├── caso3.py             # Caso de prueba 3 (2.5598055while3!=88¬56.a)
├── codigo.py            # Archivo de prueba (ejemplo con clases Animal y Cow)
├── salida_caso1.txt     # Resultados esperados para caso1.py
├── salida_caso2.txt     # Resultados esperados para caso2.py
├── salida_caso3.txt     # Resultados esperados para caso3.py
├── salida_codigo.txt    # Resultados esperados para codigo.py
├── Prueba.py            # Archivo de prueba 
├── README.txt           # Este archivo
└── lexer.py             # Analizador léxico
```

---

## ⚙️ Ejecución

1. Abrir la terminal en la carpeta del proyecto:

   ```bash
   cd Proyecto1
   ```

2. Ejecutar el analizador:

   ```bash
   python3 lexer.py
   ```

3. Cuando el programa pregunte:

   ```
   Ingrese el nombre del archivo de entrada (.py):
   ```

   se debe escribir el nombre del archivo a analizar, por ejemplo:

   ```
   codigo.py
   ```

---

## 🧪 Casos de prueba

### ✔️ Caso 1: `caso1.py`

Entrada:

```
90.00.50
```

Salida esperada:

```
<tk_entero,90,1,1>
<tk_punto,1,3>
<tk_entero,00,1,4>
<tk_punto,1,6>
<tk_entero,50,1,7>
```

---

### ❌ Caso 2: `caso2.py`

Entrada:

```
1¬239
```

Salida esperada:

```
<tk_entero,1,1,1>
>>> Error léxico(linea:1,posicion:2)
```

---

### ❌ Caso 3: `caso3.py`

Entrada:

```
2.5598055while3!=88¬56.a
```

Salida esperada:

```
<tk_entero,2,1,1>
<tk_punto,1,2>
<tk_entero,5598055,1,3>
<id,while3,1,10>
<tk_distinto,1,16>
<tk_entero,88,1,18>
>>> Error léxico(linea:1,posicion:20)
```

---

### ✔️ Caso 4: `codigo.py`

Archivo de prueba con clases `Animal` y `Cow`.
El analizador genera tokens para identificadores, palabras reservadas, operadores, y cadenas, como por ejemplo:

```
<class,1,1>
<id,Animal,1,7>
...
<tk_cadena,"Animal",4,26>
<tk_cadena,"???",9,9>
<tk_cadena,"Cow",12,24>
<tk_cadena,"moo",16,9>
```

---

## 🚀 Notas

* El analizador reconoce:

  * Palabras reservadas de Python.
  * Identificadores válidos.
  * Números enteros.
  * Operadores simples y múltiples.
  * Cadenas entre comillas simples o dobles.
* Al encontrar un carácter inválido, muestra un **error léxico** y detiene el análisis.
* El programa **no usa librerías externas**, cumple con la restricción del enunciado.

---

✍️ **Autores:** \[Paula Ortiz / Sofia Londoño ]
📅 **Fecha:** \[10 de Septiembre, 2025]

---
