import os, shutil

dict_extension = {
    'video_extension' : ('.mp4' , '.mkv' , '.MKV' ),
    'image_extension' : ('.png' , '.jpge'),
    'document_extension' : ('.pdf'),
}

folderpath = input('enter folder path : ')

def file_finder(folder_path ,file_extensions):
    files=[]
    for file in os.listdir(folder_path):
        for extension in file_extensions:
            if file.endswith(extension):
                files.append(file)
    return files


#print(file_finder(folderpath, video_extension))

for extension_type , extension_tuple in dict_extension.items():
    folder_name = extension_type.split('_')[0] + 'files'
    folder_path = os.path.join(folderpath , folder_name)
    os.mkdir(folder_path)
    for items in file_finder(folderpath , extension_tuple):
        items_path = os.path.join(folderpath , items)
        item_new_path = os.path.join(folder_path , items)
        shutil.move(items_path , item_new_path)

    #print(extension_type)
    #print(file_finder(folderpath , extension_tuple))







