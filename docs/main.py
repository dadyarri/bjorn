def define_env(env):

    @env.macro
    def version():
        with open("../VERSION.txt", "r") as f:
            return f.readline()


    @env.macro
    def requirements(file: str):
        result = []
        with open(f"../{file}.txt") as f:
            reqs = f.readlines()
        for req in reqs:
            req = req.split("==")
            result.append({"package": req[0], "version": req[1][:-1]})
        return result