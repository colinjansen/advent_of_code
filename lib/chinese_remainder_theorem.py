def extended_gcd(a, b):
    """
    Returns (x, y, gcd) where ax + by = gcd
    """
    if a == 0:
        return 0, 1, b
    
    old_x, old_y = 1, 0
    cur_x, cur_y = 0, 1
    
    while b != 0:
        quotient = a // b
        a, b = b, a % b
        cur_x, old_x = old_x - quotient * cur_x, cur_x
        cur_y, old_y = old_y - quotient * cur_y, cur_y
        
    return old_x, old_y, a

def mod_inverse(a, m):
    """
    Returns the modular multiplicative inverse of a modulo m
    """
    x, _, gcd = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"Modular inverse does not exist for {a} (mod {m})")
    return x % m

def chinese_remainder_theorem(remainders, moduli):
    """
    Solves the system of congruences:
    x ≡ remainders[i] (mod moduli[i]) for all i
    
    Args:
        remainders: List of remainders
        moduli: List of moduli (must be pairwise coprime)
    
    Returns:
        x: Solution to the system of congruences
    """
    if len(remainders) != len(moduli):
        raise ValueError("Number of remainders must equal number of moduli")
    
    total = 0
    prod = 1
    
    # Calculate product of moduli
    for modulus in moduli:
        prod *= modulus
        
    for remainder, modulus in zip(remainders, moduli):
        p = prod // modulus
        total += remainder * p * mod_inverse(p, modulus)
        total %= prod
        
    return total