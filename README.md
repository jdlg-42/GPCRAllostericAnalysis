# TFG
Repositorio de toda la parte relacionada al código sobre el TFG.

El flujo de trabajo que se va a seguir es el siguiente:
1. Lectura y comprensión de la literatura que ya hay del tema, relacionada fundamentalmente al alosterismo y el rol de las proteínas quinasas en las funciones celulares. Así como también los avances en la materia a nivel computacional, y las principales técnicas para los estudios *in silico* de las proteínas. 
2. Aprender a usar Python y las principales librerías de bioinformática y biología computacional.
    a. Algunas librerías de interés son Biopython, PyInteraph 2, etc.
4. Generar un dataset, una base de datos que contenga estructuras y secuencias de proteínas quinasa. Estos datos procederán de PDB, ASD y UniProt, entre otros, para obtener información relevante con respecto a sitios de unión y demás.
    a. Debe incluir información referente a sitios alostéricos conocidos y mutaciones que afecten a la actividad quinasa.
5. Tras ello se entrenará un modelo de lenguaje de proteínas (PLM) para predecir el efecto de las mutaciones en la comunicación alostérica e identificar así hotspots.
6. Se generará una red de estructura de proteínas (PSN) para las quinasas escogidas empleando su estructura tridimensional, para luego analizar dichas redes empleando métodos basados en la teoría de grafos y así identificar residuos de interés que tengna un papel en el alosterismo.
