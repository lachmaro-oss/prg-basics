def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f"{hours:02d}:{minutes:02d}"
    
    elif time_format == '12':
        period = 'am' if hours < 12 else 'pm'
        
        hours_12 = hours % 12
        if hours_12 == 0:
            hours_12 = 12
            
        return f"{hours_12}:{minutes:02d}{period}"
    
    else:
        print("Nieprawidłowy format czasu. Użyj '12' lub '24'.")

test_cases = [
    (15, 38, '24'),
    (8, 3, '24'),
    (0, 5, '24'),
    (11, 15, '12'),
    (0, 7, '12'),
    (7, 30, '12'),
    (12, 46, '12'),
    (13, 10, '12'),
    (19, 2, '12')
]

print("Wyniki testów:")
for hours, minutes, fmt in test_cases:
    result = time_string(hours, minutes, fmt)
    print(f"time_string({hours:2d}, {minutes:2d}, '{fmt}') -> '{result}'")