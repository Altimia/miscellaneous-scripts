def remove_duplicates():
    with open('out.txt', 'r') as f:
        lines = f.read().splitlines()

    seen = set()
    duplicates = set()

    with open('unique.txt', 'w') as f:
        for line in lines:      
            if line not in seen:
                seen.add(line)   
                f.write(line + '\n')    
            else:
                duplicates.add(line)

    print("Duplicates found:")
    for dup in duplicates:   
        print(dup)

remove_duplicates()