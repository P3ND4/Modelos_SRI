  # Modelos_SRI

## Autores:
- José Carlos Pendas Rodríguez
- Max Bengochea Moré

## Modelo Usado:
- Modelo Booleano
- Modelo Booleano Extendido

## Cómo ejecutar:
1. Abrir la consola en la carpeta principal y escribir:
```bash
./startup.md
```
2. En la consola le pedirá elegir el modelo que desee usar.

3. Una vez que cargue el corpus de documentos, le pedirá que escriba la consulta que desee realizar.

## Explicación del modelo:
Modelo Booleano: Primero se carga el corpus para instanciar la matriz de pertenencia donde las columnas representan las palabras y las filas los documentos. Entonces, la posición (i, j) tendrá valor 0 o 1 en dependencia de si el término j aparece en el documento i. El usuario debe insertar en la consulta las palabras que desee, separadas con los operadores booleanos. Esta consulta se lleva a forma normal disyuntiva (DNF) y se evalúa en cada documento tomando los valores de las palabras según la matriz.

Modelo Booleano Extendido: Para este se utiliza una matriz similar, pero en lugar de 0 o 1 para indicar si pertenece la palabra, ésta tendrá su peso en el documento, el cual se asocia a su frecuencia. Para asignarle un peso final a cada documento que cumpla con la condición de la consulta, se le asigna la sumatoria de las palabras que aparecen en cada conjunción dentro de la consulta.

## Insuficiencias de la implementación:
Para una entrada con "not" podría pasar que al no asignar valor a la palabra operada por este caso, como "A OR NOT B", te muestre documentos donde estén A y B con la misma relevancia que uno donde esté A, suponiendo que A es igualmente relevante para ambos, que tal vez asignando algún valor extra a estos documentos podría solucionar esto.

## Fuentes de Datos:
https://ir-datasets.com
