Position = {'Manager': ['Director',
                        'Deputy Director'],
            'Teacher': ['Specialist',
                        'Methodist',
                        'Senior Lecturer'],
            'Staff': ['Cleaner',
                      'Porter',
                      'Watchman'],
            'dict': {'asd': 1, 'c': 2}}
count1 = len(Position)
count2 = len(Position['Manager'])
count3 = len(Position['Staff'])
print(Position, 'len', count1, '\n',
      Position['Manager'], 'len', count2, '\n',
      (Position['Manager']))
print(Position['dict']['c'])
