import numpy as np
import re
import ast
import extcolors

def ujemanjeFun(poster, slika): 
    dist = [0,0,0,0]
    ujemanje = 0

    for i in range(len(poster)):
        sestevekDolzin = 0
        for j in range(len(poster[i][0])):
            sestevekDolzin += abs(poster[i][0][j]-slika[0][i][0][j])
            #print(poster[i][0][j])
            #print(slika[0][i][0][j])
        dist[i] = sestevekDolzin

    dist[0] = dist[0]*0.6
    dist[1] = dist[1]*0.3
    dist[2] = dist[2]*0.1
    dist[3] = dist[3]*0.05
    
    #print(dist)
    ujemanje = dist[0] + dist[1] + dist[2] + dist[3]
    #print(ujemanje)
    return ujemanje

def primerjaj(dataFile_path, pictureFile_path):
    print("DATAFILEPATH: ", dataFile_path)
    print("PICTUREFILEPATH: ", pictureFile_path)
    # Read the content of the data file

    with open(dataFile_path, 'r') as file:
        data = file.read()

    colors = extcolors.extract_from_path(pictureFile_path)
    del colors[0][4:]
    print(colors)
    dataTransformed = ast.literal_eval(data)
    #print(dataTransformed[1][1])

    seznamPosterjev = []
    
    for i in range(len(dataTransformed)):
        dataTransformed[i][1] = dataTransformed[i][1][:4]
        #print("DATATRANSFORMED Z INDEKSOM ", i, "  --   ",dataTransformed[i][1])
        #print("COLORS OF SELECTED IMAGE: ", colors[0])
        seznamPosterjev.append((ujemanjeFun(dataTransformed[i][1], colors),i,dataTransformed[i][0]))

    return seznamPosterjev


posterji = 'barve.txt'
slika = './capturedImages/CapturedImage.png'
print(primerjaj(posterji, slika))
