def is_hit(actual_dist: float, projectile_dist: float) -> bool:
    """
    Returns True if the actual and projectile distances are within 10 m.
    """
    # You can just return the value of the expression directly
    # return abs(actual_dist - projectile_dist) < 10
    if abs(actual_dist - projectile_dist) < 10:
        return True
    else:
        return False # need a return for every branch
    
def main() -> None:
    print(is_hit(5, 20))

main()