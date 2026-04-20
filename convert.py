import sys
import os

def convert(filepath):
    if not filepath.endswith('.kicad_sym'):
        print(f"Skipping {filepath}, doesn't end with .kicad_sym")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    out_dir = filepath + 'dir'
    os.makedirs(out_dir, exist_ok=True)

    header_end = -1
    symbols = []
    
    depth = 0
    in_string = False
    escape = False
    
    symbol_start = -1
    symbol_name = ""
    
    i = 0
    while i < len(content):
        c = content[i]
        
        if escape:
            escape = False
        elif c == '\\':
            escape = True
        elif c == '"':
            in_string = not in_string
        elif not in_string:
            if c == '(':
                depth += 1
                
                if depth == 2:
                    if content[i:i+8] == '(symbol ':
                        if header_end == -1:
                            header_end = i
                        symbol_start = i
                        
                        # Find the name (it comes right after `(symbol `)
                        # We peek ahead to extract the name
                        q_start = content.find('"', i)
                        nextLine = content.find('\n', i)
                        if q_start != -1 and q_start < nextLine:
                            q_end = content.find('"', q_start + 1)
                            symbol_name = content[q_start+1:q_end]
                        else:
                            # Not quoted
                            first_space = content.find(' ', i)
                            next_space = content.find(' ', first_space+1)
                            next_paren = content.find('\n', first_space+1)
                            end_idx = min(x for x in [next_space, next_paren, nextLine] if x != -1)
                            symbol_name = content[first_space+1:end_idx].strip()
                            
            elif c == ')':
                if depth == 2 and symbol_start != -1:
                    symbol_content = content[symbol_start:i+1]
                    symbols.append((symbol_name, symbol_content))
                    symbol_start = -1
                depth -= 1
                
        i += 1

    if header_end == -1:
        print("Could not find any symbols or header end!")
        return
        
    header = content[:header_end]
    
    for name, sym_content in symbols:
        # Avoid illegal characters in filenames
        safe_name = name.replace('/', '_').replace(':', '_').replace('\\', '_')
        out_path = os.path.join(out_dir, f"{safe_name}.kicad_sym")
        with open(out_path, 'w', encoding='utf-8') as f:
            # We append a newline before the closing paren because `sym_content` ends traversing at the `)` character
            f.write(header + sym_content + '\n)\n')
            
    print(f"Converted {len(symbols)} symbols to {out_dir}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python convert.py <path_to.kicad_sym>")
    else:
        convert(sys.argv[1])
