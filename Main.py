import DataImporter as DI
import yaml

if __name__=='__main__':
    #Create a dictionary to save the imported data
    with open("DataSourceInfo.yml", "r") as file:
        path_info = yaml.load(file, Loader=yaml.FullLoader)
        folder_dir = path_info['folder_dir']
        file_format =path_info['file_format'] 
        Fnames = path_info['fname']
        
    with open("CriticalCol.yml", "r") as stream:
        ValidCols = yaml.load(stream, Loader=yaml.FullLoader)

    Data_dict = DI.ReadConvert(folder_dir, Fnames, file_format, convert2='.csv')
    train_dict = DI.ColumnSelect(Data_dict, ValidCols)
    