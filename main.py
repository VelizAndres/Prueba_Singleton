from cloud_logger import CloudLogger
from logger import Logger
from traceback import format_exc


def main():
    log_nube: Logger = CloudLogger("Prueba2")

    # Se cambia el nombre para la colección
    # Pero al aplicar el patrón singleton
    # Se converva unicamente la primera instancia
    # Por lo tanto solo la primera colección es valida
    # La colección "Prueba" no se crea
    # La colección "Prueba2" es la unica existente
    log2_nube: Logger = CloudLogger("Prueba")
    run: bool = True
    while run:
        try:
            log_nube.message("Ingrese un numero")
            log2_nube.message("Ingrese un numero")
            num: int = int(input('\n'))
            if num <= 0 or num >= 25:
                log_nube.warning("Debe ingresar un numero menor a 25 y mayor a cero")
                log2_nube.warning("Debe ingresar un numero menor a 25 y mayor a cero")
            else:
                result: int = 1
                for i in range(num):
                    result += i * result
                log_nube.success(f'Resultado = {result}')
                log2_nube.success(f'Resultado = {result}')
                run = False

        except BaseException:
            exc = format_exc()
            log_nube.error("Debe ingresar un numero = " + exc)
            log2_nube.error("Debe ingresar un numero = " + exc)


main()

