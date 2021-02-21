# Entorno Virtual
* Para activar el entorno virtual, ejecutar `.source venv/bin/activate`
* Para desactivarlo ejecutar `deactivate`

# Requerimientos
* python (>=3)
* mysql
* Instalar los requerimientos ejecutar `pip install -r requirements.txt`

# Aplicaccion
* Ejecutar `python3 manage.py runserver`



* Notas

### Capa de Servicio
# https://www.iteramos.com/pregunta/13133/diferencia-entre-repositorio-y-capa-de-servicios

### Buscar el titulo Decoupling the Service Layer
# https://docs.microsoft.com/en-us/aspnet/mvc/overview/older-versions-1/models-data/validating-with-a-service-layer-cs

# Mi flujo es <Controlador> <-> <Servicio> <-> <Repositorio> <-> <Modelo>
# Otro flujo <Servicio> <-> <Servicio> <-> <Repositorio> <-> <Modelo>

# Elijo que siempre a servicio por si cambia un poco la logica de algo (registro por ejemplo), el repositorio no hace falta tocarlo.
