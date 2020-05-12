import sys
import json
import zipfile

# Get project.json from .sb3 file
def get_s3_prject_data(sb3):
    data = ''
    try:
        with zipfile.ZipFile(sb3) as zip_data:
            file_data = zip_data.read('project.json')
            data = file_data.decode('utf-8')
    except zipfile.BadZipFile:
        print(traceback.format_exc())

    return data

# Get Values from project.json
def get_values(data):
    values = []
    json_dict = json.loads(data)
    for item in json_dict['targets']:
        for key, value in (item['broadcasts'].items()):
            values.append(value)
    return values

# Check use of values by sprite 
def sprite_used(values, data):
    result = {}
    for val in values:
        result[val]=[]

    json_dict = json.loads(data)
    for item in json_dict['targets']:
        for val in values:
            if (("'"+val+"'") in str(item['blocks'])):
                result[val].append(item['name'])

    return result

if __name__ == '__main__':
    args = sys.argv

    data = get_s3_prject_data(args[1])
    message = get_values(data)
    result = sprite_used(message, data)

    if (len(args) > 2):
        if (args[2] == 'csv'):
            line = ''
            for key, value in result.items():
                line = key + ','
                for v in value:
                    line += v + ','
                # print(line.encode('shift_jis'))
                # line = line.encode('cp932', "ignore")
                # line = line.decode('cp932')
                print(line)
        else:
            print(result)
    else:
        print(result)
