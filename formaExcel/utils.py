import os

def trova_valore_max_modifica_file(percorso, nome_no_ext):
    file_in_caretlla = os.listdir(percorso)

    file_trovati = []
    for file in file_in_caretlla:
        if file.startswith(nome_no_ext):
            file_trovati.append(file)

    max_val = 0
    for file in file_trovati:
        if file.count("_modifica_") == 1:
            val = int(file.split("_")[-1].split(".")[0])
            if max_val < val:
                max_val = val
    return max_val

def da_int_a_formato_numero_str(incremento, lunghezza_numero=3):
    incremento = str(incremento)
    return "0" * (lunghezza_numero - len(incremento)) + incremento

if __name__ == "__main__":
    print("TEST")

    inc = da_int_a_formato_numero_str(1)
    assert inc == "001"
    inc = da_int_a_formato_numero_str(10)
    assert inc == "010"
    inc = da_int_a_formato_numero_str(100)
    assert inc == "100"
