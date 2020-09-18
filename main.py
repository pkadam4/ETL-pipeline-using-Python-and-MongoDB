from transformation import Transformation
import json

class Engine:
    
    def __init__(self, dataSource, dataSet):
        trans_obj = Transformation(dataSource, dataSet)
        
        
if __name__ == '__main__':
    
    etl_data = json.load(open('data_config.json'))
    for dataSource, dataSet in etl_data['data_sources'].items():
        print(dataSource)
        for data in dataSet:
            print(data)
            main_obj = Engine(dataSource, data)