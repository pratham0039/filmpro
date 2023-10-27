# views.py
from django.views.generic import ListView, DetailView, UpdateView
from .models import Character, Scene, UploadedPDF,SceneDurationRemark
from django.urls import reverse 
import fitz  # PyMuPDF
import re
import pandas as pd
import subprocess
import os

from django.conf import settings

from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .forms import SceneDurationRemarkForm  # Import your custom form




class CharacterListView(ListView):
    model = Character
    template_name = 'listch.html'
    context_object_name = 'characters'

class SceneListView(DetailView):
    model = Character
    template_name = 'each_actor.html'
    context_object_name = 'character'

def scene_list(request):
    scenes = Scene.objects.all()
    return render(request, 'allscene.html', {'scenes': scenes})


def save_description(request, pk):
    # Retrieve the Scene object based on the provided pk
    scene = get_object_or_404(Scene, pk=pk)

    if request.method == "POST":
        desc = request.POST.get('desc')
        scene.description = desc
        scene.save()
        return redirect(f'/scenes/{pk}')
    
def save_hm(request, pk):
    # Retrieve the Scene object based on the provided pk
    scene = get_object_or_404(Scene, pk=pk)

    if request.method == "POST":
        hm = request.POST.get('hm')
        scene.hair_makeup = hm
        scene.save()
        return redirect(f'/scenes/{pk}')
    
def save_kp(request, pk):
    # Retrieve the Scene object based on the provided pk
    scene = get_object_or_404(Scene, pk=pk)

    if request.method == "POST":
        kp = request.POST.get('kp')
        scene.key_props= kp
        scene.save()
        return redirect(f'/scenes/{pk}')

def save_pro(request, pk):
    # Retrieve the Scene object based on the provided pk
    scene = get_object_or_404(Scene, pk=pk)

    if request.method == "POST":
        pro = request.POST.get('pro')
        scene.production = pro
        scene.save()
        return redirect(f'/scenes/{pk}')
    
def save_pr(request, pk):
    # Retrieve the Scene object based on the provided pk
    scene = get_object_or_404(Scene, pk=pk)

    if request.method == "POST":
        pr = request.POST.get('pr')
        scene.props = pr
        scene.save()
        return redirect(f'/scenes/{pk}')
    
def save_sd(request, pk):
    scene = get_object_or_404(Scene, pk=pk)

    if request.method == "POST":
        sd = request.POST.get('sd')
        scene.set_dressing= sd
        scene.save()
        return redirect(f'/scenes/{pk}')
    
def save_ex(request, pk):
    scene = get_object_or_404(Scene, pk=pk)

    if request.method == "POST":
        ex = request.POST.get('ex')
        scene.extras = ex
        scene.save()
        return redirect(f'/scenes/{pk}')

def save_pv(request, pk):
    scene = get_object_or_404(Scene, pk=pk)

    if request.method == "POST":
        pv = request.POST.get('pv')
        scene.picture_vechiles = pv
        scene.save()
        return redirect(f'/scenes/{pk}')
    
def save_prod(request, pk):
    scene = get_object_or_404(Scene, pk=pk)

    if request.method == "POST":
        prod = request.POST.get('prod')
        scene.production = prod
        scene.save()
        return redirect(f'/scenes/{pk}')
    
def save_sp(request, pk):
    scene = get_object_or_404(Scene, pk=pk)

    if request.method == "POST":
        sp = request.POST.get('sp')
        scene.special_professionals = sp
        scene.save()
        return redirect(f'/scenes/{pk}')

def save_sfx(request, pk):
    scene = get_object_or_404(Scene, pk=pk)

    if request.method == "POST":
        sfx = request.POST.get('sfx')
        scene.sfx = sfx
        scene.save()
        return redirect(f'/scenes/{pk}')

def save_vfx(request, pk):
    scene = get_object_or_404(Scene, pk=pk)

    if request.method == "POST":
        vfx = request.POST.get('vfx')
        scene.vfx = vfx
        scene.save()
        return redirect(f'/scenes/{pk}')
    
def save_seq(request, pk):
    scene = get_object_or_404(Scene, pk=pk)

    if request.method == "POST":
        seq = request.POST.get('seq')
        scene.special_equipments = seq
        scene.save()
        return redirect(f'/scenes/{pk}')

def save_notes(request, pk):
    scene = get_object_or_404(Scene, pk=pk)

    if request.method == "POST":
        notes = request.POST.get('notes')
        scene.notes = notes
        scene.save()
        return redirect(f'/scenes/{pk}')
    
def save_story_notes(request, pk):
    scene = get_object_or_404(Scene, pk=pk)

    if request.method == "POST":
        story = request.FILES.get('story')
        scene.story = story
        scene.save()
        return redirect(f'/scenes/{pk}')







def save_costume_notes(request, pk):
    # Retrieve the Scene object based on the provided pk
    scene = get_object_or_404(Scene, pk=pk)

    if request.method == "POST":
        cn = request.POST.get('costume-notes')
        scene.cn = cn
        scene.save()
        return redirect(f'/scenes/{pk}')
    
def CharacterDetailView(request, pk):
    # Retrieve the Scene object based on the provided pk
    scene = get_object_or_404(Scene, pk=pk)
    
    # Retrieve the list of duration and remark objects for the scene
    duration_remarks = SceneDurationRemark.objects.filter(scene_number=scene.scene_number)
    
    return render(request, 'scene_details.html', {'scene': scene, 'duration_remark': duration_remarks})

def loginpage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(123)

        if email == 'pratham' and password == '0039':
            # Redirect to a different URL
            return redirect('/characters/')  # Replace 'different_url_name' with the actual URL name
        

    return render(request, 'signin.html')

def homepage(request):

    return redirect('/loginpage/')


   

def delete_all_entries(request):
    if request.method == 'POST':
        Scene.objects.all().delete()
        Character.objects.all().delete()
        UploadedPDF.objects.all().delete()
        SceneDurationRemark.objects.all().delete()
        # Delete files in the "pdf" folder within the media directory
        media_root = settings.MEDIA_ROOT
        pdf_folder_path = os.path.join(media_root, 'pdfs')
        pdf_folder_path2 = os.path.join(media_root, 'scene_images')
        scan_folder_path = 'pdfs'

        # Ensure the folder exists before attempting to delete its contents
        if os.path.exists(pdf_folder_path):
            for filename in os.listdir(pdf_folder_path):
                file_path = os.path.join(pdf_folder_path, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
        if os.path.exists(pdf_folder_path2):
            for filename2 in os.listdir(pdf_folder_path2):
                file_path2 = os.path.join(pdf_folder_path2, filename2)
                if os.path.isfile(file_path2):
                    os.remove(file_path2)
        if os.path.exists(scan_folder_path) and os.path.isdir(scan_folder_path):
            for filename in os.listdir(scan_folder_path):
                file_path = os.path.join(scan_folder_path, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
        

        # Redirect to a success page or wherever you'd like
        return redirect('/upload/')
    return render(request, 'character_detail.html')


def edit_character(request, pk):
    scene = Scene.objects.get(pk=pk)
    if request.method == "POST":
        desc = request.POST.get('character_detail')
        scene.description = desc
        scene.save()
        return redirect(f'/scenes/{pk}')
    





def upload_pdf(request):
    if Scene.objects.count() != 0:
        return redirect('/characters')


    if request.method == 'POST':
        # Assuming you have a form field named 'pdf' for the PDF file upload
        pdf_file = request.FILES.get('pdf')
        if pdf_file:
            # Save the uploaded PDF to the database
            uploaded_pdf = UploadedPDF(pdf_file=pdf_file)
            uploaded_pdf.save()

            # Run Python code on the PDF (You need to define this function)
            process_pdf(uploaded_pdf.pdf_file.path)
            subprocess.call(['python', 'manage.py', 'import_excel'])

            # Run the code that takes 5 seconds
            # ...

            return redirect(f'/characters')

    return render(request, 'upload.html')


def remove_common_keys(dict1, dict2):
    for key in list(dict2.keys()):
        if key in dict1:
            del dict2[key]

def has_lowercase_word(line):
    words = line.split()  # Split the line into words
    for word in words:
        if any(char.islower() for char in word):
            return True
        if word=='-':
            return True
    return False
def extract_scenes_from_text(text):
    # Define the regular expression pattern to match scene headings
    scene_pattern = r'(?:EXT\.|INT\.|I/E\.|TRANSITION\:|\\CUT TO\\:|INT/EXT\.)\s*.*?(?=EXT\.|INT\.|I/E\.|TRANSITION\:|\\CUT TO\\:|INT/EXT\.|$)'
    # Use regex to find all scenes based on the pattern
    scenes = re.findall(scene_pattern, text, re.DOTALL | re.IGNORECASE)

    return scenes

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text("text")
    doc.close()
    return text

def find_words_with_all_caps_and_no_symbols(line):
    words = line.split()
    capital_words = []

    for word in words:
        # Use a regular expression to check if the word consists of capital letters only and has no symbols
        if re.match(r'^[A-Z]*$', word) and not re.search(r'[!@#$%^&*(),.?":{}|<>]', word):
            capital_words.append(word)

    return capital_words
      
   
def process_pdf(pdf_path):
    file_name1 = 'trial 1.csv'
    folder_path1 = 'static'
    file_path1 = os.path.join(folder_path1, file_name1)
    df = pd.read_csv(file_path1)
    df.drop(df.index, inplace=True)

   
    
    word_freq2 = {}
    pdf_path = pdf_path  # Replace with the actual path to your PDF file
    extracted_text = extract_text_from_pdf(pdf_path)

    lines = extracted_text.split('\n')
    word_freq = {}
    scenes = extract_scenes_from_text(extracted_text)
    for line in lines:
        if has_lowercase_word(line):
            continue
        else:
            capital = find_words_with_all_caps_and_no_symbols(line)
            character = ""
            for c in capital:
              character = character + c

              if character != " " or character != "":
                if character in word_freq:
                  word_freq[character] += 1
                else:
                  word_freq[character] = 1
    
    for idx, scene in enumerate(scenes, start=1):
        # Extract the description part of the scene

        scene_without_spaces = "".join(scene.split())

        # Search for character names in the scene description


        scene_description = scene.split("\n")[0]
        scene_script = None
        try:
          sceneno = scene.split("\n")[1]

        except:
          continue
        lines = scene_description.split('\n')
        for line in lines:
            if has_lowercase_word(line):
              continue
            else:
              capital = find_words_with_all_caps_and_no_symbols(line)
              character = ""
              for c in capital:
                character = character + c

            if character != " " or character != "":
              if character in word_freq2:
                word_freq2[character] += 1
              else:
                word_freq2[character] = 1
    remove_common_keys(word_freq2, word_freq)
   

    excluded_words = ['PLAY', 'CUT', 'FORADTEAM', 'FOR','FORAD']
    filtered_word_counts = {word: count for word, count in word_freq.items() if count >= 15 and word not in excluded_words}
    
    keys_to_remove = []
    for key2 in filtered_word_counts.keys():
        for key1 in word_freq2.keys():
            if key2 in key1:
                keys_to_remove.append(key2)
   
    for key in set(keys_to_remove):
        filtered_word_counts.pop(key)
   



    for idx, scene in enumerate(scenes, start=1):
    # Extract the description part of the scene
        
        scene_without_spaces = "".join(scene.split())
        charactersss = []
        scene_description = scene.split("\n")[0]
        try:
          sceneno = scene.split("\n")[1]

        except:
          continue

        for word, frequency in filtered_word_counts.items():
        # Convert both the word and paragraph to lowercase for a case-insensitive search
            word = word.lower()
            scene_without_spaces_lower = scene_without_spaces.lower()


        # Count the occurrences of the word


            if word in scene_without_spaces_lower:
              charactersss.append(word)
        # Search for character names in the scene description







        # Extract time of day, location, and place from the summary
        time_of_day_list = []
        location_list = []
        place_list = []
        pattern = r"(EXT|INT|I/E|INT/EXT)\s*\.\s*(.*?)\s*-\s*(\w+(?:\s+\w+)*)"
        match = re.match(pattern, scene_description)
        if match:
            location = match.group(1)
            place = match.group(2)
           
            time_of_day = match.group(3)
            time_of_day_list.append(time_of_day)
            location_list.append(location)
            place_list.append(place)

       
        for time_of_day, location, place in zip(time_of_day_list, location_list, place_list):
            new_row = {'scene_number': sceneno, 'int_ext': location, 'timeofday': time_of_day, 'location':place, 'description': scene, 'cast_id' : charactersss, 'costume_notes' :charactersss, 'hair_makeup': charactersss }
            df = df._append(new_row, ignore_index=True)
            #print(f"Scene {sceneno}:\nTime of Day: {time_of_day}\nLocation: {location}\nPlace: {place}\n {scene_script}\n character = {charactersss}")


    #for word, frequency in word_freq2.items():
       #print(f"{word}: {frequency}")

    
    file_name = 'trial 1.csv'
    folder_path = 'static'
    file_path = os.path.join(folder_path, file_name)
    df.to_csv(file_path, index=False)







def add_duration_remark(request, pk):
    scene = Scene.objects.get(pk=pk)

    if request.method == "POST":
        form = SceneDurationRemarkForm(request.POST)

        if form.is_valid():
            duration = form.cleaned_data['duration']
            remark = form.cleaned_data['remark']
            lenscs = form.cleaned_data['lenscs']
            notescs = form.cleaned_data['notescs']
            shotno = form.cleaned_data['shotno']
            
            # Create a new SceneDurationRemark object
            SceneDurationRemark.objects.create(scene_number=scene.scene_number, duration=duration, remark=remark, lenscs = lenscs, notescs = notescs, shotno = shotno)

            # Get the list of duration_remarks for the scene
            duration_remarks = SceneDurationRemark.objects.filter(scene_number=scene.scene_number)

            # Redirect back to the character detail page with updated data
            return redirect(f'/scenes/{pk}')
    


    
