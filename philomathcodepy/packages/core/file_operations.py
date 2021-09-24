#author: daniel Medina
#date: 9.24.2021
from philomathcodepy.packages.core.random import random 
import xml.etree.ElementTree as ET
import json
class file_operations:
    file_extensions = dict()
    file_extensions['text'] = ".txt"
    file_extensions['json'] = ".json"
    file_extensions['csv'] = ".csv"
    file_extensions['csproj'] = ".csproj"

    def create_json_file(self,dictionaryList,fileName):
        if len(dictionaryList) > 0:
            with open(fileName,'w') as file:
                file.writelines(json.dumps(dictionaryList))
            return True
        else: 
            return False
    def get_packages_used_from_csproj(self,csproj_file_name):
        if len(csproj_file_name) > 0:
            #xml open
            tree = ET.parse(csproj_file_name)
    # get root element
            root = tree.getroot()
    # print(root)
            data_list = []
            searchSettings = dict()

            searchSettings["searchDotNetCliToolReference"] = "DotNetCliToolReference"
            searchSettings["searchPackageReference"] = "PackageReference"
            searchSettings["searchPackageReferenceCount"] = root.findall("ItemGroup/PackageReference")
            searchSettings["searchDotNetCliToolReferenceCount"] = root.findall("ItemGroup/DotNetCliToolReference")

            if searchSettings["searchPackageReferenceCount"].__len__() > 0:
                for r in root.findall("ItemGroup/PackageReference"):
                    package = dict()
                    data_to_save = dict()
                    package = r.attrib
                    data_to_save['Package'] = package['Include']
                    data_to_save['Version'] = package["Version"]
                    # print(data_to_save)
                    data_list.append(data_to_save)
            if searchSettings["searchDotNetCliToolReferenceCount"].__len__() > 0:
                for r in root.findall("ItemGroup/DotNetCliToolReference"):
                    package = dict()
                    data_to_save = dict()
                    package = r.attrib
                    # data_to_save['DotNetCliToolReference'] = package['Include']
                    data_to_save['Package'] = package['Include']
                    data_to_save['Version'] = package["Version"]
                    # print(data_to_save)
                    data_list.append(data_to_save)
            return data_list
        else:
            return list()

    #generate new file name
    def new_filename(self,fileExtension,additionalFileNameText,useRandomGuid):
        if len(additionalFileNameText) > 0:
            #if use random guid is true, use a random guid; if not, return just additional file text and file extension
            if useRandomGuid:
                random_generator = random()
                return additionalFileNameText + random_generator.random_guid_hex() + fileExtension
            else:
                return additionalFileNameText + fileExtension
        else:
            #return random guid with file extension if additional filename text is not supplied
            random_generator = random()
            if len(fileExtension) > 0:
                return random_generator.random_guid() + fileExtension
            else:
                #will return a txt file if a file extension is not provided
                return random_generator.random_guid() + self.file_extensions['text']


            