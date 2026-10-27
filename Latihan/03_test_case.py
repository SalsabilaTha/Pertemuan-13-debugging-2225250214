def status_lulus(nilai): 
    if nilai >= 60: 
        return "Lulus"  
    return "Tidak Lulus"

test_cases = [59, 60, 61]

for nilai in test_cases:
    print(f"Nilai: {nilai}: {status_lulus(nilai)}")