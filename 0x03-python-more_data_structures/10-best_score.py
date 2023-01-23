<<<<<<< HEAD

=======
#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    b_score = max(a_dictionary.values(), default=None)
    for k, v in a_dictionary.items():
        if v == b_score:
            return k
>>>>>>> b70771774ee31cbaf3a38c1368c43e216bcf72de
