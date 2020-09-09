# Constants
HAPPY = 'happy'
SAD = 'sad'


# Definitions
def feed(hamster):
    if hamster.get('Hungry'):
        hamster.update({'Hungry': False, 'Weight': hamster.get('Weight') + 1})
    else:
        print('La mascota no tiene hambre')


def play(hamster, min_weight=5):
    if hamster.get('Mood') == SAD:
        hamster.update({'Mood': HAPPY})

    if hamster.get('Weight') >= min_weight:
        hamster.update({'Weight': hamster.get('Weight') - 1})

    if hamster.get('Weight') < min_weight:
        hamster.update({'Hungry': True})
        print(f"{hamster.get('Name')} está cansado y hambriento")

def presentation(hamster):
    print(f"Nombre: {hamster.get('Name')}")
    print(f"Edad: {hamster.get('Age')} años")
    print(f"Peso: {hamster.get('Weight')} kg")
    print(f"Hambriento: {hamster.get('Hungry')}")
    print(f"Estado de ánimo: {hamster.get('Mood')}")
    print(f"Photo: {hamster.get('Photo')}")
    print('')


if __name__ == '__main__':

    hamster1 = {'Name': 'Coco',
               'Age': 7,
               'Weight': 8.3,
               'Hungry': True,
               'Mood': SAD,
               'Photo': '<:3)---'
               }

    hamster2 = {'Name': 'Sonic',
                'Age': 10,
                'Weight': 12.4,
                'Hungry': True,
                'Mood': SAD,
                'Photo': '(^-^)'
                }

    for h in [hamster1, hamster2]:
        presentation(h)
        feed(h)
        play(h)
        
    presentation(hamster1)
    presentation(hamster2)

