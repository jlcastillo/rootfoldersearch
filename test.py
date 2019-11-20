import rootfoldersearch

rootPath = rootfoldersearch.findpath("rootfoldersearch/__init__.py", cwd='./rootfoldersearch', depth=2)

print(rootPath)
