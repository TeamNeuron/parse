# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 16:37:30 2015

@author: Justin_C
"""
import xml.etree.ElementTree as ET
import csv

def parse1(file1):
    csvRecipes = []
    tree = ET.parse(file1)
    root = tree.getroot()
    for child in root:
        recipe = []
        #print child.get('description')  
        recipeName = child.get('description')
        recipe.append(recipeName)
        ingredientList = []
        ingredientQuantity = dict()
        
        for h in child:
            #Recipe Item quantity given, but do not understand what it means
          #  print h.tag, h.attrib
        
            t = h.tag
            if (t == "RecipeItem"):
            #    print h.get('ItemName')
            #    print h.get('itemQuantity')
                ingredientList.append(h.get('ItemName'))
                ingredientQuantity[h.get('ItemName')] = h.get('itemQuantity')
            #print ingredientList
            #print ingredientQuantity
        ingredientString = ""
        for info in ingredientList:
            ingredientString = ingredientString + info + "|"
        
        recipe.append(ingredientString[:-1])
        csvRecipes.append(recipe)
    string1 = ""
    entireList = open(file1, 'r')
    for line in entireList:
        string1 = string1 + str(line)
    memoList = str.split(string1, "<recipe createDate")
    del memoList[0]
    count = 0
    del csvRecipes[0]
    for recipe in memoList:
        #add 13
        #subtract 2
        first = recipe.index('description=')
        first = first + 13
        second = recipe.index('modifyDate=')
        second = second - 2
        
    
        try:
            third = recipe.index("METHOD")
            fourth = recipe.index(']]></memo>')
            csvRecipes[count].append(recipe[third:fourth])
            count += 1
#            for item in csvRecipes:
#                if item[0] == recipe[first:second]:
#                    item.append(recipe[third:fourth])
#                    print (recipe[third:fourth])

    #need to remove everything before the xml data        
        #need to parse the recipe to make it look cleaner
        except:
            csvRecipes[count].append(recipe[third:fourth])
            count += 1
#            for item in csvRecipes:
#                if item[0] == recipe[first:second]:
#                    item.append(recipe[third:fourth])
#                    print (recipe[third:fourth])
                #third is good need to work on the bottom portion
    
        
                
    with open("output.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows(csvRecipes)
    return 1
            
            

def main():
    
    print "hello"
    parse1("ArmedForcesRecipes.xml")
     
    return 1
    
main()