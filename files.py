import pdb




filevar = open("files.md")
filecontents = filevar.readlines()
filevar.close()
# pdb.set_trace()
filecontents.insert(5,"        cfg\n")
filecontents.append("Leon has added stuff to the file")

savefile = open("files.md","w")
savefile.writelines(filecontents)
savefile.close()
print(filecontents)