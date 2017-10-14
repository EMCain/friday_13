import random

GHOST = """
 .-.
(o o) boo!
| O \\
 \\   \\
  `~~~'
"""

CAT = """
                         .-.
                          \\ \\
                           \\ \\
                            | |
                            | |
          /\\---/\\   _,---._ | |
         /^   ^  \\,'       `. ;
        ( O   O   )           ;
         `.=o=__,'            \\
           /         _,--.__   \\
          /  _ )   ,'   `-. `-. \\
         / ,' /  ,'        \\ \\ \\ \\
        / /  / ,'          (,_)(,_)
       (,;  (,,)      jrei
"""

BAT = """

         mm
      /^(  )^\\
      \\,(..),/
        V~~V    -AL
"""

ANIMALS = [
    ('ghost', GHOST, 'boo'),
    ('black cat', CAT, 'hissssssss'),
    ('bat', BAT, 'eeeek')
]

def scare(num):
    """pass in an integer (whole number)"""

    name, picture, sound = random.choice(ANIMALS)
    # print picture num times (after converting num to an integer)
    print(int(num)*picture)
    print(sound + '! You were scared by ' + num + ' ' + name + 's!' )

print('Happy Friday the 13th!')
while True:
    num = input('\nPlease type a ~~spooky~~ number between 1 and 13: ')
    scare(num)
