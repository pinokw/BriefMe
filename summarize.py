import sys, os
fileDir = os.path.dirname(os.path.realpath('__file__'))

doc_list=[]
doc_folder = os.path.join(fileDir, 'docs')
for file in os.listdir(doc_folder):
    if file.endswith(".docx"):
            doc_list.append(os.path.join(doc_folder, file))
print (doc_folder)