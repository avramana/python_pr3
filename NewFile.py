import loadgen


lg = loadgen.loadgen()

lg.readConfig(type1)

jsonObj = lg.readJson(diff_files)
lg.writeTODB(jsonObj)






