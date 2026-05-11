class error_sistema(Exception):
    """clase base para errores del sistema"""
    pass


class cliente_invalido_error(error_sistema):
    """error cuando los datos del cliente son invalidos"""
    pass


class servicio_no_disponible_error(error_sistema):
    """error cuando un servicio no esta disponible"""
    pass


class reserva_invalida_error(error_sistema):
    """error cuando una reserva no puede procesarse"""
    pass


class pago_invalido_error(error_sistema):
    """error relacionado con pagos incorrectos"""
    pass


class duracion_invalida_error(error_sistema):
    """error cuando la duracion es incorrecta"""
    pass