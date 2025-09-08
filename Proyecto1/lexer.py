# Lista manual de palabras reservadas de Python
RESERVED = {
    "False","None","True","and","as","assert","break","class","continue","def",
    "del","elif","else","except","finally","for","from","global","if","import",
    "in","is","lambda","nonlocal","not","or","pass","raise","return","try",
    "while","with","yield"
}

# Ampliación para el ejemplo del PDF
RESERVED_EXTRA = {
    "print","object","str","bool","int","float","list","dict","set","tuple","self"
}
RESERVED |= RESERVED_EXTRA

# Operadores multi-caracter
MULTI_OPS = {
    "!=": "tk_distinto",
    "==": "tk_igualdad",
    "<=": "tk_menor_igual",
    ">=": "tk_mayor_igual",
    "->": "tk_ejecuta",
    "**": "tk_potencia",
    "//": "tk_div_entera",
}

# Operadores de un solo caracter
SINGLE_OPS = {
    "(": "tk_par_izq",
    ")": "tk_par_der",
    "[": "tk_cor_izq",
    "]": "tk_cor_der",
    "{": "tk_llave_izq",
    "}": "tk_llave_der",
    ",": "tk_coma",
    ":": "tk_dos_puntos",
    ".": "tk_punto",
    ";": "tk_pyc",
    "=": "tk_asig",
    "+": "tk_suma",
    "-": "tk_resta",
    "*": "tk_mult",
    "/": "tk_div",
    "%": "tk_mod",
    "<": "tk_menor",
    ">": "tk_mayor",
}

def error(linea, columna):
    print(f">>> Error léxico(linea:{linea},posicion:{columna})")
    exit(1)

def es_id_start(ch):
    return ch == "_" or ch.isalpha()

def es_id_part(ch):
    return ch == "_" or ch.isalnum()

def tokenize(texto):
    tokens = []
    i = 0
    n = len(texto)
    linea = 1
    col = 1

    while i < n:
        ch = texto[i]

        # Espacios y tabs
        if ch in " \t\r":
            i += 1
            col += 1
            continue

        # Nueva línea
        if ch == "\n":
            i += 1
            linea += 1
            col = 1
            continue

        # Comentarios
        if ch == "#":
            while i < n and texto[i] != "\n":
                i += 1
                col += 1
            continue

        # Cadenas "..." o '...'
        if ch == '"' or ch == "'":
            q = ch
            start_line, start_col = linea, col
            i += 1
            col += 1
            lex = []
            while i < n and texto[i] != q:
                if texto[i] == "\n":
                    error(start_line, start_col)
                lex.append(texto[i])
                i += 1
                col += 1
            if i >= n:
                error(start_line, start_col)
            i += 1
            col += 1
            contenido = "".join(lex)
            print(f'<tk_cadena,"{contenido}",{start_line},{start_col}>')
            continue

        # Identificadores / Reservadas
        if es_id_start(ch):
            start_line, start_col = linea, col
            j = i
            while j < n and es_id_part(texto[j]):
                j += 1
            lexema = texto[i:j]
            if lexema in RESERVED:
                print(f"<{lexema},{start_line},{start_col}>")
            else:
                print(f"<id,{lexema},{start_line},{start_col}>")
            col += (j - i)
            i = j
            continue

        # Números enteros
        if ch.isdigit():
            start_line, start_col = linea, col
            j = i
            while j < n and texto[j].isdigit():
                j += 1

            lexema = texto[i:j]
            print(f"<tk_entero,{lexema},{start_line},{start_col}>")
            col += (j - i)
            i = j
            continue

        # Operadores multi (subcadena más larga)
        if i + 1 < n:
            par = texto[i:i+2]
            if par in MULTI_OPS:
                start_line, start_col = linea, col
                print(f"<{MULTI_OPS[par]},{start_line},{start_col}>")
                i += 2
                col += 2
                continue

        # Operadores simples
        if ch in SINGLE_OPS:
            start_line, start_col = linea, col
            print(f"<{SINGLE_OPS[ch]},{start_line},{start_col}>")
            i += 1
            col += 1
            continue

        # Error léxico
        error(linea, col)

    return tokens

def main():
    infile = input("Ingrese el nombre del archivo de entrada (.py): ")
    with open(infile, "r", encoding="utf-8") as f:
        src = f.read()

    toks = tokenize(src)
    print("\n".join(toks))


main()
