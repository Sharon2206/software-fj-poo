# Software FJ - Sistema de Gestión de Servicios y Reservas


## Descripción del proyecto

Este proyecto fue desarrollado como parte de la asignatura de Programación de la Universidad Nacional y a Distancia.

El sistema simula la gestión de clientes, servicios y reservas para una empresa llamada Software FJ, la cual ofrece distintos tipos de servicios como:

- Reserva de salas
- Alquiler de equipos
- Asesorías especializadas

El programa fue desarrollado completamente en Python y no utiliza bases de datos, toda la información se maneja mediante objetos, listas y archivos de texto para el registro de eventos y errores.



## Objetivo del proyecto

El objetivo principal fue aplicar conceptos de programación orientada a objetos y manejo avanzado de excepciones mediante un sistema funcional y organizado.

En el desarrollo del proyecto se implementaron temas como:

- Abstracción
- Herencia
- Polimorfismo
- Encapsulación
- Clases abstractas
- Sobrescritura de métodos
- Manejo de excepciones
- Registro de logs
- Validaciones
- Uso de listas y objetos



## Funcionalidades principales

El sistema permite:

- Registrar clientes
- Mostrar servicios disponibles
- Crear reservas
- Procesar reservas
- Confirmar reservas
- Validar datos ingresados
- Registrar errores en logs.txt

Adicional el sistema continúa funcionando incluso cuando ocurren errores, gracias al manejo de excepciones implementados.

## Estructura del proyecto

```bash
software-fj-poo/
│
├── main.py
├── logs.txt
├── README.md
│
├── modelos/
├── servicios/
├── excepciones/
└── utilidades/