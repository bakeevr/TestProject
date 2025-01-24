def validate_imei(imei: str) -> bool:
    if len(imei) != 15 or not imei.isdigit():
        return False

    total = 0
    for i, char in enumerate(imei):
        n = int(char)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n = (n // 10) + (n % 10)
        total += n

    return total % 10 == 0