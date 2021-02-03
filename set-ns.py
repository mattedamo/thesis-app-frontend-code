import yaml, os, sys


def main():
    github_ref = os.getenv("GITHUB_REF")
    ref_list = github_ref.split("/")
    if "master" in github_ref:
        branch = ref_list[-1]
        ns = "prod"
    elif "releases" or "features" in github_ref:
        ns = ref_list[-2]+"/"+ref_list[-1]
    else:
        sys.exit("Not valid branch name")

    with open("./input.yaml") as file:
        input = yaml.load(file, Loader=yaml.FullLoader)
    if "ns" in input.keys():
        if ns != input["ns"]:
            sys.exit("You have to edit input.yaml before expect that it can be applied on kubernetes!")
    else:
        input["ns"] = ns
    with open("./input.yaml", "w") as file:
                yaml.dump(input, file)

if __name__ == '__main__':
    main()
