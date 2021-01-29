import yaml, os

def main():  

    with open("./fakefile.yaml") as file:
            fakefile = yaml.load(file, Loader=yaml.FullLoader)

    with open("./fakevalue.yaml") as file:
            fakevalue = yaml.load(file, Loader=yaml.FullLoader)
    print(fakevalue)

    
    secrets = fakefile.get("secrets")
    
    value = {"value": [{"name": "NOME", "valuefrom": { "secretKeyRef": { "name" : "NAME", "key" : "KEY"}}}]}
    print(value)
    for val in secrets:
        for x,y in val.items():
            print(x)
"""
    if "secretGenerator" in kustomization.keys():
        kustomization.pop("secretGenerator", None)
        literals = []
        for ele in secrets:
            literals.append(ele)
        kustomization["secretGenerator"] = [{"name" : tier+"-"+kind_name , "literals" : literals}]
        with open(kustomization_path) as file:
            yaml.dump(kustomization, file)
        
        valueToReturn = {}
        """
if __name__ == '__main__':
    main()
