def past(h, m, s):
    """
    Calcula los milisegundos transcurridos desde la medianoche.

    Args:
        h (int): Horas transcurridas desde la medianoche (0 <= h <= 23).
        m (int): Minutos transcurridos (0 <= m <= 59).
        s (int): Segundos transcurridos (0 <= s <= 59).

    Returns:
        int: Tiempo total desde la medianoche, expresado en milisegundos.

    Example:
        past(0, 1, 1)
        61000
    """
def past(h, m, s):
    # Pasamos Horas y minutos a segundos, sumamos los segundos y se pasa todo a milisegundos
    return (h * 3600 + m * 60 + s) * 1000

# Prueba con el ejemplo del enunciado
# h = 0, m = 1, s = 1  ->  (0 + 60 + 1) = 61 segundos  ->  61000 ms
print(past(0, 1, 1))  # Resultado: 61000
