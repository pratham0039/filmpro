from django.core.management.base import BaseCommand
from characters.models import Character, Scene
import pandas as pd
import json
import os


class Command(BaseCommand):
    help = 'Import data from an Excel sheet'

    def handle(self, *args, **options):
        file_name = 'trial 1.csv'
        folder_path = 'static'
        file_path = os.path.join(folder_path, file_name)
        data = pd.read_csv(file_path)
        i = 0
        y = 0

        for index, row in data.iterrows():
            y = y+1
            if y = 30:
                break
            scene_number = row['scene_number']
            location = row['location']
            description = row['description']
            cn = row['costume_notes']
            hair_makeup = row['hair_makeup']
            key_props = row['key_props']
            props = row['props']
            set_dressing = row['set_dressing']
            extras = row['extras']
            picture_vechiles = row['picture_vechiles']
            production = row['production']
            special_professionals= row['special_professionals']
            sfx = row['sfx']
            vfx = row['vfx']
            special_equipments = row['special_equipments']
            notes = row['notes']
            timeofday = row['timeofday']
            int_ext = row['int_ext']
            

            # Handle empty values in description and costume_notes
            description = description if not pd.isna(description) else None
            cn = cn if not pd.isna(cn) else None
            hair_makeup = hair_makeup if not pd.isna(hair_makeup) else None
            key_props = key_props if not pd.isna(key_props) else None
            props = props if not pd.isna(props) else None
            set_dressing = set_dressing if not pd.isna(set_dressing) else None
            extras = extras if not pd.isna(extras) else None
            picture_vechiles = picture_vechiles if not pd.isna(picture_vechiles) else None
            production = production if not pd.isna(production) else None
            special_professionals = special_professionals if not pd.isna(special_professionals) else None
            sfx = sfx if not pd.isna(sfx) else None
            vfx = vfx if not pd.isna(vfx) else None
            special_equipments = special_equipments if not pd.isna(special_equipments) else None
            notes = notes if not pd.isna(notes) else None
            timeofday = timeofday if not pd.isna(timeofday) else None
            int_ext = int_ext if not pd.isna(int_ext) else None

            



            # Handle empty 'cast_id' values
            cast_id_string = row['cast_id']


            image_paths = [
                ('char_images/Icons_1.png'),
                ('char_images/Icons_2.png'),
                ('char_images/Icons_3.png'),
                ('char_images/Icons_4.png'),
                ('char_images/Icons_5.png'),
                ('char_images/Icons_6.png'),
                ('char_images/Icons_7.png'),
                ('char_images/Icons_8.png'),
                ('char_images/Icons_9.png'),
                ('char_images/Icons_10.png'),
                ('char_images/Icons_11.png'),
                ('char_images/Icons_12.png'),
                ('char_images/Icons_13.png'),
                ('char_images/Icons_14.png'),
                ('char_images/Icons_15.png'),
                ('char_images/Icons_16.png'),
                ('char_images/Icons_17.png'),
                ('char_images/Icons_18.png'),
                ('char_images/Icons_19.png'),
                ('char_images/Icons_20.png'),









                # Add more image paths as needed
            ]
           

            # Clean up character names to ensure consistency

            character_names = [name.strip(" '[]") for name in cast_id_string.split(',') if name]

            # Create a list of Character objects based on character_names
            #characters = [Character.objects.get_or_create(name=name)[0] for name in (character_names)]
            #for character in characters:
            #    if character.avatar.name == "static\imgdd.png":
            #        print("yes")
            #        character.avatar.name == image_paths[i]
            #        i = i+1
            #        character.save()
            #    print(f"Character Name: {character.avatar.name}")
            
            characters = []

           
            
            

            for name in character_names:
                
                character = Character.objects.get_or_create(name=name)[0]
                if character.avatar.url == "/media/static/img%07dd.png" and i < len(image_paths):
                    character.avatar.name = image_paths[i]
                    i = i+ 1


                character.save()
                characters.append(character)
                print(i)
                print(f"Character Name: {character.name}")
                print(f"Updated Avatar URL: {character.avatar.url}\n")

            
            



            

            # Create a Scene object
            scene, created = Scene.objects.get_or_create(
                scene_number=scene_number,
                location=location,
                description=description,
                cn = cn,
                hair_makeup = hair_makeup,
                key_props = key_props,
                props = props,
                set_dressing = set_dressing,
                extras = extras,
                picture_vechiles = picture_vechiles,
                production = production,
                special_professionals= special_professionals,
                sfx = sfx,
                vfx = vfx,
                special_equipments = special_equipments,
                notes = notes,
                timeofday = timeofday,
                int_ext = int_ext
                  # Assign the costume_notes here
            )

            # Add the characters to the scene
            scene.characters.add(*characters)
            
