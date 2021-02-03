import yaml, os, sys

def main():
    github_ref = os.environ["GITHUB_REF"]
    if "master" in github_ref:
        branch = "master"
    elif "features" or "releases" in github_ref:
        branch_list = github_ref.split("/")
        branch = branch_list[-2]+"/"+branch_list[-1]
    with open("./input.yaml") as file:
        input = yaml.load(file, Loader=yaml.FullLoader)
    if "branch" not in input.keys():
        sys.exit("You have to insert the correct namespace manually into the input yaml file, "+ 
                        "to confirm that you have made the actual changes in it!")
    if branch != input["branch"]:
        sys.exit("You have to insert the correct namespace manually into the input yaml file, "+ 
                        "to confirm that you have made the actual changes in it!")
       
    if "clusters" not in input.keys():
        sys.exit("You have to specific the cluster name(s) where you want to deploy the application!")
if __name__ == '__main__':
    main()
